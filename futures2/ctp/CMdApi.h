#ifndef CMDAPI_H
#define CMDAPI_H

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcMdApi.h"

static inline int MdSpi_OnFrontConnected(PyObject *);
static inline int MdSpi_OnFrontDisconnected(PyObject *, int);
static inline int MdSpi_OnHeartBeatWarning(PyObject *, int);
static inline int MdSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUnSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUnSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRtnDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *);
static inline int MdSpi_OnRtnForQuoteRsp(PyObject *, CThostFtdcForQuoteRspField *);

#define X_CALL(op) \
	do { \
		PyGILState_STATE gilstate = PyGILState_Ensure(); \
		tid = PyThread_get_thread_ident(); \
		if ((op) == -1) PyErr_Print(); \
		PyGILState_Release(gilstate); \
	} while (0)

class CMdSpi : public CThostFtdcMdSpi {
public:
	long tid;

	CMdSpi(PyObject *obj):tid(0),self(obj) {}
	virtual ~CMdSpi() {}

	virtual void OnFrontConnected() {
		X_CALL(MdSpi_OnFrontConnected(self));
	}

	virtual void OnFrontDisconnected(int nReason) {
		X_CALL(MdSpi_OnFrontDisconnected(self, nReason));
	}

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		X_CALL(MdSpi_OnHeartBeatWarning(self, nTimeLapse));
	}

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(MdSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(MdSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(MdSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(MdSpi_OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(MdSpi_OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(MdSpi_OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(MdSpi_OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
		X_CALL(MdSpi_OnRtnDepthMarketData(self, pDepthMarketData));
	}

	virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
		X_CALL(MdSpi_OnRtnForQuoteRsp(self, pForQuoteRsp));
	}

private:
	PyObject *self;
};

static CThostFtdcMdApi *g_GcApi = NULL;
static long g_GcTid = 0;

static inline void ReleaseMdApi(CThostFtdcMdApi *api, CMdSpi *spi) {
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
#define S_DepthMarketData "DepthMarketData"
#define S_ForQuoteRsp "ForQuoteRsp"
#define S_RspInfo "RspInfo"
#define S_RspUserLogin "RspUserLogin"
#define S_SpecificInstrument "SpecificInstrument"
#define S_UserLogout "UserLogout"

#endif /* CMDAPI_H */
