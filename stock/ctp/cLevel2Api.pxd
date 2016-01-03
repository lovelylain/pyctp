# -*- coding: utf-8 -*-

from cLevel2ApiStruct cimport *
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

cdef extern from "ThostFtdcLevel2UserApi.h":
    cdef cppclass CLevel2Api "CThostFtdcLevel2UserApi":
        void Release() nogil
        void Init() nogil
        int Join() nogil
        const_char *GetTradingDay() nogil
        void RegisterFront(char *pszFrontAddress) nogil
        void RegisterSpi(CLevel2Spi *pSpi) nogil
        int SubscribeLevel2MarketData(CSpecificSecurityField *pSecurityList, int nCount) nogil
        int UnSubscribeLevel2MarketData(CSpecificSecurityField *pSecurityList, int nCount) nogil
        int SubscribeNGTSIndex(CSpecificSecurityField *pSecurityList, int nCount) nogil
        int UnSubscribeNGTSIndex(CSpecificSecurityField *pSecurityList, int nCount) nogil
        void SubscribePublicTopic(TE_RESUME_TYPE nResumeType) nogil
        int ReqUserLogin(CReqUserLoginField *pReqUserLogin, int nRequestID) nogil
        int ReqUserLogout(CUserLogoutField *pUserLogout, int nRequestID) nogil

cdef extern from "ThostFtdcLevel2UserApi.h" namespace "CThostFtdcLevel2UserApi":
    CLevel2Api *CreateFtdcLevel2UserApi(const_char *pszFlowPath, cbool bIsUsingUdp) nogil except +

cdef extern from "CLevel2Api.h":
    cdef cppclass CLevel2Spi:
        CLevel2Spi(PyObject *obj)
        long tid
    void ReleaseLevel2Api(CLevel2Api *api, CLevel2Spi *spi)
    cdef PyObject *Xmod "__pyx_m"
    cdef PyMethodDef _init_method
    int CheckMemory(void *) except 0
    void XFixSysModules()
    object XStr(const_char *v)
    cdef const_char *S___name__, *S_ctypes, *S_addressof, *S_from_address, *S_Level2MarketData, *S_NGTSIndex, *S_RspInfo, *S_RspUserLogin, *S_SpecificSecurity, *S_UserLogout
