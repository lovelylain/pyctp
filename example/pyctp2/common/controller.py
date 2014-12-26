#-*- coding:utf-8 -*-

import threading
import bisect
import random
import logging
import sched
import time
try:
    import queue
except ImportError:
    import Queue as queue

from .base import BaseObject,EMPTY_LIST,DAY_FINALIZE_TICK
from .utils import now2next,TList
from .macro_command_queue import mcq_stub


class SyncLastMap(object):
    '''
        多线程访问的合约最后更新时间
    '''
    def __init__(self):
        self._lock = threading.Lock()
        self._last_map = {}

    def reset(self,contract_names):
        with self._lock:
            self._last_map = dict([(cid,BaseObject(time='',msec='',volume=0)) for cid in contract_names])

    def check(self,cid,dtime,dmsec,dvolume):
        assert cid in self._last_map,'contract %s 不在 订阅的合约列表中,dtime=%s,订阅合约=%s' % (cid,dtime,self._last_map.keys())
        with self._lock:
            dlast = self._last_map[cid]
            if dvolume <= dlast.volume and (dtime < dlast.time or (dtime == dlast.time and dmsec <= dlast.msec)):
                #不能仅靠时间.因为夜盘存在, 而当日夜盘归属下一日,所以晚的时间在前面,白天的time反而在后面发生
                #不仅仅依靠volume,是为了记录volume未变但是买卖盘改变的tick
                return False
            else:
                dlast.volume = dvolume
                dlast.time = dtime
                dlast.msec = dmsec
                return True


class Controller(object):
    '''
        所有事项均在线程内处理
        管理诸多Agent
        并且处理换日
        原则上1个Environ只能有一个Controller, 这样ticks数据在append时就不会出现竞争和出现重复(因为contract实际上只有一份)
            或者通过contracts的垂直切分,多个controller也不会互相竞争

        本类是线程内版本, 可用于backtesting
        子类TController是单独线程的队列版本, 用于实盘.
            两者共享大部分代码
    '''
    def __init__(self,mc_queue=mcq_stub):
        '''
            command_queue: 宏命令队列，用于驱动
            last_map放置在这里的原因是 一个controller可以对应多个listener, 而last_map必须在这些个listener中共享
                    至于为何不把new_tick的所有判断都放在controller中,是考虑到一旦判断为新的tick,其从CTP格式到标准格式的转换完全是平台相关的,不应在这个层面出现
            调用顺序:
                ctl = Controller()
                ...
                ctl.register_agent(..)
                ...
                ctl.add_listener(..)
                ...
                ctl.reset()
                ...
        '''
        self._cur = BaseObject(date=0,time=0,msec=0)
        self._lock = threading.Lock()
        self._contract2agents = {}
        self._contracts = {}
        self._last_map = SyncLastMap()
        self._agents = set()
        self._listeners = set()
        self._mc_queue = mc_queue
        self._lock = threading.Lock()

        #self.time_trigger = TimeTrigger(save_point,self.day_finalize,save_interval)

    @property
    def agents(self):
        return self._agents

    @property
    def contracts(self):
        return self._contracts.values()

    def add_listener(self,listener):
        ''' 非常重要,必须在初始化后马上设定
            在日结时须更新其监听的合约
        '''
        self._listeners.add(listener)

    def register_agent(self,agent):
        '''
            仅用于动态新增Agent
        '''
        self._agents.add(agent)
        self._register_contract(agent)

    def reset(self):
        self._reset_contracts()
        self._update_listened_contracts()
        self._last_map.reset(self._contract2agents.keys())

    def check_last(self,cid,dtime,dmesc,dvolume):
        '''
            被listener调用
        '''
        return self._last_map.check(cid,dtime,dmesc,dvolume)

    def new_tick(self,ctick):
        '''
            自行同步
            对于线程化后队列方式,则不需要这样同步. 队列本身就是同步装置
        '''
        #print("in controller new_tick")
        with self._lock:
            self._new_tick(ctick)

    def _new_tick(self,ctick): #
        #在ticks中添加tick.
        # 对于本类,因为是线程内操作,故也是同步的. 虽然有竞争风险(因为使用了多个接收线程, 但通过SyncLastMap能解决绝大部分问题)
        # 对于TController,因为在另一线程中通过队列操作,故已经同步了,不需要再加锁
        self._contracts[ctick.instrument].ticks.append(ctick) #必须在这里添加, 对TController此处是已同步点
        #print(ctick.instrument,ctick.time)
        #驱动macroCommand队列
        if self._check_next(ctick):
            #print("before trigger mc_queue")
            self._mc_queue.trigger(ctick.time)
            #print("after trigger mc_queue")
        ##驱动数据处理
        #print('TC:',time.time()-ctick.create_time)
        for agent in self._contract2agents.get(ctick.instrument,EMPTY_LIST):
            try:
                #print("new_tick arrived:",ctick.instrument,ctick.time,agent.name)
                agent.new_tick(ctick)
                #print("new_tick handled:",ctick.instrument,ctick.time,agent.name)
            except Exception as einst:
                logging.error('agent new_tick handler exception:%s' % (str(einst),))
                logging.exception('agent new_tick handler exception')       #打印堆栈
        #print('in controller,%d' % (ctick.time,))
    
    def day_finalize(self):
        '''  需要被外部调用以完成日结. 不自己搞定是为了模拟一致性
        '''
        self._day_finalize()

    def _day_finalize(self):

        '''
            同步后调用
        '''
        logging.info('day_finalizing.....')
        for contract in self._contracts.values():
            contract.ticks.append(DAY_FINALIZE_TICK)
            #print("dayfinalize1:",contract.name,len(contract.ticks))
        self._cur.date = self._cur.time = self._cur.msec = -1
        for agent in self._agents:
            agent.day_finalize()
        self._agents = [agent for agent in self._agents if agent.is_active] #不再监听不活跃的agent
        for contract in self._contracts.values():
            #print("dayfinalize2:",contract.name,len(contract.ticks))
            contract.ticks.remove_all()
            #print("dayfinalize3:",contract.name,len(contract.ticks))
        self.reset()
        logging.info('day_finalized')

    def _check_next2(self,ctick):
        '''
            @deprecated, 不需要lock
            判断当前tick是否已经切换到下一tick
            因为存在多合约,所以可能多次进入的是同一tick的不同合约的数据
        '''
        with self._lock:
            if ctick.time > self._cur.time or (ctick.time == self._cur.time and ctick.msec > self._cur.msec):
                self._cur.date = ctick.date
                self._cur.time = ctick.time
                self._cur.msec = ctick.msec
                return True
            return False

    def _check_next(self,ctick):
        '''
            判断当前tick是否已经切换到下一tick
            因为存在多合约,所以可能多次进入的是同一tick的不同合约的数据
        '''
        if ctick.time > self._cur.time or (ctick.time == self._cur.time and ctick.msec > self._cur.msec):
            self._cur.date = ctick.date
            self._cur.time = ctick.time
            self._cur.msec = ctick.msec
            return True
        return False


    def _update_listened_contracts(self):
        contracts = self._contract2agents.keys()
        #print(contracts)
        logging.info('listened contracts:%s',str(contracts))
        for listener in self._listeners:
            listener.update_instruments(contracts)

    def _reset_contracts(self):
        self._contract2agents.clear()
        #self._contracts.clear()
        for agent in self._agents:
            self._register_contract(agent)

    def _register_contract(self,agent):
        c2as = self._contract2agents
        #print(agent.contracts)
        for contract in agent.contracts:
            #print("contract name:",contract.name,agent.name)
            c2as.setdefault(contract.name,[]).append(agent)
            if contract not in self._contracts:
                self._contracts[contract.name] = contract
        #print(c2as)



