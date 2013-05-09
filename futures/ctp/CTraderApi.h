#ifndef CTRADERAPI_H
#define CTRADERAPI_H

#include <Python.h>
#include "ThostFtdcTraderApi.h"

static inline void TraderSpi_OnFrontConnected(PyObject *);
static inline void TraderSpi_OnFrontDisconnected(PyObject *, int);
static inline void TraderSpi_OnHeartBeatWarning(PyObject *, int);
static inline void TraderSpi_OnRspAuthenticate(PyObject *, CThostFtdcRspAuthenticateField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspUserPasswordUpdate(PyObject *, CThostFtdcUserPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspTradingAccountPasswordUpdate(PyObject *, CThostFtdcTradingAccountPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspOrderInsert(PyObject *, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspParkedOrderInsert(PyObject *, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspParkedOrderAction(PyObject *, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspOrderAction(PyObject *, CThostFtdcInputOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQueryMaxOrderVolume(PyObject *, CThostFtdcQueryMaxOrderVolumeField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspSettlementInfoConfirm(PyObject *, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspRemoveParkedOrder(PyObject *, CThostFtdcRemoveParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspRemoveParkedOrderAction(PyObject *, CThostFtdcRemoveParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryOrder(PyObject *, CThostFtdcOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTrade(PyObject *, CThostFtdcTradeField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInvestorPosition(PyObject *, CThostFtdcInvestorPositionField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTradingAccount(PyObject *, CThostFtdcTradingAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInvestor(PyObject *, CThostFtdcInvestorField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTradingCode(PyObject *, CThostFtdcTradingCodeField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInstrumentMarginRate(PyObject *, CThostFtdcInstrumentMarginRateField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInstrumentCommissionRate(PyObject *, CThostFtdcInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryExchange(PyObject *, CThostFtdcExchangeField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInstrument(PyObject *, CThostFtdcInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQrySettlementInfo(PyObject *, CThostFtdcSettlementInfoField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTransferBank(PyObject *, CThostFtdcTransferBankField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInvestorPositionDetail(PyObject *, CThostFtdcInvestorPositionDetailField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryNotice(PyObject *, CThostFtdcNoticeField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQrySettlementInfoConfirm(PyObject *, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryInvestorPositionCombineDetail(PyObject *, CThostFtdcInvestorPositionCombineDetailField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryCFMMCTradingAccountKey(PyObject *, CThostFtdcCFMMCTradingAccountKeyField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryEWarrantOffset(PyObject *, CThostFtdcEWarrantOffsetField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTransferSerial(PyObject *, CThostFtdcTransferSerialField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryAccountregister(PyObject *, CThostFtdcAccountregisterField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRtnOrder(PyObject *, CThostFtdcOrderField *);
static inline void TraderSpi_OnRtnTrade(PyObject *, CThostFtdcTradeField *);
static inline void TraderSpi_OnErrRtnOrderInsert(PyObject *, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *);
static inline void TraderSpi_OnErrRtnOrderAction(PyObject *, CThostFtdcOrderActionField *, CThostFtdcRspInfoField *);
static inline void TraderSpi_OnRtnInstrumentStatus(PyObject *, CThostFtdcInstrumentStatusField *);
static inline void TraderSpi_OnRtnTradingNotice(PyObject *, CThostFtdcTradingNoticeInfoField *);
static inline void TraderSpi_OnRtnErrorConditionalOrder(PyObject *, CThostFtdcErrorConditionalOrderField *);
static inline void TraderSpi_OnRspQryContractBank(PyObject *, CThostFtdcContractBankField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryParkedOrder(PyObject *, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryParkedOrderAction(PyObject *, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryTradingNotice(PyObject *, CThostFtdcTradingNoticeField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryBrokerTradingParams(PyObject *, CThostFtdcBrokerTradingParamsField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQryBrokerTradingAlgos(PyObject *, CThostFtdcBrokerTradingAlgosField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRtnFromBankToFutureByBank(PyObject *, CThostFtdcRspTransferField *);
static inline void TraderSpi_OnRtnFromFutureToBankByBank(PyObject *, CThostFtdcRspTransferField *);
static inline void TraderSpi_OnRtnRepealFromBankToFutureByBank(PyObject *, CThostFtdcRspRepealField *);
static inline void TraderSpi_OnRtnRepealFromFutureToBankByBank(PyObject *, CThostFtdcRspRepealField *);
static inline void TraderSpi_OnRtnFromBankToFutureByFuture(PyObject *, CThostFtdcRspTransferField *);
static inline void TraderSpi_OnRtnFromFutureToBankByFuture(PyObject *, CThostFtdcRspTransferField *);
static inline void TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(PyObject *, CThostFtdcRspRepealField *);
static inline void TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(PyObject *, CThostFtdcRspRepealField *);
static inline void TraderSpi_OnRtnQueryBankBalanceByFuture(PyObject *, CThostFtdcNotifyQueryAccountField *);
static inline void TraderSpi_OnErrRtnBankToFutureByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
static inline void TraderSpi_OnErrRtnFutureToBankByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
static inline void TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(PyObject *, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
static inline void TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(PyObject *, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
static inline void TraderSpi_OnErrRtnQueryBankBalanceByFuture(PyObject *, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *);
static inline void TraderSpi_OnRtnRepealFromBankToFutureByFuture(PyObject *, CThostFtdcRspRepealField *);
static inline void TraderSpi_OnRtnRepealFromFutureToBankByFuture(PyObject *, CThostFtdcRspRepealField *);
static inline void TraderSpi_OnRspFromBankToFutureByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspFromFutureToBankByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRspQueryBankAccountMoneyByFuture(PyObject *, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline void TraderSpi_OnRtnOpenAccountByBank(PyObject *, CThostFtdcOpenAccountField *);
static inline void TraderSpi_OnRtnCancelAccountByBank(PyObject *, CThostFtdcCancelAccountField *);
static inline void TraderSpi_OnRtnChangeAccountByBank(PyObject *, CThostFtdcChangeAccountField *);

class CTraderSpi : public CThostFtdcTraderSpi {
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

	virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspAuthenticate(self, pRspAuthenticate, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQueryMaxOrderVolume(self, pQueryMaxOrderVolume, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRtnOrder(CThostFtdcOrderField *pOrder) {
		TraderSpi_OnRtnOrder(self, pOrder);
	}

	virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {
		TraderSpi_OnRtnTrade(self, pTrade);
	}

	virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnOrderInsert(self, pInputOrder, pRspInfo);
	}

	virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnOrderAction(self, pOrderAction, pRspInfo);
	}

	virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {
		TraderSpi_OnRtnInstrumentStatus(self, pInstrumentStatus);
	}

	virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {
		TraderSpi_OnRtnTradingNotice(self, pTradingNoticeInfo);
	}

	virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) {
		TraderSpi_OnRtnErrorConditionalOrder(self, pErrorConditionalOrder);
	}

	virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) {
		TraderSpi_OnRtnFromBankToFutureByBank(self, pRspTransfer);
	}

	virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer) {
		TraderSpi_OnRtnFromFutureToBankByBank(self, pRspTransfer);
	}

	virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal) {
		TraderSpi_OnRtnRepealFromBankToFutureByBank(self, pRspRepeal);
	}

	virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal) {
		TraderSpi_OnRtnRepealFromFutureToBankByBank(self, pRspRepeal);
	}

	virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) {
		TraderSpi_OnRtnFromBankToFutureByFuture(self, pRspTransfer);
	}

	virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer) {
		TraderSpi_OnRtnFromFutureToBankByFuture(self, pRspTransfer);
	}

	virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
		TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal);
	}

	virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
		TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal);
	}

	virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) {
		TraderSpi_OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount);
	}

	virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo);
	}

	virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo);
	}

	virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo);
	}

	virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo);
	}

	virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo) {
		TraderSpi_OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo);
	}

	virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal) {
		TraderSpi_OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal);
	}

	virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal) {
		TraderSpi_OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal);
	}

	virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		TraderSpi_OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast);
	}

	virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {
		TraderSpi_OnRtnOpenAccountByBank(self, pOpenAccount);
	}

	virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount) {
		TraderSpi_OnRtnCancelAccountByBank(self, pCancelAccount);
	}

	virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) {
		TraderSpi_OnRtnChangeAccountByBank(self, pChangeAccount);
	}

private:
	PyObject *self;
};

static inline void ReleaseTraderApi(CThostFtdcTraderApi *api, CTraderSpi *spi) {
	if (api) {
		api->RegisterSpi(NULL);
#ifndef _WIN32
		if (!spi) {api->Init(); usleep(100000);}
#endif
		api->Release();
		if (spi) delete spi;
	}
}

static const char *const PY_STRINGS[] = {"from_address", "Accountregister", "BrokerTradingAlgos", "BrokerTradingParams", "CFMMCTradingAccountKey", "CancelAccount", "ChangeAccount", "ContractBank", "DepthMarketData", "EWarrantOffset", "ErrorConditionalOrder", "Exchange", "InputOrder", "InputOrderAction", "Instrument", "InstrumentCommissionRate", "InstrumentMarginRate", "InstrumentStatus", "Investor", "InvestorPosition", "InvestorPositionCombineDetail", "InvestorPositionDetail", "Notice", "NotifyQueryAccount", "OpenAccount", "Order", "OrderAction", "ParkedOrder", "ParkedOrderAction", "QueryMaxOrderVolume", "RemoveParkedOrder", "RemoveParkedOrderAction", "ReqQueryAccount", "ReqRepeal", "ReqTransfer", "RspAuthenticate", "RspInfo", "RspRepeal", "RspTransfer", "RspUserLogin", "SettlementInfo", "SettlementInfoConfirm", "Trade", "TradingAccount", "TradingAccountPasswordUpdate", "TradingCode", "TradingNotice", "TradingNoticeInfo", "TransferBank", "TransferSerial", "UserLogout", "UserPasswordUpdate"};

#endif /* CTRADERAPI_H */
