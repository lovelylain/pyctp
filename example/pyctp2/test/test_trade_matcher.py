# -*- coding:utf-8 -*-

import logging
import unittest
import unittest.mock as mock

from ..common.base import BaseObject,TEST_PATH,LONG,SHORT,XOPEN
from ..trader.position import Order,Position
from ..trader.trade_command import (OpenInstruction,
                                    CloseInstruction,
                                    CancelInstruction,
                        )
from ..trader.strategy import PCLOSE

from ..common.contract_type import ContractInfo,CF,M,RU,P
from ..common.errors import TradeError
from ..test.test_environ import prepare_environ


class TradeMatchTestCase(unittest.TestCase):
    def setUp(self):
        self._env = prepare_environ()
        self._acc = self._env.get_account()
        self._matcher = self._env._matcher
        self._n_reject = 0
        self._n_approve = 0
        self._n_progress = 0
        self._n_done = 0

    def on_reject(self,position):
        #print("in test_matcher reject")
        self._n_reject += 1

    def on_approved(self):
        self._n_approve += 1

    def on_progress(self,position,volume,price):
        self._n_progress += 1

    def on_done(self,position,volume_traded):
        self._n_done += 1

    def test_open1(self):
        pos = Position(ContractInfo("ru1409",1409,RU),LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        instr = OpenInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        self._env.approve_open([order])
        self._matcher.execute(instr)
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(1,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(1,self._n_done)

    def test_open1_wait(self):
        pos = Position(ContractInfo("ru1409",1409,RU),LONG)
        order = Order(pos,XOPEN,15130,1,1,-30)
        instr = OpenInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        #print("in test_open1_wait..........................")
        self._env.approve_open([order])
        self._matcher.execute(instr)
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(0,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(0,self._n_done)

        #新tick驱动: 1. 不成交
        ru_tick2 = BaseObject(instrument='ru1409',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 16130,
                         high = 99999999,low=0,
                )
        self._acc.api.new_tick(ru_tick2)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(0,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(0,self._n_done)
        #新tick驱动: 2. 成交
        ru_tick2 = BaseObject(instrument='ru1409',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 14130,
                         high = 99999999,low=0,
                )
        self._acc.api.new_tick(ru_tick2)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(1,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(1,self._n_done)

    def test_open1_cancel_failure(self):
        pos = Position(ContractInfo("ru1409",RU),LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        instr = OpenInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        self._env.approve_open([order])
        self._matcher.execute(instr)
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(1,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(1,self._n_done)
        cancel_command = CancelInstruction(instr)
        self._env._matcher.execute(cancel_command)    #直接在CancelInstructi中返回,不经由api层
        self.assertEqual(0,self._acc.api.cancelled)
        self.assertEqual(0,self._acc.api.cancel_after_traded)    #直接在CancelInstructi中返回,不经由api层

    def test_cancel_failure_branch(self):
        pio = BaseObject(InstrumentID="NOT_EXIST")
        self._acc.api.ReqOrderAction(pio,0)
        self.assertEqual(1,self._acc.api.cancel_after_traded)

    def test_open1_cancel(self):
        pos = Position(ContractInfo("ru1409",RU),LONG)
        order = Order(pos,XOPEN,15130,1,1,-30)
        instr = OpenInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        #print("in test_open1_cancel..........................")
        self._env.approve_open([order])
        self._matcher.execute(instr)
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(0,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(0,self._n_done)

        #print(len(self.acc.api.wlist),self.acc.api.wlist)
        cancel_command = CancelInstruction(instr)
        self._env._matcher.execute(cancel_command)
        self.assertEqual(1,self._acc.api.cancelled)

    def test_open_ctp_reject(self):
        pos = Position(ContractInfo("XH501",1501,RU),LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        instr = OpenInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        self._env.approve_open([order])
        #print("TOR:exec")
        self._matcher.execute(instr)
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(0,self._n_progress)
        self.assertEqual(1,self._n_reject)
        self.assertEqual(0,self._n_done)

    def test_open_exchange_reject(self):
        pos = Position(ContractInfo("XX501",1501,RU),LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        instr = OpenInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        self._env.approve_open([order])
        #print("TOR:exec")
        self._matcher.execute(instr)
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(0,self._n_progress)
        self.assertEqual(1,self._n_reject)
        self.assertEqual(0,self._n_done)

    def test_open2(self):
        pos1 = Position(ContractInfo("ru1409",1409,RU),LONG)
        pos2 = Position(ContractInfo("m1501",1501,M),LONG)
        order1 = Order(pos1,XOPEN,15300,1,1,30)
        order2 = Order(pos2,XOPEN,3666,1,1,30)
        instr1 = OpenInstruction(order1,pos1)
        instr2 = OpenInstruction(order2,pos2)
        instr1.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        instr2.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        self._env.approve_open([order1,order2])
        #print("order1.approved:",order1.approved,order1.get_contract_name())
        #print("order2.approved:",order2.approved,order2.get_contract_name())
        #print(command.instructions[0].get_contract_name(),command.instructions[1].get_contract_name())
        #print("test_open2 execute:0")
        self._matcher.execute(instr1)
        self._matcher.execute(instr2)
        #print("test_open2 execute:1")
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(2,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(2,self._n_done)

    def test_close1_reject(self):
        pos = Position(ContractInfo("CF501",1501,CF),LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        instr = CloseInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        instr._order._approved = 1
        instr._order.account = 'acc1'
        #print("test_close1:execute:before....................................")
        self._matcher.execute(instr)
        #print("test_close1:execute:end..................................................")
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(0,self._n_progress)
        self.assertEqual(1,self._n_reject)
        self.assertEqual(0,self._n_done)

    def test_close1(self):
        c_cf501 = ContractInfo('CF501',1501,CF)
        pos = Position(c_cf501,LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        instr = OpenInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        self._env.approve_open([order])
        self._matcher.execute(instr)
        pos._open_orders.append(order)

        self.assertEqual(0,self._n_approve)
        self.assertEqual(1,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(1,self._n_done)

        #print("*****************next step")

        #order = Order(pos,XOPEN,SHORT,15300,1,1,30)
        cmd = PCLOSE(position=pos,base_price=15300,volume=1,extra_hops=30) #extra_hops为绝对跳差，与direction无关
        cmd.unit = 1
        cmd.planned = 1
        order = pos.add_close_order(cmd)
        instr = CloseInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        instr._order._approved = 1
        instr._order.account = 'acc1'
        #print("test_close1:execute:before....................................")
        self._matcher.execute(instr)
        #print("test_close1:execute:end..................................................")
        #print(self.n_approve,self.n_progress,self.n_reject,self.n_done)
        self.assertEqual(0,self._n_approve)
        self.assertEqual(2,self._n_progress)
        self.assertEqual(0,self._n_reject)
        self.assertEqual(2,self._n_done)

    def test_reject_other(self):
        self._matcher.on_reject("UNKNOWN",LONG,1,1,0)

    def test_time_reject(self):
        c_cf501 = ContractInfo('CF501',1501,CF)
        pos = Position(c_cf501,LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        instr = OpenInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        self._env.approve_open([order])
        self._matcher.execute(instr)
        pos._open_orders.append(order)

        #order = Order(pos,XOPEN,SHORT,15300,1,1,30)
        cmd = PCLOSE(position=pos,base_price=15300,volume=1,extra_hops=30)
        cmd.unit = 1
        cmd.planned = 1
        order = pos.add_close_order(cmd)
        instr = CloseInstruction(order,pos)
        instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
        instr._order._approved = 1
        instr._order.account = 'acc1'
        instr.trigger_time = 1201101400

        #直接hack进_wlist
        self._matcher._wlist.setdefault(self._matcher._info2key(order.contract_name,
                                             order.direction,
                                             order.approved,
                                             order.target_price,
                    ),[]).append(instr)

        self._env._tick_macro_command_queue.put_command = mock.Mock()

        self._matcher.on_reject(instr.contract_name,
                                order.direction,order.approved,order.target_price,
                                TradeError.TIME_ERROR
                            )

        mcmd = self._env._tick_macro_command_queue.put_command.call_args[0][0]
        self.assertEqual(self._matcher.execute,mcmd._target)
        self.assertEqual(instr,mcmd._params)
        self.assertEqual(1201103000,mcmd._trigger_time)

if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_trade_matcher.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()
