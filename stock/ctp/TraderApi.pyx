# -*- coding: utf-8 -*-

from cTraderApi cimport *

cdef ApiStruct_addressof, ApiStruct_DepthMarketData, ApiStruct_Exchange, ApiStruct_InputOrder, ApiStruct_InputOrderAction, ApiStruct_Instrument, ApiStruct_InstrumentCommissionRate, ApiStruct_InstrumentStatus, ApiStruct_Investor, ApiStruct_InvestorPosition, ApiStruct_InvestorPositionDetail, ApiStruct_Order, ApiStruct_OrderAction, ApiStruct_QueryMaxOrderVolume, ApiStruct_RspAuthenticate, ApiStruct_RspInfo, ApiStruct_RspUserLogin, ApiStruct_Trade, ApiStruct_TradingAccount, ApiStruct_TradingAccountPasswordUpdate, ApiStruct_TradingCode, ApiStruct_UserLogout, ApiStruct_UserPasswordUpdate
cdef extern _init(self, m):
    global ApiStruct_addressof, ApiStruct_DepthMarketData, ApiStruct_Exchange, ApiStruct_InputOrder, ApiStruct_InputOrderAction, ApiStruct_Instrument, ApiStruct_InstrumentCommissionRate, ApiStruct_InstrumentStatus, ApiStruct_Investor, ApiStruct_InvestorPosition, ApiStruct_InvestorPositionDetail, ApiStruct_Order, ApiStruct_OrderAction, ApiStruct_QueryMaxOrderVolume, ApiStruct_RspAuthenticate, ApiStruct_RspInfo, ApiStruct_RspUserLogin, ApiStruct_Trade, ApiStruct_TradingAccount, ApiStruct_TradingAccountPasswordUpdate, ApiStruct_TradingCode, ApiStruct_UserLogout, ApiStruct_UserPasswordUpdate
    ApiStruct_addressof = XGetAttr(PyImport_ImportModule(S_ctypes), S_addressof)
    fa = XStr(S_from_address)
    ApiStruct_DepthMarketData = XGotAttr(XGetAttr(m, S_DepthMarketData), fa)
    ApiStruct_Exchange = XGotAttr(XGetAttr(m, S_Exchange), fa)
    ApiStruct_InputOrder = XGotAttr(XGetAttr(m, S_InputOrder), fa)
    ApiStruct_InputOrderAction = XGotAttr(XGetAttr(m, S_InputOrderAction), fa)
    ApiStruct_Instrument = XGotAttr(XGetAttr(m, S_Instrument), fa)
    ApiStruct_InstrumentCommissionRate = XGotAttr(XGetAttr(m, S_InstrumentCommissionRate), fa)
    ApiStruct_InstrumentStatus = XGotAttr(XGetAttr(m, S_InstrumentStatus), fa)
    ApiStruct_Investor = XGotAttr(XGetAttr(m, S_Investor), fa)
    ApiStruct_InvestorPosition = XGotAttr(XGetAttr(m, S_InvestorPosition), fa)
    ApiStruct_InvestorPositionDetail = XGotAttr(XGetAttr(m, S_InvestorPositionDetail), fa)
    ApiStruct_Order = XGotAttr(XGetAttr(m, S_Order), fa)
    ApiStruct_OrderAction = XGotAttr(XGetAttr(m, S_OrderAction), fa)
    ApiStruct_QueryMaxOrderVolume = XGotAttr(XGetAttr(m, S_QueryMaxOrderVolume), fa)
    ApiStruct_RspAuthenticate = XGotAttr(XGetAttr(m, S_RspAuthenticate), fa)
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

    def Create(self, const_char *pszFlowPath="", cbool bIsUsingUdp=False):
        if self.api is not NULL: return
        self.api = CreateFtdcTraderApi(pszFlowPath, bIsUsingUdp)
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

    # def RegisterNameServer(self, char *pszNsAddress):
        # if self.api is NULL: return
        # self.api.RegisterNameServer(pszNsAddress)

    # def RegisterFensUserInfo(self, pFensUserInfo):
        # if self.api is NULL: return
        # self.api.RegisterFensUserInfo(<CFensUserInfoField *><size_t>ApiStruct_addressof(pFensUserInfo))

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

    # def ReqParkedOrderInsert(self, pParkedOrder, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pParkedOrder)
        # with nogil: nRequestID = self.api.ReqParkedOrderInsert(<CParkedOrderField *>address, nRequestID)
        # return nRequestID

    # def ReqParkedOrderAction(self, pParkedOrderAction, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pParkedOrderAction)
        # with nogil: nRequestID = self.api.ReqParkedOrderAction(<CParkedOrderActionField *>address, nRequestID)
        # return nRequestID

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

    # def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pSettlementInfoConfirm)
        # with nogil: nRequestID = self.api.ReqSettlementInfoConfirm(<CSettlementInfoConfirmField *>address, nRequestID)
        # return nRequestID

    # def ReqRemoveParkedOrder(self, pRemoveParkedOrder, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pRemoveParkedOrder)
        # with nogil: nRequestID = self.api.ReqRemoveParkedOrder(<CRemoveParkedOrderField *>address, nRequestID)
        # return nRequestID

    # def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pRemoveParkedOrderAction)
        # with nogil: nRequestID = self.api.ReqRemoveParkedOrderAction(<CRemoveParkedOrderActionField *>address, nRequestID)
        # return nRequestID

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

    # def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryInstrumentMarginRate)
        # with nogil: nRequestID = self.api.ReqQryInstrumentMarginRate(<CQryInstrumentMarginRateField *>address, nRequestID)
        # return nRequestID

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

    # def ReqQrySettlementInfo(self, pQrySettlementInfo, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQrySettlementInfo)
        # with nogil: nRequestID = self.api.ReqQrySettlementInfo(<CQrySettlementInfoField *>address, nRequestID)
        # return nRequestID

    # def ReqQryTransferBank(self, pQryTransferBank, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryTransferBank)
        # with nogil: nRequestID = self.api.ReqQryTransferBank(<CQryTransferBankField *>address, nRequestID)
        # return nRequestID

    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail, int nRequestID):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pQryInvestorPositionDetail)
        with nogil: nRequestID = self.api.ReqQryInvestorPositionDetail(<CQryInvestorPositionDetailField *>address, nRequestID)
        return nRequestID

    # def ReqQryNotice(self, pQryNotice, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryNotice)
        # with nogil: nRequestID = self.api.ReqQryNotice(<CQryNoticeField *>address, nRequestID)
        # return nRequestID

    # def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQrySettlementInfoConfirm)
        # with nogil: nRequestID = self.api.ReqQrySettlementInfoConfirm(<CQrySettlementInfoConfirmField *>address, nRequestID)
        # return nRequestID

    # def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryInvestorPositionCombineDetail)
        # with nogil: nRequestID = self.api.ReqQryInvestorPositionCombineDetail(<CQryInvestorPositionCombineDetailField *>address, nRequestID)
        # return nRequestID

    # def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryCFMMCTradingAccountKey)
        # with nogil: nRequestID = self.api.ReqQryCFMMCTradingAccountKey(<CQryCFMMCTradingAccountKeyField *>address, nRequestID)
        # return nRequestID

    # def ReqQryEWarrantOffset(self, pQryEWarrantOffset, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryEWarrantOffset)
        # with nogil: nRequestID = self.api.ReqQryEWarrantOffset(<CQryEWarrantOffsetField *>address, nRequestID)
        # return nRequestID

    # def ReqQryTransferSerial(self, pQryTransferSerial, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryTransferSerial)
        # with nogil: nRequestID = self.api.ReqQryTransferSerial(<CQryTransferSerialField *>address, nRequestID)
        # return nRequestID

    # def ReqQryAccountregister(self, pQryAccountregister, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryAccountregister)
        # with nogil: nRequestID = self.api.ReqQryAccountregister(<CQryAccountregisterField *>address, nRequestID)
        # return nRequestID

    # def ReqQryContractBank(self, pQryContractBank, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryContractBank)
        # with nogil: nRequestID = self.api.ReqQryContractBank(<CQryContractBankField *>address, nRequestID)
        # return nRequestID

    # def ReqQryParkedOrder(self, pQryParkedOrder, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryParkedOrder)
        # with nogil: nRequestID = self.api.ReqQryParkedOrder(<CQryParkedOrderField *>address, nRequestID)
        # return nRequestID

    # def ReqQryParkedOrderAction(self, pQryParkedOrderAction, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryParkedOrderAction)
        # with nogil: nRequestID = self.api.ReqQryParkedOrderAction(<CQryParkedOrderActionField *>address, nRequestID)
        # return nRequestID

    # def ReqQryTradingNotice(self, pQryTradingNotice, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryTradingNotice)
        # with nogil: nRequestID = self.api.ReqQryTradingNotice(<CQryTradingNoticeField *>address, nRequestID)
        # return nRequestID

    # def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryBrokerTradingParams)
        # with nogil: nRequestID = self.api.ReqQryBrokerTradingParams(<CQryBrokerTradingParamsField *>address, nRequestID)
        # return nRequestID

    # def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pQryBrokerTradingAlgos)
        # with nogil: nRequestID = self.api.ReqQryBrokerTradingAlgos(<CQryBrokerTradingAlgosField *>address, nRequestID)
        # return nRequestID

    # def ReqFromBankToFutureByFuture(self, pReqTransfer, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pReqTransfer)
        # with nogil: nRequestID = self.api.ReqFromBankToFutureByFuture(<CReqTransferField *>address, nRequestID)
        # return nRequestID

    # def ReqFromFutureToBankByFuture(self, pReqTransfer, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pReqTransfer)
        # with nogil: nRequestID = self.api.ReqFromFutureToBankByFuture(<CReqTransferField *>address, nRequestID)
        # return nRequestID

    # def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount, int nRequestID):
        # cdef size_t address
        # if self.spi is NULL: return
        # address = ApiStruct_addressof(pReqQueryAccount)
        # with nogil: nRequestID = self.api.ReqQueryBankAccountMoneyByFuture(<CReqQueryAccountField *>address, nRequestID)
        # return nRequestID


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

