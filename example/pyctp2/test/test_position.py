#-*- coding:utf-8 -*-

import logging
import time
import unittest
import unittest.mock as mock

from ..common.base import (
                XOPEN,XCLOSE,XCLOSE_TODAY,
                LONG,SHORT,
                BaseObject,
                TEST_PATH,
                MAX_VALUE,
            )
from ..common.contract_type import ContractInfo as ci,M,P
from ..common.cjson import dumps,loads

from ..trader.strategy import POPEN,PCLOSE

from ..trader.position import (
                Order,
                Position,
                PosInfo,
                PositionHolder,
                Closer,ContractCloser,GlobalCloser,
                LongCloserParameter1,
                ORDER_STATUS,

        )


class OrderTestCase(unittest.TestCase):
    def setUp(self):
        self._contract = ci('m1501',1501,M)
        self._pos = Position(self._contract,LONG)

    def tearDown(self):
        pass

    def test_base(self):
        order = Order(self._pos,XOPEN,3500,1,1,30)
        order.approve(10,350000)
        order.trigger_time = 100 #测试通道
        self.assertEqual(ORDER_STATUS.INITIALIZED,order._state)
        self.assertEqual(10,order.approved)
        self.assertEqual(self._contract._name,order.contract_name)
        self.assertEqual(self._contract,order.contract)
        self.assertEqual([],order._details)

    def test_calc_margin(self):
        order = Order(self._pos,XOPEN,3500,1,1,30)
        order.target_price = 3530
        self._pos.contract.long_marginrate = 0.1
        self._pos.contract.multiple = 50
        self.assertTrue(abs(17650-order.calc_margin()) < 0.001)

    def test_accomplished(self):
        order = Order(self._pos,XOPEN,3500,1,1,30)
        order._accomplished = 1
        self.assertEqual(1,order.true_accomplished)
        order._accomplished2 = 2
        self.assertEqual(2,order.true_accomplished)

    def test_part_accomplished(self):
        order = Order(self._pos,XOPEN,3500,1,1,30)
        self.assertEqual(0,order.accomplished)
        self.assertEqual(0,order.accomplished2)
        self.assertEqual(0,order.transfered)
        order.part_accomplished(10)
        self.assertEqual(10,order.accomplished)
        self.assertEqual(10,order.accomplished2)
        self.assertEqual(10,order.transfered)

    def test_isdone(self):
        order = Order(self._pos,XOPEN,3500,1,1,30)
        order._state = ORDER_STATUS.ACCEPT
        self.assertEqual(False,order.done)
        order._state = ORDER_STATUS.REJECT
        self.assertEqual(True,order.done)
        order._state = ORDER_STATUS.CANCELLED
        self.assertEqual(True,order.done)
        order._state = ORDER_STATUS.PART_SUCCESSED
        self.assertEqual(True,order.done)
        order._state = ORDER_STATUS.SUCCESSED
        self.assertEqual(True,order.done)

    def test_on_reject(self):
        order = Order(self._pos,XOPEN,3500,1,1,30)
        self.assertEqual(False,order.done)
        order.on_reject()
        self.assertEqual(True,order.done)

    def test_on_progress(self):
        order = Order(self._pos,XOPEN,3500,2,2,30)
        order.approve(2,70000)
        self.assertEqual(0,order._accomplished)
        order.on_progress(1,3501)
        self.assertEqual(1,order._accomplished)
        self.assertEqual(1,len(order._details))
        self.assertEqual(1,order._details[0].volume)
        self.assertEqual(3501,order._details[0].price)
        self.assertRaises(AssertionError,order.on_progress,2,3501)
        order.on_progress(1,3502)
        self.assertEqual(2,order._accomplished)
        self.assertEqual(2,len(order._details))
        self.assertEqual(1,order._details[-1].volume)
        self.assertEqual(3502,order._details[-1].price)

    def test_on_done(self):
        order = Order(self._pos,XOPEN,3500,2,2,30)
        self.assertRaises(AssertionError,order.on_done,2)
        order.approve(2,70000)
        order.on_done(2)
        self.assertEqual(2,order._accomplished2)
        self.assertEqual(ORDER_STATUS.SUCCESSED,order._state)

    def test_on_done_cancelled(self):
        order2 = Order(self._pos,XOPEN,3500,2,2,30)
        order2.approve(2,70000)
        order2.on_done(1)
        self.assertEqual(1,order2._accomplished2)
        self.assertEqual(ORDER_STATUS.CANCELLED,order2._state)

    def test_on_done_part_success(self):
        order = Order(self._pos,XOPEN,3500,2,2,30)
        order.approve(2,70000)
        order.on_progress(1,3501)
        order.on_done(1)
        self.assertEqual(1,order._accomplished2)
        self.assertEqual(ORDER_STATUS.PART_SUCCESSED,order._state)

    def test_on_the_flying(self):
        order = Order(self._pos,XOPEN,3500,2,2,30)
        order.approve(2,80000)
        self.assertEqual(2,order.volume_on_the_flying)
        order.on_done(1)
        self.assertEqual(1,order.volume_on_the_flying)

