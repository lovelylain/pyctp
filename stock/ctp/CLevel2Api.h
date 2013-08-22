#ifndef CLEVEL2API_H
#define CLEVEL2API_H

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcLevel2UserApi.h"

_USING_LEVEL2_NS_
static inline int Level2Spi_OnFrontConnected(PyObject *);
static inline int Level2Spi_OnFrontDisconnected(PyObject *, int);
static inline int Level2Spi_OnHeartBeatWarning(PyObject *, int);
static inline int Level2Spi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int Level2Spi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int Level2Spi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int Level2Spi_OnRspSubLevel2MarketData(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline int Level2Spi_OnRspUnSubLevel2MarketData(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline int Level2Spi_OnRspSubNGTSIndex(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline int Level2Spi_OnRspUnSubNGTSIndex(PyObject *, CThostFtdcSpecificSecurityField *, CThostFtdcRspInfoField *, int, bool);
static inline int Level2Spi_OnRtnLevel2MarketData(PyObject *, CThostFtdcLevel2MarketDataField *);
static inline int Level2Spi_OnRtnNGTSIndex(PyObject *, CThostFtdcNGTSIndexField *);

#define X_CALL(op) \
	do { \
		PyGILState_STATE gilstate = PyGILState_Ensure(); \
		tid = PyThread_get_thread_ident(); \
		if ((op) == -1) PyErr_Print(); \
		PyGILState_Release(gilstate); \
	} while (0)

class CLevel2Spi : public CThostFtdcLevel2UserSpi {
public:
	long tid;

	CLevel2Spi(PyObject *obj):tid(0),self(obj) {}
	virtual ~CLevel2Spi() {}

	virtual void OnFrontConnected() {
		X_CALL(Level2Spi_OnFrontConnected(self));
	}

	virtual void OnFrontDisconnected(int nReason) {
		X_CALL(Level2Spi_OnFrontDisconnected(self, nReason));
	}

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		X_CALL(Level2Spi_OnHeartBeatWarning(self, nTimeLapse));
	}

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(Level2Spi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(Level2Spi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(Level2Spi_OnRspError(self, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSubLevel2MarketData(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(Level2Spi_OnRspSubLevel2MarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUnSubLevel2MarketData(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(Level2Spi_OnRspUnSubLevel2MarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSubNGTSIndex(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(Level2Spi_OnRspSubNGTSIndex(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUnSubNGTSIndex(CThostFtdcSpecificSecurityField *pSpecificSecurity, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(Level2Spi_OnRspUnSubNGTSIndex(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnLevel2MarketData(CThostFtdcLevel2MarketDataField *pLevel2MarketData) {
		X_CALL(Level2Spi_OnRtnLevel2MarketData(self, pLevel2MarketData));
	}

	virtual void OnRtnNGTSIndex(CThostFtdcNGTSIndexField *pNGTSIndex) {
		X_CALL(Level2Spi_OnRtnNGTSIndex(self, pNGTSIndex));
	}

private:
	PyObject *self;
};

static CThostFtdcLevel2UserApi *g_GcApi = NULL;
static long g_GcTid = 0;

static inline void ReleaseLevel2Api(CThostFtdcLevel2UserApi *api, CLevel2Spi *spi) {
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

static PyObject *_init(PyObject *, PyObject *);
static PyMethodDef _init_method = {"_init", _init, METH_O, NULL};

#define CheckMemory(p) (p || PyErr_NoMemory())
#if PY_MAJOR_VERSION < 3
#define XStr PyString_FromString
#define XFixSysModules()
#else
#define XStr PyUnicode_FromString
#define XFixSysModules() \
	do { \
		PyObject *n = PyDict_GetItemString(PyModule_GetDict(__pyx_m), "__name__"); \
		if (n) n = PyUnicode_AsEncodedString(n, "ascii", NULL); \
		if (n) { \
			const char *name = PyBytes_AS_STRING(n); \
			PyObject *m = PyImport_GetModuleDict(); \
			if (name && m) { \
				if (strcmp(name, __Pyx_MODULE_NAME) != 0 && \
					PyDict_GetItemString(m, __Pyx_MODULE_NAME) == __pyx_m) \
					PyDict_DelItemString(m, __Pyx_MODULE_NAME); \
				if (!PyDict_GetItemString(m, name)) \
					PyDict_SetItemString(m, name, __pyx_m); \
			} \
			Py_DECREF(n); \
		} \
	} while (0)
#endif

#define S___name__ "__name__"
#define S_ctypes "ctypes"
#define S_addressof "addressof"
#define S_from_address "from_address"
#define S_Level2MarketData "Level2MarketData"
#define S_NGTSIndex "NGTSIndex"
#define S_RspInfo "RspInfo"
#define S_RspUserLogin "RspUserLogin"
#define S_SpecificSecurity "SpecificSecurity"
#define S_UserLogout "UserLogout"

#endif /* CLEVEL2API_H */
