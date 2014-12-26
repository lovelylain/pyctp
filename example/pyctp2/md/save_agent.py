#-*- coding:utf-8 -*-

import os
import os.path
import time
import threading
import logging
import random
import gc

from ..common.base import BaseObject,CN_TRADE_SECTION,DAY_FINALIZE_TICK,check_path
from ..common.agent import ManagedAgent
from ..core.dac import MINUTE,MINUTED
#from .minute import Minutes

#TICK_STR = '%(time)d,%(msec)d,%(price)d,%(high)d,%(low)d,%(dvolume)d,%(holding)d,%(bid_price)d,%(bid_volume)d,%(ask_price)d,%(ask_volume)d\n'
#MINUTE_STR = '%(sdate)d,%(stime)d,%(sopen)d,%(shigh)d,%(slow)d,%(sclose)d,%(svolume)d,%(sholding)d\n'
#DAY_STR = '%(sdate)d,%(sopen)d,%(shigh)d,%(slow)d,%(sclose)d,%(svolume)d,%(sholding)d\n'
TICK_FORMAT = '{0.time},{0.msec},{0.price:.%(flen)df},{0.high:.%(flen)df},{0.low:.%(flen)df},{0.dvolume},{0.damount},{0.holding},{0.bid_price:.%(flen)df},{0.bid_volume},{0.ask_price:.%(flen)df},{0.ask_volume}\n'
MINUTE_FORMAT = '{0.sdate},{0.stime},{0.sopen:.%(flen)df},{0.shigh:.%(flen)df},{0.slow:.%(flen)df},{0.sclose:.%(flen)df},{0.svolume},{0.samount},{0.sholding}\n'
DAY_FORMAT = '{0.sdate},{0.sopen:.%(flen)df},{0.shigh:.%(flen)df},{0.slow:.%(flen)df},{0.sclose:.%(flen)df},{0.svolume},{0.samount},{0.sholding}\n'