class CloserTestCase(unittest.TestCase):
    def test_closer_func1(self):
        func1 = mock.Mock()

        closer = Closer(func1,LongCloserParameter1)
        closer.prepare([BaseObject()])
        closer.check(BaseObject(),[BaseObject()])
        self.assertTrue(True)

    def test_closer_func2(self):
        func2 = mock.Mock()

        closer = Closer(func2,LongCloserParameter1())
        closer.prepare([BaseObject(),BaseObject()])
        closer.check(BaseObject(),BaseObject(),[BaseObject()])
        self.assertTrue(True)

    def test_closer_dump(self):
        contract = ci('m1501',1501,M)
        pos = Position(contract,LONG)
        pos2 = Position(contract,LONG)
        closer = Closer(pos.add_close_order,LongCloserParameter1())
        closer.prepare([pos,pos2])
        cs=dumps(closer)
        rcs = loads(cs)
        self.assertEqual("add_close_order",rcs.close_func_name)
        #print(cs)

    def test_id(self):
        contract = ci('m1501',1501,M)
        pos = Position(contract,LONG)
        closer = Closer(pos.add_close_order,LongCloserParameter1())
        closer2 = Closer(pos.add_close_order,LongCloserParameter1())
        self.assertEqual(closer._id+1,closer2._id)

        func1 = mock.Mock()
        closer3 = ContractCloser(func1,LongCloserParameter1)
        self.assertEqual(closer._id+2,closer3._id)

        func2 = mock.Mock()

        closer4 = GlobalCloser(func2,LongCloserParameter1)
        self.assertEqual(closer._id+3,closer4._id)

    def test_calc_target_price(self):
        contract = BaseObject(upperlimit_price=3000,lowerlimit_price=2500,price_tick=2)
        #direction=LONG
        self.assertEqual(3000,Order.calc_target_price(contract,LONG,2800,MAX_VALUE))
        self.assertEqual(2500,Order.calc_target_price(contract,LONG,2800,-MAX_VALUE))
        self.assertEqual(2860,Order.calc_target_price(contract,LONG,2800,30))
        self.assertEqual(2740,Order.calc_target_price(contract,LONG,2800,-30))
        self.assertEqual(3000,Order.calc_target_price(contract,LONG,2800,200))
        self.assertEqual(2500,Order.calc_target_price(contract,LONG,2800,-200))
        #direction=SHORT
        self.assertEqual(2500,Order.calc_target_price(contract,SHORT,2800,MAX_VALUE))
        self.assertEqual(3000,Order.calc_target_price(contract,SHORT,2800,-MAX_VALUE))
        self.assertEqual(2740,Order.calc_target_price(contract,SHORT,2800,30))
        self.assertEqual(2860,Order.calc_target_price(contract,SHORT,2800,-30))
        self.assertEqual(2500,Order.calc_target_price(contract,SHORT,2800,200))
        self.assertEqual(3000,Order.calc_target_price(contract,SHORT,2800,-200))



