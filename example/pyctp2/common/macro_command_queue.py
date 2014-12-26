# -*- coding:utf-8 -*-

"""
    使用heapq实现
    Trade中使用两个macro_command_queue:
        1. tick_mcq: 
            tick驱动的mcq, 为短队列
            同时也被 s100驱动
        2. s100队列
            每100s驱动一次, 主要用于保存数据(saveagent) 和 主动同步持仓金额状态(tradeagent)
"""

import time
import threading
import logging

from heapq import *


class MacroCommand(object):
    """
        绝对触发时间
    """
    def __init__(self,target,params,trigger_time):
        self._target = target
        self._params = params
        self._trigger_time = trigger_time

    @property
    def trigger_time(self):
        return self._trigger_time

    def check2exec(self,cur_time):
        #print("trigger_time=%s,cur_time=%s" % (self.trigger_time,cur_time))
        if self._trigger_time <= cur_time:
            if self._params:
                self._target(self._params)
            else:
                self._target()
            return True
        else:
            return False

    def __lt__(self, other):
        return self.trigger_time < other.trigger_time

    def __gt__(self, other):    #也可不用
        return self.trigger_time > other.trigger_time

    def __eq__(self, other):
        return self.trigger_time == other.trigger_time


TERMINAL_COMMAND = MacroCommand(None,None,999999999999)    #终止符,末位时间

class DeferCommand(MacroCommand):
    """
        相对触发时间
    """
    def __init__(self,command,delta):
        MacroCommand.__init__(self,command, None, time.time()+delta)
    

class DeferTradeCommand(DeferCommand):
    def __init__(self,trade_queue,trade_command,delta):
        DeferCommand.__init__(self,self._put2trade_queue,delta)
        self._trade_queue = trade_queue
        self._trade_command = trade_command

    def _put2trade_queue(self):
        self._trade_queue.put_command(self._trade_command)

    def __lt__(self,other):     #同优先级比较
        #return self._trade_command.priority < other._trade_command.priority
        #print("in lt")
        if super(DeferTradeCommand, self).__lt__(other):   #如果时间不同则不需要再判断
            return True
        elif super(DeferTradeCommand, self).__eq__(other) and isinstance(other,DeferTradeCommand): #只有当时间相同且均为DerferTradeCommand时,才需要继续比较优先级
            return self._trade_command.priority < other._trade_command.priority
        else:
            return False


    def __gt__(self,other): #也可不用
        #return self._trade_command.priority > other._trade_command.priority
        #print("in gt")
        if super(DeferTradeCommand, self).__gt__(other):   #如果时间不同则不需要再判断
            return True
        elif super(DeferTradeCommand, self).__eq__(other) and isinstance(other,DeferTradeCommand): #只有当时间相同且均为DerferTradeCommand时,才需要继续比较优先级
            return self._trade_command.priority > other._trade_command.priority
        else:
            return False


class BaseMacroCommandQueue(object):
    '''
        仅靠新tick到来驱动的命令队列
        是线程内处理
        为避免混乱,必须确保裸的OpenCommand不会被放进队列. 而必须在wrapper中,通过判断Agent状态来确认后续的命令是否要执行
    '''
    def __init__(self,time_func=time.time):
        self._time_func = time_func
        self._cqueue = []
        self._lock = threading.Lock()    #用于插入和弹出的锁定

    def put_command(self,command):
        self._lock.acquire()
        #print(len(self._cqueue),type(command))
        #heappush(self._cqueue,(command.trigger_time,command))   #这样的比较速度最快
        heappush(self._cqueue,command)
        self._lock.release()

    def trigger(self,xtime=0):
        """
            xtime: 预留参数
        """
        self._exec()

    def _exec(self):
        """
            正常运行返回True
            发现终结命令时,返回False
        """
        is_terminated = False
        cur_time = self._time_func()
        #print("cur_time=",cur_time)
        #print("in macroCommandQueue:",cur_time)
        if len(self._cqueue) == 0:   #短路操作
            return True
        try:
            while 1:
                self._lock.acquire()
                #cur = heappop(self._cqueue)[1]
                cur = heappop(self._cqueue)
                self._lock.release()
                if id(cur) == id(TERMINAL_COMMAND):
                    is_terminated = True
                    break
                is_done = cur.check2exec(cur_time)
                if  not is_done:    #最小值也未到执行时间
                    self.put_command(cur)
                    break
        except IndexError as einst:
            pass    #取到空
        finally:
            if self._lock.locked():
                self._lock.release()
        return not is_terminated

    def start(self):    #统一接口
        pass