class SaveAgent(ManagedAgent):
    '''
        由调用者保证对SaveAgent对象的同步处理, 即调用已经被顺序化了
        未采用MacroCommandQueue方式来处理ticks/minutes/day的数据保存, 也是基于这一目的.
            否则, macro_command方式的保存命令,与ticks而来的数据到达处理属于不同线程,会发生竞争状态,从而必须在对象的方法层次处理同步
              就引入了不必要的复杂性和开销

    '''
    def __init__(self,contract_manager,relative_path):
        ManagedAgent.__init__(self,contract_manager)
        self._cbuffer = {}
        self._error_ticks = {}
        self._reset_cbuffer()
        #self.stwaste = 0
        #self.nt = 0
        self.relative_path = relative_path[:-1] if (relative_path[-1] == '/' or relative_path[-1] == os.sep) else relative_path
        if not os.path.isdir(self.relative_path):
            os.makedirs(self.relative_path)
        for contract in self._contract_manager.current_contracts():
            cpath = '%s/%s' % (self.relative_path,contract.name)
            check_path(cpath)
            #if not os.path.isdir(cpath):
            #    os.makedirs(cpath)
        print('SaveAgent initialized')

    def _new_tick(self,ctick):
        #到这里时已经强制同步了,所以不用考虑竞争
        #twaste = time.time() - ctick.create_time
        #self.stwaste += twaste
        #self.nt += 1
        #print(twaste,self.stwaste/self.nt)
        super(SaveAgent, self)._new_tick(ctick)
        cb = self._cbuffer[ctick.instrument]
        ticks = cb.contract.ticks
        minutes = MINUTE(ticks)
        #print('in SaveAgent,ctick=%s',(ctick.time,))
        if minutes.modified:
            #print("before save minutes1",ctick.instrument,minutes[-1].stime,)
            sbefore =  len(ticks)
            self._save_minute1(ctick.instrument,minutes[-1])
            safter = len(ticks)
            print("after save minutes1,contract=%s,time=%s,before_len=%d,after_len=%s" %(ctick.instrument,minutes[-1].stime,sbefore,safter))
            #if len(ticks) > 2000 or random.randint(0,1000) > 900:
            if safter > 100 or random.randint(0,1000) > 900:
                #print("before ticks remove_head 1:",cb.ticks_saved_size)
                try:
                    #self._save_ticks1(ctick.instrument,ticks,cb.ticks_saved_size)
                    self._save_ticks1(ctick.instrument,ticks)
                except Exception as e:
                    print("save_ticks exception:",e)
                #cb.ticks_saved_size = len(ticks)
                ###调试用
                print("ticks remove_all:%s,safter=%d"%(ctick.instrument,safter))
                #ticks.remove_head(cb.ticks_saved_size)
                ticks.remove_all()
                #cb.ticks_saved_size = 0
                gc.collect()
                objgraph.show_most_common_types(limit=20)

    def day_finalize(self):
        super(SaveAgent, self).day_finalize()
        for contract_name,cdata in self._cbuffer.items():
            #完成分钟处理,已经不需要
            #cdata.minutes.day_finalize()
            #完成ticks保存
            #self._save_ticks1(contract_name,cdata.contract.ticks,cdata.ticks_saved_size)
            self._save_ticks1(contract_name,cdata.contract.ticks)
            #cdata.ticks_saved_size = len(cdata.contract.ticks)
            #cdata.ticks.remove_all()   #由controller自行删除
            #完成日分钟保存, 此时, controller已将日结TICK插入
            minutes = MINUTE(cdata.contract.ticks)
            if len(minutes) > 0:
                self._save_minute1(contract_name,minutes[-1])
            days = MINUTED(minutes)
            #完成日保存
            #self._save_day(contract_name,cdata.minutes.get_day())
            if len(days) > 0:
                self._save_day(contract_name,days[-1])
            minutes.remove_part(600)    #保留600条
        self._reset_cbuffer()

    def _save_ticks1(self,contract_name,ticks,saved_size=0):
        '''
            可能会导致部分夜盘ticks保存到上一日,在replay时须注意
        '''
        size_ticks = len(ticks)
        if size_ticks <= saved_size:
            print("!!!!可保存数少于预保存数: 可保存数=%d,预保存数=%d" % (size_ticks,saved_size))
            return
        #tdate = ticks[0].tdate
        tdate = ticks[saved_size].tdate
        if tdate == DAY_FINALIZE_TICK.tdate:
            #print("DAY_FINALIZE_TICK:",len(ticks),saved_size)
            if size_ticks <= saved_size+1:
                return
            else:
                tdate = ticks[saved_size+1].tdate
        b = time.time()
        sformat = TICK_FORMAT % {'flen':self._cbuffer[contract_name].contract.ctype.flen}
        cpath = '%s/%s' % (self.relative_path,contract_name)
        check_path(cpath)
        with open('%s/%s.csv' % (cpath,tdate),'at') as tf:
            for tick in ticks[saved_size:]:
                if tick != DAY_FINALIZE_TICK:
                    #tick.time %= 10000000000    #MMDDhhmmss
                    tf.write(sformat.format(tick))
                    #tf.write('%(time)d,%(msec)d,%(price)d,%(high)d,%(low)d,%(dvolume)d,%(holding)d,%(bid_price)d,%(bid_volume)d,%(ask_price)d,%(ask_volume)d\n' % tick.mydict())
                    #tf.write('%(min1)04d%(sec)02d,%(msec)d,%(price)d,%(high)d,%(low)d,%(dvolume)d,%(holding)d,%(bid_price)d,%(bid_volume)d,%(ask_price)d,%(ask_volume)d\n' % tick.mydict())
        logging.debug('thread=%s,save ticks %s, used:%s' % (threading.current_thread().ident,contract_name,time.time()-b,))

    def _save_minute1(self,contract_name,minute):
        b = time.time()
        sformat = MINUTE_FORMAT % {'flen':self._cbuffer[contract_name].contract.ctype.flen}
        cpath = '%s/%s' % (self.relative_path,contract_name)
        check_path(cpath)
        with open('%s/minutes.csv' % (cpath,),'at') as mf:
            #if minute.svolume > 0:
                #mf.write('%(sdate)d,%(stime)d,%(sopen)d,%(shigh)d,%(slow)d,%(sclose)d,%(svolume)d,%(sholding)d\n' % minute.__dict__)
            if minute.svolume > 0:
                mf.write(sformat.format(minute))    #20141016,不保存svolume=0
                logging.debug('thread=%s,save minute %s, used:%s' % (threading.current_thread().ident,contract_name,time.time()-b,))
            else:
                logging.debug('thread=%s,svolume<=0,not save minute %s' % (threading.current_thread().ident,contract_name))

    def _save_day(self,contract_name,day):
        if day.sdate == 0:
            logging.info('当日数据为空:%s' % contract_name)
            return 
        sformat = DAY_FORMAT % {'flen':self._cbuffer[contract_name].contract.ctype.flen}
        logging.info('保存日数据:%s' % contract_name)
        cpath = '%s/%s' % (self.relative_path,contract_name)
        check_path(cpath)
        with open('%s/days.csv' % (cpath,),'at') as mf:
            mf.write(sformat.format(day))
            #mf.write('%(sdate)d,%(sopen)d,%(shigh)d,%(slow)d,%(sclose)d,%(svolume)d,%(sholding)d\n' % day.__dict__)
        logging.info('保存日数据完毕:%s' % contract_name)

    def _reset_cbuffer(self):
        self._cbuffer = {}
        for contract in self._contract_manager.current_contracts():
            #self._cbuffer[contract.name] = BaseObject(ctype=contract.ctype,ticks=[],minutes=Minutes(contract))
            #self._cbuffer[contract.name] = BaseObject(contract=contract,ticks_saved_size=0)
            self._cbuffer[contract.name] = BaseObject(contract=contract)

import threading
try:
    import queue
except ImportError:
    import Queue as queue

class TSaveAgent(SaveAgent,threading.Thread):
    '''
        自同步方式. 可以与Controller组合
        未使用. 
        目前采用的方式是 Controller ==> handler thread --> SaveAgent的方式
            既TController -> SaveAgent, 线程在Controller的方式
    '''
    def __init__(self,contract_manager,relative_path):
        SaveAgent.__init__(self,contract_manager,relative_path)
        threading.Thread.__init__(self)
        self._queue = queue.Queue()
        self._lock = threading.Lock()
        
    def run(self):
        while self.is_active: #is_active必须设定, 定义在BaseAgent中
            ctick = self._queue.get()
            self._new_tick(ctick)

    def new_tick(self,ctick):
        with self._lock:
            self._queue.put(ctick)



