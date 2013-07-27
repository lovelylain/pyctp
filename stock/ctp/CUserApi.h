#ifndef CUSERAPI_H
#define CUSERAPI_H

#include <Python.h>
#include <pythread.h>
#include "ThostFtdcLevel2UserApi.h"

_USING_LEVEL2_NS_
static inline int UserSpi_OnFrontConnected(PyObject *);
static inline int UserSpi_OnFrontDisconnected(PyObject *, int);
static inline int UserSpi_OnHeartBeatWarning(PyObject *, int);
static inline int UserSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int UserSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int UserSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int UserSpi_OnRspSubLevel2MarketData(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline int UserSpi_OnRspUnSubLevel2MarketData(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline int UserSpi_OnRspSubNGTSIndex(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline int UserSpi_OnRspUnSubNGTSIndex(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline int UserSpi_OnRtnLevel2MarketData(PyObject *, CThostFtdcLevel2MarketDataField *);
static inline int UserSpi_OnRtnNGTSIndex(PyObject *, CThostFtdcNGTSIndexField *);

#define X_CALL(op) \
	do { \
		PyGILState_STATE gilstate = PyGILState_Ensure(); \
		tid = PyThread_get_thread_ident(); \
		if ((op) == -1) PyErr_Print(); \
		PyGILState_Release(gilstate); \
	} while (0)

class CUserSpi : public CThostFtdcLevel2UserSpi {
public:
	long tid;

	CUserSpi(PyObject *obj):tid(0),self(obj) {}
	virtual ~CUserSpi() {}

	virtual void OnFrontConnected() {
		X_CALL(UserSpi_OnFrontConnected(self));
	}

	virtual void OnFrontDisconnected(int nReason) {
		X_CALL(UserSpi_OnFrontDisconnected(self, nReason));
	}

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		X_CALL(UserSpi_OnHeartBeatWarning(self, nTimeLapse));
	}

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(UserSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(UserSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(UserSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSubLevel2MarketData(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(UserSpi_OnRspSubLevel2MarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUnSubLevel2MarketData(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(UserSpi_OnRspUnSubLevel2MarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSubNGTSIndex(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(UserSpi_OnRspSubNGTSIndex(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUnSubNGTSIndex(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(UserSpi_OnRspUnSubNGTSIndex(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnLevel2MarketData(CThostFtdcLevel2MarketDataField *pLevel2MarketData) {
		X_CALL(UserSpi_OnRtnLevel2MarketData(self, pLevel2MarketData));
	}

	virtual void OnRtnNGTSIndex(CThostFtdcNGTSIndexField *pNGTSIndex) {
		X_CALL(UserSpi_OnRtnNGTSIndex(self, pNGTSIndex));
	}

private:
	PyObject *self;
};

static CThostFtdcLevel2UserApi *g_GcApi = NULL;
static long g_GcTid = 0;

static inline void ReleaseUserApi(CThostFtdcLevel2UserApi *api, CUserSpi *spi) {
	long tid = PyThread_get_thread_ident();
	if (g_GcApi && g_GcTid != tid) {
		g_GcApi->Release();
		g_GcApi = NULL;
	}
	if (api) {
		api->RegisterSpi(NULL);
		if (!spi) {
#ifndef _WIN32
			api->Init(); usleep(100000);
#endif
			api->Release();
		} else {
			if (spi->tid != tid) {
				api->Release();
			} else {
				g_GcApi = api;
				g_GcTid = tid;
			}
			delete spi;
		}
	}
}

#define CheckMemory(p) (p || PyErr_NoMemory())
#if PY_MAJOR_VERSION < 3
#define XStr PyString_FromString
#else
#define XStr PyUnicode_FromString
#endif

#define S_dot "."
#define S_ApiStruct ".UserApiStruct"
#define S___name__ "__name__"
#define S_rpartition "rpartition"
#define S_ctypes "ctypes"
#define S_addressof "addressof"
#define S_from_address "from_address"
#define S_Level2MarketData "Level2MarketData"
#define S_NGTSIndex "NGTSIndex"
#define S_RspInfo "RspInfo"
#define S_RspUserLogin "RspUserLogin"
#define S_SpecificSecurity "SpecificSecurity"
#define S_UserLogout "UserLogout"

#endif /* CUSERAPI_H */
