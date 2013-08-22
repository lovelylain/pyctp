#ifndef CTRADERAPI_H
#define CTRADERAPI_H

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcTraderApiSSE.h"

static inline int TraderSpi_OnFrontConnected(PyObject *);
static inline int TraderSpi_OnFrontDisconnected(PyObject *, int);
static inline int TraderSpi_OnHeartBeatWarning(PyObject *, int);
static inline int TraderSpi_OnRspAuthenticate(PyObject *, CZQThostFtdcRspAuthenticateField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserLogin(PyObject *, CZQThostFtdcRspUserLoginField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserLogout(PyObject *, CZQThostFtdcUserLogoutField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserPasswordUpdate(PyObject *, CZQThostFtdcUserPasswordUpdateField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspTradingAccountPasswordUpdate(PyObject *, CZQThostFtdcTradingAccountPasswordUpdateField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOrderInsert(PyObject *, CZQThostFtdcInputOrderField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOrderAction(PyObject *, CZQThostFtdcInputOrderActionField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQueryMaxOrderVolume(PyObject *, CZQThostFtdcQueryMaxOrderVolumeField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryOrder(PyObject *, CZQThostFtdcOrderField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTrade(PyObject *, CZQThostFtdcTradeField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPosition(PyObject *, CZQThostFtdcInvestorPositionField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingAccount(PyObject *, CZQThostFtdcTradingAccountField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestor(PyObject *, CZQThostFtdcInvestorField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingCode(PyObject *, CZQThostFtdcTradingCodeField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrumentCommissionRate(PyObject *, CZQThostFtdcInstrumentCommissionRateField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchange(PyObject *, CZQThostFtdcExchangeField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrument(PyObject *, CZQThostFtdcInstrumentField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryDepthMarketData(PyObject *, CZQThostFtdcDepthMarketDataField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPositionDetail(PyObject *, CZQThostFtdcInvestorPositionDetailField *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspError(PyObject *, CZQThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnOrder(PyObject *, CZQThostFtdcOrderField *);
static inline int TraderSpi_OnRtnTrade(PyObject *, CZQThostFtdcTradeField *);
static inline int TraderSpi_OnErrRtnOrderInsert(PyObject *, CZQThostFtdcInputOrderField *, CZQThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnOrderAction(PyObject *, CZQThostFtdcOrderActionField *, CZQThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnInstrumentStatus(PyObject *, CZQThostFtdcInstrumentStatusField *);

#define X_CALL(op) \
	do { \
		PyGILState_STATE gilstate = PyGILState_Ensure(); \
		tid = PyThread_get_thread_ident(); \
		if ((op) == -1) PyErr_Print(); \
		PyGILState_Release(gilstate); \
	} while (0)

class CTraderSpi : public CZQThostFtdcTraderSpi {
public:
	long tid;

	CTraderSpi(PyObject *obj):tid(0),self(obj) {}
	virtual ~CTraderSpi() {}

	virtual void OnFrontConnected() {
		X_CALL(TraderSpi_OnFrontConnected(self));
	}

	virtual void OnFrontDisconnected(int nReason) {
		X_CALL(TraderSpi_OnFrontDisconnected(self, nReason));
	}

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		X_CALL(TraderSpi_OnHeartBeatWarning(self, nTimeLapse));
	}

	virtual void OnRspAuthenticate(CZQThostFtdcRspAuthenticateField *pRspAuthenticate, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspAuthenticate(self, pRspAuthenticate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogin(CZQThostFtdcRspUserLoginField *pRspUserLogin, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogout(CZQThostFtdcUserLogoutField *pUserLogout, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserPasswordUpdate(CZQThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspTradingAccountPasswordUpdate(CZQThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspOrderInsert(CZQThostFtdcInputOrderField *pInputOrder, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspOrderAction(CZQThostFtdcInputOrderActionField *pInputOrderAction, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQueryMaxOrderVolume(CZQThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryOrder(CZQThostFtdcOrderField *pOrder, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTrade(CZQThostFtdcTradeField *pTrade, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestorPosition(CZQThostFtdcInvestorPositionField *pInvestorPosition, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTradingAccount(CZQThostFtdcTradingAccountField *pTradingAccount, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestor(CZQThostFtdcInvestorField *pInvestor, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTradingCode(CZQThostFtdcTradingCodeField *pTradingCode, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInstrumentCommissionRate(CZQThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryExchange(CZQThostFtdcExchangeField *pExchange, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInstrument(CZQThostFtdcInstrumentField *pInstrument, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryDepthMarketData(CZQThostFtdcDepthMarketDataField *pDepthMarketData, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestorPositionDetail(CZQThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspError(CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnOrder(CZQThostFtdcOrderField *pOrder) {
		X_CALL(TraderSpi_OnRtnOrder(self, pOrder));
	}

	virtual void OnRtnTrade(CZQThostFtdcTradeField *pTrade) {
		X_CALL(TraderSpi_OnRtnTrade(self, pTrade));
	}

	virtual void OnErrRtnOrderInsert(CZQThostFtdcInputOrderField *pInputOrder, CZQThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnOrderInsert(self, pInputOrder, pRspInfo));
	}

	virtual void OnErrRtnOrderAction(CZQThostFtdcOrderActionField *pOrderAction, CZQThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnOrderAction(self, pOrderAction, pRspInfo));
	}

	virtual void OnRtnInstrumentStatus(CZQThostFtdcInstrumentStatusField *pInstrumentStatus) {
		X_CALL(TraderSpi_OnRtnInstrumentStatus(self, pInstrumentStatus));
	}

private:
	PyObject *self;
};

static CZQThostFtdcTraderApi *g_GcApi = NULL;
static long g_GcTid = 0;

static inline void ReleaseTraderApi(CZQThostFtdcTraderApi *api, CTraderSpi *spi) {
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
#define S_Exchange "Exchange"
#define S_InputOrder "InputOrder"
#define S_InputOrderAction "InputOrderAction"
#define S_Instrument "Instrument"
#define S_InstrumentCommissionRate "InstrumentCommissionRate"
#define S_InstrumentStatus "InstrumentStatus"
#define S_Investor "Investor"
#define S_InvestorPosition "InvestorPosition"
#define S_InvestorPositionDetail "InvestorPositionDetail"
#define S_Order "Order"
#define S_OrderAction "OrderAction"
#define S_QueryMaxOrderVolume "QueryMaxOrderVolume"
#define S_RspAuthenticate "RspAuthenticate"
#define S_RspInfo "RspInfo"
#define S_RspUserLogin "RspUserLogin"
#define S_Trade "Trade"
#define S_TradingAccount "TradingAccount"
#define S_TradingAccountPasswordUpdate "TradingAccountPasswordUpdate"
#define S_TradingCode "TradingCode"
#define S_UserLogout "UserLogout"
#define S_UserPasswordUpdate "UserPasswordUpdate"

#endif /* CTRADERAPI_H */
