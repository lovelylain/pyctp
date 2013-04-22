# -*- coding: utf-8 -*-

__all__ = ['BaseStruct', 'TE_RESUME', 'TERT_RESTART', 'TERT_RESUME', 'TERT_QUICK', 'EXP_Normal', 'EXP_GenOrderByTrade', 'ICT_EID', 'ICT_IDCard', 'ICT_OfficerIDCard', 'ICT_PoliceIDCard', 'ICT_SoldierIDCard', 'ICT_HouseholdRegister', 'ICT_Passport', 'ICT_TaiwanCompatriotIDCard', 'ICT_HomeComingCard', 'ICT_LicenseNo', 'ICT_OtherCard', 'IR_All', 'IR_Group', 'IR_Single', 'DR_All', 'DR_Group', 'DR_Single', 'DS_Asynchronous', 'DS_Synchronizing', 'DS_Synchronized', 'BDS_Synchronized', 'BDS_Synchronizing', 'ECS_NoConnection', 'ECS_QryInstrumentSent', 'ECS_GotInformation', 'TCS_NotConnected', 'TCS_Connected', 'TCS_QryInstrumentSent', 'TCS_SubPrivateFlow', 'FC_DataAsync', 'FC_ForceUserLogout', 'FC_UserPasswordUpdate', 'FC_BrokerPasswordUpdate', 'FC_InvestorPasswordUpdate', 'FC_OrderInsert', 'FC_OrderAction', 'FC_SyncSystemData', 'FC_SyncBrokerData', 'FC_BachSyncBrokerData', 'FC_SuperQuery', 'FC_ParkedOrderInsert', 'FC_ParkedOrderAction', 'FC_SyncOTP', 'BFC_ForceUserLogout', 'BFC_UserPasswordUpdate', 'BFC_SyncBrokerData', 'BFC_BachSyncBrokerData', 'BFC_OrderInsert', 'BFC_OrderAction', 'BFC_AllQuery', 'BFC_log', 'BFC_BaseQry', 'BFC_TradeQry', 'BFC_Trade', 'BFC_Virement', 'BFC_Risk', 'BFC_Session', 'BFC_RiskNoticeCtl', 'BFC_RiskNotice', 'BFC_BrokerDeposit', 'BFC_QueryFund', 'BFC_QueryOrder', 'BFC_QueryTrade', 'BFC_QueryPosition', 'BFC_QueryMarketData', 'BFC_QueryUserEvent', 'BFC_QueryRiskNotify', 'BFC_QueryFundChange', 'BFC_QueryInvestor', 'BFC_QueryTradingCode', 'BFC_ForceClose', 'BFC_PressTest', 'BFC_RemainCalc', 'BFC_NetPositionInd', 'BFC_RiskPredict', 'BFC_DataExport', 'BFC_RiskTargetSetup', 'BFC_SyncOTP', 'OAS_Submitted', 'OAS_Accepted', 'OAS_Rejected', 'OST_AllTraded', 'OST_PartTradedQueueing', 'OST_PartTradedNotQueueing', 'OST_NoTradeQueueing', 'OST_NoTradeNotQueueing', 'OST_Canceled', 'OST_Unknown', 'OST_NotTouched', 'OST_Touched', 'OSS_InsertSubmitted', 'OSS_CancelSubmitted', 'OSS_ModifySubmitted', 'OSS_Accepted', 'OSS_InsertRejected', 'OSS_CancelRejected', 'OSS_ModifyRejected', 'PSD_Today', 'PSD_History', 'PDT_UseHistory', 'PDT_NoUseHistory', 'ER_Broker', 'ER_Host', 'ER_Maker', 'PC_Futures', 'PC_Options', 'PC_Combination', 'PC_Spot', 'PC_EFP', 'PC_StockA', 'PC_StockB', 'PC_ETF', 'PC_ETFPurRed', 'IP_NotStart', 'IP_Started', 'IP_Pause', 'IP_Expired', 'D_Buy', 'D_Sell', 'D_ETFPur', 'D_ETFRed', 'D_MarginTrade', 'D_ShortSell', 'D_RepayMargin', 'D_RepayStock', 'D_DirectRepayMargin', 'D_DirectRepayStock', 'D_TransferSecurities', 'PT_Net', 'PT_Gross', 'PD_Net', 'PD_Long', 'PD_Short', 'PD_MarginTrade', 'PD_ShortSell', 'SS_NonActive', 'SS_Startup', 'SS_Operating', 'SS_Settlement', 'SS_SettlementFinished', 'RA_Trade', 'RA_Settlement', 'HF_Speculation', 'HF_Hedge', 'OPT_AnyPrice', 'OPT_LimitPrice', 'OPT_BestPrice', 'OPT_LastPrice', 'OPT_LastPricePlusOneTicks', 'OPT_LastPricePlusTwoTicks', 'OPT_LastPricePlusThreeTicks', 'OPT_AskPrice1', 'OPT_AskPrice1PlusOneTicks', 'OPT_AskPrice1PlusTwoTicks', 'OPT_AskPrice1PlusThreeTicks', 'OPT_BidPrice1', 'OPT_BidPrice1PlusOneTicks', 'OPT_BidPrice1PlusTwoTicks', 'OPT_BidPrice1PlusThreeTicks', 'OPT_ActiveANetPassSvrCode', 'OPT_InactiveANetPassSvrCode', 'OPT_ActiveBNetPassSvrCode', 'OPT_InactiveBNetPassSvrCode', 'OPT_Repurchase', 'OPT_DesignatedCancel', 'OPT_Designated', 'OPT_SubscribingShares', 'OPT_Split', 'OPT_TenderOffer', 'OPT_TenderOfferCancel', 'OPT_Ballot', 'OPT_ConvertibleBondsConvet', 'OPT_ConvertibleBondsRepurchase', 'OPT_Exercise', 'OPT_PurchasingFunds', 'OPT_RedemingFunds', 'OPT_SubscribingFunds', 'OPT_LOFIssue', 'OPT_LOFSetBonusType', 'OPT_LOFConvert', 'OPT_DebentureStockIn', 'OPT_DebentureStockOut', 'OPT_PurchasesETF', 'OPT_RedeemETF', 'OPT_ShortAccToCreditAcc', 'OPT_CreditAccToShortAcc', 'OPT_InvAccToCreditAcc', 'OPT_ShortAccToHostAcc', 'OF_Open', 'OF_Close', 'OF_ForceClose', 'OF_CloseToday', 'OF_CloseYesterday', 'OF_ForceOff', 'OF_LocalForceClose', 'FCC_NotForceClose', 'FCC_LackDeposit', 'FCC_ClientOverPositionLimit', 'FCC_MemberOverPositionLimit', 'FCC_NotMultiple', 'FCC_Violation', 'FCC_Other', 'ORDT_Normal', 'ORDT_DeriveFromQuote', 'ORDT_DeriveFromCombination', 'ORDT_Combination', 'ORDT_ConditionalOrder', 'ORDT_Swap', 'TC_IOC', 'TC_GFS', 'TC_GFD', 'TC_GTD', 'TC_GTC', 'TC_GFA', 'VC_AV', 'VC_MV', 'VC_CV', 'CC_Immediately', 'CC_Touch', 'CC_TouchProfit', 'CC_ParkedOrder', 'CC_LastPriceGreaterThanStopPrice', 'CC_LastPriceGreaterEqualStopPrice', 'CC_LastPriceLesserThanStopPrice', 'CC_LastPriceLesserEqualStopPrice', 'CC_AskPriceGreaterThanStopPrice', 'CC_AskPriceGreaterEqualStopPrice', 'CC_AskPriceLesserThanStopPrice', 'CC_AskPriceLesserEqualStopPrice', 'CC_BidPriceGreaterThanStopPrice', 'CC_BidPriceGreaterEqualStopPrice', 'CC_BidPriceLesserThanStopPrice', 'CC_BidPriceLesserEqualStopPrice', 'AF_Delete', 'AF_Modify', 'TR_Allow', 'TR_Forbidden', 'OSRC_Participant', 'OSRC_Administrator', 'TRDT_Common', 'TRDT_OptionsExecution', 'TRDT_OTC', 'TRDT_EFPDerived', 'TRDT_CombinationDerived', 'TRDT_EFTPurchase', 'TRDT_EFTRedem', 'PSRC_LastPrice', 'PSRC_Buy', 'PSRC_Sell', 'IS_BeforeTrading', 'IS_NoTrading', 'IS_Continous', 'IS_AuctionOrdering', 'IS_AuctionBalance', 'IS_AuctionMatch', 'IS_Closed', 'IER_Automatic', 'IER_Manual', 'IER_Fuse', 'BS_NoUpload', 'BS_Uploaded', 'BS_Failed', 'RS_All', 'RS_ByProduct', 'RP_ByVolume', 'RP_ByFeeOnHand', 'RL_Level1', 'RL_Level2', 'RL_Level3', 'RL_Level4', 'RL_Level5', 'RL_Level6', 'RL_Level7', 'RL_Level8', 'RL_Level9', 'RSD_ByPeriod', 'RSD_ByStandard', 'MT_Out', 'MT_In', 'ISPI_BaseMargin', 'ISPI_LowestInterest', 'ISPI_MortgageRatio', 'ISPI_MarginWay', 'ISPI_BillDeposit', 'ESPI_MortgageRatio', 'ESPI_OtherFundItem', 'ESPI_OtherFundImport', 'ESPI_SHFEDelivFee', 'ESPI_DCEDelivFee', 'ESPI_CFFEXMinPrepa', 'SPI_InvestorIDMinLength', 'SPI_AccountIDMinLength', 'SPI_UserRightLogon', 'SPI_SettlementBillTrade', 'SPI_TradingCode', 'SPI_CheckFund', 'SPI_UploadSettlementFile', 'SPI_DownloadCSRCFile', 'SPI_SettlementBillFile', 'SPI_CSRCOthersFile', 'SPI_InvestorPhoto', 'TPID_EncryptionStandard', 'TPID_RiskMode', 'TPID_RiskModeGlobal', 'FI_SettlementFund', 'FI_Trade', 'FI_InvestorPosition', 'FI_SubEntryFund', 'FUT_Settlement', 'FUT_Check', 'FFT_Txt', 'FFT_Zip', 'FFT_DBF', 'FUS_SucceedUpload', 'FUS_FailedUpload', 'FUS_SucceedLoad', 'FUS_PartSucceedLoad', 'FUS_FailedLoad', 'TD_Out', 'TD_In', 'BF_ICBC', 'BF_ABC', 'BF_BC', 'BF_CBC', 'BF_BOC', 'BF_Other', 'SC_NoSpecialRule', 'SC_NoSpringFestival', 'IPT_LastSettlement', 'IPT_LaseClose', 'PLP_Active', 'PLP_NonActive', 'PLP_Canceled', 'DM_CashDeliv', 'DM_CommodityDeliv', 'FIOT_FundIO', 'FIOT_Transfer', 'FT_Deposite', 'FT_ItemFund', 'FT_Company', 'FD_In', 'FD_Out', 'FS_Record', 'FS_Check', 'FS_Charge', 'PS_None', 'PS_Publishing', 'PS_Published', 'ES_NonActive', 'ES_Startup', 'ES_Initialize', 'ES_Initialized', 'ES_Close', 'ES_Closed', 'ES_Settlement', 'STS_Initialize', 'STS_Settlementing', 'STS_Settlemented', 'STS_Finished', 'CT_Person', 'CT_Company', 'CT_Fund', 'BT_Trade', 'BT_TradeSettle', 'FAS_Low', 'FAS_Normal', 'FAS_Focus', 'FAS_Risk', 'FAS_ByTrade', 'FAS_ByDeliv', 'FAS_None', 'FAS_FixFee', 'PWDT_Trade', 'PWDT_Account', 'AG_All', 'AG_OnlyLost', 'AG_OnlyGain', 'AG_None', 'ICP_Include', 'ICP_NotInclude', 'AWT_Enable', 'AWT_Disable', 'FPWD_UnCheck', 'FPWD_Check', 'TT_BankToFuture', 'TT_FutureToBank', 'TVF_Invalid', 'TVF_Valid', 'TVF_Reverse', 'RN_CD', 'RN_ZT', 'RN_QT', 'SEX_None', 'SEX_Man', 'SEX_Woman', 'UT_Investor', 'UT_Operator', 'UT_SuperUser', 'RATETYPE_MarginRate', 'RATETYPE_CommRate', 'RATETYPE_AllRate', 'NOTETYPE_TradeSettleBill', 'NOTETYPE_TradeSettleMonth', 'NOTETYPE_CallMarginNotes', 'NOTETYPE_ForceCloseNotes', 'NOTETYPE_TradeNotes', 'NOTETYPE_DelivNotes', 'SBS_Day', 'SBS_Volume', 'ST_Day', 'ST_Month', 'URT_Logon', 'URT_Transfer', 'URT_EMail', 'URT_Fax', 'URT_ConditionOrder', 'MPT_PreSettlementPrice', 'MPT_SettlementPrice', 'MPT_AveragePrice', 'MPT_OpenPrice', 'BGS_None', 'BGS_NoGenerated', 'BGS_Generated', 'AT_HandlePositionAlgo', 'AT_FindMarginRateAlgo', 'HPA_Base', 'HPA_DCE', 'HPA_CZCE', 'HPA_NoneTrade', 'HPA_Stock', 'FMRA_Base', 'FMRA_DCE', 'FMRA_CZCE', 'HTAA_Base', 'HTAA_DCE', 'HTAA_CZCE', 'PST_Order', 'PST_Open', 'PST_Fund', 'PST_Settlement', 'QIR_All', 'QIR_Group', 'QIR_Single', 'IRS_Normal', 'IRS_Warn', 'IRS_Call', 'IRS_Force', 'IRS_Exception', 'UET_All', 'UET_Login', 'UET_Logout', 'UET_Trading', 'UET_TradingError', 'UET_UpdatePassword', 'UET_Other', 'ICS_Close', 'ICS_CloseToday', 'SM_Non', 'SM_Instrument', 'SM_Product', 'SM_Investor', 'PAOS_NotSend', 'PAOS_Send', 'PAOS_Deleted', 'VDS_Dealing', 'VDS_DeaclSucceed', 'ORGS_Standard', 'ORGS_ESunny', 'ORGS_KingStarV6', 'VTS_NaturalDeal', 'VTS_SucceedEnd', 'VTS_FailedEND', 'VTS_Exception', 'VTS_ManualDeal', 'VTS_MesException', 'VTS_SysException', 'VBAT_BankBook', 'VBAT_BankCard', 'VBAT_CreditCard', 'VMS_Natural', 'VMS_Canceled', 'VAA_NoAvailAbility', 'VAA_AvailAbility', 'VAA_Repeal', 'VTC_BankBankToFuture', 'VTC_BankFutureToBank', 'VTC_FutureBankToFuture', 'VTC_FutureFutureToBank', 'CFMMCKK_REQUEST', 'CFMMCKK_AUTO', 'CFMMCKK_MANUAL', 'CFT_IDCard', 'CFT_Passport', 'CFT_OfficerIDCard', 'CFT_SoldierIDCard', 'CFT_HomeComingCard', 'CFT_HouseholdRegister', 'CFT_LicenseNo', 'CFT_InstitutionCodeCard', 'CFT_TempLicenseNo', 'CFT_NoEnterpriseLicenseNo', 'CFT_OtherCard', 'CFT_SuperDepAgree', 'FBC_Others', 'FBC_TransferDetails', 'FBC_CustAccStatus', 'FBC_AccountTradeDetails', 'FBC_FutureAccountChangeInfoDetails', 'FBC_CustMoneyDetail', 'FBC_CustCancelAccountInfo', 'FBC_CustMoneyResult', 'FBC_OthersExceptionResult', 'FBC_CustInterestNetMoneyDetails', 'FBC_CustMoneySendAndReceiveDetails', 'FBC_CorporationMoneyTotal', 'FBC_MainbodyMoneyTotal', 'FBC_MainPartMonitorData', 'FBC_PreparationMoney', 'FBC_BankMoneyMonitorData', 'CEC_Exchange', 'CEC_Cash', 'YNI_Yes', 'YNI_No', 'BLT_CurrentMoney', 'BLT_UsableMoney', 'BLT_FetchableMoney', 'BLT_FreezeMoney', 'GD_Unknown', 'GD_Male', 'GD_Female', 'FPF_BEN', 'FPF_OUR', 'FPF_SHA', 'PWKT_ExchangeKey', 'PWKT_PassWordKey', 'PWKT_MACKey', 'PWKT_MessageKey', 'PWT_Query', 'PWT_Fetch', 'PWT_Transfer', 'PWT_Trade', 'EM_NoEncry', 'EM_DES', 'EM_3DES', 'BRF_BankNotNeedRepeal', 'BRF_BankWaitingRepeal', 'BRF_BankBeenRepealed', 'BRORF_BrokerNotNeedRepeal', 'BRORF_BrokerWaitingRepeal', 'BRORF_BrokerBeenRepealed', 'TS_Bank', 'TS_Future', 'TS_Store', 'LF_Yes', 'LF_No', 'BAS_Normal', 'BAS_Freeze', 'BAS_ReportLoss', 'MAS_Normal', 'MAS_Cancel', 'MSS_Point', 'MSS_PrePoint', 'MSS_CancelPoint', 'SYT_FutureBankTransfer', 'SYT_StockBankTransfer', 'SYT_TheThirdPartStore', 'TEF_NormalProcessing', 'TEF_Success', 'TEF_Failed', 'TEF_Abnormal', 'TEF_ManualProcessedForException', 'TEF_CommuFailedNeedManualProcess', 'TEF_SysErrorNeedManualProcess', 'PSS_NotProcess', 'PSS_StartProcess', 'PSS_Finished', 'CUSTT_Person', 'CUSTT_Institution', 'FBTTD_FromBankToFuture', 'FBTTD_FromFutureToBank', 'OOD_Open', 'OOD_Destroy', 'AVAF_Invalid', 'AVAF_Valid', 'AVAF_Repeal', 'OT_Bank', 'OT_Future', 'OT_PlateForm', 'OL_HeadQuarters', 'OL_Branch', 'PID_FutureProtocal', 'PID_ICBCProtocal', 'PID_ABCProtocal', 'PID_CBCProtocal', 'PID_CCBProtocal', 'PID_BOCOMProtocal', 'PID_FBTPlateFormProtocal', 'CM_ShortConnect', 'CM_LongConnect', 'SRM_ASync', 'SRM_Sync', 'BAT_BankBook', 'BAT_SavingCard', 'BAT_CreditCard', 'FAT_BankBook', 'FAT_SavingCard', 'FAT_CreditCard', 'OS_Ready', 'OS_CheckIn', 'OS_CheckOut', 'OS_CheckFileArrived', 'OS_CheckDetail', 'OS_DayEndClean', 'OS_Invalid', 'CCBFM_ByAmount', 'CCBFM_ByMonth', 'CAPIT_Client', 'CAPIT_Server', 'CAPIT_UserApi', 'LS_Connected', 'LS_Disconnected', 'BPWDF_NoCheck', 'BPWDF_BlankCheck', 'BPWDF_EncryptCheck', 'SAT_AccountID', 'SAT_CardID', 'SAT_SHStockholderID', 'SAT_SZStockholderID', 'TRFS_Normal', 'TRFS_Repealed', 'SPTYPE_Broker', 'SPTYPE_Bank', 'REQRSP_Request', 'REQRSP_Response', 'FBTUET_SignIn', 'FBTUET_FromBankToFuture', 'FBTUET_FromFutureToBank', 'FBTUET_OpenAccount', 'FBTUET_CancelAccount', 'FBTUET_ChangeAccount', 'FBTUET_RepealFromBankToFuture', 'FBTUET_RepealFromFutureToBank', 'FBTUET_QueryBankAccount', 'FBTUET_QueryFutureAccount', 'FBTUET_SignOut', 'FBTUET_SyncKey', 'FBTUET_Other', 'NC_NOERROR', 'NC_Warn', 'NC_Call', 'NC_Force', 'NC_CHUANCANG', 'NC_Exception', 'FCT_Manual', 'FCT_Single', 'FCT_Group', 'RNM_System', 'RNM_SMS', 'RNM_EMail', 'RNS_NotGen', 'RNS_Generated', 'RNS_SendError', 'RNS_SendOk', 'RNS_Received', 'RNS_Confirmed', 'RUE_ExportData', 'COST_LastPriceAsc', 'COST_LastPriceDesc', 'COST_AskPriceAsc', 'COST_AskPriceDesc', 'COST_BidPriceAsc', 'COST_BidPriceDesc', 'UOAST_NoSend', 'UOAST_Sended', 'UOAST_Generated', 'UOAST_SendFail', 'UOAST_Success', 'UOAST_Fail', 'UOAST_Cancel', 'UOACS_NoApply', 'UOACS_Submited', 'UOACS_Sended', 'UOACS_Success', 'UOACS_Refuse', 'UOACS_Cancel', 'QT_Radio', 'QT_Option', 'QT_Blank', 'PT_ApplyTradingCode', 'PT_CancelTradingCode', 'PT_ModifyIDCard', 'PT_ModifyNoIDCard', 'PT_ExchOpenBak', 'PT_ExchCancelBak', 'BT_Request', 'BT_Response', 'BT_Notice', 'CRC_Success', 'CRC_Working', 'CRC_InfoFail', 'CRC_IDCardFail', 'CRC_OtherFail', 'CfMMCCT_All', 'CfMMCCT_Person', 'CfMMCCT_Company', 'EIDT_SHFE', 'EIDT_CZCE', 'EIDT_DCE', 'EIDT_CFFEX', 'ECIDT_Hedge', 'ECIDT_Arbitrage', 'ECIDT_Speculation', 'UF_NoUpdate', 'UF_Success', 'UF_Fail', 'UF_TCSuccess', 'UF_TCFail', 'UF_Cancel', 'AOID_OpenInvestor', 'AOID_ModifyIDCard', 'AOID_ModifyNoIDCard', 'AOID_ApplyTradingCode', 'AOID_CancelTradingCode', 'AOID_CancelInvestor', 'ASID_NoComplete', 'ASID_Submited', 'ASID_Checked', 'ASID_Refused', 'ASID_Deleted', 'UOASM_ByAPI', 'UOASM_ByFile', 'EvM_ADD', 'EvM_UPDATE', 'EvM_DELETE', 'EvM_CHECK', 'UOAA_ASR', 'UOAA_ASNR', 'UOAA_NSAR', 'UOAA_NSR', 'EvM_InvestorGroupFlow', 'CL_Zero', 'CL_One', 'CL_Two', 'CHS_Init', 'CHS_Checking', 'CHS_Checked', 'CHS_Refuse', 'CHS_Cancel', 'CHU_Unused', 'CHU_Used', 'CHU_Fail', 'BAO_ByAccProperty', 'BAO_ByFBTransfer', 'MBTS_ByInstrument', 'MBTS_ByDayInsPrc', 'MBTS_ByDayIns', 'FTC_BankLaunchBankToBroker', 'FTC_BrokerLaunchBankToBroker', 'FTC_BankLaunchBrokerToBank', 'FTC_BrokerLaunchBrokerToBank', 'OTP_NONE', 'OTP_TOTP', 'OTPS_Unused', 'OTPS_Used', 'OTPS_Disuse', 'BUT_Investor', 'FUTT_Commodity', 'FUTT_Financial', 'FET_Restriction', 'FET_TodayRestriction', 'FET_Transfer', 'FET_Credit', 'FET_InvestorWithdrawAlm', 'AST_FBTransfer', 'AST_ManualEntry', 'CST_UnifyAccount', 'CST_ManualEntry', 'UR_All', 'UR_Single', 'STT_Stock', 'STT_BuyNetService', 'STT_CancelRepurchase', 'STT_CancelRegister', 'STT_Register', 'STT_PurchaseIssue', 'STT_Allotment', 'STT_SellTender', 'STT_BuyTender', 'STT_NetVote', 'STT_SellConvertibleBonds', 'STT_OptionExecute', 'STT_PurchaseOF', 'STT_RedeemOF', 'STT_SubscribeOF', 'STT_OFCustodianTranfer', 'STT_OFDividendConfig', 'STT_OFTransfer', 'STT_BondsIn', 'STT_BondsOut', 'STT_PurchaseETF', 'STT_RedeemETF', 'STT_ConvertibleRegister', 'CDS_Forbidden', 'CDS_Allow', 'CDS_OnlyPurchase', 'CDS_OnlyRedeem', 'ETFCRS_Forbidden', 'ETFCRS_Allow', 'ETFCRS_Force', 'Dissemination', 'ReqUserLogin', 'RspUserLogin', 'UserLogout', 'ForceUserLogout', 'ReqAuthenticate', 'RspAuthenticate', 'AuthenticationInfo', 'TransferHeader', 'TransferBankToFutureReq', 'TransferBankToFutureRsp', 'TransferFutureToBankReq', 'TransferFutureToBankRsp', 'TransferQryBankReq', 'TransferQryBankRsp', 'TransferQryDetailReq', 'TransferQryDetailRsp', 'RspInfo', 'Exchange', 'Product', 'Instrument', 'Broker', 'Trader', 'Investor', 'TradingCode', 'PartBroker', 'SuperUser', 'SuperUserFunction', 'InvestorGroup', 'TradingAccount', 'InvestorPosition', 'InstrumentMarginRate', 'InstrumentCommissionRate', 'DepthMarketData', 'InstrumentTradingRight', 'BrokerUser', 'BrokerUserPassword', 'BrokerUserFunction', 'TraderOffer', 'SettlementInfo', 'InstrumentMarginRateAdjust', 'ExchangeMarginRate', 'ExchangeMarginRateAdjust', 'SettlementRef', 'CurrentTime', 'CommPhase', 'LoginInfo', 'LogoutAll', 'FrontStatus', 'UserPasswordUpdate', 'InputOrder', 'Order', 'ExchangeOrder', 'ExchangeOrderInsertError', 'InputOrderAction', 'OrderAction', 'ExchangeOrderAction', 'ExchangeOrderActionError', 'ExchangeTrade', 'Trade', 'UserSession', 'QueryMaxOrderVolume', 'SettlementInfoConfirm', 'SyncDeposit', 'BrokerSync', 'SyncingInvestor', 'SyncingTradingCode', 'SyncingInvestorGroup', 'SyncingTradingAccount', 'SyncingInvestorPosition', 'SyncingInstrumentMarginRate', 'SyncingInstrumentCommissionRate', 'SyncingInstrumentTradingRight', 'QryOrder', 'QryTrade', 'QryInvestorPosition', 'QryTradingAccount', 'QryInvestor', 'QryTradingCode', 'QryInvestorGroup', 'QryInstrumentMarginRate', 'QryInstrumentCommissionRate', 'QryInstrumentTradingRight', 'QryBroker', 'QryTrader', 'QryPartBroker', 'QrySuperUserFunction', 'QryUserSession', 'QryFrontStatus', 'QryExchangeOrder', 'QryOrderAction', 'QryExchangeOrderAction', 'QrySuperUser', 'QryExchange', 'QryProduct', 'QryInstrument', 'QryDepthMarketData', 'QryBrokerUser', 'QryBrokerUserFunction', 'QryTraderOffer', 'QrySyncDeposit', 'QrySettlementInfo', 'QryHisOrder', 'MarketData', 'MarketDataBase', 'MarketDataStatic', 'MarketDataLastMatch', 'MarketDataBestPrice', 'MarketDataBid23', 'MarketDataAsk23', 'MarketDataBid45', 'MarketDataAsk45', 'MarketDataUpdateTime', 'SpecificInstrument', 'InstrumentStatus', 'QryInstrumentStatus', 'InvestorAccount', 'PositionProfitAlgorithm', 'Discount', 'QryTransferBank', 'TransferBank', 'QryInvestorPositionDetail', 'InvestorPositionDetail', 'TradingAccountPassword', 'MDTraderOffer', 'QryMDTraderOffer', 'QryNotice', 'Notice', 'UserRight', 'QrySettlementInfoConfirm', 'LoadSettlementInfo', 'BrokerWithdrawAlgorithm', 'TradingAccountPasswordUpdateV1', 'TradingAccountPasswordUpdate', 'QryCombinationLeg', 'QrySyncStatus', 'CombinationLeg', 'SyncStatus', 'QryLinkMan', 'LinkMan', 'QryBrokerUserEvent', 'BrokerUserEvent', 'QryContractBank', 'ContractBank', 'InvestorPositionCombineDetail', 'ParkedOrder', 'ParkedOrderAction', 'QryParkedOrder', 'QryParkedOrderAction', 'RemoveParkedOrder', 'RemoveParkedOrderAction', 'InvestorWithdrawAlgorithm', 'QryInvestorPositionCombineDetail', 'MarketDataAveragePrice', 'VerifyInvestorPassword', 'UserIP', 'TradingNoticeInfo', 'TradingNotice', 'QryTradingNotice', 'QryErrOrder', 'ErrOrder', 'ErrorConditionalOrder', 'QryErrOrderAction', 'ErrOrderAction', 'QryExchangeSequence', 'ExchangeSequence', 'QueryMaxOrderVolumeWithPrice', 'QryBrokerTradingParams', 'BrokerTradingParams', 'QryBrokerTradingAlgos', 'BrokerTradingAlgos', 'QueryBrokerDeposit', 'BrokerDeposit', 'QryCFMMCBrokerKey', 'CFMMCBrokerKey', 'CFMMCTradingAccountKey', 'QryCFMMCTradingAccountKey', 'BrokerUserOTPParam', 'ManualSyncBrokerUserOTP', 'ReqOpenAccount', 'ReqCancelAccount', 'ReqChangeAccount', 'ReqTransfer', 'RspTransfer', 'ReqRepeal', 'RspRepeal', 'ReqQueryAccount', 'RspQueryAccount', 'FutureSignIO', 'RspFutureSignIn', 'ReqFutureSignOut', 'RspFutureSignOut', 'ReqQueryTradeResultBySerial', 'RspQueryTradeResultBySerial', 'ReqDayEndFileReady', 'ReturnResult', 'VerifyFuturePassword', 'VerifyCustInfo', 'VerifyFuturePasswordAndCustInfo', 'DepositResultInform', 'ReqSyncKey', 'RspSyncKey', 'NotifyQueryAccount', 'TransferSerial', 'QryTransferSerial', 'NotifyFutureSignIn', 'NotifyFutureSignOut', 'NotifySyncKey', 'MaxStockPositionAmount', 'error']

