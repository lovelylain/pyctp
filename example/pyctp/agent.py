#-*- coding:utf-8 -*-
'''
20110406
todo: 1. 确认在Agent的prepare_base中使用sleep不会阻碍下一个数据的接收
      2. 完成当日的收盘作业
      3. 设计中间保存的格式
      4. 完成情景恢复

Agent的目的是合并行情和交易API到一个类中进行处理
    把行情和交易分开，从技术角度上来看挺好，但从使用者角度看就有些蛋疼了.
    正常都是根据行情决策

todo:
    0. 生产环境必须考虑多个行情接入端, 有可能会出现延时情况.
    #1. 当日风险控制，当日交易次数限制以及交易损失限制

后续工作
 B.1. 合约的自动匹配

关注ifuncs1a
xud_short_2
rsi_long_x2
xdown60
up0
ipmacd_long_t2
acd_da_sz_b2


##因为流控原因,所有Qry命令都用Command模式?
  不需要,可以忍受1s的延时. 因为行情通过别的来接收  

三类配置文件，都用INI格式记录
1. 基本配置 base.ini  这个是完全私人的
   记录登陆站点，登陆ID以及口令 

    [Base]
    ;User用于设定连接行情的设定 
    users = User1,User2,User3
    ;Trade用于设定连接交易端的设定
    traders = Trader1,Trader2

    [User1]
    port = 
    broker_id = 
    investor_id = 
    passwd = 

    [User2]
    ....

2. 策略配置 strategy.ini
   配置盯盘的合约
   配置交易的合约, 每个合约可以指定多个策略

   a. 保存行情的设置, 其中[Trace_Instruments]为合约类设置
[Trace_Instruments]
traces = IF,ru,fu,zn,rb,pb,m,a,c,y,b,l,p,v,SR,CF,TA,WS,RO,ER,WT
;a/al/au重复,c/cu重复
;traces = IF,ru,fu,cu,al,zn,au,rb,pb,m,a,c,y,b,l,p,v,SR,CF,TA,WS,RO,ER,WT
    ;[Trace_Instruments_Raw]为绝对设置
[Trace_Instruments_Raw]
IFs = IF1104,IF1105,IF1106,IF1109
CFs = CF109,CF107
   b. 交易策略定制 (todo:将来考虑自动判断主力合约) 
    [Alias_Def]
    IF_main = IF1105
    CF_main = CF109
    ;TODO:确定main之后,计算next,third,fourth,分别表示次合约、第三合约、第四合约. 找到主力合约后，按字母序确定
    [Trade_Config]
    ;如果策略文件为strategy，则可以不写
    ;strategy_file = strategy
    traces = IF_main,CF_main
    
    [IF_main]
    max_volume = 2
    strategys = IF_A,IF_B,IF_C

    [IF_A]
    max_holding = 2
    open_volume = 1
    opener = day_long_break
    closer = datr_long_stoper
    
    [IF_B]
    ...


3. 中断恢复状态 state.ini
   记录当前的持仓及相关策略,止损相关

    [Time_Stamp]
    lastupdate = 

    [Holdings]
    holdings = IF1104,IF1105,CF1109,

    [IF1104]
    instrment = IF1104
    long_volume = xxxx
    short_volume = xxxx
    h_long = IF1104_L1,IF1104_L2
    h_short = IF1104_S1,IF1104_S2

    [IF1104_L1]
    volume = xxxx
    opener = xxxx
    stopers = xxxx,yyyy
    open_price = 3200
    current_stop_price = 3193

    [IF1104_L2]
    ...

    [IF1104_S1]
    ...

    [IF1105]
    ...
    ...

A. 中断恢复
   中断恢复是在创建instrment之后，重新初始化Position和Order的过程 
    


'''

import sched
import time
import logging
import thread
import threading
import bisect

from base import *
from dac import ATR,ATR1,STREND,STREND1,MA,MA1,MACD,MACD1,date2week
import hreader

import UserApiStruct as ustruct
import UserApiType as utype
from MdApi import MdApi, MdSpi
from TraderApi import TraderApi, TraderSpi  

import config
import strategy

#日内最后交易时间，超过为越界
LAST_TRADE_TIME = 1515

#数据定义中唯一一个enum
THOST_TERT_RESTART  = 0
THOST_TERT_RESUME   = 1
THOST_TERT_QUICK    = 2

NFUNC = lambda data:None    #空函数桩

INSTS = [
         u'IF1104',u'IF1105',
         u'zn1104',u'zn1105'
        ]

INSTS_SAVE = [  #已经废掉
         u'IF1104',u'IF1105',
         #郑州   
         u'CF109',u'CF111',
         u'ER109',u'ER111',
         u'RO109',u'RO111',
         u'TA105',u'TA106',
         u'WA109',u'WS111',
         #大连
         u'm1109',u'm1111',
         u'c1109',u'c1111',
         u'y1109',u'y1111',
         u'a1201',u'a1203',
         u'l1105',u'l1106',
         u'p1109',u'p1111',
         u'v1105',u'v1106',
         #上海
         u'rb1110',u'rb1111',
         u'zn1105',u'zn1106',
         u'al1105',u'al1106',
         u'cu1105',u'cu1106',
         u'ru1105',u'ru1106',
         u'fu1105',u'fu1106',
         ]  #必须采用ctp使用的合约名字，内部不做检验
#INSTS = [u'IF1103']  #必须采用ctp使用的合约名字，内部不做检验
#建议每跟踪的一个合约都使用一个行情-交易对. 因为行情的接收是阻塞式的,在做处理的时候会延误后面接收的行情
#套利时每一对合约都用一个行情-交易对
#INSTS = [u'IF1102']

#mylock = thread.allocate_lock()

dir_py2ctp = lambda dir : '0' if dir == LONG else '1'


class MdSpiDelegate(MdSpi):
    '''
        将行情信息转发到Agent
        并自行处理杂务
    '''
    logger = logging.getLogger('ctp.MdSpiDelegate')
    
    last_map = {}

    def __init__(self,
            instruments, #合约映射 name ==>c_instrument
            broker_id,   #期货公司ID
            investor_id, #投资者ID
            passwd, #口令
            agent,  #实际操作对象
        ):        
        self.instruments = set([name for name in instruments])
        self.broker_id =broker_id
        self.investor_id = investor_id
        self.passwd = passwd
        self.agent = agent
        ##必须在每日重新连接时初始化它. 这一点用到了生产行情服务器收盘后关闭的特点(模拟的不关闭)
        MdSpiDelegate.last_map = dict([(id,0) for id in instruments])
        self.last_day = 0

    def checkErrorRspInfo(self, info):
        if info.ErrorID !=0:
            logger.error(u"MD:ErrorID:%s,ErrorMsg:%s" %(info.ErrorID,info.ErrorMsg))
        return info.ErrorID !=0

    def OnRspError(self, info, RequestId, IsLast):
        self.logger.error(u'MD:requestID:%s,IsLast:%s,info:%s' % (RequestId,IsLast,str(info)))

    def OnFrontDisConnected(self, reason):
        self.logger.info(u'MD:front disconnected,reason:%s' % (reason,))

    def OnFrontConnected(self):
        self.logger.info(u'MD:front connected')
        self.user_login(self.broker_id, self.investor_id, self.passwd)

    def user_login(self, broker_id, investor_id, passwd):
        req = ustruct.ReqUserLogin(BrokerID=broker_id, UserID=investor_id, Password=passwd)
        r=self.api.ReqUserLogin(req,self.agent.inc_request_id())

    def OnRspUserLogin(self, userlogin, info, rid, is_last):
        self.logger.info(u'MD:user login,info:%s,rid:%s,is_last:%s' % (info,rid,is_last))
        scur_day = int(time.strftime('%Y%m%d'))
        if scur_day > self.agent.scur_day:    #换日,重新设置volume
            self.logger.info(u'MD:换日, %s-->%s' % (self.agent.scur_day,scur_day))
            #self.agent.scur_day = scur_day
            self.agent.day_switch(scur_day)
            MdSpiDelegate.last_map = dict([(id,0) for id in self.instruments])
        if is_last and not self.checkErrorRspInfo(info):
            self.logger.info(u"MD:get today's trading day:%s" % repr(self.api.GetTradingDay()))
            self.subscribe_market_data(self.instruments)

    def subscribe_market_data(self, instruments):
        self.api.SubscribeMarketData(list(instruments))

    def OnRtnDepthMarketData(self, depth_market_data):
        #print depth_market_data.BidPrice1,depth_market_data.BidVolume1,depth_market_data.AskPrice1,depth_market_data.AskVolume1,depth_market_data.LastPrice,depth_market_data.Volume,depth_market_data.UpdateTime,depth_market_data.UpdateMillisec,depth_market_data.InstrumentID
        #print 'on data......\n',
        #with mylock:
        try:
            #mylock.acquire()
            #self.logger.debug(u'获得锁.................,mylock.id=%s' % id(mylock))        
            if depth_market_data.LastPrice > 999999 or depth_market_data.LastPrice < 10:
                self.logger.warning(u'MD:收到的行情数据有误:%s,LastPrice=:%s' %(depth_market_data.InstrumentID,depth_market_data.LastPrice))
            if depth_market_data.InstrumentID not in self.instruments:
                self.logger.warning(u'MD:收到未订阅的行情:%s' %(depth_market_data.InstrumentID,))
            #self.logger.debug(u'收到行情:%s,time=%s:%s' %(depth_market_data.InstrumentID,depth_market_data.UpdateTime,depth_market_data.UpdateMillisec))
            dp = depth_market_data
            self.logger.debug(u'MD:收到行情，inst=%s,time=%s，volume=%s,last_volume=%s' % (dp.InstrumentID,dp.UpdateTime,dp.Volume,self.last_map[dp.InstrumentID]))
            if dp.Volume <= self.last_map[dp.InstrumentID]:
                self.logger.debug(u'MD:行情无变化，inst=%s,time=%s，volume=%s,last_volume=%s' % (dp.InstrumentID,dp.UpdateTime,dp.Volume,self.last_map[dp.InstrumentID]))
                return  #行情未变化
            self.last_map[dp.InstrumentID] = dp.Volume
            #mylock.release()   #至此已经去掉重复的数据

            #self.logger.debug(u'after modify instrument=%s,lastvolume:%s,curVolume:%s' % (dp.InstrumentID,self.last_map[dp.InstrumentID],dp.Volume))
            #self.logger.debug(u'before loop')
            self.agent.inc_tick()
            ctick = self.market_data2tick(depth_market_data)
            self.agent.RtnTick(ctick)
        finally:
            pass
            #mylock.release()   #至此主要工作完成
            #self.logger.debug(u'释放锁.................,mylock.id=%s' % id(mylock))
        

        #self.logger.debug(u'before write md:')
        if self.agent.save_flag == True:
            ff = open(hreader.make_tick_filename(ctick.instrument),'a+')
            #print type(dp.UpdateMillisec),type(dp.OpenInterest),type(dp.Volume),type(dp.BidVolume1)
            #ff.write(u'%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (dp.TradingDay,dp.UpdateTime,dp.UpdateMillisec,dp.OpenInterest,dp.Volume,dp.LastPrice,dp.HighestPrice,dp.LowestPrice,dp.BidPrice1,dp.BidVolume1,dp.AskPrice1,dp.AskVolume1))
            try:
                ff.write(u'%(instrument)s,%(date)s,%(min1)s,%(sec)s,%(msec)s,%(holding)s,%(dvolume)s,%(price)s,%(high)s,%(low)s,%(bid_price)s,%(bid_volume)s,%(ask_price)s,%(ask_volume)s\n' % ctick.__dict__)
            except Exception,inst:
                print str(depth_market_data),str(depth_market_data.TradingDay),str(depth_market_data.UpdateTime)
            ff.close()
        #self.logger.debug(u'after write md:')
        #time.sleep(0.3)
        #self.logger.debug(u'after write sleep:')

    def market_data2tick(self,market_data):
        #market_data的格式转换和整理, 交易数据都转换为整数
        try:
            #rev的后四个字段在模拟行情中经常出错
            rev = BaseObject(instrument = market_data.InstrumentID,date=self.agent.scur_day,bid_price=0,bid_volume=0,ask_price=0,ask_volume=0)
            rev.min1 = int(market_data.UpdateTime[:2]+market_data.UpdateTime[3:5])
            rev.sec = int(market_data.UpdateTime[-2:])
            rev.msec = int(market_data.UpdateMillisec)
            rev.holding = int(market_data.OpenInterest+0.1)
            rev.dvolume = market_data.Volume
            rev.price = int(market_data.LastPrice*10+0.1)
            rev.high = int(market_data.HighestPrice*10+0.1)
            rev.low = int(market_data.LowestPrice*10+0.1)
            rev.bid_price = int(market_data.BidPrice1*10+0.1)
            rev.bid_volume = market_data.BidVolume1
            rev.ask_price = int(market_data.AskPrice1*10+0.1)
            rev.ask_volume = market_data.AskVolume1
            if len(market_data.TradingDay.strip()) > 0:
                rev.date = int(market_data.TradingDay)
            else:#有时候会有错
                rev.date = self.last_day    
            rev.time = rev.date%10000 * 1000000+ rev.min1*100 + rev.sec
            rev.switch_min = False  #分钟切换
            self.last_day = rev.date
        except Exception,inst:
            #self.logger.warning(u'MD:行情数据转换错误:%s' % str(inst))
            self.logger.warning(u'MD:%s 行情数据转换错误:%s,updateTime="%s",msec="%s",tday="%s"' % (market_data.InstrumentID,str(inst),market_data.UpdateTime,market_data.UpdateMillisec,market_data.TradingDay))
        return rev