class ContractCloserTestCase(unittest.TestCase):
    def setUp(self):
        self._pholder = BaseObject(get_volume_holding=lambda x:10)

    def test_closer_func(self):
        func1 = mock.Mock()

        contract = ci('m1501',1501,M)
        closer = ContractCloser(func1,LongCloserParameter1)
        closer.prepare(self._pholder,contract)
        closer.check(BaseObject(),BaseObject(),[BaseObject()])
        closer.check(BaseObject(),BaseObject(),[BaseObject(),BaseObject()])
        self.assertTrue(True)

    def test_closer_dump(self):
        contract = ci('m1501',1501,M)
        pos = Position(contract,LONG)
        closer = ContractCloser(pos.add_close_order,LongCloserParameter1())
        closer.prepare(self._pholder,contract)
        cs=dumps(closer)
        rcs = loads(cs)
        self.assertEqual("add_close_order",rcs.close_func_name)
        #print(cs)

class GlobalCloserTestCase(unittest.TestCase):
    def setUp(self):
        self._pholder = BaseObject(name2positions=[10,20])

    def test_closer_func(self):
        func1 = mock.Mock()

        closer = GlobalCloser(func1,LongCloserParameter1)
        closer.prepare(self._pholder)
        closer.check(BaseObject(),BaseObject(),[BaseObject()])
        closer.check(BaseObject(),BaseObject(),[BaseObject(),BaseObject()])
        self.assertTrue(True)

    def test_closer_dump(self):
        func1 = mock.Mock()

        contract = ci('m1501',1501,M)
        pos = Position(contract,LONG)
        closer = GlobalCloser(pos.add_close_order,LongCloserParameter1())
        #closer = GlobalCloser(func1,LongCloserParameter())
        closer.prepare(self._pholder)
        cs=dumps(closer)
        rcs = loads(cs)
        self.assertEqual("add_close_order",rcs.close_func_name)
        #print(closer.close_func)