_init = list(globals()); _init.extend(__all__)
import sys
from ctypes import c_char, c_short, c_int, c_double, Structure

u = (lambda s:s) if sys.version_info[0] >= 3 else (lambda s:s.decode('unicode-escape'))

class BaseStruct(Structure):
    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, ', '.join('%s=%r'%(k,getattr(self,k)) for k,t in self._fields_))

TE_RESUME = c_int #流重传方式
TERT_RESTART = 0 #从本交易日开始重传
TERT_RESUME = 1 #从上次收到的续传
TERT_QUICK = 2 #只传送登录后的流内容
TTraderID = c_char * 21 #交易所交易员代码
TInvestorID = c_char * 15 #投资者代码
TBrokerID = c_char * 11 #经纪公司代码
TBrokerAbbr = c_char * 9 #经纪公司简称
TBrokerName = c_char * 81 #经纪公司名称
TExchangeInstID = c_char * 31 #合约在交易所的代码
TOrderRef = c_char * 13 #报单引用
TParticipantID = c_char * 11 #会员代码
TUserID = c_char * 16 #用户代码
TPassword = c_char * 41 #密码
TClientID = c_char * 11 #交易编码
TInstrumentID = c_char * 31 #合约代码
TMarketID = c_char * 31 #市场代码
TProductName = c_char * 21 #产品名称
TExchangeID = c_char * 9 #交易所代码
TExchangeName = c_char * 31 #交易所名称
TExchangeAbbr = c_char * 9 #交易所简称
TExchangeFlag = c_char * 2 #交易所标志
TMacAddress = c_char * 21 #Mac地址
TExchangeProperty = c_char #交易所属性
EXP_Normal = '0' #正常
EXP_GenOrderByTrade = '1' #根据成交生成报单
TDate = c_char * 9 #日期
TTime = c_char * 9 #时间
TLongTime = c_char * 13 #长时间
TInstrumentName = c_char * 21 #合约名称
TSettlementGroupID = c_char * 9 #结算组代码
TOrderSysID = c_char * 21 #报单编号
TTradeID = c_char * 21 #成交编号
TCommandType = c_char * 65 #DB命令类型
TIPAddress = c_char * 16 #IP地址
TProductInfo = c_char * 11 #产品信息
TProtocolInfo = c_char * 11 #协议信息
TBusinessUnit = c_char * 21 #业务单元
TDepositSeqNo = c_char * 15 #出入金流水号
TIdentifiedCardNo = c_char * 51 #证件号码
TIdCardType = c_char #证件类型
ICT_EID = '0' #组织机构代码
ICT_IDCard = '1' #身份证
ICT_OfficerIDCard = '2' #军官证
ICT_PoliceIDCard = '3' #警官证
ICT_SoldierIDCard = '4' #士兵证
ICT_HouseholdRegister = '5' #户口簿
ICT_Passport = '6' #护照
ICT_TaiwanCompatriotIDCard = '7' #台胞证
ICT_HomeComingCard = '8' #回乡证
ICT_LicenseNo = '9' #营业执照号
ICT_OtherCard = 'x' #其他证件
TOrderLocalID = c_char * 13 #本地报单编号
TUserName = c_char * 81 #用户名称
TPartyName = c_char * 81 #参与人名称
TErrorMsg = c_char * 81 #错误信息
TFieldName = c_char * 2049 #字段名
TFieldContent = c_char * 2049 #字段内容
TSystemName = c_char * 41 #系统名称
TContent = c_char * 501 #消息正文
TInvestorRange = c_char #投资者范围
IR_All = '1' #所有
IR_Group = '2' #投资者组
IR_Single = '3' #单一投资者
TDepartmentRange = c_char #投资者范围
DR_All = '1' #所有
DR_Group = '2' #组织架构
DR_Single = '3' #单一投资者
TDataSyncStatus = c_char #数据同步状态
DS_Asynchronous = '1' #未同步
DS_Synchronizing = '2' #同步中
DS_Synchronized = '3' #已同步
TBrokerDataSyncStatus = c_char #经纪公司数据同步状态
BDS_Synchronized = '1' #已同步
BDS_Synchronizing = '2' #同步中
TExchangeConnectStatus = c_char #交易所连接状态
ECS_NoConnection = '1' #没有任何连接
ECS_QryInstrumentSent = '2' #已经发出合约查询请求
ECS_GotInformation = '9' #已经获取信息
TTraderConnectStatus = c_char #交易所交易员连接状态
TCS_NotConnected = '1' #没有任何连接
TCS_Connected = '2' #已经连接
TCS_QryInstrumentSent = '3' #已经发出合约查询请求
TCS_SubPrivateFlow = '4' #订阅私有流
TFunctionCode = c_char #功能代码
FC_DataAsync = '1' #数据异步化
FC_ForceUserLogout = '2' #强制用户登出
FC_UserPasswordUpdate = '3' #变更管理用户口令
FC_BrokerPasswordUpdate = '4' #变更经纪公司口令
FC_InvestorPasswordUpdate = '5' #变更投资者口令
FC_OrderInsert = '6' #报单插入
FC_OrderAction = '7' #报单操作
FC_SyncSystemData = '8' #同步系统数据
FC_SyncBrokerData = '9' #同步经纪公司数据
FC_BachSyncBrokerData = 'A' #批量同步经纪公司数据
FC_SuperQuery = 'B' #超级查询
FC_ParkedOrderInsert = 'C' #报单插入
FC_ParkedOrderAction = 'D' #报单操作
FC_SyncOTP = 'E' #同步动态令牌
TBrokerFunctionCode = c_char #经纪公司功能代码
BFC_ForceUserLogout = '1' #强制用户登出
BFC_UserPasswordUpdate = '2' #变更用户口令
BFC_SyncBrokerData = '3' #同步经纪公司数据
BFC_BachSyncBrokerData = '4' #批量同步经纪公司数据
BFC_OrderInsert = '5' #报单插入
BFC_OrderAction = '6' #报单操作
BFC_AllQuery = '7' #全部查询
BFC_log = 'a' #系统功能：登入/登出/修改密码等
BFC_BaseQry = 'b' #基本查询：查询基础数据，如合约，交易所等常量
BFC_TradeQry = 'c' #交易查询：如查成交，委托
BFC_Trade = 'd' #交易功能：报单，撤单
BFC_Virement = 'e' #银期转账
BFC_Risk = 'f' #风险监控
BFC_Session = 'g' #查询/管理：查询会话，踢人等
BFC_RiskNoticeCtl = 'h' #风控通知控制
BFC_RiskNotice = 'i' #风控通知发送
BFC_BrokerDeposit = 'j' #察看经纪公司资金权限
BFC_QueryFund = 'k' #资金查询
BFC_QueryOrder = 'l' #报单查询
BFC_QueryTrade = 'm' #成交查询
BFC_QueryPosition = 'n' #持仓查询
BFC_QueryMarketData = 'o' #行情查询
BFC_QueryUserEvent = 'p' #用户事件查询
BFC_QueryRiskNotify = 'q' #风险通知查询
BFC_QueryFundChange = 'r' #出入金查询
BFC_QueryInvestor = 's' #投资者信息查询
BFC_QueryTradingCode = 't' #交易编码查询
BFC_ForceClose = 'u' #强平
BFC_PressTest = 'v' #压力测试
BFC_RemainCalc = 'w' #权益反算
BFC_NetPositionInd = 'x' #净持仓保证金指标
BFC_RiskPredict = 'y' #风险预算
BFC_DataExport = 'z' #数据导出
BFC_RiskTargetSetup = 'A' #风控指标设置
BFC_SyncOTP = 'E' #同步动态令牌
TOrderActionStatus = c_char #报单操作状态
OAS_Submitted = 'a' #已经提交
OAS_Accepted = 'b' #已经接受
OAS_Rejected = 'c' #已经被拒绝
TOrderStatus = c_char #报单状态
OST_AllTraded = '0' #全部成交
OST_PartTradedQueueing = '1' #部分成交还在队列中
OST_PartTradedNotQueueing = '2' #部分成交不在队列中
OST_NoTradeQueueing = '3' #未成交还在队列中
OST_NoTradeNotQueueing = '4' #未成交不在队列中
OST_Canceled = '5' #撤单
OST_Unknown = 'a' #未知
OST_NotTouched = 'b' #尚未触发
OST_Touched = 'c' #已触发
TOrderSubmitStatus = c_char #报单提交状态
OSS_InsertSubmitted = '0' #已经提交
OSS_CancelSubmitted = '1' #撤单已经提交
OSS_ModifySubmitted = '2' #修改已经提交
OSS_Accepted = '3' #已经接受
OSS_InsertRejected = '4' #报单已经被拒绝
OSS_CancelRejected = '5' #撤单已经被拒绝
OSS_ModifyRejected = '6' #改单已经被拒绝
TPositionDate = c_char #持仓日期
PSD_Today = '1' #今日持仓
PSD_History = '2' #历史持仓
TPositionDateType = c_char #持仓日期类型
PDT_UseHistory = '1' #使用历史持仓
PDT_NoUseHistory = '2' #不使用历史持仓
TTradingRole = c_char #交易角色
ER_Broker = '1' #代理
ER_Host = '2' #自营
ER_Maker = '3' #做市商
TProductClass = c_char #产品类型
PC_Futures = '1' #期货
PC_Options = '2' #期权
PC_Combination = '3' #组合
PC_Spot = '4' #即期
PC_EFP = '5' #期转现
PC_StockA = '6' #证券A股
PC_StockB = '7' #证券B股
PC_ETF = '8' #ETF
PC_ETFPurRed = '9' #ETF申赎
TInstLifePhase = c_char #合约生命周期状态
IP_NotStart = '0' #未上市
IP_Started = '1' #上市
IP_Pause = '2' #停牌
IP_Expired = '3' #到期
TDirection = c_char #买卖方向
D_Buy = '0' #买
D_Sell = '1' #卖
D_ETFPur = '2' #ETF申购
D_ETFRed = '3' #ETF赎回
D_MarginTrade = '4' #融资买入
D_ShortSell = '5' #融券卖出
D_RepayMargin = '6' #卖券还款
D_RepayStock = '7' #买券还券
D_DirectRepayMargin = '8' #直接还款
D_DirectRepayStock = '9' #直接还券
D_TransferSecurities = '10' #担保品划转
TPositionType = c_char #持仓类型
PT_Net = '1' #净持仓
PT_Gross = '2' #综合持仓
TPosiDirection = c_char #持仓多空方向
PD_Net = '1' #净
PD_Long = '2' #多头
PD_Short = '3' #空头
PD_MarginTrade = '4' #融资
PD_ShortSell = '5' #融券
TSysSettlementStatus = c_char #系统结算状态
SS_NonActive = '1' #不活跃
SS_Startup = '2' #启动
SS_Operating = '3' #操作
SS_Settlement = '4' #结算
SS_SettlementFinished = '5' #结算完成
TRatioAttr = c_char #费率属性
RA_Trade = '0' #交易费率
RA_Settlement = '1' #结算费率
THedgeFlag = c_char #投机套保标志
HF_Speculation = '1' #投机
HF_Hedge = '3' #套保
TOrderPriceType = c_char #报单价格条件
OPT_AnyPrice = '1' #任意价
OPT_LimitPrice = '2' #限价
OPT_BestPrice = '3' #最优价
OPT_LastPrice = '4' #最新价
OPT_LastPricePlusOneTicks = '5' #最新价浮动上浮1个ticks
OPT_LastPricePlusTwoTicks = '6' #最新价浮动上浮2个ticks
OPT_LastPricePlusThreeTicks = '7' #最新价浮动上浮3个ticks
OPT_AskPrice1 = '8' #卖一价
OPT_AskPrice1PlusOneTicks = '9' #卖一价浮动上浮1个ticks
OPT_AskPrice1PlusTwoTicks = 'A' #卖一价浮动上浮2个ticks
OPT_AskPrice1PlusThreeTicks = 'B' #卖一价浮动上浮3个ticks
OPT_BidPrice1 = 'C' #买一价
OPT_BidPrice1PlusOneTicks = 'D' #买一价浮动上浮1个ticks
OPT_BidPrice1PlusTwoTicks = 'E' #买一价浮动上浮2个ticks
OPT_BidPrice1PlusThreeTicks = 'F' #买一价浮动上浮3个ticks
OPT_ActiveANetPassSvrCode = 'G' #激活A股网络密码服务代码
OPT_InactiveANetPassSvrCode = 'H' #注销A股网络密码服务代码
OPT_ActiveBNetPassSvrCode = 'I' #激活B股网络密码服务代码
OPT_InactiveBNetPassSvrCode = 'J' #注销B股网络密码服务代码
OPT_Repurchase = 'K' #回购注销
OPT_DesignatedCancel = 'L' #指定撤销
OPT_Designated = 'M' #指定登记
OPT_SubscribingShares = 'N' #证券参与申购
OPT_Split = 'O' #证券参与配股
OPT_TenderOffer = 'P' #要约收购登记
OPT_TenderOfferCancel = 'Q' #要约收购撤销
OPT_Ballot = 'R' #证券投票
OPT_ConvertibleBondsConvet = 'S' #可转债转换登记
OPT_ConvertibleBondsRepurchase = 'T' #可转债回售登记
OPT_Exercise = 'U' #权证行权
OPT_PurchasingFunds = 'V' #开放式基金申购
OPT_RedemingFunds = 'W' #开放式基金赎回
OPT_SubscribingFunds = 'X' #开放式基金认购
OPT_LOFIssue = 'Y' #开放式基金转托管转出
OPT_LOFSetBonusType = 'Z' #开放式基金设置分红方式
OPT_LOFConvert = 'a' #开放式基金转换为其他基金
OPT_DebentureStockIn = 'b' #债券入库
OPT_DebentureStockOut = 'c' #债券出库
OPT_PurchasesETF = 'd' #ETF申购
OPT_RedeemETF = 'e' #ETF赎回
OPT_ShortAccToCreditAcc = 'f' #证券公司融券专用账户过户到证券公司信用交易担保证券账户
OPT_CreditAccToShortAcc = 'g' #证券公司信用交易担保证券账户过户到证券公司融券专用账户
OPT_InvAccToCreditAcc = 'h' #投资者普通证券账户过户到证券公司信用交易担保证券账户
OPT_ShortAccToHostAcc = 'i' #证券公司融券专用账户过户到证券公司自营账户
TOffsetFlag = c_char #开平标志
OF_Open = '0' #开仓
OF_Close = '1' #平仓
OF_ForceClose = '2' #强平
OF_CloseToday = '3' #平今
OF_CloseYesterday = '4' #平昨
OF_ForceOff = '5' #强减
OF_LocalForceClose = '6' #本地强平
TForceCloseReason = c_char #强平原因
FCC_NotForceClose = '0' #非强平
FCC_LackDeposit = '1' #资金不足
FCC_ClientOverPositionLimit = '2' #客户超仓
FCC_MemberOverPositionLimit = '3' #会员超仓
FCC_NotMultiple = '4' #持仓非整数倍
FCC_Violation = '5' #违规
FCC_Other = '6' #其它
TOrderType = c_char #报单类型
ORDT_Normal = '0' #正常
ORDT_DeriveFromQuote = '1' #报价衍生
ORDT_DeriveFromCombination = '2' #组合衍生
ORDT_Combination = '3' #组合报单
ORDT_ConditionalOrder = '4' #条件单
ORDT_Swap = '5' #互换单
TTimeCondition = c_char #有效期类型
TC_IOC = '1' #立即完成，否则撤销
TC_GFS = '2' #本节有效
TC_GFD = '3' #当日有效
TC_GTD = '4' #指定日期前有效
TC_GTC = '5' #撤销前有效
TC_GFA = '6' #集合竞价有效
TVolumeCondition = c_char #成交量类型
VC_AV = '1' #任何数量
VC_MV = '2' #最小数量
VC_CV = '3' #全部数量
TContingentCondition = c_char #触发条件
CC_Immediately = '1' #立即
CC_Touch = '2' #止损
CC_TouchProfit = '3' #止赢
CC_ParkedOrder = '4' #预埋单
CC_LastPriceGreaterThanStopPrice = '5' #最新价大于条件价
CC_LastPriceGreaterEqualStopPrice = '6' #最新价大于等于条件价
CC_LastPriceLesserThanStopPrice = '7' #最新价小于条件价
CC_LastPriceLesserEqualStopPrice = '8' #最新价小于等于条件价
CC_AskPriceGreaterThanStopPrice = '9' #卖一价大于条件价
CC_AskPriceGreaterEqualStopPrice = 'A' #卖一价大于等于条件价
CC_AskPriceLesserThanStopPrice = 'B' #卖一价小于条件价
CC_AskPriceLesserEqualStopPrice = 'C' #卖一价小于等于条件价
CC_BidPriceGreaterThanStopPrice = 'D' #买一价大于条件价
CC_BidPriceGreaterEqualStopPrice = 'E' #买一价大于等于条件价
CC_BidPriceLesserThanStopPrice = 'F' #买一价小于条件价
CC_BidPriceLesserEqualStopPrice = 'H' #买一价小于等于条件价
TActionFlag = c_char #操作标志
AF_Delete = '0' #删除
AF_Modify = '3' #修改
TTradingRight = c_char #交易权限
TR_Allow = '0' #可以交易
TR_Forbidden = '2' #不能交易
TOrderSource = c_char #报单来源
OSRC_Participant = '0' #来自参与者
OSRC_Administrator = '1' #来自管理员
TTradeType = c_char #成交类型
TRDT_Common = '0' #普通成交
TRDT_OptionsExecution = '1' #期权执行
TRDT_OTC = '2' #OTC成交
TRDT_EFPDerived = '3' #期转现衍生成交
TRDT_CombinationDerived = '4' #组合衍生成交
TRDT_EFTPurchase = '5' #ETF申购
TRDT_EFTRedem = '6' #ETF赎回
TPriceSource = c_char #成交价来源
PSRC_LastPrice = '0' #前成交价
PSRC_Buy = '1' #买委托价
PSRC_Sell = '2' #卖委托价
TInstrumentStatus = c_char #合约交易状态
IS_BeforeTrading = '0' #开盘前
IS_NoTrading = '1' #非交易
IS_Continous = '2' #连续交易
IS_AuctionOrdering = '3' #集合竞价报单
IS_AuctionBalance = '4' #集合竞价价格平衡
IS_AuctionMatch = '5' #集合竞价撮合
IS_Closed = '6' #收盘
TInstStatusEnterReason = c_char #品种进入交易状态原因
IER_Automatic = '1' #自动切换
IER_Manual = '2' #手动切换
IER_Fuse = '3' #熔断
TOrderActionRef = c_int #报单操作引用
TInstallCount = c_int #安装数量
TInstallID = c_int #安装编号
TErrorID = c_int #错误代码
TSettlementID = c_int #结算编号
TVolume = c_int #数量
TFrontID = c_int #前置编号
TSessionID = c_int #会话编号
TSequenceNo = c_int #序号
TCommandNo = c_int #DB命令序号
TMillisec = c_int #时间（毫秒）
TVolumeMultiple = c_int #合约数量乘数
TTradingSegmentSN = c_int #交易阶段编号
TRequestID = c_int #请求编号
TYear = c_int #年份
TMonth = c_int #月份
TBool = c_int #布尔型
TPrice = c_double #价格
TCombOffsetFlag = c_char * 5 #组合开平标志
TCombHedgeFlag = c_char * 5 #组合投机套保标志
TRatio = c_double #比率
TMoney = c_double #资金
TLargeVolume = c_double #大额数量
TSequenceSeries = c_short #序列系列号
TCommPhaseNo = c_short #通讯时段编号
TSequenceLabel = c_char * 2 #序列编号
TPriority = c_int #优先级
TContractCode = c_char * 41 #合同编号
TCity = c_char * 41 #市
TIsStock = c_char * 11 #是否股民
TChannel = c_char * 51 #渠道
TAddress = c_char * 101 #通讯地址
TZipCode = c_char * 7 #邮政编码
TTelephone = c_char * 41 #联系电话
TFax = c_char * 41 #传真
TMobile = c_char * 41 #手机
TEMail = c_char * 41 #电子邮件
TMemo = c_char * 161 #备注
TCompanyCode = c_char * 51 #企业代码
TWebsite = c_char * 51 #网站地址
TTaxNo = c_char * 31 #税务登记号
TBatchStatus = c_char #处理状态
BS_NoUpload = '1' #未上传
BS_Uploaded = '2' #已上传
BS_Failed = '3' #审核失败
TPropertyID = c_char * 33 #属性代码
TPropertyName = c_char * 65 #属性名称
TLicenseNo = c_char * 51 #营业执照号
TAgentID = c_char * 13 #经纪人代码
TAgentName = c_char * 41 #经纪人名称
TAgentGroupID = c_char * 13 #经纪人组代码
TAgentGroupName = c_char * 41 #经纪人组名称
TReturnStyle = c_char #按品种返还方式
RS_All = '1' #按所有品种
RS_ByProduct = '2' #按品种
TReturnPattern = c_char #返还模式
RP_ByVolume = '1' #按成交手数
RP_ByFeeOnHand = '2' #按留存手续费
TReturnLevel = c_char #返还级别
RL_Level1 = '1' #级别1
RL_Level2 = '2' #级别2
RL_Level3 = '3' #级别3
RL_Level4 = '4' #级别4
RL_Level5 = '5' #级别5
RL_Level6 = '6' #级别6
RL_Level7 = '7' #级别7
RL_Level8 = '8' #级别8
RL_Level9 = '9' #级别9
TReturnStandard = c_char #返还标准
RSD_ByPeriod = '1' #分阶段返还
RSD_ByStandard = '2' #按某一标准
TMortgageType = c_char #质押类型
MT_Out = '0' #质出
MT_In = '1' #质入
TInvestorSettlementParamID = c_char #投资者结算参数代码
ISPI_BaseMargin = '1' #基础保证金
ISPI_LowestInterest = '2' #最低权益标准
ISPI_MortgageRatio = '4' #质押比例
ISPI_MarginWay = '5' #保证金算法
ISPI_BillDeposit = '9' #结算单(盯市)权益等于结存
TExchangeSettlementParamID = c_char #交易所结算参数代码
ESPI_MortgageRatio = '1' #质押比例
ESPI_OtherFundItem = '2' #分项资金导入项
ESPI_OtherFundImport = '3' #分项资金入交易所出入金
ESPI_SHFEDelivFee = '4' #上期所交割手续费收取方式
ESPI_DCEDelivFee = '5' #大商所交割手续费收取方式
ESPI_CFFEXMinPrepa = '6' #中金所开户最低可用金额
TSystemParamID = c_char #系统参数代码
SPI_InvestorIDMinLength = '1' #投资者代码最小长度
SPI_AccountIDMinLength = '2' #投资者帐号代码最小长度
SPI_UserRightLogon = '3' #投资者开户默认登录权限
SPI_SettlementBillTrade = '4' #投资者交易结算单成交汇总方式
SPI_TradingCode = '5' #统一开户更新交易编码方式
SPI_CheckFund = '6' #结算是否判断存在未复核的出入金和分项资金
SPI_UploadSettlementFile = 'U' #上传的结算文件标识
SPI_DownloadCSRCFile = 'D' #下载的保证金存管文件
SPI_SettlementBillFile = 'S' #结算单文件标识
SPI_CSRCOthersFile = 'C' #证监会文件标识
SPI_InvestorPhoto = 'P' #投资者照片路径
TTradeParamID = c_char #交易系统参数代码
TPID_EncryptionStandard = 'E' #系统加密算法
TPID_RiskMode = 'R' #系统风险算法
TPID_RiskModeGlobal = 'G' #系统风险算法是否全局 0-否 1-是
TSettlementParamValue = c_char * 256 #参数代码值
TCounterID = c_char * 33 #计数器代码
TInvestorGroupName = c_char * 41 #投资者分组名称
TBrandCode = c_char * 257 #牌号
TWarehouse = c_char * 257 #仓库
TProductDate = c_char * 41 #产期
TGrade = c_char * 41 #等级
TClassify = c_char * 41 #类别
TPosition = c_char * 41 #货位
TYieldly = c_char * 41 #产地
TWeight = c_char * 41 #公定重量
TSubEntryFundNo = c_int #分项资金流水号
TFileID = c_char #文件标识
FI_SettlementFund = 'F' #资金数据
FI_Trade = 'T' #成交数据
FI_InvestorPosition = 'P' #投资者持仓数据
FI_SubEntryFund = 'O' #投资者分项资金数据
TFileName = c_char * 257 #文件名称
TFileType = c_char #文件上传类型
FUT_Settlement = '0' #结算
FUT_Check = '1' #核对
TFileFormat = c_char #文件格式
FFT_Txt = '0' #文本文件(.txt)
FFT_Zip = '1' #压缩文件(.zip)
FFT_DBF = '2' #DBF文件(.dbf)
TFileUploadStatus = c_char #文件状态
FUS_SucceedUpload = '1' #上传成功
FUS_FailedUpload = '2' #上传失败
FUS_SucceedLoad = '3' #导入成功
FUS_PartSucceedLoad = '4' #导入部分成功
FUS_FailedLoad = '5' #导入失败
TTransferDirection = c_char #移仓方向
TD_Out = '0' #移出
TD_In = '1' #移入
TUploadMode = c_char * 21 #上传文件类型
TAccountID = c_char * 15 #投资者帐号
TBankFlag = c_char #银行统一标识类型
BF_ICBC = '1' #工商银行
BF_ABC = '2' #农业银行
BF_BC = '3' #中国银行
BF_CBC = '4' #建设银行
BF_BOC = '5' #交通银行
BF_Other = 'Z' #其他银行
TBankAccount = c_char * 41 #银行账户
TOpenName = c_char * 61 #银行账户的开户人名称
TOpenBank = c_char * 101 #银行账户的开户行
TBankName = c_char * 101 #银行名称
TPublishPath = c_char * 257 #发布路径
TOperatorID = c_char * 65 #操作员代码
TMonthCount = c_int #月份数量
TAdvanceMonthArray = c_char * 13 #月份提前数组
TDateExpr = c_char * 1025 #日期表达式
TInstrumentIDExpr = c_char * 41 #合约代码表达式
TInstrumentNameExpr = c_char * 41 #合约名称表达式
TSpecialCreateRule = c_char #特殊的创建规则
SC_NoSpecialRule = '0' #没有特殊创建规则
SC_NoSpringFestival = '1' #不包含春节
TBasisPriceType = c_char #挂牌基准价类型
IPT_LastSettlement = '1' #上一合约结算价
IPT_LaseClose = '2' #上一合约收盘价
TProductLifePhase = c_char #产品生命周期状态
PLP_Active = '1' #活跃
PLP_NonActive = '2' #不活跃
PLP_Canceled = '3' #注销
TDeliveryMode = c_char #交割方式
DM_CashDeliv = '1' #现金交割
DM_CommodityDeliv = '2' #实物交割
TLogLevel = c_char * 33 #日志级别
TProcessName = c_char * 257 #存储过程名称
TOperationMemo = c_char * 1025 #操作摘要
TFundIOType = c_char #出入金类型
FIOT_FundIO = '1' #出入金
FIOT_Transfer = '2' #银期转帐
TFundType = c_char #资金类型
FT_Deposite = '1' #银行存款
FT_ItemFund = '2' #分项资金
FT_Company = '3' #公司调整
TFundDirection = c_char #出入金方向
FD_In = '1' #入金
FD_Out = '2' #出金
TFundStatus = c_char #资金状态
FS_Record = '1' #已录入
FS_Check = '2' #已复核
FS_Charge = '3' #已冲销
TBillNo = c_char * 15 #票据号
TBillName = c_char * 33 #票据名称
TPublishStatus = c_char #发布状态
PS_None = '1' #未发布
PS_Publishing = '2' #正在发布
PS_Published = '3' #已发布
TEnumValueID = c_char * 65 #枚举值代码
TEnumValueType = c_char * 33 #枚举值类型
TEnumValueLabel = c_char * 65 #枚举值名称
TEnumValueResult = c_char * 33 #枚举值结果
TSystemStatus = c_char #系统状态
ES_NonActive = '1' #不活跃
ES_Startup = '2' #启动
ES_Initialize = '3' #交易开始初始化
ES_Initialized = '4' #交易完成初始化
ES_Close = '5' #收市开始
ES_Closed = '6' #收市完成
ES_Settlement = '7' #结算
TSettlementStatus = c_char #结算状态
STS_Initialize = '0' #初始
STS_Settlementing = '1' #结算中
STS_Settlemented = '2' #已结算
STS_Finished = '3' #结算完成
TRangeIntType = c_char * 33 #限定值类型
TRangeIntFrom = c_char * 33 #限定值下限
TRangeIntTo = c_char * 33 #限定值上限
TFunctionID = c_char * 25 #功能代码
TFunctionValueCode = c_char * 257 #功能编码
TFunctionName = c_char * 65 #功能名称
TRoleID = c_char * 11 #角色编号
TRoleName = c_char * 41 #角色名称
TDescription = c_char * 401 #描述
TCombineID = c_char * 25 #组合编号
TCombineType = c_char * 25 #组合类型
TInvestorType = c_char #投资者类型
CT_Person = '0' #自然人
CT_Company = '1' #法人
CT_Fund = '2' #投资基金
TBrokerType = c_char #经纪公司类型
BT_Trade = '0' #交易会员
BT_TradeSettle = '1' #交易结算会员
TRiskLevel = c_char #风险等级
FAS_Low = '1' #低风险客户
FAS_Normal = '2' #普通客户
FAS_Focus = '3' #关注客户
FAS_Risk = '4' #风险客户
TFeeAcceptStyle = c_char #手续费收取方式
FAS_ByTrade = '1' #按交易收取
FAS_ByDeliv = '2' #按交割收取
FAS_None = '3' #不收
FAS_FixFee = '4' #按指定手续费收取
TPasswordType = c_char #密码类型
PWDT_Trade = '1' #交易密码
PWDT_Account = '2' #资金密码
TAlgorithm = c_char #盈亏算法
AG_All = '1' #浮盈浮亏都计算
AG_OnlyLost = '2' #浮盈不计，浮亏计
AG_OnlyGain = '3' #浮盈计，浮亏不计
AG_None = '4' #浮盈浮亏都不计算
TIncludeCloseProfit = c_char #是否包含平仓盈利
ICP_Include = '0' #包含平仓盈利
ICP_NotInclude = '2' #不包含平仓盈利
TAllWithoutTrade = c_char #是否受可提比例限制
AWT_Enable = '0' #不受可提比例限制
AWT_Disable = '2' #受可提比例限制
TComment = c_char * 31 #盈亏算法说明
TVersion = c_char * 4 #版本号
TTradeCode = c_char * 7 #交易代码
TTradeDate = c_char * 9 #交易日期
TTradeTime = c_char * 9 #交易时间
TTradeSerial = c_char * 9 #发起方流水号
TTradeSerialNo = c_int #发起方流水号
TFutureID = c_char * 11 #期货公司代码
TBankID = c_char * 4 #银行代码
TBankBrchID = c_char * 5 #银行分中心代码
TBankBranchID = c_char * 11 #分中心代码
TOperNo = c_char * 17 #交易柜员
TDeviceID = c_char * 3 #渠道标志
TRecordNum = c_char * 7 #记录数
TFutureAccount = c_char * 22 #期货资金账号
TFuturePwdFlag = c_char #资金密码核对标志
FPWD_UnCheck = '0' #不核对
FPWD_Check = '1' #核对
TTransferType = c_char #银期转账类型
TT_BankToFuture = '0' #银行转期货
TT_FutureToBank = '1' #期货转银行
TFutureAccPwd = c_char * 17 #期货资金密码
TCurrencyCode = c_char * 4 #币种
TRetCode = c_char * 5 #响应代码
TRetInfo = c_char * 129 #响应信息
TTradeAmt = c_char * 20 #银行总余额
TUseAmt = c_char * 20 #银行可用余额
TFetchAmt = c_char * 20 #银行可取余额
TTransferValidFlag = c_char #转账有效标志
TVF_Invalid = '0' #无效或失败
TVF_Valid = '1' #有效
TVF_Reverse = '2' #冲正
TCertCode = c_char * 21 #证件号码
TReason = c_char #事由
RN_CD = '0' #错单
RN_ZT = '1' #资金在途
RN_QT = '2' #其它
TFundProjectID = c_char * 5 #资金项目编号
TSex = c_char #性别
SEX_None = '0' #未知
SEX_Man = '1' #男
SEX_Woman = '2' #女
TProfession = c_char * 41 #职业
TNational = c_char * 31 #国籍
TProvince = c_char * 16 #省
TRegion = c_char * 16 #区
TCountry = c_char * 16 #国家
TLicenseNO = c_char * 33 #营业执照
TCompanyType = c_char * 16 #企业性质
TBusinessScope = c_char * 1001 #经营范围
TCapitalCurrency = c_char * 4 #注册资本币种
TUserType = c_char #用户类型
UT_Investor = '0' #投资者
UT_Operator = '1' #操作员
UT_SuperUser = '2' #管理员
TRateType = c_char #费率类型
RATETYPE_MarginRate = '2' #保证金率
RATETYPE_CommRate = '1' #手续费率
RATETYPE_AllRate = '0' #所有
TNoteType = c_char #通知类型
NOTETYPE_TradeSettleBill = '1' #交易结算单
NOTETYPE_TradeSettleMonth = '2' #交易结算月报
NOTETYPE_CallMarginNotes = '3' #追加保证金通知书
NOTETYPE_ForceCloseNotes = '4' #强行平仓通知书
NOTETYPE_TradeNotes = '5' #成交通知书
NOTETYPE_DelivNotes = '6' #交割通知书
TSettlementStyle = c_char #结算单方式
SBS_Day = '1' #逐日盯市
SBS_Volume = '2' #逐笔对冲
TBrokerDNS = c_char * 256 #域名
TSentence = c_char * 501 #语句
TSettlementBillType = c_char #结算单类型
ST_Day = '0' #日报
ST_Month = '1' #月报
TUserRightType = c_char #客户权限类型
URT_Logon = '1' #登录
URT_Transfer = '2' #银期转帐
URT_EMail = '3' #邮寄结算单
URT_Fax = '4' #传真结算单
URT_ConditionOrder = '5' #条件单
TMarginPriceType = c_char #保证金价格类型
MPT_PreSettlementPrice = '1' #昨结算价
MPT_SettlementPrice = '2' #最新价
MPT_AveragePrice = '3' #成交均价
MPT_OpenPrice = '4' #开仓价
TBillGenStatus = c_char #结算单生成状态
BGS_None = '0' #不生成
BGS_NoGenerated = '1' #未生成
BGS_Generated = '2' #已生成
TAlgoType = c_char #算法类型
AT_HandlePositionAlgo = '1' #持仓处理算法
AT_FindMarginRateAlgo = '2' #寻找保证金率算法
THandlePositionAlgoID = c_char #持仓处理算法编号
HPA_Base = '1' #基本
HPA_DCE = '2' #大连商品交易所
HPA_CZCE = '3' #郑州商品交易所
HPA_NoneTrade = '4' #非交易
HPA_Stock = '5' #证券
TFindMarginRateAlgoID = c_char #寻找保证金率算法编号
FMRA_Base = '1' #基本
FMRA_DCE = '2' #大连商品交易所
FMRA_CZCE = '3' #郑州商品交易所
THandleTradingAccountAlgoID = c_char #资金处理算法编号
HTAA_Base = '1' #基本
HTAA_DCE = '2' #大连商品交易所
HTAA_CZCE = '3' #郑州商品交易所
TPersonType = c_char #联系人类型
PST_Order = '1' #指定下单人
PST_Open = '2' #开户授权人
PST_Fund = '3' #资金调拨人
PST_Settlement = '4' #结算单确认人
TQueryInvestorRange = c_char #查询范围
QIR_All = '1' #所有
QIR_Group = '2' #查询分类
QIR_Single = '3' #单一投资者
TInvestorRiskStatus = c_char #投资者风险状态
IRS_Normal = '1' #正常
IRS_Warn = '2' #警告
IRS_Call = '3' #追保
IRS_Force = '4' #强平
IRS_Exception = '5' #异常
TLegID = c_int #单腿编号
TLegMultiple = c_int #单腿乘数
TImplyLevel = c_int #派生层数
TClearAccount = c_char * 33 #结算账户
TOrganNO = c_char * 6 #结算账户
TClearbarchID = c_char * 6 #结算账户联行号
TUserEventType = c_char #用户事件类型
UET_All = ' ' #所有
UET_Login = '1' #登录
UET_Logout = '2' #登出
UET_Trading = '3' #交易成功
UET_TradingError = '4' #交易失败
UET_UpdatePassword = '5' #修改密码
UET_Other = '9' #其他
TUserEventInfo = c_char * 1025 #用户事件信息
TCloseStyle = c_char #平仓方式
ICS_Close = '0' #先开先平
ICS_CloseToday = '1' #先平今再平昨
TStatMode = c_char #统计方式
SM_Non = '0' #----
SM_Instrument = '1' #按合约统计
SM_Product = '2' #按产品统计
SM_Investor = '3' #按投资者统计
TParkedOrderStatus = c_char #预埋单状态
PAOS_NotSend = '1' #未发送
PAOS_Send = '2' #已发送
PAOS_Deleted = '3' #已删除
TParkedOrderID = c_char * 13 #预埋报单编号
TParkedOrderActionID = c_char * 13 #预埋撤单编号
TVirDealStatus = c_char #处理状态
VDS_Dealing = '1' #正在处理
VDS_DeaclSucceed = '2' #处理成功
TOrgSystemID = c_char #原有系统代码
ORGS_Standard = '0' #综合交易平台
ORGS_ESunny = '1' #易盛系统
ORGS_KingStarV6 = '2' #金仕达V6系统
TVirTradeStatus = c_char #交易状态
VTS_NaturalDeal = '0' #正常处理中
VTS_SucceedEnd = '1' #成功结束
VTS_FailedEND = '2' #失败结束
VTS_Exception = '3' #异常中
VTS_ManualDeal = '4' #已人工异常处理
VTS_MesException = '5' #通讯异常 ，请人工处理
VTS_SysException = '6' #系统出错，请人工处理
TVirBankAccType = c_char #银行帐户类型
VBAT_BankBook = '1' #存折
VBAT_BankCard = '2' #储蓄卡
VBAT_CreditCard = '3' #信用卡
TVirementStatus = c_char #银行帐户类型
VMS_Natural = '0' #正常
VMS_Canceled = '9' #销户
TVirementAvailAbility = c_char #有效标志
VAA_NoAvailAbility = '0' #未确认
VAA_AvailAbility = '1' #有效
VAA_Repeal = '2' #冲正
TVirementTradeCode = c_char #交易代码
VTC_BankBankToFuture = '102001' #银行发起银行资金转期货
VTC_BankFutureToBank = '102002' #银行发起期货资金转银行
VTC_FutureBankToFuture = '202001' #期货发起银行资金转期货
VTC_FutureFutureToBank = '202002' #期货发起期货资金转银行
TPhotoTypeName = c_char * 41 #影像类型名称
TPhotoTypeID = c_char * 5 #影像类型代码
TPhotoName = c_char * 161 #影像名称
TTopicID = c_int #主题代码
TReportTypeID = c_char * 3 #交易报告类型标识
TCharacterID = c_char * 5 #交易特征代码
TAMLParamID = c_char * 21 #参数代码
TAMLInvestorType = c_char * 3 #投资者类型
TAMLIdCardType = c_char * 3 #证件类型
TAMLTradeDirect = c_char * 3 #资金进出方向
TAMLTradeModel = c_char * 3 #资金进出方式
TAMLParamID = c_char * 21 #参数代码
TAMLOpParamValue = c_double #业务参数代码值
TAMLCustomerCardType = c_char * 81 #客户身份证件/证明文件类型
TAMLInstitutionName = c_char * 65 #金融机构网点名称
TAMLDistrictID = c_char * 7 #金融机构网点所在地区行政区划代码
TAMLRelationShip = c_char * 3 #金融机构网点与大额交易的关系
TAMLInstitutionType = c_char * 3 #金融机构网点代码类型
TAMLInstitutionID = c_char * 13 #金融机构网点代码
TAMLAccountType = c_char * 5 #账户类型
TAMLTradingType = c_char * 7 #交易方式
TAMLTransactClass = c_char * 7 #涉外收支交易分类与代码
TAMLCapitalIO = c_char * 3 #资金收付标识
TAMLSite = c_char * 10 #交易地点
TAMLCapitalPurpose = c_char * 129 #资金用途
TAMLReportType = c_char * 2 #报文类型
TAMLSerialNo = c_char * 5 #编号
TAMLStatus = c_char * 2 #状态
TAMLGenStatus = c_char * 2 #状态
TAMLSeqCode = c_char * 65 #业务标识号
TAMLFileName = c_char * 257 #AML文件名
TAMLMoney = c_double #反洗钱资金
TAMLFileAmount = c_int #反洗钱资金
TCFMMCKey = c_char * 21 #密钥类型(保证金监管)
TCFMMCKeyKind = c_char #动态密钥类别(保证金监管)
CFMMCKK_REQUEST = 'R' #主动请求更新
CFMMCKK_AUTO = 'A' #CFMMC自动更新
CFMMCKK_MANUAL = 'M' #CFMMC手动更新
TIndividualName = c_char * 51 #个人姓名
TCurrencyID = c_char * 4 #币种代码
TCustNumber = c_char * 36 #客户编号
TOrganCode = c_char * 36 #机构编码
TOrganName = c_char * 71 #机构名称
TSuperOrganCode = c_char * 12 #上级机构编码,即期货公司总部、银行总行
TSubBranchID = c_char * 31 #分支机构
TSubBranchName = c_char * 71 #分支机构名称
TBranchNetCode = c_char * 31 #机构网点号
TBranchNetName = c_char * 71 #机构网点名称
TOrganFlag = c_char * 2 #机构标识
TBankCodingForFuture = c_char * 33 #银行对期货公司的编码
TBankReturnCode = c_char * 7 #银行对返回码的定义
TPlateReturnCode = c_char * 5 #银期转帐平台对返回码的定义
TBankSubBranchID = c_char * 31 #银行分支机构编码
TFutureBranchID = c_char * 31 #期货分支机构编码
TReturnCode = c_char * 7 #返回代码
TOperatorCode = c_char * 17 #操作员
TClearDepID = c_char * 6 #机构结算帐户机构号
TClearBrchID = c_char * 6 #机构结算帐户联行号
TClearName = c_char * 71 #机构结算帐户名称
TBankAccountName = c_char * 71 #银行帐户名称
TInvDepID = c_char * 6 #机构投资人账号机构号
TInvBrchID = c_char * 6 #机构投资人联行号
TMessageFormatVersion = c_char * 36 #信息格式版本
TDigest = c_char * 36 #摘要
TAuthenticData = c_char * 129 #认证数据
TPasswordKey = c_char * 129 #密钥
TFutureAccountName = c_char * 129 #期货帐户名称
TMobilePhone = c_char * 21 #手机
TFutureMainKey = c_char * 129 #期货公司主密钥
TFutureWorkKey = c_char * 129 #期货公司工作密钥
TFutureTransKey = c_char * 129 #期货公司传输密钥
TBankMainKey = c_char * 129 #银行主密钥
TBankWorkKey = c_char * 129 #银行工作密钥
TBankTransKey = c_char * 129 #银行传输密钥
TBankServerDescription = c_char * 129 #银行服务器描述信息
TAddInfo = c_char * 129 #附加信息
TDescrInfoForReturnCode = c_char * 129 #返回码描述
TCountryCode = c_char * 21 #国家代码
TSerial = c_int #流水号
TPlateSerial = c_int #平台流水号
TBankSerial = c_char * 13 #银行流水号
TCorrectSerial = c_int #被冲正交易流水号
TFutureSerial = c_int #期货公司流水号
TApplicationID = c_int #应用标识
TBankProxyID = c_int #银行代理标识
TFBTCoreID = c_int #银期转帐核心系统标识
TServerPort = c_int #服务端口号
TRepealedTimes = c_int #已经冲正次数
TRepealTimeInterval = c_int #冲正时间间隔
TTotalTimes = c_int #每日累计转帐次数
TFBTRequestID = c_int #请求ID
TTID = c_int #交易ID
TTradeAmount = c_double #交易金额（元）
TCustFee = c_double #应收客户费用（元）
TFutureFee = c_double #应收期货公司费用（元）
TSingleMaxAmt = c_double #单笔最高限额
TSingleMinAmt = c_double #单笔最低限额
TTotalAmt = c_double #每日累计转帐额度
TCertificationType = c_char #证件类型
CFT_IDCard = '0' #身份证
CFT_Passport = '1' #护照
CFT_OfficerIDCard = '2' #军官证
CFT_SoldierIDCard = '3' #士兵证
CFT_HomeComingCard = '4' #回乡证
CFT_HouseholdRegister = '5' #户口簿
CFT_LicenseNo = '6' #营业执照号
CFT_InstitutionCodeCard = '7' #组织机构代码证
CFT_TempLicenseNo = '8' #临时营业执照号
CFT_NoEnterpriseLicenseNo = '9' #民办非企业登记证书
CFT_OtherCard = 'x' #其他证件
CFT_SuperDepAgree = 'a' #主管部门批文
TFileBusinessCode = c_char #文件业务功能
FBC_Others = '0' #其他
FBC_TransferDetails = '1' #转账交易明细对账
FBC_CustAccStatus = '2' #客户账户状态对账
FBC_AccountTradeDetails = '3' #账户类交易明细对账
FBC_FutureAccountChangeInfoDetails = '4' #期货账户信息变更明细对账
FBC_CustMoneyDetail = '5' #客户资金台账余额明细对账
FBC_CustCancelAccountInfo = '6' #客户销户结息明细对账
FBC_CustMoneyResult = '7' #客户资金余额对账结果
FBC_OthersExceptionResult = '8' #其它对账异常结果文件
FBC_CustInterestNetMoneyDetails = '9' #客户结息净额明细
FBC_CustMoneySendAndReceiveDetails = 'a' #客户资金交收明细
FBC_CorporationMoneyTotal = 'b' #法人存管银行资金交收汇总
FBC_MainbodyMoneyTotal = 'c' #主体间资金交收汇总
FBC_MainPartMonitorData = 'd' #总分平衡监管数据
FBC_PreparationMoney = 'e' #存管银行备付金余额
FBC_BankMoneyMonitorData = 'f' #协办存管银行资金监管数据
TCashExchangeCode = c_char #汇钞标志
CEC_Exchange = '1' #汇
CEC_Cash = '2' #钞
TYesNoIndicator = c_char #是或否标识
YNI_Yes = '0' #是
YNI_No = '1' #否
TBanlanceType = c_char #余额类型
BLT_CurrentMoney = '0' #当前余额
BLT_UsableMoney = '1' #可用余额
BLT_FetchableMoney = '2' #可取余额
BLT_FreezeMoney = '3' #冻结余额
TGender = c_char #性别
GD_Unknown = '0' #未知状态
GD_Male = '1' #男
GD_Female = '2' #女
TFeePayFlag = c_char #费用支付标志
FPF_BEN = '0' #由受益方支付费用
FPF_OUR = '1' #由发送方支付费用
FPF_SHA = '2' #由发送方支付发起的费用，受益方支付接受的费用
TPassWordKeyType = c_char #密钥类型
PWKT_ExchangeKey = '0' #交换密钥
PWKT_PassWordKey = '1' #密码密钥
PWKT_MACKey = '2' #MAC密钥
PWKT_MessageKey = '3' #报文密钥
TFBTPassWordType = c_char #密码类型
PWT_Query = '0' #查询
PWT_Fetch = '1' #取款
PWT_Transfer = '2' #转帐
PWT_Trade = '3' #交易
TFBTEncryMode = c_char #加密方式
EM_NoEncry = '0' #不加密
EM_DES = '1' #DES
EM_3DES = '2' #3DES
TBankRepealFlag = c_char #银行冲正标志
BRF_BankNotNeedRepeal = '0' #银行无需自动冲正
BRF_BankWaitingRepeal = '1' #银行待自动冲正
BRF_BankBeenRepealed = '2' #银行已自动冲正
TBrokerRepealFlag = c_char #期商冲正标志
BRORF_BrokerNotNeedRepeal = '0' #期商无需自动冲正
BRORF_BrokerWaitingRepeal = '1' #期商待自动冲正
BRORF_BrokerBeenRepealed = '2' #期商已自动冲正
TInstitutionType = c_char #机构类别
TS_Bank = '0' #银行
TS_Future = '1' #期商
TS_Store = '2' #券商
TLastFragment = c_char #最后分片标志
LF_Yes = '0' #是最后分片
LF_No = '1' #不是最后分片
TBankAccStatus = c_char #银行账户状态
BAS_Normal = '0' #正常
BAS_Freeze = '1' #冻结
BAS_ReportLoss = '2' #挂失
TMoneyAccountStatus = c_char #资金账户状态
MAS_Normal = '0' #正常
MAS_Cancel = '1' #销户
TManageStatus = c_char #存管状态
MSS_Point = '0' #指定存管
MSS_PrePoint = '1' #预指定
MSS_CancelPoint = '2' #撤销指定
TSystemType = c_char #应用系统类型
SYT_FutureBankTransfer = '0' #银期转帐
SYT_StockBankTransfer = '1' #银证转帐
SYT_TheThirdPartStore = '2' #第三方存管
TTxnEndFlag = c_char #银期转帐划转结果标志
TEF_NormalProcessing = '0' #正常处理中
TEF_Success = '1' #成功结束
TEF_Failed = '2' #失败结束
TEF_Abnormal = '3' #异常中
TEF_ManualProcessedForException = '4' #已人工异常处理
TEF_CommuFailedNeedManualProcess = '5' #通讯异常 ，请人工处理
TEF_SysErrorNeedManualProcess = '6' #系统出错，请人工处理
TProcessStatus = c_char #银期转帐服务处理状态
PSS_NotProcess = '0' #未处理
PSS_StartProcess = '1' #开始处理
PSS_Finished = '2' #处理完成
TCustType = c_char #客户类型
CUSTT_Person = '0' #自然人
CUSTT_Institution = '1' #机构户
TFBTTransferDirection = c_char #银期转帐方向
FBTTD_FromBankToFuture = '1' #入金，银行转期货
FBTTD_FromFutureToBank = '2' #出金，期货转银行
TOpenOrDestroy = c_char #开销户类别
OOD_Open = '1' #开户
OOD_Destroy = '0' #销户
TAvailabilityFlag = c_char #有效标志
AVAF_Invalid = '0' #未确认
AVAF_Valid = '1' #有效
AVAF_Repeal = '2' #冲正
TOrganType = c_char #机构类型
OT_Bank = '1' #银行代理
OT_Future = '2' #交易前置
OT_PlateForm = '9' #银期转帐平台管理
TOrganLevel = c_char #机构级别
OL_HeadQuarters = '1' #银行总行或期商总部
OL_Branch = '2' #银行分中心或期货公司营业部
TProtocalID = c_char #协议类型
PID_FutureProtocal = '0' #期商协议
PID_ICBCProtocal = '1' #工行协议
PID_ABCProtocal = '2' #农行协议
PID_CBCProtocal = '3' #中国银行协议
PID_CCBProtocal = '4' #建行协议
PID_BOCOMProtocal = '5' #交行协议
PID_FBTPlateFormProtocal = 'X' #银期转帐平台协议
TConnectMode = c_char #套接字连接方式
CM_ShortConnect = '0' #短连接
CM_LongConnect = '1' #长连接
TSyncMode = c_char #套接字通信方式
SRM_ASync = '0' #异步
SRM_Sync = '1' #同步
TBankAccType = c_char #银行帐号类型
BAT_BankBook = '1' #银行存折
BAT_SavingCard = '2' #储蓄卡
BAT_CreditCard = '3' #信用卡
TFutureAccType = c_char #期货公司帐号类型
FAT_BankBook = '1' #银行存折
FAT_SavingCard = '2' #储蓄卡
FAT_CreditCard = '3' #信用卡
TOrganStatus = c_char #接入机构状态
OS_Ready = '0' #启用
OS_CheckIn = '1' #签到
OS_CheckOut = '2' #签退
OS_CheckFileArrived = '3' #对帐文件到达
OS_CheckDetail = '4' #对帐
OS_DayEndClean = '5' #日终清理
OS_Invalid = '9' #注销
TCCBFeeMode = c_char #建行收费模式
CCBFM_ByAmount = '1' #按金额扣收
CCBFM_ByMonth = '2' #按月扣收
TCommApiType = c_char #通讯API类型
CAPIT_Client = '1' #客户端
CAPIT_Server = '2' #服务端
CAPIT_UserApi = '3' #交易系统的UserApi
TServiceID = c_int #服务编号
TServiceLineNo = c_int #服务线路编号
TServiceName = c_char * 61 #服务名
TLinkStatus = c_char #连接状态
LS_Connected = '1' #已经连接
LS_Disconnected = '2' #没有连接
TCommApiPointer = c_int #通讯API指针
TPwdFlag = c_char #密码核对标志
BPWDF_NoCheck = '0' #不核对
BPWDF_BlankCheck = '1' #明文核对
BPWDF_EncryptCheck = '2' #密文核对
TSecuAccType = c_char #期货帐号类型
SAT_AccountID = '1' #资金帐号
SAT_CardID = '2' #资金卡号
SAT_SHStockholderID = '3' #上海股东帐号
SAT_SZStockholderID = '4' #深圳股东帐号
TTransferStatus = c_char #转账交易状态
TRFS_Normal = '0' #正常
TRFS_Repealed = '1' #被冲正
TSponsorType = c_char #发起方
SPTYPE_Broker = '0' #期商
SPTYPE_Bank = '1' #银行
TReqRspType = c_char #请求响应类别
REQRSP_Request = '0' #请求
REQRSP_Response = '1' #响应
TFBTUserEventType = c_char #银期转帐用户事件类型
FBTUET_SignIn = '0' #签到
FBTUET_FromBankToFuture = '1' #银行转期货
FBTUET_FromFutureToBank = '2' #期货转银行
FBTUET_OpenAccount = '3' #开户
FBTUET_CancelAccount = '4' #销户
FBTUET_ChangeAccount = '5' #变更银行账户
FBTUET_RepealFromBankToFuture = '6' #冲正银行转期货
FBTUET_RepealFromFutureToBank = '7' #冲正期货转银行
FBTUET_QueryBankAccount = '8' #查询银行账户
FBTUET_QueryFutureAccount = '9' #查询期货账户
FBTUET_SignOut = 'A' #签退
FBTUET_SyncKey = 'B' #密钥同步
FBTUET_Other = 'Z' #其他
TBankIDByBank = c_char * 21 #银行自己的编码
TNotifyClass = c_char #风险通知类型
NC_NOERROR = '0' #正常
NC_Warn = '1' #警示
NC_Call = '2' #追保
NC_Force = '3' #强平
NC_CHUANCANG = '4' #穿仓
NC_Exception = '5' #异常
TRiskNofityInfo = c_char * 257 #客户风险通知消息
TForceCloseSceneId = c_char * 24 #强平场景编号
TForceCloseType = c_char #强平单类型
FCT_Manual = '0' #手工强平
FCT_Single = '1' #单一投资者辅助强平
FCT_Group = '2' #批量投资者辅助强平
TInstrumentIDs = c_char * 101 #多个产品代码,用+分隔,如cu+zn
TRiskNotifyMethod = c_char #风险通知途径
RNM_System = '0' #系统通知
RNM_SMS = '1' #短信通知
RNM_EMail = '2' #邮件通知
TRiskNotifyStatus = c_char #风险通知状态
RNS_NotGen = '0' #未生成
RNS_Generated = '1' #已生成未发送
RNS_SendError = '2' #发送失败
RNS_SendOk = '3' #已发送未接收
RNS_Received = '4' #已接收未确认
RNS_Confirmed = '5' #已确认
TRiskUserEvent = c_char #风控用户操作事件
RUE_ExportData = '0' #导出数据
TConditionalOrderSortType = c_char #条件单索引条件
COST_LastPriceAsc = '0' #使用最新价升序
COST_LastPriceDesc = '1' #使用最新价降序
COST_AskPriceAsc = '2' #使用卖价升序
COST_AskPriceDesc = '3' #使用卖价降序
COST_BidPriceAsc = '4' #使用买价升序
COST_BidPriceDesc = '5' #使用买价降序
TSendType = c_char #报送状态
UOAST_NoSend = '0' #未发送
UOAST_Sended = '1' #已发送
UOAST_Generated = '2' #已生成
UOAST_SendFail = '3' #报送失败
UOAST_Success = '4' #接收成功
UOAST_Fail = '5' #接收失败
UOAST_Cancel = '6' #取消报送
TClientIDStatus = c_char #交易编码状态
UOACS_NoApply = '1' #未申请
UOACS_Submited = '2' #已提交申请
UOACS_Sended = '3' #已发送申请
UOACS_Success = '4' #完成
UOACS_Refuse = '5' #拒绝
UOACS_Cancel = '6' #已撤销编码
TIndustryID = c_char * 17 #行业编码
TQuestionID = c_char * 5 #特有信息编号
TQuestionContent = c_char * 41 #特有信息说明
TOptionID = c_char * 13 #选项编号
TOptionContent = c_char * 61 #选项说明
TQuestionType = c_char #特有信息类型
QT_Radio = '1' #单选
QT_Option = '2' #多选
QT_Blank = '3' #填空
TProcessID = c_char * 33 #业务流水号
TSeqNo = c_int #流水号
TUOAProcessStatus = c_char * 3 #流程状态
TProcessType = c_char #流程功能类型
PT_ApplyTradingCode = '1' #申请交易编码
PT_CancelTradingCode = '2' #撤销交易编码
PT_ModifyIDCard = '3' #修改身份信息
PT_ModifyNoIDCard = '4' #修改一般信息
PT_ExchOpenBak = '5' #交易所开户报备
PT_ExchCancelBak = '6' #交易所销户报备
TBusinessType = c_char #业务类型
BT_Request = '1' #请求
BT_Response = '2' #应答
BT_Notice = '3' #通知
TCfmmcReturnCode = c_char #监控中心返回码
CRC_Success = '0' #成功
CRC_Working = '1' #该客户已经有流程在处理中
CRC_InfoFail = '2' #监控中客户资料检查失败
CRC_IDCardFail = '3' #监控中实名制检查失败
CRC_OtherFail = '4' #其他错误
TExReturnCode = c_int #交易所返回码
TClientType = c_char #客户类型
CfMMCCT_All = '0' #所有
CfMMCCT_Person = '1' #个人
CfMMCCT_Company = '2' #单位
TExchangeIDType = c_char #交易所编号
EIDT_SHFE = 'S' #上海期货交易所
EIDT_CZCE = 'Z' #郑州商品交易所
EIDT_DCE = 'D' #大连商品交易所
EIDT_CFFEX = 'J' #中国金融期货交易所
TExClientIDType = c_char #交易编码类型
ECIDT_Hedge = '1' #套保
ECIDT_Arbitrage = '2' #套利
ECIDT_Speculation = '3' #投机
TClientClassify = c_char * 11 #客户分类码
TUOAOrganType = c_char * 9 #单位性质
TUOACountryCode = c_char * 9 #国家代码
TAreaCode = c_char * 9 #区号
TFuturesID = c_char * 21 #监控中心为客户分配的代码
TCffmcDate = c_char * 11 #日期
TCffmcTime = c_char * 11 #时间
TNocID = c_char * 21 #组织机构代码
TUpdateFlag = c_char #更新状态
UF_NoUpdate = '0' #未更新
UF_Success = '1' #更新全部信息成功
UF_Fail = '2' #更新全部信息失败
UF_TCSuccess = '3' #更新交易编码成功
UF_TCFail = '4' #更新交易编码失败
UF_Cancel = '5' #已丢弃
TApplyOperateID = c_char #申请动作
AOID_OpenInvestor = '1' #开户
AOID_ModifyIDCard = '2' #修改身份信息
AOID_ModifyNoIDCard = '3' #修改一般信息
AOID_ApplyTradingCode = '4' #申请交易编码
AOID_CancelTradingCode = '5' #撤销交易编码
AOID_CancelInvestor = '6' #销户
TApplyStatusID = c_char #申请状态
ASID_NoComplete = '1' #未补全
ASID_Submited = '2' #已提交
ASID_Checked = '3' #已审核
ASID_Refused = '4' #已拒绝
ASID_Deleted = '5' #已删除
TSendMethod = c_char #发送方式
UOASM_ByAPI = '1' #电子发送
UOASM_ByFile = '2' #文件发送
TEventType = c_char * 33 #业务操作类型
TEventMode = c_char #操作方法
EvM_ADD = '1' #增加
EvM_UPDATE = '2' #修改
EvM_DELETE = '3' #删除
EvM_CHECK = '4' #复核
TUOAAutoSend = c_char #统一开户申请自动发送
UOAA_ASR = '1' #自动发送并接收
UOAA_ASNR = '2' #自动发送，不自动接收
UOAA_NSAR = '3' #不自动发送，自动接收
UOAA_NSR = '4' #不自动发送，也不自动接收
TQueryDepth = c_int #查询深度
TDataCenterID = c_int #数据中心代码
TFlowID = c_char #流程ID
EvM_InvestorGroupFlow = '1' #投资者对应投资者组设置
TCheckLevel = c_char #复核级别
CL_Zero = '0' #零级复核
CL_One = '1' #一级复核
CL_Two = '2' #二级复核
TCheckNo = c_int #操作次数
TCheckStatus = c_char #复核级别
CHS_Init = '0' #未复核
CHS_Checking = '1' #复核中
CHS_Checked = '2' #已复核
CHS_Refuse = '3' #拒绝
CHS_Cancel = '4' #作废
TUsedStatus = c_char #生效状态
CHU_Unused = '0' #未生效
CHU_Used = '1' #已生效
CHU_Fail = '2' #生效失败
TRateTemplateName = c_char * 61 #模型名称
TPropertyString = c_char * 2049 #用于查询的投资属性字段
TBankAcountOrigin = c_char #账户来源
BAO_ByAccProperty = '0' #手工录入
BAO_ByFBTransfer = '1' #银期转账
TMonthBillTradeSum = c_char #结算单月报成交汇总方式
MBTS_ByInstrument = '0' #同日同合约
MBTS_ByDayInsPrc = '1' #同日同合约同价格
MBTS_ByDayIns = '2' #同合约
TFBTTradeCodeEnum = c_char #银期交易代码枚举
FTC_BankLaunchBankToBroker = '102001' #银行发起银行转期货
FTC_BrokerLaunchBankToBroker = '202001' #期货发起银行转期货
FTC_BankLaunchBrokerToBank = '102002' #银行发起期货转银行
FTC_BrokerLaunchBrokerToBank = '202002' #期货发起期货转银行
TRateTemplateID = c_char * 9 #模型代码
TRiskRate = c_char * 21 #风险度
TTimestamp = c_int #时间戳
TInvestorIDRuleName = c_char * 61 #号段规则名称
TInvestorIDRuleExpr = c_char * 513 #号段规则表达式
TLastDrift = c_int #上次OTP漂移值
TLastSuccess = c_int #上次OTP成功值
TAuthKey = c_char * 41 #令牌密钥
TSerialNumber = c_char * 17 #序列号
TOTPType = c_char #动态令牌类型
OTP_NONE = '0' #无动态令牌
OTP_TOTP = '1' #时间令牌
TOTPVendorsID = c_char * 2 #动态令牌提供商
TOTPVendorsName = c_char * 61 #动态令牌提供商名称
TOTPStatus = c_char #动态令牌状态
OTPS_Unused = '0' #未使用
OTPS_Used = '1' #已使用
OTPS_Disuse = '2' #注销
TBrokerUserType = c_char #经济公司用户类型
BUT_Investor = '1' #投资者
TFutureType = c_char #期货类型
FUTT_Commodity = '1' #商品期货
FUTT_Financial = '2' #金融期货
TFundEventType = c_char #资金管理操作类型
FET_Restriction = '0' #转账限额
FET_TodayRestriction = '1' #当日转账限额
FET_Transfer = '2' #期商流水
FET_Credit = '3' #资金冻结
FET_InvestorWithdrawAlm = '4' #投资者可提资金比例
TAccountSourceType = c_char #资金账户来源
AST_FBTransfer = '0' #银期同步
AST_ManualEntry = '1' #手工录入
TCodeSourceType = c_char #交易编码来源
CST_UnifyAccount = '0' #统一开户
CST_ManualEntry = '1' #手工录入
TUserRange = c_char #操作员范围
UR_All = '0' #所有
UR_Single = '1' #单一操作员
TTimeSpan = c_char * 9 #时间跨度
TImportSequenceID = c_char * 17 #动态令牌导入批次编号
TBranchID = c_char * 9 #营业部编号
TTableName = c_char * 17 #和交易所交换表编号
TStockPrice = c_char * 9 #证券交易价格
TStockTradeType = c_char #证券交易类型
STT_Stock = '0' #可交易证券
STT_BuyNetService = '1' #买入网络密码服务
STT_CancelRepurchase = '2' #回购注销
STT_CancelRegister = '3' #指定撤销
STT_Register = '4' #指定登记
STT_PurchaseIssue = '5' #买入发行申购
STT_Allotment = '6' #卖出配股
STT_SellTender = '7' #卖出要约收购
STT_BuyTender = '8' #买入要约收购
STT_NetVote = '9' #网上投票
STT_SellConvertibleBonds = 'a' #卖出可转债回售
STT_OptionExecute = 'b' #权证行权代码
STT_PurchaseOF = 'c' #开放式基金申购
STT_RedeemOF = 'd' #开放式基金赎回
STT_SubscribeOF = 'e' #开放式基金认购
STT_OFCustodianTranfer = 'f' #开放式基金转托管转出
STT_OFDividendConfig = 'g' #开放式基金分红设置
STT_OFTransfer = 'h' #开放式基金转成其他基金
STT_BondsIn = 'i' #债券入库
STT_BondsOut = 'j' #债券出库
STT_PurchaseETF = 'k' #EFT申购
STT_RedeemETF = 'l' #EFT赎回
STT_ConvertibleRegister = 'm' #可转债回售登记
TStockSeq = c_char * 11 #股票使用流水号
TStockWth = c_int #股票使用流水号
TWTFS = c_int #委托方式
TWTLB = c_int #委托类别
TWTRQ = c_int #委托日期
TCreationredemptionStatus = c_char #基金当天申购赎回状态
CDS_Forbidden = '0' #不允许申购赎回
CDS_Allow = '1' #表示允许申购和赎回
CDS_OnlyPurchase = '2' #允许申购、不允许赎回
CDS_OnlyRedeem = '3' #不允许申购、允许赎回
TETFCurrenceReplaceStatus = c_char #ETF现金替代标志
ETFCRS_Forbidden = '0' #禁止现金替代
ETFCRS_Allow = '1' #可以现金替代
ETFCRS_Force = '2' #必须现金替代
TINTEGER = c_int #一般整型
TINT3 = c_int #三位数整型
TINT6 = c_int #六位数整型
TREAL9P3 = c_double #九点三实型
TREAL10P4 = c_double #十点四实型
TREAL16P2 = c_double #十六点二实型
TREAL16P8 = c_double #十六点八实型
TREAL22P2 = c_double #二十二点二实型
TCHAR1 = c_char * 2 #一字节CHAR
TCHAR2 = c_char * 3 #二字节CHAR
TCHAR3 = c_char * 4 #三字节CHAR
TCHAR4 = c_char * 5 #四字节CHAR
TCHAR5 = c_char * 6 #五字节CHAR
TCHAR6 = c_char * 7 #六字节CHAR
TCHAR8 = c_char * 9 #八字节CHAR
TCHAR10 = c_char * 11 #十字节CHAR
TCHAR12 = c_char * 13 #十二字节CHAR
TCHAR13 = c_char * 14 #十三字节CHAR
TCHAR14 = c_char * 15 #十四字节CHAR
TCHAR16 = c_char * 17 #十六字节CHAR
TVCHAR4 = c_char * 5 #四字节VCHAR
TVCHAR6 = c_char * 7 #六字节VCHAR
TVCHAR8 = c_char * 9 #八字节VCHAR
TVCHAR10 = c_char * 11 #十字节VCHAR
TVCHAR12 = c_char * 13 #十二字节VCHAR
TVCHAR16 = c_char * 17 #十六字节VCHAR
TVCHAR20 = c_char * 21 #二十字节VCHAR
TVCHAR30 = c_char * 31 #三十字节VCHAR
TVCHAR50 = c_char * 51 #五十字节VCHAR
TVCHAR60 = c_char * 61 #六十字节VCHAR
TVCHAR65 = c_char * 66 #六十五字节VCHAR
TVCHAR80 = c_char * 81 #八十字节VCHAR
TVCHAR255 = c_char * 256 #二五五字节VCHAR
TAuthInfo = c_char * 129 #客户端认证信息
TAuthCode = c_char * 17 #客户端认证码

