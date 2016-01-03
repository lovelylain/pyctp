# -*- coding: utf-8 -*-

from cMdApi cimport *
from libc cimport stdlib

cdef ApiStruct_addressof, ApiStruct_DepthMarketData, ApiStruct_ForQuoteRsp, ApiStruct_RspInfo, ApiStruct_RspUserLogin, ApiStruct_SpecificInstrument, ApiStruct_UserLogout
cdef extern _init(self, m):
    global ApiStruct_addressof, ApiStruct_DepthMarketData, ApiStruct_ForQuoteRsp, ApiStruct_RspInfo, ApiStruct_RspUserLogin, ApiStruct_SpecificInstrument, ApiStruct_UserLogout
    ApiStruct_addressof = XGetAttr(PyImport_ImportModule(S_ctypes), S_addressof)
    fa = XStr(S_from_address)
    ApiStruct_DepthMarketData = XGotAttr(XGetAttr(m, S_DepthMarketData), fa)
    ApiStruct_ForQuoteRsp = XGotAttr(XGetAttr(m, S_ForQuoteRsp), fa)
    ApiStruct_RspInfo = XGotAttr(XGetAttr(m, S_RspInfo), fa)
    ApiStruct_RspUserLogin = XGotAttr(XGetAttr(m, S_RspUserLogin), fa)
    ApiStruct_SpecificInstrument = XGotAttr(XGetAttr(m, S_SpecificInstrument), fa)
    ApiStruct_UserLogout = XGotAttr(XGetAttr(m, S_UserLogout), fa)
XFixSysModules()
CSetAttr(Xmod, _init_method.ml_name, PyCFunction_NewEx(&_init_method, NULL, XCGetAttr(Xmod, S___name__)))


cdef void MdApi_Release(MdApi self):
    ReleaseMdApi(self.api, self.spi)
    self.api = self.spi = NULL

cdef class MdApi:
    cdef CMdApi *api
    cdef CMdSpi *spi

    def __dealloc__(self):
        MdApi_Release(self)

    def Alive(self):
        if self.spi is not NULL: return self.spi.tid
        if self.api is not NULL: return False

    def Create(self, const_char *pszFlowPath="", cbool bIsUsingUdp=False, cbool bIsMulticast=False):
        if self.api is not NULL: return
        self.api = CreateFtdcMdApi(pszFlowPath, bIsUsingUdp, bIsMulticast)
        CheckMemory(self.api)

    def GetApiVersion(self):
        return GetApiVersion()

    def Release(self):
        MdApi_Release(self)

    def Init(self):
        if self.api is NULL or self.spi is not NULL: return
        self.spi = new CMdSpi(<PyObject *>self)
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

    def SubscribeMarketData(self, pInstrumentIDs):
        cdef int nCount
        cdef char **ppInstrumentID
        if self.spi is NULL: return
        nCount = len(pInstrumentIDs)
        ppInstrumentID = <char **>stdlib.malloc(sizeof(char *) * nCount)
        CheckMemory(ppInstrumentID)
        try:
            for i from 0 <= i < nCount:
                ppInstrumentID[i] = pInstrumentIDs[i]
            with nogil: nCount = self.api.SubscribeMarketData(ppInstrumentID, nCount)
        finally:
            stdlib.free(ppInstrumentID)
        return nCount

    def UnSubscribeMarketData(self, pInstrumentIDs):
        cdef int nCount
        cdef char **ppInstrumentID
        if self.spi is NULL: return
        nCount = len(pInstrumentIDs)
        ppInstrumentID = <char **>stdlib.malloc(sizeof(char *) * nCount)
        CheckMemory(ppInstrumentID)
        try:
            for i from 0 <= i < nCount:
                ppInstrumentID[i] = pInstrumentIDs[i]
            with nogil: nCount = self.api.UnSubscribeMarketData(ppInstrumentID, nCount)
        finally:
            stdlib.free(ppInstrumentID)
        return nCount

    def SubscribeForQuoteRsp(self, pInstrumentIDs):
        cdef int nCount
        cdef char **ppInstrumentID
        if self.spi is NULL: return
        nCount = len(pInstrumentIDs)
        ppInstrumentID = <char **>stdlib.malloc(sizeof(char *) * nCount)
        CheckMemory(ppInstrumentID)
        try:
            for i from 0 <= i < nCount:
                ppInstrumentID[i] = pInstrumentIDs[i]
            with nogil: nCount = self.api.SubscribeForQuoteRsp(ppInstrumentID, nCount)
        finally:
            stdlib.free(ppInstrumentID)
        return nCount

    def UnSubscribeForQuoteRsp(self, pInstrumentIDs):
        cdef int nCount
        cdef char **ppInstrumentID
        if self.spi is NULL: return
        nCount = len(pInstrumentIDs)
        ppInstrumentID = <char **>stdlib.malloc(sizeof(char *) * nCount)
        CheckMemory(ppInstrumentID)
        try:
            for i from 0 <= i < nCount:
                ppInstrumentID[i] = pInstrumentIDs[i]
            with nogil: nCount = self.api.UnSubscribeForQuoteRsp(ppInstrumentID, nCount)
        finally:
            stdlib.free(ppInstrumentID)
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


cdef extern int MdSpi_OnFrontConnected(self) except -1:
    self.OnFrontConnected()
    return 0

cdef extern int MdSpi_OnFrontDisconnected(self, int nReason) except -1:
    self.OnFrontDisconnected(nReason)
    return 0

cdef extern int MdSpi_OnHeartBeatWarning(self, int nTimeLapse) except -1:
    self.OnHeartBeatWarning(nTimeLapse)
    return 0

cdef extern int MdSpi_OnRspUserLogin(self, CRspUserLoginField *pRspUserLogin, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogin(None if pRspUserLogin is NULL else ApiStruct_RspUserLogin(<size_t>pRspUserLogin), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspUserLogout(self, CUserLogoutField *pUserLogout, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogout(None if pUserLogout is NULL else ApiStruct_UserLogout(<size_t>pUserLogout), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspError(self, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspError(None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspSubMarketData(self, CSpecificInstrumentField *pSpecificInstrument, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspSubMarketData(None if pSpecificInstrument is NULL else ApiStruct_SpecificInstrument(<size_t>pSpecificInstrument), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspUnSubMarketData(self, CSpecificInstrumentField *pSpecificInstrument, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUnSubMarketData(None if pSpecificInstrument is NULL else ApiStruct_SpecificInstrument(<size_t>pSpecificInstrument), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspSubForQuoteRsp(self, CSpecificInstrumentField *pSpecificInstrument, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspSubForQuoteRsp(None if pSpecificInstrument is NULL else ApiStruct_SpecificInstrument(<size_t>pSpecificInstrument), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspUnSubForQuoteRsp(self, CSpecificInstrumentField *pSpecificInstrument, CRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspUnSubForQuoteRsp(None if pSpecificInstrument is NULL else ApiStruct_SpecificInstrument(<size_t>pSpecificInstrument), None if pRspInfo is NULL else ApiStruct_RspInfo(<size_t>pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRtnDepthMarketData(self, CDepthMarketDataField *pDepthMarketData) except -1:
    self.OnRtnDepthMarketData(None if pDepthMarketData is NULL else ApiStruct_DepthMarketData(<size_t>pDepthMarketData))
    return 0

cdef extern int MdSpi_OnRtnForQuoteRsp(self, CForQuoteRspField *pForQuoteRsp) except -1:
    self.OnRtnForQuoteRsp(None if pForQuoteRsp is NULL else ApiStruct_ForQuoteRsp(<size_t>pForQuoteRsp))
    return 0
