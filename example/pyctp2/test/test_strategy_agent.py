# -*- coding:utf-8 -*-

import os
import logging
import unittest
import unittest.mock as mock

from ..common.utils import ArgsCached
from ..common.contract_type import ContractInfo,M,P
from ..common.base import BaseObject,LONG,TEST_STATE_PATH,DAY_FINALIZE_TICK,TICK,TEST_PATH
from ..trader.strategy_agent import StrategyAgent,AgentState
from ..trader.position import POSITION_APPROVE_STATUS
from ..trader.strategy import POPEN
from ..trader.trade_command import OpenInstruction,CloseInstruction
from ..trader import strategy_agent
from ..test.a_strategy import SExampleA,SExampleA2,SExampleA3
from ..test.m_strategy import SExampleAB,SExampleAB2,SExampleAB0


class StrategyAgentTestCase(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(TEST_STATE_PATH):
            os.makedirs(TEST_STATE_PATH)
        strategy_agent.STATE_FNAME = TEST_STATE_PATH + '/positions.%s.txt'

        ArgsCached._args2obj.clear()        #清除缓存
        self._m = ContractInfo("m1501",1501,M)
        self._p = ContractInfo("p1501",1501,P)
        #print(self._m._ymonth,self._p._ymonth)
        self._m.long_marginrate = 0.1
        self._m.short_marginrate = 0.1
        self._m.multiple = 10
        self._p.long_marginrate = 0.1
        self._p.short_marginrate = 0.1
        self._p.multiple = 10
        self._account = "ACCOUNT_TEST"


    def test_base(self):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        agent = StrategyAgent(coordinator,[self._m])
        self.assertTrue(True)
        self.assertEqual(1,len(agent.contracts))
        self.assertEqual(self._m,agent.contracts[0])
        self.assertEqual(AgentState.ACTIVE,agent.state)
        agent.next_state()
        self.assertEqual(AgentState.CLOSE_ONLY,agent.state)
        agent.next_state()
        self.assertEqual(AgentState.MUST_CLOSE,agent.state)
        agent.next_state()
        self.assertEqual(AgentState.FINISHED,agent.state)
        self.assertEqual(["m1501"],agent.contract_names)
        #通道测试
        self.assertEqual([],agent.active_positions)
        self.assertEqual([],agent.get_positions_by_name("m1501"))
        self.assertEqual(0,agent.get_holding_volume("m1501"))
        #name
        #strategy_agent.STATE_FNAME = TEST_STATE_PATH + '/positions.%s.txt'

        self.assertEqual("SExampleA_m1501",agent.name)
        self.assertEqual("info/test/state/positions.SExampleA_m1501.txt",agent.state_path_name)

    def test_is_active(self):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        agent = StrategyAgent(coordinator,[self._m])
        self.assertTrue(agent.is_active)
        agent.s2close_only()
        self.assertTrue(agent.is_active)
        agent.s2must_close()
        self.assertTrue(agent.is_active)
        agent.s2finished()
        self.assertFalse(agent.is_active)
        agent.s2transfered()
        self.assertFalse(agent.is_active)

    def test_state(self):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        agent = StrategyAgent(coordinator,[self._m])
        self.assertEqual(AgentState.ACTIVE,agent.state)
        agent.s2must_close()
        self.assertEqual(AgentState.MUST_CLOSE,agent.state)
        agent.s2finished()
        self.assertEqual(AgentState.FINISHED,agent.state)

    def test_base2(self):       #2个Contract
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        agent = StrategyAgent(coordinator,[self._m,self._p])
        self.assertTrue(True)
        self.assertEqual([self._m,self._p],[agent.contracts[0],agent.contracts[1]])
        name_set2 = set(agent.contract_names)
        self.assertEqual(2,len(name_set2))
        self.assertTrue("m1501" in name_set2)
        self.assertTrue("p1501" in name_set2)
        #name
        #strategy_agent.STATE_FNAME = TEST_STATE_PATH + '/positions.%s.txt'

        self.assertEqual("SExampleA_m1501_p1501",agent.name)         #这里的顺序其实仅对此特定
        self.assertEqual("info/test/state/positions.SExampleA_m1501_p1501.txt",agent.state_path_name)

    def test_on_approve(self):  #通道测试
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        coordinator.available_balance = 50000

        agent = StrategyAgent(coordinator,[self._m])

        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        commands = agent.check_open(ctick,self._m)
        cmd = commands[0]
        agent.on_approved(cmd,POSITION_APPROVE_STATUS.REJECTED)

    def test_on_reject(self):  #通道测试
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        coordinator.available_balance = 50000

        agent = StrategyAgent(coordinator,[self._m])

        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        commands = agent.check_open(ctick,self._m)
        cmd = commands[0]
        agent.on_approved(cmd)
        agent.on_reject(cmd)

    def test_on_done(self):  #通道测试
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        coordinator.available_balance = 50000

        agent = StrategyAgent(coordinator,[self._m])

        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        commands = agent.check_open(ctick,self._m)
        cmd = commands[0]
        agent.on_approved(cmd)
        agent.on_progress(cmd,3660,1)
        agent.on_done(cmd,1)

    def test_open(self):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        coordinator.available_balance = 20000

        agent = StrategyAgent(coordinator,[self._m])

        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        commands = agent.check_open(ctick,self._m)
        self.assertEqual(1,len(commands))
        #print(commands)
        self.assertEqual(1,len(agent._position_holder._active_positions))
        open_order = agent._position_holder._active_positions[0].open_orders[0]
        self.assertEqual("m1501",open_order.contract_name)
        self.assertEqual(2,open_order.unit)
        self.assertEqual(2,open_order.planned)
        self.assertEqual(0,open_order.approved)
        commands[0].on_approved(POSITION_APPROVE_STATUS.REJECTED)
        self.assertEqual(0,len(agent._position_holder._active_positions)) #被删除
        self.assertEqual(1,len(agent._position_holder._closed_positions))
        #批准
        commands = agent.check_open(ctick,self._m)
        open_order = agent._position_holder._active_positions[0].open_orders[0]
        self.assertEqual(1,len(agent._position_holder._active_positions))
        open_order._approved = 2
        commands[0].on_approved()
        self.assertEqual(1,len(agent._position_holder._active_positions))
        #reject
        commands = agent.check_open(ctick,self._m)
        open_order = agent._position_holder._active_positions[0].open_orders[0]
        self.assertEqual(2,len(agent._position_holder._active_positions))
        open_order._approved = 1
        commands[0].on_reject()
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(2,len(agent._position_holder._closed_positions))

    def test_open1_1(self):     #测试开仓完成
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleA
        coordinator.available_balance = 20000

        agent = StrategyAgent(coordinator,[self._m])

        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        commands = agent.check_open(ctick,self._m)
        self.assertEqual(1,len(commands))
        #print(commands)
        self.assertEqual(1,len(agent._position_holder._active_positions))
        open_order = agent._position_holder._active_positions[0].open_orders[0]
        self.assertEqual("m1501",open_order.contract_name)
        self.assertEqual(2,open_order.unit)
        self.assertEqual(2,open_order.planned)
        self.assertEqual(0,open_order.approved)
        open_order._approved = 1
        commands[0].on_approved()
        self.assertEqual(1,len(agent._position_holder._active_positions))
        commands[0].on_done(1)
        commands[0].on_progress(1,3661)
        self.assertEqual(1,len(agent._position_holder._active_positions))


    def test_open2(self):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleAB
        coordinator.available_balance = 50000

        agent = StrategyAgent(coordinator,[self._m,self._p])

        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        ctick2 = mock.Mock()
        ctick2.price = 4660
        agent.contracts[1].ticks.append(ctick2)
        commands = agent.check_open(ctick,self._m,self._p)
        self.assertEqual(2,len(commands))
        #print(commands)
        self.assertEqual(2,len(agent._position_holder._active_positions))
        #print(agent.position_holder.active_positions)
        open_order1 = agent._position_holder._active_positions[0].open_orders[0]
        open_order2 = agent._position_holder._active_positions[1].open_orders[0]
        self.assertEqual("m1501",open_order1.contract_name)
        self.assertEqual(2,open_order1.unit)
        self.assertEqual(2,open_order1.planned)
        self.assertEqual(0,open_order1.approved)
        self.assertEqual("p1501",open_order2.contract_name)
        self.assertEqual(2,open_order2.unit)
        self.assertEqual(2,open_order2.planned)
        self.assertEqual(0,open_order2.approved)
        commands[0].on_approved(POSITION_APPROVE_STATUS.REJECTED)
        self.assertEqual(1,len(agent._position_holder._active_positions)) #被删除
        commands[1].on_approved(POSITION_APPROVE_STATUS.REJECTED)
        self.assertEqual(0,len(agent._position_holder._active_positions)) #被删除


    def test_base_get(self):
        t1 = TICK(self._m.name,20140101)
        t2 = TICK(self._p.name,20140101)
        t1.common_reset()
        t2.common_reset()
        t1.price = 1000
        t2.price = 2000
        self._m.ticks.append(t1)
        self._p.ticks.append(t2)

        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleAB
        coordinator.available_balance = 50000

        agent = StrategyAgent(coordinator,[self._m,self._p])
        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        ctick2 = mock.Mock()
        ctick2.price = 4660
        agent.contracts[1].ticks.append(ctick2)
        commands = agent.check_open(ctick,self._m,self._p)
        agent.get_net_holding_volume()  #通道测试
        agent.get_holding_info()  #通道测试
        sc = agent.calc_current_margin()    #通道测试
        self.assertEqual(0,sc)      #之前曾经返回[0,0]
        self.assertTrue(True)

    def test_recalc_state(self):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleAB
        coordinator.available_balance = 50000

        agent = StrategyAgent(coordinator,[self._m,self._p])
        self.assertEqual(AgentState.ACTIVE,agent.state)
        agent.recalc_state(20140917)
        self.assertEqual(AgentState.ACTIVE,agent.state)
        agent.recalc_state(20141209)
        self.assertEqual(AgentState.CLOSE_ONLY,agent.state)
        agent.recalc_state(20141211)
        self.assertEqual(AgentState.MUST_CLOSE,agent.state)

    def test_recalc_state2(self):   #两个不同期合约
        p1 = ContractInfo("p1409",1409,P)

        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleAB
        coordinator.available_balance = 50000

        agent = StrategyAgent(coordinator,[self._m,p1])
        self.assertEqual(AgentState.ACTIVE,agent.state)
        agent.recalc_state(20140709)
        self.assertEqual(AgentState.ACTIVE,agent.state)
        agent.recalc_state(20140810)
        self.assertEqual(AgentState.CLOSE_ONLY,agent.state)
        agent.recalc_state(20140811)
        self.assertEqual(AgentState.MUST_CLOSE,agent.state)

    def test_recalc_state_day0(self):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleAB
        coordinator.available_balance = 50000

        agent = StrategyAgent(coordinator,[self._m,self._p])
        self.assertEqual(AgentState.ACTIVE,agent.state)
        agent.recalc_state()    #测试通路
        self.assertTrue(True)

    def _prepare_close_1(self,mystrategy):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = mystrategy
        coordinator.available_balance = 20000
        # 设定mock函数
        agent = StrategyAgent(coordinator, [self._m])

        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)

        commands = agent.check_open(ctick, self._m)

        open_order = agent._position_holder._active_positions[0].open_orders[0]
        #print("++++++++++++++++++++++:",open_order.planned)
        open_order._approved = 2
        open_order._trade_info = BaseObject(trading_day=20101232)
        commands[0].on_done(2)
        self.assertEqual(2,agent.get_holding_volume(self._m._name))

        #print(open_order.state)
        return agent

    def test_close1(self):      #测试普通的closer
        agent = self._prepare_close_1(SExampleA)
        ctick = mock.Mock()
        ctick.price = 3661

        c_commands = agent.check_close(ctick,self._m)
        #print(open_order.state,c_commands[0].position.close_orders[0].state)
        self.assertEqual(1,len(c_commands))
        self.assertEqual(2,c_commands[0].order.approved)
        self.assertEqual(3660,c_commands[0].order.base_price)
        self.assertEqual(self._m,c_commands[0].order.contract)
        pos = c_commands[0].position
        self.assertEqual(pos,agent._position_holder._active_positions[0])
        self.assertEqual(1,len(pos.close_orders))

        #print(commands[0].position.close_orders[0].state,commands[0].position.close_orders[0].is_done())
        #print("pre on done")
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(0,len(agent._position_holder._closed_positions))

        #结束
        c_commands[0].on_done(2)
        #print("after on done")
        self.assertEqual(0,len(agent._position_holder._active_positions))
        self.assertEqual(1,len(agent._position_holder._closed_positions))
        self.assertEqual(pos,agent._position_holder._closed_positions[-1])

        c_commands = agent.check_close(ctick,self._m)    #已关闭
        self.assertEqual(0,len(c_commands))


    def test_close1_2(self):        #测试contractCloser
        agent = self._prepare_close_1(SExampleA2)
        ctick = mock.Mock()
        ctick.price = 3661

        commands = agent.check_open(ctick,self._m)
        open_order = agent._position_holder._active_positions[1].open_orders[0]
        self.assertEqual(1,open_order.unit)
        open_order._approved = 1
        open_order._trade_info = BaseObject(trading_day=20101232)
        self.assertEqual(3,agent.get_holding_volume(self._m._name))

        c_commands = agent.check_close(ctick,self._m)
        #print(c_commands)
        self.assertEqual(2,len(c_commands))

        #print(c_commands[0].order.approved,c_commands[1].order.approved)
        #按逆序分派
        self.assertEqual(1,c_commands[0].order.approved)
        self.assertEqual(agent._position_holder._active_positions[1],c_commands[0].position)
        self.assertEqual(2,c_commands[1].order.approved)
        self.assertEqual(agent._position_holder._active_positions[0],c_commands[1].position)
        self.assertEqual(1,len(c_commands[0].position.close_orders))
        self.assertEqual(1,len(c_commands[1].position.close_orders))
        self.assertEqual(3660,c_commands[0].order.base_price)
        self.assertEqual(self._m,c_commands[0].order.contract)

        self.assertEqual(0,agent.get_holding_volume(self._m._name))

        c_commands = agent.check_close(ctick,self._m)    #已关闭
        #print(c_commands)
        self.assertEqual(0,len(c_commands))


    def test_close1_2b(self):           #测试ContractCloser的分步平仓
        agent = self._prepare_close_1(SExampleA3)
        ctick = mock.Mock()
        ctick.price = 3661

        commands = agent.check_open(ctick,self._m)
        open_order = agent._position_holder._active_positions[1].open_orders[0]
        self.assertEqual(1,open_order.unit)
        open_order._approved = 1
        open_order._trade_info = BaseObject(trading_day=20101232)
        self.assertEqual(3,agent.get_holding_volume(self._m._name))

        #第一次只平2手
        c_commands = agent.check_close(ctick,self._m)
        #print(c_commands)
        self.assertEqual(2,len(c_commands))

        #print(c_commands[0].order.approved,c_commands[1].order.approved)
        #按逆序分派
        self.assertEqual(1,c_commands[0].order.approved)
        self.assertEqual(agent._position_holder._active_positions[1],c_commands[0].position)
        self.assertEqual(1,c_commands[1].order.approved)
        self.assertEqual(agent._position_holder._active_positions[0],c_commands[1].position)
        self.assertEqual(1,len(c_commands[0].position.close_orders))
        self.assertEqual(1,len(c_commands[1].position.close_orders))
        self.assertEqual(3660,c_commands[0].order.base_price)
        self.assertEqual(self._m,c_commands[0].order.contract)

        self.assertEqual(1,agent.get_holding_volume(self._m._name))
        self.assertEqual(1,agent._position_holder._active_positions[0].volume_holding)

        c_commands = agent.check_close(ctick,self._m)    #还有1手
        #print(c_commands)
        self.assertEqual(1,len(c_commands))
        self.assertEqual(1,c_commands[0].order.approved)
        self.assertEqual(agent._position_holder._active_positions[0],c_commands[0].position)
        self.assertEqual(0,agent.get_holding_volume(self._m._name))


        c_commands = agent.check_close(ctick,self._m)    #已关闭
        #print(c_commands)
        self.assertEqual(0,len(c_commands))

    def _prepare_close_2(self,mystrategy):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = mystrategy
        coordinator.available_balance = 50000
        # 设定mock函数
        agent = StrategyAgent(coordinator, [self._m, self._p])


        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        ctick2 = mock.Mock()
        ctick2.price = 4660
        agent.contracts[1].ticks.append(ctick2)

        commands = agent.check_open(ctick, self._m, self._p)
        open_order = agent._position_holder._active_positions[0].open_orders[0]
        open_order._approved = 2
        open_order._trade_info = BaseObject(trading_day=20101232)
        commands[0].on_approved()
        commands[0].on_done(2)
        commands[0].on_progress(1, 3661)
        open_order = agent._position_holder._active_positions[1].open_orders[0]
        open_order._trade_info = BaseObject(trading_day=20101232)
        open_order._approved = 1
        commands[1].on_approved()
        commands[1].on_done(1)
        commands[1].on_progress(1, 3661)
        return agent

    def test_close2(self):
        agent = self._prepare_close_2(SExampleAB)

        ctick = mock.Mock()
        c_commands = agent.check_close(ctick,self._m,self._p)
        self.assertEqual(2,len(c_commands))

        self.assertEqual(2,c_commands[0].order.approved)
        self.assertEqual(1,c_commands[1].order.approved)
        self.assertEqual(3660,c_commands[0].order.base_price)
        self.assertEqual(self._m,c_commands[0].order.contract)
        pos = c_commands[0].position
        pos2 = c_commands[1].position
        self.assertEqual(pos,agent._position_holder._active_positions[0])
        self.assertEqual(pos2,agent._position_holder._active_positions[1])
        self.assertEqual(1,len(pos.close_orders))
        self.assertEqual(1,len(pos2.close_orders))

        #print(commands[0].position.close_orders[0].state,commands[0].position.close_orders[0].is_done())
        #print("pre on done")
        self.assertEqual(2,len(agent._position_holder._active_positions))
        self.assertEqual(0,len(agent._position_holder._closed_positions))
        #结束
        c_commands[0].on_done(2)
        #print("after on done")
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(1,len(agent._position_holder._closed_positions))
        self.assertEqual(pos,agent._position_holder._closed_positions[-1])
        c_commands[1].on_done(1)
        self.assertEqual(0,len(agent._position_holder._active_positions))
        self.assertEqual(2,len(agent._position_holder._closed_positions))
        self.assertEqual(pos2,agent._position_holder._closed_positions[-1])

        c_commands = agent.check_close(ctick,self._m)    #已关闭
        self.assertEqual(0,len(c_commands))

    def test_close2_1(self):      #分段关闭
        agent = self._prepare_close_2(SExampleAB2)

        ctick = mock.Mock()
        c_commands = agent.check_close(ctick,self._m,self._p)
        self.assertEqual(2,len(c_commands))

        self.assertEqual(1,c_commands[0].order.approved)
        self.assertEqual(3660,c_commands[0].order.base_price)
        self.assertEqual(self._m,c_commands[0].order.contract)
        pos = c_commands[0].position
        pos2 = c_commands[1].position
        self.assertEqual(pos,agent._position_holder._active_positions[0])
        self.assertEqual(pos2,agent._position_holder._active_positions[1])
        self.assertEqual(1,len(pos.close_orders))
        self.assertEqual(1,len(pos2.close_orders))

        #print(commands[0].position.close_orders[0].state,commands[0].position.close_orders[0].is_done())
        #print("pre on done")
        self.assertEqual(2,len(agent._position_holder._active_positions))
        self.assertEqual(0,len(agent._position_holder._closed_positions))
        #结束
        c_commands[0].on_done(1)
        #print("after on done")
        self.assertEqual(2,len(agent._position_holder._active_positions))
        self.assertEqual(0,len(agent._position_holder._closed_positions))
        c_commands[1].on_done(1)
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(1,len(agent._position_holder._closed_positions))
        self.assertEqual(pos2,agent._position_holder._closed_positions[-1])

        c_commands = agent.check_close(ctick,self._m,self._p)    #继续关闭第一个仓位
        self.assertEqual(1,len(c_commands))
        c_commands[0].on_done(1)
        self.assertEqual(0,len(agent._position_holder._active_positions))
        self.assertEqual(2,len(agent._position_holder._closed_positions))
        self.assertEqual(pos,agent._position_holder._closed_positions[-1])

    def test_close20(self):     #盯2个合约,但是分别行动
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleAB0
        coordinator.available_balance = 20000

        agent = StrategyAgent(coordinator, [self._m, self._p])

        ctick = mock.Mock()
        ctick.instrument = "m1501"
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        ctick2 = mock.Mock()
        ctick2.instrument = "p1501"
        ctick2.price = 4660
        agent.contracts[1].ticks.append(ctick2)


        commands = agent.check_open(ctick, self._m, self._p)
        self.assertEqual(1,len(commands))
        self.assertEqual(self._m,commands[0].order.contract)
        self.assertEqual(2,commands[0].order.unit)
        open_order = agent._position_holder._active_positions[0].open_orders[0]
        open_order._approved = 2
        open_order._trade_info = BaseObject(trading_day=20101232)
        commands[0].on_approved()
        commands[0].on_done(2)
        commands[0].on_progress(2, 3661)

        coordinator.available_balance = 10000
        ctick.instrument = "p1501"
        commands = agent.check_open(ctick, self._m, self._p)
        self.assertEqual(1,len(commands))
        self.assertEqual(1,commands[0].order.unit)
        self.assertEqual(self._p,commands[0].order.contract)
        open_order = agent._position_holder._active_positions[1].open_orders[0]
        open_order._approved = 1
        open_order._trade_info = BaseObject(trading_day=20101232)
        commands[0].on_approved()
        commands[0].on_done(1)
        commands[0].on_progress(1, 3661)

        c_commands = agent.check_close(ctick,self._m,self._p)
        #print(c_commands[0].order.wanted,c_commands[1].order.wanted)
        self.assertEqual(1,len(c_commands))

        self.assertEqual(1,c_commands[0].order.approved)
        self.assertEqual(4660,c_commands[0].order.base_price)
        self.assertEqual(self._p,c_commands[0].order.contract)
        pos = c_commands[0].position
        self.assertEqual(pos,agent._position_holder._active_positions[1])
        self.assertEqual(1,len(pos.close_orders))


        #print(commands[0].position.close_orders[0].state,commands[0].position.close_orders[0].is_done())
        #print("pre on done")
        self.assertEqual(2,len(agent._position_holder._active_positions))
        self.assertEqual(0,len(agent._position_holder._closed_positions))
        #结束
        c_commands[0].on_done(1)
        #print("after on done")
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(1,len(agent._position_holder._closed_positions))
        self.assertEqual(pos,agent._position_holder._closed_positions[-1])

        ctick.instrument = "m1501"

        c_commands = agent.check_close(ctick,self._m,self._p)
        #print(c_commands[0].order.wanted,c_commands[1].order.wanted)
        self.assertEqual(1,len(c_commands))

        self.assertEqual(2,c_commands[0].order.approved)
        self.assertEqual(3660,c_commands[0].order.base_price)
        self.assertEqual(self._m,c_commands[0].order.contract)
        pos = c_commands[0].position
        self.assertEqual(pos,agent._position_holder._active_positions[0])
        self.assertEqual(1,len(pos.close_orders))


        #print(commands[0].position.close_orders[0].state,commands[0].position.close_orders[0].is_done())
        #print("pre on done")
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(1,len(agent._position_holder._closed_positions))
        #结束
        c_commands[0].on_done(2)
        #print("after on done")
        self.assertEqual(0,len(agent._position_holder._active_positions))
        self.assertEqual(2,len(agent._position_holder._closed_positions))
        self.assertEqual(pos,agent._position_holder._closed_positions[-1])

        c_commands = agent.check_close(ctick,self._m)    #已关闭
        self.assertEqual(0,len(c_commands))

    def test_day_finalize(self):
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleAB2
        #设定mock函数
        def make_initial_volume(*popens):
            popens[0].wanted = popens[0].planned = 2
            popens[1].wanted = popens[1].planned = 1
        coordinator.make_initial_volume.side_effect = make_initial_volume

        agent = StrategyAgent(coordinator,[self._m,self._p])

        agent._last_tick = DAY_FINALIZE_TICK

        self._m.ticks.append(BaseObject(price=1000))
        self._p.ticks.append(BaseObject(price=2000))
        agent.day_finalize()
        self.assertTrue(True)

    def test_force_close(self):
        agent = self._prepare_close_2(SExampleAB2)

        ctick = mock.Mock()
        ctick.price = 3661

        self.assertEqual(2,len(agent._position_holder._active_positions))
        c_commands = agent.force_close_all()
        c_commands[0].on_done(c_commands[0].order.approved)
        self.assertEqual(1,len(agent._position_holder._active_positions))
        c_commands[1].on_done(c_commands[1].order.approved)
        self.assertEqual(0,len(agent._position_holder._active_positions))

    def test_force_open1(self):
        coordinator = mock.Mock()
        #设定mock函数
        def make_initial_volume(*popens):
            popens[0].wanted = popens[0].planned = 1
        coordinator.make_initial_volume.side_effect = make_initial_volume

        agent = StrategyAgent(coordinator,[self._m])

        ctick = mock.Mock()
        ctick.price = 3660
        agent.contracts[0].ticks.append(ctick)
        command1 = POPEN(self._m,3661,LONG,[])
        command1.planned = command1.unit = 1
        self.assertEqual(0,len(agent._position_holder._active_positions))
        agent.force_open([command1])
        self.assertEqual(1,len(agent._position_holder._active_positions))

    def test_force_open2(self):
        coordinator = mock.Mock()
        #设定mock函数
        def make_initial_volume(*popens):
            popens[0].wanted = popens[0].planned = 1
        coordinator.make_initial_volume.side_effect = make_initial_volume

        agent = StrategyAgent(coordinator,[self._m,self._p])

        agent.contracts[0].ticks.append(BaseObject(price=3660))
        agent.contracts[1].ticks.append(BaseObject(price=4660))

        command1 = POPEN(self._m,3661,LONG,[])
        command1.planned = command1.unit = 1
        command2 = POPEN(self._p,4661,LONG,[])
        command2.planned = command2.unit = 1
        self.assertEqual(0,len(agent._position_holder._active_positions))
        agent.force_open([command1,command2])
        self.assertEqual(2,len(agent._position_holder._active_positions))

    def test_force_open_failed(self):
        coordinator = mock.Mock()
        #设定mock函数
        def make_initial_volume(*popens):
            popens[0].wanted = popens[0].planned = 1
        coordinator.make_initial_volume.side_effect = make_initial_volume

        agent = StrategyAgent(coordinator,[self._m,self._p])

        agent.contracts[0].ticks.append(BaseObject(price=3660))
        agent.contracts[1].ticks.append(BaseObject(price=4660))

        command1 = POPEN(self._m,3661,LONG,[])
        command1.planned = command1.unit = 1
        command2 = POPEN(self._m,4661,LONG,[])
        command2.planned = command2.unit = 1
        self.assertEqual(0,len(agent._position_holder._active_positions))
        self.assertRaises(AssertionError,agent.force_open,[command1,command2])      #同一个position没必要分为多个positions来打开

    def test_snapshot(self):
        #if not os.path.isdir(TEST_STATE_PATH):
        #    os.makedirs(TEST_STATE_PATH)
        #strategy_agent.STATE_FNAME = TEST_STATE_PATH + '/positions.%s.txt'
        agent = self._prepare_close_2(SExampleAB2)
        #print(agent.get_path_name())


        ctick = mock.Mock()
        c_commands = agent.check_close(ctick,self._m,self._p)
        pos = c_commands[0].position
        pos2 = c_commands[1].position
        c_commands[0].on_done(1)
        c_commands[1].on_done(1)
        agent.snapshot()

    def test__complete_position_holder(self):
        #if not os.path.isdir(TEST_STATE_PATH):
        #    os.makedirs(TEST_STATE_PATH)
        #strategy_agent.STATE_FNAME = TEST_STATE_PATH + '/positions.%s.txt'
        agent = self._prepare_close_1(SExampleA)

        ctick = mock.Mock()
        ctick.price = 3660

        commands = agent.check_open(ctick, self._m)
        open_order = agent._position_holder._active_positions[0].open_orders[0]
        open_order._approved = 0
        open_order._trade_info = BaseObject(trading_day=20101232)
        commands[0].on_done(0)
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(1,len(agent._position_holder._closed_positions))
        #print(agent.get_path_name())

        agent.snapshot()
        #print(agent.strategy.__getattribute__("_check_close"))
        pholder = agent._load_position_holder()
        self.assertEqual(1,len(pholder.active_positions))
        #self.assertEqual(1,len(pholder.closed_positions))
        self.assertEqual(agent._strategy._check_close,list(pholder.active_positions[0].closers)[0].close_func)

    def test__complete_position_holder2(self):
        #if not os.path.isdir(TEST_STATE_PATH):
        #    os.makedirs(TEST_STATE_PATH)
        #strategy_agent.STATE_FNAME = TEST_STATE_PATH + '/positions.%s.txt'
        agent = self._prepare_close_1(SExampleA)

        ctick = mock.Mock()
        ctick.price = 3660

        commands = agent.check_open(ctick, self._m)
        open_order = agent._position_holder._active_positions[1].open_orders[0]
        open_order._approved = 1
        open_order._trade_info = BaseObject(trading_day=20101232)
        commands[0].on_done(1)
        self.assertEqual(2,len(agent._position_holder._active_positions))
        self.assertEqual(0,len(agent._position_holder._closed_positions))
        #print(agent.get_path_name())

        agent.snapshot()
        #print(agent.strategy.__getattribute__("_check_close"))
        pholder = agent._load_position_holder()
        self.assertEqual(2,len(pholder.active_positions))
        self.assertEqual(0,len(pholder.closed_positions))
        self.assertEqual(agent._strategy._check_close,list(pholder.active_positions[0].closers)[0].close_func)
        self.assertEqual(agent._strategy._check_close,list(pholder.active_positions[1].closers)[0].close_func)

    def test_resume(self):
        #if not os.path.isdir(TEST_STATE_PATH):
        #    os.makedirs(TEST_STATE_PATH)
        #strategy_agent.STATE_FNAME = TEST_STATE_PATH + '/positions.%s.txt'

        agent = self._prepare_close_1(SExampleA)
        agent.snapshot()
        #agent.resume()

    def test_check(self):   #通过测试new_tick来测试_check
        coordinator = mock.Mock()
        coordinator.strategy_clazz = SExampleAB
        coordinator.available_balance = 1000000
        m1501 = ContractInfo("m1501",1501,M)
        p1501 = ContractInfo("p1501",1501,P)

        agent = StrategyAgent(coordinator,[m1501,p1501])
        ctick = mock.Mock()
        ctick.price = 3660
        m1501.ticks.append(ctick)
        ctick2 = mock.Mock()
        ctick2.price = 4660
        p1501.ticks.append(ctick2)

        commands = agent.check_open(ctick,m1501,p1501)
        assert len(commands) == 2
        assert len(agent._position_holder._active_positions) == 2
        #print(commands[0].order.planned)
        open_order = agent._position_holder._active_positions[0].open_orders[0]
        open_order._approved = 2
        open_order._trade_info = BaseObject(trading_day=20101232)
        open_order.account = self._account
        commands[0].on_approved()
        commands[0].on_done(2)
        commands[0].on_progress(2, 3661)
        open_order = agent._position_holder._active_positions[1].open_orders[0]
        open_order._trade_info = BaseObject(trading_day=20101232)
        open_order._approved = 2
        open_order.account = self._account
        commands[1].on_approved()
        commands[1].on_done(2)
        commands[1].on_progress(2, 3661)
        assert agent.position_holder.get_volume_holding("m1501")==2
        assert agent.position_holder.get_volume_holding("p1501")==2

        #第二个
        commands = agent.check_open(ctick,m1501,p1501)
        open_order = agent._position_holder._active_positions[2].open_orders[0]
        open_order._approved = 1
        open_order.account = self._account
        open_order._trade_info = BaseObject(trading_day=20101232)
        commands[0].on_approved()
        commands[0].on_done(1)
        commands[0].on_progress(1, 3661)
        open_order = agent._position_holder._active_positions[3].open_orders[0]
        open_order._approved = 1
        open_order.account = self._account
        open_order._trade_info = BaseObject(trading_day=20101232)
        commands[1].on_approved()
        commands[1].on_done(1)
        commands[1].on_progress(1, 3661)

        #打印信息
        assert len(agent._position_holder._active_positions) == 4
        assert agent._position_holder._active_positions[0].contract == m1501
        assert agent._position_holder._active_positions[1].contract == p1501
        assert agent._position_holder._active_positions[2].contract == m1501
        assert agent._position_holder._active_positions[3].contract == p1501
        assert agent._position_holder._active_positions[0].volume_holding == 2
        assert agent._position_holder._active_positions[1].volume_holding == 2
        assert agent._position_holder._active_positions[2].volume_holding == 1
        assert agent._position_holder._active_positions[3].volume_holding == 1
        assert agent.position_holder.get_volume_holding("m1501")==3
        assert agent.position_holder.get_volume_holding("p1501")==3

        #check it !!! 仅通道测试
        ctick = mock.Mock()
        ctick.price = 3660

        coordinator.lock_open_volume.return_value = POSITION_APPROVE_STATUS.APPROVED
        def sdx(instrs):        #设定开仓批准数
            for instr in instrs:
                instr.order.approve(1)
        coordinator.lock_open_volume.side_effect = sdx

        agent._new_tick(ctick)

        self.assertEqual(4,len(coordinator.execute.call_args_list))
        #print(coordinator.execute.call_args_list)
        #只关闭各合约倒数第一个pos
        #因为coordinator为mock,且未完成内在逻辑,故结果只能如下
        c1 = coordinator.execute.call_args_list[0][0][0]
        c2 = coordinator.execute.call_args_list[1][0][0]
        self.assertTrue(isinstance(c1,CloseInstruction))
        self.assertEqual(m1501,c1.contract)
        self.assertEqual(1,c1.planned)
        self.assertTrue(isinstance(c2,CloseInstruction))
        self.assertEqual(p1501,c2.contract)
        self.assertEqual(1,c2.planned)
        self.assertTrue(c2.order.account)   #必须设定了account
        #open
        c3 = coordinator.execute.call_args_list[2][0][0]
        c4 = coordinator.execute.call_args_list[3][0][0]
        self.assertTrue(isinstance(c3,OpenInstruction))
        self.assertEqual(m1501,c3.contract)
        self.assertEqual(19,c3.planned)
        self.assertTrue(isinstance(c4,OpenInstruction))
        self.assertEqual(p1501,c4.contract)
        self.assertEqual(29,c4.planned)


if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_strategy_agent.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()
