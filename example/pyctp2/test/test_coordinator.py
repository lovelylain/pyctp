# -*- coding:utf-8 -*-
import logging
import unittest
import unittest.mock as mock
import operator
import time
import os

from ..trader.coordinator import Coordinator, POSITION_HANDLE_TICK
from ..common.base import TEST_PATH,TICK,BaseObject,LONG,SHORT,ZERO_TICK,TEST_STATE_PATH
from ..common.contract_type import M,P,ContractInfo,ContractManager
from ..common.utils import next_trading_day,second2time,ArgsCached
from ..trader.strategy_agent import StrategyAgent,AgentState
from ..trader.position import ORDER_STATUS,Closer,ContractCloser,GlobalCloser,Position
from ..test.m_strategy import SExampleAB
from ..test.test_environ import prepare_environ
from ..trader import strategy_agent


def _prepare_agent_from(coordinator):

    m1501 = ContractInfo("m1501",1501,M)
    p1501 = ContractInfo("p1501",1501,P)
    for c in [m1501,p1501]:
        #c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
        #c._ticks = [BaseObject(price=3000,dvolume=100000,high=3100,low=2900)]
        last_tick = TICK(c.name,20990101)
        last_tick.common_reset()
        last_tick.price = 3000
        last_tick.dvolume = 100000
        last_tick.high = 3100
        last_tick.low = 2900

        c.ticks.append(last_tick)
        c._minutes = [BaseObject()] #制止resume时load数据
        #print("",type(coordinator.env))
        coordinator.env._contracts[c.name] = c
        coordinator.env.get_account().api._contracts[c.name] = c

    coordinator.env.reset_contracts([m1501,p1501])
    #coordinator.env.macro_queue.trigger()
    coordinator.env.macro_queue.trigger(time.time()+100)

    agent = StrategyAgent(coordinator,[m1501,p1501])
    ctick = mock.Mock()
    ctick.price = 3660
    commands = agent.check_open(ctick,m1501,p1501)
    assert len(commands) == 2
    assert len(agent._position_holder._active_positions) == 2
    #print(commands[0].order.planned)
    open_order = agent._position_holder._active_positions[0].open_orders[0]
    open_order._approved = 2
    open_order._trade_info = BaseObject(trading_day=20101232)
    commands[0].on_approved()
    commands[0].on_done(2)
    commands[0].on_progress(2, 3661)
    open_order = agent._position_holder._active_positions[1].open_orders[0]
    open_order._trade_info = BaseObject(trading_day=20101232)
    open_order._approved = 2
    commands[1].on_approved()
    commands[1].on_done(1)
    commands[1].on_progress(1, 3661)
    assert agent.position_holder.get_volume_holding("m1501")==2
    assert agent.position_holder.get_volume_holding("p1501")==1

    #第二个
    commands = agent.check_open(ctick,m1501,p1501)
    open_order = agent._position_holder._active_positions[2].open_orders[0]
    open_order._approved = 1
    open_order._trade_info = BaseObject(trading_day=20101232)
    commands[0].on_approved()
    commands[0].on_done(1)
    commands[0].on_progress(1, 3661)

    #打印信息
    assert len(agent._position_holder._active_positions) == 3
    assert agent._position_holder._active_positions[0].contract == m1501
    assert agent._position_holder._active_positions[1].contract == p1501
    assert agent._position_holder._active_positions[2].contract == m1501
    assert agent._position_holder._active_positions[0].volume_holding == 2
    assert agent._position_holder._active_positions[1].volume_holding == 1
    assert agent._position_holder._active_positions[2].volume_holding == 1
    assert agent.position_holder.get_volume_holding("m1501")==3
    assert agent.position_holder.get_volume_holding("p1501")==1

    return agent


def _prepare_agent_to(coordinator):
    m1505 = ContractInfo("m1505",1505,M)
    p1505 = ContractInfo("p1505",1505,P)
    m1505._minutes = [BaseObject()]
    p1505._minutes = [BaseObject()]
    agent = StrategyAgent(coordinator,[m1505,p1505])



