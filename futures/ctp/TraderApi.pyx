# -*- coding: utf-8 -*-

from cTraderApi cimport *

cdef ApiStruct_addressof, ApiStruct_Accountregister, ApiStruct_BrokerTradingAlgos, ApiStruct_BrokerTradingParams, ApiStruct_CFMMCTradingAccountKey, ApiStruct_CFMMCTradingAccountToken, ApiStruct_CancelAccount, ApiStruct_ChangeAccount, ApiStruct_CombAction, ApiStruct_CombInstrumentGuard, ApiStruct_ContractBank, ApiStruct_DepthMarketData, ApiStruct_EWarrantOffset, ApiStruct_ErrorConditionalOrder, ApiStruct_Exchange, ApiStruct_ExchangeMarginRate, ApiStruct_ExchangeMarginRateAdjust, ApiStruct_ExchangeRate, ApiStruct_ExecOrder, ApiStruct_ExecOrderAction, ApiStruct_ForQuote, ApiStruct_ForQuoteRsp, ApiStruct_InputCombAction, ApiStruct_InputExecOrder, ApiStruct_InputExecOrderAction, ApiStruct_InputForQuote, ApiStruct_InputOrder, ApiStruct_InputOrderAction, ApiStruct_InputQuote, ApiStruct_InputQuoteAction, ApiStruct_Instrument, ApiStruct_InstrumentCommissionRate, ApiStruct_InstrumentMarginRate, ApiStruct_InstrumentStatus, ApiStruct_Investor, ApiStruct_InvestorPosition, ApiStruct_InvestorPositionCombineDetail, ApiStruct_InvestorPositionDetail, ApiStruct_InvestorProductGroupMargin, ApiStruct_Notice, ApiStruct_NotifyQueryAccount, ApiStruct_OpenAccount, ApiStruct_OptionInstrCommRate, ApiStruct_OptionInstrTradeCost, ApiStruct_Order, ApiStruct_OrderAction, ApiStruct_ParkedOrder, ApiStruct_ParkedOrderAction, ApiStruct_Product, ApiStruct_ProductExchRate, ApiStruct_QueryCFMMCTradingAccountToken, ApiStruct_QueryMaxOrderVolume, ApiStruct_Quote, ApiStruct_QuoteAction, ApiStruct_RemoveParkedOrder, ApiStruct_RemoveParkedOrderAction, ApiStruct_ReqQueryAccount, ApiStruct_ReqRepeal, ApiStruct_ReqTransfer, ApiStruct_RspAuthenticate, ApiStruct_RspInfo, ApiStruct_RspRepeal, ApiStruct_RspTransfer, ApiStruct_RspUserLogin, ApiStruct_SecAgentACIDMap, ApiStruct_SettlementInfo, ApiStruct_SettlementInfoConfirm, ApiStruct_Trade, ApiStruct_TradingAccount, ApiStruct_TradingAccountPasswordUpdate, ApiStruct_TradingCode, ApiStruct_TradingNotice, ApiStruct_TradingNoticeInfo, ApiStruct_TransferBank, ApiStruct_TransferSerial, ApiStruct_UserLogout, ApiStruct_UserPasswordUpdate
cdef extern _init(self, m):
    global ApiStruct_addressof, ApiStruct_Accountregister, ApiStruct_BrokerTradingAlgos, ApiStruct_BrokerTradingParams, ApiStruct_CFMMCTradingAccountKey, ApiStruct_CFMMCTradingAccountToken, ApiStruct_CancelAccount, ApiStruct_ChangeAccount, ApiStruct_CombAction, ApiStruct_CombInstrumentGuard, ApiStruct_ContractBank, ApiStruct_DepthMarketData, ApiStruct_EWarrantOffset, ApiStruct_ErrorConditionalOrder, ApiStruct_Exchange, ApiStruct_ExchangeMarginRate, ApiStruct_ExchangeMarginRateAdjust, ApiStruct_ExchangeRate, ApiStruct_ExecOrder, ApiStruct_ExecOrderAction, ApiStruct_ForQuote, ApiStruct_ForQuoteRsp, ApiStruct_InputCombAction, ApiStruct_InputExecOrder, ApiStruct_InputExecOrderAction, ApiStruct_InputForQuote, ApiStruct_InputOrder, ApiStruct_InputOrderAction, ApiStruct_InputQuote, ApiStruct_InputQuoteAction, ApiStruct_Instrument, ApiStruct_InstrumentCommissionRate, ApiStruct_InstrumentMarginRate, ApiStruct_InstrumentStatus, ApiStruct_Investor, ApiStruct_InvestorPosition, ApiStruct_InvestorPositionCombineDetail, ApiStruct_InvestorPositionDetail, ApiStruct_InvestorProductGroupMargin, ApiStruct_Notice, ApiStruct_NotifyQueryAccount, ApiStruct_OpenAccount, ApiStruct_OptionInstrCommRate, ApiStruct_OptionInstrTradeCost, ApiStruct_Order, ApiStruct_OrderAction, ApiStruct_ParkedOrder, ApiStruct_ParkedOrderAction, ApiStruct_Product, ApiStruct_ProductExchRate, ApiStruct_QueryCFMMCTradingAccountToken, ApiStruct_QueryMaxOrderVolume, ApiStruct_Quote, ApiStruct_QuoteAction, ApiStruct_RemoveParkedOrder, ApiStruct_RemoveParkedOrderAction, ApiStruct_ReqQueryAccount, ApiStruct_ReqRepeal, ApiStruct_ReqTransfer, ApiStruct_RspAuthenticate, ApiStruct_RspInfo, ApiStruct_RspRepeal, ApiStruct_RspTransfer, ApiStruct_RspUserLogin, ApiStruct_SecAgentACIDMap, ApiStruct_SettlementInfo, ApiStruct_SettlementInfoConfirm, ApiStruct_Trade, ApiStruct_TradingAccount, ApiStruct_TradingAccountPasswordUpdate, ApiStruct_TradingCode, ApiStruct_TradingNotice, ApiStruct_TradingNoticeInfo, ApiStruct_TransferBank, ApiStruct_TransferSerial, ApiStruct_UserLogout, ApiStruct_UserPasswordUpdate
    ApiStruct_addressof = XGetAttr(PyImport_ImportModule(S_ctypes), S_addressof)
    fa = XStr(S_from_address)
    ApiStruct_Accountregister = XGotAttr(XGetAttr(m, S_Accountregister), fa)
    ApiStruct_BrokerTradingAlgos = XGotAttr(XGetAttr(m, S_BrokerTradingAlgos), fa)
    ApiStruct_BrokerTradingParams = XGotAttr(XGetAttr(m, S_BrokerTradingParams), fa)
    ApiStruct_CFMMCTradingAccountKey = XGotAttr(XGetAttr(m, S_CFMMCTradingAccountKey), fa)
    ApiStruct_CFMMCTradingAccountToken = XGotAttr(XGetAttr(m, S_CFMMCTradingAccountToken), fa)
    ApiStruct_CancelAccount = XGotAttr(XGetAttr(m, S_CancelAccount), fa)
    ApiStruct_ChangeAccount = XGotAttr(XGetAttr(m, S_ChangeAccount), fa)
    ApiStruct_CombAction = XGotAttr(XGetAttr(m, S_CombAction), fa)
    ApiStruct_CombInstrumentGuard = XGotAttr(XGetAttr(m, S_CombInstrumentGuard), fa)
    ApiStruct_ContractBank = XGotAttr(XGetAttr(m, S_ContractBank), fa)
    ApiStruct_DepthMarketData = XGotAttr(XGetAttr(m, S_DepthMarketData), fa)
    ApiStruct_EWarrantOffset = XGotAttr(XGetAttr(m, S_EWarrantOffset), fa)
    ApiStruct_ErrorConditionalOrder = XGotAttr(XGetAttr(m, S_ErrorConditionalOrder), fa)
    ApiStruct_Exchange = XGotAttr(XGetAttr(m, S_Exchange), fa)
    ApiStruct_ExchangeMarginRate = XGotAttr(XGetAttr(m, S_ExchangeMarginRate), fa)
    ApiStruct_ExchangeMarginRateAdjust = XGotAttr(XGetAttr(m, S_ExchangeMarginRateAdjust), fa)
    ApiStruct_ExchangeRate = XGotAttr(XGetAttr(m, S_ExchangeRate), fa)
    ApiStruct_ExecOrder = XGotAttr(XGetAttr(m, S_ExecOrder), fa)
    ApiStruct_ExecOrderAction = XGotAttr(XGetAttr(m, S_ExecOrderAction), fa)
    ApiStruct_ForQuote = XGotAttr(XGetAttr(m, S_ForQuote), fa)
    ApiStruct_ForQuoteRsp = XGotAttr(XGetAttr(m, S_ForQuoteRsp), fa)
    ApiStruct_InputCombAction = XGotAttr(XGetAttr(m, S_InputCombAction), fa)
    ApiStruct_InputExecOrder = XGotAttr(XGetAttr(m, S_InputExecOrder), fa)
    ApiStruct_InputExecOrderAction = XGotAttr(XGetAttr(m, S_InputExecOrderAction), fa)
    ApiStruct_InputForQuote = XGotAttr(XGetAttr(m, S_InputForQuote), fa)
    ApiStruct_InputOrder = XGotAttr(XGetAttr(m, S_InputOrder), fa)
    ApiStruct_InputOrderAction = XGotAttr(XGetAttr(m, S_InputOrderAction), fa)
    ApiStruct_InputQuote = XGotAttr(XGetAttr(m, S_InputQuote), fa)
    ApiStruct_InputQuoteAction = XGotAttr(XGetAttr(m, S_InputQuoteAction), fa)
    ApiStruct_Instrument = XGotAttr(XGetAttr(m, S_Instrument), fa)
    ApiStruct_InstrumentCommissionRate = XGotAttr(XGetAttr(m, S_InstrumentCommissionRate), fa)
    ApiStruct_InstrumentMarginRate = XGotAttr(XGetAttr(m, S_InstrumentMarginRate), fa)
    ApiStruct_InstrumentStatus = XGotAttr(XGetAttr(m, S_InstrumentStatus), fa)
    ApiStruct_Investor = XGotAttr(XGetAttr(m, S_Investor), fa)
    ApiStruct_InvestorPosition = XGotAttr(XGetAttr(m, S_InvestorPosition), fa)
    ApiStruct_InvestorPositionCombineDetail = XGotAttr(XGetAttr(m, S_InvestorPositionCombineDetail), fa)
    ApiStruct_InvestorPositionDetail = XGotAttr(XGetAttr(m, S_InvestorPositionDetail), fa)
    ApiStruct_InvestorProductGroupMargin = XGotAttr(XGetAttr(m, S_InvestorProductGroupMargin), fa)
    ApiStruct_Notice = XGotAttr(XGetAttr(m, S_Notice), fa)
    ApiStruct_NotifyQueryAccount = XGotAttr(XGetAttr(m, S_NotifyQueryAccount), fa)
    ApiStruct_OpenAccount = XGotAttr(XGetAttr(m, S_OpenAccount), fa)
    ApiStruct_OptionInstrCommRate = XGotAttr(XGetAttr(m, S_OptionInstrCommRate), fa)
    ApiStruct_OptionInstrTradeCost = XGotAttr(XGetAttr(m, S_OptionInstrTradeCost), fa)
    ApiStruct_Order = XGotAttr(XGetAttr(m, S_Order), fa)
    ApiStruct_OrderAction = XGotAttr(XGetAttr(m, S_OrderAction), fa)
    ApiStruct_ParkedOrder = XGotAttr(XGetAttr(m, S_ParkedOrder), fa)
    ApiStruct_ParkedOrderAction = XGotAttr(XGetAttr(m, S_ParkedOrderAction), fa)
    ApiStruct_Product = XGotAttr(XGetAttr(m, S_Product), fa)
    ApiStruct_ProductExchRate = XGotAttr(XGetAttr(m, S_ProductExchRate), fa)
    ApiStruct_QueryCFMMCTradingAccountToken = XGotAttr(XGetAttr(m, S_QueryCFMMCTradingAccountToken), fa)
    ApiStruct_QueryMaxOrderVolume = XGotAttr(XGetAttr(m, S_QueryMaxOrderVolume), fa)
    ApiStruct_Quote = XGotAttr(XGetAttr(m, S_Quote), fa)
    ApiStruct_QuoteAction = XGotAttr(XGetAttr(m, S_QuoteAction), fa)
    ApiStruct_RemoveParkedOrder = XGotAttr(XGetAttr(m, S_RemoveParkedOrder), fa)
    ApiStruct_RemoveParkedOrderAction = XGotAttr(XGetAttr(m, S_RemoveParkedOrderAction), fa)
    ApiStruct_ReqQueryAccount = XGotAttr(XGetAttr(m, S_ReqQueryAccount), fa)
    ApiStruct_ReqRepeal = XGotAttr(XGetAttr(m, S_ReqRepeal), fa)
    ApiStruct_ReqTransfer = XGotAttr(XGetAttr(m, S_ReqTransfer), fa)
    ApiStruct_RspAuthenticate = XGotAttr(XGetAttr(m, S_RspAuthenticate), fa)
    ApiStruct_RspInfo = XGotAttr(XGetAttr(m, S_RspInfo), fa)
    ApiStruct_RspRepeal = XGotAttr(XGetAttr(m, S_RspRepeal), fa)
    ApiStruct_RspTransfer = XGotAttr(XGetAttr(m, S_RspTransfer), fa)
    ApiStruct_RspUserLogin = XGotAttr(XGetAttr(m, S_RspUserLogin), fa)
    ApiStruct_SecAgentACIDMap = XGotAttr(XGetAttr(m, S_SecAgentACIDMap), fa)
    ApiStruct_SettlementInfo = XGotAttr(XGetAttr(m, S_SettlementInfo), fa)
    ApiStruct_SettlementInfoConfirm = XGotAttr(XGetAttr(m, S_SettlementInfoConfirm), fa)
    ApiStruct_Trade = XGotAttr(XGetAttr(m, S_Trade), fa)
    ApiStruct_TradingAccount = XGotAttr(XGetAttr(m, S_TradingAccount), fa)
    ApiStruct_TradingAccountPasswordUpdate = XGotAttr(XGetAttr(m, S_TradingAccountPasswordUpdate), fa)
    ApiStruct_TradingCode = XGotAttr(XGetAttr(m, S_TradingCode), fa)
    ApiStruct_TradingNotice = XGotAttr(XGetAttr(m, S_TradingNotice), fa)
    ApiStruct_TradingNoticeInfo = XGotAttr(XGetAttr(m, S_TradingNoticeInfo), fa)
    ApiStruct_TransferBank = XGotAttr(XGetAttr(m, S_TransferBank), fa)
    ApiStruct_TransferSerial = XGotAttr(XGetAttr(m, S_TransferSerial), fa)
    ApiStruct_UserLogout = XGotAttr(XGetAttr(m, S_UserLogout), fa)
    ApiStruct_UserPasswordUpdate = XGotAttr(XGetAttr(m, S_UserPasswordUpdate), fa)
