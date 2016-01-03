# -*- coding: utf-8 -*-

from cTraderApi cimport *

cdef ApiStruct_addressof, ApiStruct_BondInterest, ApiStruct_DepthMarketData, ApiStruct_Exchange, ApiStruct_FundTransfer, ApiStruct_InputFundTransfer, ApiStruct_InputOrder, ApiStruct_InputOrderAction, ApiStruct_Instrument, ApiStruct_InstrumentCommissionRate, ApiStruct_Investor, ApiStruct_InvestorPosition, ApiStruct_MarketRationInfo, ApiStruct_Order, ApiStruct_OrderAction, ApiStruct_RspInfo, ApiStruct_RspUserLogin, ApiStruct_Trade, ApiStruct_TradingAccount, ApiStruct_TradingAccountPasswordUpdate, ApiStruct_TradingCode, ApiStruct_UserLogout, ApiStruct_UserPasswordUpdate
cdef extern _init(self, m):
    global ApiStruct_addressof, ApiStruct_BondInterest, ApiStruct_DepthMarketData, ApiStruct_Exchange, ApiStruct_FundTransfer, ApiStruct_InputFundTransfer, ApiStruct_InputOrder, ApiStruct_InputOrderAction, ApiStruct_Instrument, ApiStruct_InstrumentCommissionRate, ApiStruct_Investor, ApiStruct_InvestorPosition, ApiStruct_MarketRationInfo, ApiStruct_Order, ApiStruct_OrderAction, ApiStruct_RspInfo, ApiStruct_RspUserLogin, ApiStruct_Trade, ApiStruct_TradingAccount, ApiStruct_TradingAccountPasswordUpdate, ApiStruct_TradingCode, ApiStruct_UserLogout, ApiStruct_UserPasswordUpdate
    ApiStruct_addressof = XGetAttr(PyImport_ImportModule(S_ctypes), S_addressof)
    fa = XStr(S_from_address)
    ApiStruct_BondInterest = XGotAttr(XGetAttr(m, S_BondInterest), fa)
    ApiStruct_DepthMarketData = XGotAttr(XGetAttr(m, S_DepthMarketData), fa)
    ApiStruct_Exchange = XGotAttr(XGetAttr(m, S_Exchange), fa)
    ApiStruct_FundTransfer = XGotAttr(XGetAttr(m, S_FundTransfer), fa)
    ApiStruct_InputFundTransfer = XGotAttr(XGetAttr(m, S_InputFundTransfer), fa)
    ApiStruct_InputOrder = XGotAttr(XGetAttr(m, S_InputOrder), fa)
    ApiStruct_InputOrderAction = XGotAttr(XGetAttr(m, S_InputOrderAction), fa)
    ApiStruct_Instrument = XGotAttr(XGetAttr(m, S_Instrument), fa)
    ApiStruct_InstrumentCommissionRate = XGotAttr(XGetAttr(m, S_InstrumentCommissionRate), fa)
    ApiStruct_Investor = XGotAttr(XGetAttr(m, S_Investor), fa)
    ApiStruct_InvestorPosition = XGotAttr(XGetAttr(m, S_InvestorPosition), fa)
    ApiStruct_MarketRationInfo = XGotAttr(XGetAttr(m, S_MarketRationInfo), fa)
    ApiStruct_Order = XGotAttr(XGetAttr(m, S_Order), fa)
    ApiStruct_OrderAction = XGotAttr(XGetAttr(m, S_OrderAction), fa)
    ApiStruct_RspInfo = XGotAttr(XGetAttr(m, S_RspInfo), fa)
    ApiStruct_RspUserLogin = XGotAttr(XGetAttr(m, S_RspUserLogin), fa)
    ApiStruct_Trade = XGotAttr(XGetAttr(m, S_Trade), fa)
    ApiStruct_TradingAccount = XGotAttr(XGetAttr(m, S_TradingAccount), fa)
    ApiStruct_TradingAccountPasswordUpdate = XGotAttr(XGetAttr(m, S_TradingAccountPasswordUpdate), fa)
    ApiStruct_TradingCode = XGotAttr(XGetAttr(m, S_TradingCode), fa)
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

    def SubscribePrivateTopic(self, TE_RESUME_TYPE nResumeType):
        if self.api is NULL: return
        self.api.SubscribePrivateTopic(nResumeType)

    def SubscribePublicTopic(self, TE_RESUME_TYPE nResumeType):
        if self.api is NULL: return
        self.api.SubscribePublicTopic(nResumeType)

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

    def ReqOrderInsert(self, pInputOrder, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputOrder)
        with nogil: nRequestID = self.api.ReqOrderInsert(<CInputOrderField *>address, nRequestID)
        return nRequestID

    def ReqOrderAction(self, pInputOrderAction, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputOrderAction)
        with nogil: nRequestID = self.api.ReqOrderAction(<CInputOrderActionField *>address, nRequestID)
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

    def ReqQryExchange(self, pQryExchange, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryExchange)
        with nogil: nRequestID = self.api.ReqQryExchange(<CQryExchangeField *>address, nRequestID)
        return nRequestID

    def ReqQryInstrument(self, pQryInstrument, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInstrument)
        with nogil: nRequestID = self.api.ReqQryInstrument(<CQryInstrumentField *>address, nRequestID)
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

    def ReqQryTradingAccount(self, pQryTradingAccount, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryTradingAccount)
        with nogil: nRequestID = self.api.ReqQryTradingAccount(<CQryTradingAccountField *>address, nRequestID)
        return nRequestID

    def ReqQryDepthMarketData(self, pQryDepthMarketData, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryDepthMarketData)
        with nogil: nRequestID = self.api.ReqQryDepthMarketData(<CQryDepthMarketDataField *>address, nRequestID)
        return nRequestID

    def ReqQryBondInterest(self, pQryBondInterest, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryBondInterest)
        with nogil: nRequestID = self.api.ReqQryBondInterest(<CQryBondInterestField *>address, nRequestID)
        return nRequestID

    def ReqQryMarketRationInfo(self, pQryMarketRationInfo, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryMarketRationInfo)
        with nogil: nRequestID = self.api.ReqQryMarketRationInfo(<CQryMarketRationInfoField *>address, nRequestID)
        return nRequestID

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInstrumentCommissionRate)
        with nogil: nRequestID = self.api.ReqQryInstrumentCommissionRate(<CQryInstrumentCommissionRateField *>address, nRequestID)
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

    def ReqFundOutByLiber(self, pInputFundTransfer, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pInputFundTransfer)
        with nogil: nRequestID = self.api.ReqFundOutByLiber(<CInputFundTransferField *>address, nRequestID)
        return nRequestID

    def ReqQryFundTransferSerial(self, pQryFundTransferSerial, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryFundTransferSerial)
        with nogil: nRequestID = self.api.ReqQryFundTransferSerial(<CQryFundTransferSerialField *>address, nRequestID)
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