# cdef extern int TraderSpi_OnRspParkedOrderInsert(self, CParkedOrderField *pParkedOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspParkedOrderInsert(None if pParkedOrder is NULL else ApiStruct_ParkedOrder(<size_t>pParkedOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspParkedOrderAction(self, CParkedOrderActionField *pParkedOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspParkedOrderAction(None if pParkedOrderAction is NULL else ApiStruct_ParkedOrderAction(<size_t>pParkedOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

cdef extern int TraderSpi_OnRspOrderAction(self, CInputOrderActionField *pInputOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspOrderAction(None if pInputOrderAction is NULL else ApiStruct_InputOrderAction(<size_t>pInputOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQueryMaxOrderVolume(self, CQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQueryMaxOrderVolume(None if pQueryMaxOrderVolume is NULL else ApiStruct_QueryMaxOrderVolume(<size_t>pQueryMaxOrderVolume), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

# cdef extern int TraderSpi_OnRspSettlementInfoConfirm(self, CSettlementInfoConfirmField *pSettlementInfoConfirm, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspSettlementInfoConfirm(None if pSettlementInfoConfirm is NULL else ApiStruct_SettlementInfoConfirm(<size_t>pSettlementInfoConfirm), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspRemoveParkedOrder(self, CRemoveParkedOrderField *pRemoveParkedOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspRemoveParkedOrder(None if pRemoveParkedOrder is NULL else ApiStruct_RemoveParkedOrder(<size_t>pRemoveParkedOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspRemoveParkedOrderAction(self, CRemoveParkedOrderActionField *pRemoveParkedOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspRemoveParkedOrderAction(None if pRemoveParkedOrderAction is NULL else ApiStruct_RemoveParkedOrderAction(<size_t>pRemoveParkedOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

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

# cdef extern int TraderSpi_OnRspQryInstrumentMarginRate(self, CInstrumentMarginRateField *pInstrumentMarginRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryInstrumentMarginRate(None if pInstrumentMarginRate is NULL else ApiStruct_InstrumentMarginRate(<size_t>pInstrumentMarginRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

cdef extern int TraderSpi_OnRspQryInstrumentCommissionRate(self, CInstrumentCommissionRateField *pInstrumentCommissionRate, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInstrumentCommissionRate(None if pInstrumentCommissionRate is NULL else ApiStruct_InstrumentCommissionRate(<size_t>pInstrumentCommissionRate), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchange(self, CExchangeField *pExchange, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryExchange(None if pExchange is NULL else ApiStruct_Exchange(<size_t>pExchange), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrument(self, CInstrumentField *pInstrument, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInstrument(None if pInstrument is NULL else ApiStruct_Instrument(<size_t>pInstrument), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryDepthMarketData(self, CDepthMarketDataField *pDepthMarketData, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryDepthMarketData(None if pDepthMarketData is NULL else ApiStruct_DepthMarketData(<size_t>pDepthMarketData), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

# cdef extern int TraderSpi_OnRspQrySettlementInfo(self, CSettlementInfoField *pSettlementInfo, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQrySettlementInfo(None if pSettlementInfo is NULL else ApiStruct_SettlementInfo(<size_t>pSettlementInfo), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryTransferBank(self, CTransferBankField *pTransferBank, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryTransferBank(None if pTransferBank is NULL else ApiStruct_TransferBank(<size_t>pTransferBank), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

cdef extern int TraderSpi_OnRspQryInvestorPositionDetail(self, CInvestorPositionDetailField *pInvestorPositionDetail, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInvestorPositionDetail(None if pInvestorPositionDetail is NULL else ApiStruct_InvestorPositionDetail(<size_t>pInvestorPositionDetail), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

# cdef extern int TraderSpi_OnRspQryNotice(self, CNoticeField *pNotice, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryNotice(None if pNotice is NULL else ApiStruct_Notice(<size_t>pNotice), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQrySettlementInfoConfirm(self, CSettlementInfoConfirmField *pSettlementInfoConfirm, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQrySettlementInfoConfirm(None if pSettlementInfoConfirm is NULL else ApiStruct_SettlementInfoConfirm(<size_t>pSettlementInfoConfirm), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryInvestorPositionCombineDetail(self, CInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryInvestorPositionCombineDetail(None if pInvestorPositionCombineDetail is NULL else ApiStruct_InvestorPositionCombineDetail(<size_t>pInvestorPositionCombineDetail), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryCFMMCTradingAccountKey(self, CCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryCFMMCTradingAccountKey(None if pCFMMCTradingAccountKey is NULL else ApiStruct_CFMMCTradingAccountKey(<size_t>pCFMMCTradingAccountKey), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryEWarrantOffset(self, CEWarrantOffsetField *pEWarrantOffset, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryEWarrantOffset(None if pEWarrantOffset is NULL else ApiStruct_EWarrantOffset(<size_t>pEWarrantOffset), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryTransferSerial(self, CTransferSerialField *pTransferSerial, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryTransferSerial(None if pTransferSerial is NULL else ApiStruct_TransferSerial(<size_t>pTransferSerial), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryAccountregister(self, CAccountregisterField *pAccountregister, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryAccountregister(None if pAccountregister is NULL else ApiStruct_Accountregister(<size_t>pAccountregister), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

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

# cdef extern int TraderSpi_OnRtnTradingNotice(self, CTradingNoticeInfoField *pTradingNoticeInfo) except -1:
    # self.OnRtnTradingNotice(None if pTradingNoticeInfo is NULL else ApiStruct_TradingNoticeInfo(<size_t>pTradingNoticeInfo))
    # return 0

# cdef extern int TraderSpi_OnRtnErrorConditionalOrder(self, CErrorConditionalOrderField *pErrorConditionalOrder) except -1:
    # self.OnRtnErrorConditionalOrder(None if pErrorConditionalOrder is NULL else ApiStruct_ErrorConditionalOrder(<size_t>pErrorConditionalOrder))
    # return 0

# cdef extern int TraderSpi_OnRspQryContractBank(self, CContractBankField *pContractBank, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryContractBank(None if pContractBank is NULL else ApiStruct_ContractBank(<size_t>pContractBank), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryParkedOrder(self, CParkedOrderField *pParkedOrder, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryParkedOrder(None if pParkedOrder is NULL else ApiStruct_ParkedOrder(<size_t>pParkedOrder), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryParkedOrderAction(self, CParkedOrderActionField *pParkedOrderAction, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryParkedOrderAction(None if pParkedOrderAction is NULL else ApiStruct_ParkedOrderAction(<size_t>pParkedOrderAction), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryTradingNotice(self, CTradingNoticeField *pTradingNotice, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryTradingNotice(None if pTradingNotice is NULL else ApiStruct_TradingNotice(<size_t>pTradingNotice), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryBrokerTradingParams(self, CBrokerTradingParamsField *pBrokerTradingParams, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryBrokerTradingParams(None if pBrokerTradingParams is NULL else ApiStruct_BrokerTradingParams(<size_t>pBrokerTradingParams), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQryBrokerTradingAlgos(self, CBrokerTradingAlgosField *pBrokerTradingAlgos, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQryBrokerTradingAlgos(None if pBrokerTradingAlgos is NULL else ApiStruct_BrokerTradingAlgos(<size_t>pBrokerTradingAlgos), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRtnFromBankToFutureByBank(self, CRspTransferField *pRspTransfer) except -1:
    # self.OnRtnFromBankToFutureByBank(None if pRspTransfer is NULL else ApiStruct_RspTransfer(<size_t>pRspTransfer))
    # return 0

# cdef extern int TraderSpi_OnRtnFromFutureToBankByBank(self, CRspTransferField *pRspTransfer) except -1:
    # self.OnRtnFromFutureToBankByBank(None if pRspTransfer is NULL else ApiStruct_RspTransfer(<size_t>pRspTransfer))
    # return 0

# cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByBank(self, CRspRepealField *pRspRepeal) except -1:
    # self.OnRtnRepealFromBankToFutureByBank(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    # return 0

# cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByBank(self, CRspRepealField *pRspRepeal) except -1:
    # self.OnRtnRepealFromFutureToBankByBank(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    # return 0

# cdef extern int TraderSpi_OnRtnFromBankToFutureByFuture(self, CRspTransferField *pRspTransfer) except -1:
    # self.OnRtnFromBankToFutureByFuture(None if pRspTransfer is NULL else ApiStruct_RspTransfer(<size_t>pRspTransfer))
    # return 0

# cdef extern int TraderSpi_OnRtnFromFutureToBankByFuture(self, CRspTransferField *pRspTransfer) except -1:
    # self.OnRtnFromFutureToBankByFuture(None if pRspTransfer is NULL else ApiStruct_RspTransfer(<size_t>pRspTransfer))
    # return 0

# cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(self, CRspRepealField *pRspRepeal) except -1:
    # self.OnRtnRepealFromBankToFutureByFutureManual(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    # return 0

# cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(self, CRspRepealField *pRspRepeal) except -1:
    # self.OnRtnRepealFromFutureToBankByFutureManual(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    # return 0

# cdef extern int TraderSpi_OnRtnQueryBankBalanceByFuture(self, CNotifyQueryAccountField *pNotifyQueryAccount) except -1:
    # self.OnRtnQueryBankBalanceByFuture(None if pNotifyQueryAccount is NULL else ApiStruct_NotifyQueryAccount(<size_t>pNotifyQueryAccount))
    # return 0

# cdef extern int TraderSpi_OnErrRtnBankToFutureByFuture(self, CReqTransferField *pReqTransfer, CRspInfoField *pRspInfo) except -1:
    # self.OnErrRtnBankToFutureByFuture(None if pReqTransfer is NULL else ApiStruct_ReqTransfer(<size_t>pReqTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    # return 0

# cdef extern int TraderSpi_OnErrRtnFutureToBankByFuture(self, CReqTransferField *pReqTransfer, CRspInfoField *pRspInfo) except -1:
    # self.OnErrRtnFutureToBankByFuture(None if pReqTransfer is NULL else ApiStruct_ReqTransfer(<size_t>pReqTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    # return 0

# cdef extern int TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(self, CReqRepealField *pReqRepeal, CRspInfoField *pRspInfo) except -1:
    # self.OnErrRtnRepealBankToFutureByFutureManual(None if pReqRepeal is NULL else ApiStruct_ReqRepeal(<size_t>pReqRepeal), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    # return 0

# cdef extern int TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(self, CReqRepealField *pReqRepeal, CRspInfoField *pRspInfo) except -1:
    # self.OnErrRtnRepealFutureToBankByFutureManual(None if pReqRepeal is NULL else ApiStruct_ReqRepeal(<size_t>pReqRepeal), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    # return 0

# cdef extern int TraderSpi_OnErrRtnQueryBankBalanceByFuture(self, CReqQueryAccountField *pReqQueryAccount, CRspInfoField *pRspInfo) except -1:
    # self.OnErrRtnQueryBankBalanceByFuture(None if pReqQueryAccount is NULL else ApiStruct_ReqQueryAccount(<size_t>pReqQueryAccount), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo))
    # return 0

# cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByFuture(self, CRspRepealField *pRspRepeal) except -1:
    # self.OnRtnRepealFromBankToFutureByFuture(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    # return 0

# cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByFuture(self, CRspRepealField *pRspRepeal) except -1:
    # self.OnRtnRepealFromFutureToBankByFuture(None if pRspRepeal is NULL else ApiStruct_RspRepeal(<size_t>pRspRepeal))
    # return 0

# cdef extern int TraderSpi_OnRspFromBankToFutureByFuture(self, CReqTransferField *pReqTransfer, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspFromBankToFutureByFuture(None if pReqTransfer is NULL else ApiStruct_ReqTransfer(<size_t>pReqTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspFromFutureToBankByFuture(self, CReqTransferField *pReqTransfer, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspFromFutureToBankByFuture(None if pReqTransfer is NULL else ApiStruct_ReqTransfer(<size_t>pReqTransfer), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRspQueryBankAccountMoneyByFuture(self, CReqQueryAccountField *pReqQueryAccount, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    # self.OnRspQueryBankAccountMoneyByFuture(None if pReqQueryAccount is NULL else ApiStruct_ReqQueryAccount(<size_t>pReqQueryAccount), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    # return 0

# cdef extern int TraderSpi_OnRtnOpenAccountByBank(self, COpenAccountField *pOpenAccount) except -1:
    # self.OnRtnOpenAccountByBank(None if pOpenAccount is NULL else ApiStruct_OpenAccount(<size_t>pOpenAccount))
    # return 0

# cdef extern int TraderSpi_OnRtnCancelAccountByBank(self, CCancelAccountField *pCancelAccount) except -1:
    # self.OnRtnCancelAccountByBank(None if pCancelAccount is NULL else ApiStruct_CancelAccount(<size_t>pCancelAccount))
    # return 0

# cdef extern int TraderSpi_OnRtnChangeAccountByBank(self, CChangeAccountField *pChangeAccount) except -1:
    # self.OnRtnChangeAccountByBank(None if pChangeAccount is NULL else ApiStruct_ChangeAccount(<size_t>pChangeAccount))
    # return 0
