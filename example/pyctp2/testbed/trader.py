# -*- coding:utf-8 -*-
"""
    对SPI的底层通路测试: 实盘
    所以只能是手工测试,不能自动化

    #TODO @20140604:
    已确认:
        郑商 对今仓采用平仓无措, 对平昨用平今/平仓均可
        上期的平昨工作OK

import pyctp2.testbed.trader as trader
import pyctp2.trader.trade_command as tc
t = trader.create_trader()
输入用户名:
输入登陆口令:

a = t.get_account()
cu1408 = tc.QueryInstrumentCommand('cu1408a')
a.trade_queue.put_command(cu1408)

from pyctp2.common.contract_type import ContractInfo as ci,CU,RU,RB,AL

c_cu1408 = ci('cu1408',CU)
c_ru1409 = ci('ru1409',RU)
c_al1408 = ci('al1408',AL)


c_cu1408 = ci('cu1408',CU)
c_ru1409 = ci('ru1409',RU)
t.reset_contracts([c_cu1408,c_ru1409,al1408])

cu1408 = tc.QueryInstrumentCommand('cu1408')
ru1409 = tc.QueryInstrumentCommand('ru1409')

a.trade_queue.put_command(cu1408)
a.trade_queue.put_command(ru1409)   #测试流控与macro_command_queue

a.spi.infos
a.spi.infos[1].getval('ProductClass')   #测试enum的有效性

ru1409a = tc.QueryInstrumentMarginRateCommand('ru1409')
a.trade_queue.put_command(ru1409a)
str(a.spi.infos[-1])

t.contracts['ru1409'].__dict__

#或者:
c_cu1408 = ci('cu1408',CU)
c_ru1409 = ci('ru1409',RU)
c_rb1409 = ci('rb1409',RB)
t.reset_contracts([c_cu1408,c_ru1409,c_rb1409])
t.query_contract_info()
"""

import logging
from ..trader.account import Account
from ..trader.environ import Environ

from ..my.ports import ZSTraders
from ..common.base import INFO_PATH,XCLOSE_TODAY,XCLOSE,LONG,SHORT
from pyctp2.trader.trade_command import *

def create_trader(ports=ZSTraders):
    """
import pyctp2.testbed.trader as trader
import pyctp2.trader.trade_command as tc
t = trader.create_trader()

a = t.get_account()
from pyctp2.common.contract_type import ContractInfo as ci,CU,RU,RB,AL
from pyctp2.common.base import LONG,SHORT
from pyctp2.trader.trade_command import *

c_cu1408 = ci('cu1408',CU)
c_ru1409 = ci('ru1409',RU)
c_al1408 = ci('al1408',AL)
c_rb1410 = ci('rb1410',RB)
t.reset_contracts([c_cu1408,c_ru1409,c_al1408,c_rb1410])

t.contracts['ru1409'].__dict__
t.contracts['al1408'].__dict__
t.contracts['rb1410'].__dict__

ta = t.calc_target_price('al1408',LONG,13420,-30)   #-30跳挂买单

#开仓
#a.spi.xopen('al1408',LONG,ta,1)    #直接开仓
    """
    logging.basicConfig(filename="%s/ctp_trade.log" % (INFO_PATH, ),
                        level=logging.DEBUG,
                        format="%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s"
                        )
    env = Environ()
    account = Account(env,ports)
    return env


def tprepare():
    """

    #撤单,须验证OrderRef,OrderActionRef哪个起作用
        """
    from ..trader import trade_command as tc
    env = create_trader()

    a = env.get_account()
    from pyctp2.common.contract_type import ContractInfo as ci,CU,RU,RB,AL,M,CF,P
    from pyctp2.common.base import LONG,SHORT


    c_cu1408 = ci('cu1410',CU)
    c_ru1409 = ci('ru1501',RU)
    c_al1408 = ci('al1410',AL)
    c_rb1410 = ci('rb1501',RB)
    c_m1501 = ci('m1501',M)
    c_cf501 = ci('CF501',CF)
    c_p1409 = ci('p1501',P)
    env.reset_contracts([c_cu1408,c_ru1409,c_al1408,c_rb1410,c_m1501,c_cf501,c_p1409])
    return env

def test_info(env):
    print(env.contracts['ru1409'].__dict__)
    print(env.contracts['rb1410'].__dict__)

def test_open1(env):
    """
        开仓悬挂分支测试
        察看 env.get_account().spi.infos[-1]中的pOrder的相关参数
        #未测试开仓成功分支
    """
    a = env.get_account()
    ta = env.calc_target_price('al1410',LONG,13420,-30)   #-30跳挂买单,以避免成交
    a.spi.xopen('al1410',LONG,ta,1)    #直接开仓

