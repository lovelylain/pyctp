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

cdef extern from "ThostFtdcTraderApi.h":
    cdef cppclass CTraderApi "CThostFtdcTraderApi":
        void Release() nogil
        void Init() nogil
        int Join() nogil
        const_char *GetTradingDay() nogil
        void RegisterFront(char *pszFrontAddress) nogil
        void RegisterNameServer(char *pszNsAddress) nogil
        void RegisterFensUserInfo(CFensUserInfoField *pFensUserInfo) nogil
        void RegisterSpi(CTraderSpi *pSpi) nogil
        void SubscribePrivateTopic(TE_RESUME_TYPE nResumeType) nogil
        void SubscribePublicTopic(TE_RESUME_TYPE nResumeType) nogil
        int ReqAuthenticate(CReqAuthenticateField *pReqAuthenticate, int nRequestID) nogil
        int ReqUserLogin(CReqUserLoginField *pReqUserLogin, int nRequestID) nogil
        int ReqUserLogout(CUserLogoutField *pUserLogout, int nRequestID) nogil
        int ReqUserPasswordUpdate(CUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) nogil
        int ReqTradingAccountPasswordUpdate(CTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, int nRequestID) nogil
        int ReqOrderInsert(CInputOrderField *pInputOrder, int nRequestID) nogil
        int ReqParkedOrderInsert(CParkedOrderField *pParkedOrder, int nRequestID) nogil
        int ReqParkedOrderAction(CParkedOrderActionField *pParkedOrderAction, int nRequestID) nogil
        int ReqOrderAction(CInputOrderActionField *pInputOrderAction, int nRequestID) nogil
        int ReqQueryMaxOrderVolume(CQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID) nogil
        int ReqSettlementInfoConfirm(CSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) nogil
        int ReqRemoveParkedOrder(CRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) nogil
        int ReqRemoveParkedOrderAction(CRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) nogil
        int ReqExecOrderInsert(CInputExecOrderField *pInputExecOrder, int nRequestID) nogil
        int ReqExecOrderAction(CInputExecOrderActionField *pInputExecOrderAction, int nRequestID) nogil
        int ReqForQuoteInsert(CInputForQuoteField *pInputForQuote, int nRequestID) nogil
        int ReqQuoteInsert(CInputQuoteField *pInputQuote, int nRequestID) nogil
        int ReqQuoteAction(CInputQuoteActionField *pInputQuoteAction, int nRequestID) nogil
        int ReqCombActionInsert(CInputCombActionField *pInputCombAction, int nRequestID) nogil
        int ReqQryOrder(CQryOrderField *pQryOrder, int nRequestID) nogil
        int ReqQryTrade(CQryTradeField *pQryTrade, int nRequestID) nogil
        int ReqQryInvestorPosition(CQryInvestorPositionField *pQryInvestorPosition, int nRequestID) nogil
        int ReqQryTradingAccount(CQryTradingAccountField *pQryTradingAccount, int nRequestID) nogil
        int ReqQryInvestor(CQryInvestorField *pQryInvestor, int nRequestID) nogil
        int ReqQryTradingCode(CQryTradingCodeField *pQryTradingCode, int nRequestID) nogil
        int ReqQryInstrumentMarginRate(CQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID) nogil
        int ReqQryInstrumentCommissionRate(CQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID) nogil
        int ReqQryExchange(CQryExchangeField *pQryExchange, int nRequestID) nogil
        int ReqQryProduct(CQryProductField *pQryProduct, int nRequestID) nogil
        int ReqQryInstrument(CQryInstrumentField *pQryInstrument, int nRequestID) nogil
        int ReqQryDepthMarketData(CQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) nogil
        int ReqQrySettlementInfo(CQrySettlementInfoField *pQrySettlementInfo, int nRequestID) nogil
        int ReqQryTransferBank(CQryTransferBankField *pQryTransferBank, int nRequestID) nogil
        int ReqQryInvestorPositionDetail(CQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID) nogil
        int ReqQryNotice(CQryNoticeField *pQryNotice, int nRequestID) nogil
        int ReqQrySettlementInfoConfirm(CQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) nogil
        int ReqQryInvestorPositionCombineDetail(CQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID) nogil
        int ReqQryCFMMCTradingAccountKey(CQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) nogil
        int ReqQryEWarrantOffset(CQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) nogil
        int ReqQryInvestorProductGroupMargin(CQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID) nogil
        int ReqQryExchangeMarginRate(CQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID) nogil
        int ReqQryExchangeMarginRateAdjust(CQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID) nogil
        int ReqQryExchangeRate(CQryExchangeRateField *pQryExchangeRate, int nRequestID) nogil
        int ReqQrySecAgentACIDMap(CQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) nogil
        int ReqQryProductExchRate(CQryProductExchRateField *pQryProductExchRate, int nRequestID) nogil
        int ReqQryOptionInstrTradeCost(CQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID) nogil
        int ReqQryOptionInstrCommRate(CQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID) nogil
        int ReqQryExecOrder(CQryExecOrderField *pQryExecOrder, int nRequestID) nogil
        int ReqQryForQuote(CQryForQuoteField *pQryForQuote, int nRequestID) nogil
        int ReqQryQuote(CQryQuoteField *pQryQuote, int nRequestID) nogil
        int ReqQryCombInstrumentGuard(CQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) nogil
        int ReqQryCombAction(CQryCombActionField *pQryCombAction, int nRequestID) nogil
        int ReqQryTransferSerial(CQryTransferSerialField *pQryTransferSerial, int nRequestID) nogil
        int ReqQryAccountregister(CQryAccountregisterField *pQryAccountregister, int nRequestID) nogil
        int ReqQryContractBank(CQryContractBankField *pQryContractBank, int nRequestID) nogil
        int ReqQryParkedOrder(CQryParkedOrderField *pQryParkedOrder, int nRequestID) nogil
        int ReqQryParkedOrderAction(CQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID) nogil
        int ReqQryTradingNotice(CQryTradingNoticeField *pQryTradingNotice, int nRequestID) nogil
        int ReqQryBrokerTradingParams(CQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) nogil
        int ReqQryBrokerTradingAlgos(CQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) nogil
        int ReqQueryCFMMCTradingAccountToken(CQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID) nogil
        int ReqFromBankToFutureByFuture(CReqTransferField *pReqTransfer, int nRequestID) nogil
        int ReqFromFutureToBankByFuture(CReqTransferField *pReqTransfer, int nRequestID) nogil
        int ReqQueryBankAccountMoneyByFuture(CReqQueryAccountField *pReqQueryAccount, int nRequestID) nogil