class Dissemination(BaseStruct): #信息分发
    _fields_ = (
        ('SequenceSeries', TSequenceSeries), #序列系列号, short
        ('SequenceNo', TSequenceNo), #序列号, int
    )
class ReqUserLogin(BaseStruct): #用户登录请求
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('Password', TPassword), #密码, char[41]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('InterfaceProductInfo', TProductInfo), #接口端产品信息, char[11]
        ('ProtocolInfo', TProtocolInfo), #协议信息, char[11]
        ('MacAddress', TMacAddress), #Mac地址, char[21]
        ('OneTimePassword', TPassword), #动态密码, char[41]
        ('ClientIPAddress', TIPAddress), #终端IP地址, char[16]
    )
class RspUserLogin(BaseStruct): #用户登录应答
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('LoginTime', TTime), #登录成功时间, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('SystemName', TSystemName), #交易系统名称, char[41]
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('MaxOrderRef', TOrderRef), #最大报单引用, char[13]
        ('SHFETime', TTime), #上期所时间, char[9]
        ('DCETime', TTime), #大商所时间, char[9]
        ('CZCETime', TTime), #郑商所时间, char[9]
        ('FFEXTime', TTime), #中金所时间, char[9]
    )
class UserLogout(BaseStruct): #用户登出请求
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
    )