class PositionTestCase(unittest.TestCase):
    def setUp(self):
        self._contract = ci('m1501',1501,M)
        self._contract._trading_day = 20141232
        self._pos = Position(self._contract,LONG)
        cc = mock.Mock()
        cc.__name__ = "TEST_MOCK"

        closer1 = Closer(cc,None)
        closer2 = ContractCloser(cc,None)
        closer3 = GlobalCloser(cc,None)
        self._popen = POPEN(self._contract,3650,LONG,[closer1,closer2,closer3],30)
        self._popen.unit = self._popen.planned = 1
        self._popen.direction = LONG
        self._open_order = self._pos.add_open_order(self._popen)
        self._open_order._approved = 1
        self._open_order._trade_info=BaseObject(trading_day = 20100101)
        self._pclose = PCLOSE(self._pos,base_price=3650,volume=2,extra_hops=30)
        self._pclose.unit = self._pclose.planned = 1

    def test_open_direction(self):
        pos = Position(self._contract,LONG)
        popen = POPEN(self._contract,3650,SHORT,[1,2,3],30)
        popen.unit = popen.planned = 1
        self.assertRaises(AssertionError,pos.add_open_order,popen) #方向不一致

    def test_open_orders(self):
        order = self._open_order
        self.assertEqual(self._pos,order.position)
        self.assertEqual(XOPEN,order.atype)
        self.assertEqual(self._pos._direction,order.direction)
        self.assertEqual(self._popen.base_price,order.base_price)
        self.assertEqual(self._popen.unit,order.unit)
        self.assertEqual(self._popen.planned,order.planned)
        self.assertEqual(self._popen.extra_hops,order.extra_hops)
        #不能有第二个open_order
        self.assertRaises(AssertionError,self._pos.add_open_order,self._popen)
        open_order = self._pos.open_order
        self.assertEqual(order,open_order)

    def test_close_order(self):
        close_order = self._pos.add_close_order(self._pclose)
        self.assertEqual(XCLOSE,close_order.atype)
        close_order._approved = 1
        self.assertEqual(1,len(self._pos._close_orders))
        self.assertRaises(AssertionError,self._pos.add_close_order,self._pclose)  #超过持仓
        self.assertEqual(1,len(self._pos._close_orders))
        self.assertEqual(close_order,self._pos._close_orders[-1])
        close_order._state = ORDER_STATUS.SUCCESSED
        close_order2 = self._pos.add_close_order(self._pclose)    #未超过持仓,因为成功后,close_order.accomplished2=0
        self.assertEqual(2,len(self._pos._close_orders))
        self.assertEqual(close_order2,self._pos._close_orders[-1])
        close_order._accomplished2 = 1
        self.assertRaises(AssertionError,self._pos.add_close_order,self._pclose)  #超过持仓

    def test_close_order_today(self):
        self._contract._trading_day = self._open_order.trade_info.trading_day
        close_order = self._pos.add_close_order(self._pclose)
        self.assertEqual(XCLOSE_TODAY,close_order.atype)

    def test_check_closed(self):
        #check_closed
        self.assertFalse(self._pos.check_closed())
        self._open_order._state = ORDER_STATUS.SUCCESSED
        self.assertTrue(self._pos.check_closed())
        self._pos._closed = False
        self._open_order._accomplished2 = 1
        self.assertFalse(self._pos.check_closed())
        #closed
        close_order = self._pos.add_close_order(self._pclose)
        self.assertFalse(self._pos.check_closed())
        close_order._approved = 1
        self.assertFalse(self._pos.check_closed())
        close_order._accomplished2 = 1
        self.assertTrue(self._pos.check_closed())

    def test_check_closed2(self):
        #check_closed
        self.assertFalse(self._pos.check_closed())
        self._open_order._state = ORDER_STATUS.SUCCESSED
        self.assertTrue(self._pos.check_closed())
        self._pos._closed = False
        self._open_order._approved = self._open_order._accomplished2 = 2
        self.assertFalse(self._pos.check_closed())
        #closed
        close_order = self._pos.add_close_order(self._pclose)
        self.assertFalse(self._pos.check_closed())
        close_order._approved = 1
        self.assertFalse(self._pos.check_closed())
        close_order._accomplished2 = 1
        self.assertFalse(self._pos.check_closed())
        close_order2 = self._pos.add_close_order(self._pclose)
        self.assertFalse(self._pos.check_closed())
        close_order2._accomplished2 = 1
        self.assertTrue(self._pos.check_closed())

    def test_get_on_the_flying(self):       #通路测试
        self.assertEqual(1,self._pos._get_on_the_flying(self._pos._open_orders))
        self._pos._open_orders.append(self._pos._open_orders[0])
        self.assertEqual(2,self._pos._get_on_the_flying(self._pos._open_orders))

    def test_get_approved(self):        #通路测试
        self.assertEqual(1,self._pos._get_approved(self._pos._open_orders))
        self._pos._open_orders.append(self._pos._open_orders[0])
        self.assertEqual(2,self._pos._get_approved(self._pos._open_orders))

    def test_get_accomplished2(self):       #通路测试
        self.assertEqual(0,self._pos._get_accomplished2(self._pos._open_orders))
        self._pos._open_orders.append(self._pos._open_orders[0])
        self.assertEqual(0,self._pos._get_accomplished2(self._pos._open_orders))
        self._open_order._accomplished2 = 1
        self.assertEqual(2,self._pos._get_accomplished2(self._pos._open_orders))

    def test_get_holding_volume(self):      #通路测试
        self.assertEqual(1,self._pos.volume_holding)

    def test_get_approved_volume(self):     #通路测试
        self.assertEqual(1,self._pos.volume_approved)

    def test_get_accomplished2_volume(self):     #通路测试
        self.assertEqual(0,self._pos.volume_accomplished2)
        self._open_order._accomplished2 = 1
        self.assertEqual(1,self._pos.volume_accomplished2)

    def test_dumps_loads(self):
        stxt = dumps(self._pos)
        #print(stxt)
        pos = loads(stxt)
        self.assertEqual(self._pos._contract.name,pos.contract.name)
        self.assertEqual(type(self._pos._contract.ctype),type(pos.contract.ctype))
        self.assertEqual(len(self._pos._closers),len(pos.closers))
        sst = [type(c) for c in self._pos._closers]
        for s in pos.closers:
            self.assertTrue(type(s) in sst)
        self.assertEqual(self._pos._open_orders[0].unit,pos.open_orders[0].unit)
        self.assertEqual(self._pos._open_orders[0].planned,pos.open_orders[0].planned)
        self.assertEqual(self._pos._open_orders[0].approved,pos.open_orders[0].approved)
        self.assertEqual(self._pos._open_orders[0].base_price,pos.open_orders[0].base_price)
        self.assertEqual(len(self._pos._close_orders),len(pos.close_orders))


