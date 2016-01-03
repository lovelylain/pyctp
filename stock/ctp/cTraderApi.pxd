# -*- coding: utf-8 -*-

from cUserApiStruct cimport *
from libcpp cimport bool as cbool
from libc.string cimport const_char

cdef extern from "Python.h":
    ctypedef struct PyObject
    ctypedef struct PyMethodDef:
        const_char *ml_name
    object PyImport_ImportModule(const_char *name)
    object PyCFunction_NewEx(PyMethodDef *ml, PyObject *self, object module)
    object XGotAttr "PyObject_GetAttr"(object o, object attr_name)
    object XGetAttr "PyObject_GetAttrString"(object o, const_char *attr_name)
    object XCGetAttr "PyObject_GetAttrString"(PyObject *o, const_char *attr_name)
    int CSetAttr "PyObject_SetAttrString"(PyObject *o, const_char *attr_name, object v) except -1

cdef extern from "ThostFtdcTraderApiSSE.h":
    cdef cppclass CTraderApi "CZQThostFtdcTraderApi":
        void Release() nogil
        void Init() nogil
        int Join() nogil
        const_char *GetTradingDay() nogil
        void RegisterFront(char *pszFrontAddress) nogil
        void RegisterSpi(CTraderSpi *pSpi) nogil
        void SubscribePrivateTopic(TE_RESUME_TYPE nResumeType) nogil
        void SubscribePublicTopic(TE_RESUME_TYPE nResumeType) nogil
        int ReqAuthenticate(CReqAuthenticateField *pReqAuthenticate, int nRequestID) nogil
        int ReqUserLogin(CReqUserLoginField *pReqUserLogin, int nRequestID) nogil
        int ReqUserLogout(CUserLogoutField *pUserLogout, int nRequestID) nogil
        int ReqUserPasswordUpdate(CUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) nogil
        int ReqTradingAccountPasswordUpdate(CTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID) nogil
        int ReqOrderInsert(CInputOrderField *pInputOrder, int nRequestID) nogil
        int ReqOrderAction(CInputOrderActionField *pInputOrderAction, int nRequestID) nogil
        int ReqQueryMaxOrderVolume(CQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID) nogil
        int ReqQryOrder(CQryOrderField *pQryOrder, int nRequestID) nogil
        int ReqQryTrade(CQryTradeField *pQryTrade, int nRequestID) nogil
        int ReqQryInvestorPosition(CQryInvestorPositionField *pQryInvestorPosition, int nRequestID) nogil
        int ReqQryTradingAccount(CQryTradingAccountField *pQryTradingAccount, int nRequestID) nogil
        int ReqQryInvestor(CQryInvestorField *pQryInvestor, int nRequestID) nogil
        int ReqQryTradingCode(CQryTradingCodeField *pQryTradingCode, int nRequestID) nogil
        int ReqQryInstrumentCommissionRate(CQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID) nogil
        int ReqQryExchange(CQryExchangeField *pQryExchange, int nRequestID) nogil
        int ReqQryInstrument(CQryInstrumentField *pQryInstrument, int nRequestID) nogil
        int ReqQryDepthMarketData(CQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) nogil
        int ReqQryInvestorPositionDetail(CQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID) nogil

cdef extern from "ThostFtdcTraderApiSSE.h" namespace "CZQThostFtdcTraderApi":
    CTraderApi *CreateFtdcTraderApi(const_char *pszFlowPath, cbool bIsUsingUdp) nogil except +

cdef extern from "CTraderApi.h":
    cdef cppclass CTraderSpi:
        CTraderSpi(PyObject *obj)
        long tid
    void ReleaseTraderApi(CTraderApi *api, CTraderSpi *spi)
    cdef PyObject *Xmod "__pyx_m"
    cdef PyMethodDef _init_method
    int CheckMemory(void *) except 0
    void XFixSysModules()
    object XStr(const_char *v)
    cdef const_char *S___name__, *S_ctypes, *S_addressof, *S_from_address, *S_DepthMarketData, *S_Exchange, *S_InputOrder, *S_InputOrderAction, *S_Instrument, *S_InstrumentCommissionRate, *S_InstrumentStatus, *S_Investor, *S_InvestorPosition, *S_InvestorPositionDetail, *S_Order, *S_OrderAction, *S_QueryMaxOrderVolume, *S_RspAuthenticate, *S_RspInfo, *S_RspUserLogin, *S_Trade, *S_TradingAccount, *S_TradingAccountPasswordUpdate, *S_TradingCode, *S_UserLogout, *S_UserPasswordUpdate