class TraderSpiDelegate(TraderSpi):
    '''
        将服务器回应转发到Agent
        并自行处理杂务
    '''
    logger = logging.getLogger('ctp.TraderSpiDelegate')    
    def __init__(self,
            instruments, #合约映射 name ==>c_instrument 
            broker_id,   #期货公司ID
            investor_id, #投资者ID
            passwd, #口令
            agent,  #实际操作对象
        ):        
        self.instruments = set([name for name in instruments])
        self.broker_id =broker_id
        self.investor_id = investor_id
        self.passwd = passwd
        self.agent = agent
        self.agent.set_spi(self)
        self.is_logged = False
 
    def isRspSuccess(self,RspInfo):
        return RspInfo == None or RspInfo.ErrorID == 0

    def login(self):
        self.logger.info(u'try login...')
        self.user_login(self.broker_id, self.investor_id, self.passwd)

    ##交易初始化
    def OnFrontConnected(self):
        '''
            当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        '''
        self.logger.info(u'TD:trader front connected')
        self.login()

    def OnFrontDisconnected(self, nReason):
        self.logger.info(u'TD:trader front disconnected,reason=%s' % (nReason,))

    def user_login(self, broker_id, investor_id, passwd):
        req = ustruct.ReqUserLogin(BrokerID=broker_id, UserID=investor_id, Password=passwd)
        r=self.api.ReqUserLogin(req,self.agent.inc_request_id())

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.logger.info(u'TD:trader login')
        self.logger.debug(u"TD:loggin %s" % str(pRspInfo))
        if not self.isRspSuccess(pRspInfo):
            self.logger.warning(u'TD:trader login failed, errMsg=%s' %(pRspInfo.ErrorMsg,))
            print u'综合交易平台登陆失败，请检查网络或用户名/口令'
            self.is_logged = False
            return
        self.is_logged = True
        self.logger.info(u'TD:trader login success')
        self.agent.login_success(pRspUserLogin.FrontID,pRspUserLogin.SessionID,pRspUserLogin.MaxOrderRef)
        #self.settlementInfoConfirm()
        self.agent.set_trading_day(self.api.GetTradingDay())
        #self.query_settlement_info()
        self.query_settlement_confirm() 

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        '''登出请求响应'''
        self.logger.info(u'TD:trader logout')
        self.is_logged = False

    def resp_common(self,rsp_info,bIsLast,name='默认'):
        #self.logger.debug("resp: %s" % str(rsp_info))
        if not self.isRspSuccess(rsp_info):
            self.logger.info(u"TD:%s失败" % name)
            return -1
        elif bIsLast and self.isRspSuccess(rsp_info):
            self.logger.info(u"TD:%s成功" % name)
            return 1
        else:
            self.logger.info(u"TD:%s结果: 等待数据接收完全..." % name)
            return 0

    def query_settlement_confirm(self):
        '''
            这个基本没用，不如直接确认
            而且需要进一步明确：有史以来第一次确认前查询确认情况还是每天第一次确认查询情况时，返回的响应中
                pSettlementInfoConfirm为空指针. 如果是后者,则建议每日不查询确认情况,或者在generate_struct中对
                CThostFtdcSettlementInfoConfirmField的new_函数进行特殊处理
            CTP写代码的这帮家伙素质太差了，边界条件也不测试，后置断言也不整，空指针乱飞
            2011-3-1 确认每天未确认前查询确认情况时,返回的响应中pSettlementInfoConfirm为空指针
            并且妥善处理空指针之后,仍然有问题,在其中查询结算单无动静
        '''
        req = ustruct.QrySettlementInfoConfirm(BrokerID=self.broker_id,InvestorID=self.investor_id)
        self.api.ReqQrySettlementInfoConfirm(req,self.agent.inc_request_id())

    def query_settlement_info(self):
        #不填日期表示取上一天结算单,并在响应函数中确认
        self.logger.info(u'TD:取上一日结算单信息并确认,BrokerID=%s,investorID=%s' % (self.broker_id,self.investor_id))
        req = ustruct.QrySettlementInfo(BrokerID=self.broker_id,InvestorID=self.investor_id,TradingDay=u'')
        #print req.BrokerID,req.InvestorID,req.TradingDay
        time.sleep(1)
        self.api.ReqQrySettlementInfo(req,self.agent.inc_request_id())

    def confirm_settlement_info(self):
        self.logger.info(u'TD-CSI:准备确认结算单')
        req = ustruct.SettlementInfoConfirm(BrokerID=self.broker_id,InvestorID=self.investor_id)
        self.api.ReqSettlementInfoConfirm(req,self.agent.inc_request_id())

    def OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        '''请求查询投资者结算信息响应'''
        print u'Rsp 结算单查询'
        if(self.resp_common(pRspInfo,bIsLast,u'结算单查询')>0):
            self.logger.info(u'结算单查询完成,准备确认')
            try:
                self.logger.info(u'TD:结算单内容:%s' % pSettlementInfo.Content)
            except Exception,inst:
                self.logger.warning(u'TD-ORQSI-A 结算单内容错误:%s' % str(inst))
            self.confirm_settlement_info()
        else:  #这里是未完成分支,需要直接忽略
            try:
                self.logger.info(u'TD:结算单接收中...:%s' % pSettlementInfo.Content)
            except Exception,inst:
                self.logger.warning(u'TD-ORQSI-B 结算单内容错误:%s' % str(inst))
            #self.agent.initialize()
            pass
            

    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        '''请求查询结算信息确认响应'''
        self.logger.debug(u"TD:结算单确认信息查询响应:rspInfo=%s,结算单确认=%s" % (pRspInfo,pSettlementInfoConfirm))
        #self.query_settlement_info()
        if(self.resp_common(pRspInfo,bIsLast,u'结算单确认情况查询')>0):
            if(pSettlementInfoConfirm == None or int(pSettlementInfoConfirm.ConfirmDate) < self.agent.scur_day):
                #其实这个判断是不对的，如果周日对周五的结果进行了确认，那么周一实际上已经不需要再次确认了
                if(pSettlementInfoConfirm != None):
                    self.logger.info(u'TD:最新结算单未确认，需查询后再确认,最后确认时间=%s,scur_day:%s' % (pSettlementInfoConfirm.ConfirmDate,self.agent.scur_day))
                else:
                    self.logger.info(u'TD:结算单确认结果为None')
                self.query_settlement_info()
            else:
                self.agent.isSettlementInfoConfirmed = True
                self.logger.info(u'TD:最新结算单已确认，不需再次确认,最后确认时间=%s,scur_day:%s' % (pSettlementInfoConfirm.ConfirmDate,self.agent.scur_day))
                self.agent.initialize()


    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        '''投资者结算结果确认响应'''
        if(self.resp_common(pRspInfo,bIsLast,u'结算单确认')>0):
            self.agent.isSettlementInfoConfirmed = True
            self.logger.info(u'TD:结算单确认时间: %s-%s' %(pSettlementInfoConfirm.ConfirmDate,pSettlementInfoConfirm.ConfirmTime))
        self.agent.initialize()


    ###交易准备
    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        '''
            保证金率回报。返回的必然是绝对值
        '''
        if bIsLast and self.isRspSuccess(pRspInfo):
            self.agent.rsp_qry_instrument_marginrate(pInstrumentMarginRate)
        else:
            #logging
            pass

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        '''
            合约回报。
        '''
        if bIsLast and self.isRspSuccess(pRspInfo):
            self.agent.rsp_qry_instrument(pInstrument)
            #print pInstrument
        else:
            #logging
            #print pInstrument
            self.agent.rsp_qry_instrument(pInstrument)  #模糊查询的结果,获得了多个合约的数据，只有最后一个的bLast是True


    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        '''
            请求查询资金账户响应
        '''
        print u'查询资金账户响应'
        self.logger.info(u'TD:资金账户响应:%s' % pTradingAccount)
        if bIsLast and self.isRspSuccess(pRspInfo):
            self.agent.rsp_qry_trading_account(pTradingAccount)
        else:
            #logging
            pass

    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        '''请求查询投资者持仓响应'''
        #print u'查询持仓响应',str(pInvestorPosition),str(pRspInfo)
        if self.isRspSuccess(pRspInfo): #每次一个单独的数据报
            self.agent.rsp_qry_position(pInvestorPosition)
        else:
            #logging
            pass

    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
        '''请求查询投资者持仓明细响应'''
        logging.info(str(pInvestorPositionDetail))
        if self.isRspSuccess(pRspInfo): #每次一个单独的数据报
            self.agent.rsp_qry_position_detail(pInvestorPositionDetail)
        else:
            #logging
            pass


    def OnRspError(self, info, RequestId, IsLast):
        ''' 错误应答
        '''
        self.logger.error(u'TD:requestID:%s,IsLast:%s,info:%s' % (RequestId,IsLast,str(info)))

    def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        '''请求查询报单响应'''
        if bIsLast and self.isRspSuccess(pRspInfo):
            self.agent.rsp_qry_order(pOrder)
        else:
            self.logger.error(u'TD:requestID:%s,IsLast:%s,info:%s' % (nRequestID,bIsLast,str(pRspInfo)))
            pass

    def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        '''请求查询成交响应'''
        if bIsLast and self.isRspSuccess(pRspInfo):
            self.agent.rsp_qry_trade(pTrade)
        else:
            #logging
            pass


    ###交易操作
    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        '''
            报单未通过参数校验,被CTP拒绝
            正常情况后不应该出现
        '''
        print pRspInfo,nRequestID
        self.logger.warning(u'TD:CTP报单录入错误回报, 正常后不应该出现,rspInfo=%s'%(str(pRspInfo),))
        #self.logger.warning(u'报单校验错误,ErrorID=%s,ErrorMsg=%s,pRspInfo=%s,bIsLast=%s' % (pRspInfo.ErrorID,pRspInfo.ErrorMsg,str(pRspInfo),bIsLast))
        #self.agent.rsp_order_insert(pInputOrder.OrderRef,pInputOrder.InstrumentID,pRspInfo.ErrorID,pRspInfo.ErrorMsg)
        self.agent.err_order_insert(pInputOrder.OrderRef,pInputOrder.InstrumentID,pRspInfo.ErrorID,pRspInfo.ErrorMsg)
    
    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        '''
            交易所报单录入错误回报
            正常情况后不应该出现
            这个回报因为没有request_id,所以没办法对应
        '''
        print u'ERROR Order Insert'
        self.logger.warning(u'TD:交易所报单录入错误回报, 正常后不应该出现,rspInfo=%s'%(str(pRspInfo),))
        self.agent.err_order_insert(pInputOrder.OrderRef,pInputOrder.InstrumentID,pRspInfo.ErrorID,pRspInfo.ErrorMsg)
    
    def OnRtnOrder(self, pOrder):
        ''' 报单通知
            CTP、交易所接受报单
            Agent中不区分，所得信息只用于撤单
        '''
        #print repr(pOrder)
        self.logger.info(u'报单响应,Order=%s' % str(pOrder))
        if pOrder.OrderStatus == 'a':
            #CTP接受，但未发到交易所
            #print u'CTP接受Order，但未发到交易所, BrokerID=%s,BrokerOrderSeq = %s,TraderID=%s, OrderLocalID=%s' % (pOrder.BrokerID,pOrder.BrokerOrderSeq,pOrder.TraderID,pOrder.OrderLocalID)
            self.logger.info(u'TD:CTP接受Order，但未发到交易所, BrokerID=%s,BrokerOrderSeq = %s,TraderID=%s, OrderLocalID=%s' % (pOrder.BrokerID,pOrder.BrokerOrderSeq,pOrder.TraderID,pOrder.OrderLocalID))
            self.agent.rtn_order(pOrder)
        else:
            #print u'交易所接受Order,exchangeID=%s,OrderSysID=%s,TraderID=%s, OrderLocalID=%s' % (pOrder.ExchangeID,pOrder.OrderSysID,pOrder.TraderID,pOrder.OrderLocalID)
            self.logger.info(u'TD:交易所接受Order,exchangeID=%s,OrderSysID=%s,TraderID=%s, OrderLocalID=%s' % (pOrder.ExchangeID,pOrder.OrderSysID,pOrder.TraderID,pOrder.OrderLocalID))
            #self.agent.rtn_order_exchange(pOrder)
            self.agent.rtn_order(pOrder)

    def OnRtnTrade(self, pTrade):
        '''成交通知'''
        self.logger.info(u'TD:成交通知,BrokerID=%s,BrokerOrderSeq = %s,exchangeID=%s,OrderSysID=%s,TraderID=%s, OrderLocalID=%s' %(pTrade.BrokerID,pTrade.BrokerOrderSeq,pTrade.ExchangeID,pTrade.OrderSysID,pTrade.TraderID,pTrade.OrderLocalID))
        self.logger.info(u'TD:成交回报,Trade=%s' % repr(pTrade))
        self.agent.rtn_trade(pTrade)

    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        '''
            ctp撤单校验错误
        '''
        self.logger.warning(u'TD:CTP撤单录入错误回报, 正常后不应该出现,rspInfo=%s'%(str(pRspInfo),))
        #self.agent.rsp_order_action(pInputOrderAction.OrderRef,pInputOrderAction.InstrumentID,pRspInfo.ErrorID,pRspInfo.ErrorMsg)
        self.agent.err_order_action(pInputOrderAction.OrderRef,pInputOrderAction.InstrumentID,pRspInfo.ErrorID,pRspInfo.ErrorMsg)

    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        ''' 
            交易所撤单操作错误回报
            正常情况后不应该出现
        '''
        self.logger.warning(u'TD:交易所撤单录入错误回报, 可能已经成交,rspInfo=%s'%(str(pRspInfo),))
        self.agent.err_order_action(pOrderAction.OrderRef,pOrderAction.InstrumentID,pRspInfo.ErrorID,pRspInfo.ErrorMsg)