cdef extern int TraderSpi_OnRspError(self, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspError(None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserLogin(self, CRspUserLoginField *pRspUserLogin, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogin(None if pRspUserLogin is NULL else ApiStruct_RspUserLogin(<size_t>pRspUserLogin), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserLogout(self, CUserLogoutField *pUserLogout, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogout(None if pUserLogout is NULL else ApiStruct_UserLogout(<size_t>pUserLogout), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspOrderInsert(self, CInputOrderField *pInputOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspOrderInsert(None if pInputOrder is NULL else ApiStruct_InputOrder(<size_t>pInputOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspOrderAction(self, CInputOrderActionField *pInputOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspOrderAction(None if pInputOrderAction is NULL else ApiStruct_InputOrderAction(<size_t>pInputOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserPasswordUpdate(self, CUserPasswordUpdateField *pUserPasswordUpdate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserPasswordUpdate(None if pUserPasswordUpdate is NULL else ApiStruct_UserPasswordUpdate(<size_t>pUserPasswordUpdate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspTradingAccountPasswordUpdate(self, CTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspTradingAccountPasswordUpdate(None if pTradingAccountPasswordUpdate is NULL else ApiStruct_TradingAccountPasswordUpdate(<size_t>pTradingAccountPasswordUpdate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchange(self, CExchangeField *pExchange, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryExchange(None if pExchange is NULL else ApiStruct_Exchange(<size_t>pExchange), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrument(self, CInstrumentField *pInstrument, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInstrument(None if pInstrument is NULL else ApiStruct_Instrument(<size_t>pInstrument), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestor(self, CInvestorField *pInvestor, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInvestor(None if pInvestor is NULL else ApiStruct_Investor(<size_t>pInvestor), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTradingCode(self, CTradingCodeField *pTradingCode, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTradingCode(None if pTradingCode is NULL else ApiStruct_TradingCode(<size_t>pTradingCode), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTradingAccount(self, CTradingAccountField *pTradingAccount, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTradingAccount(None if pTradingAccount is NULL else ApiStruct_TradingAccount(<size_t>pTradingAccount), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryDepthMarketData(self, CDepthMarketDataField *pDepthMarketData, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryDepthMarketData(None if pDepthMarketData is NULL else ApiStruct_DepthMarketData(<size_t>pDepthMarketData), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryBondInterest(self, CBondInterestField *pBondInterest, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryBondInterest(None if pBondInterest is NULL else ApiStruct_BondInterest(<size_t>pBondInterest), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryMarketRationInfo(self, CMarketRationInfoField *pMarketRationInfo, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryMarketRationInfo(None if pMarketRationInfo is NULL else ApiStruct_MarketRationInfo(<size_t>pMarketRationInfo), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrumentCommissionRate(self, CInstrumentCommissionRateField *pInstrumentCommissionRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInstrumentCommissionRate(None if pInstrumentCommissionRate is NULL else ApiStruct_InstrumentCommissionRate(<size_t>pInstrumentCommissionRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
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

cdef extern int TraderSpi_OnRspFundOutByLiber(self, CInputFundTransferField *pInputFundTransfer, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspFundOutByLiber(None if pInputFundTransfer is NULL else ApiStruct_InputFundTransfer(<size_t>pInputFundTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRtnFundOutByLiber(self, CFundTransferField *pFundTransfer) except -1:
    self.OnRtnFundOutByLiber(None if pFundTransfer is NULL else ApiStruct_FundTransfer(<size_t>pFundTransfer))
    return 0

cdef extern int TraderSpi_OnErrRtnFundOutByLiber(self, CInputFundTransferField *pInputFundTransfer, CRspInfoField *pRspInfo) except -1:
    self.OnErrRtnFundOutByLiber(None if pInputFundTransfer is NULL else ApiStruct_InputFundTransfer(<size_t>pInputFundTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnFundInByBank(self, CFundTransferField *pFundTransfer) except -1:
    self.OnRtnFundInByBank(None if pFundTransfer is NULL else ApiStruct_FundTransfer(<size_t>pFundTransfer))
    return 0

cdef extern int TraderSpi_OnRspQryFundTransferSerial(self, CFundTransferField *pFundTransfer, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryFundTransferSerial(None if pFundTransfer is NULL else ApiStruct_FundTransfer(<size_t>pFundTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0
