# -*- coding: utf-8 -*-

'''
对CTP进行mock，目的有二：
    1. 为agent提供桩机，便于agent功能的开发和测试
    2. 结合实时行情，测试策略的实时信号
    3. 结合历史ticks行情，对策略进行确认测试

TODO:   为真实起见，在mock中采用Command模式 
桩机控制: (数据播放循环)
    数据播放
    触发Agent数据准备
    触发Agent策略执行
    触发API桩机-->Command
    控制器触发SPI 
    ...   
'''

import time
import logging

import hreader
import agent
import config
import strategy

import UserApiStruct as ustruct
import UserApiType as utype

from base import *

class TraderMock(object):
    def __init__(self,myagent):
        self.myagent = myagent
        self.available = 1000000    #初始100W
        self.myspi = BaseObject(is_logged=True,confirm_settlement_info=self.confirm_settlement_info)

    def ReqOrderInsert(self, order, request_id):
        '''报单录入请求, 需要调用成交函数'''
        logging.info(u'报单')
        oid = order.OrderRef
        trade = ustruct.Trade(
                    InstrumentID = order.InstrumentID,
                    Direction=order.Direction,
                    Price = order.LimitPrice,
                    Volume = order.VolumeTotalOriginal,
                    OrderRef = oid,
                    TradeID=oid,
                    OrderSysID=oid,
                    BrokerOrderSeq=oid,
                    OrderLocalID = oid,
                    TradeTime = time.strftime('%H%M%S'),#只有备案作用
                )
        if order.CombOffsetFlag == utype.THOST_FTDC_OF_Open:#开仓. 为方便起见,假设都是股指
            self.available -= order.LimitPrice * 300 * 0.17
        else:
            self.available += order.LimitPrice * 300 * 0.17
        fl_open = strategy.MAX_OPEN_OVERFLOW * 0.2
        fl_close = strategy.MAX_CLOSE_OVERFLOW * 0.2
        if order.CombOffsetFlag == utype.THOST_FTDC_OF_Open:
            trade.Price += -fl_open if order.Direction == utype.THOST_FTDC_D_Buy else fl_open
        else:
            trade.Price += -fl_close if order.Direction == utype.THOST_FTDC_D_Buy else fl_close
        self.myagent.rtn_trade(trade)

    def ReqOrderAction(self, corder, request_id):
        '''撤单请求'''
        #print u'in cancel'
        oid = corder.OrderRef
        rorder = ustruct.Order(
                    InstrumentID = corder.InstrumentID,
                    OrderRef = corder.OrderRef,
                    OrderStatus = utype.THOST_FTDC_OST_Canceled,
                )
        #self.myagent.rtn_order(rorder)
        self.myagent.err_order_action(rorder.OrderRef,rorder.InstrumentID,u'26',u'测试撤单--报单已成交')

    def ReqQryTradingAccount(self,req,req_id=0):
        logging.info(u'查询帐户余额')
        account = BaseObject(Available=self.available) 
        self.myagent.rsp_qry_trading_account(account)

    def ReqQryInstrument(self,req,req_id=0):#只有唯一一个合约
        logging.info(u'查询合约')
        ins = BaseObject(InstrumentID = req.InstrumentID,VolumeMultiple = 300,PriceTick=0.2)
        self.myagent.rsp_qry_instrument(ins)

    def ReqQryInstrumentMarginRate(self,req,req_id=0):
        logging.info(u'查询保证金')
        mgr = BaseObject(InstrumentID = req.InstrumentID,LongMarginRatioByMoney=0.17,ShortMarginRatioByMoney=0.17)
        self.myagent.rsp_qry_instrument_marginrate(mgr)

    def ReqQryInvestorPosition(self,req,req_id=0):
        #暂默认无持仓
        pass

    def confirm_settlement_info(self):
        self.myagent.isSettlementInfoConfirmed = True


class UserMock(object):
    pass

class MockManager(object):
    pass

class MockMd(object):
    '''简单起见，只模拟一个合约，用于功能测试
    '''
    def __init__(self,instrument):
        self.instrument = instrument
        self.agent = agent.Agent(None,None,[instrument],{})

    def play(self,tday=0):
        ticks = hreader.read_ticks(self.instrument,tday)
        for tick in ticks:
            self.agent.RtnTick(tick)
            #self.agent.RtnTick(tick)

