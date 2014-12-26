# -*-coding:utf-8 -*-

"""
    对Environ以下的基础框架进行测试, 采用最低限度的Stub
    EnvironTestCase, TradeMatchTestCase
    执行方式:
    在 ..\..路径下,即quant\下
    python -m unittest pyctp2.test.test_environ
    #ipython3 -m unittest pyctp2.test.test_environ  #速度略慢

    利用AccountStub + PassiveMacroCommandQueue + TradeCommandQueueStub + TradeApiStub的完整通道测试
    其中AccountStub + PassiveMacroCommandQueue + TradeCommandQueueStub 与 实盘共享绝大部分代码
    TradeApiStub为完整的Stub

"""

import logging
import time
import unittest
import unittest.mock as mock

from ..common.base import BaseObject,TEST_PATH,LONG,SHORT,XOPEN
from ..trader.environ import Environ
from ..common.macro_command_queue import PassiveMacroCommandQueue,DeferCommand,DeferTradeCommand
from ..test.account_stub import AccountStub
from ..trader.trade_command import (LOGIN_COMMAND,
                        )

#from ..trader.trade_command_queue import TradeCommandQueueStub
from ..trader.position import Order,Position
from ..common.contract_type import ContractInfo,CU,RU,RB,AL,M,CF,P,XX


from ..my.ports import ZSUsers

INIT_AVAILABLE = 1000000


