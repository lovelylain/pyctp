#ifndef CTRADERAPI_H
#define CTRADERAPI_H

#include <Python.h>
#include "ThostFtdcTraderApiSSE.h"

static inline void TraderSpi_OnFrontConnected(PyObject *);
static inline void TraderSpi_OnFrontDisconnected(PyObject *, int);
static inline void TraderSpi_OnHeartBeatWarning(PyObject *, int);
static inline void TraderSpi_OnRspAuthenticate(PyObject *, CZQThostFtdcRspAuthenticateField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspUserLogin(PyObject *, CZQThostFtdcRspUserLoginField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspUserLogout(PyObject *, CZQThostFtdcUserLogoutField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspUserPasswordUpdate(PyObject *, CZQThostFtdcUserPasswordUpdateField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspOrderInsert(PyObject *, CZQThostFtdcInputOrderField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspOrderAction(PyObject *, CZQThostFtdcInputOrderActionField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQueryMaxOrderVolume(PyObject *, CZQThostFtdcQueryMaxOrderVolumeField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryOrder(PyObject *, CZQThostFtdcOrderField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTrade(PyObject *, CZQThostFtdcTradeField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInvestorPosition(PyObject *, CZQThostFtdcInvestorPositionField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTradingAccount(PyObject *, CZQThostFtdcTradingAccountField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInvestor(PyObject *, CZQThostFtdcInvestorField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTradingCode(PyObject *, CZQThostFtdcTradingCodeField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInstrumentCommissionRate(PyObject *, CZQThostFtdcInstrumentCommissionRateField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryExchange(PyObject *, CZQThostFtdcExchangeField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInstrument(PyObject *, CZQThostFtdcInstrumentField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryDepthMarketData(PyObject *, CZQThostFtdcDepthMarketDataField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInvestorPositionDetail(PyObject *, CZQThostFtdcInvestorPositionDetailField *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspError(PyObject *, CZQThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRtnOrder(PyObject *, CZQThostFtdcOrderField *);
static inline void TraderSpi_OnRtnTrade(PyObject *, CZQThostFtdcTradeField *);
static inline void TraderSpi_OnErrRtnOrderInsert(PyObject *, CZQThostFtdcInputOrderField *, CZQThostFtdcRspInfoField *);
static inline void TraderSpi_OnErrRtnOrderAction(PyObject *, CZQThostFtdcOrderActionField *, CZQThostFtdcRspInfoField *);
static inline void TraderSpi_OnRtnInstrumentStatus(PyObject *, CZQThostFtdcInstrumentStatusField *);

class CTraderSpi : public CZQThostFtdcTraderSpi {
public:
	CTraderSpi(PyObject *obj):self(obj) {}
	virtual ~CTraderSpi() {}

	virtual void OnFrontConnected() {
		TraderSpi_OnFrontConnected(self);
	}

	virtual void OnFrontDisconnected(int nReason) {
		TraderSpi_OnFrontDisconnected(self, nReason);
	}

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		TraderSpi_OnHeartBeatWarning(self, nTimeLapse);
	}

	virtual void OnRspAuthenticate(CZQThostFtdcRspAuthenticateField *pRspAuthenticate, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspAuthenticate(self, pRspAuthenticate, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserLogin(CZQThostFtdcRspUserLoginField *pRspUserLogin, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserLogout(CZQThostFtdcUserLogoutField *pUserLogout, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserPasswordUpdate(CZQThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspOrderInsert(CZQThostFtdcInputOrderField *pInputOrder, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspOrderAction(CZQThostFtdcInputOrderActionField *pInputOrderAction, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQueryMaxOrderVolume(CZQThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryOrder(CZQThostFtdcOrderField *pOrder, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTrade(CZQThostFtdcTradeField *pTrade, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInvestorPosition(CZQThostFtdcInvestorPositionField *pInvestorPosition, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTradingAccount(CZQThostFtdcTradingAccountField *pTradingAccount, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInvestor(CZQThostFtdcInvestorField *pInvestor, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTradingCode(CZQThostFtdcTradingCodeField *pTradingCode, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInstrumentCommissionRate(CZQThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryExchange(CZQThostFtdcExchangeField *pExchange, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInstrument(CZQThostFtdcInstrumentField *pInstrument, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryDepthMarketData(CZQThostFtdcDepthMarketDataField *pDepthMarketData, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInvestorPositionDetail(CZQThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspError(CZQThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRtnOrder(CZQThostFtdcOrderField *pOrder) {
		TraderSpi_OnRtnOrder(self, pOrder);
	}

	virtual void OnRtnTrade(CZQThostFtdcTradeField *pTrade) {
		TraderSpi_OnRtnTrade(self, pTrade);
	}

	virtual void OnErrRtnOrderInsert(CZQThostFtdcInputOrderField *pInputOrder, CZQThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnOrderInsert(self, pInputOrder, pRspInfo);
	}

	virtual void OnErrRtnOrderAction(CZQThostFtdcOrderActionField *pOrderAction, CZQThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnOrderAction(self, pOrderAction, pRspInfo);
	}

	virtual void OnRtnInstrumentStatus(CZQThostFtdcInstrumentStatusField *pInstrumentStatus) {
		TraderSpi_OnRtnInstrumentStatus(self, pInstrumentStatus);
	}

private:
	PyObject *self;
};

static inline void ReleaseTraderApi(CZQThostFtdcTraderApi *api, CTraderSpi *spi) {
	if (api) {
		api->RegisterSpi(NULL);
#ifndef _WIN32
		if (!spi) {api->Init(); usleep(100000);}
#endif
		api->Release();
		if (spi) delete spi;
	}
}

static const char *const PY_STRINGS[] = {"from_address", "DepthMarketData", "Exchange", "InputOrder", "InputOrderAction", "Instrument", "InstrumentCommissionRate", "InstrumentStatus", "Investor", "InvestorPosition", "InvestorPositionDetail", "Order", "OrderAction", "QueryMaxOrderVolume", "RspAuthenticate", "RspInfo", "RspUserLogin", "Trade", "TradingAccount", "TradingCode", "UserLogout", "UserPasswordUpdate"};

#endif /* CTRADERAPI_H */