class ForceUserLogout(BaseStruct): #强制交易员退出
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
    )
class ReqAuthenticate(BaseStruct): #客户端认证请求
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('AuthCode', TAuthCode), #认证码, char[17]
    )
class RspAuthenticate(BaseStruct): #客户端认证响应
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
    )
class AuthenticationInfo(BaseStruct): #客户端认证信息
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('AuthInfo', TAuthInfo), #认证信息, char[129]
        ('IsResult', TBool), #是否为认证结果, int
    )
class TransferHeader(BaseStruct): #银期转帐报文头
    _fields_ = (
        ('Version', TVersion), #版本号，常量，1.0, char[4]
        ('TradeCode', TTradeCode), #交易代码，必填, char[7]
        ('TradeDate', TTradeDate), #交易日期，必填，格式：yyyymmdd, char[9]
        ('TradeTime', TTradeTime), #交易时间，必填，格式：hhmmss, char[9]
        ('TradeSerial', TTradeSerial), #发起方流水号，N/A, char[9]
        ('FutureID', TFutureID), #期货公司代码，必填, char[11]
        ('BankID', TBankID), #银行代码，根据查询银行得到，必填, char[4]
        ('BankBrchID', TBankBrchID), #银行分中心代码，根据查询银行得到，必填, char[5]
        ('OperNo', TOperNo), #操作员，N/A, char[17]
        ('DeviceID', TDeviceID), #交易设备类型，N/A, char[3]
        ('RecordNum', TRecordNum), #记录数，N/A, char[7]
        ('SessionID', TSessionID), #会话编号，N/A, int
        ('RequestID', TRequestID), #请求编号，N/A, int
    )
class TransferBankToFutureReq(BaseStruct): #银行资金转期货请求，TradeCode=202001
    _fields_ = (
        ('FutureAccount', TAccountID), #期货资金账户, char[15]
        ('FuturePwdFlag', TFuturePwdFlag), #密码标志, char
        ('FutureAccPwd', TFutureAccPwd), #密码, char[17]
        ('TradeAmt', TMoney), #转账金额, double
        ('CustFee', TMoney), #客户手续费, double
        ('CurrencyCode', TCurrencyCode), #币种：RMB-人民币 USD-美圆 HKD-港元, char[4]
    )
class TransferBankToFutureRsp(BaseStruct): #银行资金转期货请求响应
    _fields_ = (
        ('RetCode', TRetCode), #响应代码, char[5]
        ('RetInfo', TRetInfo), #响应信息, char[129]
        ('FutureAccount', TAccountID), #资金账户, char[15]
        ('TradeAmt', TMoney), #转帐金额, double
        ('CustFee', TMoney), #应收客户手续费, double
        ('CurrencyCode', TCurrencyCode), #币种, char[4]
    )
class TransferFutureToBankReq(BaseStruct): #期货资金转银行请求，TradeCode=202002
    _fields_ = (
        ('FutureAccount', TAccountID), #期货资金账户, char[15]
        ('FuturePwdFlag', TFuturePwdFlag), #密码标志, char
        ('FutureAccPwd', TFutureAccPwd), #密码, char[17]
        ('TradeAmt', TMoney), #转账金额, double
        ('CustFee', TMoney), #客户手续费, double
        ('CurrencyCode', TCurrencyCode), #币种：RMB-人民币 USD-美圆 HKD-港元, char[4]
    )
class TransferFutureToBankRsp(BaseStruct): #期货资金转银行请求响应
    _fields_ = (
        ('RetCode', TRetCode), #响应代码, char[5]
        ('RetInfo', TRetInfo), #响应信息, char[129]
        ('FutureAccount', TAccountID), #资金账户, char[15]
        ('TradeAmt', TMoney), #转帐金额, double
        ('CustFee', TMoney), #应收客户手续费, double
        ('CurrencyCode', TCurrencyCode), #币种, char[4]
    )
class TransferQryBankReq(BaseStruct): #查询银行资金请求，TradeCode=204002
    _fields_ = (
        ('FutureAccount', TAccountID), #期货资金账户, char[15]
        ('FuturePwdFlag', TFuturePwdFlag), #密码标志, char
        ('FutureAccPwd', TFutureAccPwd), #密码, char[17]
        ('CurrencyCode', TCurrencyCode), #币种：RMB-人民币 USD-美圆 HKD-港元, char[4]
    )