class TController(Controller,threading.Thread):
    """
        单独线程处理版本, 通过队列之后, 线程顺序处理到来的tick. 即内部的tick处理是线程安全的
    """
    def __init__(self,mc_queue=mcq_stub):
        Controller.__init__(self,mc_queue)
        threading.Thread.__init__(self)
        self._queue = queue.Queue()
        #self.stwaste = 0
        #self.nt = 0

    def new_tick(self,ctick):
        self._queue.put(ctick)

    def day_finalize(self):
        super(TController, self).day_finalize()

    def _new_tick(self,ctick):
        #twaste = time.time() - ctick.create_time
        #self.stwaste += twaste
        #self.nt += 1
        #print(twaste,self.stwaste/self.nt,self.queue.qsize())
        #print(ctick.instrument,ctick.time)
        Controller._new_tick(self,ctick)

    def run(self):
        while 1:
            ctick = self._queue.get()
            if ctick.price > 0:
                self._new_tick(ctick)
            else:
                self._day_finalize()

"""
class NullCommandManager(object):
    def next_round(self):
        pass


class ResumableController(Controller):
    '''
        用于交易agent,需要断点恢复
        TODO
    '''
    def __init__(self,actor=NullCommandManager()):
        Controller.__init__(self,actor)
"""


class Scheduler(object):
    '''
        仅被SaveAgent使用
        定时驱动
        使用sched实现
        目前已经转为使用MacroCommandQueue
    '''
    def __init__(self,tpoint,target,tround=24*60*60):
        '''
            tpoint为HHMMSS,其中hour为24小时计时
            tround为第一次触发后,后续触发的时间间隔
        '''
        self._tpoint = tpoint
        self._target = target
        self._tround = tround
        self._scheduler = sched.scheduler(time.time,time.sleep)
        self._thread = threading.Thread(target=self._start)
        self._thread.daemon = True
        self._thread.start()

    def _start(self):
        print('scheduler starting...')
        seconds = now2next(self._tpoint//10000,self._tpoint%10000//100,self._tpoint%100)
        logging.info('start time trigger %s' % (seconds,))
        print(seconds)
        self._scheduler.enter(seconds,1,self._func,())
        self._scheduler.run()

    def _func(self):
        logging.info('in time trigger....')
        self._scheduler.enter(self._tround,1,self._func,())
        print('next trigger:',self._tround)
        self._target()
        logging.info('time trigger end,next trig:%s' % (self._tround,))



#CS = BaseObject(REDAY=100,EXECUTING=101,SUCCESS=200,CS_CANCELD=300,FAILED=400)