cdef extern from "ThostFtdcTraderApi.h" namespace "CThostFtdcTraderApi":
    CTraderApi *CreateFtdcTraderApi(const_char *pszFlowPath) nogil except +
    const_char *GetApiVersion() nogil

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
    cdef const_char *S___name__, *S_ctypes, *S_addressof, *S_from_address, *S_Accountregister, *S_BrokerTradingAlgos, *S_BrokerTradingParams, *S_CFMMCTradingAccountKey, *S_CFMMCTradingAccountToken, *S_CancelAccount, *S_ChangeAccount, *S_CombAction, *S_CombInstrumentGuard, *S_ContractBank, *S_DepthMarketData, *S_EWarrantOffset, *S_ErrorConditionalOrder, *S_Exchange, *S_ExchangeMarginRate, *S_ExchangeMarginRateAdjust, *S_ExchangeRate, *S_ExecOrder, *S_ExecOrderAction, *S_ForQuote, *S_ForQuoteRsp, *S_InputCombAction, *S_InputExecOrder, *S_InputExecOrderAction, *S_InputForQuote, *S_InputOrder, *S_InputOrderAction, *S_InputQuote, *S_InputQuoteAction, *S_Instrument, *S_InstrumentCommissionRate, *S_InstrumentMarginRate, *S_InstrumentStatus, *S_Investor, *S_InvestorPosition, *S_InvestorPositionCombineDetail, *S_InvestorPositionDetail, *S_InvestorProductGroupMargin, *S_Notice, *S_NotifyQueryAccount, *S_OpenAccount, *S_OptionInstrCommRate, *S_OptionInstrTradeCost, *S_Order, *S_OrderAction, *S_ParkedOrder, *S_ParkedOrderAction, *S_Product, *S_ProductExchRate, *S_QueryCFMMCTradingAccountToken, *S_QueryMaxOrderVolume, *S_Quote, *S_QuoteAction, *S_RemoveParkedOrder, *S_RemoveParkedOrderAction, *S_ReqQueryAccount, *S_ReqRepeal, *S_ReqTransfer, *S_RspAuthenticate, *S_RspInfo, *S_RspRepeal, *S_RspTransfer, *S_RspUserLogin, *S_SecAgentACIDMap, *S_SettlementInfo, *S_SettlementInfoConfirm, *S_Trade, *S_TradingAccount, *S_TradingAccountPasswordUpdate, *S_TradingCode, *S_TradingNotice, *S_TradingNoticeInfo, *S_TransferBank, *S_TransferSerial, *S_UserLogout, *S_UserPasswordUpdate