class TransferQryBankRsp(BaseStruct): #查询银行资金请求响应
    _fields_ = (
        ('RetCode', TRetCode), #响应代码, char[5]
        ('RetInfo', TRetInfo), #响应信息, char[129]
        ('FutureAccount', TAccountID), #资金账户, char[15]
        ('TradeAmt', TMoney), #银行余额, double
        ('UseAmt', TMoney), #银行可用余额, double
        ('FetchAmt', TMoney), #银行可取余额, double
        ('CurrencyCode', TCurrencyCode), #币种, char[4]
    )
class TransferQryDetailReq(BaseStruct): #查询银行交易明细请求，TradeCode=204999
    _fields_ = (
        ('FutureAccount', TAccountID), #期货资金账户, char[15]
    )
class TransferQryDetailRsp(BaseStruct): #查询银行交易明细请求响应
    _fields_ = (
        ('TradeDate', TDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('TradeCode', TTradeCode), #交易代码, char[7]
        ('FutureSerial', TTradeSerialNo), #期货流水号, int
        ('FutureID', TFutureID), #期货公司代码, char[11]
        ('FutureAccount', TFutureAccount), #资金帐号, char[22]
        ('BankSerial', TTradeSerialNo), #银行流水号, int
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBrchID', TBankBrchID), #银行分中心代码, char[5]
        ('BankAccount', TBankAccount), #银行账号, char[41]
        ('CertCode', TCertCode), #证件号码, char[21]
        ('CurrencyCode', TCurrencyCode), #货币代码, char[4]
        ('TxAmount', TMoney), #发生金额, double
        ('Flag', TTransferValidFlag), #有效标志, char
    )
class RspInfo(BaseStruct): #响应信息
    _fields_ = (
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class Exchange(BaseStruct): #交易所
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ExchangeName', TExchangeName), #交易所名称, char[31]
        ('ExchangeProperty', TExchangeProperty), #交易所属性, char
    )
class Product(BaseStruct): #产品
    _fields_ = (
        ('ProductID', TInstrumentID), #产品代码, char[31]
        ('ProductName', TProductName), #产品名称, char[21]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ProductClass', TProductClass), #产品类型, char
        ('VolumeMultiple', TVolumeMultiple), #合约数量乘数, int
        ('PriceTick', TPrice), #最小变动价位, double
        ('MaxMarketOrderVolume', TVolume), #市价单最大下单量, int
        ('MinMarketOrderVolume', TVolume), #市价单最小下单量, int
        ('MaxLimitOrderVolume', TVolume), #限价单最大下单量, int
        ('MinLimitOrderVolume', TVolume), #限价单最小下单量, int
        ('PositionType', TPositionType), #持仓类型, char
        ('PositionDateType', TPositionDateType), #持仓日期类型, char
        ('EFTMinTradeVolume', TVolume), #ETF最小交易单位, int
    )
class Instrument(BaseStruct): #合约
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('InstrumentName', TInstrumentName), #合约名称, char[21]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('ProductID', TInstrumentID), #产品代码, char[31]
        ('ProductClass', TProductClass), #产品类型, char
        ('DeliveryYear', TYear), #交割年份, int
        ('DeliveryMonth', TMonth), #交割月, int
        ('MaxMarketOrderVolume', TVolume), #市价单最大下单量, int
        ('MinMarketOrderVolume', TVolume), #市价单最小下单量, int
        ('MaxLimitOrderVolume', TVolume), #限价单最大下单量, int
        ('MinLimitOrderVolume', TVolume), #限价单最小下单量, int
        ('VolumeMultiple', TVolumeMultiple), #合约数量乘数, int
        ('PriceTick', TPrice), #最小变动价位, double
        ('CreateDate', TDate), #创建日, char[9]
        ('OpenDate', TDate), #上市日, char[9]
        ('ExpireDate', TDate), #到期日, char[9]
        ('StartDelivDate', TDate), #开始交割日, char[9]
        ('EndDelivDate', TDate), #结束交割日, char[9]
        ('InstLifePhase', TInstLifePhase), #合约生命周期状态, char
        ('IsTrading', TBool), #当前是否交易, int
        ('PositionType', TPositionType), #持仓类型, char
        ('PositionDateType', TPositionDateType), #持仓日期类型, char
        ('LongMarginRatio', TRatio), #多头保证金率, double
        ('ShortMarginRatio', TRatio), #空头保证金率, double
        ('OrderCanBeWithdraw', TBool), #报单能否撤单, int
        ('MinBuyVolume', TVolume), #最小买下单单位, int
        ('MinSellVolume', TVolume), #最小卖下单单位, int
    )
class Broker(BaseStruct): #经纪公司
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('BrokerAbbr', TBrokerAbbr), #经纪公司简称, char[9]
        ('BrokerName', TBrokerName), #经纪公司名称, char[81]
        ('IsActive', TBool), #是否活跃, int
    )
class Trader(BaseStruct): #交易所交易员
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('Password', TPassword), #密码, char[41]
        ('InstallCount', TInstallCount), #安装数量, int
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('BranchID', TBranchID), #营业部编号, char[9]
    )
class Investor(BaseStruct): #投资者
    _fields_ = (
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorGroupID', TInvestorID), #投资者分组代码, char[15]
        ('InvestorName', TPartyName), #投资者名称, char[81]
        ('IdentifiedCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('IsActive', TBool), #是否活跃, int
        ('Telephone', TTelephone), #联系电话, char[41]
        ('Address', TAddress), #通讯地址, char[101]
        ('OpenDate', TDate), #开户日期, char[9]
        ('Mobile', TMobile), #手机, char[41]
        ('SHBranchID', TBranchID), #上海营业部编号, char[9]
        ('SZBranchID', TBranchID), #深圳营业部编号, char[9]
        ('IsCreditAccount', TBool), #是否信用账户, int
    )
class TradingCode(BaseStruct): #交易编码
    _fields_ = (
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ClientID', TClientID), #客户代码, char[11]
        ('IsActive', TBool), #是否活跃, int
    )
class PartBroker(BaseStruct): #会员编码和经纪公司编码对照表
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('IsActive', TBool), #是否活跃, int
    )
class SuperUser(BaseStruct): #管理用户
    _fields_ = (
        ('UserID', TUserID), #用户代码, char[16]
        ('UserName', TUserName), #用户名称, char[81]
        ('Password', TPassword), #密码, char[41]
        ('IsActive', TBool), #是否活跃, int
    )
class SuperUserFunction(BaseStruct): #管理用户功能权限
    _fields_ = (
        ('UserID', TUserID), #用户代码, char[16]
        ('FunctionCode', TFunctionCode), #功能代码, char
    )
class InvestorGroup(BaseStruct): #投资者组
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorGroupID', TInvestorID), #投资者分组代码, char[15]
        ('InvestorGroupName', TInvestorGroupName), #投资者分组名称, char[41]
    )
class TradingAccount(BaseStruct): #资金账户
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('PreMortgage', TMoney), #上次质押金额, double
        ('PreCredit', TMoney), #上次信用额度, double
        ('PreDeposit', TMoney), #上次存款额, double
        ('PreBalance', TMoney), #上次结算准备金, double
        ('PreMargin', TMoney), #上次占用的保证金, double
        ('InterestBase', TMoney), #利息基数, double
        ('Interest', TMoney), #利息收入, double
        ('Deposit', TMoney), #入金金额, double
        ('Withdraw', TMoney), #出金金额, double
        ('FrozenMargin', TMoney), #冻结的保证金, double
        ('FrozenCash', TMoney), #冻结的资金, double
        ('FrozenCommission', TMoney), #冻结的手续费, double
        ('CurrMargin', TMoney), #当前保证金总额, double
        ('CashIn', TMoney), #资金差额, double
        ('Commission', TMoney), #手续费, double
        ('CloseProfit', TMoney), #平仓盈亏, double
        ('PositionProfit', TMoney), #持仓盈亏, double
        ('Balance', TMoney), #期货结算准备金, double
        ('Available', TMoney), #可用资金, double
        ('WithdrawQuota', TMoney), #可取资金, double
        ('Reserve', TMoney), #基本准备金, double
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('Credit', TMoney), #信用额度, double
        ('Mortgage', TMoney), #质押金额, double
        ('ExchangeMargin', TMoney), #交易所保证金, double
        ('DeliveryMargin', TMoney), #投资者交割保证金, double
        ('ExchangeDeliveryMargin', TMoney), #交易所交割保证金, double
        ('FrozenTransferFee', TMoney), #冻结的过户费, double
        ('FrozenStampTax', TMoney), #冻结的印花税, double
        ('TransferFee', TMoney), #过户费, double
        ('StampTax', TMoney), #印花税, double
        ('ConversionAmount', TMoney), #折算金额, double
        ('CreditAmount', TMoney), #授信额度, double
        ('LowLimitRatio', TRatio), #最低维持担保比例, double
        ('MarginTradingAmount', TMoney), #融资买入金额, double
        ('ShortSellingAmount', TMoney), #融券卖出金额, double
        ('MarginTradingAvail', TMoney), #融资买入可用金额, double
        ('ShortSellingAvail', TMoney), #融券卖出可用金额, double
        ('CreditRatio', TRatio), #维持担保比例, double
        ('StockValue', TMoney), #证券总价值, double
    )
class InvestorPosition(BaseStruct): #投资者持仓
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('PosiDirection', TPosiDirection), #持仓多空方向, char
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('PositionDate', TPositionDate), #持仓日期, char
        ('YdPosition', TVolume), #上日持仓, int
        ('Position', TVolume), #今日持仓, int
        ('LongFrozen', TVolume), #多头冻结, int
        ('ShortFrozen', TVolume), #空头冻结, int
        ('LongFrozenAmount', TMoney), #开仓冻结金额, double
        ('ShortFrozenAmount', TMoney), #开仓冻结金额, double
        ('OpenVolume', TVolume), #开仓量, int
        ('CloseVolume', TVolume), #平仓量, int
        ('OpenAmount', TMoney), #开仓金额, double
        ('CloseAmount', TMoney), #平仓金额, double
        ('PositionCost', TMoney), #持仓成本, double
        ('FrozenCash', TMoney), #冻结的资金, double
        ('CashIn', TMoney), #资金差额, double
        ('Commission', TMoney), #手续费, double
        ('CloseProfit', TMoney), #平仓盈亏, double
        ('PositionProfit', TMoney), #持仓盈亏, double
        ('PreSettlementPrice', TPrice), #上次结算价, double
        ('SettlementPrice', TPrice), #本次结算价, double
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('OpenCost', TMoney), #开仓成本, double
        ('ExchangeMargin', TMoney), #交易所保证金, double
        ('TodayPosition', TVolume), #今日持仓, int
        ('TransferFee', TMoney), #过户费, double
        ('StampTax', TMoney), #印花税, double
        ('TodayPurRedVolume', TVolume), #今日申购赎回数量, int
        ('ConversionRate', TRatio), #折算率, double
        ('ConversionAmount', TMoney), #折算金额, double
        ('MarginTradeVolume', TVolume), #融资买入出数量, int
        ('MarginTradeAmount', TMoney), #融资买入金额, double
        ('MarginTradeFrozenVolume', TVolume), #融资买入冻结数量, int
        ('MarginTradeFrozenAmount', TMoney), #融资买入冻结金额, double
        ('MarginTradeConversionAmount', TMoney), #融资买入折算金额, double
        ('ShortSellVolume', TVolume), #融券卖出数量, int
        ('ShortSellAmount', TMoney), #融券卖出金额, double
        ('ShortSellConversionAmount', TMoney), #融券卖出折算金额, double
        ('ShortSellFrozenVolume', TVolume), #融券卖出冻结数量, int
        ('ShortSellFrozenAmount', TMoney), #融券卖出冻结金额, double
        ('StockValue', TMoney), #证券价值, double
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class InstrumentMarginRate(BaseStruct): #合约保证金率
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('LongMarginRatioByMoney', TRatio), #多头保证金率, double
        ('LongMarginRatioByVolume', TMoney), #多头保证金费, double
        ('ShortMarginRatioByMoney', TRatio), #空头保证金率, double
        ('ShortMarginRatioByVolume', TMoney), #空头保证金费, double
        ('IsRelative', TBool), #是否相对交易所收取, int
    )
class InstrumentCommissionRate(BaseStruct): #合约手续费率
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('BuyStampTaxRateByMoney', TRatio), #买印花税率, double
        ('BuyStampTaxRateByVolume', TRatio), #买印花税率(按手数), double
        ('SellStampTaxRateByMoney', TRatio), #卖印花税率, double
        ('SellStampTaxRateByVolume', TRatio), #卖印花税率(按手数), double
        ('BuyTransferFeeRateByMoney', TRatio), #买过户费率, double
        ('BuyTransferFeeRateByVolume', TRatio), #买过户费率(按手数), double
        ('SellTransferFeeRateByMoney', TRatio), #卖过户费率, double
        ('SellTransferFeeRateByVolume', TRatio), #卖过户费率(按手数), double
        ('BuyTradeFeeByMoney', TRatio), #买交易费, double
        ('BuyTradeFeeByVolume', TRatio), #买交易费(按手数), double
        ('SellTradeFeeByMoney', TRatio), #卖交易费率, double
        ('SellTradeFeeByVolume', TRatio), #卖交易费率(按手数), double
        ('BuyMarginByMoney', TRatio), #买交易附加费率, double
        ('SellMarginByMoney', TRatio), #卖交易附加费率, double
        ('MinTradeFee', TPrice), #最小过户费, double
    )
class DepthMarketData(BaseStruct): #深度行情
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('LastPrice', TPrice), #最新价, double
        ('PreSettlementPrice', TPrice), #上次结算价, double
        ('PreClosePrice', TPrice), #昨收盘, double
        ('PreOpenInterest', TLargeVolume), #昨持仓量, double
        ('OpenPrice', TPrice), #今开盘, double
        ('HighestPrice', TPrice), #最高价, double
        ('LowestPrice', TPrice), #最低价, double
        ('Volume', TVolume), #数量, int
        ('Turnover', TMoney), #成交金额, double
        ('OpenInterest', TLargeVolume), #持仓量, double
        ('ClosePrice', TPrice), #今收盘, double
        ('SettlementPrice', TPrice), #本次结算价, double
        ('UpperLimitPrice', TPrice), #涨停板价, double
        ('LowerLimitPrice', TPrice), #跌停板价, double
        ('PreDelta', TRatio), #昨虚实度, double
        ('CurrDelta', TRatio), #今虚实度, double
        ('UpdateTime', TTime), #最后修改时间, char[9]
        ('UpdateMillisec', TMillisec), #最后修改毫秒, int
        ('BidPrice1', TPrice), #申买价一, double
        ('BidVolume1', TVolume), #申买量一, int
        ('AskPrice1', TPrice), #申卖价一, double
        ('AskVolume1', TVolume), #申卖量一, int
        ('BidPrice2', TPrice), #申买价二, double
        ('BidVolume2', TVolume), #申买量二, int
        ('AskPrice2', TPrice), #申卖价二, double
        ('AskVolume2', TVolume), #申卖量二, int
        ('BidPrice3', TPrice), #申买价三, double
        ('BidVolume3', TVolume), #申买量三, int
        ('AskPrice3', TPrice), #申卖价三, double
        ('AskVolume3', TVolume), #申卖量三, int
        ('BidPrice4', TPrice), #申买价四, double
        ('BidVolume4', TVolume), #申买量四, int
        ('AskPrice4', TPrice), #申卖价四, double
        ('AskVolume4', TVolume), #申卖量四, int
        ('BidPrice5', TPrice), #申买价五, double
        ('BidVolume5', TVolume), #申买量五, int
        ('AskPrice5', TPrice), #申卖价五, double
        ('AskVolume5', TVolume), #申卖量五, int
        ('AveragePrice', TPrice), #当日均价, double
    )
class InstrumentTradingRight(BaseStruct): #投资者合约交易权限
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('Direction', TDirection), #买卖, char
        ('TradingRight', TTradingRight), #交易权限, char
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class BrokerUser(BaseStruct): #经纪公司用户
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserName', TUserName), #用户名称, char[81]
        ('UserType', TUserType), #用户类型, char
        ('IsActive', TBool), #是否活跃, int
        ('IsUsingOTP', TBool), #是否使用令牌, int
    )
class BrokerUserPassword(BaseStruct): #经纪公司用户口令
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('Password', TPassword), #密码, char[41]
    )
class BrokerUserFunction(BaseStruct): #经纪公司用户功能权限
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('BrokerFunctionCode', TBrokerFunctionCode), #经纪公司功能代码, char
    )
class TraderOffer(BaseStruct): #交易所交易员报盘机
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('Password', TPassword), #密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('TraderConnectStatus', TTraderConnectStatus), #交易所交易员连接状态, char
        ('ConnectRequestDate', TDate), #发出连接请求的日期, char[9]
        ('ConnectRequestTime', TTime), #发出连接请求的时间, char[9]
        ('LastReportDate', TDate), #上次报告日期, char[9]
        ('LastReportTime', TTime), #上次报告时间, char[9]
        ('ConnectDate', TDate), #完成连接日期, char[9]
        ('ConnectTime', TTime), #完成连接时间, char[9]
        ('StartDate', TDate), #启动日期, char[9]
        ('StartTime', TTime), #启动时间, char[9]
        ('TradingDay', TDate), #交易日, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('BranchID', TBranchID), #营业部编号, char[9]
    )
class SettlementInfo(BaseStruct): #投资者结算结果
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('SequenceNo', TSequenceNo), #序号, int
        ('Content', TContent), #消息正文, char[501]
    )
class InstrumentMarginRateAdjust(BaseStruct): #合约保证金率调整
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('LongMarginRatioByMoney', TRatio), #多头保证金率, double
        ('LongMarginRatioByVolume', TMoney), #多头保证金费, double
        ('ShortMarginRatioByMoney', TRatio), #空头保证金率, double
        ('ShortMarginRatioByVolume', TMoney), #空头保证金费, double
        ('IsRelative', TBool), #是否相对交易所收取, int
    )
class ExchangeMarginRate(BaseStruct): #交易所保证金率
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('LongMarginRatioByMoney', TRatio), #多头保证金率, double
        ('LongMarginRatioByVolume', TMoney), #多头保证金费, double
        ('ShortMarginRatioByMoney', TRatio), #空头保证金率, double
        ('ShortMarginRatioByVolume', TMoney), #空头保证金费, double
    )
class ExchangeMarginRateAdjust(BaseStruct): #交易所保证金率调整
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('LongMarginRatioByMoney', TRatio), #跟随交易所投资者多头保证金率, double
        ('LongMarginRatioByVolume', TMoney), #跟随交易所投资者多头保证金费, double
        ('ShortMarginRatioByMoney', TRatio), #跟随交易所投资者空头保证金率, double
        ('ShortMarginRatioByVolume', TMoney), #跟随交易所投资者空头保证金费, double
        ('ExchLongMarginRatioByMoney', TRatio), #交易所多头保证金率, double
        ('ExchLongMarginRatioByVolume', TMoney), #交易所多头保证金费, double
        ('ExchShortMarginRatioByMoney', TRatio), #交易所空头保证金率, double
        ('ExchShortMarginRatioByVolume', TMoney), #交易所空头保证金费, double
        ('NoLongMarginRatioByMoney', TRatio), #不跟随交易所投资者多头保证金率, double
        ('NoLongMarginRatioByVolume', TMoney), #不跟随交易所投资者多头保证金费, double
        ('NoShortMarginRatioByMoney', TRatio), #不跟随交易所投资者空头保证金率, double
        ('NoShortMarginRatioByVolume', TMoney), #不跟随交易所投资者空头保证金费, double
    )
class SettlementRef(BaseStruct): #结算引用
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
    )
class CurrentTime(BaseStruct): #当前时间
    _fields_ = (
        ('CurrDate', TDate), #当前日期, char[9]
        ('CurrTime', TTime), #当前时间, char[9]
        ('CurrMillisec', TMillisec), #当前时间（毫秒）, int
    )
class CommPhase(BaseStruct): #通讯阶段
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('CommPhaseNo', TCommPhaseNo), #通讯时段编号, short
    )
class LoginInfo(BaseStruct): #登录信息
    _fields_ = (
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('LoginDate', TDate), #登录日期, char[9]
        ('LoginTime', TTime), #登录时间, char[9]
        ('IPAddress', TIPAddress), #IP地址, char[16]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('InterfaceProductInfo', TProductInfo), #接口端产品信息, char[11]
        ('ProtocolInfo', TProtocolInfo), #协议信息, char[11]
        ('SystemName', TSystemName), #系统名称, char[41]
        ('Password', TPassword), #密码, char[41]
        ('MaxOrderRef', TOrderRef), #最大报单引用, char[13]
        ('MacAddress', TMacAddress), #Mac地址, char[21]
        ('OneTimePassword', TPassword), #动态密码, char[41]
    )
class LogoutAll(BaseStruct): #登录信息
    _fields_ = (
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('SystemName', TSystemName), #系统名称, char[41]
    )
class FrontStatus(BaseStruct): #前置状态
    _fields_ = (
        ('FrontID', TFrontID), #前置编号, int
        ('LastReportDate', TDate), #上次报告日期, char[9]
        ('LastReportTime', TTime), #上次报告时间, char[9]
        ('IsActive', TBool), #是否活跃, int
    )
class UserPasswordUpdate(BaseStruct): #用户口令变更
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('OldPassword', TPassword), #原来的口令, char[41]
        ('NewPassword', TPassword), #新的口令, char[41]
    )
class InputOrder(BaseStruct): #输入报单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('UserID', TUserID), #用户代码, char[16]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderPriceType', TOrderPriceType), #报单价格条件, char
        ('Direction', TDirection), #买卖方向, char
        ('CombOffsetFlag', TCombOffsetFlag), #组合开平标志, char[5]
        ('CombHedgeFlag', TCombHedgeFlag), #组合投机套保标志, char[5]
        ('LimitPrice', TStockPrice), #价格, char[9]
        ('VolumeTotalOriginal', TVolume), #数量, int
        ('TimeCondition', TTimeCondition), #有效期类型, char
        ('GTDDate', TDate), #GTD日期, char[9]
        ('VolumeCondition', TVolumeCondition), #成交量类型, char
        ('MinVolume', TVolume), #最小成交量, int
        ('ContingentCondition', TContingentCondition), #触发条件, char
        ('StopPrice', TPrice), #止损价, double
        ('ForceCloseReason', TForceCloseReason), #强平原因, char
        ('IsAutoSuspend', TBool), #自动挂起标志, int
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('RequestID', TRequestID), #请求编号, int
        ('UserForceClose', TBool), #用户强评标志, int
    )
class Order(BaseStruct): #报单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('UserID', TUserID), #用户代码, char[16]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderPriceType', TOrderPriceType), #报单价格条件, char
        ('Direction', TDirection), #买卖方向, char
        ('CombOffsetFlag', TCombOffsetFlag), #组合开平标志, char[5]
        ('CombHedgeFlag', TCombHedgeFlag), #组合投机套保标志, char[5]
        ('LimitPrice', TStockPrice), #价格, char[9]
        ('VolumeTotalOriginal', TVolume), #数量, int
        ('TimeCondition', TTimeCondition), #有效期类型, char
        ('GTDDate', TDate), #GTD日期, char[9]
        ('VolumeCondition', TVolumeCondition), #成交量类型, char
        ('MinVolume', TVolume), #最小成交量, int
        ('ContingentCondition', TContingentCondition), #触发条件, char
        ('StopPrice', TPrice), #止损价, double
        ('ForceCloseReason', TForceCloseReason), #强平原因, char
        ('IsAutoSuspend', TBool), #自动挂起标志, int
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('RequestID', TRequestID), #请求编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderSubmitStatus', TOrderSubmitStatus), #报单提交状态, char
        ('NotifySequence', TSequenceNo), #报单提示序号, int
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('OrderSysID', TOrderSysID), #报单编号, char[21]
        ('OrderSource', TOrderSource), #报单来源, char
        ('OrderStatus', TOrderStatus), #报单状态, char
        ('OrderType', TOrderType), #报单类型, char
        ('VolumeTraded', TVolume), #今成交数量, int
        ('VolumeTotal', TVolume), #剩余数量, int
        ('InsertDate', TDate), #报单日期, char[9]
        ('InsertTime', TTime), #委托时间, char[9]
        ('ActiveTime', TTime), #激活时间, char[9]
        ('SuspendTime', TTime), #挂起时间, char[9]
        ('UpdateTime', TTime), #最后修改时间, char[9]
        ('CancelTime', TTime), #撤销时间, char[9]
        ('ActiveTraderID', TTraderID), #最后修改交易所交易员代码, char[21]
        ('ClearingPartID', TParticipantID), #结算会员编号, char[11]
        ('SequenceNo', TSequenceNo), #序号, int
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('StatusMsg', TErrorMsg), #状态信息, char[81]
        ('UserForceClose', TBool), #用户强评标志, int
        ('ActiveUserID', TUserID), #操作用户代码, char[16]
        ('BrokerOrderSeq', TSequenceNo), #经纪公司报单编号, int
        ('RelativeOrderSysID', TOrderSysID), #相关报单, char[21]
        ('BranchID', TBranchID), #营业部编号, char[9]
        ('TradeAmount', TMoney), #成交数量, double
        ('IsETF', TBool), #是否ETF, int
        ('AccountID', TAccountID), #资金帐号, char[15]
    )