class c_instrument(object):
    @staticmethod
    def create_instruments(names,strategy,t2order=t2order_if):
        '''根据名称序列和策略序列创建instrument
           其中策略序列的结构为:
           [总最大持仓量,策略1,策略2...] 
        '''
        objs = dict([(name,c_instrument(name,t2order=t2order)) for name in names])
        for item in strategy.values():
            if item.name not in objs:
                logging.warning(u'策略针对合约%s不在盯盘列表中' % (item.name,))
                continue
            objs[item.name].max_volume = item.max_volume #
            objs[item.name].max_vtimes = item.max_vtimes #
            objs[item.name].max_lost = item.max_lost #            
            #objs[item.name].strategy = dict([(ss.get_name(),ss) for ss in item[1:]])
            objs[item.name].strategy = dict([(ss.name,ss) for ss in item.strategys])
            objs[item.name].initialize_positions()
        return objs

    def __init__(self,name,t2order = t2order_if):
        self.name = name
        #保证金率
        self.marginrate = (0,0) #(多,空)
        #合约乘数
        self.multiple = 0
        #最小跳动
        self.tick_base = 0  #单位为0.1
        #持仓量
        #BaseObject(hlong,hshort,clong,cshort) #历史多、历史空、今日多、今日空 #必须与实际数据一致, 实际上没用到
        self.position = BaseObject(hlong=0,hshort=0,clong=0,cshort=0)
        #持仓明细策略名==>Position #(合约、策略名、策略、基准价、基准时间、orderref、持仓方向、持仓量、当前止损价)
        self.position_detail = {}   #在Agent的ontrade中设定, 并需要在resume中恢复
        #设定的最大持仓手数
        self.max_volume = 1
        self.max_vtimes = 1  #最大的手次，如一次开2手，则为2手次
        self.max_lost = 0
        self.cur_vtimes = 0
        self.cur_profit = 0 #当前收益

        #应用策略 开仓函数名 ==> STRATEGY对象)
        self.strategy = {}
        
        #行情数据
        #其中tdata.m1/m3/m5/m15/m30/d1为不同周期的数据
        #   tdata.cur_min是当前分钟的行情，包括开盘,最高,最低,当前价格,持仓,累计成交量
        #   tdata.cur_day是当日的行情，包括开盘,最高,最低,当前价格,持仓,累计成交量, 其中最高/最低有两类，一者是tick的当前价集合得到的，一者是tick中的最高/最低价得到的
        self.t2order = t2order_if if hreader.is_if(self.name) else t2order_com
        #self.t2order = t2order
        ##模拟的在外面解决
        #if int(time.strftime('%H%M%S')) > 170000:   #模拟
        #    self.t2order = t2order_mock
        #elif int(time.strftime('%H%M%S')) > 151500:   #模拟
        #    self.t2order = t2order_mock2

        self.data = BaseObject()
        self.begin_flag = False #save标志，默认第一个不保存, 因为第一次切换的上一个是历史数据

    def initialize_positions(self): #根据策略初始化头寸为0
        self.position_detail = dict([(ss.name,strategy.Position(self,ss)) for ss in self.strategy.values()])

    def calc_remained_volume(self):   #计算剩余的可开仓量
        if self.cur_vtimes >= self.max_vtimes:    #超过日开仓次数限制
            logging.info(u'超过日开仓手次限制:%s|%s' % (self.cur_vtimes,self.max_vtimes))
            return 0
        #if self.cur_profit <= -self.max_lost:   #超过日最大损失
        #    logging.info(u'超过日开损失限制:%s|%s' % (self.cur_profit,self.max_lost))
        #    return 0
        locked_volume = 0
        opened_volume = 0
        for position in self.position_detail.values():
            plocked,popened = position.get_locked_volume() 
            locked_volume += plocked
            opened_volume += popened
            logging.debug(u'计算策略锁定量: pos:%s,locked_volume=%s,opened_volume=%s' % (position,plocked,popened))
        remained_volume = self.max_volume - locked_volume if self.max_volume > locked_volume else 0
        logging.info(u'A_CRV2:%s合约总锁定数=%s,合约最大允许数=%s,剩余可开仓数=%s,已开仓数=%s' % (self.name,locked_volume,self.max_volume,remained_volume,opened_volume))
        return remained_volume

    def calc_margin_amount(self,price,direction):   
        '''
            计算保证金
            所有price以0.1为基准
            返回的保证金以1为单位
        '''
        #print self.name,self.marginrate[0],self.marginrate[1],self.multiple
        my_marginrate = self.marginrate[0] if direction == LONG else self.marginrate[1]
        print 'self.name=%s,price=%s,multiple=%s,my_marginrate=%s' % (self.name,price,self.multiple,my_marginrate)
        if self.name[:2].upper() == 'IF':
            #print 'price=%s,multiple=%s,my_marginrate=%s' % (price,self.multiple,my_marginrate)
            return price / 10.0 * self.multiple * my_marginrate * 1.05  #避免保证金问题
        else:
            return price * self.multiple * my_marginrate * 1.05

    def make_target_price(self,price,direction): 
        '''
            计算开平仓时的溢出价位
            传入的price以0.1为单位
            返回的目标价以1为单位
        '''
        return (price + SLIPPAGE_BASE * self.tick_base if direction == LONG else price-SLIPPAGE_BASE * self.tick_base)/10.0

    def get_order(self,vtime):
        #print self.t2order
        return self.t2order[vtime]

    def day_switch(self):
        self.cur_vtimes = 0
        self.cur_profit = 0
        for ss in self.strategy.values():   #重新初始化opener
            ss.opener = ss.opener_class()
        
    def add_vtimes(self,v):
        self.cur_vtimes += v

    def add_profit(self,profit):
        '''
            这个必须在平仓的时候计算，但是因为可能是一次指令多次回报(包括开仓和平仓)
        '''
        self.cur_profit += profit
        logging.info(u'当前利润:%s' % (self.cur_profit,))


