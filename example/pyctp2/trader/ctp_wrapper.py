#-*- coding:gbk -*-

import logging
import threading

from ctp.futures import TraderApi
from ctp.futures import ApiStruct as UStruct
from ctp.futures import ApiStruct as UType

from ..common.base import (BaseObject,
                           LONG,
                           XCLOSE_TODAY,
                           STATE_PATH,
                        )
from ..common.errors import TradeError
from . import trade_command
from ..trader.position import ORDER_STATUS



class TraderSpiDelegate(TraderApi):
    """
        将服务器回应转发到Agent
        并自行处理杂务
        SPI回调函数中如需要再次调用TradeApi, 则仍需通过trade_command_queue, 以实现统一入口和同步
    """
    logger = logging.getLogger('ctp.TraderSpiDelegate')
    def __init__(self,
            broker,
            investor,
            passwd,
        ):
        self._trade_command_queue = None
        #self.macro_command_queue = macro_command_queue
        #更新数据用
        self._broker = broker
        self._investor = investor
        self._passwd = passwd
        self.reset_login_info()
        #order_ref => command 的映射, 用于在回调中获取相关信息
        self._ref_map = {}
        self._first_login_time = 0
        self._infos = []
        self._uids = set()
        self._lock = threading.Lock()
        #self.log_fname = STATE_PATH + "/trade.log"

    @property
    def broker(self):
        return self._broker

    @property
    def investor(self):
        return self._investor

    @property
    def front_id(self):
        return self.login_info.front_id

    @property
    def session_id(self):
        return self.login_info.session_id

    @property
    def queue(self):
        #return self._trade_command_queue
        raise TypeError("不支持读取TraderSpiDelegate的trade_command_queue")

    @queue.setter
    def queue(self,queue):
        self._trade_command_queue = queue

    def reset_login_info(self):
        self.login_info = BaseObject(front_id='', session_id='', order_ref=0, trading_day=0, is_logged = False, is_settlement_info_confirmed = False)

    def inc_request_id(self):
        with self._lock:
            self.login_info.order_ref += 1
            return self.login_info.order_ref

    def peep_next_request_id(self): #仅用于测试stub的方法
        return self.login_info.order_ref + 1

    #def delay_command(self, command, delta):
    #    self.macro_command_queue.put_command(DelayedCommand(command, delta))

    def r2uid(self,trading_day,exchange_id,order_sys_id):
        uid = "%s:%s:%s" % (trading_day,exchange_id,order_sys_id)
        return uid
        #print("CW:uid:",uid)

    def day_finalize(self):
        self.reset_login_info()

    #回复状态处理
    def isRspSuccess(self, RspInfo):
        return RspInfo == None or RspInfo.ErrorID == 0

    def resp_common(self, rsp_info, bIsLast, name='默认'):
        #self.logger.debug("resp: %s" % str(rsp_info))
        if not self.isRspSuccess(rsp_info):
            self.logger.info("TD:%s失败" % name)
            return -1
        elif bIsLast and self.isRspSuccess(rsp_info):
            self.logger.info("TD:%s成功" % name)
            return 1
        else:
            self.logger.info("TD:%s结果: 等待数据接收完全..." % name)
            return 0

    def OnRspError(self, info, RequestId, IsLast):
        """ 错误应答
        """
        self.logger.error('TD:requestID:%s, IsLast:%s, info:%s' % (RequestId, IsLast, str(info)))

    ##交易初始化
    #登陆,确认结算单
    def OnFrontConnected(self):
        """
            当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        """
        self.logger.info('TD:trader front connected')
        self._trade_command_queue.put_command(trade_command.LOGIN_COMMAND)

    def OnFrontDisconnected(self, nReason):
        self.logger.info('TD:trader front disconnected, reason=%s' % (nReason, ))

    def user_login(self):
        self.logger.info('TD:trader to login')
        req = UStruct.ReqUserLogin(BrokerID=self._broker, UserID=self._investor, Password=self._passwd)
        ref_id = self.inc_request_id()
        ret = self.ReqUserLogin(req, ref_id)
        self.logger.info('TD:trader to login, issued')
        return ret

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.logger.info("TD:on trader login:%s" % str(pRspUserLogin))
        self.logger.debug("TD:loggin %s" % str(pRspInfo))
        if not self.isRspSuccess(pRspInfo):
            self.logger.warning('TD:trader login failed, errMsg=%s' %(pRspInfo.ErrorMsg, ))
            print('综合交易平台登陆失败，请检查网络或用户名/口令')
            self.login_info.is_logged = False
            return
        self.login_info.is_logged = True
        if self._first_login_time == 0:
            self._first_login_time = pRspUserLogin.LoginTime     #是 HH:MM:SS方式,还是 hh:mm:ss方式? 后者指无前导0
        self.logger.info('TD:trader login success')
        self._login_success(pRspUserLogin.FrontID, pRspUserLogin.SessionID, pRspUserLogin.MaxOrderRef, pRspUserLogin.TradingDay)
        self._trade_command_queue.on_login_success(pRspUserLogin.TradingDay)
        #self.trade_command_queue.put_command(trade_command.SETTLEMENT_QUERY_COMMAND)

    def _login_success(self, frontID, sessionID, max_order_ref, trading_day):
        self.login_info.front_id = frontID
        self.login_info.session_id = sessionID
        self.login_info.order_ref = int(max_order_ref) + 10000
        self.login_info.trading_day = trading_day

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        """登出请求响应"""
        self.logger.info('TD:trader logout')
        self.login_info.is_logged = False

    def query_settlement_info(self):
        #不填日期表示取上一天结算单, 并在响应函数中确认
        self.logger.info('TD:取上一日结算单信息并确认, BrokerID=%s, investorID=%s' % (self._broker, self._investor))
        req = UStruct.QrySettlementInfo(BrokerID=self._broker, InvestorID=self._investor, TradingDay='')
        #time.sleep(1)   #避免流控, 因为此时ticks未必已经开始动作, 故不采用macro_command_queue方式. 这里因为不再查询结算单是否已确认, 所以已经没有流控限制
        ref_id = self.inc_request_id()
        ret = self.ReqQrySettlementInfo(req, ref_id)
        return ret

    def OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast):
        """请求查询投资者结算信息响应
            当结算信息被切分成几段,且切分位置正好把一个中文切开,有可能会出现错误
        """
        #print('Rsp 结算单查询')
        if(self.resp_common(pRspInfo, bIsLast, '结算单查询')>0):
            self.logger.info('结算单查询完成, 准备确认')
            try:
                self.logger.info('TD:结算单内容:%s' % pSettlementInfo.Content)
            except Exception as inst:
                self.logger.warning('TD-ORQSI-A 结算单内容错误:%s' % str(inst))
            #self.trade_command_queue.on_query_settlement_info(pSettlementInfo)     #这里不是完整内容, 没必要
            self._trade_command_queue.put_command(trade_command.SETTLEMENT_CONFIRM_COMMAND)
        else:  #这里是未完成分支, 需要直接忽略
            try:
                self.logger.info('TD:结算单接收中...:%s' % pSettlementInfo.Content)
            except Exception as inst:
                self.logger.warning('TD-ORQSI-B 结算单内容错误:%s' % str(inst))

    def confirm_settlement_info(self):
        self.logger.info('TD-CSI:准备确认结算单')
        req = UStruct.SettlementInfoConfirm(BrokerID=self._broker, InvestorID=self._investor)
        ref_id = self.inc_request_id()
        ret = self.ReqSettlementInfoConfirm(req, ref_id)
        return ret

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        """投资者结算结果确认响应"""
        if(self.resp_common(pRspInfo, bIsLast, '结算单确认')>0):
            self.login_info.is_settlement_info_confirmed = True
            self.logger.info('TD:结算单确认时间: %s-%s' %(pSettlementInfoConfirm.ConfirmDate, pSettlementInfoConfirm.ConfirmTime))
            self._trade_command_queue.on_settlement_info_confirmed()

    #交易准备
    #获取帐户资金
    def fetch_trading_account(self):
        #获取资金帐户
        logging.info('A:获取资金帐户..')
        req = UStruct.QryTradingAccount(BrokerID=self._broker, InvestorID=self._investor)
        ref_id = self.inc_request_id()
        ret = self.ReqQryTradingAccount(req,  ref_id)
        return ret,ref_id
        #logging.info('A:查询资金账户, 函数发出返回值:%s' % r)

    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
        """
            请求查询资金账户响应
        """
        self.logger.info('TD:资金账户响应:%s' % pTradingAccount)
        if bIsLast and self.isRspSuccess(pRspInfo):
            pTA = pTradingAccount
            self._trade_command_queue.on_query_trading_account(nRequestID, pTA.Balance, pTA.Available, pTA.CurrMargin, pTA.FrozenMargin)
        else:
            #logging
            pass

    # 获取持仓
    def fetch_investor_position(self, instrument_id):
        #获取合约的当前持仓
        logging.info('A:获取合约%s的当前持仓..' % (instrument_id, ))
        req = UStruct.QryInvestorPosition(BrokerID=self._broker, InvestorID=self._investor, InstrumentID=instrument_id)
        ref_id = self.inc_request_id()
        ret = self.ReqQryInvestorPosition(req, self.ref_id)
        #logging.info('A:查询持仓, 函数发出返回值:%s' % rP)
        return ret,ref_id

    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast):
        """请求查询投资者持仓响应"""
        #print '查询持仓响应', str(pInvestorPosition), str(pRspInfo)
        if self.isRspSuccess(pRspInfo): #每次一个单独的数据报
            pass
        else:
            #logging
            pass

    # 获取持仓明细
    def fetch_investor_position_detail(self, instrument_id):
        """
            获取合约的当前持仓明细，目前没用
        """
        logging.info('A:获取合约%s的当前持仓..' % (instrument_id, ))
        req = UStruct.QryInvestorPositionDetail(BrokerID=self._broker, InvestorID=self._investor, InstrumentID=instrument_id)
        ref_id = self.inc_request_id()
        ret = self.ReqQryInvestorPositionDetail(req,  self.ref_id)
        #logging.info('A:查询持仓, 函数发出返回值:%s' % r)
        return ret,ref_id

    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast):
        """请求查询投资者持仓明细响应"""
        logging.info(str(pInvestorPositionDetail))
        if self.isRspSuccess(pRspInfo): #每次一个单独的数据报
            pass
        else:
            #logging
            pass

    #获取合约保证金率
    def fetch_instrument_marginrate(self, instrument_id):
        req = UStruct.QryInstrumentMarginRate(BrokerID=self._broker,
                        InvestorID = self._investor,
                        InstrumentID=instrument_id,
                        HedgeFlag = UType.HF_Speculation
                )
        ref_id = self.inc_request_id()
        ret= self.ReqQryInstrumentMarginRate(req, self.inc_request_id())
        logging.info('A:查询保证金率, 函数发出返回值:%s' % ret)
        return ret

    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast):
        """
            保证金率回报。返回的必然是绝对值
            这里返回的是调整后(交易所根据持仓量按规则调整)的保证金率
        """
        self._infos.append(pInstrumentMarginRate)
        if not pInstrumentMarginRate:   # 也会出现pInstrumentMarginRate和pRspInfo均为None这种情况,当查询不存在的合约时
            return
        if bIsLast and self.isRspSuccess(pRspInfo):
            pIMR = pInstrumentMarginRate
            self._trade_command_queue.on_query_instrument_marginrate(pIMR.InstrumentID, pIMR.LongMarginRatioByMoney, pIMR.ShortMarginRatioByMoney)
        else:
            #logging
            pass

    #查询合约信息
    def fetch_instrument(self, instrument_id):
        req = UStruct.QryInstrument(
                        InstrumentID=instrument_id,
                )
        ref_id = self.inc_request_id()
        ret = self.ReqQryInstrument(req, self.inc_request_id())
        logging.info('A:查询合约, 函数发出返回值:%s' % ret)
        return ret

    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast):
        """
            合约回报。
            这里返回的是原始保证金率,所以没有实际用处
        """
        self._infos.append(pInstrument)
        self.logger.info("CT_ORQI_1:%s" % pInstrument)
        self.logger.info("CT_ORQI_2:%s" % pRspInfo)
        #居然可能返回 pInstrument和pRespInfo均为None,这个状态不对!!
        if not pInstrument:
            return
        if bIsLast and self.isRspSuccess(pRspInfo):
            self._trade_command_queue.on_query_instrument(pInstrument.InstrumentID,
                                                         pInstrument.ExchangeID,
                                                         pInstrument.PriceTick,
                                                         pInstrument.VolumeMultiple,
                                                         pInstrument.LongMarginRatio,
                                                         pInstrument.ShortMarginRatio,
                                                    )
            #print pInstrument
        else:#模糊查询的结果, 获得了多个合约的数据，只有最后一个的bLast是True
            self._trade_command_queue.on_query_instrument(pInstrument.InstrumentID,
                                                         pInstrument.ExchangeID,
                                                         pInstrument.PriceTick,
                                                         pInstrument.VolumeMultiple,
                                                         pInstrument.LongMarginRatio,
                                                         pInstrument.ShortMarginRatio,
                                                    )

    def OnRtnInstrumentStatus(self, pInstrumentStatus):
        #pInstrumentStatus.InstrumentID 是 品种名称
        self.logger.info("CWR:ORIS:{id},{time},{status}".format(id=pInstrumentStatus.InstrumentID,time=pInstrumentStatus.EnterTime,status=pInstrumentStatus.InstrumentStatus))
        status = int(pInstrumentStatus.InstrumentStatus)
        #is_on_trading = True if status  == '2' or status =='3' else False
        #self._trade_command_queue.on_instrument_status(pInstrumentStatus.InstrumentID,pInstrumentStatus.EnterTime,is_on_trading)
        self._trade_command_queue.on_instrument_status(pInstrumentStatus.InstrumentID,pInstrumentStatus.EnterTime,status)

    #获取行情信息, 目的在于获取当日涨跌停价格
    def fetch_depth_market_data(self, instrument_id):
        ref_id = self.inc_request_id()
        req = UStruct.QryDepthMarketData(InstrumentID = instrument_id)
        ret = self.ReqQryDepthMarketData(req, ref_id)
        logging.info('A:查询合约行情, 函数发出返回值:%s' % ret)
        return ret

    def OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast):
        """请求查询行情响应
           一次只查询一个合约的, 故一次成功, isLast=1
        """
        self.logger.info('TD:查询行情响应:%s' % pDepthMarketData)
        if bIsLast and self.isRspSuccess(pRspInfo):
            pDMD = pDepthMarketData
            self._trade_command_queue.on_query_market_data(pDMD.InstrumentID,
                                                          int(pDMD.TradingDay),
                                                          pDMD.UpperLimitPrice,
                                                          pDMD.LowerLimitPrice
                                                         )
        else: #不应该出现
            logging.error('Error on query market data:%s' % (pDepthMarketData.InstrumentID, ))
            pass

    #交易部分
    #开仓

    def to_ctp_direction(self,direction):
        #print(direction)
        return UType.D_Buy if direction == LONG else UType.D_Sell

    def from_ctp_direction(self,ctp_direction):
        return LONG if ctp_direction == UType.D_Buy else UType.D_Sell

    def xopen(self, instrument_id, direction, volume, price):
        #print("spidelegate,xopen",instrument_id,volume,price,self)
        ref_id = self.inc_request_id()
        req = UStruct.InputOrder(
                InstrumentID = instrument_id,
                Direction = self.to_ctp_direction(direction),
                OrderRef = str(ref_id),
                LimitPrice = price,    #有个疑问，double类型如何保证舍入舍出，在服务器端取整?
                VolumeTotalOriginal = volume,
                OrderPriceType = UType.OPT_LimitPrice,
                ContingentCondition = UType.CC_Immediately,

                BrokerID = self._broker,
                InvestorID = self._investor,
                CombOffsetFlag = UType.OF_Open,          #开仓 5位字符, 但是只用到第0位
                CombHedgeFlag = UType.HF_Speculation,    #投机 5位字符, 但是只用到第0位

                VolumeCondition = UType.VC_AV,
                MinVolume = 1,   #这个作用有点不确定, 有的文档设成0了
                ForceCloseReason = UType.FCC_NotForceClose,
                IsAutoSuspend = 1,
                UserForceClose = 0,
                TimeCondition = UType.TC_GFD,
            )
        ret = self.ReqOrderInsert(req, ref_id)
        return ret

    def xclose(self, instrument_id, close_type,direction, volume,price):
        """
            上期所区分平昨和平今
                搞反的话就会被CTP直接拒绝. 如平昨来平当日仓,且无足够昨仓,就会报:综合交易平台：平昨仓位不足
        """
        ref_id = self.inc_request_id()
        close_flag = UType.OF_CloseToday if close_type == XCLOSE_TODAY else UType.OF_Close
        req = UStruct.InputOrder(
                InstrumentID = instrument_id,
                Direction = self.to_ctp_direction(direction),
                OrderRef = str(ref_id),
                LimitPrice = price,    #有个疑问，double类型如何保证舍入舍出，在服务器端取整?
                VolumeTotalOriginal = volume,
                OrderPriceType = UType.OPT_LimitPrice,

                BrokerID = self._broker,
                InvestorID = self._investor,
                CombOffsetFlag = close_flag,
                CombHedgeFlag = UType.HF_Speculation,    #投机 5位字符, 但是只用到第0位

                VolumeCondition = UType.VC_AV,
                MinVolume = 1,   #这个作用有点不确定, 有的文档设成0了
                ForceCloseReason = UType.FCC_NotForceClose,
                IsAutoSuspend = 1,
                UserForceClose = 0,
                TimeCondition = UType.TC_GFD,
            )
        ret = self.ReqOrderInsert(req, ref_id)
        return ret

    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        """
            报单未通过参数校验, 被CTP拒绝
            正常情况后不应该出现
            为不可恢复的错误,只允许在调试期间
        """
        #print('ERROR Order Insert,CTP Reject')
        self.logger.error('TD:CTP报单录入错误回报, 正常后不应该出现, rspInfo=%s'%(str(pRspInfo), ))
        #self.trade_command_queue.on_rtn_order(pInputOrder.OrderRef,ORDER_STATUS.LOCAL_REJECT)
        self._trade_command_queue.on_reject(pInputOrder.InstrumentID,
                                           self.from_ctp_direction(pInputOrder.Direction),
                                           pInputOrder.VolumeTotalOriginal,
                                           pInputOrder.LimitPrice,
                                           pRspInfo.ErrorID,
                                    )


    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        """
            交易所报单录入错误回报
            正常情况后不应该出现
            为不可恢复的错误,只允许在调试期间
        """
        #print('ERROR Order Insert,Exchange Reject')
        self.logger.error('TD:交易所报单录入错误回报, 正常后不应该出现, rspInfo=%s'%(str(pRspInfo), ))
        self.logger.error('%s:%s:%s:%s',pInputOrder.OrderRef, pInputOrder.InstrumentID, pRspInfo.ErrorID, pRspInfo.ErrorMsg)
        #self.trade_command_queue.on_rtn_order(pInputOrder.OrderRef,ORDER_STATUS.EXCHANGE_REJECT)
        self._trade_command_queue.on_reject(pInputOrder.InstrumentID,
                                           self.from_ctp_direction(pInputOrder.Direction),
                                           pInputOrder.VolumeTotalOriginal,
                                           pInputOrder.LimitPrice,
                                           pRspInfo.ErrorID,
                                    )


    def _check_accepted(self, pOrder):
        uid = self.r2uid(pOrder.TradingDay, pOrder.ExchangeID, pOrder.OrderSysID)
        #print("CW:uid=",uid)
        #print("CW:check_accepted:",uid,pOrder.TradingDay, pOrder.ExchangeID, pOrder.OrderSysID)
        if uid in self._uids:
            return uid
        trade_info = BaseObject(front_id=pOrder.FrontID, session_id=pOrder.SessionID, trading_day=int(pOrder.TradingDay),
                                exchange_id=pOrder.ExchangeID, order_sys_id=pOrder.OrderSysID,
                                order_ref = pOrder.OrderRef,
                    )
        self._trade_command_queue.on_accept(pOrder.InstrumentID,
                                           self.from_ctp_direction(pOrder.Direction),
                                           pOrder.VolumeTotalOriginal,
                                           pOrder.LimitPrice,
                                           uid,
                                           trade_info,
        )
        self._uids.add(uid)
        return uid

    def OnRtnOrder(self, pOrder):
        """ 报单通知
            CTP、交易所接受报单
        """
        self._infos.append(pOrder)
        #print("ORO:direction",pOrder.Direction)
        #self.logger.info('报单响应 repr, Order=%s' % repr(pOrder))
        #print("ORO:",pOrder.ExchangeID)
        self.logger.info('报单响应 str, Order=%s' % str(pOrder))
        if pOrder.FrontID == self.login_info.front_id and pOrder.SessionID != self.login_info.session_id:
            self.logger.info("收到登陆前的委托回报,%s,%s",self.login_info.front_id,self.login_info.session_id)
            #self.trade_command_queue.on_pre_rtn_order(pOrder.FrontID,pOrder.SessionID,pOrder.OrderRef,pOrder.InstrumentID,pOrder.InsertTime,pOrder.VolumeTotal,pOrder.VolumeTraded)
            pass
        elif pOrder.OrderSubmitStatus == UType.OSS_InsertRejected:
            ##情况1: 在夜盘时发出未被夜盘交易的品种的报单 #报单提交状态:报单已经被拒绝 #状态信息:已撤单报单被拒绝DCE:该品种当前是初始化后!#报单状态:撤单
            ##情况2: 暂停交易时段下单:  #报单提交状态:报单已经被拒绝 #状态信息:已撤单报单被拒绝DCE:该品种当前是开市暂停! #报单状态:撤单:
            ##情况3: 闭市后下单(15:00/15:15之后) #报单提交状态:报单已经被拒绝#状态信息:已撤单报单被拒绝DCE:该品种当前是闭市! #报单状态:撤单
            ##此时,先收到 #状态信息:报单已提交 的RtnOrder,再收到 报单被拒绝的 RtnOrder,就是说收到两个RtnOrder
            #   ctp.TraderSpiDelegate:OnRtnOrder:493:2014-08-25 13:26:07,602 INFO 报单响应 str, Order=<报单日期:20140825,郑商所成交数量:0,买卖方向:买,报单提交状态:已经提交,会话编号:-943256868,最小成交量:1,数量:1,撤销时间:,止损价:0.0,委托时间:13:27:09,经纪公司报单编号:7866,今成交数量:0,合约在交易所的代码:m1501,结算编号:1,激活时间:,GTD日期:,报单引用:10040,触发条件:立即,成交量类型:任何数量,报单类型:正常,本地报单编号:         693,报单提示序号:0,相关报单:,报单价格条件:限价,挂起时间:,剩余数量:1,状态信息:报单已提交,安装编号:2,强平原因:非强平,合约代码:m1501,前置编号:2,用户强评标志:0,报单状态:未知,交易所代码:DCE,报单编号:,请求编号:0,自动挂起标志:1,互换单标志:0,序号:0,组合开平标志:0,报单来源:来自参与者,交易日:20140825,结算会员编号:,有效期类型:当日有效,最后修改时间:,用户端产品信息:,价格:3401.0,组合投机套保标志:1>
            #   ctp.TraderSpiDelegate:OnRtnOrder:512:2014-08-25 13:26:07,602 INFO TD:CTP接受Order，但未发到交易所
            #   ctp.TraderSpiDelegate:OnRtnOrder:493:2014-08-25 13:26:07,641 INFO 报单响应 str, Order=<报单日期:20140825,郑商所成交数量:0,买卖方向:买,报单提交状态:报单已经被拒绝,会话编号:-943256868,最小成交量:1,数量:1,撤销时间:,止损价:0.0,委托时间:13:27:09,经纪公司报单编号:7866,今成交数量:0,合约在交易所的代码:m1501,结算编号:1,激活时间:,GTD日期:,报单引用:10040,触发条件:立即,成交量类型:任何数量,报单类型:正常,本地报单编号:         693,报单提示序号:1,相关报单:,报单价格条件:限价,挂起时间:,剩余数量:1,状态信息:已撤单报单被拒绝DCE:该品种当前是开市暂停!,安装编号:2,强平原因:非强平,合约代码:m1501,前置编号:2,用户强评标志:0,报单状态:撤单,交易所代码:DCE,报单编号:,请求编号:0,自动挂起标志:1,互换单标志:0,序号:0,组合开平标志:0,报单来源:来自参与者,交易日:20140825有效期类型:当日有效,最后修改时间:,用户端产品信息:,价格:3401.0,组合投机套保标志:1>
            #   ctp.TraderSpiDelegate:OnRtnOrder:501:2014-08-25 13:26:07,641 INFO RTN_REJECT:报单被拒绝
            self.logger.info("RTN_REJECT:报单被拒绝")
            self._trade_command_queue.on_reject(pOrder.InstrumentID,
                                               self.from_ctp_direction(pOrder.Direction),
                                               pOrder.VolumeTotalOriginal,
                                               pOrder.LimitPrice,
                                               #-1,   #没有具体原因的拒绝
                                               TradeError.TIME_ERROR,
                                            )
        elif pOrder.OrderStatus == UType.OST_Unknown and pOrder.OrderSysID== '' :
            #CTP接受，但未发到交易所  pOrder.OrderSubmitStatus == UType.OSS_InsertSubmitted.  未必!!!.成交时也是已提交状态
            #print 'CTP接受Order，但未发到交易所, BrokerID=%s, BrokerOrderSeq = %s, TraderID=%s, OrderLocalID=%s' % (pOrder.BrokerID, pOrder.BrokerOrderSeq, pOrder.TraderID, pOrder.OrderLocalID)
            self.logger.info('TD:CTP接受Order，但未发到交易所, BrokerID=%s, BrokerOrderSeq = %s, TraderID=%s, OrderLocalID=%s' % (pOrder.BrokerID, pOrder.BrokerOrderSeq, pOrder.TraderID, pOrder.OrderLocalID))
            #print('TD:CTP接受Order，但未发到交易所, BrokerID=%s, BrokerOrderSeq = %s, TraderID=%s, OrderLocalID=%s' % (pOrder.BrokerID, pOrder.BrokerOrderSeq, pOrder.TraderID, pOrder.OrderLocalID))
            #self._check_accepted(pOrder)   #exchange_id未设定
        elif pOrder.OrderStatus == UType.OST_Unknown and pOrder.OrderSysID != '':     #交易所接受后,得到OrderSysID
            #print '交易所接受Order, exchangeID=%s, OrderSysID=%s, TraderID=%s, OrderLocalID=%s' % (pOrder.ExchangeID, pOrder.OrderSysID, pOrder.TraderID, pOrder.OrderLocalID)
            self.logger.info('TD:交易所接受Order, exchangeID=%s, OrderSysID=%s, TraderID=%s, OrderLocalID=%s' % (pOrder.ExchangeID, pOrder.OrderSysID, pOrder.TraderID, pOrder.OrderLocalID))
            self._check_accepted(pOrder)
        elif pOrder.OrderStatus == UType.OST_PartTradedNotQueueing:
            uid = self._check_accepted(pOrder)    #可能由于各种原因导致未出现单独的Exchange Accept回应
            #print("ORO:VT:",pOrder.VolumeTraded)
            self._trade_command_queue.on_rtn_order(uid,ORDER_STATUS.PART_SUCCESSED,pOrder.VolumeTraded)
        elif pOrder.OrderStatus == UType.OST_AllTraded:
            uid = self._check_accepted(pOrder)    #可能由于各种原因导致未出现单独的Exchange Accept回应
            self._trade_command_queue.on_rtn_order(uid,ORDER_STATUS.SUCCESSED,pOrder.VolumeTraded)
        elif pOrder.OrderStatus == UType.OST_Canceled or pOrder.OrderStatus == UType.OST_NoTradeNotQueueing:
            uid = self._check_accepted(pOrder)    #可能由于各种原因导致未出现单独的Exchange Accept回应
            self._trade_command_queue.on_rtn_order(uid,ORDER_STATUS.CANCELLED,pOrder.VolumeTraded)

    def OnRtnTrade(self, pTrade):
        """
            成交通知
        """
        self.logger.info("SPI_OT:收到成交回报 %s",str(pTrade))
        #print("SPI_OT:",pTrade.ExchangeID)
        #if pTrade.TradeTime < self.first_login_time:       #不可能收到登陆前的成交回报,只会收到委托回报
        #    self.logger.info("收到登陆前的成交回报",str(pTrade))
        #    self.trade_command_queue.on_pre_trade(pTrade.ExchangeID,pTrade.OrderSysID,pTrade.TradeTime,pTrade.InstrumentId,pTrade.Volume,pTrade.Price)
        #else:
        self.logger.info("收到成交回报:%s",str(pTrade))
        self.logger.info('SPI_TD:成交通知, BrokerID=%s, BrokerOrderSeq = %s, exchangeID=%s, OrderSysID=%s, TraderID=%s, OrderLocalID=%s' %(pTrade.BrokerID, pTrade.BrokerOrderSeq, pTrade.ExchangeID, pTrade.OrderSysID, pTrade.TraderID, pTrade.OrderLocalID))
        uid = self.r2uid(pTrade.TradingDay, pTrade.ExchangeID, pTrade.OrderSysID)   #必然之前已经存在OnRtnOrder的调用
        self._trade_command_queue.on_trade(uid,int(pTrade.TradeDate),pTrade.TradeTime,pTrade.Volume,pTrade.Price)

    def xcancel(self,instrument_id,exchange_id,order_sys_id,front_id,session_id,order_ref):
        """
            当以RESTART方式订阅流时,会收到之前的委托/成交回报. 在委托回报中,有各委托单状态
                如果撤单的时候数据对不上号,就会有 撤单找不到相应报单 的错误
            撤单请求返回的OnRtnOrder是被撤单的这个pOrder的委托响应的状态更新,不会有单独的撤单OnRtnOrder
                该OnRtnOrder中, front_id,session_id等都对应到被撤的那个pOrder
                如果是重新登陆,那么发出撤单命令的这个session_id和OnRtnOrder响应中的session_id是不一样的
        """
        self.logger.info('SPI_XC:取消命令')
        ref_id = self.inc_request_id()
        #orderActionRef是一个可有可无的值,设置错了也无关紧要
        req = UStruct.InputOrderAction(
                InstrumentID = instrument_id,
                BrokerID = self._broker,
                InvestorID = self._investor,
                ActionFlag = UType.AF_Delete,
                OrderActionRef = ref_id,    #   这需要一个int,真TM矛盾, OrderRef是一个String
                #OrderActionRef = order_ref, #   这个ref无关紧要,根据文档,应当是ref_id
            )
        if exchange_id:   #已设置,则采用Exchange_id+orderSysID方式. 这两种方式均可撤当日任意单
            req.ExchangeID = exchange_id
            req.OrderSysID = order_sys_id
        else:   #采用frontID + sessionID + orderRef标识的方式. 这两种方式均可撤当日任意单
            #这个分支的测试 必须在OnRtnOrder第一次Callback时才能触发. 需要在该回调中测试
            req.FrontID = front_id
            req.SessionID = session_id
            req.OrderRef = str(order_ref)
        ret= self.ReqOrderAction(req,self.inc_request_id())
        return ret

    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast):
        """
            ctp撤单校验错误
        """
        self.logger.warning('TD:CTP撤单录入错误回报, 正常后不应该出现, rspInfo=%s'%(str(pRspInfo), ))
        #self.trade_command_queue.on_rtn_order(pInputOrderAction.OrderRef,ORDER_STATUS.LOCAL_REJECT)

    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        """
            交易所撤单操作错误回报
        """
        #print("in CTP_WRAPPER:OEROA")
        self.logger.warning('TD:交易所撤单录入错误回报, 可能已经成交, rspInfo=%s'%(str(pRspInfo), ))
        #self.trade_command_queue.on_rtn_order(pOrderAction.OrderRef,ORDER_STATUS.EXCHANGE_REJECT)


