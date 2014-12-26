# *-* coding:utf-8 -*-

import threading

from ..common.base import INTERNAL_PATH
from ..trader.account import Account
from ..trader.ctp_wrapper import TraderSpiDelegate
from .trader_api_stub import TraderApiStub
from ..trader.trade_command_queue import TradeCommandQueueStub,BaseTradeCommandQueue
from ..trader.trade_command import QueryAccountCommand

class TraderSpiStub(TraderSpiDelegate, TraderApiStub):
    pass

class AccountStub(Account):
    """
        使用真实的SPI,以及Stub的API
        尽可能缩小与实际执行的差异
    """
    def __init__(self,env,ports_info,id,available = 1000000,TCQ=TradeCommandQueueStub):
        self._id = id
        self._ports_info = ports_info
        self._balance = available
        self._available = available
        self._margin = 0 #保证金
        self._locked = 0 #保证金锁定/冻结的保证金
        self._pre_locked = 0 #预锁定
        self._lock = threading.Lock()    #其实可以用一个啥也不做处理with的上下文对象来搞定, 必要时可优化
        self._stamp = 10000  #时间戳,每次lock，update后都递增
        self._env = env
        self.initialize(TCQ)

    def initialize(self,TCQ):
        self._env.register_account(self)
        self.spi = TraderSpiStub(self._ports_info.broker,self._ports_info.investor,self._ports_info.passwd)

        self.trade_queue = TCQ(self._env,self)
        self.spi.queue = self.trade_queue
        #print("in trade_spi_stub initialize")
        self.api = self.spi
        #print("in TAS_RS:Before RegisterSPI")
        self.api.Create(self,self._available)
        #print("in TAS_RS:After RegisterSPI")
        #self.trade_queue.start()
        self.trade_queue.put_command(QueryAccountCommand(self._stamp))

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    #def update_available(self,available):   #被apistub调用
    #   self.available = available

    def trigger_trade_queue(self):  # 只有在使用BaseTradeCommandQueueStub时才意义
        self.trade_queue.run()