XFixSysModules()
CSetAttr(Xmod, _init_method.ml_name, PyCFunction_NewEx(&_init_method, NULL, XCGetAttr(Xmod, S___name__)))


cdef void TraderApi_Release(TraderApi self):
    ReleaseTraderApi(self.api, self.spi)
    self.api = self.spi = NULL

cdef class TraderApi:
    cdef CTraderApi *api
    cdef CTraderSpi *spi

    def __dealloc__(self):
        TraderApi_Release(self)

    def Alive(self):
        if self.spi is not NULL: return self.spi.tid
        if self.api is not NULL: return False

    def Create(self, const_char *pszFlowPath=""):
        if self.api is not NULL: return
        self.api = CreateFtdcTraderApi(pszFlowPath)
        CheckMemory(self.api)

    def GetApiVersion(self):
        return GetApiVersion()

    def Release(self):
        TraderApi_Release(self)

    def Init(self):
        if self.api is NULL or self.spi is not NULL: return
        self.spi = new CTraderSpi(<PyObject *>self)
        CheckMemory(self.spi)
        self.api.RegisterSpi(self.spi)
        self.api.Init()

    def Join(self):
        cdef int ret
        if self.spi is NULL: return
        with nogil: ret = self.api.Join()
        return ret

    def GetTradingDay(self):
        cdef const_char *ret
        if self.spi is NULL: return
        with nogil: ret = self.api.GetTradingDay()
        return ret

    def RegisterFront(self, char *pszFrontAddress):
        if self.api is NULL: return
        self.api.RegisterFront(pszFrontAddress)

    def RegisterNameServer(self, char *pszNsAddress):
        if self.api is NULL: return
        self.api.RegisterNameServer(pszNsAddress)

    def RegisterFensUserInfo(self, pFensUserInfo):
        if self.api is NULL: return
        self.api.RegisterFensUserInfo(<CFensUserInfoField *><size_t>ApiStruct_addressof(pFensUserInfo))

    def SubscribePrivateTopic(self, TE_RESUME_TYPE nResumeType):
        if self.api is NULL: return
        self.api.SubscribePrivateTopic(nResumeType)

    def SubscribePublicTopic(self, TE_RESUME_TYPE nResumeType):
        if self.api is NULL: return
        self.api.SubscribePublicTopic(nResumeType)

    def ReqAuthenticate(self, pReqAuthenticate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pReqAuthenticate)
        with nogil: nRequestID = self.api.ReqAuthenticate(<CReqAuthenticateField *>address, nRequestID)
        return nRequestID

    def ReqUserLogin(self, pReqUserLogin, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pReqUserLogin)
        with nogil: nRequestID = self.api.ReqUserLogin(<CReqUserLoginField *>address, nRequestID)
        return nRequestID

    def ReqUserLogout(self, pUserLogout, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pUserLogout)
        with nogil: nRequestID = self.api.ReqUserLogout(<CUserLogoutField *>address, nRequestID)
        return nRequestID

    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pUserPasswordUpdate)
        with nogil: nRequestID = self.api.ReqUserPasswordUpdate(<CUserPasswordUpdateField *>address, nRequestID)
        return nRequestID

    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pTradingAccountPasswordUpdate)
        with nogil: nRequestID = self.api.ReqTradingAccountPasswordUpdate(<CTradingAccountPasswordUpdateField *>address, nRequestID)
        return nRequestID

    def ReqOrderInsert(self, pInputOrder, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputOrder)
        with nogil: nRequestID = self.api.ReqOrderInsert(<CInputOrderField *>address, nRequestID)
        return nRequestID

    def ReqParkedOrderInsert(self, pParkedOrder, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pParkedOrder)
        with nogil: nRequestID = self.api.ReqParkedOrderInsert(<CParkedOrderField *>address, nRequestID)
        return nRequestID

    def ReqParkedOrderAction(self, pParkedOrderAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pParkedOrderAction)
        with nogil: nRequestID = self.api.ReqParkedOrderAction(<CParkedOrderActionField *>address, nRequestID)
        return nRequestID

    def ReqOrderAction(self, pInputOrderAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputOrderAction)
        with nogil: nRequestID = self.api.ReqOrderAction(<CInputOrderActionField *>address, nRequestID)
        return nRequestID

    def ReqQueryMaxOrderVolume(self, pQueryMaxOrderVolume, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQueryMaxOrderVolume)
        with nogil: nRequestID = self.api.ReqQueryMaxOrderVolume(<CQueryMaxOrderVolumeField *>address, nRequestID)
        return nRequestID

    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pSettlementInfoConfirm)
        with nogil: nRequestID = self.api.ReqSettlementInfoConfirm(<CSettlementInfoConfirmField *>address, nRequestID)
        return nRequestID

    def ReqRemoveParkedOrder(self, pRemoveParkedOrder, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pRemoveParkedOrder)
        with nogil: nRequestID = self.api.ReqRemoveParkedOrder(<CRemoveParkedOrderField *>address, nRequestID)
        return nRequestID

    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pRemoveParkedOrderAction)
        with nogil: nRequestID = self.api.ReqRemoveParkedOrderAction(<CRemoveParkedOrderActionField *>address, nRequestID)
        return nRequestID

    def ReqExecOrderInsert(self, pInputExecOrder, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputExecOrder)
        with nogil: nRequestID = self.api.ReqExecOrderInsert(<CInputExecOrderField *>address, nRequestID)
        return nRequestID

    def ReqExecOrderAction(self, pInputExecOrderAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputExecOrderAction)
        with nogil: nRequestID = self.api.ReqExecOrderAction(<CInputExecOrderActionField *>address, nRequestID)
        return nRequestID

    def ReqForQuoteInsert(self, pInputForQuote, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputForQuote)
        with nogil: nRequestID = self.api.ReqForQuoteInsert(<CInputForQuoteField *>address, nRequestID)
        return nRequestID

    def ReqQuoteInsert(self, pInputQuote, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputQuote)
        with nogil: nRequestID = self.api.ReqQuoteInsert(<CInputQuoteField *>address, nRequestID)
        return nRequestID

    def ReqQuoteAction(self, pInputQuoteAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputQuoteAction)
        with nogil: nRequestID = self.api.ReqQuoteAction(<CInputQuoteActionField *>address, nRequestID)
        return nRequestID

    def ReqCombActionInsert(self, pInputCombAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputCombAction)
        with nogil: nRequestID = self.api.ReqCombActionInsert(<CInputCombActionField *>address, nRequestID)
        return nRequestID

    def ReqQryOrder(self, pQryOrder, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryOrder)
        with nogil: nRequestID = self.api.ReqQryOrder(<CQryOrderField *>address, nRequestID)
        return nRequestID

    def ReqQryTrade(self, pQryTrade, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryTrade)
        with nogil: nRequestID = self.api.ReqQryTrade(<CQryTradeField *>address, nRequestID)
        return nRequestID

    def ReqQryInvestorPosition(self, pQryInvestorPosition, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInvestorPosition)
        with nogil: nRequestID = self.api.ReqQryInvestorPosition(<CQryInvestorPositionField *>address, nRequestID)
        return nRequestID

    def ReqQryTradingAccount(self, pQryTradingAccount, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryTradingAccount)
        with nogil: nRequestID = self.api.ReqQryTradingAccount(<CQryTradingAccountField *>address, nRequestID)
        return nRequestID

    def ReqQryInvestor(self, pQryInvestor, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInvestor)
        with nogil: nRequestID = self.api.ReqQryInvestor(<CQryInvestorField *>address, nRequestID)
        return nRequestID

    def ReqQryTradingCode(self, pQryTradingCode, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryTradingCode)
        with nogil: nRequestID = self.api.ReqQryTradingCode(<CQryTradingCodeField *>address, nRequestID)
        return nRequestID

    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInstrumentMarginRate)
        with nogil: nRequestID = self.api.ReqQryInstrumentMarginRate(<CQryInstrumentMarginRateField *>address, nRequestID)
        return nRequestID

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInstrumentCommissionRate)
        with nogil: nRequestID = self.api.ReqQryInstrumentCommissionRate(<CQryInstrumentCommissionRateField *>address, nRequestID)
        return nRequestID

    def ReqQryExchange(self, pQryExchange, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryExchange)
        with nogil: nRequestID = self.api.ReqQryExchange(<CQryExchangeField *>address, nRequestID)
        return nRequestID

    def ReqQryProduct(self, pQryProduct, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryProduct)
        with nogil: nRequestID = self.api.ReqQryProduct(<CQryProductField *>address, nRequestID)
        return nRequestID

    def ReqQryInstrument(self, pQryInstrument, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInstrument)
        with nogil: nRequestID = self.api.ReqQryInstrument(<CQryInstrumentField *>address, nRequestID)
        return nRequestID

    def ReqQryDepthMarketData(self, pQryDepthMarketData, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryDepthMarketData)
        with nogil: nRequestID = self.api.ReqQryDepthMarketData(<CQryDepthMarketDataField *>address, nRequestID)
        return nRequestID

    def ReqQrySettlementInfo(self, pQrySettlementInfo, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQrySettlementInfo)
        with nogil: nRequestID = self.api.ReqQrySettlementInfo(<CQrySettlementInfoField *>address, nRequestID)
        return nRequestID

    def ReqQryTransferBank(self, pQryTransferBank, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryTransferBank)
        with nogil: nRequestID = self.api.ReqQryTransferBank(<CQryTransferBankField *>address, nRequestID)
        return nRequestID

    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInvestorPositionDetail)
        with nogil: nRequestID = self.api.ReqQryInvestorPositionDetail(<CQryInvestorPositionDetailField *>address, nRequestID)
        return nRequestID

    def ReqQryNotice(self, pQryNotice, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryNotice)
        with nogil: nRequestID = self.api.ReqQryNotice(<CQryNoticeField *>address, nRequestID)
        return nRequestID

    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQrySettlementInfoConfirm)
        with nogil: nRequestID = self.api.ReqQrySettlementInfoConfirm(<CQrySettlementInfoConfirmField *>address, nRequestID)
        return nRequestID

    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInvestorPositionCombineDetail)
        with nogil: nRequestID = self.api.ReqQryInvestorPositionCombineDetail(<CQryInvestorPositionCombineDetailField *>address, nRequestID)
        return nRequestID

    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryCFMMCTradingAccountKey)
        with nogil: nRequestID = self.api.ReqQryCFMMCTradingAccountKey(<CQryCFMMCTradingAccountKeyField *>address, nRequestID)
        return nRequestID

    def ReqQryEWarrantOffset(self, pQryEWarrantOffset, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryEWarrantOffset)
        with nogil: nRequestID = self.api.ReqQryEWarrantOffset(<CQryEWarrantOffsetField *>address, nRequestID)
        return nRequestID

    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInvestorProductGroupMargin)
        with nogil: nRequestID = self.api.ReqQryInvestorProductGroupMargin(<CQryInvestorProductGroupMarginField *>address, nRequestID)
        return nRequestID

    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryExchangeMarginRate)
        with nogil: nRequestID = self.api.ReqQryExchangeMarginRate(<CQryExchangeMarginRateField *>address, nRequestID)
        return nRequestID

    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryExchangeMarginRateAdjust)
        with nogil: nRequestID = self.api.ReqQryExchangeMarginRateAdjust(<CQryExchangeMarginRateAdjustField *>address, nRequestID)
        return nRequestID

    def ReqQryExchangeRate(self, pQryExchangeRate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryExchangeRate)
        with nogil: nRequestID = self.api.ReqQryExchangeRate(<CQryExchangeRateField *>address, nRequestID)
        return nRequestID

    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQrySecAgentACIDMap)
        with nogil: nRequestID = self.api.ReqQrySecAgentACIDMap(<CQrySecAgentACIDMapField *>address, nRequestID)
        return nRequestID

    def ReqQryProductExchRate(self, pQryProductExchRate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryProductExchRate)
        with nogil: nRequestID = self.api.ReqQryProductExchRate(<CQryProductExchRateField *>address, nRequestID)
        return nRequestID

    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryOptionInstrTradeCost)
        with nogil: nRequestID = self.api.ReqQryOptionInstrTradeCost(<CQryOptionInstrTradeCostField *>address, nRequestID)
        return nRequestID

    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryOptionInstrCommRate)
        with nogil: nRequestID = self.api.ReqQryOptionInstrCommRate(<CQryOptionInstrCommRateField *>address, nRequestID)
        return nRequestID

    def ReqQryExecOrder(self, pQryExecOrder, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryExecOrder)
        with nogil: nRequestID = self.api.ReqQryExecOrder(<CQryExecOrderField *>address, nRequestID)
        return nRequestID

    def ReqQryForQuote(self, pQryForQuote, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryForQuote)
        with nogil: nRequestID = self.api.ReqQryForQuote(<CQryForQuoteField *>address, nRequestID)
        return nRequestID

    def ReqQryQuote(self, pQryQuote, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryQuote)
        with nogil: nRequestID = self.api.ReqQryQuote(<CQryQuoteField *>address, nRequestID)
        return nRequestID

    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryCombInstrumentGuard)
        with nogil: nRequestID = self.api.ReqQryCombInstrumentGuard(<CQryCombInstrumentGuardField *>address, nRequestID)
        return nRequestID

    def ReqQryCombAction(self, pQryCombAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryCombAction)
        with nogil: nRequestID = self.api.ReqQryCombAction(<CQryCombActionField *>address, nRequestID)
        return nRequestID

    def ReqQryTransferSerial(self, pQryTransferSerial, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryTransferSerial)
        with nogil: nRequestID = self.api.ReqQryTransferSerial(<CQryTransferSerialField *>address, nRequestID)
        return nRequestID

    def ReqQryAccountregister(self, pQryAccountregister, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryAccountregister)
        with nogil: nRequestID = self.api.ReqQryAccountregister(<CQryAccountregisterField *>address, nRequestID)
        return nRequestID

    def ReqQryContractBank(self, pQryContractBank, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryContractBank)
        with nogil: nRequestID = self.api.ReqQryContractBank(<CQryContractBankField *>address, nRequestID)
        return nRequestID

    def ReqQryParkedOrder(self, pQryParkedOrder, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryParkedOrder)
        with nogil: nRequestID = self.api.ReqQryParkedOrder(<CQryParkedOrderField *>address, nRequestID)
        return nRequestID

    def ReqQryParkedOrderAction(self, pQryParkedOrderAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryParkedOrderAction)
        with nogil: nRequestID = self.api.ReqQryParkedOrderAction(<CQryParkedOrderActionField *>address, nRequestID)
        return nRequestID

    def ReqQryTradingNotice(self, pQryTradingNotice, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryTradingNotice)
        with nogil: nRequestID = self.api.ReqQryTradingNotice(<CQryTradingNoticeField *>address, nRequestID)
        return nRequestID

    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryBrokerTradingParams)
        with nogil: nRequestID = self.api.ReqQryBrokerTradingParams(<CQryBrokerTradingParamsField *>address, nRequestID)
        return nRequestID

    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryBrokerTradingAlgos)
        with nogil: nRequestID = self.api.ReqQryBrokerTradingAlgos(<CQryBrokerTradingAlgosField *>address, nRequestID)
        return nRequestID

    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQueryCFMMCTradingAccountToken)
        with nogil: nRequestID = self.api.ReqQueryCFMMCTradingAccountToken(<CQueryCFMMCTradingAccountTokenField *>address, nRequestID)
        return nRequestID

    def ReqFromBankToFutureByFuture(self, pReqTransfer, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pReqTransfer)
        with nogil: nRequestID = self.api.ReqFromBankToFutureByFuture(<CReqTransferField *>address, nRequestID)
        return nRequestID

    def ReqFromFutureToBankByFuture(self, pReqTransfer, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pReqTransfer)
        with nogil: nRequestID = self.api.ReqFromFutureToBankByFuture(<CReqTransferField *>address, nRequestID)
        return nRequestID

    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pReqQueryAccount)
        with nogil: nRequestID = self.api.ReqQueryBankAccountMoneyByFuture(<CReqQueryAccountField *>address, nRequestID)
        return nRequestID