class ExchangeOrder(BaseStruct): #交易所报单
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderPriceType', TOrderPriceType), #报单价格条件, char
        ('Direction', TDirection), #买卖方向, char
        ('CombOffsetFlag', TCombOffsetFlag), #组合开平标志, char[5]
        ('CombHedgeFlag', TCombHedgeFlag), #组合投机套保标志, char[5]
        ('LimitPrice', TStockPrice), #价格, char[9]
        ('VolumeTotalOriginal', TVolume), #数量, int
        ('TimeCondition', TTimeCondition), #有效期类型, char
        ('GTDDate', TDate), #GTD日期, char[9]
        ('VolumeCondition', TVolumeCondition), #成交量类型, char
        ('MinVolume', TVolume), #最小成交量, int
        ('ContingentCondition', TContingentCondition), #触发条件, char
        ('StopPrice', TPrice), #止损价, double
        ('ForceCloseReason', TForceCloseReason), #强平原因, char
        ('IsAutoSuspend', TBool), #自动挂起标志, int
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('RequestID', TRequestID), #请求编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderSubmitStatus', TOrderSubmitStatus), #报单提交状态, char
        ('NotifySequence', TSequenceNo), #报单提示序号, int
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('OrderSysID', TOrderSysID), #报单编号, char[21]
        ('OrderSource', TOrderSource), #报单来源, char
        ('OrderStatus', TOrderStatus), #报单状态, char
        ('OrderType', TOrderType), #报单类型, char
        ('VolumeTraded', TVolume), #今成交数量, int
        ('VolumeTotal', TVolume), #剩余数量, int
        ('InsertDate', TDate), #报单日期, char[9]
        ('InsertTime', TTime), #委托时间, char[9]
        ('ActiveTime', TTime), #激活时间, char[9]
        ('SuspendTime', TTime), #挂起时间, char[9]
        ('UpdateTime', TTime), #最后修改时间, char[9]
        ('CancelTime', TTime), #撤销时间, char[9]
        ('ActiveTraderID', TTraderID), #最后修改交易所交易员代码, char[21]
        ('ClearingPartID', TParticipantID), #结算会员编号, char[11]
        ('SequenceNo', TSequenceNo), #序号, int
        ('BranchID', TBranchID), #营业部编号, char[9]
    )
class ExchangeOrderInsertError(BaseStruct): #交易所报单插入失败
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class InputOrderAction(BaseStruct): #输入报单操作
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('OrderActionRef', TOrderActionRef), #报单操作引用, int
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('RequestID', TRequestID), #请求编号, int
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ActionFlag', TActionFlag), #操作标志, char
        ('LimitPrice', TPrice), #价格, double
        ('VolumeChange', TVolume), #数量变化, int
        ('UserID', TUserID), #用户代码, char[16]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
    )
class OrderAction(BaseStruct): #报单操作
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('OrderActionRef', TOrderActionRef), #报单操作引用, int
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('RequestID', TRequestID), #请求编号, int
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ActionFlag', TActionFlag), #操作标志, char
        ('LimitPrice', TPrice), #价格, double
        ('VolumeChange', TVolume), #数量变化, int
        ('ActionDate', TDate), #操作日期, char[9]
        ('ActionTime', TTime), #操作时间, char[9]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ActionLocalID', TOrderLocalID), #操作本地编号, char[13]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('OrderActionStatus', TOrderActionStatus), #报单操作状态, char
        ('UserID', TUserID), #用户代码, char[16]
        ('BranchID', TBranchID), #营业部编号, char[9]
        ('StatusMsg', TErrorMsg), #状态信息, char[81]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
    )
class ExchangeOrderAction(BaseStruct): #交易所报单操作
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ActionFlag', TActionFlag), #操作标志, char
        ('LimitPrice', TPrice), #价格, double
        ('VolumeChange', TVolume), #数量变化, int
        ('ActionDate', TDate), #操作日期, char[9]
        ('ActionTime', TTime), #操作时间, char[9]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ActionLocalID', TOrderLocalID), #操作本地编号, char[13]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('OrderActionStatus', TOrderActionStatus), #报单操作状态, char
        ('UserID', TUserID), #用户代码, char[16]
        ('BranchID', TBranchID), #营业部编号, char[9]
    )
class ExchangeOrderActionError(BaseStruct): #交易所报单操作失败
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderSysID', TOrderSysID), #报单编号, char[21]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ActionLocalID', TOrderLocalID), #操作本地编号, char[13]
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class ExchangeTrade(BaseStruct): #交易所成交
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('TradeID', TTradeID), #成交编号, char[21]
        ('Direction', TDirection), #买卖方向, char
        ('OrderSysID', TOrderSysID), #报单编号, char[21]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('TradingRole', TTradingRole), #交易角色, char
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('OffsetFlag', TOffsetFlag), #开平标志, char
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('Price', TStockPrice), #价格, char[9]
        ('Volume', TVolume), #数量, int
        ('TradeDate', TDate), #成交时期, char[9]
        ('TradeTime', TTime), #成交时间, char[9]
        ('TradeType', TTradeType), #成交类型, char
        ('PriceSource', TPriceSource), #成交价来源, char
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ClearingPartID', TParticipantID), #结算会员编号, char[11]
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('SequenceNo', TSequenceNo), #序号, int
    )
class Trade(BaseStruct): #成交
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('UserID', TUserID), #用户代码, char[16]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('TradeID', TTradeID), #成交编号, char[21]
        ('Direction', TDirection), #买卖方向, char
        ('OrderSysID', TOrderSysID), #报单编号, char[21]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('TradingRole', TTradingRole), #交易角色, char
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('OffsetFlag', TOffsetFlag), #开平标志, char
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('Price', TStockPrice), #价格, char[9]
        ('Volume', TVolume), #数量, int
        ('TradeDate', TDate), #成交时期, char[9]
        ('TradeTime', TTime), #成交时间, char[9]
        ('TradeType', TTradeType), #成交类型, char
        ('PriceSource', TPriceSource), #成交价来源, char
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ClearingPartID', TParticipantID), #结算会员编号, char[11]
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('SequenceNo', TSequenceNo), #序号, int
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('BrokerOrderSeq', TSequenceNo), #经纪公司报单编号, int
    )
class UserSession(BaseStruct): #用户会话
    _fields_ = (
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('LoginDate', TDate), #登录日期, char[9]
        ('LoginTime', TTime), #登录时间, char[9]
        ('IPAddress', TIPAddress), #IP地址, char[16]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('InterfaceProductInfo', TProductInfo), #接口端产品信息, char[11]
        ('ProtocolInfo', TProtocolInfo), #协议信息, char[11]
        ('MacAddress', TMacAddress), #Mac地址, char[21]
    )
class QueryMaxOrderVolume(BaseStruct): #查询最大报单数量
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('Direction', TDirection), #买卖方向, char
        ('OffsetFlag', TOffsetFlag), #开平标志, char
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('MaxVolume', TVolume), #最大允许报单数量, int
    )
class SettlementInfoConfirm(BaseStruct): #投资者结算结果确认信息
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('ConfirmDate', TDate), #确认日期, char[9]
        ('ConfirmTime', TTime), #确认时间, char[9]
    )
class SyncDeposit(BaseStruct): #出入金同步
    _fields_ = (
        ('DepositSeqNo', TDepositSeqNo), #出入金流水号, char[15]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('Deposit', TMoney), #入金金额, double
        ('IsForce', TBool), #是否强制进行, int
    )
class BrokerSync(BaseStruct): #经纪公司同步
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
    )
class SyncingInvestor(BaseStruct): #正在同步中的投资者
    _fields_ = (
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorGroupID', TInvestorID), #投资者分组代码, char[15]
        ('InvestorName', TPartyName), #投资者名称, char[81]
        ('IdentifiedCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('IsActive', TBool), #是否活跃, int
        ('Telephone', TTelephone), #联系电话, char[41]
        ('Address', TAddress), #通讯地址, char[101]
        ('OpenDate', TDate), #开户日期, char[9]
        ('Mobile', TMobile), #手机, char[41]
        ('SHBranchID', TBranchID), #上海营业部编号, char[9]
        ('SZBranchID', TBranchID), #深圳营业部编号, char[9]
        ('IsCreditAccount', TBool), #是否信用账户, int
    )
class SyncingTradingCode(BaseStruct): #正在同步中的交易代码
    _fields_ = (
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ClientID', TClientID), #客户代码, char[11]
        ('IsActive', TBool), #是否活跃, int
    )
class SyncingInvestorGroup(BaseStruct): #正在同步中的投资者分组
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorGroupID', TInvestorID), #投资者分组代码, char[15]
        ('InvestorGroupName', TInvestorGroupName), #投资者分组名称, char[41]
    )
class SyncingTradingAccount(BaseStruct): #正在同步中的交易账号
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('PreMortgage', TMoney), #上次质押金额, double
        ('PreCredit', TMoney), #上次信用额度, double
        ('PreDeposit', TMoney), #上次存款额, double
        ('PreBalance', TMoney), #上次结算准备金, double
        ('PreMargin', TMoney), #上次占用的保证金, double
        ('InterestBase', TMoney), #利息基数, double
        ('Interest', TMoney), #利息收入, double
        ('Deposit', TMoney), #入金金额, double
        ('Withdraw', TMoney), #出金金额, double
        ('FrozenMargin', TMoney), #冻结的保证金, double
        ('FrozenCash', TMoney), #冻结的资金, double
        ('FrozenCommission', TMoney), #冻结的手续费, double
        ('CurrMargin', TMoney), #当前保证金总额, double
        ('CashIn', TMoney), #资金差额, double
        ('Commission', TMoney), #手续费, double
        ('CloseProfit', TMoney), #平仓盈亏, double
        ('PositionProfit', TMoney), #持仓盈亏, double
        ('Balance', TMoney), #期货结算准备金, double
        ('Available', TMoney), #可用资金, double
        ('WithdrawQuota', TMoney), #可取资金, double
        ('Reserve', TMoney), #基本准备金, double
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('Credit', TMoney), #信用额度, double
        ('Mortgage', TMoney), #质押金额, double
        ('ExchangeMargin', TMoney), #交易所保证金, double
        ('DeliveryMargin', TMoney), #投资者交割保证金, double
        ('ExchangeDeliveryMargin', TMoney), #交易所交割保证金, double
        ('FrozenTransferFee', TMoney), #冻结的过户费, double
        ('FrozenStampTax', TMoney), #冻结的印花税, double
        ('TransferFee', TMoney), #过户费, double
        ('StampTax', TMoney), #印花税, double
        ('ConversionAmount', TMoney), #折算金额, double
        ('CreditAmount', TMoney), #授信额度, double
        ('LowLimitRatio', TRatio), #最低维持担保比例, double
        ('MarginTradingAmount', TMoney), #融资买入金额, double
        ('ShortSellingAmount', TMoney), #融券卖出金额, double
        ('MarginTradingAvail', TMoney), #融资买入可用金额, double
        ('ShortSellingAvail', TMoney), #融券卖出可用金额, double
        ('CreditRatio', TRatio), #维持担保比例, double
        ('StockValue', TMoney), #证券总价值, double
    )
class SyncingInvestorPosition(BaseStruct): #正在同步中的投资者持仓
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('PosiDirection', TPosiDirection), #持仓多空方向, char
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('PositionDate', TPositionDate), #持仓日期, char
        ('YdPosition', TVolume), #上日持仓, int
        ('Position', TVolume), #今日持仓, int
        ('LongFrozen', TVolume), #多头冻结, int
        ('ShortFrozen', TVolume), #空头冻结, int
        ('LongFrozenAmount', TMoney), #开仓冻结金额, double
        ('ShortFrozenAmount', TMoney), #开仓冻结金额, double
        ('OpenVolume', TVolume), #开仓量, int
        ('CloseVolume', TVolume), #平仓量, int
        ('OpenAmount', TMoney), #开仓金额, double
        ('CloseAmount', TMoney), #平仓金额, double
        ('PositionCost', TMoney), #持仓成本, double
        ('FrozenCash', TMoney), #冻结的资金, double
        ('CashIn', TMoney), #资金差额, double
        ('Commission', TMoney), #手续费, double
        ('CloseProfit', TMoney), #平仓盈亏, double
        ('PositionProfit', TMoney), #持仓盈亏, double
        ('PreSettlementPrice', TPrice), #上次结算价, double
        ('SettlementPrice', TPrice), #本次结算价, double
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('OpenCost', TMoney), #开仓成本, double
        ('ExchangeMargin', TMoney), #交易所保证金, double
        ('TodayPosition', TVolume), #今日持仓, int
        ('TransferFee', TMoney), #过户费, double
        ('StampTax', TMoney), #印花税, double
        ('TodayPurRedVolume', TVolume), #今日申购赎回数量, int
        ('ConversionRate', TRatio), #折算率, double
        ('ConversionAmount', TMoney), #折算金额, double
        ('MarginTradeVolume', TVolume), #融资买入出数量, int
        ('MarginTradeAmount', TMoney), #融资买入金额, double
        ('MarginTradeFrozenVolume', TVolume), #融资买入冻结数量, int
        ('MarginTradeFrozenAmount', TMoney), #融资买入冻结金额, double
        ('MarginTradeConversionAmount', TMoney), #融资买入折算金额, double
        ('ShortSellVolume', TVolume), #融券卖出数量, int
        ('ShortSellAmount', TMoney), #融券卖出金额, double
        ('ShortSellConversionAmount', TMoney), #融券卖出折算金额, double
        ('ShortSellFrozenVolume', TVolume), #融券卖出冻结数量, int
        ('ShortSellFrozenAmount', TMoney), #融券卖出冻结金额, double
        ('StockValue', TMoney), #证券价值, double
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class SyncingInstrumentMarginRate(BaseStruct): #正在同步中的合约保证金率
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('LongMarginRatioByMoney', TRatio), #多头保证金率, double
        ('LongMarginRatioByVolume', TMoney), #多头保证金费, double
        ('ShortMarginRatioByMoney', TRatio), #空头保证金率, double
        ('ShortMarginRatioByVolume', TMoney), #空头保证金费, double
        ('IsRelative', TBool), #是否相对交易所收取, int
    )
class SyncingInstrumentCommissionRate(BaseStruct): #正在同步中的合约手续费率
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('BuyStampTaxRateByMoney', TRatio), #买印花税率, double
        ('BuyStampTaxRateByVolume', TRatio), #买印花税率(按手数), double
        ('SellStampTaxRateByMoney', TRatio), #卖印花税率, double
        ('SellStampTaxRateByVolume', TRatio), #卖印花税率(按手数), double
        ('BuyTransferFeeRateByMoney', TRatio), #买过户费率, double
        ('BuyTransferFeeRateByVolume', TRatio), #买过户费率(按手数), double
        ('SellTransferFeeRateByMoney', TRatio), #卖过户费率, double
        ('SellTransferFeeRateByVolume', TRatio), #卖过户费率(按手数), double
        ('BuyTradeFeeByMoney', TRatio), #买交易费, double
        ('BuyTradeFeeByVolume', TRatio), #买交易费(按手数), double
        ('SellTradeFeeByMoney', TRatio), #卖交易费率, double
        ('SellTradeFeeByVolume', TRatio), #卖交易费率(按手数), double
        ('BuyMarginByMoney', TRatio), #买交易附加费率, double
        ('SellMarginByMoney', TRatio), #卖交易附加费率, double
        ('MinTradeFee', TPrice), #最小过户费, double
    )
class SyncingInstrumentTradingRight(BaseStruct): #正在同步中的合约交易权限
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('Direction', TDirection), #买卖, char
        ('TradingRight', TTradingRight), #交易权限, char
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class QryOrder(BaseStruct): #查询报单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderSysID', TOrderSysID), #报单编号, char[21]
        ('InsertTimeStart', TTime), #开始时间, char[9]
        ('InsertTimeEnd', TTime), #结束时间, char[9]
    )
class QryTrade(BaseStruct): #查询成交
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('TradeID', TTradeID), #成交编号, char[21]
        ('TradeTimeStart', TTime), #开始时间, char[9]
        ('TradeTimeEnd', TTime), #结束时间, char[9]
    )
class QryInvestorPosition(BaseStruct): #查询投资者持仓
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
    )
class QryTradingAccount(BaseStruct): #查询资金账户
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class QryInvestor(BaseStruct): #查询投资者
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class QryTradingCode(BaseStruct): #查询交易编码
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ClientID', TClientID), #客户代码, char[11]
    )
class QryInvestorGroup(BaseStruct): #查询交易编码
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
    )
class QryInstrumentMarginRate(BaseStruct): #查询交易编码
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
    )
class QryInstrumentCommissionRate(BaseStruct): #查询交易编码
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
    )
class QryInstrumentTradingRight(BaseStruct): #查询交易编码
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
    )
class QryBroker(BaseStruct): #查询经纪公司
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
    )
class QryTrader(BaseStruct): #查询交易员
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
    )
class QryPartBroker(BaseStruct): #查询经纪公司会员代码
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
    )
class QrySuperUserFunction(BaseStruct): #查询管理用户功能权限
    _fields_ = (
        ('UserID', TUserID), #用户代码, char[16]
    )
class QryUserSession(BaseStruct): #查询用户会话
    _fields_ = (
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
    )
class QryFrontStatus(BaseStruct): #查询前置状态
    _fields_ = (
        ('FrontID', TFrontID), #前置编号, int
    )
class QryExchangeOrder(BaseStruct): #查询交易所报单
    _fields_ = (
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
    )
class QryOrderAction(BaseStruct): #查询报单操作
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class QryExchangeOrderAction(BaseStruct): #查询交易所报单操作
    _fields_ = (
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
    )
class QrySuperUser(BaseStruct): #查询管理用户
    _fields_ = (
        ('UserID', TUserID), #用户代码, char[16]
    )
class QryExchange(BaseStruct): #查询交易所
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class QryProduct(BaseStruct): #查询产品
    _fields_ = (
        ('ProductID', TInstrumentID), #产品代码, char[31]
    )
class QryInstrument(BaseStruct): #查询合约
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('ProductID', TInstrumentID), #产品代码, char[31]
    )
class QryDepthMarketData(BaseStruct): #查询行情
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
    )
class QryBrokerUser(BaseStruct): #查询经纪公司用户
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
    )
class QryBrokerUserFunction(BaseStruct): #查询经纪公司用户权限
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
    )
class QryTraderOffer(BaseStruct): #查询交易员报盘机
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
    )
class QrySyncDeposit(BaseStruct): #查询出入金流水
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('DepositSeqNo', TDepositSeqNo), #出入金流水号, char[15]
    )
class QrySettlementInfo(BaseStruct): #查询投资者结算结果
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('TradingDay', TDate), #交易日, char[9]
    )
class QryHisOrder(BaseStruct): #查询报单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderSysID', TOrderSysID), #报单编号, char[21]
        ('InsertTimeStart', TTime), #开始时间, char[9]
        ('InsertTimeEnd', TTime), #结束时间, char[9]
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
    )
class MarketData(BaseStruct): #市场行情
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('LastPrice', TPrice), #最新价, double
        ('PreSettlementPrice', TPrice), #上次结算价, double
        ('PreClosePrice', TPrice), #昨收盘, double
        ('PreOpenInterest', TLargeVolume), #昨持仓量, double
        ('OpenPrice', TPrice), #今开盘, double
        ('HighestPrice', TPrice), #最高价, double
        ('LowestPrice', TPrice), #最低价, double
        ('Volume', TVolume), #数量, int
        ('Turnover', TMoney), #成交金额, double
        ('OpenInterest', TLargeVolume), #持仓量, double
        ('ClosePrice', TPrice), #今收盘, double
        ('SettlementPrice', TPrice), #本次结算价, double
        ('UpperLimitPrice', TPrice), #涨停板价, double
        ('LowerLimitPrice', TPrice), #跌停板价, double
        ('PreDelta', TRatio), #昨虚实度, double
        ('CurrDelta', TRatio), #今虚实度, double
        ('UpdateTime', TTime), #最后修改时间, char[9]
        ('UpdateMillisec', TMillisec), #最后修改毫秒, int
    )
class MarketDataBase(BaseStruct): #行情基础属性
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('PreSettlementPrice', TPrice), #上次结算价, double
        ('PreClosePrice', TPrice), #昨收盘, double
        ('PreOpenInterest', TLargeVolume), #昨持仓量, double
        ('PreDelta', TRatio), #昨虚实度, double
    )
class MarketDataStatic(BaseStruct): #行情静态属性
    _fields_ = (
        ('OpenPrice', TPrice), #今开盘, double
        ('HighestPrice', TPrice), #最高价, double
        ('LowestPrice', TPrice), #最低价, double
        ('ClosePrice', TPrice), #今收盘, double
        ('UpperLimitPrice', TPrice), #涨停板价, double
        ('LowerLimitPrice', TPrice), #跌停板价, double
        ('SettlementPrice', TPrice), #本次结算价, double
        ('CurrDelta', TRatio), #今虚实度, double
    )
class MarketDataLastMatch(BaseStruct): #行情最新成交属性
    _fields_ = (
        ('LastPrice', TPrice), #最新价, double
        ('Volume', TVolume), #数量, int
        ('Turnover', TMoney), #成交金额, double
        ('OpenInterest', TLargeVolume), #持仓量, double
    )
class MarketDataBestPrice(BaseStruct): #行情最优价属性
    _fields_ = (
        ('BidPrice1', TPrice), #申买价一, double
        ('BidVolume1', TVolume), #申买量一, int
        ('AskPrice1', TPrice), #申卖价一, double
        ('AskVolume1', TVolume), #申卖量一, int
    )
class MarketDataBid23(BaseStruct): #行情申买二、三属性
    _fields_ = (
        ('BidPrice2', TPrice), #申买价二, double
        ('BidVolume2', TVolume), #申买量二, int
        ('BidPrice3', TPrice), #申买价三, double
        ('BidVolume3', TVolume), #申买量三, int
    )
class MarketDataAsk23(BaseStruct): #行情申卖二、三属性
    _fields_ = (
        ('AskPrice2', TPrice), #申卖价二, double
        ('AskVolume2', TVolume), #申卖量二, int
        ('AskPrice3', TPrice), #申卖价三, double
        ('AskVolume3', TVolume), #申卖量三, int
    )
class MarketDataBid45(BaseStruct): #行情申买四、五属性
    _fields_ = (
        ('BidPrice4', TPrice), #申买价四, double
        ('BidVolume4', TVolume), #申买量四, int
        ('BidPrice5', TPrice), #申买价五, double
        ('BidVolume5', TVolume), #申买量五, int
    )
class MarketDataAsk45(BaseStruct): #行情申卖四、五属性
    _fields_ = (
        ('AskPrice4', TPrice), #申卖价四, double
        ('AskVolume4', TVolume), #申卖量四, int
        ('AskPrice5', TPrice), #申卖价五, double
        ('AskVolume5', TVolume), #申卖量五, int
    )
class MarketDataUpdateTime(BaseStruct): #行情更新时间属性
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('UpdateTime', TTime), #最后修改时间, char[9]
        ('UpdateMillisec', TMillisec), #最后修改毫秒, int
    )
class SpecificInstrument(BaseStruct): #指定的合约
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class InstrumentStatus(BaseStruct): #合约状态
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('SettlementGroupID', TSettlementGroupID), #结算组代码, char[9]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('InstrumentStatus', TInstrumentStatus), #合约交易状态, char
        ('TradingSegmentSN', TTradingSegmentSN), #交易阶段编号, int
        ('EnterTime', TTime), #进入本状态时间, char[9]
        ('EnterReason', TInstStatusEnterReason), #进入本状态原因, char
    )
class QryInstrumentStatus(BaseStruct): #查询合约状态
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
    )
class InvestorAccount(BaseStruct): #投资者账户
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('AccountID', TAccountID), #投资者帐号, char[15]
    )
class PositionProfitAlgorithm(BaseStruct): #浮动盈亏算法
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Algorithm', TAlgorithm), #盈亏算法, char
        ('Memo', TMemo), #备注, char[161]
    )
class Discount(BaseStruct): #会员资金折扣
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('Discount', TRatio), #资金折扣比例, double
    )
class QryTransferBank(BaseStruct): #查询转帐银行
    _fields_ = (
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBrchID', TBankBrchID), #银行分中心代码, char[5]
    )
class TransferBank(BaseStruct): #转帐银行
    _fields_ = (
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBrchID', TBankBrchID), #银行分中心代码, char[5]
        ('BankName', TBankName), #银行名称, char[101]
        ('IsActive', TBool), #是否活跃, int
    )
class QryInvestorPositionDetail(BaseStruct): #查询投资者持仓明细
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
    )
class InvestorPositionDetail(BaseStruct): #投资者持仓明细
    _fields_ = (
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('Direction', TDirection), #买卖, char
        ('OpenDate', TDate), #开仓日期, char[9]
        ('TradeID', TTradeID), #成交编号, char[21]
        ('Volume', TVolume), #数量, int
        ('OpenPrice', TPrice), #开仓价, double
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('TradeType', TTradeType), #成交类型, char
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('Margin', TMoney), #投资者保证金, double
        ('ExchMargin', TMoney), #交易所保证金, double
        ('LastSettlementPrice', TPrice), #昨结算价, double
        ('SettlementPrice', TPrice), #结算价, double
        ('CloseVolume', TVolume), #平仓量, int
        ('CloseAmount', TMoney), #平仓金额, double
        ('TransferFee', TMoney), #过户费, double
        ('StampTax', TMoney), #印花税, double
        ('Commission', TMoney), #手续费, double
    )
class TradingAccountPassword(BaseStruct): #资金账户口令域
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #密码, char[41]
    )
class MDTraderOffer(BaseStruct): #交易所行情报盘机
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('Password', TPassword), #密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('TraderConnectStatus', TTraderConnectStatus), #交易所交易员连接状态, char
        ('ConnectRequestDate', TDate), #发出连接请求的日期, char[9]
        ('ConnectRequestTime', TTime), #发出连接请求的时间, char[9]
        ('LastReportDate', TDate), #上次报告日期, char[9]
        ('LastReportTime', TTime), #上次报告时间, char[9]
        ('ConnectDate', TDate), #完成连接日期, char[9]
        ('ConnectTime', TTime), #完成连接时间, char[9]
        ('StartDate', TDate), #启动日期, char[9]
        ('StartTime', TTime), #启动时间, char[9]
        ('TradingDay', TDate), #交易日, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('BranchID', TBranchID), #营业部编号, char[9]
    )
class QryMDTraderOffer(BaseStruct): #查询行情报盘机
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
    )
class QryNotice(BaseStruct): #查询客户通知
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
    )
class Notice(BaseStruct): #客户通知
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('Content', TContent), #消息正文, char[501]
        ('SequenceLabel', TSequenceLabel), #经纪公司通知内容序列号, char[2]
    )
class UserRight(BaseStruct): #用户权限
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserRightType', TUserRightType), #客户权限类型, char
        ('IsForbidden', TBool), #是否禁止, int
    )
class QrySettlementInfoConfirm(BaseStruct): #查询结算信息确认域
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class LoadSettlementInfo(BaseStruct): #装载结算信息
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
    )
