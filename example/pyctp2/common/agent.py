#-*- coding:utf-8 -*-
'''
    经过测试
    Agent级别的线程化对于python来说没有实际意义
        因为即便将Agent任务细分,比如Save时每一个品种(多个不同期合约)一个Agent
        从而有10-20个Agent线程
        但由于GIL的存在,这些线程的调度反而徒耗时间
    有实际意义的线程化应当是Controller级别,即在Controller中整出一个工作线程,然后对应多个Agent
'''


import threading
try:
    import queue
except ImportError:
    import Queue as queue


class BaseAgent(object):
    """
        外部处理线程
    """
    def __init__(self):
        #self._last_tick = None
        pass

    def new_tick(self,ctick):
        '''
            新数据到来时,由外部调用
        '''
        self._new_tick(ctick)

    def _new_tick(self,ctick):
        '''
            实际处理tick,须子类继承
        '''
        pass

    def day_finalize(self):     #此时,日结tick已由controller插入
        pass

    @property
    def is_active(self):
        return True

class RecordAgent(BaseAgent):   #只记录最后一个tick,用于计算记录成交量
    pass

class ManagedAgent(BaseAgent):
    def __init__(self,contract_manager=None,tday=0):
        BaseAgent.__init__(self)
        self._contract_manager = contract_manager
        #self._tday = tday
        #self._tymd = (tday //10000,tday%10000//100,tday%100)
        self.tday = tday

    @property
    def contract_names(self):
        cs = self._contract_manager.current_contracts(*self._tymd)
        return [c.name for c in cs]

    @property
    def contracts(self):
        return self._contract_manager.current_contracts(*self._tymd)

    @property
    def tday(self):
        return self._tday

    @tday.setter
    def tday(self,v):
        self._tday = v
        self._tymd = (v //10000,v%10000//100,v%100)


class ThreadAgent(threading.Thread):
    """
        工作线程处理的Agent
        未用到
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self._queue = queue.Queue()

    def run(self):
        while self.is_active(): #is_active必须设定
            ctick = self._queue.get()
            self._new_tick(ctick)

    def new_tick(self,ctick):
        self._queue.put(ctick)

    def _new_tick(self,ctick):
        '''
            实际处理tick的函数
        '''
        pass

    def is_active(self):
        return True