class PosInfoTestCase(unittest.TestCase):#被间接测试
    def test_pos_info(self):
        pinfo = PosInfo("ctest",10,5)
        self.assertEqual(10,pinfo._num_long)
        self.assertEqual(5,pinfo._num_short)
        self.assertEqual(15,pinfo.total)
        self.assertEqual(5,pinfo.net)
        pinfo.add_short(11)
        self.assertEqual(16,pinfo._num_short)
        pinfo.add_long(11)
        self.assertEqual(21,pinfo._num_long)
        self.assertEqual(37,pinfo.total)
        self.assertEqual(5,pinfo.net)

    def test_add(self):
        pinfo = PosInfo("ctest",10,5)
        pother = PosInfo("ctest",1,3)
        pinfo.add(pother)
        self.assertEqual(11,pinfo._num_long)
        self.assertEqual(8,pinfo._num_short)
        self.assertEqual(19,pinfo.total)
        self.assertEqual(3,pinfo.net)
        pother2 = PosInfo("ctest2",0,1)
        self.assertRaises(AssertionError,pinfo.add(pother))


class PositionHolderTestCase(unittest.TestCase):
    def setUp(self):
        self._contract_m = ci('m1501',1501,M)
        self._contract_p = ci('p1501',1501,P)
        self._contract_m._trading_day = 20141232
        self._contract_p._trading_day = 20141232
        pos1 = Position(self._contract_m,LONG)
        pos2 = Position(self._contract_m,LONG)
        pos3 = Position(self._contract_p,LONG)

        cc = mock.Mock()
        cc.__name__ = "TEST_MOCK"
        closer1 = Closer(cc,LongCloserParameter1())
        closer2 = ContractCloser(cc,None)
        closer3 = GlobalCloser(cc,None)

        self._poses = [pos1,pos2,pos3]
        popen1 = POPEN(self._contract_m,3650,LONG,[closer1,closer2,closer3],30)
        popen1.unit = popen1.planned = 1
        popen1.direction = LONG
        open_order1 = pos1.add_open_order(popen1)
        open_order1._approved = 1
        open_order1._trade_info=BaseObject(trading_day = 20100101)

        closer1_2 = Closer(cc,LongCloserParameter1())
        closer2_2 = ContractCloser(cc,None)
        closer3_2 = GlobalCloser(cc,None)
        popen2 = POPEN(self._contract_m,3650,LONG,[closer1_2,closer2_2,closer3_2],30)
        popen2.unit = popen2.planned = 1
        popen2.direction = LONG

        open_order2 = pos2.add_open_order(popen2)
        open_order2._approved = 2
        open_order2._trade_info=BaseObject(trading_day = 20100101)

        closer1_3 = Closer(cc,LongCloserParameter1())
        closer2_3= ContractCloser(cc,None)
        closer3_3 = GlobalCloser(cc,None)

        popen3 = POPEN(self._contract_p,3650,SHORT,[closer1_3,closer2_3,closer3_3],30)
        popen3.unit = popen3.planned = 1
        popen3.direction = LONG
        open_order3 = pos3.add_open_order(popen3)
        open_order3._approved = 1
        open_order3._trade_info=BaseObject(trading_day = 20100101)
        #self.pclose = PCLOSE(self.pos1,base_price=3650,volume=2,extra_hops=30)
        #self.pclose.wanted = self.pclose.planned = 1

    def test_base(self):
        pholder = PositionHolder()
        self.assertEqual(1,pholder._max_position_id)
        self.assertEqual(2,pholder.inc_position_id())
        self.assertEqual(2,pholder._max_position_id)

    def test_check_consistency(self):
        pholder = PositionHolder()
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:])
        self.assertTrue(pholder.check_consistency())
        pos4 = Position(self._contract_m,LONG)
        #测试 active_positions中position也必须在name2position中出现
        pholder._active_positions.append(pos4)
        self.assertRaises(AssertionError,pholder.check_consistency)
        del pholder._active_positions[3]
        self.assertTrue(pholder.check_consistency())
        # 测试name2position中的position必须在active_position中出现
        pholder._name2positions[pos4._contract.name].append(pos4)
        self.assertRaises(AssertionError,pholder.check_consistency)

    def test_add_positions(self):
        """
            测试 add_positions/_add_position/_fill_closer
                为半通道测试
        """
        pholder = PositionHolder()
        pholder.add_positions(self._poses[0:1])
        self.assertEqual(1,len(pholder._active_positions))
        self.assertEqual(1,len(pholder._name2positions))
        self.assertEqual(self._poses[0],pholder._active_positions[0])
        self.assertEqual(self._poses[0],pholder._name2positions[self._poses[0]._contract.name][0])
        pholder.add_positions(self._poses[1:])
        self.assertEqual(3,len(pholder._active_positions))
        self.assertEqual(2,len(pholder._name2positions))
        self.assertEqual(self._poses[2],pholder._active_positions[2])
        self.assertEqual([self._poses[0],self._poses[1]],pholder._name2positions[self._poses[0]._contract.name])
        self.assertEqual(self._poses[2],pholder._name2positions[self._poses[2]._contract.name][0])

    def test_add_positions_failed(self):
        pholder = PositionHolder()
        self.assertRaises(AssertionError,pholder.add_positions,self._poses[0:2])      #同个Contract不能同时发出多个Position

    def test_on_order_done(self):
        pholder = PositionHolder()
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:])
        self.assertEqual(3,len(pholder._active_positions))
        self.assertEqual(2,len(pholder._name2positions))
        self.assertEqual([self._poses[0],self._poses[1]],pholder._name2positions[self._poses[0]._contract.name])
        self._poses[0]._open_orders[0]._approved=0
        self.assertTrue(self._poses[0].check_closed())
        pholder.on_order_done(self._poses[0])
        self.assertEqual(2,len(pholder._active_positions))
        self.assertEqual(2,len(pholder._name2positions))
        self.assertEqual([self._poses[1]],pholder._name2positions[self._poses[0]._contract.name])
        self.assertEqual(1,len(pholder._closed_positions))
        pholder.to_dict()           #closed position
        self.assertTrue(True)       #顺利到达

    def test_get_by_name(self):
        pholder = PositionHolder()
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:])
        poses1 = pholder.get_positions_by_name("m1501")
        poses2 = pholder.get_positions_by_name("p1501")
        self.assertEqual(2,len(poses1))
        self.assertEqual(1,len(poses2))
        self.assertEqual([self._poses[0],self._poses[1]],poses1)
        self.assertEqual([self._poses[2]],poses2)

    def test_get_holding_volume(self):      #通道测试
        pholder = PositionHolder()
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:])
        hvs = pholder.get_volume_holding("m1501")
        self.assertEqual(3,hvs)
        hvs2 = pholder.get_volume_holding("p1501")
        self.assertEqual(1,hvs2)

    def test_get_approved_volume(self):     #通道测试
        pholder = PositionHolder()
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:])
        hvs = pholder.get_volume_approved("m1501")
        self.assertEqual(3,hvs)
        hvs2 = pholder.get_volume_approved("p1501")
        self.assertEqual(1,hvs2)
        self._poses[0]._open_orders[0]._approved = 0
        self._poses[1]._open_orders[0]._approved = 1
        hvs3 = pholder.get_volume_approved("m1501")
        self.assertEqual(1,hvs3)


    def test_get_holding_info(self):      #通道测试
        pholder = PositionHolder()

        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:2])
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:2])

        #pholder.add_positions(self.poses[0:1])

        hvs = pholder.get_volume_holding("m1501")
        self.assertEqual(6,hvs)

        pinfo = pholder.get_holding_info("m1501")
        self.assertEqual(6,pinfo.total)
        self.assertEqual(6,pinfo.net)
        self.assertEqual(6,pinfo.num_long)
        self.assertEqual(0,pinfo.num_short)

        #这个只是了解了内部实现逻辑之后的临时设定, 在pos内部是不和谐的,但测试够用
        self._poses[1]._direction = SHORT
        pinfo = pholder.get_holding_info("m1501")
        self.assertEqual(6,pinfo.total)
        self.assertEqual(-2,pinfo.net)
        self.assertEqual(2,pinfo.num_long)
        self.assertEqual(4,pinfo.num_short)

        self._poses[1]._open_orders[0]._approved = 1
        pinfo = pholder.get_holding_info("m1501")
        self.assertEqual(4,pinfo.total)
        self.assertEqual(0,pinfo.net)
        self.assertEqual(2,pinfo.num_long)
        self.assertEqual(2,pinfo.num_short)


    def test_get_approved_info(self):     #通道测试
        pholder = PositionHolder()

        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:2])
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:2])

        #pholder.add_positions(self.poses[0:1])

        hvs = pholder.get_volume_approved("m1501")
        self.assertEqual(6,hvs)

        pinfo = pholder.get_approved_info("m1501")
        self.assertEqual(6,pinfo.total)
        self.assertEqual(6,pinfo.net)
        self.assertEqual(6,pinfo.num_long)
        self.assertEqual(0,pinfo.num_short)

        #这个只是了解了内部实现逻辑之后的临时设定, 在pos内部是不和谐的,但测试够用
        self._poses[1]._direction = SHORT
        pinfo = pholder.get_approved_info("m1501")
        self.assertEqual(6,pinfo.total)
        self.assertEqual(-2,pinfo.net)
        self.assertEqual(2,pinfo.num_long)
        self.assertEqual(4,pinfo.num_short)


    def test_to_dict(self):     #通道测试
        pholder = PositionHolder()
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:])
        sdict = pholder.to_dict()
        self.assertTrue(True)
        stxt = dumps(pholder)
        self.assertTrue(True)
        #print(stxt)
        ##测试closed_position
        self._poses[0]._open_orders[0]._approved = 0
        pholder.on_order_done(self._poses[0])
        self.assertEqual(1,len(pholder._closed_positions))
        sdict = pholder.to_dict()
        stxt = dumps(pholder)
        self.assertTrue(True)


    def test_serialize(self):
        pholder = PositionHolder()
        pholder.add_positions(self._poses[0:1])
        pholder.add_positions(self._poses[1:])

        #print(list(pholder.active_positions[1].closers)[0].positions)
        stxt = dumps(pholder)
        #print(stxt)
        pholder2 = loads(stxt)
        self.assertEqual(3,len(pholder2.active_positions))
        self.assertEqual(2,len(pholder2.name2positions))
        self.assertEqual(self._poses[0]._contract.name,pholder2.active_positions[0].contract.name)
        #print(id(self.poses[0]),id(pholder2.active_positions[0]))
        self.assertEqual(pholder2.get_positions_by_name("m1501")[0],pholder2.active_positions[0])
        self.assertEqual(pholder2.get_positions_by_name("m1501")[1],pholder2.active_positions[1])
        self.assertEqual(pholder2.get_positions_by_name("p1501")[0],pholder2.active_positions[2])
        for closer in pholder2.active_positions[0].closers:
            if isinstance(closer,Closer):
                self.assertEqual(pholder2.active_positions[0],closer._positions[0])
                self.assertEqual(1,len(closer._positions))
            else:
                self.assertEqual(pholder2,closer._position_holder)

        for closer in pholder2.active_positions[1].closers:
            if isinstance(closer,Closer):
                self.assertEqual(pholder2.active_positions[1],closer._positions[0])
                self.assertEqual(pholder2.active_positions[2],closer._positions[1])
                self.assertEqual(2,len(closer._positions))
            else:
                self.assertEqual(pholder2,closer._position_holder)

        #测试 close_positions通道
        self.assertEqual(0,len(pholder._closed_positions))
        self._poses[0]._open_orders[0]._approved = 0
        pholder.on_order_done(self._poses[0])
        self.assertEqual(1,len(pholder._closed_positions))
        stxt2 = dumps(pholder)
        #print(stxt2)
        pholder3 = loads(stxt2)
        #self.assertEqual(1,len(pholder3.closed_positions))
        #self.assertEqual(pholder._closed_positions[0].contract.name,pholder3.closed_positions[0].contract.name)
        #self.assertEqual(pholder._closed_positions[0].open_orders[0].base_price,pholder3.closed_positions[0].open_orders[0].base_price)
        #elf.assertEqual(pholder._closed_positions[0].open_orders[0].approved,pholder3.closed_positions[0].open_orders[0].approved)


if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_position.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()