class SaveMock(object):
    '''简单起见，只模拟一个合约，用于功能测试
    '''
    def __init__(self,instrument,tday=0):
        self.instrument = instrument
        self.agent = agent.SaveAgent(None,None,[instrument],{},tday=tday)

    def play(self,tday=0):
        ticks = hreader.read_ticks(self.instrument,tday)
        for tick in ticks:
            self.agent.RtnTick(tick)
            #self.agent.RtnTick(tick)


class NULLAgent(object):
    #只用于为行情提供桩
    logger = logging.getLogger('ctp.nullagent')

    def __init__(self,trader,cuser,instruments):
        '''
            trader为交易对象
        '''
        self.trader = trader
        self.cuser = cuser
        self.instruments = instruments
        self.request_id = 1
        ###
        self.lastupdate = 0
        self.front_id = None
        self.session_id = None
        self.order_ref = 1
        self.trading_day = 20110101
        self.scur_day = int(time.strftime('%Y%m%d'))

        #hreader.prepare_directory(INSTS_SAVE)

    def set_spi(self,spi):
        self.spi = spi

    def inc_request_id(self):
        self.request_id += 1
        return self.request_id

    def inc_order_ref(self):
        self.order_ref += 1
        return self.order_ref

    def set_trading_day(self,trading_day):
        self.trading_day = trading_day

    def get_trading_day(self):
        return self.trading_day

    def login_success(self,frontID,sessionID,max_order_ref):
        self.front_id = frontID
        self.session_id = sessionID
        self.order_ref = int(max_order_ref)

    def RtnTick(self,ctick):#行情处理主循环
        pass

def create_agent_with_mocktrader(instrument,tday,sname='strategy_mock.ini'):
    trader = TraderMock(None)
    print sname
    strategy_cfg = config.parse_strategy(name=sname)

    ##这里没有考虑现场恢复，state中需注明当日
    cuser = BaseObject(broker_id='test',port=1111,investor_id='test',passwd='test')
    myagent = agent.Agent(trader,cuser,[instrument],strategy_cfg,tday=tday) 
    trader.myagent = myagent

    req = BaseObject(InstrumentID=instrument)
    trader.ReqQryInstrumentMarginRate(req)
    trader.ReqQryInstrument(req)
    trader.ReqQryTradingAccount(req)
    return myagent

def run_ticks(ticks,myagent):
    for tick in ticks:
        myagent.inc_tick()
        #print tick.min1
        myagent.RtnTick(tick)

def log_config():
    config_logging('ctp_trade_mock.log',console_level=logging.INFO)

'''
##需要运行python26


import base
import ctp_mock
import hreader

ctp_mock.log_config()

preday = 20120515
tday = 20120516
instrument = 'IF1206'
myagent = ctp_mock.create_agent_with_mocktrader(instrument,-1)    #不需要tday的当日数据
myagent.instruments[instrument].t2order = base.t2order_if
myagent.scur_day = preday
#myagent.save_flag = True
myagent.prepare_data_env()
myagent.scur_day = tday
#myagent.instruments[instrument].data.atrd1
ticks = hreader.read_ticks(instrument,tday)    #不加载当日数据
#ctp_mock.run_ticks(ticks,myagent)
myagent.resume()
ctp_mock.run_ticks(ticks,myagent)

##推进
tday = 20120530
myagent.day_switch(tday)
ticks = hreader.read_ticks(instrument,tday)    #不加载当日数据
ctp_mock.run_ticks(ticks,myagent)

######
#使用trade.ini
import base
import ctp_mock
import hreader

ctp_mock.log_config()

preday = 20120530
tday = 20120531
instrument = 'IF1206'
myagent = ctp_mock.create_agent_with_mocktrader(instrument,-1,sname='strategy_trader.ini')    #不需要tday的当日数据
myagent.instruments[instrument].t2order = base.t2order_if
myagent.scur_day = preday
#myagent.save_flag = True
myagent.prepare_data_env()
myagent.scur_day = tday
#myagent.instruments[instrument].data.atrd1
ticks = hreader.read_ticks(instrument,tday)    #不加载当日数据
#ctp_mock.run_ticks(ticks,myagent)
myagent.resume()
ctp_mock.run_ticks(ticks,myagent)


###############
import base
import ctp_mock
import hreader

ctp_mock.log_config()

preday = 20110928
tday = 20110929
instrument = 'IF1110'
myagent = ctp_mock.create_agent_with_mocktrader(instrument,-1,sname='strategy_trader.ini')    #不需要tday的当日数据
myagent.instruments[instrument].t2order = base.t2order_if
myagent.scur_day = preday
#myagent.save_flag = True
myagent.prepare_data_env()
myagent.scur_day = tday
#myagent.instruments[instrument].data.atrd1
ticks = hreader.read_ticks(instrument,tday)    #不加载当日数据
#ctp_mock.run_ticks(ticks,myagent)
myagent.resume()
ctp_mock.run_ticks(ticks,myagent)


################
#第一次的ticks只到10:02
################
#当日第二次接续


################
################
#后续日期
time.sleep(2)

tday = 20110727
myagent.scur_day = tday
ticks = hreader.read_ticks(instrument,tday)    #不加载当日数据
ctp_mock.run_ticks(ticks,myagent)

time.sleep(2)

tday = 20110728
myagent.scur_day = tday
ticks = hreader.read_ticks(instrument,tday)    #不加载当日数据
ctp_mock.run_ticks(ticks,myagent)

'''

