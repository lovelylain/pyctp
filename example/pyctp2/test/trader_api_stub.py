# -*- coding: utf-8 -*-

"""
    用作TraderSpi的Stub
"""

import logging
from datetime import datetime

from ctp.futures import TraderApi
from ctp.futures import ApiStruct as UStruct
from ctp.futures import ApiStruct as UType

from ..common.base import BaseObject,LONG,SHORT,TICK
from ..common.base import TEST_PATH as LOG_PATH
from ..common.contract_type import CM_ALL_TEST as call,ContractInfo


class TraderApiStub(TraderApi):
    logger = logging.getLogger('ctp.TraderApiStub')

    def Create(self,account,available = 1000000):
        self._account = account
        self._trading_day = datetime.now().strftime("%Y%m%d")
        self._exchange = ExchangeStub(self._trading_day,available)
        self._exchange_id = "TAStub_Exchange"
        self._investor_id = "TAStub_Investor"
        self._broker_id = "TAStub_BrokerID"
        self._front_id = 0
        self._session_id = 999999
        self._defaultReqInfo = BaseObject(BrokerID = self._broker_id,InvestorID = self._investor_id)
        self._suceessRspInfo = UStruct.RspInfo(0,b"No errors")
        self._failureRspInfo = UStruct.RspInfo(1,b"Error")
        self._init_order_ref = 10000000
        self._current_order_sys_id = 20000000
        #self._contracts = dict([(contract.name,contract) for contract in call.current_contracts()])
        self._contracts = {} #name=>contracts的映射,在QueryInstrument中填充
        self._ctick = TICK(instrument='C_STUB',date=self._trading_day)
        self._last_tick_map = {}    #instrument_id => last_tick
        self._wlist = {}     #contract_name ==> pOrder的列表,等待成交
        self._cancelled = 0  #仅用于测试
        self._cancel_after_traded = 0
        self._orders = []

    @property
    def contracts(self):
        return self._contracts

    @property
    def cancelled(self):
        return self._cancelled

    @property
    def last_tick_map(self):
        return self._last_tick_map

    @property
    def cancel_after_traded(self):
        return self._cancel_after_traded

    @property
    def exchange(self):
        return self._exchange

    @property
    def available(self):
        return self._exchange._available

    def inc_order_sys_id(self):
        self._current_order_sys_id += 1
        return self._current_order_sys_id

    def _add_contract(self,contract):
        """
            添加可被测试用到的contract. 仅用于测试,不用于模拟
        """
        self._contracts[contract.name] = contract    #不判断直接赋值

    def new_tick(self,tick):
        """
            设置所需用到的成交价格
        """
        self._ctick = tick
        self._last_tick_map[tick.instrument] = tick
        #print(tick.instrument,tick.time)
        self._check_trade(tick)     #判断是否有新的成交

    def ReqParkedOrderAction(self, pParkedOrderAction, nRequestID):
        '''预埋撤单录入请求'''
        #未实现
        pass

    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount, nRequestID):
        '''期货发起查询银行余额请求'''
        #未实现
        pass

    def ReqQryTrade(self, pQryTrade, nRequestID):
        '''请求查询成交'''
        #未实现
        pass

    def ReqParkedOrderInsert(self, pParkedOrder, nRequestID):
        '''预埋单录入请求'''
        #未实现
        pass

    def ReqRemoveParkedOrder(self, pRemoveParkedOrder, nRequestID):
        '''请求删除预埋单'''
        #未实现
        pass

    def ReqQryParkedOrder(self, pQryParkedOrder, nRequestID):
        '''请求查询预埋单'''
        #未实现
        pass

    def ReqAuthenticate(self, pReqAuthenticateField, nRequestID):
        '''客户端认证请求'''
        #未实现
        pass

    def ReqQryTransferBank(self, pQryTransferBank, nRequestID):
        '''请求查询转帐银行'''
        #未实现
        pass

    def RegisterFront(self, pszFrontAddress):
        '''注册前置机网络地址
@param pszFrontAddress：前置机网络地址。
@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。'''
        #Stub不需要注册
        self.logger.info("TAStub-RF:%s" % (pszFrontAddress,))
        pass

    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin, nRequestID):
        '''请求查询投资者品种/跨品种保证金'''
        #未实现
        pass

    def SubscribePrivateTopic(self, nResumeType):
        '''订阅私有流。
@param nResumeType 私有流重传方式
        THOST_TERT_RESTART:从本交易日开始重传
        THOST_TERT_RESUME:从上次收到的续传
        THOST_TERT_QUICK:只传送登录后私有流的内容
@remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。'''
        #Stub不需要实现
        pass

    def ReqFromBankToFutureByFuture(self, pReqTransfer, nRequestID):
        '''期货发起银行资金转期货请求'''
        #未实现
        pass


    def ReqQryEWarrantOffset(self, pQryEWarrantOffset, nRequestID):
        '''请求查询仓单折抵信息'''
        #未实现
        pass

    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction, nRequestID):
        '''请求删除预埋撤单'''
        #未实现
        pass

    def ReqQryParkedOrderAction(self, pQryParkedOrderAction, nRequestID):
        '''请求查询预埋撤单'''
        #未实现
        pass

    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate, nRequestID):
        '''请求查询交易所保证金率'''
        #未实现
        pass

    def ReqUserLogout(self, pUserLogout, nRequestID):
        '''登出请求'''
        #Stub不需要实现
        pass

    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust, nRequestID):
        '''请求查询交易所调整保证金率'''
        #未实现
        pass

    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm, nRequestID):
        '''投资者结算结果确认'''
        self.OnRspSettlementInfoConfirm(pSettlementInfoConfirm, self._suceessRspInfo, nRequestID, True)

    def Join(self, ):
        '''等待接口线程结束运行
@return 线程退出代码'''
        #Stub不需要实现
        pass

    def ReqQryDepthMarketData(self, pQryDepthMarketData, nRequestID):
        '''请求查询行情'''
        if pQryDepthMarketData.InstrumentID in self._last_tick_map:
            cp = self._last_tick_map[pQryDepthMarketData.InstrumentID].price
            uprice = cp * 1.05
            lprice = cp * .95
            #print(pQryDepthMarketData.InstrumentID,cp,uprice,lprice)
        else:
            uprice = 99999999
            lprice = 0
        dmdata = UStruct.DepthMarketData(InstrumentID=pQryDepthMarketData.InstrumentID,TradingDay=self._trading_day,UpperLimitPrice=uprice,LowerLimitPrice=lprice)
        self.OnRspQryDepthMarketData(dmdata, self._suceessRspInfo, nRequestID, True)
        self.logger.info("TAStub-RQDMD:%s" % (pQryDepthMarketData.InstrumentID,))

    def RegisterFensUserInfo(self, pFensUserInfo):
        '''注册名字服务器用户信息
@param pFensUserInfo：用户信息。'''
        #未实现
        pass

    def ReqQryInvestor(self, pQryInvestor, nRequestID):
        '''请求查询投资者'''
        #未实现
        pass

    def ReqFromFutureToBankByFuture(self, pReqTransfer, nRequestID):
        '''期货发起期货资金转银行请求'''
        #未实现
        pass

    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate, nRequestID):
        '''请求查询合约保证金率'''
        #print("query marginrate:",pQryInstrumentMarginRate.InstrumentID)
        im = UStruct.InstrumentMarginRate(InstrumentID=pQryInstrumentMarginRate.InstrumentID,LongMarginRatioByMoney=0.1,ShortMarginRatioByMoney=0.1)
        self.OnRspQryInstrumentMarginRate(im, self._suceessRspInfo, nRequestID, True)

    def ReqOrderInsert(self, pInputOrder, nRequestID):
        '''报单录入请求
            设定: (与实际不符, 只为了测试相关分支)
                普通合约名错误     CTP_REJECT
                特定合约名(CERROR)错误     EXCHANGE_REJECT
                    保证金错误       EXCHANGE_REJECT

        '''
        #print("ROI:direction:",pInputOrder.Direction)
        self.logger.info("TAStub-ROI:%s" % (str(pInputOrder),))
        print("TAStub-ROI:%s" % (str(pInputOrder),))
        #print("ROI:1:",pInputOrder.InstrumentID)
        if pInputOrder.InstrumentID[:2] == "XH":    #测试CTP_REJECT专用通道
            #调用CTP_REJECT
            self.OnRspOrderInsert(pInputOrder, self._failureRspInfo, nRequestID, True)
            return

        self._orders.append(pInputOrder)
        last_tick = self._last_tick_map[pInputOrder.InstrumentID]
        pOrder = UStruct.Order(InstrumentID=pInputOrder.InstrumentID,
                               LimitPrice = pInputOrder.LimitPrice,
                               Direction = pInputOrder.Direction,
                               VolumeTotalOriginal = pInputOrder.VolumeTotalOriginal,
                               #TradingDay = self.trading_day,
                               TradingDay = last_tick.date,
                               UpdateTime = last_tick.time,
                               OrderRef = nRequestID,
                               FrontID = self._front_id,
                               SessionID = self._session_id,
                               OrderStatus = UType.OST_Unknown,
                               CombOffsetFlag = pInputOrder.CombOffsetFlag,
                            )
        #print(pOrder)
        #efunc = self._exchange.add if pInputOrder.CombOffsetFlag == UType.OF_Open else self._exchange.remove
        efunc = self._exchange.lock if pInputOrder.CombOffsetFlag == UType.OF_Open else self._exchange.check_holding
        if not efunc(self._contracts[pInputOrder.InstrumentID],pInputOrder.Direction,pInputOrder.VolumeTotalOriginal,pOrder.LimitPrice):
            #保证金或平仓数不够, CTP拒绝
            logging.warning("TAStub-ROI:CTP拒绝")
            #print("TAStub-ROI:CTP拒绝")
            self.OnErrRtnOrderInsert(pInputOrder, self._failureRspInfo)
            pOrder.OrderSubmitStatus = UType.OSS_InsertRejected
            self.OnRtnOrder(pOrder)
            return
        #print("TAStub-ROI:CTP ACCEPT")

        #CTP_ACCEPT
        pOrder.OrderSubmitStatus = UType.OSS_InsertSubmitted
        self.OnRtnOrder(pOrder)
        #print("ROI CTP ACCEPTED: ",pInputOrder.InstrumentID)
        if pInputOrder.InstrumentID[:2] == "XX":
            #调用EXCHANGE_REJECT,
            self.OnErrRtnOrderInsert(pInputOrder, self._failureRspInfo)
            pOrder.OrderSubmitStatus = UType.OSS_InsertRejected
            self.OnRtnOrder(pOrder) #理论上应该有两次reject调用
            return

        #EXCHANGE_ACCEPT
        #print("ROI EXCHANGE ACCEPTED: ",pInputOrder.InstrumentID)
        pOrder.ExchangeID = self._exchange_id
        pOrder.OrderSysID = self.inc_order_sys_id()
        pOrder.OrderSubmitStatus = UType.OSS_Accepted
        self.OnRtnOrder(pOrder) #

        pOrder.volume_wanted = pInputOrder.VolumeTotalOriginal
        self._wlist.setdefault(pOrder.InstrumentID,[]).append(pOrder)
        #print("TAStub-ROI last_tick:",last_tick,last_tick.instrument,pOrder.InstrumentID,last_tick.price,pOrder.LimitPrice)
        self._check_trade(last_tick)
        #print("ExchangeStub.available:",self.exchange.available)
        #self._account.update_available(self.exchange.available)
        self._account.update(self._account._stamp+1,self.exchange.balance,self.exchange.available,self.exchange.margin,self.exchange.locked)
        #print(self._account.available,self.exchange.available)
        print("ExchangeStub.available:",self.exchange.available)

    def _check_trade(self,last_tick):
        if last_tick.instrument not in self._wlist:
            return
        pOrders = self._wlist[last_tick.instrument]
        untouched = []
        for pOrder in pOrders:
            if self._check_trade_one(pOrder,last_tick):
                pOrder.is_done = True
            else:
                untouched.append(pOrder)
        self._wlist[last_tick.instrument] = untouched

    def _check_trade_one(self,pOrder,last_tick):
        #print(last_tick.price,pOrder.LimitPrice)
        if pOrder.Direction == UType.D_Buy and last_tick.price > pOrder.LimitPrice:
            return False
        elif pOrder.Direction == UType.D_Sell and last_tick.price < pOrder.LimitPrice:
            return False

        #print("check_trade_one:True")

        #其它完成状态. 通道测试(非逻辑!!)
        #RTN_ORDER_DONE, 各种状态, 因为trade_matcher中允许多次on_done,所以这么测试分支没有问题

        #正确完成状态: 全部成功
        pOrder.VolumeTraded = pOrder.volume_wanted
        pOrder.OrderStatus = UType.OST_AllTraded
        self.OnRtnOrder(pOrder) #

        #RTN_TRADE
        pTrade = UStruct.Trade(InstrumentID=pOrder.InstrumentID,
                               Direction = pOrder.Direction,
                               ExchangeID = self._exchange_id,
                               OrderSysID = pOrder.OrderSysID,
                               #TradingDay = self.trading_day,
                               TradingDay = last_tick.date,
                               TradeDate = last_tick.date,
                               TradeTime = last_tick.time,
                               Volume = pOrder.VolumeTraded,
                               Price = last_tick.price,
                )
        self.OnRtnTrade(pTrade)
        if pOrder.CombOffsetFlag == UType.OF_Open:
            self._exchange.add(self._contracts[pOrder.InstrumentID],pOrder.Direction,pOrder.VolumeTotalOriginal,last_tick.price,pOrder.LimitPrice)
        else:
            self._exchange.remove(self._contracts[pOrder.InstrumentID],pOrder.Direction,pOrder.VolumeTotalOriginal,last_tick.price)
        #print("ROI SUCCESS: ",pInputOrder.InstrumentID)
        return True

    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail, nRequestID):
        '''请求查询投资者持仓明细'''
        #未实现
        pass

    def ReqQryTradingAccount(self, pQryTradingAccount, nRequestID):
        '''请求查询资金账户'''
        self.logger.info("TAStub-RTA:%s" % (str(pQryTradingAccount),))
        ta = UStruct.TradingAccount(TradingDay=self._trading_day,
                                    Available=self._exchange.available,
                                    Balance=self._exchange.balance,
                                    CurrMargin=self._exchange.margin,
                    )
        self.OnRspQryTradingAccount(ta, self._suceessRspInfo, nRequestID, True)

    def SubscribePublicTopic(self, nResumeType):
        '''订阅公共流。
@param nResumeType 公共流重传方式
        THOST_TERT_RESTART:从本交易日开始重传
        THOST_TERT_RESUME:从上次收到的续传
        THOST_TERT_QUICK:只传送登录后公共流的内容
@remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。'''
        #Stub不须实现
        pass

    def RegisterNameServer(self, pszNsAddress):
        '''注册名字服务器网络地址
@param pszNsAddress：名字服务器网络地址。
@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。
@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
@remark RegisterNameServer优先于RegisterFront'''
        #Stub不须实现
        pass

    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm, nRequestID):
        '''请求查询结算信息确认'''
        #暂不实现
        pass

    def ReqQryExchange(self, pQryExchange, nRequestID):
        '''请求查询交易所'''
        #未实现
        pass

    def ReqQryOrder(self, pQryOrder, nRequestID):
        '''请求查询报单'''
        #未实现
        pass

    def ReqQryNotice(self, pQryNotice, nRequestID):
        '''请求查询客户通知'''
        #未实现
        pass

    def ReqQryInstrument(self, pQryInstrument, nRequestID):
        '''请求查询合约'''
        self.logger.info("TAStub-RQI:%s" % (str(pQryInstrument),))
        ctype = call.cname2ctype(pQryInstrument.InstrumentID)
        contract = ContractInfo(pQryInstrument.InstrumentID,ctype)
        self._add_contract(contract)
        instr = UStruct.Instrument(InstrumentID=pQryInstrument.InstrumentID,ExchangeID=ctype.exchange_name,PriceTick=ctype.unit,VolumeMultiple=ctype.multiplier)
        self.OnRspQryInstrument(instr, self._suceessRspInfo, nRequestID, True)

    def ReqQueryMaxOrderVolume(self, pQueryMaxOrderVolume, nRequestID):
        '''查询最大报单数量请求'''
        #未实现
        pass

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, nRequestID):
        '''请求查询合约手续费率'''
        #未实现
        pass

    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, nRequestID):
        '''资金账户口令更新请求'''
        #未实现
        pass

    def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        '''用户登录请求'''
        self.logger.info("TAStub-ROI:%s" % (str(pReqUserLoginField),))
        rul = UStruct.RspUserLogin(BrokerID=self._broker_id,FrontID=self._front_id,SessionID=self._session_id,MaxOrderRef=self._init_order_ref,TradingDay=self._trading_day)
        self.OnRspUserLogin(rul, self._suceessRspInfo, nRequestID, True)

    def Init(self, ):
        '''初始化
@remark 初始化运行环境,只有调用后,接口才开始工作'''
        pass

    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey, nRequestID):
        '''请求查询保证金监管系统经纪公司资金账户密钥'''
        #未实现
        pass

    def ReqQryContractBank(self, pQryContractBank, nRequestID):
        '''请求查询签约银行'''
        #未实现
        pass

    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, nRequestID):
        '''用户口令更新请求'''
        #未实现
        pass

    def GetTradingDay(self, ):
        '''获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日'''
        return self._trading_day

    def ReqQryTradingNotice(self, pQryTradingNotice, nRequestID):
        '''请求查询交易通知'''
        #未实现
        pass

    def ReqQryAccountregister(self, pQryAccountregister, nRequestID):
        '''请求查询银期签约关系'''
        #未实现
        pass

    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos, nRequestID):
        '''请求查询经纪公司交易算法'''
        #未实现
        pass

    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams, nRequestID):
        '''请求查询经纪公司交易参数'''
        #未实现
        pass

    def ReqQryTransferSerial(self, pQryTransferSerial, nRequestID):
        '''请求查询转帐流水'''
        #未实现
        pass

    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail, nRequestID):
        '''请求查询投资者持仓明细'''
        #未实现
        pass

    def ReqQryInvestorPosition(self, pQryInvestorPosition, nRequestID):
        '''请求查询投资者持仓'''
        #未实现
        pass

    def ReqOrderAction(self, pInputOrderAction, nRequestID):
        '''报单操作请求'''
        #撤单, 交易成功, 为测试调用CTP/EXCHANGE撤单错误
        self.logger.info("TAStub-ROA:%s" % (str(pInputOrderAction),))
        target_order = None
        if pInputOrderAction.InstrumentID in self._wlist:
            i = -1
            porders = self._wlist[pInputOrderAction.InstrumentID]
            for porder in porders:
                i += 1
                if porder.ExchangeID == pInputOrderAction.ExchangeID and porder.OrderSysID == pInputOrderAction.OrderSysID:
                    target_order = porder
                    break
            if i>=0:
                del porders[i]

        if target_order:
            #print("撤单")
            self._cancelled += 1
            #取消的各种状态
            #莫名失败
            porder.OrderStatus = UType.OST_NoTradeNotQueueing
            self.OnRtnOrder(porder) #
            #部分取消
            porder.OrderStatus = UType.OST_PartTradedNotQueueing
            self.OnRtnOrder(porder) #
            #全部取消
            porder.OrderStatus = UType.OST_Canceled
            self.OnRtnOrder(porder) #
        else:   #在CancelInstruction中作了设置,正常不可能进这个分支
            #已经成交
            self._cancel_after_traded += 1
            #print("已经成交,不能撤单")
            pioa = UStruct.InputOrderAction()
            self.OnRspOrderAction(pioa, self._failureRspInfo, nRequestID, True)
            poa = UStruct.OrderAction()
            self.OnErrRtnOrderAction(poa, self._failureRspInfo)

    def Release(self, ):
        '''删除接口对象本身
@remark 不再使用本接口对象时,调用该函数删除接口对象'''
        pass

    def ReqQrySettlementInfo(self, pQrySettlementInfo, nRequestID):
        '''请求查询投资者结算结果'''
        si = UStruct.SettlementInfo(TradingDay=self._trading_day)
        self.OnRspQrySettlementInfo(si, self._suceessRspInfo, nRequestID, True)

    def ReqQryTradingCode(self, pQryTradingCode, nRequestID):
        '''请求查询交易编码'''
        #未实现
        pass