def test_open3(env):
    """
        开仓悬挂分支测试
        察看 env.get_account().spi.infos[-1]中的pOrder的相关参数
        #未测试开仓成功分支
    """
    a = env.get_account()
    ta = env.calc_target_price('al1408',SHORT,13420,30)   #反向30跳挂卖单,以避免成交
    a.spi.xopen('al1408',SHORT,ta,1)    #直接开仓


def test_cancel(env,pOrder = None):
    """
        order_info是 需要撤单的那个Order的 on_rtn_order的返回响应
        #撤单,须验证OrderRef,OrderActionRef哪个起作用
        pyctp1中,OrderRef是撤的那个Order的Ref, OrderActionRef是这个撤单Order的Ref
        instrument_id,exchange_id,order_sys_id,front_id,session_id,order_ref

        a = env.get_account()
        trader.test_cancel(env,a.spi.infos[-1])
    """
    a = env.get_account()
    #a.spi.xcancel(pOrder.InstrumentID,pOrder.ExchangeID,pOrder.OrderSysID,pOrder.FrontID,pOrder.SessionID,pOrder.OrderRef)
    #a.spi.xcancel("al1408","SHFE",'      871218',2,1557989959,'10028')  #OrderSysID中6个空格很重要
    a.spi.xcancel("al1408","SHFE",'       94888',0,0,None)  #OrderSysID中前导空格很重要, 一共是12个字节
    #a.spi.xcancel("al1408",None,None,2,-637533005,10034)  #OrderSysID中6个空格很重要, 一共是12个字节
    #需肉眼判断撤单是否成功

def test_open2(env):
    """
        开仓成功分支,测试通路
        察看 env.get_account().spi.infos[-1]中的pOrder的相关参数
    """
    a = env.get_account()
    ta = env.calc_target_price('al1408',LONG,13380,0)   #30跳挂买单,以成交
    a.spi.xopen('al1408',LONG,ta,1)    #直接开仓

def test_open2s(env):
    """
        开仓成功分支,测试通路
        察看 env.get_account().spi.infos[-1]中的pOrder的相关参数
    """
    a = env.get_account()
    ta = env.calc_target_price('al1408',SHORT,13385,0)   #30跳挂买单,以成交
    a.spi.xopen('al1408',SHORT,1,ta)    #直接开仓


def test_open22(env):
    """
        开仓成功分支,测试通路
        m1501
        察看 env.get_account().spi.infos[-1]中的pOrder的相关参数
    """
    a = env.get_account()
    ta = env.calc_target_price('m1501',LONG,3515,30)   #30跳挂买单,以成交
    a.spi.xopen('m1501',LONG,1,ta)    #直接开仓


def test_close1a(env):
    """
        上期所平今
        pOrder为开仓成功的on_rtn_order的返回值
    """
    a = env.get_account()
    ta = env.calc_target_price('al1408',SHORT,13620,-30)   #-30跳挂卖单,以成交
    a.spi.xclose('al1408',XCLOSE_TODAY,SHORT,ta,1)    #直接开仓
    #ta = env.calc_target_price('al1408',LONG,13620,30)   #+30跳挂买单,以成交
    #a.spi.xclose('al1408',XCLOSE_TODAY,LONG,ta,1)    #直接开仓

def test_close1b(env,pOrder=None):
    """
        大商所平今
        pOrder为开仓成功的on_rtn_order的返回值
    """
    a = env.get_account()
    ta = env.calc_target_price('p1409',LONG,5750,30)   #-30跳挂卖单,以成交
    a.spi.xclose('p1409',XCLOSE,LONG,ta,1)    #直接开仓

def test_close1c(env,pOrder=None):
    """
        大商所
        pOrder为开仓成功的on_rtn_order的返回值
    """
    a = env.get_account()
    ta = env.calc_target_price('m1501',SHORT,3515,-30)   #-30跳挂卖单,以成交
    a.spi.xclose('m1501',XCLOSE,SHORT,ta,1)    #直接开仓


def test_close2a(env,pOrder=None):
    """
        上期所平昨
            如果用平昨去平今仓,直接被CTP拒绝,
        pOrder为开仓成功的on_rtn_order的返回值
    """
    from ..common.base import SHORT
    a = env.get_account()
    ta = env.calc_target_price('al1408',SHORT,13620,-30)   #-30跳挂卖单,以成交
    a.spi.xclose('al1408',XCLOSE,SHORT,ta,1)    #直接开仓
    #ta = env.calc_target_price('al1408',LONG,13620,30)   #+30跳挂单,以成交
    #a.spi.xclose('al1408',XCLOSE,LONG,ta,1)    #直接开仓

def test_close2v(env,pOrder):
    """
        大商所平昨
        pOrder为开仓成功的on_rtn_order的返回值
    """
    pass