def trade_mock(instrument='IF1108'):
    #logging.basicConfig(filename="ctp_trade_mock.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')

    tday = 20110726
    myagent = create_agent_with_mocktrader(instrument,-1)    #不需要tday的当日数据
    myagent.scur_day = tday
    myagent.save_flag = True
    ticks = hreader.read_ticks(instrument,tday)    #不加载当日数据
    #for tick in ticks:myagent.inc_tick(),myagent.RtnTick(tick)
    #for tick in ticks:
    #    myagent.inc_tick()
    #    myagent.RtnTick(tick)
    run_ticks(ticks,myagent)

def semi_mock(instrument='IF1110',base_name='mybase.ini',base='Base'):
    ''' 半模拟
        实际行情，mock交易
    '''
    logging.basicConfig(filename="ctp_semi_mock.log",level=logging.INFO,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')    
    tday = int(time.strftime('%Y%m%d'))
    myagent = create_agent_with_mocktrader(instrument,tday)    #不需要tday的当日数据

    myagent.resume()

    base_cfg = config.parse_base(base_name,base)
    for user in base_cfg.users:
        agent.make_user(myagent,base_cfg.users[user],user)
    
    return myagent

def comp_mock(base_name='mybase.ini',base='Base',strategy_name='strategy_trader.ini'):
    ''' 全模拟
        实际行情，模拟交易
    '''
    logging.basicConfig(filename="ctp_comp_mock.log",level=logging.INFO,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')    
    #tday = int(time.strftime('%Y%m%d'))
    #myagent = create_agent_with_mocktrader(instrument,tday)    #不需要tday的当日数据
    trader,myagent = agent.create_trader(name='mybase.ini',base='Base_Mock',sname=strategy_name)

    myagent.resume()

    #用实际行情
    base_cfg = config.parse_base(base_name,'Base_Mock')
    for user in base_cfg.users:
        agent.make_user(myagent,base_cfg.users[user],user)
    
    return myagent

def comp_real(base_name='mybase.ini',base='Base',strategy_name='strategy_trader.ini'):
    ''' 实际交易
    '''
    logging.basicConfig(filename="ctp_comp_real.log",level=logging.INFO,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')    
    #tday = int(time.strftime('%Y%m%d'))
    #myagent = create_agent_with_mocktrader(instrument,tday)    #不需要tday的当日数据
    trader,myagent = agent.create_trader(name='mybase.ini',base='BASE_REAL',sname=strategy_name)

    myagent.resume()

    #用实际行情
    base_cfg = config.parse_base(base_name,'BASE_REAL')
    for user in base_cfg.users:
        agent.make_user(myagent,base_cfg.users[user],user)
    
    return myagent

def comp_real2(base_name='mybase.ini',base='Base',strategy_name='strategy_trader.ini',t2order=t2order_if):
    ''' 实际交易
    '''
    logging.basicConfig(filename="ctp_comp_real.log",level=logging.INFO,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')    
    #tday = int(time.strftime('%Y%m%d'))
    #myagent = create_agent_with_mocktrader(instrument,tday)    #不需要tday的当日数据
    trader,myagent = agent.create_trader(name=base_name,base=base,sname=strategy_name,t2order=t2order)

    myagent.resume()

    #用实际行情
    base_cfg = config.parse_base(base_name,base)
    for user in base_cfg.users:
        agent.make_user(myagent,base_cfg.users[user],user)
    
    return myagent


if __name__ == '__main__':
    log_config()
    trade_mock()

