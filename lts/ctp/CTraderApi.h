#ifndef CTRADERAPI_H
#define CTRADERAPI_H

#include "Python.h"
#include "pythread.h"
#include "SecurityFtdcTraderApi.h"

static inline int TraderSpi_OnFrontConnected(PyObject *);
static inline int TraderSpi_OnFrontDisconnected(PyObject *, int);
static inline int TraderSpi_OnHeartBeatWarning(PyObject *, int);
static inline int TraderSpi_OnRspError(PyObject *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserLogin(PyObject *, CSecurityFtdcRspUserLoginField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserLogout(PyObject *, CSecurityFtdcUserLogoutField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOrderInsert(PyObject *, CSecurityFtdcInputOrderField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOrderAction(PyObject *, CSecurityFtdcInputOrderActionField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserPasswordUpdate(PyObject *, CSecurityFtdcUserPasswordUpdateField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspTradingAccountPasswordUpdate(PyObject *, CSecurityFtdcTradingAccountPasswordUpdateField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchange(PyObject *, CSecurityFtdcExchangeField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrument(PyObject *, CSecurityFtdcInstrumentField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestor(PyObject *, CSecurityFtdcInvestorField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingCode(PyObject *, CSecurityFtdcTradingCodeField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingAccount(PyObject *, CSecurityFtdcTradingAccountField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryDepthMarketData(PyObject *, CSecurityFtdcDepthMarketDataField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryBondInterest(PyObject *, CSecurityFtdcBondInterestField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryMarketRationInfo(PyObject *, CSecurityFtdcMarketRationInfoField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrumentCommissionRate(PyObject *, CSecurityFtdcInstrumentCommissionRateField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryOrder(PyObject *, CSecurityFtdcOrderField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTrade(PyObject *, CSecurityFtdcTradeField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPosition(PyObject *, CSecurityFtdcInvestorPositionField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnOrder(PyObject *, CSecurityFtdcOrderField *);
static inline int TraderSpi_OnRtnTrade(PyObject *, CSecurityFtdcTradeField *);
static inline int TraderSpi_OnErrRtnOrderInsert(PyObject *, CSecurityFtdcInputOrderField *, CSecurityFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnOrderAction(PyObject *, CSecurityFtdcOrderActionField *, CSecurityFtdcRspInfoField *);
static inline int TraderSpi_OnRspFundOutByLiber(PyObject *, CSecurityFtdcInputFundTransferField *, CSecurityFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnFundOutByLiber(PyObject *, CSecurityFtdcFundTransferField *);
static inline int TraderSpi_OnErrRtnFundOutByLiber(PyObject *, CSecurityFtdcInputFundTransferField *, CSecurityFtdcRspInfoField *);
static inline int TraderSpi_OnRtnFundInByBank(PyObject *, CSecurityFtdcFundTransferField *);
static inline int TraderSpi_OnRspQryFundTransferSerial(PyObject *, CSecurityFtdcFundTransferField *, CSecurityFtdcRspInfoField *, int, bool);

#define X_CALL(op) \
	do { \
		PyGILState_STATE gilstate = PyGILState_Ensure(); \
		tid = PyThread_get_thread_ident(); \
		if ((op) == -1) PyErr_Print(); \
		PyGILState_Release(gilstate); \
	} while (0)

class CTraderSpi : public CSecurityFtdcTraderSpi {
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

	virtual void OnRspError(CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogin(CSecurityFtdcRspUserLoginField *pRspUserLogin, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogout(CSecurityFtdcUserLogoutField *pUserLogout, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspOrderInsert(CSecurityFtdcInputOrderField *pInputOrder, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspOrderAction(CSecurityFtdcInputOrderActionField *pInputOrderAction, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserPasswordUpdate(CSecurityFtdcUserPasswordUpdateField *pUserPasswordUpdate, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspTradingAccountPasswordUpdate(CSecurityFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryExchange(CSecurityFtdcExchangeField *pExchange, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInstrument(CSecurityFtdcInstrumentField *pInstrument, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestor(CSecurityFtdcInvestorField *pInvestor, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTradingCode(CSecurityFtdcTradingCodeField *pTradingCode, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTradingAccount(CSecurityFtdcTradingAccountField *pTradingAccount, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryDepthMarketData(CSecurityFtdcDepthMarketDataField *pDepthMarketData, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryBondInterest(CSecurityFtdcBondInterestField *pBondInterest, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryBondInterest(self, pBondInterest, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryMarketRationInfo(CSecurityFtdcMarketRationInfoField *pMarketRationInfo, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryMarketRationInfo(self, pMarketRationInfo, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInstrumentCommissionRate(CSecurityFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryOrder(CSecurityFtdcOrderField *pOrder, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTrade(CSecurityFtdcTradeField *pTrade, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestorPosition(CSecurityFtdcInvestorPositionField *pInvestorPosition, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnOrder(CSecurityFtdcOrderField *pOrder) {
		X_CALL(TraderSpi_OnRtnOrder(self, pOrder));
	}

	virtual void OnRtnTrade(CSecurityFtdcTradeField *pTrade) {
		X_CALL(TraderSpi_OnRtnTrade(self, pTrade));
	}

	virtual void OnErrRtnOrderInsert(CSecurityFtdcInputOrderField *pInputOrder, CSecurityFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnOrderInsert(self, pInputOrder, pRspInfo));
	}

	virtual void OnErrRtnOrderAction(CSecurityFtdcOrderActionField *pOrderAction, CSecurityFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnOrderAction(self, pOrderAction, pRspInfo));
	}

	virtual void OnRspFundOutByLiber(CSecurityFtdcInputFundTransferField *pInputFundTransfer, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspFundOutByLiber(self, pInputFundTransfer, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnFundOutByLiber(CSecurityFtdcFundTransferField *pFundTransfer) {
		X_CALL(TraderSpi_OnRtnFundOutByLiber(self, pFundTransfer));
	}

	virtual void OnErrRtnFundOutByLiber(CSecurityFtdcInputFundTransferField *pInputFundTransfer, CSecurityFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnFundOutByLiber(self, pInputFundTransfer, pRspInfo));
	}

	virtual void OnRtnFundInByBank(CSecurityFtdcFundTransferField *pFundTransfer) {
		X_CALL(TraderSpi_OnRtnFundInByBank(self, pFundTransfer));
	}

	virtual void OnRspQryFundTransferSerial(CSecurityFtdcFundTransferField *pFundTransfer, CSecurityFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryFundTransferSerial(self, pFundTransfer, pRspInfo, nRequestID, bIsLast));
	}

private:
	PyObject *self;
};

static CSecurityFtdcTraderApi *g_GcApi = NULL;
static long g_GcTid = 0;

static inline void ReleaseTraderApi(CSecurityFtdcTraderApi *api, CTraderSpi *spi) {
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
#define S_BondInterest "BondInterest"
#define S_DepthMarketData "DepthMarketData"
#define S_Exchange "Exchange"
#define S_FundTransfer "FundTransfer"
#define S_InputFundTransfer "InputFundTransfer"
#define S_InputOrder "InputOrder"
#define S_InputOrderAction "InputOrderAction"
#define S_Instrument "Instrument"
#define S_InstrumentCommissionRate "InstrumentCommissionRate"
#define S_Investor "Investor"
#define S_InvestorPosition "InvestorPosition"
#define S_MarketRationInfo "MarketRationInfo"
#define S_Order "Order"
#define S_OrderAction "OrderAction"
#define S_RspInfo "RspInfo"
#define S_RspUserLogin "RspUserLogin"
#define S_Trade "Trade"
#define S_TradingAccount "TradingAccount"
#define S_TradingAccountPasswordUpdate "TradingAccountPasswordUpdate"
#define S_TradingCode "TradingCode"
#define S_UserLogout "UserLogout"
#define S_UserPasswordUpdate "UserPasswordUpdate"

#endif /* CTRADERAPI_H */