class EnvironTestCase(unittest.TestCase):
    def setUp(self):
        self._env = prepare_environ()
        self._acc = self._env.get_account()
        #print("call once",cls.acc.trader.ctick.instrument)

    def tearDown(self):
        self._acc.api.exchange.finalize()   #关闭记录交易信息的文件

    def test_prepared(self):
        """
            测试prepare的结果, 实际上prepare中进行了一系列的调用
                A. 测试 MacroCommandQueue-->TradeCommandQueue的调用通路
                B. 执行了QueryInstrumentCommand/QueryInstrumentMarginRateCommand/QueryDepthMarketDataCommand
                C. 测试了DeferTradeCommand
                D. 测试了QueryAccountCommand
            未测试: #TODO
                A. calc_margin              #OK
                B. _which                   #OK
                C1. approve_open            #ok
                C2. _approve_one             #ok
                D. execute / matcher        #单独测试
                E. macro_command_queue      #OK

        """
        self.assertGreater(len(self._acc.api.last_tick_map),0)
        self.assertGreater(len(self._acc.api.last_tick_map),len(self._acc.api.contracts))
        self.assertEqual(list(self._acc.api.contracts.keys()).sort(),list(self._env._contracts.keys()).sort())
        self.assertEqual(INIT_AVAILABLE,self._acc.available)
        #print(EnvironTestCase.acc.trader.contracts.keys(),EnvironTestCase.env.contracts.keys())


    def test_margin(self):
        self.assertEqual(15130*10*0.1,self._env._calc_margin("ru1409",LONG,15130))
        self.assertEqual(15100*10*0.1,self._env._calc_margin("ru1409",SHORT,15100))
        #print(margin)

    def test_which(self):
        acc,amount = self._env._which(100000)
        self.assertEqual(100000,amount)
        acc,amount = self._env._which(1000000)
        self.assertEqual(1000000,amount)
        acc,amount = self._env._which(10000000)
        self.assertEqual(1000000,amount)

    def test_which2(self):
        """
            测试2个帐号
        """
        account2 = AccountStub(self._env,ZSUsers,id="acc2",available=INIT_AVAILABLE/2)
        self._env.register_account(account2)
        #print(len(self.env.account_map))
        acc,amount = self._env._which(500001)
        self.assertEqual(500001,amount)
        self.assertEqual("acc1",acc.id)
        acc.available -= 500001
        #acc1剩余499999
        acc,amount = self._env._which(500000)
        self.assertEqual(500000,amount)
        self.assertEqual("acc2",acc.id)
        acc.available -= 500000
        #acc2剩余0
        acc,amount = self._env._which(1000000)
        self.assertEqual(499999,amount)
        self.assertEqual("acc1",acc.id)
        #
        acc,amount = self._env._which(30000)
        self.assertEqual(30000,amount)
        self.assertEqual("acc1",acc.id)

    def test_mcq(self):
        it = BaseObject(v=100)
        def mc():
            it.v += 10
        mc()
        self.assertEqual(110,it.v)
        dc = DeferCommand(mc,10)
        self._env.put_macro_command(dc)
        self.assertEqual(110,it.v)
        self._env.macro_queue.trigger(time.time()+5)
        self.assertEqual(110,it.v)
        self._env.macro_queue.trigger(time.time()+11)
        self.assertEqual(120,it.v)
        #测试多个命令
        dc2 = DeferCommand(mc,100)
        dc3 = DeferCommand(mc,200)
        self._env.put_macro_command(dc2)
        self._env.put_macro_command(dc2)
        self._env.put_macro_command(dc2)
        self._env.put_macro_command(dc3)
        self._env.macro_queue.trigger(time.time()+5)
        self.assertEqual(120,it.v)
        self._env.macro_queue.trigger(time.time()+105)
        self.assertEqual(150,it.v)
        self._env.macro_queue.trigger(time.time()+205)
        self.assertEqual(160,it.v)

    def test_mcq_trade_command(self):
        tq = self._acc.trade_queue
        it = BaseObject(v=100)
        def mc():
            it.v += 10
        self.assertEqual(100,it.v)
        dc = DeferTradeCommand(tq,mc,10)
        self._env.put_macro_command(dc)
        self.assertEqual(100,it.v)
        self._env.macro_queue.trigger(time.time()+5)
        self.assertEqual(100,it.v)
        self.assertRaises(KeyError,self._env.macro_queue.trigger,time.time()+15) #在TradeCommandQuque._exec中触发
        self.assertEqual(100,it.v)
        log_dc = DeferTradeCommand(tq,LOGIN_COMMAND,10)
        self._env.put_macro_command(log_dc)
        self._env.macro_queue.trigger(time.time()+5)
        #print("TMTC:15")
        self._env.macro_queue.trigger(time.time()+15)

    def test_close_today(self):
        self.assertTrue(self._env.is_contract_CLOSETODAY("ru1409"))
        self.assertFalse(self._env.is_contract_CLOSETODAY("m1501"))
        self.assertRaises(KeyError,self._env.is_contract_CLOSETODAY,"x1501")

    def test_matcher(self):
        #只测试通道. 未测试正常的交易命令分支, 需要独立测试
        matcher= self._env.matcher
        LOGIN_COMMAND.account = self._env.get_account().id
        self._env.execute_trade_command(LOGIN_COMMAND)

    def test_approve_one(self):
        pos = Position(ContractInfo("ru1409",1409,RU),LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        self._env.approve_one(order)
        self.assertEqual(1000000-(15300+30*5)*10*0.1,self._acc.available)
        order = Order(pos,XOPEN,15300,1,1,-30)
        self._env.approve_one(order)
        self.assertEqual(1000000-(15300+30*5)*10*0.1-(15300-30*5)*10*0.1,self._acc.available)
        order._direction = SHORT
        self._env.approve_one(order)
        self.assertEqual(1000000-(15300+30*5)*10*0.1-(15300-30*5)*10*0.1*2,self._acc.available)
        self.assertEqual("acc1",order.account)

    def test_approve(self):
        pos = Position(ContractInfo("ru1409",1409,RU),LONG)
        order = Order(pos,XOPEN,15300,1,1,30)
        self._env.approve_open([order])
        self.assertEqual(1000000-(15300+30*5)*10*0.1,self._acc.available)
        self._env.approve_open([order,order,order])
        self.assertEqual(1000000-(15300+30*5)*10*0.1*4,self._acc.available)

    def test_approve_drawback(self):
        pos = Position(ContractInfo("ru1409",1409,RU),LONG)
        order = Order(pos,XOPEN,15300,30,30,30)
        self._env.approve_open([order])
        self.assertEqual(1000000-(15300+30*5)*10*0.1*30,self._acc.available)
        order2 = Order(pos,XOPEN,15300,20,20,30)
        order3 = Order(pos,XOPEN,15300,20,20,30)
        #print("TAD:before approve")
        self._env.approve_open([order2,order3])
        self.assertEqual(1000000-(15300+30*5)*10*0.1*30,self._acc.available)

    def test_instrument_status(self):
        self._env.update_instrument_status("ru",3)
        #self.assertTrue(self._env._contracts["ru1409"].status)
        self.assertEqual(3,RU.trading_status)

    def test_calc_strategy_balance(self):
        coord1 = mock.Mock()
        coord2 = mock.Mock()
        coord3 = mock.Mock()
        coord1.shares = 10
        coord2.shares = 30
        self._env._coordinators = [coord1,coord2]
        self.assertEqual(0,self._env.calc_strategy_balance(coord3))
        self.assertEqual(250000,self._env.calc_strategy_balance(coord1))
        self.assertEqual(750000,self._env.calc_strategy_balance(coord2))



def prepare_environ():
    #env = Environ(controller=controller,TickMCQ=PassiveMacroCommandQueue,SecMCQ=PassiveMacroCommandQueue)
    env = Environ(TickMCQ=PassiveMacroCommandQueue,SecMCQ=PassiveMacroCommandQueue)
    account = AccountStub(env,ZSUsers,id="acc1",available=INIT_AVAILABLE)
    #env.register_account(account)
    _prepare_contracts(env)
    return env

def _prepare_contracts(env):

    acc = env.get_account()
    prepare_ticks(acc)

    c_cu1408 = ContractInfo('cu1408',1408,CU)
    c_ru1409 = ContractInfo('ru1409',1409,RU)
    c_al1408 = ContractInfo('al1408',1408,AL)
    c_rb1410 = ContractInfo('rb1410',1410,RB)
    c_m1501 = ContractInfo('m1501',1501,M)
    c_cf501 = ContractInfo('CF501',1501,CF)
    c_p1409 = ContractInfo('p1409',1409,P)
    xerror = ContractInfo('XX501',1501,XX)
    xerror2 = ContractInfo('XH501',1501,XX)
    env.reset_contracts([c_cu1408,c_ru1409,c_al1408,c_rb1410,c_m1501,c_cf501,c_p1409,xerror,xerror2])
    env.macro_queue.trigger()
    env.macro_queue.trigger(time.time()+100)
    acc.trigger_trade_queue()


def prepare_ticks(acc):
    cu_tick = BaseObject(instrument='cu1408',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 49280,
                         high = 99999999,low=0,
            )
    ru_tick = BaseObject(instrument='ru1409',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 15130,
                         high = 99999999,low=0,
            )
    al_tick = BaseObject(instrument='al1408',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 13450,
                         high = 99999999,low=0,
            )
    rb_tick = BaseObject(instrument='rb1410',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3072,
                         high = 99999999,low=0,
            )
    m_tick = BaseObject(instrument='m1501',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 3056,
                         high = 99999999,low=0,
            )
    cf_tick = BaseObject(instrument='CF501',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 15380,
                         high = 99999999,low=0,
            )
    p_tick = BaseObject(instrument='p1409',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 5894,
                         high = 99999999,low=0,
            )
    x_tick = BaseObject(instrument='x1409',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 15894,
                         high = 99999999,low=0,
            )

    xx_tick = BaseObject(instrument='XX501',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 15380,
                         high = 99999999,low=0,
            )

    xh_tick = BaseObject(instrument='XH501',date='20140101',min1='120101',sec=59,msec=0,holding=0,damount=0,
                         time = 2014010112010159,
                         price = 15380,
                         high = 99999999,low=0,
            )

    ticks = [cu_tick,ru_tick,al_tick,rb_tick,m_tick,cf_tick,p_tick,x_tick,xx_tick,xh_tick]
    for tick in ticks:
       acc.api.new_tick(tick)

if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_environ.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()