class AbsAgent(object):
    ''' 抽取与交易无关的功能，便于单独测试
    '''
    def __init__(self):
        ##命令队列(不区分查询和交易)
        self.commands = []  #每个元素为(trigger_tick,func), 用于当tick==trigger_tick时触发func
        self.tick = 0

    def inc_tick(self):
        self.tick += 1
        #self.check_commands()
        return self.tick

    def get_tick(self):
        return self.tick

    def put_command(self,trigger_tick,command): #按顺序插入
        #print func_name(command)
        cticks = [ttick for ttick,cmd in self.commands] #不要用command这个名称，否则会覆盖传入的参数,导致后面的插入操作始终插入的是原序列最后一个command的拷贝
        ii = bisect.bisect(cticks,trigger_tick)
        #print 'trigger_tick=%s,cticks=%s,len(command)=%s' % (trigger_tick,str(cticks),len(self.commands))
        self.commands.insert(ii,(trigger_tick,command))
        logging.debug(u'AA_P:trigger_tick=%s,cticks=%s,len(command)=%s' % (trigger_tick,str(cticks),len(self.commands)))

    def check_commands(self):   
        '''
            执行命令队列中触发时间<=当前tick的命令. 注意一个tick=0.5s
            以后考虑一个tick只触发一个命令?
        '''
        #print 'in check command'
        l = len(self.commands)
        i = 0
        #if l>0:
        #    pass
        #    print 'in check command,len=%s,self.tick=%s,command time=%s' % (l,self.tick,self.commands[-1][0])
        while(i<l and self.tick >= self.commands[i][0]):
            logging.info(u'AA_C:exec command,i=%s,tick=%s,command[i][0]=%s' % (i,self.tick,self.commands[i][0]))
            self.commands[i][1]()
            i += 1
        if i>0:
            #print 'del execed command'
            del self.commands[0:i]
        #print len(self.commands)