class BrokerWithdrawAlgorithm(BaseStruct): #经纪公司可提资金算法表
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('WithdrawAlgorithm', TAlgorithm), #可提资金算法, char
        ('UsingRatio', TRatio), #资金使用率, double
        ('IncludeCloseProfit', TIncludeCloseProfit), #可提是否包含平仓盈利, char
        ('AllWithoutTrade', TAllWithoutTrade), #本日无仓且无成交客户是否受可提比例限制, char
        ('AvailIncludeCloseProfit', TIncludeCloseProfit), #可用是否包含平仓盈利, char
        ('IsBrokerUserEvent', TBool), #是否启用用户事件, int
    )
class TradingAccountPasswordUpdateV1(BaseStruct): #资金账户口令变更域
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('OldPassword', TPassword), #原来的口令, char[41]
        ('NewPassword', TPassword), #新的口令, char[41]
    )
class TradingAccountPasswordUpdate(BaseStruct): #资金账户口令变更域
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('OldPassword', TPassword), #原来的口令, char[41]
        ('NewPassword', TPassword), #新的口令, char[41]
    )
class QryCombinationLeg(BaseStruct): #查询组合合约分腿
    _fields_ = (
        ('CombInstrumentID', TInstrumentID), #组合合约代码, char[31]
        ('LegID', TLegID), #单腿编号, int
        ('LegInstrumentID', TInstrumentID), #单腿合约代码, char[31]
    )
class QrySyncStatus(BaseStruct): #查询组合合约分腿
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
    )
class CombinationLeg(BaseStruct): #组合交易合约的单腿
    _fields_ = (
        ('CombInstrumentID', TInstrumentID), #组合合约代码, char[31]
        ('LegID', TLegID), #单腿编号, int
        ('LegInstrumentID', TInstrumentID), #单腿合约代码, char[31]
        ('Direction', TDirection), #买卖方向, char
        ('LegMultiple', TLegMultiple), #单腿乘数, int
        ('ImplyLevel', TImplyLevel), #派生层数, int
    )
class SyncStatus(BaseStruct): #数据同步状态
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('DataSyncStatus', TDataSyncStatus), #数据同步状态, char
    )
class QryLinkMan(BaseStruct): #查询联系人
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class LinkMan(BaseStruct): #联系人
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('PersonType', TPersonType), #联系人类型, char
        ('IdentifiedCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('PersonName', TPartyName), #名称, char[81]
        ('Telephone', TTelephone), #联系电话, char[41]
        ('Address', TAddress), #通讯地址, char[101]
        ('ZipCode', TZipCode), #邮政编码, char[7]
        ('Priority', TPriority), #优先级, int
    )
class QryBrokerUserEvent(BaseStruct): #查询经纪公司用户事件
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserEventType', TUserEventType), #用户事件类型, char
    )
class BrokerUserEvent(BaseStruct): #查询经纪公司用户事件
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserEventType', TUserEventType), #用户事件类型, char
        ('EventSequenceNo', TSequenceNo), #用户事件序号, int
        ('EventDate', TDate), #事件发生日期, char[9]
        ('EventTime', TTime), #事件发生时间, char[9]
        ('UserEventInfo', TUserEventInfo), #用户事件信息, char[1025]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
    )
class QryContractBank(BaseStruct): #查询签约银行请求
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBrchID', TBankBrchID), #银行分中心代码, char[5]
    )
class ContractBank(BaseStruct): #查询签约银行响应
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBrchID', TBankBrchID), #银行分中心代码, char[5]
        ('BankName', TBankName), #银行名称, char[101]
    )
class InvestorPositionCombineDetail(BaseStruct): #投资者组合持仓明细
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('OpenDate', TDate), #开仓日期, char[9]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('ComTradeID', TTradeID), #组合编号, char[21]
        ('TradeID', TTradeID), #撮合编号, char[21]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('Direction', TDirection), #买卖, char
        ('TotalAmt', TVolume), #持仓量, int
        ('Margin', TMoney), #投资者保证金, double
        ('ExchMargin', TMoney), #交易所保证金, double
        ('MarginRateByMoney', TRatio), #保证金率, double
        ('MarginRateByVolume', TRatio), #保证金率(按手数), double
        ('LegID', TLegID), #单腿编号, int
        ('LegMultiple', TLegMultiple), #单腿乘数, int
        ('CombInstrumentID', TInstrumentID), #组合持仓合约编码, char[31]
    )
class ParkedOrder(BaseStruct): #预埋单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('UserID', TUserID), #用户代码, char[16]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderPriceType', TOrderPriceType), #报单价格条件, char
        ('Direction', TDirection), #买卖方向, char
        ('CombOffsetFlag', TCombOffsetFlag), #组合开平标志, char[5]
        ('CombHedgeFlag', TCombHedgeFlag), #组合投机套保标志, char[5]
        ('LimitPrice', TStockPrice), #价格, char[9]
        ('VolumeTotalOriginal', TVolume), #数量, int
        ('TimeCondition', TTimeCondition), #有效期类型, char
        ('GTDDate', TDate), #GTD日期, char[9]
        ('VolumeCondition', TVolumeCondition), #成交量类型, char
        ('MinVolume', TVolume), #最小成交量, int
        ('ContingentCondition', TContingentCondition), #触发条件, char
        ('StopPrice', TPrice), #止损价, double
        ('ForceCloseReason', TForceCloseReason), #强平原因, char
        ('IsAutoSuspend', TBool), #自动挂起标志, int
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('RequestID', TRequestID), #请求编号, int
        ('UserForceClose', TBool), #用户强评标志, int
        ('ParkedOrderID', TParkedOrderID), #预埋报单编号, char[13]
        ('UserType', TUserType), #用户类型, char
        ('Status', TParkedOrderStatus), #预埋单状态, char
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class ParkedOrderAction(BaseStruct): #输入预埋单操作
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('OrderActionRef', TOrderActionRef), #报单操作引用, int
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('RequestID', TRequestID), #请求编号, int
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ActionFlag', TActionFlag), #操作标志, char
        ('LimitPrice', TPrice), #价格, double
        ('VolumeChange', TVolume), #数量变化, int
        ('UserID', TUserID), #用户代码, char[16]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ParkedOrderActionID', TParkedOrderActionID), #预埋撤单单编号, char[13]
        ('UserType', TUserType), #用户类型, char
        ('Status', TParkedOrderStatus), #预埋撤单状态, char
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class QryParkedOrder(BaseStruct): #查询预埋单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class QryParkedOrderAction(BaseStruct): #查询预埋撤单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class RemoveParkedOrder(BaseStruct): #删除预埋单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('ParkedOrderID', TParkedOrderID), #预埋报单编号, char[13]
    )
class RemoveParkedOrderAction(BaseStruct): #删除预埋撤单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('ParkedOrderActionID', TParkedOrderActionID), #预埋撤单编号, char[13]
    )
class InvestorWithdrawAlgorithm(BaseStruct): #经纪公司可提资金算法表
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('UsingRatio', TRatio), #可提资金比例, double
    )
class QryInvestorPositionCombineDetail(BaseStruct): #查询组合持仓明细
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('CombInstrumentID', TInstrumentID), #组合持仓合约编码, char[31]
    )
class MarketDataAveragePrice(BaseStruct): #成交均价
    _fields_ = (
        ('AveragePrice', TPrice), #当日均价, double
    )
class VerifyInvestorPassword(BaseStruct): #校验投资者密码
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('Password', TPassword), #密码, char[41]
    )
class UserIP(BaseStruct): #用户IP
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('IPAddress', TIPAddress), #IP地址, char[16]
        ('IPMask', TIPAddress), #IP地址掩码, char[16]
        ('MacAddress', TMacAddress), #Mac地址, char[21]
    )
class TradingNoticeInfo(BaseStruct): #用户事件通知信息
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('SendTime', TTime), #发送时间, char[9]
        ('FieldContent', TContent), #消息正文, char[501]
        ('SequenceSeries', TSequenceSeries), #序列系列号, short
        ('SequenceNo', TSequenceNo), #序列号, int
    )
class TradingNotice(BaseStruct): #用户事件通知
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorRange', TInvestorRange), #投资者范围, char
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('SequenceSeries', TSequenceSeries), #序列系列号, short
        ('UserID', TUserID), #用户代码, char[16]
        ('SendTime', TTime), #发送时间, char[9]
        ('SequenceNo', TSequenceNo), #序列号, int
        ('FieldContent', TContent), #消息正文, char[501]
    )
class QryTradingNotice(BaseStruct): #查询交易事件通知
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class QryErrOrder(BaseStruct): #查询错误报单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class ErrOrder(BaseStruct): #错误报单
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('UserID', TUserID), #用户代码, char[16]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderPriceType', TOrderPriceType), #报单价格条件, char
        ('Direction', TDirection), #买卖方向, char
        ('CombOffsetFlag', TCombOffsetFlag), #组合开平标志, char[5]
        ('CombHedgeFlag', TCombHedgeFlag), #组合投机套保标志, char[5]
        ('LimitPrice', TStockPrice), #价格, char[9]
        ('VolumeTotalOriginal', TVolume), #数量, int
        ('TimeCondition', TTimeCondition), #有效期类型, char
        ('GTDDate', TDate), #GTD日期, char[9]
        ('VolumeCondition', TVolumeCondition), #成交量类型, char
        ('MinVolume', TVolume), #最小成交量, int
        ('ContingentCondition', TContingentCondition), #触发条件, char
        ('StopPrice', TPrice), #止损价, double
        ('ForceCloseReason', TForceCloseReason), #强平原因, char
        ('IsAutoSuspend', TBool), #自动挂起标志, int
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('RequestID', TRequestID), #请求编号, int
        ('UserForceClose', TBool), #用户强评标志, int
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class ErrorConditionalOrder(BaseStruct): #查询错误报单操作
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('UserID', TUserID), #用户代码, char[16]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('OrderPriceType', TOrderPriceType), #报单价格条件, char
        ('Direction', TDirection), #买卖方向, char
        ('CombOffsetFlag', TCombOffsetFlag), #组合开平标志, char[5]
        ('CombHedgeFlag', TCombHedgeFlag), #组合投机套保标志, char[5]
        ('LimitPrice', TStockPrice), #价格, char[9]
        ('VolumeTotalOriginal', TVolume), #数量, int
        ('TimeCondition', TTimeCondition), #有效期类型, char
        ('GTDDate', TDate), #GTD日期, char[9]
        ('VolumeCondition', TVolumeCondition), #成交量类型, char
        ('MinVolume', TVolume), #最小成交量, int
        ('ContingentCondition', TContingentCondition), #触发条件, char
        ('StopPrice', TPrice), #止损价, double
        ('ForceCloseReason', TForceCloseReason), #强平原因, char
        ('IsAutoSuspend', TBool), #自动挂起标志, int
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('RequestID', TRequestID), #请求编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('ExchangeInstID', TExchangeInstID), #合约在交易所的代码, char[31]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderSubmitStatus', TOrderSubmitStatus), #报单提交状态, char
        ('NotifySequence', TSequenceNo), #报单提示序号, int
        ('TradingDay', TDate), #交易日, char[9]
        ('SettlementID', TSettlementID), #结算编号, int
        ('OrderSysID', TOrderSysID), #报单编号, char[21]
        ('OrderSource', TOrderSource), #报单来源, char
        ('OrderStatus', TOrderStatus), #报单状态, char
        ('OrderType', TOrderType), #报单类型, char
        ('VolumeTraded', TVolume), #今成交数量, int
        ('VolumeTotal', TVolume), #剩余数量, int
        ('InsertDate', TDate), #报单日期, char[9]
        ('InsertTime', TTime), #委托时间, char[9]
        ('ActiveTime', TTime), #激活时间, char[9]
        ('SuspendTime', TTime), #挂起时间, char[9]
        ('UpdateTime', TTime), #最后修改时间, char[9]
        ('CancelTime', TTime), #撤销时间, char[9]
        ('ActiveTraderID', TTraderID), #最后修改交易所交易员代码, char[21]
        ('ClearingPartID', TParticipantID), #结算会员编号, char[11]
        ('SequenceNo', TSequenceNo), #序号, int
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('StatusMsg', TErrorMsg), #状态信息, char[81]
        ('UserForceClose', TBool), #用户强评标志, int
        ('ActiveUserID', TUserID), #操作用户代码, char[16]
        ('BrokerOrderSeq', TSequenceNo), #经纪公司报单编号, int
        ('RelativeOrderSysID', TOrderSysID), #相关报单, char[21]
        ('BranchID', TBranchID), #营业部编号, char[9]
        ('TradeAmount', TMoney), #成交数量, double
        ('IsETF', TBool), #是否ETF, int
        ('AccountID', TAccountID), #资金帐号, char[15]
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class QryErrOrderAction(BaseStruct): #查询错误报单操作
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class ErrOrderAction(BaseStruct): #错误报单操作
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('OrderActionRef', TOrderActionRef), #报单操作引用, int
        ('OrderRef', TOrderRef), #报单引用, char[13]
        ('RequestID', TRequestID), #请求编号, int
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('ActionFlag', TActionFlag), #操作标志, char
        ('LimitPrice', TPrice), #价格, double
        ('VolumeChange', TVolume), #数量变化, int
        ('ActionDate', TDate), #操作日期, char[9]
        ('ActionTime', TTime), #操作时间, char[9]
        ('TraderID', TTraderID), #交易所交易员代码, char[21]
        ('InstallID', TInstallID), #安装编号, int
        ('OrderLocalID', TOrderLocalID), #本地报单编号, char[13]
        ('ActionLocalID', TOrderLocalID), #操作本地编号, char[13]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ClientID', TClientID), #客户代码, char[11]
        ('BusinessUnit', TBusinessUnit), #业务单元, char[21]
        ('OrderActionStatus', TOrderActionStatus), #报单操作状态, char
        ('UserID', TUserID), #用户代码, char[16]
        ('BranchID', TBranchID), #营业部编号, char[9]
        ('StatusMsg', TErrorMsg), #状态信息, char[81]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class QryExchangeSequence(BaseStruct): #查询交易所状态
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class ExchangeSequence(BaseStruct): #交易所状态
    _fields_ = (
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('SequenceNo', TSequenceNo), #序号, int
        ('MarketStatus', TInstrumentStatus), #合约交易状态, char
    )
class QueryMaxOrderVolumeWithPrice(BaseStruct): #根据价格查询最大报单数量
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('Direction', TDirection), #买卖方向, char
        ('OffsetFlag', TOffsetFlag), #开平标志, char
        ('HedgeFlag', THedgeFlag), #投机套保标志, char
        ('MaxVolume', TVolume), #最大允许报单数量, int
        ('Price', TPrice), #报单价格, double
    )
class QryBrokerTradingParams(BaseStruct): #查询经纪公司交易参数
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class BrokerTradingParams(BaseStruct): #经纪公司交易参数
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('MarginPriceType', TMarginPriceType), #保证金价格类型, char
        ('Algorithm', TAlgorithm), #盈亏算法, char
        ('AvailIncludeCloseProfit', TIncludeCloseProfit), #可用是否包含平仓盈利, char
    )
class QryBrokerTradingAlgos(BaseStruct): #查询经纪公司交易算法
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
    )
class BrokerTradingAlgos(BaseStruct): #经纪公司交易算法
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('HandlePositionAlgoID', THandlePositionAlgoID), #持仓处理算法编号, char
        ('FindMarginRateAlgoID', TFindMarginRateAlgoID), #寻找保证金率算法编号, char
        ('HandleTradingAccountAlgoID', THandleTradingAccountAlgoID), #资金处理算法编号, char
    )
class QueryBrokerDeposit(BaseStruct): #查询经纪公司资金
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class BrokerDeposit(BaseStruct): #经纪公司资金
    _fields_ = (
        ('TradingDay', TTradeDate), #交易日期, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ParticipantID', TParticipantID), #会员代码, char[11]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('PreBalance', TMoney), #上次结算准备金, double
        ('CurrMargin', TMoney), #当前保证金总额, double
        ('CloseProfit', TMoney), #平仓盈亏, double
        ('Balance', TMoney), #期货结算准备金, double
        ('Deposit', TMoney), #入金金额, double
        ('Withdraw', TMoney), #出金金额, double
        ('Available', TMoney), #可提资金, double
        ('Reserve', TMoney), #基本准备金, double
        ('FrozenMargin', TMoney), #冻结的保证金, double
    )
class QryCFMMCBrokerKey(BaseStruct): #查询保证金监管系统经纪公司密钥
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
    )
class CFMMCBrokerKey(BaseStruct): #保证金监管系统经纪公司密钥
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ParticipantID', TParticipantID), #经纪公司统一编码, char[11]
        ('CreateDate', TDate), #密钥生成日期, char[9]
        ('CreateTime', TTime), #密钥生成时间, char[9]
        ('KeyID', TSequenceNo), #密钥编号, int
        ('CurrentKey', TCFMMCKey), #动态密钥, char[21]
        ('KeyKind', TCFMMCKeyKind), #动态密钥类型, char
    )
class CFMMCTradingAccountKey(BaseStruct): #保证金监管系统经纪公司资金账户密钥
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('ParticipantID', TParticipantID), #经纪公司统一编码, char[11]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('KeyID', TSequenceNo), #密钥编号, int
        ('CurrentKey', TCFMMCKey), #动态密钥, char[21]
    )
class QryCFMMCTradingAccountKey(BaseStruct): #请求查询保证金监管系统经纪公司资金账户密钥
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
    )
class BrokerUserOTPParam(BaseStruct): #用户动态令牌参数
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('OTPVendorsID', TOTPVendorsID), #动态令牌提供商, char[2]
        ('SerialNumber', TSerialNumber), #动态令牌序列号, char[17]
        ('AuthKey', TAuthKey), #令牌密钥, char[41]
        ('LastDrift', TLastDrift), #漂移值, int
        ('LastSuccess', TLastSuccess), #成功值, int
        ('OTPType', TOTPType), #动态令牌类型, char
    )
class ManualSyncBrokerUserOTP(BaseStruct): #手工同步用户动态令牌
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('OTPType', TOTPType), #动态令牌类型, char
        ('FirstOTP', TPassword), #第一个动态密码, char[41]
        ('SecondOTP', TPassword), #第二个动态密码, char[41]
    )
class ReqOpenAccount(BaseStruct): #转帐开户请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('Gender', TGender), #性别, char
        ('CountryCode', TCountryCode), #国家代码, char[21]
        ('CustType', TCustType), #客户类型, char
        ('Address', TAddress), #地址, char[101]
        ('ZipCode', TZipCode), #邮编, char[7]
        ('Telephone', TTelephone), #电话号码, char[41]
        ('MobilePhone', TMobilePhone), #手机, char[21]
        ('Fax', TFax), #传真, char[41]
        ('EMail', TEMail), #电子邮件, char[41]
        ('MoneyAccountStatus', TMoneyAccountStatus), #资金账户状态, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('CashExchangeCode', TCashExchangeCode), #汇钞标志, char
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('TID', TTID), #交易ID, int
    )
class ReqCancelAccount(BaseStruct): #转帐销户请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('Gender', TGender), #性别, char
        ('CountryCode', TCountryCode), #国家代码, char[21]
        ('CustType', TCustType), #客户类型, char
        ('Address', TAddress), #地址, char[101]
        ('ZipCode', TZipCode), #邮编, char[7]
        ('Telephone', TTelephone), #电话号码, char[41]
        ('MobilePhone', TMobilePhone), #手机, char[21]
        ('Fax', TFax), #传真, char[41]
        ('EMail', TEMail), #电子邮件, char[41]
        ('MoneyAccountStatus', TMoneyAccountStatus), #资金账户状态, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('CashExchangeCode', TCashExchangeCode), #汇钞标志, char
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('TID', TTID), #交易ID, int
    )
class ReqChangeAccount(BaseStruct): #变更银行账户请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('Gender', TGender), #性别, char
        ('CountryCode', TCountryCode), #国家代码, char[21]
        ('CustType', TCustType), #客户类型, char
        ('Address', TAddress), #地址, char[101]
        ('ZipCode', TZipCode), #邮编, char[7]
        ('Telephone', TTelephone), #电话号码, char[41]
        ('MobilePhone', TMobilePhone), #手机, char[21]
        ('Fax', TFax), #传真, char[41]
        ('EMail', TEMail), #电子邮件, char[41]
        ('MoneyAccountStatus', TMoneyAccountStatus), #资金账户状态, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('NewBankAccount', TBankAccount), #新银行帐号, char[41]
        ('NewBankPassWord', TPassword), #新银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('InstallID', TInstallID), #安装编号, int
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('TID', TTID), #交易ID, int
        ('Digest', TDigest), #摘要, char[36]
    )
class ReqTransfer(BaseStruct): #转账请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('FutureSerial', TFutureSerial), #期货公司流水号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('TradeAmount', TTradeAmount), #转帐金额, double
        ('FutureFetchAmount', TTradeAmount), #期货可取金额, double
        ('FeePayFlag', TFeePayFlag), #费用支付标志, char
        ('CustFee', TCustFee), #应收客户费用, double
        ('BrokerFee', TFutureFee), #应收期货公司费用, double
        ('Message', TAddInfo), #发送方给接收方的消息, char[129]
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('TransferStatus', TTransferStatus), #转账交易状态, char
    )
class RspTransfer(BaseStruct): #银行发起银行资金转期货响应
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('FutureSerial', TFutureSerial), #期货公司流水号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('TradeAmount', TTradeAmount), #转帐金额, double
        ('FutureFetchAmount', TTradeAmount), #期货可取金额, double
        ('FeePayFlag', TFeePayFlag), #费用支付标志, char
        ('CustFee', TCustFee), #应收客户费用, double
        ('BrokerFee', TFutureFee), #应收期货公司费用, double
        ('Message', TAddInfo), #发送方给接收方的消息, char[129]
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('TransferStatus', TTransferStatus), #转账交易状态, char
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class ReqRepeal(BaseStruct): #冲正请求
    _fields_ = (
        ('RepealTimeInterval', TRepealTimeInterval), #冲正时间间隔, int
        ('RepealedTimes', TRepealedTimes), #已经冲正次数, int
        ('BankRepealFlag', TBankRepealFlag), #银行冲正标志, char
        ('BrokerRepealFlag', TBrokerRepealFlag), #期商冲正标志, char
        ('PlateRepealSerial', TPlateSerial), #被冲正平台流水号, int
        ('BankRepealSerial', TBankSerial), #被冲正银行流水号, char[13]
        ('FutureRepealSerial', TFutureSerial), #被冲正期货流水号, int
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('FutureSerial', TFutureSerial), #期货公司流水号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('TradeAmount', TTradeAmount), #转帐金额, double
        ('FutureFetchAmount', TTradeAmount), #期货可取金额, double
        ('FeePayFlag', TFeePayFlag), #费用支付标志, char
        ('CustFee', TCustFee), #应收客户费用, double
        ('BrokerFee', TFutureFee), #应收期货公司费用, double
        ('Message', TAddInfo), #发送方给接收方的消息, char[129]
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('TransferStatus', TTransferStatus), #转账交易状态, char
    )
class RspRepeal(BaseStruct): #冲正响应
    _fields_ = (
        ('RepealTimeInterval', TRepealTimeInterval), #冲正时间间隔, int
        ('RepealedTimes', TRepealedTimes), #已经冲正次数, int
        ('BankRepealFlag', TBankRepealFlag), #银行冲正标志, char
        ('BrokerRepealFlag', TBrokerRepealFlag), #期商冲正标志, char
        ('PlateRepealSerial', TPlateSerial), #被冲正平台流水号, int
        ('BankRepealSerial', TBankSerial), #被冲正银行流水号, char[13]
        ('FutureRepealSerial', TFutureSerial), #被冲正期货流水号, int
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('FutureSerial', TFutureSerial), #期货公司流水号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('TradeAmount', TTradeAmount), #转帐金额, double
        ('FutureFetchAmount', TTradeAmount), #期货可取金额, double
        ('FeePayFlag', TFeePayFlag), #费用支付标志, char
        ('CustFee', TCustFee), #应收客户费用, double
        ('BrokerFee', TFutureFee), #应收期货公司费用, double
        ('Message', TAddInfo), #发送方给接收方的消息, char[129]
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('TransferStatus', TTransferStatus), #转账交易状态, char
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class ReqQueryAccount(BaseStruct): #查询账户信息请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('FutureSerial', TFutureSerial), #期货公司流水号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
    )
class RspQueryAccount(BaseStruct): #查询账户信息响应
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('FutureSerial', TFutureSerial), #期货公司流水号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('BankUseAmount', TTradeAmount), #银行可用金额, double
        ('BankFetchAmount', TTradeAmount), #银行可取金额, double
    )
class FutureSignIO(BaseStruct): #期商签到签退
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Digest', TDigest), #摘要, char[36]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
    )
class RspFutureSignIn(BaseStruct): #期商签到响应
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Digest', TDigest), #摘要, char[36]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
        ('PinKey', TPasswordKey), #PIN密钥, char[129]
        ('MacKey', TPasswordKey), #MAC密钥, char[129]
    )
class ReqFutureSignOut(BaseStruct): #期商签退请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Digest', TDigest), #摘要, char[36]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
    )
class RspFutureSignOut(BaseStruct): #期商签退响应
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Digest', TDigest), #摘要, char[36]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class ReqQueryTradeResultBySerial(BaseStruct): #查询指定流水号的交易结果请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('Reference', TSerial), #流水号, int
        ('RefrenceIssureType', TInstitutionType), #本流水号发布者的机构类型, char
        ('RefrenceIssure', TOrganCode), #本流水号发布者机构编码, char[36]
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('TradeAmount', TTradeAmount), #转帐金额, double
        ('Digest', TDigest), #摘要, char[36]
    )
class RspQueryTradeResultBySerial(BaseStruct): #查询指定流水号的交易结果响应
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
        ('Reference', TSerial), #流水号, int
        ('RefrenceIssureType', TInstitutionType), #本流水号发布者的机构类型, char
        ('RefrenceIssure', TOrganCode), #本流水号发布者机构编码, char[36]
        ('OriginReturnCode', TReturnCode), #原始返回代码, char[7]
        ('OriginDescrInfoForReturnCode', TDescrInfoForReturnCode), #原始返回码描述, char[129]
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('TradeAmount', TTradeAmount), #转帐金额, double
        ('Digest', TDigest), #摘要, char[36]
    )
class ReqDayEndFileReady(BaseStruct): #日终文件就绪请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('FileBusinessCode', TFileBusinessCode), #文件业务功能, char
        ('Digest', TDigest), #摘要, char[36]
    )
