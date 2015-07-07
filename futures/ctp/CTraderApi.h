#ifndef CTRADERAPI_H
#define CTRADERAPI_H

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcTraderApi.h"

static inline int TraderSpi_OnFrontConnected(PyObject *);
static inline int TraderSpi_OnFrontDisconnected(PyObject *, int);
static inline int TraderSpi_OnHeartBeatWarning(PyObject *, int);
static inline int TraderSpi_OnRspAuthenticate(PyObject *, CThostFtdcRspAuthenticateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserPasswordUpdate(PyObject *, CThostFtdcUserPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspTradingAccountPasswordUpdate(PyObject *, CThostFtdcTradingAccountPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOrderInsert(PyObject *, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspParkedOrderInsert(PyObject *, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspParkedOrderAction(PyObject *, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOrderAction(PyObject *, CThostFtdcInputOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQueryMaxOrderVolume(PyObject *, CThostFtdcQueryMaxOrderVolumeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspSettlementInfoConfirm(PyObject *, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspRemoveParkedOrder(PyObject *, CThostFtdcRemoveParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspRemoveParkedOrderAction(PyObject *, CThostFtdcRemoveParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspExecOrderInsert(PyObject *, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspExecOrderAction(PyObject *, CThostFtdcInputExecOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspForQuoteInsert(PyObject *, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQuoteInsert(PyObject *, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQuoteAction(PyObject *, CThostFtdcInputQuoteActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspCombActionInsert(PyObject *, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryOrder(PyObject *, CThostFtdcOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTrade(PyObject *, CThostFtdcTradeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPosition(PyObject *, CThostFtdcInvestorPositionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingAccount(PyObject *, CThostFtdcTradingAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestor(PyObject *, CThostFtdcInvestorField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingCode(PyObject *, CThostFtdcTradingCodeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrumentMarginRate(PyObject *, CThostFtdcInstrumentMarginRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrumentCommissionRate(PyObject *, CThostFtdcInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchange(PyObject *, CThostFtdcExchangeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryProduct(PyObject *, CThostFtdcProductField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrument(PyObject *, CThostFtdcInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQrySettlementInfo(PyObject *, CThostFtdcSettlementInfoField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTransferBank(PyObject *, CThostFtdcTransferBankField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPositionDetail(PyObject *, CThostFtdcInvestorPositionDetailField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryNotice(PyObject *, CThostFtdcNoticeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQrySettlementInfoConfirm(PyObject *, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPositionCombineDetail(PyObject *, CThostFtdcInvestorPositionCombineDetailField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryCFMMCTradingAccountKey(PyObject *, CThostFtdcCFMMCTradingAccountKeyField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryEWarrantOffset(PyObject *, CThostFtdcEWarrantOffsetField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorProductGroupMargin(PyObject *, CThostFtdcInvestorProductGroupMarginField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchangeMarginRate(PyObject *, CThostFtdcExchangeMarginRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchangeMarginRateAdjust(PyObject *, CThostFtdcExchangeMarginRateAdjustField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchangeRate(PyObject *, CThostFtdcExchangeRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQrySecAgentACIDMap(PyObject *, CThostFtdcSecAgentACIDMapField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryProductExchRate(PyObject *, CThostFtdcProductExchRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryOptionInstrTradeCost(PyObject *, CThostFtdcOptionInstrTradeCostField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryOptionInstrCommRate(PyObject *, CThostFtdcOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExecOrder(PyObject *, CThostFtdcExecOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryForQuote(PyObject *, CThostFtdcForQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryQuote(PyObject *, CThostFtdcQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryCombInstrumentGuard(PyObject *, CThostFtdcCombInstrumentGuardField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryCombAction(PyObject *, CThostFtdcCombActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTransferSerial(PyObject *, CThostFtdcTransferSerialField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryAccountregister(PyObject *, CThostFtdcAccountregisterField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnOrder(PyObject *, CThostFtdcOrderField *);
static inline int TraderSpi_OnRtnTrade(PyObject *, CThostFtdcTradeField *);
static inline int TraderSpi_OnErrRtnOrderInsert(PyObject *, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnOrderAction(PyObject *, CThostFtdcOrderActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnInstrumentStatus(PyObject *, CThostFtdcInstrumentStatusField *);
static inline int TraderSpi_OnRtnTradingNotice(PyObject *, CThostFtdcTradingNoticeInfoField *);
static inline int TraderSpi_OnRtnErrorConditionalOrder(PyObject *, CThostFtdcErrorConditionalOrderField *);
static inline int TraderSpi_OnRtnExecOrder(PyObject *, CThostFtdcExecOrderField *);
static inline int TraderSpi_OnErrRtnExecOrderInsert(PyObject *, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnExecOrderAction(PyObject *, CThostFtdcExecOrderActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnForQuoteInsert(PyObject *, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnQuote(PyObject *, CThostFtdcQuoteField *);
static inline int TraderSpi_OnErrRtnQuoteInsert(PyObject *, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnQuoteAction(PyObject *, CThostFtdcQuoteActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnForQuoteRsp(PyObject *, CThostFtdcForQuoteRspField *);
static inline int TraderSpi_OnRtnCFMMCTradingAccountToken(PyObject *, CThostFtdcCFMMCTradingAccountTokenField *);
static inline int TraderSpi_OnRtnCombAction(PyObject *, CThostFtdcCombActionField *);
static inline int TraderSpi_OnErrRtnCombActionInsert(PyObject *, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRspQryContractBank(PyObject *, CThostFtdcContractBankField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryParkedOrder(PyObject *, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryParkedOrderAction(PyObject *, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingNotice(PyObject *, CThostFtdcTradingNoticeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryBrokerTradingParams(PyObject *, CThostFtdcBrokerTradingParamsField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryBrokerTradingAlgos(PyObject *, CThostFtdcBrokerTradingAlgosField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQueryCFMMCTradingAccountToken(PyObject *, CThostFtdcQueryCFMMCTradingAccountTokenField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnFromBankToFutureByBank(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi_OnRtnFromFutureToBankByBank(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi_OnRtnRepealFromBankToFutureByBank(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnRepealFromFutureToBankByBank(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnFromBankToFutureByFuture(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi_OnRtnFromFutureToBankByFuture(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnQueryBankBalanceByFuture(PyObject *, CThostFtdcNotifyQueryAccountField *);
static inline int TraderSpi_OnErrRtnBankToFutureByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnFutureToBankByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(PyObject *, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(PyObject *, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnQueryBankBalanceByFuture(PyObject *, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnRepealFromBankToFutureByFuture(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnRepealFromFutureToBankByFuture(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRspFromBankToFutureByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspFromFutureToBankByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQueryBankAccountMoneyByFuture(PyObject *, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnOpenAccountByBank(PyObject *, CThostFtdcOpenAccountField *);
static inline int TraderSpi_OnRtnCancelAccountByBank(PyObject *, CThostFtdcCancelAccountField *);
static inline int TraderSpi_OnRtnChangeAccountByBank(PyObject *, CThostFtdcChangeAccountField *);

#define X_CALL(op) \
	do { \
		PyGILState_STATE gilstate = PyGILState_Ensure(); \
		tid = PyThread_get_thread_ident(); \
		if ((op) == -1) PyErr_Print(); \
		PyGILState_Release(gilstate); \
	} while (0)

class CTraderSpi : public CThostFtdcTraderSpi {
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

	virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspAuthenticate(self, pRspAuthenticate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspExecOrderInsert(self, pInputExecOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspExecOrderAction(self, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspForQuoteInsert(self, pInputForQuote, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQuoteInsert(self, pInputQuote, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQuoteAction(self, pInputQuoteAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspCombActionInsert(self, pInputCombAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryProduct(self, pProduct, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryExchangeMarginRate(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryExchangeRate(self, pExchangeRate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryProductExchRate(self, pProductExchRate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryExecOrder(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryExecOrder(self, pExecOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryForQuote(self, pForQuote, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryQuote(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryQuote(self, pQuote, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryCombAction(self, pCombAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnOrder(CThostFtdcOrderField *pOrder) {
		X_CALL(TraderSpi_OnRtnOrder(self, pOrder));
	}

	virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {
		X_CALL(TraderSpi_OnRtnTrade(self, pTrade));
	}

	virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnOrderInsert(self, pInputOrder, pRspInfo));
	}

	virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnOrderAction(self, pOrderAction, pRspInfo));
	}

	virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {
		X_CALL(TraderSpi_OnRtnInstrumentStatus(self, pInstrumentStatus));
	}

	virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {
		X_CALL(TraderSpi_OnRtnTradingNotice(self, pTradingNoticeInfo));
	}

	virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) {
		X_CALL(TraderSpi_OnRtnErrorConditionalOrder(self, pErrorConditionalOrder));
	}

	virtual void OnRtnExecOrder(CThostFtdcExecOrderField *pExecOrder) {
		X_CALL(TraderSpi_OnRtnExecOrder(self, pExecOrder));
	}

	virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnExecOrderInsert(self, pInputExecOrder, pRspInfo));
	}

	virtual void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnExecOrderAction(self, pExecOrderAction, pRspInfo));
	}

	virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnForQuoteInsert(self, pInputForQuote, pRspInfo));
	}

	virtual void OnRtnQuote(CThostFtdcQuoteField *pQuote) {
		X_CALL(TraderSpi_OnRtnQuote(self, pQuote));
	}

	virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnQuoteInsert(self, pInputQuote, pRspInfo));
	}

	virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnQuoteAction(self, pQuoteAction, pRspInfo));
	}

	virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
		X_CALL(TraderSpi_OnRtnForQuoteRsp(self, pForQuoteRsp));
	}

	virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {
		X_CALL(TraderSpi_OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken));
	}

	virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction) {
		X_CALL(TraderSpi_OnRtnCombAction(self, pCombAction));
	}

	virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnCombActionInsert(self, pInputCombAction, pRspInfo));
	}

	virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) {
		X_CALL(TraderSpi_OnRtnFromBankToFutureByBank(self, pRspTransfer));
	}

	virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer) {
		X_CALL(TraderSpi_OnRtnFromFutureToBankByBank(self, pRspTransfer));
	}

	virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal) {
		X_CALL(TraderSpi_OnRtnRepealFromBankToFutureByBank(self, pRspRepeal));
	}

	virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal) {
		X_CALL(TraderSpi_OnRtnRepealFromFutureToBankByBank(self, pRspRepeal));
	}

	virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) {
		X_CALL(TraderSpi_OnRtnFromBankToFutureByFuture(self, pRspTransfer));
	}

	virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer) {
		X_CALL(TraderSpi_OnRtnFromFutureToBankByFuture(self, pRspTransfer));
	}

	virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
		X_CALL(TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal));
	}

	virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
		X_CALL(TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal));
	}

	virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) {
		X_CALL(TraderSpi_OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount));
	}

	virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo));
	}

	virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo));
	}

	virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo));
	}

	virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo));
	}

	virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo) {
		X_CALL(TraderSpi_OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo));
	}

	virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal) {
		X_CALL(TraderSpi_OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal));
	}

	virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal) {
		X_CALL(TraderSpi_OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal));
	}

	virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		X_CALL(TraderSpi_OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {
		X_CALL(TraderSpi_OnRtnOpenAccountByBank(self, pOpenAccount));
	}

	virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount) {
		X_CALL(TraderSpi_OnRtnCancelAccountByBank(self, pCancelAccount));
	}

	virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) {
		X_CALL(TraderSpi_OnRtnChangeAccountByBank(self, pChangeAccount));
	}

private:
	PyObject *self;
};

static CThostFtdcTraderApi *g_GcApi = NULL;
static long g_GcTid = 0;

static inline void ReleaseTraderApi(CThostFtdcTraderApi *api, CTraderSpi *spi) {
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
#define S_Accountregister "Accountregister"
#define S_BrokerTradingAlgos "BrokerTradingAlgos"
#define S_BrokerTradingParams "BrokerTradingParams"
#define S_CFMMCTradingAccountKey "CFMMCTradingAccountKey"
#define S_CFMMCTradingAccountToken "CFMMCTradingAccountToken"
#define S_CancelAccount "CancelAccount"
#define S_ChangeAccount "ChangeAccount"
#define S_CombAction "CombAction"
#define S_CombInstrumentGuard "CombInstrumentGuard"
#define S_ContractBank "ContractBank"
#define S_DepthMarketData "DepthMarketData"
#define S_EWarrantOffset "EWarrantOffset"
#define S_ErrorConditionalOrder "ErrorConditionalOrder"
#define S_Exchange "Exchange"
#define S_ExchangeMarginRate "ExchangeMarginRate"
#define S_ExchangeMarginRateAdjust "ExchangeMarginRateAdjust"
#define S_ExchangeRate "ExchangeRate"
#define S_ExecOrder "ExecOrder"
#define S_ExecOrderAction "ExecOrderAction"
#define S_ForQuote "ForQuote"
#define S_ForQuoteRsp "ForQuoteRsp"
#define S_InputCombAction "InputCombAction"
#define S_InputExecOrder "InputExecOrder"
#define S_InputExecOrderAction "InputExecOrderAction"
#define S_InputForQuote "InputForQuote"
#define S_InputOrder "InputOrder"
#define S_InputOrderAction "InputOrderAction"
#define S_InputQuote "InputQuote"
#define S_InputQuoteAction "InputQuoteAction"
#define S_Instrument "Instrument"
#define S_InstrumentCommissionRate "InstrumentCommissionRate"
#define S_InstrumentMarginRate "InstrumentMarginRate"
#define S_InstrumentStatus "InstrumentStatus"
#define S_Investor "Investor"
#define S_InvestorPosition "InvestorPosition"
#define S_InvestorPositionCombineDetail "InvestorPositionCombineDetail"
#define S_InvestorPositionDetail "InvestorPositionDetail"
#define S_InvestorProductGroupMargin "InvestorProductGroupMargin"
#define S_Notice "Notice"
#define S_NotifyQueryAccount "NotifyQueryAccount"
#define S_OpenAccount "OpenAccount"
#define S_OptionInstrCommRate "OptionInstrCommRate"
#define S_OptionInstrTradeCost "OptionInstrTradeCost"
#define S_Order "Order"
#define S_OrderAction "OrderAction"
#define S_ParkedOrder "ParkedOrder"
#define S_ParkedOrderAction "ParkedOrderAction"
#define S_Product "Product"
#define S_ProductExchRate "ProductExchRate"
#define S_QueryCFMMCTradingAccountToken "QueryCFMMCTradingAccountToken"
#define S_QueryMaxOrderVolume "QueryMaxOrderVolume"
#define S_Quote "Quote"
#define S_QuoteAction "QuoteAction"
#define S_RemoveParkedOrder "RemoveParkedOrder"
#define S_RemoveParkedOrderAction "RemoveParkedOrderAction"
#define S_ReqQueryAccount "ReqQueryAccount"
#define S_ReqRepeal "ReqRepeal"
#define S_ReqTransfer "ReqTransfer"
#define S_RspAuthenticate "RspAuthenticate"
#define S_RspInfo "RspInfo"
#define S_RspRepeal "RspRepeal"
#define S_RspTransfer "RspTransfer"
#define S_RspUserLogin "RspUserLogin"
#define S_SecAgentACIDMap "SecAgentACIDMap"
#define S_SettlementInfo "SettlementInfo"
#define S_SettlementInfoConfirm "SettlementInfoConfirm"
#define S_Trade "Trade"
#define S_TradingAccount "TradingAccount"
#define S_TradingAccountPasswordUpdate "TradingAccountPasswordUpdate"
#define S_TradingCode "TradingCode"
#define S_TradingNotice "TradingNotice"
#define S_TradingNoticeInfo "TradingNoticeInfo"
#define S_TransferBank "TransferBank"
#define S_TransferSerial "TransferSerial"
#define S_UserLogout "UserLogout"
#define S_UserPasswordUpdate "UserPasswordUpdate"

#endif /* CTRADERAPI_H */