class Agent(AbsAgent):
    logger = logging.getLogger('ctp.agent')

    def __init__(self,trader,cuser,instruments,strategy_cfg,tday=0,t2order=t2order_if):
        '''
            trader为交易对象
            tday为当前日,为0则为当日
        '''
        AbsAgent.__init__(self)
        ##计时, 用来激发队列
        ##
        self.trader = trader
        #self.trader.myagent = self
        #if trader != None:
        #    trader.initialize(self)
        self.cuser = cuser
        self.strategy_cfg = strategy_cfg
        self.strategy = strategy_cfg.strategy
        self.t2order = t2order
        self.instruments = c_instrument.create_instruments(instruments,self.strategy,t2order=t2order)
        self.request_id = 1
        self.initialized = False
        self.data_funcs = []  #计算函数集合. 如计算各类指标, 顺序关系非常重要
                              #每一类函数由一对函数组成，.sfunc计算序列用，.func1为动态计算用，只计算当前值
                              #接口为(data), 从data的属性中取数据,并计算另外一些属性
        ###交易
        self.lastupdate = 0
        self.ref2order = {}    #orderref==>order
        #self.queued_orders = []     #因为保证金原因等待发出的指令(合约、策略族、基准价、基准时间(到秒))
        self.front_id = None
        self.session_id = None
        self.order_ref = 1
        self.trading_day = 20110101
        self.scur_day = int(time.strftime('%Y%m%d')) if tday==0 else tday
        #当前资金/持仓
        self.available = 0  #可用资金
        ##查询命令队列
        self.qry_commands = []  #每个元素为查询命令，用于初始化时查询相关数据
        
        #计算函数 sfunc为序列计算函数(用于初始计算), func1为动态计算函数(用于分钟完成时的即时运算)
        self.register_data_funcs(
                BaseObject(sfunc=NFUNC,func1=hreader.time_period_switch),    #时间切换函数
                BaseObject(sfunc=ATR,func1=ATR1),
                BaseObject(sfunc=MA,func1=MA1),
                BaseObject(sfunc=MACD,func1=MACD1),
                BaseObject(sfunc=STREND,func1=STREND1),
            )

        #初始化
        hreader.prepare_directory(instruments)
        self.prepare_data_env()
        #调度器
        self.scheduler = sched.scheduler(time.time, time.sleep)
        #保存锁
        self.lock = threading.Lock()
        #保存分钟数据标志
        self.save_flag = False  #默认不保存

        #actions
        self.actions = []

        self.init_init()    #init中的init,用于子类的处理

        #结算单
        self.isSettlementInfoConfirmed = False  #结算单未确认


    def init_init(self):    #init中的init,用于子类的处理
        pass

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

    def initialize(self):
        '''
            初始化，如保证金率，账户资金等
        '''
        ##必须先把持仓初始化成配置值或者0
        self.qry_commands.append(self.fetch_trading_account)
        for inst in self.instruments:
            self.qry_commands.append(fcustom(self.fetch_instrument,instrument_id = inst))
            self.qry_commands.append(fcustom(self.fetch_instrument_marginrate,instrument_id = inst))
            self.qry_commands.append(fcustom(self.fetch_investor_position,instrument_id = inst))
        time.sleep(1)   #保险起见
        self.check_qry_commands()
        self.initialized = True #避免因为断开后自动重连造成的重复访问

    def check_qry_commands(self):
        #必然是在rsp中要发出另一个查询
        if len(self.qry_commands)>0:
            time.sleep(1)   #这个只用于非行情期的执行. 
            self.qry_commands[0]()
            del self.qry_commands[0]
        logging.debug(u'查询命令序列长度:%s' % (len(self.qry_commands),))


    def prepare_data_env(self):
        '''
            准备数据环境, 如需要的30分钟数据
        '''
        #print 'in prepare_data_env'
        hdatas = hreader.prepare_data([name for name in self.instruments],self.scur_day)
        for hdata in hdatas.values():
            #print 'PDE_B:',hdata.name
            self.instruments[hdata.name].data = hdata
            for dfo in self.data_funcs:
                #print 'PDE_C:',hdata.name,dfo.sfunc
                dfo.sfunc(hdata)
            
    def register_data_funcs(self,*funcss):
        for funcs in funcss:
            self.data_funcs.append(funcs)

    ##内务处理
    def fetch_trading_account(self):
        #获取资金帐户
        logging.info(u'A:获取资金帐户..')
        req = ustruct.QryTradingAccount(BrokerID=self.cuser.broker_id, InvestorID=self.cuser.investor_id)
        r=self.trader.ReqQryTradingAccount(req,self.inc_request_id())
        #logging.info(u'A:查询资金账户, 函数发出返回值:%s' % r)

    def fetch_investor_position(self,instrument_id):
        #获取合约的当前持仓
        logging.info(u'A:获取合约%s的当前持仓..' % (instrument_id,))
        req = ustruct.QryInvestorPosition(BrokerID=self.cuser.broker_id, InvestorID=self.cuser.investor_id,InstrumentID=instrument_id)
        r=self.trader.ReqQryInvestorPosition(req,self.inc_request_id())
        #logging.info(u'A:查询持仓, 函数发出返回值:%s' % rP)
    
    def fetch_investor_position_detail(self,instrument_id):
        '''
            获取合约的当前持仓明细，目前没用
        '''
        logging.info(u'A:获取合约%s的当前持仓..' % (instrument_id,))
        req = ustruct.QryInvestorPositionDetail(BrokerID=self.cuser.broker_id, InvestorID=self.cuser.investor_id,InstrumentID=instrument_id)
        r=self.trader.ReqQryInvestorPositionDetail(req,self.inc_request_id())
        #logging.info(u'A:查询持仓, 函数发出返回值:%s' % r)

    def fetch_instrument_marginrate(self,instrument_id):
        req = ustruct.QryInstrumentMarginRate(BrokerID=self.cuser.broker_id,
                        InvestorID=self.cuser.investor_id,
                        InstrumentID=instrument_id,
                        HedgeFlag = utype.THOST_FTDC_HF_Speculation
                )
        r = self.trader.ReqQryInstrumentMarginRate(req,self.inc_request_id())
        logging.info(u'A:查询保证金率, 函数发出返回值:%s' % r)

    def fetch_instrument(self,instrument_id):
        req = ustruct.QryInstrument(
                        InstrumentID=instrument_id,
                )
        time.sleep(1)
        r = self.trader.ReqQryInstrument(req,self.inc_request_id())
        logging.info(u'A:查询合约, 函数发出返回值:%s' % r)

    def fetch_instruments_by_exchange(self,exchange_id):
        '''不能单独用exchange_id,因此没有意义
        '''
        req = ustruct.QryInstrument(
                        ExchangeID=exchange_id,
                )
        r = self.trader.ReqQryInstrument(req,self.inc_request_id())
        logging.info(u'A:查询合约, 函数发出返回值:%s' % r)

    ##交易处理
    def RtnTick(self,ctick):#行情处理主循环
        #logging.info(u'AR_A:cur_tick=%s' % (self.tick,))
        #print u'in my lock, close长度:%s,ma_5长度:%s\n' %(len(self.instruments[ctick.instrument].data.sclose),len(self.instruments[ctick.instrument].data.ma_5))
        if self.trader != None and not self.trader.myspi.is_logged:
            logging.info(u'trader not logging,try login.......')
            self.trader.myspi.login()
        elif not self.isSettlementInfoConfirmed: #结算单未确认
            logging.info(u'结算单未确认.....')
            self.trader.myspi.confirm_settlement_info()
        inst = ctick.instrument
        if not self.prepare_tick(ctick):    #非法ticks数据
            #print 'invalid ticks'
            logging.warning(u'非法ticks')
            return 
        #先平仓
        close_positions = self.check_close_signal(ctick)
        if len(close_positions)>0:
            self.make_command(close_positions)
        #再开仓.
        open_signals = self.check_open_signal(ctick)
        if len(open_signals) > 0:
            self.make_command(open_signals)
        #检查待发出命令
        self.check_commands()
        ##扫尾
        self.finalize()
        #print u'after my lock, close长度:%s,ma_5长度:%s\n' %(len(self.instrument[ctick.instrument].data.sclose),len(self.instrument[ctick.instrument].data.ma_5))
        
    def prepare_tick(self,ctick):
        '''
            准备计算, 包括分钟数据、指标的计算
            返回值表示该tick数据是否有效
        '''
        inst = ctick.instrument
        if inst not in self.instruments:
            logger.info(u'接收到未订阅的合约数据:%s' % (inst,))
            return False
        dinst = self.instruments[inst]#.data
        ctick.iorder = dinst.get_order(ctick.min1)
        if (ctick.iorder < dinst.data.cur_min.viorder and ctick.date == dinst.data.cur_min.vdate) or ctick.date < dinst.data.cur_min.vdate:
            #print ctick.date,ctick.time,dinst.data.cur_min.vdate,dinst.data.cur_min.vtime
            logging.info(u'过滤:time=%s,ctick.iorder=%s,ctick.date=%s,ddc.viorder=%s,ddc.vdate=%s' % (ctick.time,ctick.iorder,ctick.date,dinst.data.cur_min.viorder,dinst.data.cur_min.vdate))
            return False
        #logging.info(u'cur_tick:%s' % (ctick.tick,))
        if(self.prepare_base(dinst,ctick)):  #如果切分分钟则返回>0
            for func in self.data_funcs:    #动态计算
                func.func1(dinst.data)
        return True

    def day_finalize(self,dinst,last_min,last_sec):
        '''指定ddata的日结操作
           将当日数据复制到history.txt 
        '''
        #print ddata.name,last_min,last_sec
        with self.lock:
            ddata = dinst.data
            '''
            if ddata.cur_min.vtime > last_min:  #存在151500或150000,不需要继续转换
                print u'%s存在151500或150000,ddata.cur_min=%s,last_min=%s' % (ddata.name,ddata.cur_min.vtime,last_min)
                self.logger.info(u'%s存在151500或150000,ddata.cur_min=%s,last_min=%s' % (ddata.name,ddata.cur_min,last_min))
            else:   #不存在151500或150000.则将最后一分钟保存
                self.save_min(dinst)
            '''
            try:
                last_current_time = hreader.read_current_last_c(dinst.name,self.scur_day).time
            except:
                last_current_time = 0
            logging.info(u'A_DF:cur_time=%s,last_min=%s' %(last_current_time,last_min))
            if last_current_time < last_min:    #如果已经有当分钟的记录，就不再需要保存了。
                self.save_min(dinst)  
                for func in self.data_funcs:    #动态计算
                    func.func1(dinst.data)
            #print 'in day_finalize'
            if self.save_flag == True:
                hreader.check_merge(ddata.name,self.scur_day)
        for action in self.actions:
            logging.info(u'%s' % (str(action),))

    def save_min(self,dinst):
        ddata = dinst.data
        ddata.sdate.append(ddata.cur_min.vdate)
        ddata.stime.append(ddata.cur_min.vtime)
        ddata.sopen.append(ddata.cur_min.vopen)
        ddata.sclose.append(ddata.cur_min.vclose)
        ddata.shigh.append(ddata.cur_min.vhigh)
        ddata.slow.append(ddata.cur_min.vlow)
        ddata.sholding.append(ddata.cur_min.vholding)
        ddata.svolume.append(ddata.cur_min.vvolume)
        ddata.siorder.append(dinst.get_order(ddata.cur_min.vtime))
        #logging.info('SM1:len(m1)=%s' % len(ddata.m1[0])) ##ddata.m1就是ddata.transaction, 而ddata.sdata=ddata.m1[IDATE]
        #print 'in save_min'
        ##需要save下
        if self.save_flag == True and ddata.cur_min.vdate == self.scur_day:   #只保存当日的
            hreader.save1(dinst.name,ddata.cur_min,self.scur_day)

    def prepare_base(self,dinst,ctick):
        '''
            返回值标示是否是分钟的切换
            这里没有处理15:00:00的问题
        '''
        rev = False #默认不切换
        ddata = dinst.data
        #print 'ctick.iorder=%s' % (ctick.iorder,)
        if (ctick.iorder == ddata.cur_min.viorder + 1 and (ctick.sec > 0 or ctick.msec>0)) or ctick.iorder > ddata.cur_min.viorder + 1 or ctick.date > ddata.cur_min.vdate:
        #时间切换. 00秒00毫秒属于上一分钟, 但如果下一单是隔了n分钟的，也直接切换
            #logging.info('PB2A:len(m1)=%s' % len(ddata.m1[0]))
            #logging.info(u'分钟切换,time=%s,min1=%s,pre_iorder=%s,cur_iorder=%s' % (ctick.time,ctick.min1,ddata.cur_min.viorder,ctick.iorder))
            ctick.switch_min = True
            rev = True
            #print ctick.min1,ddata.cur_min.vtime,ctick.date,ddata.cur_min.vdate
            if (len(ddata.stime)>0 and (ctick.date > ddata.sdate[-1] or ctick.min1 > ddata.stime[-1])) or len(ddata.stime)==0:#已有分钟与已保存的有差别
                ''' #2011-05-01 去掉. 因为把00归入上一分钟
                #这里把00秒归入到新的分钟里面. todo:需要把00归入到老的分钟??一切都迎刃而解
                if (hreader.is_if(ctick.instrument) and ctick.min1 == 1515 and ctick.sec==0) or (not hreader.is_if(ctick.instrument) and ctick.min1 == 1500 and ctick.sec==0): #最后一秒钟算1514/1500的, 需要处理没有1500/1515时候的最后一分钟
                    print u'最后一秒钟....'
                    ddata.cur_min.vclose = ctick.price
                    if ctick.price > ddata.cur_min.vhigh:
                        ddata.cur_min.vhigh = ctick.price
                    if ctick.price < ddata.cur_min.vlow:
                        ddata.cur_min.vlow = ctick.price
                    ddata.cur_min.vholding = ctick.holding
                    ddata.cur_min.vvolume += (ctick.dvolume - ddata.cur_day.vvolume)
                '''
                #if ddata.cur_min.vdate != 0:    #不是史上第一个
                #    #print u'正常保存分钟数据.......'
                #    self.save_min(dinst)
                #else:#是史上第一分钟，之前的cur_min是默认值, 即无保存价值
                #    #print u'不保存分钟数据,date=%s' % (ddata.cur_min.vdate)
                #    rev = False
                if dinst.begin_flag:
                    #print u'保存分钟数据,date=%s,time=%s' % (ddata.cur_min.vdate,ddata.cur_min.vtime)
                    #logging.info('PB2A1:len(m1)=%s' % len(ddata.m1[0]))
                    self.save_min(dinst)
                    #logging.info('PB2A2:len(m1)=%s' % len(ddata.m1[0]))
                else:
                    #print u'第-1分钟数据不保存,date=%s,time=%s' % (ddata.cur_min.vdate,ddata.cur_min.vtime)
                    dinst.begin_flag = True
                    rev = False
            ddata.cur_min.vdate = ctick.date
            ddata.cur_min.vtime = ctick.min1
            ddata.cur_min.vopen = ctick.price
            ddata.cur_min.vclose = ctick.price
            ddata.cur_min.vhigh = ctick.price
            ddata.cur_min.vlow = ctick.price
            ddata.cur_min.vholding = ctick.holding
            ddata.cur_min.vvolume = ctick.dvolume - ddata.cur_day.vvolume if ctick.date == ddata.cur_day.vdate else ctick.dvolume
            ddata.cur_min.viorder = ctick.iorder
            #print 'in change:',ddata.cur_min.vvolume
            #logging.info('PB2B:len(m1)=%s' % len(ddata.m1[0]))
        elif ctick.iorder == ddata.cur_min.viorder or (ctick.iorder == ddata.cur_min.viorder + 1 and ctick.sec == 0 and ctick.msec==0):#当分钟的处理. 在接续时，如果resume时间正好是当分钟，会发生当分钟重复计数
            #print ddata.cur_min.vvolume,ctick.dvolume,ddata.cur_day.vvolume,ctick.time,ctick.sec,ctick.msec
            ddata.cur_min.vclose = ctick.price
            if ctick.price > ddata.cur_min.vhigh:
                ddata.cur_min.vhigh = ctick.price
            if ctick.price < ddata.cur_min.vlow:
                ddata.cur_min.vlow = ctick.price
            ddata.cur_min.vholding = ctick.holding
            ddata.cur_min.vvolume += (ctick.dvolume - ddata.cur_day.vvolume)
            #print ddata.cur_min.vvolume
        else:#早先的tick，只在测试时用到
            pass
        ##日的处理
        if ctick.date != ddata.cur_day.vdate:
            ddata.cur_day.vdate = ctick.date
            ddata.cur_day.vopen = ctick.price
            ddata.cur_day.vhigh = ctick.price
            ddata.cur_day.vlow = ctick.price
            ddata.cur_day.iihigh = 0
            ddata.cur_day.iilow = 0
            ddata.cur_day.weekday = date2week(ctick.date)
            ddata.cur_day.ibegin = len(ddata.sdate)   #最新一个分钟的位置,应当是下一分钟。因为还没保存
        else:
            if ctick.price > ddata.cur_day.vhigh:
                ddata.cur_day.vhigh = ctick.price   #根据当前价比较得到的最大/最小
                ddata.cur_day.iihigh = ctick.iorder
            if ctick.price < ddata.cur_day.vlow:
                ddata.cur_day.vlow = ctick.price
                ddata.cur_day.iilow = ctick.iorder
        ddata.cur_day.vholding = ctick.holding
        ddata.cur_day.vvolume = ctick.dvolume
        ddata.cur_day.vhighd = ctick.high   #服务器传过来的最大/最小
        ddata.cur_day.vlowd = ctick.low
        ddata.cur_day.vclose = ctick.price
        ddata.cur_day.vtime = ctick.min1
        #if (hreader.is_if(ctick.instrument) and ctick.min1 == 1514 and ctick.sec==59) or (not hreader.is_if(ctick.instrument) and ctick.min1 == 1459 and ctick.sec==59): #收盘作业
        #print ddata.cur_min.viorder,ctick.sec,ctick.min1,ddata.cur_min.vtime
        if ddata.cur_min.viorder == 270 and ctick.sec == 59 and ctick.min1 >=ddata.cur_min.vtime: #避免收到历史行情引发问题
            #print 'in closing',ddata.cur_min.viorder,ctick.sec,ddata.cur_min.vtime,ctick.min1
            threading.Timer(1,self.day_finalize,args=[dinst,ctick.min1,ctick.sec]).start()
            #self.day_finalize(dinst,ctick.min1,ctick.sec)
        #threading.Timer(3,self.day_finalize,args=[dinst,ctick.min1,ctick.sec]).start()
        return rev
    
    def check_close_signal(self,ctick):
        '''
            检查平仓信号
            #TODO: 必须考虑出现平仓信号时，position还没完全成交的情况
                   在OnTrade中进行position的细致处理 
        '''
        signals = []
        if ctick.instrument not in self.instruments:
            logging.warning(u'需要监控的%s未记录行情数据')
            print u'需要监控的%s未记录行情数据'
            return signals
        cur_inst = self.instruments[ctick.instrument]
        is_touched = False  #止损位变化
        for position in cur_inst.position_detail.values():
            for order in position.orders:
                if order.opened_volume > 0 and order.close_lock == False:
                    #mysignal = order.stoper.check(ctick)
                    mysignal = order.check_stop(ctick)
                    if mysignal[0] != 0 and order.close_lock == False:    #平仓
                        logging.info(u'平仓信号,time=%s,inst=%s,cur_price=%s,base_price=%s' % (ctick.time,cur_inst.name,ctick.price,mysignal[1]))
                        signals.append(BaseObject(instrument=cur_inst,
                                volume=order.opened_volume,
                                #direction = dir_py2ctp(order.get_stop_direction()),
                                direction = order.get_stop_direction(),
                                base_price = mysignal[1],
                                #target_price=order.stoper.calc_target_price(mysignal[1],cur_inst.tick_base),
                                target_price=order.calc_stop_price(mysignal[1],cur_inst.tick_base),
                                source_order = order, #原始头寸
                                mytime = ctick.time,
                                action_type = XCLOSE,
                            )
                        )
                        #TODO:这里需要设定虚拟被平，就是说如果已经启动平仓了，就不能下一秒再平
                        #     或者更进一步，直接认为平仓必然成功，然后设定已经被平标志，默认已经被平  
                        order.close_lock = True
                    if mysignal[2] != 0:#止损位置变化
                        logging.info(u'止损位变化.....')
                        is_touched = True
        if is_touched:
            self.save_state()
        return signals

    def check_open_signal(self,ctick):
        '''
            检查开仓信号返回信号集合[s1,s2,....]
            其中每个元素包含以下属性:
                合约号
                开仓方向
                开仓策略
                平仓函数
                最大手数
                基准价
        '''
        #print 'in check_open_signal'
        signals = []
        if ctick.instrument not in self.instruments:
            logging.warning(u'A_COS:需要监控的%s未记录行情数据')
            return signals
        cur_inst = self.instruments[ctick.instrument]
        for ss in cur_inst.strategy.values():
            #print u'检查开仓...%s:%s %s,ss.name=%s' % (ctick.min1,ctick.sec,ctick.msec,ss.name)
            mysignal = ss.opener.check(cur_inst.data,ctick)
            #print u'检查完毕..........'
            if mysignal[0] != 0:
                base_price = mysignal[1] if mysignal[1]>0 else ctick.price
                candidate = strategy.Order(#instrument=cur_inst,
                                position=cur_inst.position_detail[ss.name],
                                base_price=base_price,
                                target_price=ss.opener.calc_target_price(base_price,cur_inst.tick_base),
                                mytime = ctick.time,
                                action_type=XOPEN,
                                #direction = dir_py2ctp(ss.opener.direction),#内部根据策略处理
                            )
                ##这里不处理保证金，直接使用理论开仓数。后面在实际开仓时才处理
                #candidate.volume,margin_amount = self.calc_open_volume(cur_inst,candidate)
                #candidate.volume = self.calc_open_volume_pre(cur_inst,candidate)
                candidate.volume = 0    #开仓时在此处不需要处理开仓量
                #print 'candidate volume:',candidate.volume
                #if candidate.volume > 0:
                #    self.available -= (candidate.volume *margin_amount)  #锁定保证金
                #    signals.append(candidate)
                signals.append(candidate)    
        return signals

    def calc_open_volume_pre(self,instrument,order):
        '''
            计算order的理论开仓数(基于策略)
        '''
        return order.position.calc_open_volume()


    def lock_open_volume(self,instrument,order):
        '''
            计算order的可开仓数
            instrument: 合约对象

            先计算理论可开数，然后根据可用保证金调整. 并虚拟锁定保证金
        '''
        logging.info(u'计算并虚拟锁定实际开仓数')
        want_volume = order.position.calc_open_volume()
        inst_remained = order.instrument.calc_remained_volume()
        logging.info(u'A_COV1:want_volume=%s,inst_remained=%s' % (want_volume,inst_remained))
        if want_volume > inst_remained:
            want_volume = inst_remained
        if want_volume <= 0:
            return 0
        margin_amount = instrument.calc_margin_amount(order.target_price,order.position.strategy.direction)
        logging.info(u'A_COV2:理论开仓数:%s,单手保证金:%s' % (want_volume,margin_amount))

        if margin_amount <= 1:#不可能只有1块钱
            logging.error(u'合约%s保证金率未初始化' % (instrument.name,))
            return 0
        available_volume = int(self.available / margin_amount)
        logging.debug(u'A_COV3:可用保证金=%s,单手保证金=%s' % (int(self.available),margin_amount))
        if available_volume == 0:
            return 0
        logging.info(u'A_COV4:want_volume=%s,avaliable_volume=%s' % (want_volume,available_volume))
        if want_volume > available_volume:
            want_volume = available_volume
        self.available -= (want_volume *margin_amount)  #保证金虚拟锁定，在成交后解锁(必须是全部成交)或撤单后解锁
        return want_volume

    def make_command(self,orders):
        '''
            根据下单指令进行开/平仓
            开仓时,埋入一分钟后的撤单指令
            TODO: 平仓时考虑直接用市价单
        '''
        for order in orders:
            order.order_ref = self.inc_order_ref()
            command = BaseObject(instrument = order.instrument.name,
                    direction = order.direction,
                    price = order.target_price/10.0, #内部都是以0.1为计量单位
                    volume = order.volume,
                    order_ref = order.order_ref,
                    action_type = order.action_type,
                )
            if order.action_type == XOPEN:##开仓情况,X跳后不论是否成功均撤单
                #需要处理实际可开数和保证金虚拟锁定
                #...........开始计算
                order.volume = self.lock_open_volume(order.instrument,order) #计算可开数并锁住相应保证金(会在后面的成交后查询中解锁)
                if order.volume == 0:
                    logging.info(u'策略%s,可下单数=0,中止' % (order.position,))
                    continue
                ##有效Order
                self.actions.append(('open',order.mytime,order.direction,order.get_strategy_name(),order.base_price,order.volume,order.target_price))
                command.volume = order.volume
                self.ref2order[command.order_ref] = order
                ##初始化止损类
                #order.stoper = order.position.strategy.closer(order.instrument.data,order.base_price)
                order.init_stopers(order.instrument.data,order.base_price)
                order.position.add_order(order)
                #............ 加锁完毕. 这样，同一instrument本时刻再有其它策略的开仓时，其calc_remained_volume能返回合适值
                logging.info(u'A_MC:当前tick=%s,下单有效时长(超过该时长未成交则撤单)=%s' % (self.get_tick(),order.position.strategy.opener.valid_length,))
                self.put_command(self.get_tick()+order.position.strategy.opener.valid_length,fcustom(self.cancel_command,command=command))
                logging.info(u'A_MC_B:设置开仓撤单完成,cur_tick=%s,触发点=%s' % (self.get_tick(),self.get_tick()+order.position.strategy.opener.valid_length))
                self.open_position(command)
            else:#平仓, Y跳后不论是否成功均撤单, 撤单应该比开仓更快，避免追不上
                #print u'平仓'
                #self.ref2order[command.order_ref] = order.source_order
                logging.info(u'A_MC_C:平仓处理')
                self.actions.append(('close',order.mytime,order.direction,order.source_order.get_strategy_name(),order.base_price,order.volume,order.target_price))
                self.ref2order[command.order_ref] = order   #2011-8-6
                #self.put_command(self.get_tick()+order.source_order.stoper.valid_length,fcustom(self.cancel_command,command=command))
                #self.put_command(self.get_tick()+order.source_order.stoper.valid_length+1,lambda : order.source_order.release_close_lock())
                #logging.info(u'A_MC_D:设置平仓撤单完成,cur_tick=%s,触发点=%s' % (self.get_tick(),self.get_tick()+order.source_order.stoper.valid_length))
                self.put_command(self.get_tick()+order.source_order.get_stop_valid_length(),fcustom(self.cancel_command,command=command))
                self.put_command(self.get_tick()+order.source_order.get_stop_valid_length()+1,lambda : order.source_order.release_close_lock())
                logging.info(u'A_MC_D:设置平仓撤单完成,cur_tick=%s,触发点=%s' % (self.get_tick(),self.get_tick()+order.source_order.get_stop_valid_length()))
                #logging.info(u'发出平仓指令，cur_tick=%s,释放锁的时间是=%s' % (self.get_tick(),self.get_tick()+order.source_order.get_stop_valid_length()+1))
                logging.info(u'发出平仓指令，cur_tick=%s,price=%s,释放锁的时间是=%s' % (self.get_tick(),command.price,self.get_tick()+order.source_order.get_stop_valid_length()+1))
                self.close_position(command)


    def open_position(self,order):
        ''' 
            发出下单指令
        '''
        req = ustruct.InputOrder(
                InstrumentID = order.instrument,
                Direction = order.direction,
                OrderRef = str(order.order_ref),
                LimitPrice = order.price,   #有个疑问，double类型如何保证舍入舍出，在服务器端取整?
                VolumeTotalOriginal = order.volume,
                OrderPriceType = utype.THOST_FTDC_OPT_LimitPrice,
                
                BrokerID = self.cuser.broker_id,
                InvestorID = self.cuser.investor_id,
                CombOffsetFlag = utype.THOST_FTDC_OF_Open,         #开仓 5位字符,但是只用到第0位
                CombHedgeFlag = utype.THOST_FTDC_HF_Speculation,   #投机 5位字符,但是只用到第0位

                VolumeCondition = utype.THOST_FTDC_VC_AV,
                MinVolume = 1,  #这个作用有点不确定,有的文档设成0了
                ForceCloseReason = utype.THOST_FTDC_FCC_NotForceClose,
                IsAutoSuspend = 1,
                UserForceClose = 0,
                TimeCondition = utype.THOST_FTDC_TC_GFD,
            )
        logging.info(u'下单: instrument=%s,方向=%s,数量=%s,价格=%s' % (order.instrument,u'多' if order.direction==utype.THOST_FTDC_D_Buy else u'空',order.volume,order.price))
        r = self.trader.ReqOrderInsert(req,self.inc_request_id())

    #def close_position(self,order,CombOffsetFlag = utype.THOST_FTDC_OF_Close): #Close==CloseYesterday
    def close_position(self,order,CombOffsetFlag = utype.THOST_FTDC_OF_CloseToday):
        ''' 
            发出平仓指令. 默认平今仓
            是平今还是平昨，可以通过order的mytime解决
        '''
        sorder = self.ref2order[order.order_ref].source_order
        sday = sorder.mytime/1000000    #MMDD
        cday = self.scur_day % 10000    #MMDD
        logging.info(u'平仓: sday=%s,cday=%s' % (sday,cday))
        cos_flag = utype.THOST_FTDC_OF_CloseToday if sday >= cday else utype.THOST_FTDC_OF_Close    #sday>cday只会在模拟中出现，否则就是穿越了

        req = ustruct.InputOrder(
                InstrumentID = order.instrument,
                Direction = order.direction,
                OrderRef = str(order.order_ref),
                LimitPrice = order.price,
                VolumeTotalOriginal = order.volume,
                #CombOffsetFlag = CombOffsetFlag,
                CombOffsetFlag = cos_flag,
                OrderPriceType = utype.THOST_FTDC_OPT_LimitPrice,
                
                BrokerID = self.cuser.broker_id,
                InvestorID = self.cuser.investor_id,
                CombHedgeFlag = utype.THOST_FTDC_HF_Speculation,   #投机 5位字符,但是只用到第0位

                VolumeCondition = utype.THOST_FTDC_VC_AV,
                MinVolume = 1,  #TODO:这个有点不确定. 需要测试确认
                ForceCloseReason = utype.THOST_FTDC_FCC_NotForceClose,
                IsAutoSuspend = 1,
                UserForceClose = 0,
                TimeCondition = utype.THOST_FTDC_TC_GFD,
            )
        r = self.trader.ReqOrderInsert(req,self.inc_request_id())

    def cancel_command(self,command):
        '''
            发出撤单指令
        '''
        #print 'in cancel command'
        logging.info(u'A_CC:取消命令')
        req = ustruct.InputOrderAction(
                InstrumentID = command.instrument,
                OrderRef = str(command.order_ref),
                BrokerID = self.cuser.broker_id,
                InvestorID = self.cuser.investor_id,
                FrontID = self.front_id,
                SessionID = self.session_id,
                ActionFlag = utype.THOST_FTDC_AF_Delete,
                #OrderActionRef = self.inc_order_ref()  #没用,不关心这个，每次撤单成功都需要去查资金
            )
        r = self.trader.ReqOrderAction(req,self.inc_request_id())

    def finalize(self):
        pass

    def save_state(self):
        '''
            保存环境
        '''
        logging.info(u'保存执行状态.....................')
        state = BaseObject(last_update=int(time.strftime('%Y%m%d')),holdings={})
        cur_orders = {} #instrument==>orders
        for inst in self.instruments.values():
            for position in inst.position_detail.values():
                if position.opened_volume>0:
                    iorders = cur_orders.setdefault(position.instrument,[])
                    iorders.extend([order for order in position.orders if order.opened_volume>0])
        for inst,orders in cur_orders.items():
            cin = BaseObject(instrument = inst,opened_volume=sum([order.opened_volume for order in orders]),orders=orders)
            state.holdings[inst.name] = cin
        config.save_state(state)
        return
            
    def resume(self):
        '''
            恢复环境
            对每一个合约:
                1. 获得必要的历史数据
                2. 获得当日分钟数据, 并计算相关指标
                3. 获得当日持仓，并初始化止损. 
                4. 需要恢复当日opener的状态。ticks重新填入?
        '''
        ##resume order
        state = config.parse_state(self.strategy_cfg,self.instruments)
        cposs = set([])
        for chd in state.holdings.values():
            cur_inst = self.instruments[chd.instrument]
            for order in chd.orders:
                #order.stoper.data = cur_inst.data   #填充data, 另bline已经搞定
                cur_position = cur_inst.position_detail[order.strategy_name]
                xorder = strategy.Order(cur_position,order.base_price,order.target_price,order.mytime,order.action_type)
                xorder.volume = xorder.opened_volume = order.volume
                xorder.trade_detail.append((order.base_price,order.volume,order.mytime))
                #xorder.stoper = order.stoper
                xorder.stopers = order.stopers
                xorder.set_stopers_data(cur_inst.data)
                xorder.cancelled = True #需要手工撤掉未成交的单子
                #cur_position.add_order(order)
                cur_position.add_order(xorder)
                cposs.add(cur_position)
        for pos in cposs:
            pos.re_calc()

        ##resume opener
        for cur_inst in self.instruments.values():
            for ss in cur_inst.strategy.values():
                ss.opener.resume(cur_inst.data,self.scur_day)
        return state

    def day_switch(self,scur_day):  #重新初始化opener
        self.scur_day = scur_day
        self.isSettlementInfoConfirmed = False
        self.actions = []
        for cur_inst in self.instruments.values():
            cur_inst.day_switch()

    ###交易

    ###回应
    def rtn_trade(self,strade):
        '''
            成交回报
            #TODO: 必须考虑出现平仓信号时，position还没完全成交的情况
                   在OnTrade中进行position的细致处理 
            #TODO: 必须处理策略分类持仓汇总和持仓总数不匹配时的问题
        '''
        logging.info(u'A_RT1:成交回报,%s:orderref=%s,orders=%s,price=%s' % (strade.InstrumentID,strade.OrderRef,self.ref2order,strade.Price))
        if int(strade.OrderRef) not in self.ref2order or strade.InstrumentID not in self.instruments:
            logging.warning(u'A_RT2:收到非本程序发出的成交回报:%s-%s' % (strade.InstrumentID,strade.OrderRef))
        cur_inst = self.instruments[strade.InstrumentID]
        myorder = self.ref2order[int(strade.OrderRef)]
        if myorder.action_type == XOPEN:#开仓, 也可用pTrade.OffsetFlag判断
            is_completed = myorder.on_trade(price=int(strade.Price*10+0.1),volume=strade.Volume,trade_time=strade.TradeTime)
            logging.info(u'A_RT31,开仓回报');
            cur_inst.add_vtimes(strade.Volume)
        else:
            myorder.source_order.on_close(price=int(strade.Price*10+0.1),volume=strade.Volume,trade_time=strade.TradeTime)
            logging.info(u'A_RT32,平仓回报,price=%s,time=%s' % (strade.Price,strade.TradeTime));
            cur_inst.add_profit(myorder.source_order.get_profit())
        self.save_state()
        ##查询可用资金
        #print 'fetch_trading_account'
        #if myorder.action_type == XCLOSE or is_completed:#平仓或者开仓完全成交
        #    self.put_command(self.get_tick()+1,self.fetch_trading_account)
        self.put_command(self.get_tick()+1,self.fetch_trading_account)  #不完全成交也可以，也就是多查询几次。有可能被抑制


    def rtn_order(self,sorder):
        '''
            交易所接受下单回报(CTP接受的已经被过滤)
            暂时只处理撤单的回报. 
        '''
        #print str(sorder)
        logging.info(u'成交/撤单回报:%s' % (str(sorder,)))
        if sorder.OrderStatus == utype.THOST_FTDC_OST_Canceled or sorder.OrderStatus == utype.THOST_FTDC_OST_PartTradedNotQueueing:   #完整撤单或部成部撤
            logging.info(u'撤单, 撤销开/平仓单')
            ##查询可用资金
            self.put_command(self.get_tick()+1,self.fetch_trading_account)
            ##处理相关Order
            myorder = self.ref2order[int(sorder.OrderRef)]
            if myorder.action_type == XOPEN:    #开仓指令cancel时需要处理，平仓指令cancel时不需要处理
                logging.info(u'撤销开仓单')
                myorder.on_cancel()

    def err_order_insert(self,order_ref,instrument_id,error_id,error_msg):
        '''
            ctp/交易所下单错误回报，不区分ctp和交易所
            正常情况下不应当出现
        '''
        pass    #可以忽略

    def err_order_action(self,order_ref,instrument_id,error_id,error_msg):
        '''
            ctp/交易所撤单错误回报，不区分ctp和交易所
            必须处理，如果已成交，撤单后必然到达这个位置
        '''
        logging.info(u'撤单时已成交，error_id=%s,error_msg=%s' %(error_id,error_msg))
        myorder = self.ref2order[int(order_ref)]
        if myorder.action_type == XOPEN and int(error_id) == 26:
            #开仓指令cancel时需要处理，平仓指令cancel时不需要处理
            logging.info(u'撤销开仓单')
            myorder.on_cancel()
        
    
    ###辅助   
    def rsp_qry_position(self,position):
        '''
            查询持仓回报, 每个合约最多得到4个持仓回报，历史多/空、今日多/空
        '''
        logging.info(u'agent 持仓:%s' % str(position))
        if position != None:    
            cur_position = self.instruments[position.InstrumentID].position
            if position.PosiDirection == utype.THOST_FTDC_PD_Long:
                if position.PositionDate == utype.THOST_FTDC_PSD_Today:
                    cur_position.clong = position.Position  #TodayPosition
                else:
                    cur_position.hlong = position.Position  #YdPosition
            else:#空头
                if position.PositionDate == utype.THOST_FTDC_PSD_Today:
                    cur_position.cshort = position.Position #TodayPosition
                else:
                    cur_position.hshort = position.Position #YdPosition
        else:#无持仓信息，保持默认设置
            pass
        self.check_qry_commands() 

    def rsp_qry_instrument_marginrate(self,marginRate):
        '''
            查询保证金率回报. 
        '''
        self.instruments[marginRate.InstrumentID].marginrate = (marginRate.LongMarginRatioByMoney,marginRate.ShortMarginRatioByMoney)
        #print marginRate.InstrumentID,self.instruments[marginRate.InstrumentID].marginrate
        self.check_qry_commands()

    def rsp_qry_trading_account(self,account):
        '''
            查询资金帐户回报
        '''
        self.available = account.Available
        self.check_qry_commands()        
    
    def rsp_qry_instrument(self,pinstrument):
        '''
            获得合约数量乘数. 
            这里的保证金率应该是和期货公司无关，所以不能使用
        '''
        if pinstrument.InstrumentID not in self.instruments:
            logging.warning(u'A_RQI:收到未监控的合约查询:%s' % (pinstrument.InstrumentID))
            return
        self.instruments[pinstrument.InstrumentID].multiple = pinstrument.VolumeMultiple
        self.instruments[pinstrument.InstrumentID].tick_base = int(pinstrument.PriceTick * 10 + 0.1)
        #print 'tick_base = %s' % (pinstrument.PriceTick,)
        self.check_qry_commands()

    def rsp_qry_position_detail(self,position_detail):
        '''
            查询持仓明细回报, 得到每一次成交的持仓,其中若已经平仓,则持量为0,平仓量>=1
            必须忽略
        '''
        print str(position_detail)
        self.check_qry_commands()

    def rsp_qry_order(self,sorder):
        '''
            查询报单
            可以忽略
        '''
        self.check_qry_commands()

    def rsp_qry_trade(self,strade):
        '''
            查询成交
            可以忽略
        '''
        self.check_qry_commands()