class ReturnResult(BaseStruct): #返回结果
    _fields_ = (
        ('ReturnCode', TReturnCode), #返回代码, char[7]
        ('DescrInfoForReturnCode', TDescrInfoForReturnCode), #返回码描述, char[129]
    )
class VerifyFuturePassword(BaseStruct): #验证期货资金密码
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('InstallID', TInstallID), #安装编号, int
        ('TID', TTID), #交易ID, int
    )
class VerifyCustInfo(BaseStruct): #验证客户信息
    _fields_ = (
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
    )
class VerifyFuturePasswordAndCustInfo(BaseStruct): #验证期货资金密码和客户信息
    _fields_ = (
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
    )
class DepositResultInform(BaseStruct): #验证期货资金密码和客户信息
    _fields_ = (
        ('DepositSeqNo', TDepositSeqNo), #出入金流水号，该流水号为银期报盘返回的流水号, char[15]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('Deposit', TMoney), #入金金额, double
        ('RequestID', TRequestID), #请求编号, int
        ('ReturnCode', TReturnCode), #返回代码, char[7]
        ('DescrInfoForReturnCode', TDescrInfoForReturnCode), #返回码描述, char[129]
    )
class ReqSyncKey(BaseStruct): #交易核心向银期报盘发出密钥同步请求
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Message', TAddInfo), #交易核心给银期报盘的消息, char[129]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
    )
class RspSyncKey(BaseStruct): #交易核心向银期报盘发出密钥同步响应
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Message', TAddInfo), #交易核心给银期报盘的消息, char[129]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class NotifyQueryAccount(BaseStruct): #查询账户信息通知
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('CustomerName', TIndividualName), #客户姓名, char[51]
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CustType', TCustType), #客户类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankPassWord', TPassword), #银行密码, char[41]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('Password', TPassword), #期货密码, char[41]
        ('FutureSerial', TFutureSerial), #期货公司流水号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('VerifyCertNoFlag', TYesNoIndicator), #验证客户证件号码标志, char
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('Digest', TDigest), #摘要, char[36]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BankSecuAccType', TBankAccType), #期货单位帐号类型, char
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('BankSecuAcc', TBankAccount), #期货单位帐号, char[41]
        ('BankPwdFlag', TPwdFlag), #银行密码标志, char
        ('SecuPwdFlag', TPwdFlag), #期货资金密码核对标志, char
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('BankUseAmount', TTradeAmount), #银行可用金额, double
        ('BankFetchAmount', TTradeAmount), #银行可取金额, double
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class TransferSerial(BaseStruct): #银期转账交易流水表
    _fields_ = (
        ('PlateSerial', TPlateSerial), #平台流水号, int
        ('TradeDate', TTradeDate), #交易发起方日期, char[9]
        ('TradingDay', TDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('TradeCode', TTradeCode), #交易代码, char[7]
        ('SessionID', TSessionID), #会话编号, int
        ('BankID', TBankID), #银行编码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构编码, char[5]
        ('BankAccType', TBankAccType), #银行帐号类型, char
        ('BankAccount', TBankAccount), #银行帐号, char[41]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('BrokerID', TBrokerID), #期货公司编码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('FutureAccType', TFutureAccType), #期货公司帐号类型, char
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('FutureSerial', TFutureSerial), #期货公司流水号, int
        ('IdCardType', TIdCardType), #证件类型, char
        ('IdentifiedCardNo', TIdentifiedCardNo), #证件号码, char[51]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('TradeAmount', TTradeAmount), #交易金额, double
        ('CustFee', TCustFee), #应收客户费用, double
        ('BrokerFee', TFutureFee), #应收期货公司费用, double
        ('AvailabilityFlag', TAvailabilityFlag), #有效标志, char
        ('OperatorCode', TOperatorCode), #操作员, char[17]
        ('BankNewAccount', TBankAccount), #新银行帐号, char[41]
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class QryTransferSerial(BaseStruct): #请求查询转帐流水
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('AccountID', TAccountID), #投资者帐号, char[15]
        ('BankID', TBankID), #银行编码, char[4]
    )
class NotifyFutureSignIn(BaseStruct): #期商签到通知
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Digest', TDigest), #摘要, char[36]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
        ('PinKey', TPasswordKey), #PIN密钥, char[129]
        ('MacKey', TPasswordKey), #MAC密钥, char[129]
    )
class NotifyFutureSignOut(BaseStruct): #期商签退通知
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Digest', TDigest), #摘要, char[36]
        ('CurrencyID', TCurrencyID), #币种代码, char[4]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class NotifySyncKey(BaseStruct): #交易核心向银期报盘发出密钥同步处理结果的通知
    _fields_ = (
        ('TradeCode', TTradeCode), #业务功能码, char[7]
        ('BankID', TBankID), #银行代码, char[4]
        ('BankBranchID', TBankBrchID), #银行分支机构代码, char[5]
        ('BrokerID', TBrokerID), #期商代码, char[11]
        ('BrokerBranchID', TFutureBranchID), #期商分支机构代码, char[31]
        ('TradeDate', TTradeDate), #交易日期, char[9]
        ('TradeTime', TTradeTime), #交易时间, char[9]
        ('BankSerial', TBankSerial), #银行流水号, char[13]
        ('TradingDay', TTradeDate), #交易系统日期 , char[9]
        ('PlateSerial', TSerial), #银期平台消息流水号, int
        ('LastFragment', TLastFragment), #最后分片标志, char
        ('SessionID', TSessionID), #会话号, int
        ('InstallID', TInstallID), #安装编号, int
        ('UserID', TUserID), #用户标识, char[16]
        ('Message', TAddInfo), #交易核心给银期报盘的消息, char[129]
        ('DeviceID', TDeviceID), #渠道标志, char[3]
        ('BrokerIDByBank', TBankCodingForFuture), #期货公司银行编码, char[33]
        ('OperNo', TOperNo), #交易柜员, char[17]
        ('RequestID', TRequestID), #请求编号, int
        ('TID', TTID), #交易ID, int
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class MaxStockPositionAmount(BaseStruct): #客户最大持仓数量
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('InvestorID', TInvestorID), #投资者代码, char[15]
        ('InstrumentID', TInstrumentID), #合约代码, char[31]
        ('MaxAmount', TVolume), #最大持仓数量, int
    )

error = {'NONE':0, 0:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u6b63\u786e'), 'INVALID_DATA_SYNC_STATUS':1, 1:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0d\u5728\u5df2\u540c\u6b65\u72b6\u6001'), 'INCONSISTENT_INFORMATION':2, 2:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4f1a\u8bdd\u4fe1\u606f\u4e0d\u4e00\u81f4'), 'INVALID_LOGIN':3, 3:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0d\u5408\u6cd5\u7684\u767b\u5f55'), 'USER_NOT_ACTIVE':4, 4:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7528\u6237\u4e0d\u6d3b\u8dc3'), 'DUPLICATE_LOGIN':5, 5:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u91cd\u590d\u7684\u767b\u5f55'), 'NOT_LOGIN_YET':6, 6:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8fd8\u6ca1\u6709\u767b\u5f55'), 'NOT_INITED':7, 7:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8fd8\u6ca1\u6709\u521d\u59cb\u5316'), 'FRONT_NOT_ACTIVE':8, 8:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u524d\u7f6e\u4e0d\u6d3b\u8dc3'), 'NO_PRIVILEGE':9, 9:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u65e0\u6b64\u6743\u9650'), 'CHANGE_OTHER_PASSWORD':10, 10:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4fee\u6539\u522b\u4eba\u7684\u53e3\u4ee4'), 'USER_NOT_FOUND':11, 11:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u627e\u4e0d\u5230\u8be5\u7528\u6237'), 'BROKER_NOT_FOUND':12, 12:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u627e\u4e0d\u5230\u8be5\u7ecf\u7eaa\u516c\u53f8'), 'INVESTOR_NOT_FOUND':13, 13:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u627e\u4e0d\u5230\u6295\u8d44\u8005'), 'OLD_PASSWORD_MISMATCH':14, 14:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u539f\u53e3\u4ee4\u4e0d\u5339\u914d'), 'BAD_FIELD':15, 15:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u62a5\u5355\u5b57\u6bb5\u6709\u8bef'), 'INSTRUMENT_NOT_FOUND':16, 16:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u627e\u4e0d\u5230\u5408\u7ea6'), 'INSTRUMENT_NOT_TRADING':17, 17:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u5408\u7ea6\u4e0d\u80fd\u4ea4\u6613'), 'NOT_EXCHANGE_PARTICIPANT':18, 18:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7ecf\u7eaa\u516c\u53f8\u4e0d\u662f\u4ea4\u6613\u6240\u7684\u4f1a\u5458'), 'INVESTOR_NOT_ACTIVE':19, 19:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u6295\u8d44\u8005\u4e0d\u6d3b\u8dc3'), 'NOT_EXCHANGE_CLIENT':20, 20:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u6295\u8d44\u8005\u672a\u5728\u4ea4\u6613\u6240\u5f00\u6237'), 'NO_VALID_TRADER_AVAILABLE':21, 21:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8be5\u4ea4\u6613\u5e2d\u4f4d\u672a\u8fde\u63a5\u5230\u4ea4\u6613\u6240'), 'DUPLICATE_ORDER_REF':22, 22:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u62a5\u5355\u9519\u8bef\uff1a\u4e0d\u5141\u8bb8\u91cd\u590d\u62a5\u5355'), 'BAD_ORDER_ACTION_FIELD':23, 23:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u9519\u8bef\u7684\u62a5\u5355\u64cd\u4f5c\u5b57\u6bb5'), 'DUPLICATE_ORDER_ACTION_REF':24, 24:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u64a4\u5355\u5df2\u62a5\u9001\uff0c\u4e0d\u5141\u8bb8\u91cd\u590d\u64a4\u5355'), 'ORDER_NOT_FOUND':25, 25:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u64a4\u5355\u627e\u4e0d\u5230\u76f8\u5e94\u62a5\u5355'), 'INSUITABLE_ORDER_STATUS':26, 26:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u62a5\u5355\u5df2\u5168\u6210\u4ea4\u6216\u5df2\u64a4\u9500\uff0c\u4e0d\u80fd\u518d\u64a4'), 'UNSUPPORTED_FUNCTION':27, 27:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0d\u652f\u6301\u7684\u529f\u80fd'), 'NO_TRADING_RIGHT':28, 28:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u6ca1\u6709\u62a5\u5355\u4ea4\u6613\u6743\u9650'), 'CLOSE_ONLY':29, 29:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u53ea\u80fd\u5e73\u4ed3'), 'OVER_CLOSE_POSITION':30, 30:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u5e73\u4ed3\u91cf\u8d85\u8fc7\u6301\u4ed3\u91cf'), 'INSUFFICIENT_MONEY':31, 31:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8d44\u91d1\u4e0d\u8db3'), 'DUPLICATE_PK':32, 32:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e3b\u952e\u91cd\u590d'), 'CANNOT_FIND_PK':33, 33:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u627e\u4e0d\u5230\u4e3b\u952e'), 'CAN_NOT_INACTIVE_BROKER':34, 34:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8bbe\u7f6e\u7ecf\u7eaa\u516c\u53f8\u4e0d\u6d3b\u8dc3\u72b6\u6001\u5931\u8d25'), 'BROKER_SYNCHRONIZING':35, 35:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7ecf\u7eaa\u516c\u53f8\u6b63\u5728\u540c\u6b65'), 'BROKER_SYNCHRONIZED':36, 36:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7ecf\u7eaa\u516c\u53f8\u5df2\u540c\u6b65'), 'SHORT_SELL':37, 37:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u53ef\u5356\u51fa\u6570\u91cf\u4e0d\u8db3'), 'INVALID_SETTLEMENT_REF':38, 38:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0d\u5408\u6cd5\u7684\u7ed3\u7b97\u5f15\u7528'), 'CFFEX_NETWORK_ERROR':39, 39:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e2d\u91d1\u6240\u7f51\u7edc\u8fde\u63a5\u5931\u8d25'), 'CFFEX_OVER_REQUEST':40, 40:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e2d\u91d1\u6240\u672a\u5904\u7406\u8bf7\u6c42\u8d85\u8fc7\u8bb8\u53ef\u6570'), 'CFFEX_OVER_REQUEST_PER_SECOND':41, 41:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e2d\u91d1\u6240\u6bcf\u79d2\u53d1\u9001\u8bf7\u6c42\u6570\u8d85\u8fc7\u8bb8\u53ef\u6570'), 'SETTLEMENT_INFO_NOT_CONFIRMED':42, 42:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7ed3\u7b97\u7ed3\u679c\u672a\u786e\u8ba4'), 'DEPOSIT_NOT_FOUND':43, 43:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u6ca1\u6709\u5bf9\u5e94\u7684\u5165\u91d1\u8bb0\u5f55'), 'EXCHANG_TRADING':44, 44:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4ea4\u6613\u6240\u5df2\u7ecf\u8fdb\u5165\u8fde\u7eed\u4ea4\u6613\u72b6\u6001'), 'PARKEDORDER_NOT_FOUND':45, 45:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u627e\u4e0d\u5230\u9884\u57cb\uff08\u64a4\u5355\uff09\u5355'), 'PARKEDORDER_HASSENDED':46, 46:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u9884\u57cb\uff08\u64a4\u5355\uff09\u5355\u5df2\u7ecf\u53d1\u9001'), 'PARKEDORDER_HASDELETE':47, 47:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u9884\u57cb\uff08\u64a4\u5355\uff09\u5355\u5df2\u7ecf\u5220\u9664'), 'INVALID_INVESTORIDORPASSWORD':48, 48:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u65e0\u6548\u7684\u6295\u8d44\u8005\u6216\u8005\u5bc6\u7801'), 'INVALID_LOGIN_IPADDRESS':49, 49:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0d\u5408\u6cd5\u7684\u767b\u5f55IP\u5730\u5740'), 'OVER_CLOSETODAY_POSITION':50, 50:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u5e73\u4eca\u4ed3\u4f4d\u4e0d\u8db3'), 'OVER_CLOSEYESTERDAY_POSITION':51, 51:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u5e73\u6628\u4ed3\u4f4d\u4e0d\u8db3'), 'BROKER_NOT_ENOUGH_CONDORDER':52, 52:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7ecf\u7eaa\u516c\u53f8\u6ca1\u6709\u8db3\u591f\u53ef\u7528\u7684\u6761\u4ef6\u5355\u6570\u91cf'), 'INVESTOR_NOT_ENOUGH_CONDORDER':53, 53:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u6295\u8d44\u8005\u6ca1\u6709\u8db3\u591f\u53ef\u7528\u7684\u6761\u4ef6\u5355\u6570\u91cf'), 'BROKER_NOT_SUPPORT_CONDORDER':54, 54:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7ecf\u7eaa\u516c\u53f8\u4e0d\u652f\u6301\u6761\u4ef6\u5355'), 'RESEND_ORDER_BROKERINVESTOR_NOTMATCH':55, 55:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u91cd\u53d1\u672a\u77e5\u5355\u7ecf\u6d4e\u516c\u53f8/\u6295\u8d44\u8005\u4e0d\u5339\u914d'), 'SYC_OTP_FAILED':56, 56:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u540c\u6b65\u52a8\u6001\u4ee4\u724c\u5931\u8d25'), 'OTP_MISMATCH':57, 57:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u52a8\u6001\u4ee4\u724c\u6821\u9a8c\u9519\u8bef'), 'OTPPARAM_NOT_FOUND':58, 58:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u627e\u4e0d\u5230\u52a8\u6001\u4ee4\u724c\u914d\u7f6e\u4fe1\u606f'), 'UNSUPPORTED_OTPTYPE':59, 59:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0d\u652f\u6301\u7684\u52a8\u6001\u4ee4\u724c\u7c7b\u578b'), 'MARKETDATA_NOT_FOUND':60, 60:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7f3a\u5c11\u9700\u8981\u7684\u8bc1\u5238\u884c\u60c5'), 'AUTH_FAILED':61, 61:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u5ba2\u6237\u7aef\u8ba4\u8bc1\u5931\u8d25'), 'NOT_AUTHENT':62, 62:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u5ba2\u6237\u7aef\u672a\u8ba4\u8bc1'), 'SEND_INSTITUTION_CODE_ERROR':1000, 1000:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u53d1\u9001\u673a\u6784\u4ee3\u7801\u9519\u8bef'), 'NO_GET_PLATFORM_SN':1001, 1001:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u53d6\u5e73\u53f0\u6d41\u6c34\u53f7\u9519\u8bef'), 'ILLEGAL_TRANSFER_BANK':1002, 1002:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u4e0d\u5408\u6cd5\u7684\u8f6c\u8d26\u94f6\u884c'), 'ALREADY_OPEN_ACCOUNT':1003, 1003:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u5df2\u7ecf\u5f00\u6237'), 'NOT_OPEN_ACCOUNT':1004, 1004:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u672a\u5f00\u6237'), 'PROCESSING':1005, 1005:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u5904\u7406\u4e2d'), 'OVERTIME':1006, 1006:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u4ea4\u6613\u8d85\u65f6'), 'RECORD_NOT_FOUND':1007, 1007:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u627e\u4e0d\u5230\u8bb0\u5f55'), 'NO_FOUND_REVERSAL_ORIGINAL_TRANSACTION':1008, 1008:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u627e\u4e0d\u5230\u88ab\u51b2\u6b63\u7684\u539f\u59cb\u4ea4\u6613'), 'CONNECT_HOST_FAILED':1009, 1009:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u8fde\u63a5\u4e3b\u673a\u5931\u8d25'), 'SEND_FAILED':1010, 1010:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u53d1\u9001\u5931\u8d25'), 'LATE_RESPONSE':1011, 1011:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u8fdf\u5230\u5e94\u7b54'), 'REVERSAL_BANKID_NOT_MATCH':1012, 1012:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u51b2\u6b63\u4ea4\u6613\u94f6\u884c\u4ee3\u7801\u9519\u8bef'), 'REVERSAL_BANKACCOUNT_NOT_MATCH':1013, 1013:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u51b2\u6b63\u4ea4\u6613\u94f6\u884c\u8d26\u6237\u9519\u8bef'), 'REVERSAL_BROKERID_NOT_MATCH':1014, 1014:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u51b2\u6b63\u4ea4\u6613\u7ecf\u7eaa\u516c\u53f8\u4ee3\u7801\u9519\u8bef'), 'REVERSAL_ACCOUNTID_NOT_MATCH':1015, 1015:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u51b2\u6b63\u4ea4\u6613\u8d44\u91d1\u8d26\u6237\u9519\u8bef'), 'REVERSAL_AMOUNT_NOT_MATCH':1016, 1016:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u51b2\u6b63\u4ea4\u6613\u4ea4\u6613\u91d1\u989d\u9519\u8bef'), 'DB_OPERATION_FAILED':1017, 1017:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u6570\u636e\u5e93\u64cd\u4f5c\u9519\u8bef'), 'SEND_ASP_FAILURE':1018, 1018:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u53d1\u9001\u5230\u4ea4\u6613\u7cfb\u7edf\u5931\u8d25'), 'NOT_SIGNIN':1019, 1019:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u6ca1\u6709\u7b7e\u5230'), 'ALREADY_SIGNIN':1020, 1020:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u5df2\u7ecf\u7b7e\u5230'), 'AMOUNT_OR_TIMES_OVER':1021, 1021:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u91d1\u989d\u6216\u6b21\u6570\u8d85\u9650'), 'NOT_IN_TRANSFER_TIME':1022, 1022:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u8fd9\u4e00\u65f6\u95f4\u6bb5\u4e0d\u80fd\u8f6c\u8d26'), 'BANK_SERVER_ERROR':1023, 1023:u('\u94f6\u884c\u4e3b\u673a\u9519'), 'BANK_SERIAL_IS_REPEALED':1024, 1024:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u94f6\u884c\u5df2\u7ecf\u51b2\u6b63'), 'BANK_SERIAL_NOT_EXIST':1025, 1025:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u94f6\u884c\u6d41\u6c34\u4e0d\u5b58\u5728'), 'NOT_ORGAN_MAP':1026, 1026:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u673a\u6784\u6ca1\u6709\u7b7e\u7ea6'), 'EXIST_TRANSFER':1027, 1027:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u5b58\u5728\u8f6c\u8d26\uff0c\u4e0d\u80fd\u9500\u6237'), 'BANK_FORBID_REVERSAL':1028, 1028:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u94f6\u884c\u4e0d\u652f\u6301\u51b2\u6b63'), 'DUP_BANK_SERIAL':1029, 1029:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u91cd\u590d\u7684\u94f6\u884c\u6d41\u6c34'), 'FBT_SYSTEM_BUSY':1030, 1030:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u8f6c\u8d26\u7cfb\u7edf\u5fd9\uff0c\u7a0d\u540e\u518d\u8bd5'), 'MACKEY_SYNCING':1031, 1031:u('\u94f6\u671f\u8f6c\u8d26\uff1aMAC\u5bc6\u94a5\u6b63\u5728\u540c\u6b65'), 'ACCOUNTID_ALREADY_REGISTER':1032, 1032:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u8d44\u91d1\u8d26\u6237\u5df2\u7ecf\u767b\u8bb0'), 'BANKACCOUNT_ALREADY_REGISTER':1033, 1033:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u94f6\u884c\u8d26\u6237\u5df2\u7ecf\u767b\u8bb0'), 'DUP_BANK_SERIAL_REDO_OK':1034, 1034:u('\u94f6\u671f\u8f6c\u8d26\uff1a\u91cd\u590d\u7684\u94f6\u884c\u6d41\u6c34,\u91cd\u53d1\u6210\u529f'), 'NO_VALID_BANKOFFER_AVAILABLE':2000, 2000:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8be5\u62a5\u76d8\u672a\u8fde\u63a5\u5230\u94f6\u884c'), 'PASSWORD_MISMATCH':2001, 2001:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8d44\u91d1\u5bc6\u7801\u9519\u8bef'), 'DUPLATION_BANK_SERIAL':2004, 2004:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u94f6\u884c\u6d41\u6c34\u53f7\u91cd\u590d'), 'DUPLATION_OFFER_SERIAL':2005, 2005:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u62a5\u76d8\u6d41\u6c34\u53f7\u91cd\u590d'), 'SERIAL_NOT_EXSIT':2006, 2006:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u88ab\u51b2\u6b63\u6d41\u6c34\u4e0d\u5b58\u5728(\u51b2\u6b63\u4ea4\u6613)'), 'SERIAL_IS_REPEALED':2007, 2007:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u539f\u6d41\u6c34\u5df2\u51b2\u6b63(\u51b2\u6b63\u4ea4\u6613)'), 'SERIAL_MISMATCH':2008, 2008:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0e\u539f\u6d41\u6c34\u4fe1\u606f\u4e0d\u7b26(\u51b2\u6b63\u4ea4\u6613)'), 'IdentifiedCardNo_MISMATCH':2009, 2009:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8bc1\u4ef6\u53f7\u7801\u6216\u7c7b\u578b\u9519\u8bef'), 'ACCOUNT_NOT_FUND':2011, 2011:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8d44\u91d1\u8d26\u6237\u4e0d\u5b58\u5728'), 'ACCOUNT_NOT_ACTIVE':2012, 2012:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8d44\u91d1\u8d26\u6237\u5df2\u7ecf\u9500\u6237'), 'NOT_ALLOW_REPEAL_BYMANUAL':2013, 2013:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8be5\u4ea4\u6613\u4e0d\u80fd\u6267\u884c\u624b\u5de5\u51b2\u6b63'), 'AMOUNT_OUTOFTHEWAY':2014, 2014:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u8f6c\u5e10\u91d1\u989d\u9519\u8bef'), 'WAITING_OFFER_RSP':999999, 999999:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u7b49\u5f85\u94f6\u671f\u62a5\u76d8\u5904\u7406\u7ed3\u679c'), 'NON_TRADALE_STOCK_VOLUME_PRICE_NOTMACTH':3000, 3000:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u975e\u4ea4\u6613\u62a5\u5355\u4ef7\u683c\u6570\u91cf\u548c\u4e1a\u52a1\u4e0d\u5339\u914d'), 'INVALID_PRODUCT':3001, 3001:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u627e\u4e0d\u5230\u4ea7\u54c1\u4fe1\u606f'), 'INVALID_BUY_VOLUME':3002, 3002:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0d\u5408\u6cd5\u7684\u4e70\u5165\u6570\u91cf'), 'INVALID_SELL_VOLUME':3003, 3003:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e0d\u5408\u6cd5\u7684\u5356\u51fa\u6570\u91cf'), 'ONLY_ETF_CAN_PURRED':3004, 3004:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u975eETF\u4ea7\u54c1\u4e0d\u80fd\u7533\u8d2d\u8d4e\u56de'), 'INVALID_ETF_VOLUME':3005, 3005:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1aETF\u7533\u8d2d\u8d4e\u56de\u6570\u91cf\u9519\u8bef'), 'NOT_ENOUGH_ETF_PUR_VOLUME':3006, 3006:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1aETF\u7533\u8d2d\u65e0\u8db3\u591f\u80a1\u7968'), 'NOT_ENOUGH_ETF_RED_VOLUME':3007, 3007:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1aETF\u8d4e\u56de\u65e0\u8db3\u591f\u57fa\u91d1'), 'UNAUTHENTNOTVALIDFORTRADE':3008, 3008:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u672a\u8ba4\u8bc1\u7684\u7528\u6237\u6ca1\u6709\u4e0b\u5355\u6743\u9650'), 'OVERAMOUNTLIMIT':3009, 3009:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u4e70\u5165\u8d85\u8fc7\u6301\u4ed3\u6570\u91cf\u9650\u5236'), 'OVERETFCASHRATIO':3010, 3010:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u73b0\u91d1\u66ff\u6362\u91d1\u989d\u8d85\u8fc7\u9650\u5236'), 'ETF_PURRED_NOTSUPCALCEL':3011, 3011:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1aETF\u7533\u8d4e\u4e0d\u80fd\u64a4\u5355'), 'INVALID_FOR_CREDITACCOUNT':3012, 3012:u('\u7efc\u5408\u4ea4\u6613\u5e73\u53f0\uff1a\u975e\u4fe1\u7528\u8d26\u6237\u4e0d\u652f\u6301\u6b64\u7c7b\u4ea4\u6613')}

def _init(export=_init):
    env = globals()
    for k in list(env):
        if k not in export: del env[k]
_init()