class ExchangeStub(object):
    def __init__(self,trading_day,available=1000000,marginrate=0.12,charge=3.0/1000):
        self._holdings = {}
        self._trading_day = trading_day
        self._available = available
        self._margin = 0
        self._locked = 0
        self._marginrate = marginrate
        self._charge = charge #手续费
        #self._fhistory = open("%s/%s_%s.txt"%(LOG_PATH,"trade_history",self._trading_day),"at")
        self._log_fname = "%s/%s_%s.txt"%(LOG_PATH,"trade_history",self._trading_day)

    def finalize(self):
        pass
        #self._fhistory.close()

    @property
    def available(self):
        return self._available

    @property
    def margin(self):
        return self._margin

    @property
    def balance(self):
        return self._available + self._margin

    @property
    def charge(self):
        return self._charge

    @property
    def locked(self):
        return self._locked

    def resume(self,items):
        """
            #deprecated, 用cjson.dump/load来解决
            items中无重复合约, item:PosInfo
        """
        for item in items:
            if item.num_long > 0:
                self._holdings[item.contract_name + '+'] = item.num_long
            if item.num_short > 0:
                self._holdings[item.contract_name + '-'] = item.num_short
        #print(self._holdings)


    def dsignal(self,direction):
        ''' 开仓，对LONG为+, SHORT为-'''
        return '+' if direction == UType.D_Buy else '-'

    def ndsignal(self,direction):
        ''' 平仓，对LONG为-, SHORT为+，即平仓需要校验的是相反的持仓,即平空是针对的多仓'''
        return '-' if direction == UType.D_Buy else '+'

    def lock(self,contract,direction,volume,price):
        """
            开仓前需要lock住保证金,不含手续费
        """
        ctype = contract.ctype
        margin = volume * contract.calc_margin(direction,price)
        if self._available - self.locked < margin:
            logging.warning("保证金不足以lock:%02f-%02f<%02f,volume=%d,price=%02f,unit=%d,marginrate=%02f,multiple=%d" % (self._available,self._locked,margin,volume,price,ctype.unit,ctype.base_marginrate,contract.multiple))
            return False
        self._available -= margin
        self._locked += margin
        return True

    def check_holding(self,contract,direction,volume,price):
        ukey = "%s%s" % (contract.name,self.ndsignal(direction))
        if ukey not in self._holdings or self._holdings[ukey] < volume:
            logging.warning("持仓不足以平仓,%s:%d",self._holdings,volume)
            return False
        return True

    def add(self,contract,direction,volume,price,locked_price):
        """
        :param contract:    contract_type.ContractInfo 实例
        :param direction:   UType.D_Buy/Sell
        :param volume:      交易手数
        :param price:       最后一次tick的价格
        :return:            是否成功. 全部成功或者全部不成功
        """
        ctype = contract.ctype
        margin = volume * contract.calc_margin(direction,price)
        locked_margin = volume * contract.calc_margin(direction,locked_price)
        #if self._available < margin:
        #    return False

        self._available -= ((margin*(1+self.charge))-locked_margin) #把之前locked的拉回来
        self._margin += margin
        self._locked -= locked_margin
        ukey = "%s%s" % (contract.name,self.dsignal(direction))
        self._holdings[ukey] = self._holdings.get(ukey,0) + volume
        with open(self._log_fname,"at") as ff:
            ff.write("open:  %s:%d:%f\n" % (ukey,volume,price))
            #self._fhistory.write("open:  %s:%d:%f\n" % (ukey,volume,price))
        #print("open:  %s:%d:%f\n" % (ukey,volume,price),self._available,margin*(1+self.charge),self.charge)
        #print("开仓手续费:",margin*self.charge)
        return True

    def remove(self,contract,direction,volume,price):
        '''
            平仓时从反方向取
        '''
        ukey = "%s%s" % (contract.name,self.ndsignal(direction))
        if ukey not in self._holdings or self._holdings[ukey] < volume:
            print("in 平仓,失败")
            return False
        self._holdings[ukey] -= volume
        ctype = contract.ctype
        margin = volume * contract.calc_margin(direction,price)

        self._available += (margin*(1-self.charge))
        self._margin -= margin
        with open(self._log_fname,"at") as ff:
            ff.write("close:  %s:%d:%f\n" % (ukey,volume,price))
            #self._fhistory.write("close:  %s:%d:%f\n" % (ukey,volume,price))
        #print("close:  %s:%d:%f\n" % (ukey,volume,price),self._available,(margin*(1-self.charge)),self.charge)
        #print("平仓手续费:",margin*self.charge)
        return True