class SaveAgent(Agent):
    def init_init(self):
        Agent.init_init(self)
        self.save_flag = True

    def RtnTick(self,ctick):#行情处理主循环
        inst = ctick.instrument
        if inst not in self.instruments:
            logging.info(u'接收到未订阅的合约数据:%s' % (inst,))
            return False
        if ctick.min1 > LAST_TRADE_TIME:
            logging.info(u'接收到不在时间范围的合约数据:%s:%s' % (inst,ctick.min1))
            return False
        dinst = self.instruments[inst]#.data
        print inst,ctick.min1
        ctick.iorder = dinst.get_order(ctick.min1)
        if (ctick.iorder < dinst.data.cur_min.viorder and ctick.date == dinst.data.cur_min.vdate) or ctick.date < dinst.data.cur_min.vdate:
            #print ctick.date,ctick.time,dinst.data.cur_min.vdate,dinst.data.cur_min.vtime
            return False
        self.prepare_base(dinst,ctick)  
    
    def rsp_qry_instrument(self,pinstrument):
        '''
            获得合约名称
        '''
        if pinstrument.InstrumentID not in self.instruments:
            self.instruments[pinstrument.InstrumentID] = c_instrument(pinstrument.InstrumentID,t2order=self.t2order)


def make_user(my_agent,hq_user,name='data'):
    user = MdApi.CreateMdApi(name)
    #print my_agent.instruments
    user.RegisterSpi(MdSpiDelegate(instruments=my_agent.instruments, 
                             broker_id=hq_user.broker_id,
                             investor_id= hq_user.investor_id,
                             passwd= hq_user.passwd,
                             agent = my_agent,
                    ))
    user.RegisterFront(hq_user.port)
    
    user.Init()


