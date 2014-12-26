# -*- coding:utf-8 -*-

#常规导入
import unittest

#测试目标
from ..trader.builder import CommonBuilder

#功能文件
from ..common.base import TICK
from ..common.macro_command_queue import PassiveMacroCommandQueue
from ..common.contract_type import ContractManager,M,RM
from ..trader.environ import Environ
from ..trader.coordinator import Coordinator

#配置文件
from ..my.ports import ZSUsers

#测试夹具
from ..test.account_stub import AccountStub
from ..test.a_strategy import SExampleA
from ..test.m_strategy import SExampleAB


INIT_AVAILABLE = 1000000

TRADING_DAY = 20140101
day2ymd = lambda day: (day//10000,day%10000//100,day%100)

class CommonBuilderTestCase(unittest.TestCase):
    def setUp(self):
        self._env = Environ(TickMCQ=PassiveMacroCommandQueue,SecMCQ=PassiveMacroCommandQueue)
        self._account = AccountStub(self._env,ZSUsers,id="acc1",available=INIT_AVAILABLE)

    def test_initialize_A(self):
        cm1 = ContractManager([M])
        self._initialize_contracts_ticks(cm1.current_contracts(*day2ymd(TRADING_DAY)))
        triples = [ (Coordinator,SExampleA,cm1),
                    #(Coordinator,SExampleAB,cm1),
                ]
        builder = CommonBuilder(self._env,triples,TRADING_DAY)
        #for c in contracts:print(c.name)
        self.assertEqual(2,len(self._env.controller._agents))
        #for agent in self._env.controller._agents:
        #    print("B",agent.name)
            #for c in agent.contracts:print(c.name)

    def test_initialize_B(self):
        cm1 = ContractManager([RM,M])
        self._initialize_contracts_ticks(cm1.current_contracts(*day2ymd(TRADING_DAY)))
        triples = [ (Coordinator,SExampleAB,cm1),
                    #(Coordinator,SExampleAB,cm1),
                ]
        builder = CommonBuilder(self._env,triples,TRADING_DAY)
        self.assertEqual(2,len(self._env.controller._agents))
        #for agent in self._env.controller._agents:
        #    print("B:",agent.name)
            #for c in agent.contracts:print(c.name)

    def test_initialize_AB(self):
        cm1 = ContractManager([RM,M])
        self._initialize_contracts_ticks(cm1.current_contracts(*day2ymd(TRADING_DAY)))
        triples = [ (Coordinator,SExampleA,ContractManager([M])),
                    (Coordinator,SExampleAB,cm1),
                ]
        builder = CommonBuilder(self._env,triples,TRADING_DAY)
        self.assertEqual(4,len(self._env.controller._agents))
        #for agent in self._env.controller._agents:
        #    print("AB:",agent.name)
            #for c in agent.contracts:print(c.name)

    def _initialize_contracts_ticks(self,contracts):
        for c in contracts:
            self._initialize_contract_ticks(c)

    def _initialize_contract_ticks(self,contract,volume=100000,shigh=3500,slow=3400):
       tk = TICK(contract.name,TRADING_DAY)
       tk.common_reset()
       tk.dvolume = volume
       tk.high = shigh
       tk.low = slow
       #contract.last_tick = tk
       contract.ticks.append(tk)