class PassiveMacroCommandQueue(BaseMacroCommandQueue):
    """
        只有外部驱动的线程内命令队列
        用不到
    """
    def __init__(self,interval=0):
        """
            interval: 和MacroCommandQueue/SecMacroCommandQueue统一接口,实际上没用
        """
        BaseMacroCommandQueue.__init__(self,time_func=self._time)
        self._interval = interval
        self._cur_time = 9999999999

    def _time(self):
        return self._cur_time

    def trigger(self,xtime=0):
        self._cur_time = time.time() if xtime == 0 else xtime
        self._exec()


class MacroCommandQueue(threading.Thread,BaseMacroCommandQueue):
    '''
        #deprecated 由 SecMacroCommandQueue与TickMacroCommandQueue代替其功能
        独立线程的命令处理队列
            每次tick到来或interval到达时,判断是否需要执行
        可以创建多条队列
        分别对应于秒频和分频
        分频队列由单独线程去驱动
    '''
    def __init__(self,interval=1):
        threading.Thread.__init__(self)
        BaseMacroCommandQueue.__init__(self,time_func=time.time)
        self._interval = interval
        self._listen_event = threading.Event()
        self._last_tick_time = 0
        #self.cqueue = []
        #self.lock = threading.Lock()    #用于插入和弹出的锁定

    #def put_command(self,command):
    #    self.lock.acquire()
    #    heappush(self.cqueue,(command.trigger_time,command))   #这样的比较速度最快
    #    self.lock.release()

    def start(self):
        threading.Thread.start(self)

    def trigger(self,xtime=0):
        """
            last_tick_time = xtime
        """
        if xtime > 0:
            self._last_tick_time = xtime
        self._listen_event.set()
        self._listen_event.clear()

    def run(self):
        while 1:
            #print("in run: waiting event,interval=%s" % (self.interval,))
            rev = self._listen_event.wait(self._interval)
            #print("in run: event triggered,interval=%s" % (self.interval,))
            rev = self._exec()
            if not rev: #终止
                #print("MacroCommandQueue接收到Terminal信号退出")
                logging.info("MacroCommandQueue接收到Terminal信号结束无限循环")
                break


class SecMacroCommandQueue(threading.Thread,BaseMacroCommandQueue): #TODO:TEST
    '''
        秒驱动的命令队列
    '''
    def __init__(self,interval=1):
        threading.Thread.__init__(self)
        BaseMacroCommandQueue.__init__(self,time_func=time.time)
        self._interval = interval
        self._listen_event = threading.Event()

    def start(self):
        threading.Thread.start(self)

    def trigger(self,xtime=0):
        #不再由外部驱动
        pass

    def run(self):
        while 1:
            #print("in run: waiting event,interval=%s" % (self.interval,))
            rev = self._listen_event.wait(self._interval)
            assert rev == False
            #print("in run: event triggered,interval=%s" % (self.interval,))
            rev = self._exec()
            if not rev: #终止
                #print("SecMacroCommandQueue接收到Terminal信号结束无限循环")
                logging.info("SecMacroCommandQueue接收到Terminal信号结束无限循环")
                break


class TickMacroCommandQueue(threading.Thread,BaseMacroCommandQueue):
    '''
        interval: 和MacroCommandQueue/SecMacroCommandQueue统一接口,实际上没用
    '''
    def __init__(self,interval=0):
        """
            interval只为保持一致接口,无用
        """
        threading.Thread.__init__(self)
        BaseMacroCommandQueue.__init__(self,time_func=self.get_last_tick_time)
        self._last_tick_time = 0
        self._listen_event = threading.Event()

    def get_last_tick_time(self):
        return self._last_tick_time

    def start(self):
        threading.Thread.start(self)

    def trigger(self,xtime=0):
        assert xtime > 0
        self._last_tick_time = xtime
        self._listen_event.set()
        self._listen_event.clear()

    def run(self):
        while 1:
            #print("in run: waiting event,interval=%s" % (self.interval,))
            rev = self._listen_event.wait()  #必须由外部驱动
            assert rev == True
            #print("in run: event triggered,interval=%s" % (self.interval,))
            rev2 = self._exec()
            if not rev2: #终止
                #print("TickMacroCommandQueue接收到Terminal信号结束无限循环")
                logging.info("TickMacroCommandQueue接收到Terminal信号结束无限循环")
                break


class MCQ_Stub(object):
    '''
        Mock类
    '''
    def put_command(self,command):
        pass

    def trigger(self,xtime=0):
        pass

mcq_stub = MCQ_Stub()