def save_raw(base_name='base.ini',strategy_name='strategy.ini',base='Base',strategy='strategy'):
    '''
        按配置文件给定的绝对合约名保存
        只用到MdUser
        base_name是保存base设置的文件名
        strategy_name是保存strategy设置的文件名

    '''
    logging.basicConfig(filename="ctp_user_agent.log",level=logging.INFO,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')

 
    base_cfg = config.parse_base(base_name,base)
    strategy_cfg = config.parse_strategy(strategy_name,strategy)
 
    my_insts = strategy_cfg.traces_raw

    #my_agent = SaveAgent(None,None,my_insts,{})
    my_agent = SaveAgent(None,None,my_insts,strategy_cfg)
    
    for user in base_cfg.users:
        make_user(my_agent,base_cfg.users[user],user)

    #获取合约列表
    return my_agent

def save_raw2():
    return save_raw(base_name='mybase.ini')


def save(base_name='base.ini',strategy_name='strategy.ini',base='Base',strategy='strategy'): 
    '''
        根据配置文件给定的合约类型，查找所有合约，然后保存
        用到了User和Trader
    '''
    logging.basicConfig(filename="ctp_user_agent.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
 
    cfg = config.parse_base(base_name,base)
    strategy_cfg = config.parse_strategy(strategy_name,strategy)
 
    ctrader = cfg.traders.values()[0]
    trader = TraderApi.CreateTraderApi(ctrader.name)
    t_agent = SaveAgent(trader,ctrader,[],strategy_cfg)
    
    myspi = TraderSpiDelegate(instruments=t_agent.instruments, 
                             broker_id=ctrader.broker_id,
                             investor_id= ctrader.investor_id,
                             passwd= ctrader.passwd,
                             agent = t_agent,
                       )
    trader.RegisterSpi(myspi)
    trader.myspi = myspi
    trader.SubscribePublicTopic(THOST_TERT_QUICK)
    trader.SubscribePrivateTopic(THOST_TERT_QUICK)
    trader.RegisterFront(ctrader.port)
    trader.Init()
    
    
    time.sleep(20)
    #print strategy_cfg.traces
    for tin in strategy_cfg.traces:
        print tin
        t_agent.fetch_instrument(tin)
        time.sleep(30)

    #for user in cfg.users:
    #    make_user(my_agent,cfg.users[user],user)

    #获取合约列表
    return t_agent

def save2():
    return save(base_name='mybase.ini')


def create_trader(name='base.ini',base='Base',sname='strategy.ini',t2order=t2order_if):
    logging.basicConfig(filename="ctp_trade.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    
    trader = TraderApi.CreateTraderApi("trader")
    
    strategy_cfg = config.parse_strategy(name=sname)
    cfg = config.parse_base(name,base)

    #模拟trader
    cuser = cfg.traders.values()[0]
    logging.info(u'broker_id=%s,investor_id=%s,passwd=%s' % (cuser.broker_id,cuser.investor_id,cuser.passwd))

    instruments = list(strategy_cfg.traces_raw)
    myagent = Agent(trader,cuser,instruments,strategy_cfg,t2order=t2order) 
    myspi = TraderSpiDelegate(instruments=myagent.instruments, 
                             broker_id=cuser.broker_id,
                             investor_id= cuser.investor_id,
                             passwd= cuser.passwd,
                             agent = myagent,
                       )
    trader.RegisterSpi(myspi)
    trader.myspi = myspi
    trader.SubscribePublicTopic(THOST_TERT_QUICK)
    trader.SubscribePrivateTopic(THOST_TERT_QUICK)
    trader.RegisterFront(cuser.port)
    trader.Init()
    return trader,myagent


def trade_test_main(name='base.ini',base='Base'):
    '''
    import agent
    trader,myagent = agent.trade_test_main()
    #开仓
    
    ##释放连接
    trader.RegisterSpi(None)
    '''
    logging.basicConfig(filename="ctp_trade.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    

    trader = TraderApi.CreateTraderApi("trader")

    cfg = config.parse_base(name,base)

    cuser = cfg.traders.values()[0]
    
    #cuser = c.SQ_TRADER2
    my_agent = Agent(trader,cuser,INSTS,{})
    myspi = TraderSpiDelegate(instruments=my_agent.instruments, 
                             broker_id=cuser.broker_id,
                             investor_id= cuser.investor_id,
                             passwd= cuser.passwd,
                             agent = my_agent,
                       )
    trader.RegisterSpi(myspi)
    trader.myspi = myspi
    trader.SubscribePublicTopic(THOST_TERT_QUICK)
    trader.SubscribePrivateTopic(THOST_TERT_QUICK)
    trader.RegisterFront(cuser.port)
    trader.Init()
    return trader,my_agent
    
'''
#测试
import agent
trader,myagent = agent.trade_test_main()

myagent.spi.OnRspOrderInsert(agent.BaseObject(OrderRef='12',InstrumentID='IF1103'),agent.BaseObject(ErrorID=1,ErrorMsg='test'),1,1)
myagent.spi.OnErrRtnOrderInsert(agent.BaseObject(OrderRef='12',InstrumentID='IF1103'),agent.BaseObject(ErrorID=1,ErrorMsg='test'))
myagent.spi.OnRspOrderAction(agent.BaseObject(OrderRef='12',InstrumentID='IF1103'),agent.BaseObject(ErrorID=1,ErrorMsg='test'),1,1)
myagent.spi.OnErrRtnOrderAction(agent.BaseObject(OrderRef='12',InstrumentID='IF1103'),agent.BaseObject(ErrorID=1,ErrorMsg='test'))

#资金和持仓
myagent.fetch_trading_account()
myagent.fetch_investor_position(u'IF1104')
myagent.fetch_instrument_marginrate(u'IF1104')
myagent.fetch_instrument(u'IF1104')
#myagent.fetch_investor_position_detail(u'IF1104')


#测试报单
morder = agent.BaseObject(instrument='IF1103',direction='0',order_ref=myagent.inc_order_ref(),price=3280,volume=1)
myagent.open_position(morder)
morder = agent.BaseObject(instrument='IF1103',direction='0',order_ref=myagent.inc_order_ref(),price=3280,volume=20)

#平仓
corder = agent.BaseObject(instrument='IF1103',direction='1',order_ref=myagent.inc_order_ref(),price=3220,volume=1)
myagent.close_position(corder)

#测试撤单
import agent
trader,myagent = agent.trade_test_main()

cref = myagent.inc_order_ref()
morder = agent.BaseObject(instrument='IF1104',direction='0',order_ref=cref,price=3180,volume=1)
myagent.open_position(morder)

rorder = agent.BaseObject(instrument='IF1103',order_ref=cref)
myagent.cancel_command(rorder)


'''


if __name__=="__main__":
    main()