class CoordinatorTestCase(unittest.TestCase):

    def setUp(self):
        #ArgsCached._args2obj.clear()
        ArgsCached.clear()

        if not os.path.isdir(TEST_STATE_PATH):
            os.makedirs(TEST_STATE_PATH)
        strategy_agent.STATE_FNAME = TEST_STATE_PATH + '/positions.%s.txt'


        #contract因为是在整个测试过程中通过缓存共享, 故不会受到setUp影响. 须在测试本身 设定环境时 规整其相关属性如last_tick
        self._m = ContractInfo("m1501",1501,M)
        self._p = ContractInfo("p1501",1501,P)
        self._m1405 = ContractInfo("m1405",1405,M)
        self._p1405 = ContractInfo("p1405",1405,P)
        self._m1409 = ContractInfo("m1409",1409,M)
        self._p1409 = ContractInfo("p1409",1409,P)

        #print("******************************")
        self._env = prepare_environ()
        self._controller = self._env.controller

        self._env._contracts.clear()
        #self._env._contracts = {}

        vhl = [(1000,3500,3400),(100,3800,3750),(1000,3500,3400),(100,3800,3750),(1000,3500,3400),(100,3800,3750)]   #(volume,high,low), volume=100,避免成为主力

        for c,dv in zip([self._m,self._p,self._m1405,self._m1409,self._p1405,self._p1409],vhl):
            #print(c.name)
            tk = TICK(c.name,20140909)
            tk.common_reset()
            tk.dvolume = dv[0]
            tk.high = dv[1]
            tk.low = dv[2]
            #c.last_tick = tk
            c.ticks.append(tk)
            c._minutes = [BaseObject()] #制止resume时load data


        #print("**********sasadfdsafdsfasaf*******")
        #self._cms = ContractManagerStub([self._m,self._p])
        self._cms = ContractManager([M,P])

        self._coordinator = Coordinator(self._env,SExampleAB,self._cms,tday=20140201)    #预加载数据

        #self._env.update_instrument("m1405","TEST",1,5,0,0)         #初始数据, 实际运行中也须对跟踪的contract设置
        #self._env.update_instrument("p1405","TEST",1,5,0,0)         #初始数据, 实际运行中也须对跟踪的contract设置
        #self._env.update_instrument("m1409","TEST",1,5,0,0)         #初始数据, 实际运行中也须对跟踪的contract设置
        #self._env.update_instrument("p1409","TEST",1,5,0,0)         #初始数据, 实际运行中也须对跟踪的contract设置
        #self._env.update_instrument("m1501","TEST",1,5,0,0)         #初始数据, 实际运行中也须对跟踪的contract设置
        #self._env.update_instrument("p1501","TEST",1,5,0,0)         #初始数据, 实际运行中也须对跟踪的contract设置

        #print("coordinator.agent:",len(self._coordinator.agents))
        #if(len(self._coordinator.agents)>0):
        #    print(self._coordinator.agents[0].name)

    def tearDown(self):
        self._env.get_account().api.exchange.finalize() #仅在测试时有意义
        ArgsCached.clear()


    def test_base(self):
        coordinator = self._coordinator
        self.assertFalse(coordinator.is_auto_transfer)
        self.assertEqual(SExampleAB,coordinator.strategy_clazz)
        self.assertEqual(self._env,coordinator.env)
        self.assertEqual(self._controller,coordinator.controller)
        self.assertEqual([],coordinator.agents)
        self.assertEqual(0,coordinator.balance)
        coordinator.balance = 10
        self.assertEqual(1000000,coordinator.available_balance)
        self.assertEqual(coordinator.balance,coordinator.available_balance) #注意,只有计算之后才相等
        coordinator2 = Coordinator(self._env,SExampleAB,self._cms,tday=20140201)    #落入已初始化的contracts中
        self.assertEqual(500000,coordinator.available_balance)
        self.assertEqual(coordinator.balance,coordinator.available_balance)
        self.assertEqual(10,coordinator.shares)

    def test_name(self):
        coordinator = self._coordinator
        self.assertEqual("Coordinator_SExampleAB_m_p",coordinator.name)
        self._cms._contract_types = []
        self.assertEqual("Coordinator_SExampleAB",coordinator.name)

    def test__contracts2name(self):
        coordinator = self._coordinator
        self.assertEqual("",coordinator._contracts2name([]))
        self.assertEqual("m1501",coordinator._contracts2name([self._m]))
        self.assertEqual("m1501.p1501",coordinator._contracts2name([self._m,self._p]))

    def test__calc_margin(self):
        coordinator = self._coordinator
        self.assertEqual(0,coordinator._calc_margin())
        a1 = mock.Mock()
        a2 = mock.Mock()
        a1.calc_current_margin.return_value = 1000
        a2.calc_current_margin.return_value = 2000
        coordinator._contracts2agent = {"m1501":a1,"p1501":a2}
        self.assertEqual(3000,coordinator._calc_margin())

    def test__contracts_flying(self):
        coordinator = self._coordinator
        cs = self._cms.current_contracts_by_ctype(M,2014,9,19)
        self.assertEqual("m1501",cs[0].name)        #确认下合约名
        self.assertEqual("m1505",cs[1].name)
        self.assertEqual("m1509",cs[2].name)
        vhl = [(150000,3500,3400),(40000,3800,3750),(12000,3900,3890)]   #(volume,high,low)
        for c,dv in zip(cs,vhl):
            tk = TICK(c.name,20140909)
            tk.common_reset()
            tk.dvolume = dv[0]
            tk.high = dv[1]
            tk.low = dv[2]
            #c.last_tick = tk
            c.ticks.append(tk)
            c._minutes = [BaseObject()] #制止resume时load data
        rev = coordinator._contracts_flying(M,20140919)
        self.assertEqual(2,len(rev))
        self.assertEqual("m1501",rev[0].name)
        self.assertEqual("m1505",rev[1].name)
        self.assertEqual(0,rev[0].iv)
        self.assertEqual(1,rev[1].iv)
        #cs[1].last_tick.dvolume = 30000
        #cs[1].last_tick.high = 4000
        #cs[1].last_tick.low = 3000
        rev = coordinator._contracts_flying(M,20140919)
        self.assertEqual(2,len(rev))
        self.assertEqual("m1501",rev[0].name)
        self.assertEqual("m1505",rev[1].name)
        #cs[1].last_tick.high = 40000
        #cs[1].last_tick.low = 30000
        cs[1].ticks[-1].high = 40000
        cs[1].ticks[-1].low = 30000
        rev = coordinator._contracts_flying(M,20140919)
        self.assertEqual(1,len(rev))
        self.assertEqual("m1501",rev[0].name)
        #成交量序号
        cs[1].ticks[-1].dvolume = 200000
        cs[1].ticks[-1].high = 4000
        cs[1].ticks[-1].low = 3000
        rev = coordinator._contracts_flying(M,20140919)
        self.assertEqual(2,len(rev))
        self.assertEqual("m1501",rev[0].name)
        self.assertEqual("m1505",rev[1].name)
        self.assertEqual(1,rev[0].iv)
        self.assertEqual(0,rev[1].iv)
        #drange=0
        cs[1].ticks[-1].high = 40000
        cs[1].ticks[-1].low = 40000
        rev = coordinator._contracts_flying(M,20140919)
        self.assertEqual(1,len(rev))
        self.assertEqual("m1501",rev[0].name)
        self.assertEqual(0,rev[0].iv)

    def test__last_group(self):
        coordinator = self._coordinator
        cs = self._cms.current_contracts_by_ctype(M,2014,9,19)
        vhl = [(150000,3500,3400),(40000,3800,3750),(12000,3900,3890)]   #(volume,high,low)
        for c,dv in zip(cs,vhl):
            tk = TICK(c.name,20140909)
            tk.common_reset()
            tk.dvolume = dv[0]
            tk.high = dv[1]
            tk.low = dv[2]
            #c.last_tick = tk
            c.ticks.append(tk)
            c._minutes = [BaseObject()] #制止resume时load data
        cs2 = self._cms.current_contracts_by_ctype(P,2014,9,19)
        for c,dv in zip(cs2,vhl):
            tk = TICK(c.name,20140909)
            tk.common_reset()
            tk.dvolume = dv[0]
            tk.high = dv[1]
            tk.low = dv[2]
            #c.last_tick = tk
            c.ticks.append(tk)
            c._minutes = [BaseObject()] #制止resume时load data
        cgrp = coordinator._last_group(20140919)
        self.assertEqual(2,len(cgrp))
        self.assertEqual("m1505",cgrp[0].name)
        self.assertEqual("p1505",cgrp[1].name)
        #cs2[1].last_tick.dvolume = 10000
        cs2[1].ticks[-1].dvolume = 10000
        cgrp = coordinator._last_group(20140919)
        self.assertEqual(2,len(cgrp))
        self.assertEqual("m1505",cgrp[0].name)
        self.assertEqual("p1501",cgrp[1].name)
        #测试稳定性
        cgrp = coordinator._last_group(20140919)
        self.assertEqual(2,len(cgrp))
        #品种P无可用合约
        #cs2[0].last_tick.dvolume = 10000
        cs2[0].ticks[-1].dvolume = 10000
        cgrp = coordinator._last_group(20140919)
        self.assertEqual([],cgrp)

    def test_check_open_volume(self):   #完全的白盒mock方式, DEPENDS Environ.approve_open
        coordinator = self._coordinator
        open_command = BaseObject()
        instr1 = BaseObject(order=BaseObject())
        instr2 = BaseObject(order=BaseObject())
        instructions = [instr1,instr2]
        coordinator._env = mock.Mock()
        coordinator.lock_open_volume(instructions)
        coordinator._env.approve_open.assert_called_once_with([instr1.order,instr2.order])

    def test_new_tick(self):
        coordinator = self._coordinator
        coordinator._contracts = {"m1501":self._m,"p1501":self._p}
        t1 = TICK("m1501",20140919)
        t1.common_reset()
        t1.min1 = 1401
        del coordinator._name2contract["m1501"].last_tick
        self.assertRaises(AttributeError,getattr,coordinator._name2contract["m1501"],"last_tick")
        coordinator.new_tick(t1)
        self.assertRaises(AttributeError,getattr,coordinator._name2contract["m1501"],"last_tick")
        t1.min1 = 1455
        #print(coordinator._contracts.keys())
        coordinator.new_tick(t1)
        self.assertEqual(t1,coordinator._name2contract["m1501"].last_tick)
        t2 = TICK("m150X",20140919)
        t2.min1 = 1401
        coordinator.new_tick(t2)
        t2.min1 = 1455
        self.assertRaises(KeyError,coordinator.new_tick,t2)

    def test_execute(self):
        coordinator = self._coordinator
        open_command = BaseObject()
        instr1 = BaseObject()
        instr2 = BaseObject()
        open_command.instructions = [instr1,instr2]
        instr1.order = BaseObject()
        instr2.order = BaseObject()
        coordinator._env = mock.Mock()
        command = BaseObject(xcommand=1)
        coordinator.execute(command)
        coordinator._env.execute_trade_command.assert_called_once_with(command)

    def test_check_agent_state(self):
        agent1 = mock.Mock()
        agent2 = mock.Mock()
        coordinator = self._coordinator
        coordinator._contracts2agent = {self._m:agent1,self._p:agent2}
        coordinator.check_agent_state(agent1)
        agent1.recalc_state.assert_called_once_with(coordinator.tday)
        agent2.recalc_state.assert_called_once_with(coordinator.tday)

    def test_deactive_previous_agents(self):
        coordinator = self._coordinator
        agent1 = mock.Mock()
        agent2 = mock.Mock()
        coordinator._contracts2agent = {self._m:agent1,self._p:agent2}
        coordinator.deactive_previous_agents(agent1)
        self.assertRaises(AssertionError,agent1.s2close_only.assert_called_once_with)
        agent2.s2close_only.assert_called_once_with()

    def test__check_transfer_volume(self):
        coordinator = self._coordinator
        pos = BaseObject(volume_holding = 10,contract = BaseObject(last_price=3000))
        p1,v1 = coordinator._check_transfer_volume(pos,5)
        p2,v2 = coordinator._check_transfer_volume(pos,15)
        self.assertEqual(pos,p1.position)
        self.assertEqual(pos,p2.position)
        self.assertEqual(5,v1)
        self.assertEqual(10,v2)
        self.assertEqual(5,p1.planned)
        self.assertEqual(10,p2.planned)
        self.assertEqual(3000,p1.base_price)
        self.assertEqual(3000,p2.base_price)
        self.assertEqual(30,p1.extra_hops)
        self.assertEqual(30,p2.extra_hops)

    def test__achieve_transfer_close(self):
        coordinator = self._coordinator
        instr1 = mock.Mock()
        instr2 = mock.Mock()
        instrs = [instr1,instr2]
        instr1.order = BaseObject(approved = 10)
        instr2.order = BaseObject(approved = 5)
        instr1.contract = BaseObject(last_price=3000)
        instr2.contract = BaseObject(last_price=4000)
        coordinator._achieve_transfer_close(instrs)
        #instr1.on_approved.assert_called_once_with()
        #instr2.on_approved.assert_called_once_with()
        instr1.on_progress.assert_called_once_with(10,3000)
        instr2.on_progress.assert_called_once_with(5,4000)
        instr1.on_done.assert_called_once_with(10)
        instr2.on_done.assert_called_once_with(5)

    def test__position_handle(self):
        coordinator = self._coordinator
        #print(type(coordinator._env))
        agent_from = _prepare_agent_from(self._coordinator)
        cagent = BaseObject()   #只用于识别
        cname = coordinator._contracts2name(agent_from.contracts)
        coordinator._contracts2agent[cname] = agent_from
        menv = mock.Mock()
        #分支: self.env.trading_day < today()
        menv.trading_day = 10
        coordinator._env = menv
        coordinator._position_handle(cagent)
        self.assertEqual(1,menv.put_sec_macro_command.call_count)
        mcmd = menv.put_sec_macro_command.call_args[0][0]
        self.assertEqual(coordinator._position_handle,mcmd._target)
        self.assertEqual(cagent,mcmd._params)
        ttime = second2time(next_trading_day()*1000000+POSITION_HANDLE_TICK)
        self.assertTrue(abs(ttime-mcmd._trigger_time)<1)
        #分支:self._auto_transfer
        coordinator._auto_transfer = True
        menv.reset_mock()
        menv.trading_day = 20991231
        coordinator.transfer = mock.Mock()
        agent_from.force_close_all = mock.Mock()
        agent_from.s2must_close()
        coordinator._position_handle(cagent)
        self.assertEqual(0,menv.put_sec_macro_command.call_count)
        coordinator.transfer.assert_called_once_with(agent_from,cagent)
        agent_from.force_close_all.assert_called_once_with()
        self.assertEqual(AgentState.TRANSFERED,agent_from.state)

        #分支: self._auto_transfer == False
        coordinator._auto_transfer = False
        menv.reset_mock()
        menv.trading_day = 20991231
        agent_from.force_close_all = mock.Mock()
        agent_from._state = AgentState.MUST_CLOSE   #只能直接这样才能设回
        coordinator._position_handle(cagent)
        self.assertEqual(0,menv.put_sec_macro_command.call_count)
        agent_from.force_close_all.assert_called_once_with()
        self.assertEqual(AgentState.FINISHED,agent_from.state)

        #_auto_transfer==True and cagent == None
        coordinator._auto_transfer = True
        menv.reset_mock()
        menv.trading_day = 20991231
        agent_from.force_close_all = mock.Mock()
        agent_from._state = AgentState.MUST_CLOSE   #只能直接这样才能设回
        coordinator._position_handle(None)
        self.assertEqual(0,menv.put_sec_macro_command.call_count)
        agent_from.force_close_all.assert_called_once_with()
        self.assertEqual(AgentState.FINISHED,agent_from.state)

        #print(ArgsCached._args2obj)
        #ArgsCached.clear()

    def test__check_transfer_close(self):
        coordinator = self._coordinator
        m1501 = ContractInfo("m1501",1501,M)
        m1501.ticks.append(BaseObject(price=3000))
        agent_from = _prepare_agent_from(self._coordinator)
        poses = agent_from.get_positions_by_name("m1501")
        self.assertEqual(2,len(poses))
        self.assertEqual(2,poses[0].volume_holding)
        self.assertEqual(1,poses[1].volume_holding)
        self.assertEqual(LONG,poses[0].direction)
        #vlong=1,vshort=1, exception
        self.assertRaises(AssertionError,coordinator._check_transfer_close,poses,1,1)
        #vlong=1
        pcloses = coordinator._check_transfer_close(poses,1,0)
        self.assertEqual(1,len(pcloses))
        self.assertEqual(poses[0],pcloses[0].position)
        self.assertEqual(3000,pcloses[0].base_price)
        self.assertEqual(1,pcloses[0].planned)
        self.assertEqual(1,pcloses[0].unit)
        self.assertEqual(SHORT,pcloses[0].direction)
        #vlong=3
        pcloses = coordinator._check_transfer_close(poses,3,0)
        self.assertEqual(2,len(pcloses))
        self.assertEqual(poses[0],pcloses[0].position)
        self.assertEqual(3000,pcloses[0].base_price)
        self.assertEqual(2,pcloses[0].planned)
        self.assertEqual(2,pcloses[0].unit)
        self.assertEqual(SHORT,pcloses[0].direction)
        self.assertEqual(poses[1],pcloses[1].position)
        self.assertEqual(3000,pcloses[1].base_price)
        self.assertEqual(1,pcloses[1].planned)
        self.assertEqual(1,pcloses[1].unit)
        self.assertEqual(SHORT,pcloses[1].direction)
        #vlong=4, exception
        self.assertRaises(AssertionError,coordinator._check_transfer_close,poses,4,0)
        #vlong=1,vshort=1
        poses[1]._direction = SHORT
        pcloses = coordinator._check_transfer_close(poses,1,1)
        self.assertEqual(2,len(pcloses))
        self.assertEqual(poses[0],pcloses[0].position)
        self.assertEqual(3000,pcloses[0].base_price)
        self.assertEqual(1,pcloses[0].planned)
        self.assertEqual(1,pcloses[0].unit)
        self.assertEqual(SHORT,pcloses[0].direction)
        self.assertEqual(poses[1],pcloses[1].position)
        self.assertEqual(3000,pcloses[1].base_price)
        self.assertEqual(1,pcloses[1].planned)
        self.assertEqual(1,pcloses[1].unit)
        self.assertEqual(LONG,pcloses[1].direction)

    def test_day_finalize(self):
        coordinator = self._coordinator
        coordinator._env = mock.Mock()
        #通道
        #准备
        for c in self._cms.current_contracts():
            #c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)
            #print(c.name)

        coordinator.day_finalize()
        self.assertEqual(1,len(coordinator._env.put_sec_macro_command.call_args_list))
        mc = coordinator._env.put_sec_macro_command.call_args[0][0]
        self.assertEqual(coordinator._position_handle,mc._target)
        self.assertTrue(isinstance(mc._params,StrategyAgent))
        ttime = second2time(next_trading_day()*1000000+POSITION_HANDLE_TICK)
        self.assertTrue(abs(ttime-mc._trigger_time)<1)

        for contract in coordinator.contracts:
            self.assertEqual(ZERO_TICK,contract.last_tick)
        self.assertEqual(len(self._cms.current_contracts()),len(coordinator._name2contract))
        coordinator._env.reset_mock()
        #print([a.name for a in coordinator.agents])
        self.assertEqual(1,len(coordinator.agents))
        self.assertEqual(AgentState.ACTIVE,coordinator.agents[0].state)
        # cname in self._contracts2agent分支
        for c in self._cms.current_contracts():
            c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
        coordinator.day_finalize()

        #last_group==[]分支,测试稳定性
        coordinator.day_finalize()
        self.assertEqual(1,len(coordinator.agents))

    def test_day_finalize2(self):
        coordinator = self._coordinator
        coordinator._env = mock.Mock()


        #测试指定日期
        coordinator.tday = 20120505
        for c in self._cms.current_contracts(2012,5,5):
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)
        for c in self._cms.current_contracts(2012,9,5):
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)
            #c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            #c.ticks.append(c.last_tick)
        for c in self._cms.current_contracts(2013,5,5):
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)
            #c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            #c.ticks.append(c.last_tick)
        coordinator.day_finalize(20120505)
        self.assertEqual(1,len(coordinator.agents))
        self.assertEqual(AgentState.ACTIVE,coordinator.agents[0].state)
        coordinator.day_finalize(20120905)
        self.assertEqual(2,len(coordinator.agents))
        #print(coordinator.agents[0].name,coordinator.agents[1].name)
        self.assertEqual(AgentState.ACTIVE,coordinator.agents[0].state)
        self.assertEqual(AgentState.ACTIVE,coordinator.agents[1].state)
        #1305不得开仓
        #print("**********************************************************")
        coordinator.day_finalize(20130405)
        self.assertEqual(3,len(coordinator.agents))
        sorted_agents = sorted(coordinator.agents,key=operator.attrgetter("name"))
        #print(sorted_agents[0].name,sorted_agents[1].name,sorted_agents[2].name)
        #self.assertEqual("SExampleAB_m1401_p1401",coordinator.agents[0].name)
        self.assertEqual(AgentState.CLOSE_ONLY,sorted_agents[0].state)
        self.assertEqual(AgentState.ACTIVE,sorted_agents[1].state)
        self.assertEqual(AgentState.ACTIVE,sorted_agents[2].state)
        #1305不再开仓
        coordinator.day_finalize(20130405)
        #print("###########################################################")
        sorted_agents = sorted(coordinator.agents,key=operator.attrgetter("name"))
        #print(sorted_agents[0].name,sorted_agents[1].name,sorted_agents[2].name)
        self.assertEqual(3,len(coordinator.agents))

        #print(sorted_agents[0].name,sorted_agents[1].name,sorted_agents[2].name)
        self.assertEqual("SExampleAB_m1305_p1305",sorted_agents[0].name)    #打印信息
        self.assertEqual("SExampleAB_m1309_p1309",sorted_agents[1].name)
        self.assertEqual("SExampleAB_m1401_p1401",sorted_agents[2].name)
        self.assertEqual(AgentState.CLOSE_ONLY,sorted_agents[0].state)
        self.assertEqual(AgentState.ACTIVE,sorted_agents[1].state)
        self.assertEqual(AgentState.ACTIVE,sorted_agents[2].state)

        #1305平仓
        coordinator.day_finalize(20130411)
        #print("###########################################################")
        sorted_agents = sorted(coordinator.agents,key=operator.attrgetter("name"))
        #print(sorted_agents[0].name,sorted_agents[1].name,sorted_agents[2].name)
        self.assertEqual(3,len(coordinator.agents))

        #print(sorted_agents[0].name,sorted_agents[1].name,sorted_agents[2].name)
        self.assertEqual("SExampleAB_m1305_p1305",sorted_agents[0].name)    #打印信息
        self.assertEqual("SExampleAB_m1309_p1309",sorted_agents[1].name)
        self.assertEqual("SExampleAB_m1401_p1401",sorted_agents[2].name)
        self.assertEqual(AgentState.MUST_CLOSE,sorted_agents[0].state)
        self.assertEqual(AgentState.ACTIVE,sorted_agents[1].state)
        self.assertEqual(AgentState.ACTIVE,sorted_agents[2].state)

        #mc1 = coordinator._env.put_sec_macro_command.call_args_list[0][0][0]
        #mc4 = coordinator._env.put_sec_macro_command.call_args_list[3][0][0]
        #print(mc1._trigger_time,mc4._trigger_time)

    def test__check_last_agent(self):   #仅通道测试
        coordinator = self._coordinator
        coordinator._env = mock.Mock()
        #for c in self._cms.current_contracts():
            #c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
        #    pass

        coordinator._check_last_agent(0)

    def test__transfer_open_part_execute(self):
        coordinator = self._coordinator
        #coordinator.execute = mock.Mock()
        for c in self._cms.current_contracts(2014,5,5):
            #print(c.name)
            #c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            #c._ticks = [BaseObject(price=3000,dvolume=100000,high=3100,low=2900)]
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)

        m1505 = ContractInfo("m1505",1505,M)
        m_tick = BaseObject(instrument='m1505',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3006,      #必须保证成交
                         high = 99999999,low=0,
            )
        self._env.get_account().api.new_tick(m_tick)
        self._env.get_account().api._contracts["m1505"] = m1505
        self._env._contracts["m1505"] = m1505
        #self._env.reset_contracts(self._env._contracts.values())
        m1505.multiple = 5

        coordinator.day_finalize(20140505)
        agent = coordinator.agents[0]
        #print(agent.contracts[0].name,agent.contracts[1].name)
        self.assertEqual("m1505",agent.contracts[0].name)
        closers = [BaseObject(a=1),BaseObject(a=2)]
        self.assertEqual(0,len(agent._position_holder._active_positions))
        self.assertEqual(0,len(agent._position_holder._name2positions))
        instr = coordinator._transfer_open(agent,LONG,m1505,closers,10,3)
        self.assertEqual(m1505,instr.contract)
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(1,len(agent._position_holder._name2positions))
        self.assertEqual(1,len(agent._position_holder._name2positions["m1505"]))
        self.assertEqual(agent._position_holder._active_positions[0],agent._position_holder._name2positions["m1505"][0])
        pos = agent._position_holder._active_positions[0]
        self.assertEqual(10,pos.volume_holding)
        self.assertEqual(7,pos.open_order.transfered)
        self.assertEqual(ORDER_STATUS.SUCCESSED,pos.open_order.state)
        #print(pos.volume_holding)

    def test__transfer_open_non_execute(self):  #完全transfer,不需要实际open
        coordinator = self._coordinator
        #coordinator.execute = mock.Mock()
        for c in self._cms.current_contracts(2014,5,5):
            #print(c.name)
            #c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            #c._ticks = [BaseObject(price=3000,dvolume=100000,high=3100,low=2900)]
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)

        m1505 = ContractInfo("m1505",1505,M)

        coordinator.day_finalize(20140505)
        agent = coordinator.agents[0]
        #print(agent.contracts[0].name,agent.contracts[1].name)
        self.assertEqual("m1505",agent.contracts[0].name)
        closers = [BaseObject(a=1),BaseObject(a=2)]
        self.assertEqual(0,len(agent._position_holder._active_positions))
        self.assertEqual(0,len(agent._position_holder._name2positions))
        instr = coordinator._transfer_open(agent,LONG,m1505,closers,10,0)
        self.assertEqual(m1505,instr.contract)
        self.assertEqual(1,len(agent._position_holder._active_positions))
        self.assertEqual(1,len(agent._position_holder._name2positions))
        self.assertEqual(1,len(agent._position_holder._name2positions["m1505"]))
        self.assertEqual(agent._position_holder._active_positions[0],agent._position_holder._name2positions["m1505"][0])
        pos = agent._position_holder._active_positions[0]
        self.assertEqual(10,pos.volume_holding)
        self.assertEqual(10,pos.open_order.transfered)
        self.assertEqual(ORDER_STATUS.SUCCESSED,pos.open_order.state)
        #print(pos.volume_holding)

    def test__transfer_open_prepare_failed(self):  #测试无合法instr而进入的直接返回分支
        coordinator = self._coordinator
        #coordinator.execute = mock.Mock()
        m1505 = ContractInfo("m1505",1505,M)

        for c in [m1505]:
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)
            c._minutes = [BaseObject()] #制止resume时load data

        agent = mock.Mock()
        agent.prepare_open_command.return_value = []
        #print(agent.contracts[0].name,agent.contracts[1].name)
        closers = [BaseObject(a=1),BaseObject(a=2)]
        instr = coordinator._transfer_open(agent,LONG,m1505,closers,10,3)
        self.assertIsNone(instr)

    def test__complete_target_closers(self):
        coordinator = self._coordinator
        m1305 = ContractInfo("m1305",1305,M)
        cagent = StrategyAgent(coordinator,[self._m,self._p])
        s_ncloser1 = Closer(None,None)
        s_ncloser2 = Closer(None,None)
        s_ccloser = ContractCloser(None,None)
        s_ccloser.prepare(None,m1305)
        s_gcloser = GlobalCloser(None,None)
        s_pos1 = Position(m1305,LONG)
        s_pos2 = Position(m1305,LONG)
        s_closed_pos3 = Position(m1305,LONG)
        s_ncloser1._positions = [s_pos1,s_closed_pos3]
        s_ncloser2._positions = [s_pos2,s_closed_pos3]

        t_ncloser1 = Closer(None,None)
        t_ncloser2 = Closer(None,None)
        t_ccloser = ContractCloser(None,None)
        t_gcloser = GlobalCloser(None,None)
        t_pos1 = Position(self._m,LONG)
        t_pos2 = Position(self._m,LONG)

        closer_source2target = {s_ncloser1:t_ncloser1,s_ncloser2:t_ncloser2,s_ccloser:t_ccloser,s_gcloser:t_gcloser}
        pos_source2target = {s_pos1:t_pos1,s_pos2:t_pos2}
        contract_source2target = {m1305:self._m}
        pos_handler = cagent._position_holder
        self.assertIsNone(t_gcloser._position_holder)
        self.assertIsNone(t_ccloser._position_holder)
        self.assertIsNone(t_ccloser.contract)

        cp_source2target = coordinator._complete_target_closers(closer_source2target,pos_source2target,contract_source2target,pos_handler)
        #1. 已关闭列表
        self.assertEqual(1,len(pos_handler._closed_positions))
        self.assertEqual(list(cp_source2target.values())[0],pos_handler._closed_positions[0])

        self.assertEqual(1,len(cp_source2target))
        self.assertEqual(self._m,list(cp_source2target.values())[0].contract)
        self.assertEqual(m1305,list(cp_source2target.keys())[0].contract)
        #GlobalCloser
        self.assertEqual(pos_handler,t_gcloser._position_holder)
        #ContractCloser
        self.assertEqual(self._m,t_ccloser.contract)
        self.assertEqual(pos_handler,t_ccloser._position_holder)
        #普通Closer
        closed_closer = pos_handler._closed_positions[0]
        self.assertEqual([t_pos1,closed_closer],t_ncloser1._positions)
        self.assertEqual([t_pos2,closed_closer],t_ncloser2._positions)

    def test_transfer(self):
        """
            移转测试
            Agent_from:
                Pos1:   M1501   90
                Pos2:   P1501   75
            Agent_to:   P1501 =>90
                        M1501 =>75
        """
        ArgsCached._args2obj.clear()
        coordinator = self._coordinator
        self._env._contracts.clear()
        #print("---------------------------------------------")
        self._env.reset_contracts(self._cms.current_contracts(2014,3,1))
        self._env.macro_queue.trigger()
        self._env.macro_queue.trigger(time.time()+100)

        #print("agents number:",len(coordinator.agents))
        #print(coordinator.agents[0].name)

        for c in self._cms.current_contracts(2014,3,1):
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)

            self._env._contracts[c.name] = c
            self._env.get_account().api._contracts[c.name] = c
            #print(c.name,c)
        coordinator.day_finalize(20140301)
        #print(coordinator.agents[0].name,coordinator.agents[1].name)
        #print(coordinator.agents[0].name)
        self.assertEqual(1,len(coordinator.agents))
        #print(coordinator.agents[0].name)
        t1 = TICK("m1501",20140301)
        t1.common_reset()
        t1.min1 = 1401

        m_tick = BaseObject(instrument='m1501',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3006,
                         high = 99999999,low=0,
            )
        p_tick = BaseObject(instrument='p1501',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3006,
                         high = 99999999,low=0,
            )
        self._env.get_account().api.new_tick(m_tick)
        self._env.get_account().api.new_tick(p_tick)
        #self._env.query_contract_info()

        agent_from = coordinator.agents[0]
        #del coordinator._name2contract["m1409"].last_tick
        #self.assertRaises(AttributeError,getattr,coordinator._name2contract["m1501"],"last_tick")
        #self._env.query_contract_info()
        agent_from.new_tick(t1)

        m1501 = ContractInfo("m1501",1501,M)
        p1501 = ContractInfo("p1501",1501,P)
        self.assertEqual("m1501",coordinator.agents[0].contracts[0].name)
        cname = self._coordinator._contracts2name([p1501,m1501])
        agent2 = StrategyAgent(self._coordinator,[p1501,m1501])
        coordinator._contracts2agent[cname] = agent2
        self.assertEqual(2,len(agent_from.position_holder._active_positions))
        self.assertEqual(0,len(agent2.position_holder._active_positions))
        #print(agent_from.get_net_holding_volume())
        hv_src0 = agent_from.get_net_holding_volume()
        #self.assertTrue(hv_src["m1501"] > 0)
        #self.assertTrue(hv_src["p1501"] > 0)
        self.assertEqual(90,hv_src0["m1501"])
        self.assertEqual(75,hv_src0["p1501"])
        hv_target = agent2.get_net_holding_volume()
        self.assertEqual(0,hv_target["m1501"])
        self.assertEqual(0,hv_target["p1501"])

        coordinator.transfer(agent_from,agent2)

        self.assertEqual(1,len(agent_from.position_holder._active_positions))
        self.assertEqual(2,len(agent2.position_holder._active_positions))

        hv_src2 = agent_from.get_net_holding_volume()
        self.assertEqual(15,hv_src2["m1501"])
        self.assertEqual(0,hv_src2["p1501"])
        hv_target = agent2.get_net_holding_volume()
        self.assertEqual(75,hv_target["m1501"])
        self.assertEqual(90,hv_target["p1501"])

        self.assertEqual(hv_src0["m1501"],hv_target["p1501"])
        self.assertEqual(hv_src0["p1501"],hv_target["m1501"])
        #for info in self._env.get_account().api._orders:
        #    print(info)

        tapi = self._env.get_account().api
        self.assertEqual(3,len(tapi._orders))
        self.assertEqual("m1501",tapi._orders[0].InstrumentID)
        self.assertEqual(90,tapi._orders[0].VolumeTotalOriginal)
        self.assertEqual(0,int(tapi._orders[0].Direction))
        self.assertEqual(0,int(tapi._orders[0].CombOffsetFlag))
        self.assertEqual("p1501",tapi._orders[1].InstrumentID)
        self.assertEqual(75,tapi._orders[1].VolumeTotalOriginal)
        self.assertEqual(0,int(tapi._orders[1].Direction))
        self.assertEqual(0,int(tapi._orders[1].CombOffsetFlag))
        self.assertEqual("p1501",tapi._orders[2].InstrumentID)
        self.assertEqual(15,tapi._orders[2].VolumeTotalOriginal)
        self.assertEqual(0,int(tapi._orders[2].Direction))
        self.assertEqual(0,int(tapi._orders[2].CombOffsetFlag))
        #for order in tapi._orders:
        #    print(order.InstrumentID,order.VolumeTotalOriginal,order.Direction,order.CombOffsetFlag)
        self.assertEqual(1,len(agent_from.position_holder._active_positions))
        agent_from.force_close_all()
        self.assertEqual(0,len(agent_from.position_holder._active_positions))
        self.assertEqual(4,len(tapi._orders))
        self.assertEqual("m1501",tapi._orders[3].InstrumentID)
        self.assertEqual(15,tapi._orders[3].VolumeTotalOriginal)
        self.assertEqual(1,int(tapi._orders[3].Direction))
        self.assertEqual(1,int(tapi._orders[3].CombOffsetFlag))

    def test_transfer2(self):
        """
            移转测试
            Agent_from:
                Pos1:   M1501   90
                Pos2:   P1501   75
            Agent_to2:
                        M1505
                        P1505
            故全关全开
        """
        ArgsCached._args2obj.clear()
        coordinator = self._coordinator
        self._env._contracts.clear()
        #print("---------------------------------------------")
        self._env.reset_contracts(self._cms.current_contracts(2014,3,1))
        self._env.macro_queue.trigger()
        self._env.macro_queue.trigger(time.time()+100)

        for c in self._cms.current_contracts(2014,3,1):
            last_tick = TICK("XT",20120505)
            last_tick.common_reset()
            last_tick.price = 3000
            last_tick.dvolume = 100000
            last_tick.high = 3100
            last_tick.low = 2900
            #BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c.ticks.append(last_tick)
            self._env._contracts[c.name] = c
            self._env.get_account().api._contracts[c.name] = c
            #print(c.name,c)
        coordinator.day_finalize(20140301)
        self.assertEqual(1,len(coordinator.agents))
        #print(coordinator.agents[0].name)
        t1 = TICK("m1501",20140301)
        t1.common_reset()
        t1.min1 = 1401

        m_tick = BaseObject(instrument='m1501',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3006,
                         high = 99999999,low=0,
            )
        p_tick = BaseObject(instrument='p1501',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3006,
                         high = 99999999,low=0,
            )
        self._env.get_account().api.new_tick(m_tick)
        self._env.get_account().api.new_tick(p_tick)
        #self._env.query_contract_info()

        agent_from = coordinator.agents[0]
        #del coordinator._name2contract["m1409"].last_tick
        #self.assertRaises(AttributeError,getattr,coordinator._name2contract["m1501"],"last_tick")
        #self._env.query_contract_info()
        agent_from.new_tick(t1)
        self.assertEqual("m1501",coordinator.agents[0].contracts[0].name)

        m1505 = ContractInfo("m1505",1505,M)
        p1505 = ContractInfo("p1505",1505,P)
        m1505.multiple = 5
        p1505.multiple = 5
        for c in [m1505,p1505]:
            #c.last_tick = BaseObject(price=3000,dvolume=100000,high=3100,low=2900)
            c._ticks = [BaseObject(price=3000,dvolume=100000,high=3100,low=2900)]
            c._minutes = [BaseObject()] #制止resume时load data
            self._env._contracts[c.name] = c
            self._env.get_account().api._contracts[c.name] = c
        m_tick2 = BaseObject(instrument='m1505',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3006,
                         high = 99999999,low=0,
            )
        p_tick2 = BaseObject(instrument='p1505',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3006,
                         high = 99999999,low=0,
            )
        self._env.get_account().api.new_tick(m_tick2)
        self._env.get_account().api.new_tick(p_tick2)


        cname = self._coordinator._contracts2name([p1505,m1505])
        agent2 = StrategyAgent(self._coordinator,[m1505,p1505])
        #coordinator._contracts2agent[cname] = agent2
        self.assertEqual(2,len(agent_from.position_holder._active_positions))
        self.assertEqual(0,len(agent2.position_holder._active_positions))
        #print(agent_from.get_net_holding_volume())
        hv_src0 = agent_from.get_net_holding_volume()
        #self.assertTrue(hv_src["m1501"] > 0)
        #self.assertTrue(hv_src["p1501"] > 0)
        self.assertEqual(90,hv_src0["m1501"])
        self.assertEqual(75,hv_src0["p1501"])
        hv_target = agent2.get_net_holding_volume()
        self.assertEqual(0,hv_target["m1505"])
        self.assertEqual(0,hv_target["p1505"])

        #self._env.get_account().available = 1000000
        self._env.get_account().api.exchange._available += 200000   #之前保证金不足以支撑后续操作.不过这个不能直接反映到account.available

        #print("------------------available:",self._env.get_account().available)
        #print("------------------available:",self._env.get_account().api.available)
        coordinator.transfer(agent_from,agent2)

        self.assertEqual(2,len(agent_from.position_holder._active_positions))
        self.assertEqual(2,len(agent2.position_holder._active_positions))

        hv_src2 = agent_from.get_net_holding_volume()
        self.assertEqual(90,hv_src2["m1501"])
        self.assertEqual(75,hv_src2["p1501"])
        hv_target = agent2.get_net_holding_volume()
        self.assertEqual(90,hv_target["m1505"])
        self.assertEqual(75,hv_target["p1505"])

        self.assertEqual(hv_src0["m1501"],hv_target["m1505"])
        self.assertEqual(hv_src0["p1501"],hv_target["p1505"])
        #for info in self._env.get_account().api._orders:
        #    print(info)

        tapi = self._env.get_account().api
        self.assertEqual(4,len(tapi._orders))
        self.assertEqual("m1501",tapi._orders[0].InstrumentID)
        self.assertEqual(90,tapi._orders[0].VolumeTotalOriginal)
        self.assertEqual(0,int(tapi._orders[0].Direction))
        self.assertEqual(0,int(tapi._orders[0].CombOffsetFlag))
        self.assertEqual("p1501",tapi._orders[1].InstrumentID)
        self.assertEqual(75,tapi._orders[1].VolumeTotalOriginal)
        self.assertEqual(0,int(tapi._orders[1].Direction))
        self.assertEqual(0,int(tapi._orders[1].CombOffsetFlag))
        self.assertEqual("m1505",tapi._orders[2].InstrumentID)
        self.assertEqual(90,tapi._orders[2].VolumeTotalOriginal)
        self.assertEqual(0,int(tapi._orders[2].Direction))
        self.assertEqual(0,int(tapi._orders[2].CombOffsetFlag))
        self.assertEqual("p1505",tapi._orders[3].InstrumentID)
        self.assertEqual(75,tapi._orders[3].VolumeTotalOriginal)
        self.assertEqual(0,int(tapi._orders[3].Direction))
        self.assertEqual(0,int(tapi._orders[3].CombOffsetFlag))
        #for order in tapi._orders:
        #    print(order.InstrumentID,order.VolumeTotalOriginal,order.Direction,order.CombOffsetFlag)
        agent_from.force_close_all()
        self.assertEqual(0,len(agent_from.position_holder._active_positions))
        self.assertEqual(6,len(tapi._orders))
        self.assertEqual("m1501",tapi._orders[4].InstrumentID)
        self.assertEqual(90,tapi._orders[4].VolumeTotalOriginal)
        self.assertEqual(1,int(tapi._orders[4].Direction))
        self.assertEqual(1,int(tapi._orders[4].CombOffsetFlag))
        self.assertEqual("p1501",tapi._orders[5].InstrumentID)
        self.assertEqual(75,tapi._orders[5].VolumeTotalOriginal)
        self.assertEqual(1,int(tapi._orders[5].Direction))
        self.assertEqual(1,int(tapi._orders[5].CombOffsetFlag))




if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_coordinator.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()