cdef extern int TraderSpi_OnFrontConnected(self) except -1:
    self.OnFrontConnected()
    return 0

cdef extern int TraderSpi_OnFrontDisconnected(self, int nReason) except -1:
    self.OnFrontDisconnected(nReason)
    return 0

cdef extern int TraderSpi_OnHeartBeatWarning(self, int nTimeLapse) except -1:
    self.OnHeartBeatWarning(nTimeLapse)
    return 0

cdef extern int TraderSpi_OnRspAuthenticate(self, CRspAuthenticateField *pRspAuthenticate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspAuthenticate(None if pRspAuthenticate is NULL else ApiStruct_RspAuthenticate(<size_t>pRspAuthenticate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserLogin(self, CRspUserLoginField *pRspUserLogin, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogin(None if pRspUserLogin is NULL else ApiStruct_RspUserLogin(<size_t>pRspUserLogin), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserLogout(self, CUserLogoutField *pUserLogout, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogout(None if pUserLogout is NULL else ApiStruct_UserLogout(<size_t>pUserLogout), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserPasswordUpdate(self, CUserPasswordUpdateField *pUserPasswordUpdate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserPasswordUpdate(None if pUserPasswordUpdate is NULL else ApiStruct_UserPasswordUpdate(<size_t>pUserPasswordUpdate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspTradingAccountPasswordUpdate(self, CTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspTradingAccountPasswordUpdate(None if pTradingAccountPasswordUpdate is NULL else ApiStruct_TradingAccountPasswordUpdate(<size_t>pTradingAccountPasswordUpdate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspOrderInsert(self, CInputOrderField *pInputOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspOrderInsert(None if pInputOrder is NULL else ApiStruct_InputOrder(<size_t>pInputOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspParkedOrderInsert(self, CParkedOrderField *pParkedOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspParkedOrderInsert(None if pParkedOrder is NULL else ApiStruct_ParkedOrder(<size_t>pParkedOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspParkedOrderAction(self, CParkedOrderActionField *pParkedOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspParkedOrderAction(None if pParkedOrderAction is NULL else ApiStruct_ParkedOrderAction(<size_t>pParkedOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspOrderAction(self, CInputOrderActionField *pInputOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspOrderAction(None if pInputOrderAction is NULL else ApiStruct_InputOrderAction(<size_t>pInputOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQueryMaxOrderVolume(self, CQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQueryMaxOrderVolume(None if pQueryMaxOrderVolume is NULL else ApiStruct_QueryMaxOrderVolume(<size_t>pQueryMaxOrderVolume), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspSettlementInfoConfirm(self, CSettlementInfoConfirmField *pSettlementInfoConfirm, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspSettlementInfoConfirm(None if pSettlementInfoConfirm is NULL else ApiStruct_SettlementInfoConfirm(<size_t>pSettlementInfoConfirm), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspRemoveParkedOrder(self, CRemoveParkedOrderField *pRemoveParkedOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspRemoveParkedOrder(None if pRemoveParkedOrder is NULL else ApiStruct_RemoveParkedOrder(<size_t>pRemoveParkedOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspRemoveParkedOrderAction(self, CRemoveParkedOrderActionField *pRemoveParkedOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspRemoveParkedOrderAction(None if pRemoveParkedOrderAction is NULL else ApiStruct_RemoveParkedOrderAction(<size_t>pRemoveParkedOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspExecOrderInsert(self, CInputExecOrderField *pInputExecOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspExecOrderInsert(None if pInputExecOrder is NULL else ApiStruct_InputExecOrder(<size_t>pInputExecOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspExecOrderAction(self, CInputExecOrderActionField *pInputExecOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspExecOrderAction(None if pInputExecOrderAction is NULL else ApiStruct_InputExecOrderAction(<size_t>pInputExecOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspForQuoteInsert(self, CInputForQuoteField *pInputForQuote, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspForQuoteInsert(None if pInputForQuote is NULL else ApiStruct_InputForQuote(<size_t>pInputForQuote), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQuoteInsert(self, CInputQuoteField *pInputQuote, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQuoteInsert(None if pInputQuote is NULL else ApiStruct_InputQuote(<size_t>pInputQuote), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQuoteAction(self, CInputQuoteActionField *pInputQuoteAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQuoteAction(None if pInputQuoteAction is NULL else ApiStruct_InputQuoteAction(<size_t>pInputQuoteAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspCombActionInsert(self, CInputCombActionField *pInputCombAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspCombActionInsert(None if pInputCombAction is NULL else ApiStruct_InputCombAction(<size_t>pInputCombAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryOrder(self, COrderField *pOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryOrder(None if pOrder is NULL else ApiStruct_Order(<size_t>pOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTrade(self, CTradeField *pTrade, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTrade(None if pTrade is NULL else ApiStruct_Trade(<size_t>pTrade), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPosition(self, CInvestorPositionField *pInvestorPosition, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInvestorPosition(None if pInvestorPosition is NULL else ApiStruct_InvestorPosition(<size_t>pInvestorPosition), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTradingAccount(self, CTradingAccountField *pTradingAccount, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTradingAccount(None if pTradingAccount is NULL else ApiStruct_TradingAccount(<size_t>pTradingAccount), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestor(self, CInvestorField *pInvestor, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInvestor(None if pInvestor is NULL else ApiStruct_Investor(<size_t>pInvestor), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTradingCode(self, CTradingCodeField *pTradingCode, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTradingCode(None if pTradingCode is NULL else ApiStruct_TradingCode(<size_t>pTradingCode), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrumentMarginRate(self, CInstrumentMarginRateField *pInstrumentMarginRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInstrumentMarginRate(None if pInstrumentMarginRate is NULL else ApiStruct_InstrumentMarginRate(<size_t>pInstrumentMarginRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrumentCommissionRate(self, CInstrumentCommissionRateField *pInstrumentCommissionRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInstrumentCommissionRate(None if pInstrumentCommissionRate is NULL else ApiStruct_InstrumentCommissionRate(<size_t>pInstrumentCommissionRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchange(self, CExchangeField *pExchange, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryExchange(None if pExchange is NULL else ApiStruct_Exchange(<size_t>pExchange), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryProduct(self, CProductField *pProduct, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryProduct(None if pProduct is NULL else ApiStruct_Product(<size_t>pProduct), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrument(self, CInstrumentField *pInstrument, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInstrument(None if pInstrument is NULL else ApiStruct_Instrument(<size_t>pInstrument), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryDepthMarketData(self, CDepthMarketDataField *pDepthMarketData, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryDepthMarketData(None if pDepthMarketData is NULL else ApiStruct_DepthMarketData(<size_t>pDepthMarketData), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQrySettlementInfo(self, CSettlementInfoField *pSettlementInfo, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQrySettlementInfo(None if pSettlementInfo is NULL else ApiStruct_SettlementInfo(<size_t>pSettlementInfo), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTransferBank(self, CTransferBankField *pTransferBank, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTransferBank(None if pTransferBank is NULL else ApiStruct_TransferBank(<size_t>pTransferBank), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPositionDetail(self, CInvestorPositionDetailField *pInvestorPositionDetail, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInvestorPositionDetail(None if pInvestorPositionDetail is NULL else ApiStruct_InvestorPositionDetail(<size_t>pInvestorPositionDetail), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryNotice(self, CNoticeField *pNotice, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryNotice(None if pNotice is NULL else ApiStruct_Notice(<size_t>pNotice), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQrySettlementInfoConfirm(self, CSettlementInfoConfirmField *pSettlementInfoConfirm, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQrySettlementInfoConfirm(None if pSettlementInfoConfirm is NULL else ApiStruct_SettlementInfoConfirm(<size_t>pSettlementInfoConfirm), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPositionCombineDetail(self, CInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInvestorPositionCombineDetail(None if pInvestorPositionCombineDetail is NULL else ApiStruct_InvestorPositionCombineDetail(<size_t>pInvestorPositionCombineDetail), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryCFMMCTradingAccountKey(self, CCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryCFMMCTradingAccountKey(None if pCFMMCTradingAccountKey is NULL else ApiStruct_CFMMCTradingAccountKey(<size_t>pCFMMCTradingAccountKey), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryEWarrantOffset(self, CEWarrantOffsetField *pEWarrantOffset, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryEWarrantOffset(None if pEWarrantOffset is NULL else ApiStruct_EWarrantOffset(<size_t>pEWarrantOffset), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestorProductGroupMargin(self, CInvestorProductGroupMarginField *pInvestorProductGroupMargin, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInvestorProductGroupMargin(None if pInvestorProductGroupMargin is NULL else ApiStruct_InvestorProductGroupMargin(<size_t>pInvestorProductGroupMargin), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchangeMarginRate(self, CExchangeMarginRateField *pExchangeMarginRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryExchangeMarginRate(None if pExchangeMarginRate is NULL else ApiStruct_ExchangeMarginRate(<size_t>pExchangeMarginRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchangeMarginRateAdjust(self, CExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryExchangeMarginRateAdjust(None if pExchangeMarginRateAdjust is NULL else ApiStruct_ExchangeMarginRateAdjust(<size_t>pExchangeMarginRateAdjust), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchangeRate(self, CExchangeRateField *pExchangeRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryExchangeRate(None if pExchangeRate is NULL else ApiStruct_ExchangeRate(<size_t>pExchangeRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQrySecAgentACIDMap(self, CSecAgentACIDMapField *pSecAgentACIDMap, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQrySecAgentACIDMap(None if pSecAgentACIDMap is NULL else ApiStruct_SecAgentACIDMap(<size_t>pSecAgentACIDMap), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryProductExchRate(self, CProductExchRateField *pProductExchRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryProductExchRate(None if pProductExchRate is NULL else ApiStruct_ProductExchRate(<size_t>pProductExchRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryOptionInstrTradeCost(self, COptionInstrTradeCostField *pOptionInstrTradeCost, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryOptionInstrTradeCost(None if pOptionInstrTradeCost is NULL else ApiStruct_OptionInstrTradeCost(<size_t>pOptionInstrTradeCost), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryOptionInstrCommRate(self, COptionInstrCommRateField *pOptionInstrCommRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryOptionInstrCommRate(None if pOptionInstrCommRate is NULL else ApiStruct_OptionInstrCommRate(<size_t>pOptionInstrCommRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExecOrder(self, CExecOrderField *pExecOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryExecOrder(None if pExecOrder is NULL else ApiStruct_ExecOrder(<size_t>pExecOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryForQuote(self, CForQuoteField *pForQuote, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryForQuote(None if pForQuote is NULL else ApiStruct_ForQuote(<size_t>pForQuote), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryQuote(self, CQuoteField *pQuote, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryQuote(None if pQuote is NULL else ApiStruct_Quote(<size_t>pQuote), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryCombInstrumentGuard(self, CCombInstrumentGuardField *pCombInstrumentGuard, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryCombInstrumentGuard(None if pCombInstrumentGuard is NULL else ApiStruct_CombInstrumentGuard(<size_t>pCombInstrumentGuard), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryCombAction(self, CCombActionField *pCombAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryCombAction(None if pCombAction is NULL else ApiStruct_CombAction(<size_t>pCombAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTransferSerial(self, CTransferSerialField *pTransferSerial, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTransferSerial(None if pTransferSerial is NULL else ApiStruct_TransferSerial(<size_t>pTransferSerial), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryAccountregister(self, CAccountregisterField *pAccountregister, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryAccountregister(None if pAccountregister is NULL else ApiStruct_Accountregister(<size_t>pAccountregister), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspError(self, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspError(None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRtnOrder(self, COrderField *pOrder) except -1:
    self.OnRtnOrder(None if pOrder is NULL else ApiStruct_Order(<size_t>pOrder))
    return 0

cdef extern int TraderSpi_OnRtnTrade(self, CTradeField *pTrade) except -1:
    self.OnRtnTrade(None if pTrade is NULL else ApiStruct_Trade(<size_t>pTrade))
    return 0

cdef extern int TraderSpi_OnErrRtnOrderInsert(self, CInputOrderField *pInputOrder, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnOrderInsert(None if pInputOrder is NULL else ApiStruct_InputOrder(<size_t>pInputOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnOrderAction(self, COrderActionField *pOrderAction, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnOrderAction(None if pOrderAction is NULL else ApiStruct_OrderAction(<size_t>pOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnInstrumentStatus(self, CInstrumentStatusField *pInstrumentStatus) except -1:
    self.OnRtnInstrumentStatus(None if pInstrumentStatus is NULL else ApiStruct_InstrumentStatus(<size_t>pInstrumentStatus))
    return 0

cdef extern int TraderSpi_OnRtnTradingNotice(self, CTradingNoticeInfoField *pTradingNoticeInfo) except -1:
    self.OnRtnTradingNotice(None if pTradingNoticeInfo is NULL else ApiStruct_TradingNoticeInfo(<size_t>pTradingNoticeInfo))
    return 0

cdef extern int TraderSpi_OnRtnErrorConditionalOrder(self, CErrorConditionalOrderField *pErrorConditionalOrder) except -1:
    self.OnRtnErrorConditionalOrder(None if pErrorConditionalOrder is NULL else ApiStruct_ErrorConditionalOrder(<size_t>pErrorConditionalOrder))
    return 0

cdef extern int TraderSpi_OnRtnExecOrder(self, CExecOrderField *pExecOrder) except -1:
    self.OnRtnExecOrder(None if pExecOrder is NULL else ApiStruct_ExecOrder(<size_t>pExecOrder))
    return 0

cdef extern int TraderSpi_OnErrRtnExecOrderInsert(self, CInputExecOrderField *pInputExecOrder, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnExecOrderInsert(None if pInputExecOrder is NULL else ApiStruct_InputExecOrder(<size_t>pInputExecOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnExecOrderAction(self, CExecOrderActionField *pExecOrderAction, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnExecOrderAction(None if pExecOrderAction is NULL else ApiStruct_ExecOrderAction(<size_t>pExecOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnForQuoteInsert(self, CInputForQuoteField *pInputForQuote, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnForQuoteInsert(None if pInputForQuote is NULL else ApiStruct_InputForQuote(<size_t>pInputForQuote), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnQuote(self, CQuoteField *pQuote) except -1:
    self.OnRtnQuote(None if pQuote is NULL else ApiStruct_Quote(<size_t>pQuote))
    return 0

cdef extern int TraderSpi_OnErrRtnQuoteInsert(self, CInputQuoteField *pInputQuote, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQuoteInsert(None if pInputQuote is NULL else ApiStruct_InputQuote(<size_t>pInputQuote), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnQuoteAction(self, CQuoteActionField *pQuoteAction, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQuoteAction(None if pQuoteAction is NULL else ApiStruct_QuoteAction(<size_t>pQuoteAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnForQuoteRsp(self, CForQuoteRspField *pForQuoteRsp) except -1:
    self.OnRtnForQuoteRsp(None if pForQuoteRsp is NULL else ApiStruct_ForQuoteRsp(<size_t>pForQuoteRsp))
    return 0

cdef extern int TraderSpi_OnRtnCFMMCTradingAccountToken(self, CCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) except -1:
    self.OnRtnCFMMCTradingAccountToken(None if pCFMMCTradingAccountToken is NULL else ApiStruct_CFMMCTradingAccountToken(<size_t>pCFMMCTradingAccountToken))
    return 0

cdef extern int TraderSpi_OnRtnCombAction(self, CCombActionField *pCombAction) except -1:
    self.OnRtnCombAction(None if pCombAction is NULL else ApiStruct_CombAction(<size_t>pCombAction))
    return 0

cdef extern int TraderSpi_OnErrRtnCombActionInsert(self, CInputCombActionField *pInputCombAction, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnCombActionInsert(None if pInputCombAction is NULL else ApiStruct_InputCombAction(<size_t>pInputCombAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnRspQryContractBank(self, CContractBankField *pContractBank, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryContractBank(None if pContractBank is NULL else ApiStruct_ContractBank(<size_t>pContractBank), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryParkedOrder(self, CParkedOrderField *pParkedOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryParkedOrder(None if pParkedOrder is NULL else ApiStruct_ParkedOrder(<size_t>pParkedOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryParkedOrderAction(self, CParkedOrderActionField *pParkedOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryParkedOrderAction(None if pParkedOrderAction is NULL else ApiStruct_ParkedOrderAction(<size_t>pParkedOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTradingNotice(self, CTradingNoticeField *pTradingNotice, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTradingNotice(None if pTradingNotice is NULL else ApiStruct_TradingNotice(<size_t>pTradingNotice), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryBrokerTradingParams(self, CBrokerTradingParamsField *pBrokerTradingParams, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryBrokerTradingParams(None if pBrokerTradingParams is NULL else ApiStruct_BrokerTradingParams(<size_t>pBrokerTradingParams), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryBrokerTradingAlgos(self, CBrokerTradingAlgosField *pBrokerTradingAlgos, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryBrokerTradingAlgos(None if pBrokerTradingAlgos is NULL else ApiStruct_BrokerTradingAlgos(<size_t>pBrokerTradingAlgos), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQueryCFMMCTradingAccountToken(self, CQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQueryCFMMCTradingAccountToken(None if pQueryCFMMCTradingAccountToken is NULL else ApiStruct_QueryCFMMCTradingAccountToken(<size_t>pQueryCFMMCTradingAccountToken), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRtnFromBankToFutureByBank(self, CRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromBankToFutureByBank(None if pRspTransfer is NULL else ApiStruct_RspTransfer(<size_t>pRspTransfer))
    return 0

cdef extern int TraderSpi_OnRtnFromFutureToBankByBank(self, CRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromFutureToBankByBank(None if pRspTransfer is NULL else ApiStruct_RspTransfer(<size_t>pRspTransfer))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByBank(self, CRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByBank(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByBank(self, CRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByBank(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnFromBankToFutureByFuture(self, CRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromBankToFutureByFuture(None if pRspTransfer is NULL else ApiStruct_RspTransfer(<size_t>pRspTransfer))
    return 0

cdef extern int TraderSpi_OnRtnFromFutureToBankByFuture(self, CRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromFutureToBankByFuture(None if pRspTransfer is NULL else ApiStruct_RspTransfer(<size_t>pRspTransfer))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(self, CRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByFutureManual(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(self, CRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByFutureManual(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnQueryBankBalanceByFuture(self, CNotifyQueryAccountField *pNotifyQueryAccount) except -1:
    self.OnRtnQueryBankBalanceByFuture(None if pNotifyQueryAccount is NULL else ApiStruct_NotifyQueryAccount(<size_t>pNotifyQueryAccount))
    return 0

cdef extern int TraderSpi_OnErrRtnBankToFutureByFuture(self, CReqTransferField *pReqTransfer, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnBankToFutureByFuture(None if pReqTransfer is NULL else ApiStruct_ReqTransfer(<size_t>pReqTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnFutureToBankByFuture(self, CReqTransferField *pReqTransfer, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnFutureToBankByFuture(None if pReqTransfer is NULL else ApiStruct_ReqTransfer(<size_t>pReqTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(self, CReqRepealField *pReqRepeal, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnRepealBankToFutureByFutureManual(None if pReqRepeal is NULL else ApiStruct_ReqRepeal(<size_t>pReqRepeal), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(self, CReqRepealField *pReqRepeal, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnRepealFutureToBankByFutureManual(None if pReqRepeal is NULL else ApiStruct_ReqRepeal(<size_t>pReqRepeal), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnQueryBankBalanceByFuture(self, CReqQueryAccountField *pReqQueryAccount, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQueryBankBalanceByFuture(None if pReqQueryAccount is NULL else ApiStruct_ReqQueryAccount(<size_t>pReqQueryAccount), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByFuture(self, CRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByFuture(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByFuture(self, CRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByFuture(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRspFromBankToFutureByFuture(self, CReqTransferField *pReqTransfer, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspFromBankToFutureByFuture(None if pReqTransfer is NULL else ApiStruct_ReqTransfer(<size_t>pReqTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspFromFutureToBankByFuture(self, CReqTransferField *pReqTransfer, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspFromFutureToBankByFuture(None if pReqTransfer is NULL else ApiStruct_ReqTransfer(<size_t>pReqTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQueryBankAccountMoneyByFuture(self, CReqQueryAccountField *pReqQueryAccount, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQueryBankAccountMoneyByFuture(None if pReqQueryAccount is NULL else ApiStruct_ReqQueryAccount(<size_t>pReqQueryAccount), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRtnOpenAccountByBank(self, COpenAccountField *pOpenAccount) except -1:
    self.OnRtnOpenAccountByBank(None if pOpenAccount is NULL else ApiStruct_OpenAccount(<size_t>pOpenAccount))
    return 0

cdef extern int TraderSpi_OnRtnCancelAccountByBank(self, CCancelAccountField *pCancelAccount) except -1:
    self.OnRtnCancelAccountByBank(None if pCancelAccount is NULL else ApiStruct_CancelAccount(<size_t>pCancelAccount))
    return 0

cdef extern int TraderSpi_OnRtnChangeAccountByBank(self, CChangeAccountField *pChangeAccount) except -1:
    self.OnRtnChangeAccountByBank(None if pChangeAccount is NULL else ApiStruct_ChangeAccount(<size_t>pChangeAccount))
    return 0
