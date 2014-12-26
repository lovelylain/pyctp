# -*- coding:utf-8 -*-


import threading
import time
from ctp.futures import TraderApi, ApiStruct
from ..trader.trade_command_queue import TradeCommandQueue
from ..trader.trade_command import QueryAccountCommand
from ..trader.ctp_wrapper import TraderSpiDelegate

from ..common.base import INTERNAL_PATH

#数据定义中唯一一个enum
class THOST_TERT_MODE:
    RESTART  = 0
    RESUME   = 1
    QUICK    = 2

class Account(object):
    def __init__(self,env,ports_info):
        self._ports_info = ports_info
        ports_info.input_account()
        self._balance = 0
        self._available = 0
        self._margin = 0 #保证金
        self._locked = 0 #保证金锁定/冻结的保证金
        self._pre_locked = 0 #预锁定
        self._lock = threading.Lock()
        self._stamp = 10000  #时间戳,每次lock，update后都递增
        self._env = env
        self.initialize()

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self,v):
        self._available = v

    @property
    def balance(self):
        return self._balance

    @property
    def margin(self):
        return self._margin

    @property
    def stamp(self):
        return self._stamp

    def initialize(self):
        self.spi = TraderSpiDelegate(self._ports_info.broker,self._ports_info.investor,self._ports_info.passwd)
        self.trade_queue = TradeCommandQueue(self._env,self)
        self.spi.queue = self.trade_queue
        #self.trader = TraderApi.CreateTraderApi(self.investor)
        self.api = self.spi
        self.api.Create("%s/%s" % (INTERNAL_PATH,self._ports_info.name))   #避免泄密
        self.api.SubscribePublicTopic(ApiStruct.TERT_QUICK)
        self.api.SubscribePrivateTopic(ApiStruct.TERT_QUICK)
        #会被灌入当日连接前的RtnOrder,可用于确认挂单(同order_ref最后的那一票)
        #self.api.SubscribePublicTopic(ApiStruct.TERT_RESTART)
        #self.api.SubscribePrivateTopic(ApiStruct.TERT_RESTART)
        for port in self._ports_info.ports:
            self.api.RegisterFront(port)
        self._env.register_account(self)
        self.api.Init()
        self.trade_queue.start()
        #self.put_command(QueryAccountCommand(self._stamp))

    def on_login(self):  #重新连接时处理
        self.put_command(QueryAccountCommand(self._stamp))

    def put_command(self,command):
        self.trade_queue.put_command(command)

    def update(self,query_stamp,balance,available,margin,locked):
        """
            通过查询-update 方式来解锁
            但是这里仍然存在微妙的问题. 如果多个lock之后, 有一个查询,则会全部解锁
            不过考虑到本地执行速度,这种情况几乎不会出现
            另,计划外的查询,也会导致解锁, 不过这个可以通过query_stamp来避免. 问题:有必要在交易时段有计划外的查询么? #CHECK: 备机除发单外,其余流程需要与主相同
        """
        if query_stamp < self._stamp:  #发出query之后已经有lock动作，需要重新update
            self.trade_queue.put_command(QueryAccountCommand)
            return False
        with self._lock:
            self._balance = balance
            self._available = available
            self._margin = margin
            self._locked = locked
            self._pre_locked = 0
            self._stamp = query_stamp

    def prelock(self,amount):
        with self._lock:
            self._pre_locked += amount
            self._available -= amount
            self._stamp += 1

    def release_prelock(self,amount):
        '''
            计算失败，回滚时释放已锁定值
        '''
        with self._lock:
            self._pre_locked -= amount
            self._available += amount
            self._stamp += 1

    @property
    def id(self):
        return '%s_%s' % (self._ports_info.broker,self._ports_info.investor)
