# -*- coding: utf-8 -*-

from cLevel2Api cimport *

cdef ApiStruct_addressof, ApiStruct_Level2MarketData, ApiStruct_NGTSIndex, ApiStruct_RspInfo, ApiStruct_RspUserLogin, ApiStruct_SpecificSecurity, ApiStruct_UserLogout
cdef extern _init(self, m):
    global ApiStruct_addressof, ApiStruct_Level2MarketData, ApiStruct_NGTSIndex, ApiStruct_RspInfo, ApiStruct_RspUserLogin, ApiStruct_SpecificSecurity, ApiStruct_UserLogout
    ApiStruct_addressof = XGetAttr(PyImport_ImportModule(S_ctypes), S_addressof)
    fa = XStr(S_from_address)
    ApiStruct_Level2MarketData = XGotAttr(XGetAttr(m, S_Level2MarketData), fa)
    ApiStruct_NGTSIndex = XGotAttr(XGetAttr(m, S_NGTSIndex), fa)
    ApiStruct_RspInfo = XGotAttr(XGetAttr(m, S_RspInfo), fa)
    ApiStruct_RspUserLogin = XGotAttr(XGetAttr(m, S_RspUserLogin), fa)
    ApiStruct_SpecificSecurity = XGotAttr(XGetAttr(m, S_SpecificSecurity), fa)
    ApiStruct_UserLogout = XGotAttr(XGetAttr(m, S_UserLogout), fa)
XFixSysModules()
CSetAttr(Xmod, _init_method.ml_name, PyCFunction_NewEx(&_init_method, NULL, XCGetAttr(Xmod, S___name__)))


cdef void Level2Api_Release(Level2Api self):
    ReleaseLevel2Api(self.api, self.spi)
    self.api = self.spi = NULL

cdef class Level2Api:
    cdef CLevel2Api *api
    cdef CLevel2Spi *spi

    def __dealloc__(self):
        Level2Api_Release(self)

    def Alive(self):
        if self.spi is not NULL: return self.spi.tid
        if self.api is not NULL: return False

    def Create(self, const_char *pszFlowPath="", cbool bIsUsingUdp=False, cbool bIsMulticast=False):
        if self.api is not NULL: return
        self.api = CreateFtdcLevel2UserApi(pszFlowPath, bIsUsingUdp)
        CheckMemory(self.api)

    def Release(self):
        Level2Api_Release(self)

    def Init(self):
        if self.api is NULL or self.spi is not NULL: return
        self.spi = new CLevel2Spi(<PyObject *>self)
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

    def SubscribePublicTopic(self, TE_RESUME_TYPE nResumeType):
        if self.api is NULL: return
        self.api.SubscribePublicTopic(nResumeType)

    def SubscribeLevel2MarketData(self, pSecurityList, int nCount):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pSecurityList)
        with nogil: nCount = self.api.SubscribeLevel2MarketData(<CSpecificSecurityField *>address, nCount)
        return nCount

    def UnSubscribeLevel2MarketData(self, pSecurityList, int nCount):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pSecurityList)
        with nogil: nCount = self.api.UnSubscribeLevel2MarketData(<CSpecificSecurityField *>address, nCount)
        return nCount

    def SubscribeNGTSIndex(self, pSecurityList, int nCount):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pSecurityList)
        with nogil: nCount = self.api.SubscribeNGTSIndex(<CSpecificSecurityField *>address, nCount)
        return nCount

    def UnSubscribeNGTSIndex(self, pSecurityList, int nCount):
        cdef size_t address
        if self.spi is NULL: return
        address = ApiStruct_addressof(pSecurityList)
        with nogil: nCount = self.api.UnSubscribeNGTSIndex(<CSpecificSecurityField *>address, nCount)
        return nCount

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


cdef extern int Level2Spi_OnFrontConnected(self) except -1:
    self.OnFrontConnected()
    return 0

cdef extern int Level2Spi_OnFrontDisconnected(self, int nReason) except -1:
    self.OnFrontDisconnected(nReason)
    return 0

cdef extern int Level2Spi_OnHeartBeatWarning(self, int nTimeLapse) except -1:
    self.OnHeartBeatWarning(nTimeLapse)
    return 0

cdef extern int Level2Spi_OnRspUserLogin(self, CRspUserLoginField *pRspUserLogin, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogin(None if pRspUserLogin is NULL else ApiStruct_RspUserLogin(<size_t>pRspUserLogin), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int Level2Spi_OnRspUserLogout(self, CUserLogoutField *pUserLogout, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogout(None if pUserLogout is NULL else ApiStruct_UserLogout(<size_t>pUserLogout), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int Level2Spi_OnRspError(self, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspError(None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int Level2Spi_OnRspSubLevel2MarketData(self, CSpecificSecurityField *pSpecificSecurity, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspSubLevel2MarketData(None if pSpecificSecurity is NULL else ApiStruct_SpecificSecurity(<size_t>pSpecificSecurity), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int Level2Spi_OnRspUnSubLevel2MarketData(self, CSpecificSecurityField *pSpecificSecurity, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUnSubLevel2MarketData(None if pSpecificSecurity is NULL else ApiStruct_SpecificSecurity(<size_t>pSpecificSecurity), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int Level2Spi_OnRspSubNGTSIndex(self, CSpecificSecurityField *pSpecificSecurity, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspSubNGTSIndex(None if pSpecificSecurity is NULL else ApiStruct_SpecificSecurity(<size_t>pSpecificSecurity), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int Level2Spi_OnRspUnSubNGTSIndex(self, CSpecificSecurityField *pSpecificSecurity, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUnSubNGTSIndex(None if pSpecificSecurity is NULL else ApiStruct_SpecificSecurity(<size_t>pSpecificSecurity), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int Level2Spi_OnRtnLevel2MarketData(self, CLevel2MarketDataField *pLevel2MarketData) except -1:
    self.OnRtnLevel2MarketData(None if pLevel2MarketData is NULL else ApiStruct_Level2MarketData(<size_t>pLevel2MarketData))
    return 0

cdef extern int Level2Spi_OnRtnNGTSIndex(self, CNGTSIndexField *pNGTSIndex) except -1:
    self.OnRtnNGTSIndex(None if pNGTSIndex is NULL else ApiStruct_NGTSIndex(<size_t>pNGTSIndex))
    return 0
