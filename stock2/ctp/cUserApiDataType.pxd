# -*- coding: utf-8 -*-

cdef extern from "ThostFtdcUserApiDataTypeSSE.h":
    cdef enum TE_RESUME_TYPE "ZQTHOST_TE_RESUME_TYPE": #流重传方式
        TERT_RESTART "THOST_TERT_RESTART" #从本交易日开始重传
        TERT_RESUME "THOST_TERT_RESUME" #从上次收到的续传
        TERT_QUICK "THOST_TERT_QUICK" #只传送登录后的流内容
    ctypedef char[21] TTraderIDType "TZQThostFtdcTraderIDType" #交易所交易员代码
    ctypedef char[15] TInvestorIDType "TZQThostFtdcInvestorIDType" #投资者代码
    ctypedef char[11] TBrokerIDType "TZQThostFtdcBrokerIDType" #经纪公司代码
    ctypedef char[9] TBrokerAbbrType "TZQThostFtdcBrokerAbbrType" #经纪公司简称
    ctypedef char[81] TBrokerNameType "TZQThostFtdcBrokerNameType" #经纪公司名称
    ctypedef char[31] TExchangeInstIDType "TZQThostFtdcExchangeInstIDType" #合约在交易所的代码
    ctypedef char[13] TOrderRefType "TZQThostFtdcOrderRefType" #报单引用
    ctypedef char[11] TParticipantIDType "TZQThostFtdcParticipantIDType" #会员代码
    ctypedef char[16] TUserIDType "TZQThostFtdcUserIDType" #用户代码
    ctypedef char[41] TPasswordType "TZQThostFtdcPasswordType" #密码
    ctypedef char[11] TClientIDType "TZQThostFtdcClientIDType" #交易编码
    ctypedef char[31] TInstrumentIDType "TZQThostFtdcInstrumentIDType" #合约代码
    ctypedef char[31] TMarketIDType "TZQThostFtdcMarketIDType" #市场代码
    ctypedef char[21] TProductNameType "TZQThostFtdcProductNameType" #产品名称
    ctypedef char[9] TExchangeIDType "TZQThostFtdcExchangeIDType" #交易所代码
    ctypedef char[31] TExchangeNameType "TZQThostFtdcExchangeNameType" #交易所名称
    ctypedef char[9] TExchangeAbbrType "TZQThostFtdcExchangeAbbrType" #交易所简称
    ctypedef char[2] TExchangeFlagType "TZQThostFtdcExchangeFlagType" #交易所标志
    ctypedef char[21] TMacAddressType "TZQThostFtdcMacAddressType" #Mac地址
    ctypedef char TExchangePropertyType "TZQThostFtdcExchangePropertyType" #交易所属性
    enum: EXP_Normal "THOST_FTDC_EXP_Normal" #正常
    enum: EXP_GenOrderByTrade "THOST_FTDC_EXP_GenOrderByTrade" #根据成交生成报单
    ctypedef char[9] TDateType "TZQThostFtdcDateType" #日期
    ctypedef char[9] TTimeType "TZQThostFtdcTimeType" #时间
    ctypedef char[13] TLongTimeType "TZQThostFtdcLongTimeType" #长时间
    ctypedef char[21] TInstrumentNameType "TZQThostFtdcInstrumentNameType" #合约名称
    ctypedef char[9] TSettlementGroupIDType "TZQThostFtdcSettlementGroupIDType" #结算组代码
    ctypedef char[21] TOrderSysIDType "TZQThostFtdcOrderSysIDType" #报单编号
    ctypedef char[21] TTradeIDType "TZQThostFtdcTradeIDType" #成交编号
    ctypedef char[65] TCommandTypeType "TZQThostFtdcCommandTypeType" #DB命令类型
    ctypedef char[16] TIPAddressType "TZQThostFtdcIPAddressType" #IP地址
    ctypedef char[11] TProductInfoType "TZQThostFtdcProductInfoType" #产品信息
    ctypedef char[11] TProtocolInfoType "TZQThostFtdcProtocolInfoType" #协议信息
    ctypedef char[21] TBusinessUnitType "TZQThostFtdcBusinessUnitType" #业务单元
    ctypedef char[15] TDepositSeqNoType "TZQThostFtdcDepositSeqNoType" #出入金流水号
    ctypedef char[51] TIdentifiedCardNoType "TZQThostFtdcIdentifiedCardNoType" #证件号码
    ctypedef char TIdCardTypeType "TZQThostFtdcIdCardTypeType" #证件类型
    enum: ICT_EID "THOST_FTDC_ICT_EID" #组织机构代码
    enum: ICT_IDCard "THOST_FTDC_ICT_IDCard" #身份证
    enum: ICT_OfficerIDCard "THOST_FTDC_ICT_OfficerIDCard" #军官证
    enum: ICT_PoliceIDCard "THOST_FTDC_ICT_PoliceIDCard" #警官证
    enum: ICT_SoldierIDCard "THOST_FTDC_ICT_SoldierIDCard" #士兵证
    enum: ICT_HouseholdRegister "THOST_FTDC_ICT_HouseholdRegister" #户口簿
    enum: ICT_Passport "THOST_FTDC_ICT_Passport" #护照
    enum: ICT_TaiwanCompatriotIDCard "THOST_FTDC_ICT_TaiwanCompatriotIDCard" #台胞证
    enum: ICT_HomeComingCard "THOST_FTDC_ICT_HomeComingCard" #回乡证
    enum: ICT_LicenseNo "THOST_FTDC_ICT_LicenseNo" #营业执照号
    enum: ICT_OtherCard "THOST_FTDC_ICT_OtherCard" #其他证件
    ctypedef char[13] TOrderLocalIDType "TZQThostFtdcOrderLocalIDType" #本地报单编号
    ctypedef char[81] TUserNameType "TZQThostFtdcUserNameType" #用户名称
    ctypedef char[81] TPartyNameType "TZQThostFtdcPartyNameType" #参与人名称
    ctypedef char[81] TErrorMsgType "TZQThostFtdcErrorMsgType" #错误信息
    ctypedef char[2049] TFieldNameType "TZQThostFtdcFieldNameType" #字段名
    ctypedef char[2049] TFieldContentType "TZQThostFtdcFieldContentType" #字段内容
    ctypedef char[41] TSystemNameType "TZQThostFtdcSystemNameType" #系统名称
    ctypedef char[501] TContentType "TZQThostFtdcContentType" #消息正文
    ctypedef char TInvestorRangeType "TZQThostFtdcInvestorRangeType" #投资者范围
    enum: IR_All "THOST_FTDC_IR_All" #所有
    enum: IR_Group "THOST_FTDC_IR_Group" #投资者组
    enum: IR_Single "THOST_FTDC_IR_Single" #单一投资者
    ctypedef char TDepartmentRangeType "TZQThostFtdcDepartmentRangeType" #投资者范围
    enum: DR_All "THOST_FTDC_DR_All" #所有
    enum: DR_Group "THOST_FTDC_DR_Group" #组织架构
    enum: DR_Single "THOST_FTDC_DR_Single" #单一投资者
    ctypedef char TDataSyncStatusType "TZQThostFtdcDataSyncStatusType" #数据同步状态
    enum: DS_Asynchronous "THOST_FTDC_DS_Asynchronous" #未同步
    enum: DS_Synchronizing "THOST_FTDC_DS_Synchronizing" #同步中
    enum: DS_Synchronized "THOST_FTDC_DS_Synchronized" #已同步
    ctypedef char TBrokerDataSyncStatusType "TZQThostFtdcBrokerDataSyncStatusType" #经纪公司数据同步状态
    enum: BDS_Synchronized "THOST_FTDC_BDS_Synchronized" #已同步
    enum: BDS_Synchronizing "THOST_FTDC_BDS_Synchronizing" #同步中
    ctypedef char TExchangeConnectStatusType "TZQThostFtdcExchangeConnectStatusType" #交易所连接状态
    enum: ECS_NoConnection "THOST_FTDC_ECS_NoConnection" #没有任何连接
    enum: ECS_QryInstrumentSent "THOST_FTDC_ECS_QryInstrumentSent" #已经发出合约查询请求
    enum: ECS_GotInformation "THOST_FTDC_ECS_GotInformation" #已经获取信息
    ctypedef char TTraderConnectStatusType "TZQThostFtdcTraderConnectStatusType" #交易所交易员连接状态
    enum: TCS_NotConnected "THOST_FTDC_TCS_NotConnected" #没有任何连接
    enum: TCS_Connected "THOST_FTDC_TCS_Connected" #已经连接
    enum: TCS_QryInstrumentSent "THOST_FTDC_TCS_QryInstrumentSent" #已经发出合约查询请求
    enum: TCS_SubPrivateFlow "THOST_FTDC_TCS_SubPrivateFlow" #订阅私有流
    ctypedef char TFunctionCodeType "TZQThostFtdcFunctionCodeType" #功能代码
    enum: FC_DataAsync "THOST_FTDC_FC_DataAsync" #数据异步化
    enum: FC_ForceUserLogout "THOST_FTDC_FC_ForceUserLogout" #强制用户登出
    enum: FC_UserPasswordUpdate "THOST_FTDC_FC_UserPasswordUpdate" #变更管理用户口令
    enum: FC_BrokerPasswordUpdate "THOST_FTDC_FC_BrokerPasswordUpdate" #变更经纪公司口令
    enum: FC_InvestorPasswordUpdate "THOST_FTDC_FC_InvestorPasswordUpdate" #变更投资者口令
    enum: FC_OrderInsert "THOST_FTDC_FC_OrderInsert" #报单插入
    enum: FC_OrderAction "THOST_FTDC_FC_OrderAction" #报单操作
    enum: FC_SyncSystemData "THOST_FTDC_FC_SyncSystemData" #同步系统数据
    enum: FC_SyncBrokerData "THOST_FTDC_FC_SyncBrokerData" #同步经纪公司数据
    enum: FC_BachSyncBrokerData "THOST_FTDC_FC_BachSyncBrokerData" #批量同步经纪公司数据
    enum: FC_SuperQuery "THOST_FTDC_FC_SuperQuery" #超级查询
    enum: FC_ParkedOrderInsert "THOST_FTDC_FC_ParkedOrderInsert" #报单插入
    enum: FC_ParkedOrderAction "THOST_FTDC_FC_ParkedOrderAction" #报单操作
    enum: FC_SyncOTP "THOST_FTDC_FC_SyncOTP" #同步动态令牌
    ctypedef char TBrokerFunctionCodeType "TZQThostFtdcBrokerFunctionCodeType" #经纪公司功能代码
    enum: BFC_ForceUserLogout "THOST_FTDC_BFC_ForceUserLogout" #强制用户登出
    enum: BFC_UserPasswordUpdate "THOST_FTDC_BFC_UserPasswordUpdate" #变更用户口令
    enum: BFC_SyncBrokerData "THOST_FTDC_BFC_SyncBrokerData" #同步经纪公司数据
    enum: BFC_BachSyncBrokerData "THOST_FTDC_BFC_BachSyncBrokerData" #批量同步经纪公司数据
    enum: BFC_OrderInsert "THOST_FTDC_BFC_OrderInsert" #报单插入
    enum: BFC_OrderAction "THOST_FTDC_BFC_OrderAction" #报单操作
    enum: BFC_AllQuery "THOST_FTDC_BFC_AllQuery" #全部查询
    enum: BFC_log "THOST_FTDC_BFC_log" #系统功能：登入/登出/修改密码等
    enum: BFC_BaseQry "THOST_FTDC_BFC_BaseQry" #基本查询：查询基础数据，如合约，交易所等常量
    enum: BFC_TradeQry "THOST_FTDC_BFC_TradeQry" #交易查询：如查成交，委托
    enum: BFC_Trade "THOST_FTDC_BFC_Trade" #交易功能：报单，撤单
    enum: BFC_Virement "THOST_FTDC_BFC_Virement" #银期转账
    enum: BFC_Risk "THOST_FTDC_BFC_Risk" #风险监控
    enum: BFC_Session "THOST_FTDC_BFC_Session" #查询/管理：查询会话，踢人等
    enum: BFC_RiskNoticeCtl "THOST_FTDC_BFC_RiskNoticeCtl" #风控通知控制
    enum: BFC_RiskNotice "THOST_FTDC_BFC_RiskNotice" #风控通知发送
    enum: BFC_BrokerDeposit "THOST_FTDC_BFC_BrokerDeposit" #察看经纪公司资金权限
    enum: BFC_QueryFund "THOST_FTDC_BFC_QueryFund" #资金查询
    enum: BFC_QueryOrder "THOST_FTDC_BFC_QueryOrder" #报单查询
    enum: BFC_QueryTrade "THOST_FTDC_BFC_QueryTrade" #成交查询
    enum: BFC_QueryPosition "THOST_FTDC_BFC_QueryPosition" #持仓查询
    enum: BFC_QueryMarketData "THOST_FTDC_BFC_QueryMarketData" #行情查询
    enum: BFC_QueryUserEvent "THOST_FTDC_BFC_QueryUserEvent" #用户事件查询
    enum: BFC_QueryRiskNotify "THOST_FTDC_BFC_QueryRiskNotify" #风险通知查询
    enum: BFC_QueryFundChange "THOST_FTDC_BFC_QueryFundChange" #出入金查询
    enum: BFC_QueryInvestor "THOST_FTDC_BFC_QueryInvestor" #投资者信息查询
    enum: BFC_QueryTradingCode "THOST_FTDC_BFC_QueryTradingCode" #交易编码查询
    enum: BFC_ForceClose "THOST_FTDC_BFC_ForceClose" #强平
    enum: BFC_PressTest "THOST_FTDC_BFC_PressTest" #压力测试
    enum: BFC_RemainCalc "THOST_FTDC_BFC_RemainCalc" #权益反算
    enum: BFC_NetPositionInd "THOST_FTDC_BFC_NetPositionInd" #净持仓保证金指标
    enum: BFC_RiskPredict "THOST_FTDC_BFC_RiskPredict" #风险预算
    enum: BFC_DataExport "THOST_FTDC_BFC_DataExport" #数据导出
    enum: BFC_RiskTargetSetup "THOST_FTDC_BFC_RiskTargetSetup" #风控指标设置
    enum: BFC_SyncOTP "THOST_FTDC_BFC_SyncOTP" #同步动态令牌
    ctypedef char TOrderActionStatusType "TZQThostFtdcOrderActionStatusType" #报单操作状态
    enum: OAS_Submitted "THOST_FTDC_OAS_Submitted" #已经提交
    enum: OAS_Accepted "THOST_FTDC_OAS_Accepted" #已经接受
    enum: OAS_Rejected "THOST_FTDC_OAS_Rejected" #已经被拒绝
    ctypedef char TOrderStatusType "TZQThostFtdcOrderStatusType" #报单状态
    enum: OST_AllTraded "THOST_FTDC_OST_AllTraded" #全部成交
    enum: OST_PartTradedQueueing "THOST_FTDC_OST_PartTradedQueueing" #部分成交还在队列中
    enum: OST_PartTradedNotQueueing "THOST_FTDC_OST_PartTradedNotQueueing" #部分成交不在队列中
    enum: OST_NoTradeQueueing "THOST_FTDC_OST_NoTradeQueueing" #未成交还在队列中
    enum: OST_NoTradeNotQueueing "THOST_FTDC_OST_NoTradeNotQueueing" #未成交不在队列中
    enum: OST_Canceled "THOST_FTDC_OST_Canceled" #撤单
    enum: OST_Unknown "THOST_FTDC_OST_Unknown" #未知
    enum: OST_NotTouched "THOST_FTDC_OST_NotTouched" #尚未触发
    enum: OST_Touched "THOST_FTDC_OST_Touched" #已触发
    ctypedef char TOrderSubmitStatusType "TZQThostFtdcOrderSubmitStatusType" #报单提交状态
    enum: OSS_InsertSubmitted "THOST_FTDC_OSS_InsertSubmitted" #已经提交
    enum: OSS_CancelSubmitted "THOST_FTDC_OSS_CancelSubmitted" #撤单已经提交
    enum: OSS_ModifySubmitted "THOST_FTDC_OSS_ModifySubmitted" #修改已经提交
    enum: OSS_Accepted "THOST_FTDC_OSS_Accepted" #已经接受
    enum: OSS_InsertRejected "THOST_FTDC_OSS_InsertRejected" #报单已经被拒绝
    enum: OSS_CancelRejected "THOST_FTDC_OSS_CancelRejected" #撤单已经被拒绝
    enum: OSS_ModifyRejected "THOST_FTDC_OSS_ModifyRejected" #改单已经被拒绝
    ctypedef char TPositionDateType "TZQThostFtdcPositionDateType" #持仓日期
    enum: PSD_Today "THOST_FTDC_PSD_Today" #今日持仓
    enum: PSD_History "THOST_FTDC_PSD_History" #历史持仓
    ctypedef char TPositionDateTypeType "TZQThostFtdcPositionDateTypeType" #持仓日期类型
    enum: PDT_UseHistory "THOST_FTDC_PDT_UseHistory" #使用历史持仓
    enum: PDT_NoUseHistory "THOST_FTDC_PDT_NoUseHistory" #不使用历史持仓
    ctypedef char TTradingRoleType "TZQThostFtdcTradingRoleType" #交易角色
    enum: ER_Broker "THOST_FTDC_ER_Broker" #代理
    enum: ER_Host "THOST_FTDC_ER_Host" #自营
    enum: ER_Maker "THOST_FTDC_ER_Maker" #做市商
    ctypedef char TProductClassType "TZQThostFtdcProductClassType" #产品类型
    enum: PC_Futures "THOST_FTDC_PC_Futures" #期货
    enum: PC_Options "THOST_FTDC_PC_Options" #期权
    enum: PC_Combination "THOST_FTDC_PC_Combination" #组合
    enum: PC_Spot "THOST_FTDC_PC_Spot" #即期
    enum: PC_EFP "THOST_FTDC_PC_EFP" #期转现
    enum: PC_StockA "THOST_FTDC_PC_StockA" #证券A股
    enum: PC_StockB "THOST_FTDC_PC_StockB" #证券B股
    enum: PC_ETF "THOST_FTDC_PC_ETF" #ETF
    enum: PC_ETFPurRed "THOST_FTDC_PC_ETFPurRed" #ETF申赎
    ctypedef char TInstLifePhaseType "TZQThostFtdcInstLifePhaseType" #合约生命周期状态
    enum: IP_NotStart "THOST_FTDC_IP_NotStart" #未上市
    enum: IP_Started "THOST_FTDC_IP_Started" #上市
    enum: IP_Pause "THOST_FTDC_IP_Pause" #停牌
    enum: IP_Expired "THOST_FTDC_IP_Expired" #到期
    ctypedef char TDirectionType "TZQThostFtdcDirectionType" #买卖方向
    enum: D_Buy "THOST_FTDC_D_Buy" #买
    enum: D_Sell "THOST_FTDC_D_Sell" #卖
    enum: D_ETFPur "THOST_FTDC_D_ETFPur" #ETF申购
    enum: D_ETFRed "THOST_FTDC_D_ETFRed" #ETF赎回
    enum: D_MarginTrade "THOST_FTDC_D_MarginTrade" #融资买入
    enum: D_ShortSell "THOST_FTDC_D_ShortSell" #融券卖出
    enum: D_RepayMargin "THOST_FTDC_D_RepayMargin" #卖券还款
    enum: D_RepayStock "THOST_FTDC_D_RepayStock" #买券还券
    enum: D_DirectRepayMargin "THOST_FTDC_D_DirectRepayMargin" #直接还款
    enum: D_DirectRepayStock "THOST_FTDC_D_DirectRepayStock" #直接还券
    enum: D_TransferSecurities "THOST_FTDC_D_TransferSecurities" #担保品划转
    ctypedef char TPositionTypeType "TZQThostFtdcPositionTypeType" #持仓类型
    enum: PT_Net "THOST_FTDC_PT_Net" #净持仓
    enum: PT_Gross "THOST_FTDC_PT_Gross" #综合持仓
    ctypedef char TPosiDirectionType "TZQThostFtdcPosiDirectionType" #持仓多空方向
    enum: PD_Net "THOST_FTDC_PD_Net" #净
    enum: PD_Long "THOST_FTDC_PD_Long" #多头
    enum: PD_Short "THOST_FTDC_PD_Short" #空头
    enum: PD_MarginTrade "THOST_FTDC_PD_MarginTrade" #融资
    enum: PD_ShortSell "THOST_FTDC_PD_ShortSell" #融券
    ctypedef char TSysSettlementStatusType "TZQThostFtdcSysSettlementStatusType" #系统结算状态
    enum: SS_NonActive "THOST_FTDC_SS_NonActive" #不活跃
    enum: SS_Startup "THOST_FTDC_SS_Startup" #启动
    enum: SS_Operating "THOST_FTDC_SS_Operating" #操作
    enum: SS_Settlement "THOST_FTDC_SS_Settlement" #结算
    enum: SS_SettlementFinished "THOST_FTDC_SS_SettlementFinished" #结算完成
    ctypedef char TRatioAttrType "TZQThostFtdcRatioAttrType" #费率属性
    enum: RA_Trade "THOST_FTDC_RA_Trade" #交易费率
    enum: RA_Settlement "THOST_FTDC_RA_Settlement" #结算费率
    ctypedef char THedgeFlagType "TZQThostFtdcHedgeFlagType" #投机套保标志
    enum: HF_Speculation "THOST_FTDC_HF_Speculation" #投机
    enum: HF_Hedge "THOST_FTDC_HF_Hedge" #套保
    ctypedef char TOrderPriceTypeType "TZQThostFtdcOrderPriceTypeType" #报单价格条件
    enum: OPT_AnyPrice "THOST_FTDC_OPT_AnyPrice" #任意价
    enum: OPT_LimitPrice "THOST_FTDC_OPT_LimitPrice" #限价
    enum: OPT_BestPrice "THOST_FTDC_OPT_BestPrice" #最优价
    enum: OPT_LastPrice "THOST_FTDC_OPT_LastPrice" #最新价
    enum: OPT_LastPricePlusOneTicks "THOST_FTDC_OPT_LastPricePlusOneTicks" #最新价浮动上浮1个ticks
    enum: OPT_LastPricePlusTwoTicks "THOST_FTDC_OPT_LastPricePlusTwoTicks" #最新价浮动上浮2个ticks
    enum: OPT_LastPricePlusThreeTicks "THOST_FTDC_OPT_LastPricePlusThreeTicks" #最新价浮动上浮3个ticks
    enum: OPT_AskPrice1 "THOST_FTDC_OPT_AskPrice1" #卖一价
    enum: OPT_AskPrice1PlusOneTicks "THOST_FTDC_OPT_AskPrice1PlusOneTicks" #卖一价浮动上浮1个ticks
    enum: OPT_AskPrice1PlusTwoTicks "THOST_FTDC_OPT_AskPrice1PlusTwoTicks" #卖一价浮动上浮2个ticks
    enum: OPT_AskPrice1PlusThreeTicks "THOST_FTDC_OPT_AskPrice1PlusThreeTicks" #卖一价浮动上浮3个ticks
    enum: OPT_BidPrice1 "THOST_FTDC_OPT_BidPrice1" #买一价
    enum: OPT_BidPrice1PlusOneTicks "THOST_FTDC_OPT_BidPrice1PlusOneTicks" #买一价浮动上浮1个ticks
    enum: OPT_BidPrice1PlusTwoTicks "THOST_FTDC_OPT_BidPrice1PlusTwoTicks" #买一价浮动上浮2个ticks
    enum: OPT_BidPrice1PlusThreeTicks "THOST_FTDC_OPT_BidPrice1PlusThreeTicks" #买一价浮动上浮3个ticks
    enum: OPT_ActiveANetPassSvrCode "THOST_FTDC_OPT_ActiveANetPassSvrCode" #激活A股网络密码服务代码
    enum: OPT_InactiveANetPassSvrCode "THOST_FTDC_OPT_InactiveANetPassSvrCode" #注销A股网络密码服务代码
    enum: OPT_ActiveBNetPassSvrCode "THOST_FTDC_OPT_ActiveBNetPassSvrCode" #激活B股网络密码服务代码
    enum: OPT_InactiveBNetPassSvrCode "THOST_FTDC_OPT_InactiveBNetPassSvrCode" #注销B股网络密码服务代码
    enum: OPT_Repurchase "THOST_FTDC_OPT_Repurchase" #回购注销
    enum: OPT_DesignatedCancel "THOST_FTDC_OPT_DesignatedCancel" #指定撤销
    enum: OPT_Designated "THOST_FTDC_OPT_Designated" #指定登记
    enum: OPT_SubscribingShares "THOST_FTDC_OPT_SubscribingShares" #证券参与申购
    enum: OPT_Split "THOST_FTDC_OPT_Split" #证券参与配股
    enum: OPT_TenderOffer "THOST_FTDC_OPT_TenderOffer" #要约收购登记
    enum: OPT_TenderOfferCancel "THOST_FTDC_OPT_TenderOfferCancel" #要约收购撤销
    enum: OPT_Ballot "THOST_FTDC_OPT_Ballot" #证券投票
    enum: OPT_ConvertibleBondsConvet "THOST_FTDC_OPT_ConvertibleBondsConvet" #可转债转换登记
    enum: OPT_ConvertibleBondsRepurchase "THOST_FTDC_OPT_ConvertibleBondsRepurchase" #可转债回售登记
    enum: OPT_Exercise "THOST_FTDC_OPT_Exercise" #权证行权
    enum: OPT_PurchasingFunds "THOST_FTDC_OPT_PurchasingFunds" #开放式基金申购
    enum: OPT_RedemingFunds "THOST_FTDC_OPT_RedemingFunds" #开放式基金赎回
    enum: OPT_SubscribingFunds "THOST_FTDC_OPT_SubscribingFunds" #开放式基金认购
    enum: OPT_LOFIssue "THOST_FTDC_OPT_LOFIssue" #开放式基金转托管转出
    enum: OPT_LOFSetBonusType "THOST_FTDC_OPT_LOFSetBonusType" #开放式基金设置分红方式
    enum: OPT_LOFConvert "THOST_FTDC_OPT_LOFConvert" #开放式基金转换为其他基金
    enum: OPT_DebentureStockIn "THOST_FTDC_OPT_DebentureStockIn" #债券入库
    enum: OPT_DebentureStockOut "THOST_FTDC_OPT_DebentureStockOut" #债券出库
    enum: OPT_PurchasesETF "THOST_FTDC_OPT_PurchasesETF" #ETF申购
    enum: OPT_RedeemETF "THOST_FTDC_OPT_RedeemETF" #ETF赎回
    enum: OPT_ShortAccToCreditAcc "THOST_FTDC_OPT_ShortAccToCreditAcc" #证券公司融券专用账户过户到证券公司信用交易担保证券账户
    enum: OPT_CreditAccToShortAcc "THOST_FTDC_OPT_CreditAccToShortAcc" #证券公司信用交易担保证券账户过户到证券公司融券专用账户
    enum: OPT_InvAccToCreditAcc "THOST_FTDC_OPT_InvAccToCreditAcc" #投资者普通证券账户过户到证券公司信用交易担保证券账户
    enum: OPT_ShortAccToHostAcc "THOST_FTDC_OPT_ShortAccToHostAcc" #证券公司融券专用账户过户到证券公司自营账户
    ctypedef char TOffsetFlagType "TZQThostFtdcOffsetFlagType" #开平标志
    enum: OF_Open "THOST_FTDC_OF_Open" #开仓
    enum: OF_Close "THOST_FTDC_OF_Close" #平仓
    enum: OF_ForceClose "THOST_FTDC_OF_ForceClose" #强平
    enum: OF_CloseToday "THOST_FTDC_OF_CloseToday" #平今
    enum: OF_CloseYesterday "THOST_FTDC_OF_CloseYesterday" #平昨
    enum: OF_ForceOff "THOST_FTDC_OF_ForceOff" #强减
    enum: OF_LocalForceClose "THOST_FTDC_OF_LocalForceClose" #本地强平
    ctypedef char TForceCloseReasonType "TZQThostFtdcForceCloseReasonType" #强平原因
    enum: FCC_NotForceClose "THOST_FTDC_FCC_NotForceClose" #非强平
    enum: FCC_LackDeposit "THOST_FTDC_FCC_LackDeposit" #资金不足
    enum: FCC_ClientOverPositionLimit "THOST_FTDC_FCC_ClientOverPositionLimit" #客户超仓
    enum: FCC_MemberOverPositionLimit "THOST_FTDC_FCC_MemberOverPositionLimit" #会员超仓
    enum: FCC_NotMultiple "THOST_FTDC_FCC_NotMultiple" #持仓非整数倍
    enum: FCC_Violation "THOST_FTDC_FCC_Violation" #违规
    enum: FCC_Other "THOST_FTDC_FCC_Other" #其它
    ctypedef char TOrderTypeType "TZQThostFtdcOrderTypeType" #报单类型
    enum: ORDT_Normal "THOST_FTDC_ORDT_Normal" #正常
    enum: ORDT_DeriveFromQuote "THOST_FTDC_ORDT_DeriveFromQuote" #报价衍生
    enum: ORDT_DeriveFromCombination "THOST_FTDC_ORDT_DeriveFromCombination" #组合衍生
    enum: ORDT_Combination "THOST_FTDC_ORDT_Combination" #组合报单
    enum: ORDT_ConditionalOrder "THOST_FTDC_ORDT_ConditionalOrder" #条件单
    enum: ORDT_Swap "THOST_FTDC_ORDT_Swap" #互换单
    ctypedef char TTimeConditionType "TZQThostFtdcTimeConditionType" #有效期类型
    enum: TC_IOC "THOST_FTDC_TC_IOC" #立即完成，否则撤销
    enum: TC_GFS "THOST_FTDC_TC_GFS" #本节有效
    enum: TC_GFD "THOST_FTDC_TC_GFD" #当日有效
    enum: TC_GTD "THOST_FTDC_TC_GTD" #指定日期前有效
    enum: TC_GTC "THOST_FTDC_TC_GTC" #撤销前有效
    enum: TC_GFA "THOST_FTDC_TC_GFA" #集合竞价有效
    ctypedef char TVolumeConditionType "TZQThostFtdcVolumeConditionType" #成交量类型
    enum: VC_AV "THOST_FTDC_VC_AV" #任何数量
    enum: VC_MV "THOST_FTDC_VC_MV" #最小数量
    enum: VC_CV "THOST_FTDC_VC_CV" #全部数量
    ctypedef char TContingentConditionType "TZQThostFtdcContingentConditionType" #触发条件
    enum: CC_Immediately "THOST_FTDC_CC_Immediately" #立即
    enum: CC_Touch "THOST_FTDC_CC_Touch" #止损
    enum: CC_TouchProfit "THOST_FTDC_CC_TouchProfit" #止赢
    enum: CC_ParkedOrder "THOST_FTDC_CC_ParkedOrder" #预埋单
    enum: CC_LastPriceGreaterThanStopPrice "THOST_FTDC_CC_LastPriceGreaterThanStopPrice" #最新价大于条件价
    enum: CC_LastPriceGreaterEqualStopPrice "THOST_FTDC_CC_LastPriceGreaterEqualStopPrice" #最新价大于等于条件价
    enum: CC_LastPriceLesserThanStopPrice "THOST_FTDC_CC_LastPriceLesserThanStopPrice" #最新价小于条件价
    enum: CC_LastPriceLesserEqualStopPrice "THOST_FTDC_CC_LastPriceLesserEqualStopPrice" #最新价小于等于条件价
    enum: CC_AskPriceGreaterThanStopPrice "THOST_FTDC_CC_AskPriceGreaterThanStopPrice" #卖一价大于条件价
    enum: CC_AskPriceGreaterEqualStopPrice "THOST_FTDC_CC_AskPriceGreaterEqualStopPrice" #卖一价大于等于条件价
    enum: CC_AskPriceLesserThanStopPrice "THOST_FTDC_CC_AskPriceLesserThanStopPrice" #卖一价小于条件价
    enum: CC_AskPriceLesserEqualStopPrice "THOST_FTDC_CC_AskPriceLesserEqualStopPrice" #卖一价小于等于条件价
    enum: CC_BidPriceGreaterThanStopPrice "THOST_FTDC_CC_BidPriceGreaterThanStopPrice" #买一价大于条件价
    enum: CC_BidPriceGreaterEqualStopPrice "THOST_FTDC_CC_BidPriceGreaterEqualStopPrice" #买一价大于等于条件价
    enum: CC_BidPriceLesserThanStopPrice "THOST_FTDC_CC_BidPriceLesserThanStopPrice" #买一价小于条件价
    enum: CC_BidPriceLesserEqualStopPrice "THOST_FTDC_CC_BidPriceLesserEqualStopPrice" #买一价小于等于条件价
    ctypedef char TActionFlagType "TZQThostFtdcActionFlagType" #操作标志
    enum: AF_Delete "THOST_FTDC_AF_Delete" #删除
    enum: AF_Modify "THOST_FTDC_AF_Modify" #修改
    ctypedef char TTradingRightType "TZQThostFtdcTradingRightType" #交易权限
    enum: TR_Allow "THOST_FTDC_TR_Allow" #可以交易
    enum: TR_Forbidden "THOST_FTDC_TR_Forbidden" #不能交易
    ctypedef char TOrderSourceType "TZQThostFtdcOrderSourceType" #报单来源
    enum: OSRC_Participant "THOST_FTDC_OSRC_Participant" #来自参与者
    enum: OSRC_Administrator "THOST_FTDC_OSRC_Administrator" #来自管理员
    ctypedef char TTradeTypeType "TZQThostFtdcTradeTypeType" #成交类型
    enum: TRDT_Common "THOST_FTDC_TRDT_Common" #普通成交
    enum: TRDT_OptionsExecution "THOST_FTDC_TRDT_OptionsExecution" #期权执行
    enum: TRDT_OTC "THOST_FTDC_TRDT_OTC" #OTC成交
    enum: TRDT_EFPDerived "THOST_FTDC_TRDT_EFPDerived" #期转现衍生成交
    enum: TRDT_CombinationDerived "THOST_FTDC_TRDT_CombinationDerived" #组合衍生成交
    enum: TRDT_EFTPurchase "THOST_FTDC_TRDT_EFTPurchase" #ETF申购
    enum: TRDT_EFTRedem "THOST_FTDC_TRDT_EFTRedem" #ETF赎回
    ctypedef char TPriceSourceType "TZQThostFtdcPriceSourceType" #成交价来源
    enum: PSRC_LastPrice "THOST_FTDC_PSRC_LastPrice" #前成交价
    enum: PSRC_Buy "THOST_FTDC_PSRC_Buy" #买委托价
    enum: PSRC_Sell "THOST_FTDC_PSRC_Sell" #卖委托价
    ctypedef char TInstrumentStatusType "TZQThostFtdcInstrumentStatusType" #合约交易状态
    enum: IS_BeforeTrading "THOST_FTDC_IS_BeforeTrading" #开盘前
    enum: IS_NoTrading "THOST_FTDC_IS_NoTrading" #非交易
    enum: IS_Continous "THOST_FTDC_IS_Continous" #连续交易
    enum: IS_AuctionOrdering "THOST_FTDC_IS_AuctionOrdering" #集合竞价报单
    enum: IS_AuctionBalance "THOST_FTDC_IS_AuctionBalance" #集合竞价价格平衡
    enum: IS_AuctionMatch "THOST_FTDC_IS_AuctionMatch" #集合竞价撮合
    enum: IS_Closed "THOST_FTDC_IS_Closed" #收盘
    ctypedef char TInstStatusEnterReasonType "TZQThostFtdcInstStatusEnterReasonType" #品种进入交易状态原因
    enum: IER_Automatic "THOST_FTDC_IER_Automatic" #自动切换
    enum: IER_Manual "THOST_FTDC_IER_Manual" #手动切换
    enum: IER_Fuse "THOST_FTDC_IER_Fuse" #熔断
    ctypedef int TOrderActionRefType "TZQThostFtdcOrderActionRefType" #报单操作引用
    ctypedef int TInstallCountType "TZQThostFtdcInstallCountType" #安装数量
    ctypedef int TInstallIDType "TZQThostFtdcInstallIDType" #安装编号
    ctypedef int TErrorIDType "TZQThostFtdcErrorIDType" #错误代码
    ctypedef int TSettlementIDType "TZQThostFtdcSettlementIDType" #结算编号
    ctypedef int TVolumeType "TZQThostFtdcVolumeType" #数量
    ctypedef int TFrontIDType "TZQThostFtdcFrontIDType" #前置编号
    ctypedef int TSessionIDType "TZQThostFtdcSessionIDType" #会话编号
    ctypedef int TSequenceNoType "TZQThostFtdcSequenceNoType" #序号
    ctypedef int TCommandNoType "TZQThostFtdcCommandNoType" #DB命令序号
    ctypedef int TMillisecType "TZQThostFtdcMillisecType" #时间（毫秒）
    ctypedef int TVolumeMultipleType "TZQThostFtdcVolumeMultipleType" #合约数量乘数
    ctypedef int TTradingSegmentSNType "TZQThostFtdcTradingSegmentSNType" #交易阶段编号
    ctypedef int TRequestIDType "TZQThostFtdcRequestIDType" #请求编号
    ctypedef int TYearType "TZQThostFtdcYearType" #年份
    ctypedef int TMonthType "TZQThostFtdcMonthType" #月份
    ctypedef int TBoolType "TZQThostFtdcBoolType" #布尔型
    ctypedef double TPriceType "TZQThostFtdcPriceType" #价格
    ctypedef char[5] TCombOffsetFlagType "TZQThostFtdcCombOffsetFlagType" #组合开平标志
    ctypedef char[5] TCombHedgeFlagType "TZQThostFtdcCombHedgeFlagType" #组合投机套保标志
    ctypedef double TRatioType "TZQThostFtdcRatioType" #比率
    ctypedef double TMoneyType "TZQThostFtdcMoneyType" #资金
    ctypedef double TLargeVolumeType "TZQThostFtdcLargeVolumeType" #大额数量
    ctypedef short TSequenceSeriesType "TZQThostFtdcSequenceSeriesType" #序列系列号
    ctypedef short TCommPhaseNoType "TZQThostFtdcCommPhaseNoType" #通讯时段编号
    ctypedef char[2] TSequenceLabelType "TZQThostFtdcSequenceLabelType" #序列编号
    ctypedef int TPriorityType "TZQThostFtdcPriorityType" #优先级
    ctypedef char[41] TContractCodeType "TZQThostFtdcContractCodeType" #合同编号
    ctypedef char[41] TCityType "TZQThostFtdcCityType" #市
    ctypedef char[11] TIsStockType "TZQThostFtdcIsStockType" #是否股民
    ctypedef char[51] TChannelType "TZQThostFtdcChannelType" #渠道
    ctypedef char[101] TAddressType "TZQThostFtdcAddressType" #通讯地址
    ctypedef char[7] TZipCodeType "TZQThostFtdcZipCodeType" #邮政编码
    ctypedef char[41] TTelephoneType "TZQThostFtdcTelephoneType" #联系电话
    ctypedef char[41] TFaxType "TZQThostFtdcFaxType" #传真
    ctypedef char[41] TMobileType "TZQThostFtdcMobileType" #手机
    ctypedef char[41] TEMailType "TZQThostFtdcEMailType" #电子邮件
    ctypedef char[161] TMemoType "TZQThostFtdcMemoType" #备注
    ctypedef char[51] TCompanyCodeType "TZQThostFtdcCompanyCodeType" #企业代码
    ctypedef char[51] TWebsiteType "TZQThostFtdcWebsiteType" #网站地址
    ctypedef char[31] TTaxNoType "TZQThostFtdcTaxNoType" #税务登记号
    ctypedef char TBatchStatusType "TZQThostFtdcBatchStatusType" #处理状态
    enum: BS_NoUpload "THOST_FTDC_BS_NoUpload" #未上传
    enum: BS_Uploaded "THOST_FTDC_BS_Uploaded" #已上传
    enum: BS_Failed "THOST_FTDC_BS_Failed" #审核失败
    ctypedef char[33] TPropertyIDType "TZQThostFtdcPropertyIDType" #属性代码
    ctypedef char[65] TPropertyNameType "TZQThostFtdcPropertyNameType" #属性名称
    ctypedef char[51] TLicenseNoType "TZQThostFtdcLicenseNoType" #营业执照号
    ctypedef char[13] TAgentIDType "TZQThostFtdcAgentIDType" #经纪人代码
    ctypedef char[41] TAgentNameType "TZQThostFtdcAgentNameType" #经纪人名称
    ctypedef char[13] TAgentGroupIDType "TZQThostFtdcAgentGroupIDType" #经纪人组代码
    ctypedef char[41] TAgentGroupNameType "TZQThostFtdcAgentGroupNameType" #经纪人组名称
    ctypedef char TReturnStyleType "TZQThostFtdcReturnStyleType" #按品种返还方式
    enum: RS_All "THOST_FTDC_RS_All" #按所有品种
    enum: RS_ByProduct "THOST_FTDC_RS_ByProduct" #按品种
    ctypedef char TReturnPatternType "TZQThostFtdcReturnPatternType" #返还模式
    enum: RP_ByVolume "THOST_FTDC_RP_ByVolume" #按成交手数
    enum: RP_ByFeeOnHand "THOST_FTDC_RP_ByFeeOnHand" #按留存手续费
    ctypedef char TReturnLevelType "TZQThostFtdcReturnLevelType" #返还级别
    enum: RL_Level1 "THOST_FTDC_RL_Level1" #级别1
    enum: RL_Level2 "THOST_FTDC_RL_Level2" #级别2
    enum: RL_Level3 "THOST_FTDC_RL_Level3" #级别3
    enum: RL_Level4 "THOST_FTDC_RL_Level4" #级别4
    enum: RL_Level5 "THOST_FTDC_RL_Level5" #级别5
    enum: RL_Level6 "THOST_FTDC_RL_Level6" #级别6
    enum: RL_Level7 "THOST_FTDC_RL_Level7" #级别7
    enum: RL_Level8 "THOST_FTDC_RL_Level8" #级别8
    enum: RL_Level9 "THOST_FTDC_RL_Level9" #级别9
    ctypedef char TReturnStandardType "TZQThostFtdcReturnStandardType" #返还标准
    enum: RSD_ByPeriod "THOST_FTDC_RSD_ByPeriod" #分阶段返还
    enum: RSD_ByStandard "THOST_FTDC_RSD_ByStandard" #按某一标准
    ctypedef char TMortgageTypeType "TZQThostFtdcMortgageTypeType" #质押类型
    enum: MT_Out "THOST_FTDC_MT_Out" #质出
    enum: MT_In "THOST_FTDC_MT_In" #质入
    ctypedef char TInvestorSettlementParamIDType "TZQThostFtdcInvestorSettlementParamIDType" #投资者结算参数代码
    enum: ISPI_BaseMargin "THOST_FTDC_ISPI_BaseMargin" #基础保证金
    enum: ISPI_LowestInterest "THOST_FTDC_ISPI_LowestInterest" #最低权益标准
    enum: ISPI_MortgageRatio "THOST_FTDC_ISPI_MortgageRatio" #质押比例
    enum: ISPI_MarginWay "THOST_FTDC_ISPI_MarginWay" #保证金算法
    enum: ISPI_BillDeposit "THOST_FTDC_ISPI_BillDeposit" #结算单(盯市)权益等于结存
    ctypedef char TExchangeSettlementParamIDType "TZQThostFtdcExchangeSettlementParamIDType" #交易所结算参数代码
    enum: ESPI_MortgageRatio "THOST_FTDC_ESPI_MortgageRatio" #质押比例
    enum: ESPI_OtherFundItem "THOST_FTDC_ESPI_OtherFundItem" #分项资金导入项
    enum: ESPI_OtherFundImport "THOST_FTDC_ESPI_OtherFundImport" #分项资金入交易所出入金
    enum: ESPI_SHFEDelivFee "THOST_FTDC_ESPI_SHFEDelivFee" #上期所交割手续费收取方式
    enum: ESPI_DCEDelivFee "THOST_FTDC_ESPI_DCEDelivFee" #大商所交割手续费收取方式
    enum: ESPI_CFFEXMinPrepa "THOST_FTDC_ESPI_CFFEXMinPrepa" #中金所开户最低可用金额
    ctypedef char TSystemParamIDType "TZQThostFtdcSystemParamIDType" #系统参数代码
    enum: SPI_InvestorIDMinLength "THOST_FTDC_SPI_InvestorIDMinLength" #投资者代码最小长度
    enum: SPI_AccountIDMinLength "THOST_FTDC_SPI_AccountIDMinLength" #投资者帐号代码最小长度
    enum: SPI_UserRightLogon "THOST_FTDC_SPI_UserRightLogon" #投资者开户默认登录权限
    enum: SPI_SettlementBillTrade "THOST_FTDC_SPI_SettlementBillTrade" #投资者交易结算单成交汇总方式
    enum: SPI_TradingCode "THOST_FTDC_SPI_TradingCode" #统一开户更新交易编码方式
    enum: SPI_CheckFund "THOST_FTDC_SPI_CheckFund" #结算是否判断存在未复核的出入金和分项资金
    enum: SPI_UploadSettlementFile "THOST_FTDC_SPI_UploadSettlementFile" #上传的结算文件标识
    enum: SPI_DownloadCSRCFile "THOST_FTDC_SPI_DownloadCSRCFile" #下载的保证金存管文件
    enum: SPI_SettlementBillFile "THOST_FTDC_SPI_SettlementBillFile" #结算单文件标识
    enum: SPI_CSRCOthersFile "THOST_FTDC_SPI_CSRCOthersFile" #证监会文件标识
    enum: SPI_InvestorPhoto "THOST_FTDC_SPI_InvestorPhoto" #投资者照片路径
    ctypedef char TTradeParamIDType "TZQThostFtdcTradeParamIDType" #交易系统参数代码
    enum: TPID_EncryptionStandard "THOST_FTDC_TPID_EncryptionStandard" #系统加密算法
    enum: TPID_RiskMode "THOST_FTDC_TPID_RiskMode" #系统风险算法
    enum: TPID_RiskModeGlobal "THOST_FTDC_TPID_RiskModeGlobal" #系统风险算法是否全局 0-否 1-是
    ctypedef char[256] TSettlementParamValueType "TZQThostFtdcSettlementParamValueType" #参数代码值
    ctypedef char[33] TCounterIDType "TZQThostFtdcCounterIDType" #计数器代码
    ctypedef char[41] TInvestorGroupNameType "TZQThostFtdcInvestorGroupNameType" #投资者分组名称
    ctypedef char[257] TBrandCodeType "TZQThostFtdcBrandCodeType" #牌号
    ctypedef char[257] TWarehouseType "TZQThostFtdcWarehouseType" #仓库
    ctypedef char[41] TProductDateType "TZQThostFtdcProductDateType" #产期
    ctypedef char[41] TGradeType "TZQThostFtdcGradeType" #等级
    ctypedef char[41] TClassifyType "TZQThostFtdcClassifyType" #类别
    ctypedef char[41] TPositionType "TZQThostFtdcPositionType" #货位
    ctypedef char[41] TYieldlyType "TZQThostFtdcYieldlyType" #产地
    ctypedef char[41] TWeightType "TZQThostFtdcWeightType" #公定重量
    ctypedef int TSubEntryFundNoType "TZQThostFtdcSubEntryFundNoType" #分项资金流水号
    ctypedef char TFileIDType "TZQThostFtdcFileIDType" #文件标识
    enum: FI_SettlementFund "THOST_FTDC_FI_SettlementFund" #资金数据
    enum: FI_Trade "THOST_FTDC_FI_Trade" #成交数据
    enum: FI_InvestorPosition "THOST_FTDC_FI_InvestorPosition" #投资者持仓数据
    enum: FI_SubEntryFund "THOST_FTDC_FI_SubEntryFund" #投资者分项资金数据
    ctypedef char[257] TFileNameType "TZQThostFtdcFileNameType" #文件名称
    ctypedef char TFileTypeType "TZQThostFtdcFileTypeType" #文件上传类型
    enum: FUT_Settlement "THOST_FTDC_FUT_Settlement" #结算
    enum: FUT_Check "THOST_FTDC_FUT_Check" #核对
    ctypedef char TFileFormatType "TZQThostFtdcFileFormatType" #文件格式
    enum: FFT_Txt "THOST_FTDC_FFT_Txt" #文本文件(.txt)
    enum: FFT_Zip "THOST_FTDC_FFT_Zip" #压缩文件(.zip)
    enum: FFT_DBF "THOST_FTDC_FFT_DBF" #DBF文件(.dbf)
    ctypedef char TFileUploadStatusType "TZQThostFtdcFileUploadStatusType" #文件状态
    enum: FUS_SucceedUpload "THOST_FTDC_FUS_SucceedUpload" #上传成功
    enum: FUS_FailedUpload "THOST_FTDC_FUS_FailedUpload" #上传失败
    enum: FUS_SucceedLoad "THOST_FTDC_FUS_SucceedLoad" #导入成功
    enum: FUS_PartSucceedLoad "THOST_FTDC_FUS_PartSucceedLoad" #导入部分成功
    enum: FUS_FailedLoad "THOST_FTDC_FUS_FailedLoad" #导入失败
    ctypedef char TTransferDirectionType "TZQThostFtdcTransferDirectionType" #移仓方向
    enum: TD_Out "THOST_FTDC_TD_Out" #移出
    enum: TD_In "THOST_FTDC_TD_In" #移入
    ctypedef char[21] TUploadModeType "TZQThostFtdcUploadModeType" #上传文件类型
    ctypedef char[15] TAccountIDType "TZQThostFtdcAccountIDType" #投资者帐号
    ctypedef char TBankFlagType "TZQThostFtdcBankFlagType" #银行统一标识类型
    enum: BF_ICBC "THOST_FTDC_BF_ICBC" #工商银行
    enum: BF_ABC "THOST_FTDC_BF_ABC" #农业银行
    enum: BF_BC "THOST_FTDC_BF_BC" #中国银行
    enum: BF_CBC "THOST_FTDC_BF_CBC" #建设银行
    enum: BF_BOC "THOST_FTDC_BF_BOC" #交通银行
    enum: BF_Other "THOST_FTDC_BF_Other" #其他银行
    ctypedef char[41] TBankAccountType "TZQThostFtdcBankAccountType" #银行账户
    ctypedef char[61] TOpenNameType "TZQThostFtdcOpenNameType" #银行账户的开户人名称
    ctypedef char[101] TOpenBankType "TZQThostFtdcOpenBankType" #银行账户的开户行
    ctypedef char[101] TBankNameType "TZQThostFtdcBankNameType" #银行名称
    ctypedef char[257] TPublishPathType "TZQThostFtdcPublishPathType" #发布路径
    ctypedef char[65] TOperatorIDType "TZQThostFtdcOperatorIDType" #操作员代码
    ctypedef int TMonthCountType "TZQThostFtdcMonthCountType" #月份数量
    ctypedef char[13] TAdvanceMonthArrayType "TZQThostFtdcAdvanceMonthArrayType" #月份提前数组
    ctypedef char[1025] TDateExprType "TZQThostFtdcDateExprType" #日期表达式
    ctypedef char[41] TInstrumentIDExprType "TZQThostFtdcInstrumentIDExprType" #合约代码表达式
    ctypedef char[41] TInstrumentNameExprType "TZQThostFtdcInstrumentNameExprType" #合约名称表达式
    ctypedef char TSpecialCreateRuleType "TZQThostFtdcSpecialCreateRuleType" #特殊的创建规则
    enum: SC_NoSpecialRule "THOST_FTDC_SC_NoSpecialRule" #没有特殊创建规则
    enum: SC_NoSpringFestival "THOST_FTDC_SC_NoSpringFestival" #不包含春节
    ctypedef char TBasisPriceTypeType "TZQThostFtdcBasisPriceTypeType" #挂牌基准价类型
    enum: IPT_LastSettlement "THOST_FTDC_IPT_LastSettlement" #上一合约结算价
    enum: IPT_LaseClose "THOST_FTDC_IPT_LaseClose" #上一合约收盘价
    ctypedef char TProductLifePhaseType "TZQThostFtdcProductLifePhaseType" #产品生命周期状态
    enum: PLP_Active "THOST_FTDC_PLP_Active" #活跃
    enum: PLP_NonActive "THOST_FTDC_PLP_NonActive" #不活跃
    enum: PLP_Canceled "THOST_FTDC_PLP_Canceled" #注销
    ctypedef char TDeliveryModeType "TZQThostFtdcDeliveryModeType" #交割方式
    enum: DM_CashDeliv "THOST_FTDC_DM_CashDeliv" #现金交割
    enum: DM_CommodityDeliv "THOST_FTDC_DM_CommodityDeliv" #实物交割
    ctypedef char[33] TLogLevelType "TZQThostFtdcLogLevelType" #日志级别
    ctypedef char[257] TProcessNameType "TZQThostFtdcProcessNameType" #存储过程名称
    ctypedef char[1025] TOperationMemoType "TZQThostFtdcOperationMemoType" #操作摘要
    ctypedef char TFundIOTypeType "TZQThostFtdcFundIOTypeType" #出入金类型
    enum: FIOT_FundIO "THOST_FTDC_FIOT_FundIO" #出入金
    enum: FIOT_Transfer "THOST_FTDC_FIOT_Transfer" #银期转帐
    ctypedef char TFundTypeType "TZQThostFtdcFundTypeType" #资金类型
    enum: FT_Deposite "THOST_FTDC_FT_Deposite" #银行存款
    enum: FT_ItemFund "THOST_FTDC_FT_ItemFund" #分项资金
    enum: FT_Company "THOST_FTDC_FT_Company" #公司调整
    ctypedef char TFundDirectionType "TZQThostFtdcFundDirectionType" #出入金方向
    enum: FD_In "THOST_FTDC_FD_In" #入金
    enum: FD_Out "THOST_FTDC_FD_Out" #出金
    ctypedef char TFundStatusType "TZQThostFtdcFundStatusType" #资金状态
    enum: FS_Record "THOST_FTDC_FS_Record" #已录入
    enum: FS_Check "THOST_FTDC_FS_Check" #已复核
    enum: FS_Charge "THOST_FTDC_FS_Charge" #已冲销
    ctypedef char[15] TBillNoType "TZQThostFtdcBillNoType" #票据号
    ctypedef char[33] TBillNameType "TZQThostFtdcBillNameType" #票据名称
    ctypedef char TPublishStatusType "TZQThostFtdcPublishStatusType" #发布状态
    enum: PS_None "THOST_FTDC_PS_None" #未发布
    enum: PS_Publishing "THOST_FTDC_PS_Publishing" #正在发布
    enum: PS_Published "THOST_FTDC_PS_Published" #已发布
    ctypedef char[65] TEnumValueIDType "TZQThostFtdcEnumValueIDType" #枚举值代码
    ctypedef char[33] TEnumValueTypeType "TZQThostFtdcEnumValueTypeType" #枚举值类型
    ctypedef char[65] TEnumValueLabelType "TZQThostFtdcEnumValueLabelType" #枚举值名称
    ctypedef char[33] TEnumValueResultType "TZQThostFtdcEnumValueResultType" #枚举值结果
    ctypedef char TSystemStatusType "TZQThostFtdcSystemStatusType" #系统状态
    enum: ES_NonActive "THOST_FTDC_ES_NonActive" #不活跃
    enum: ES_Startup "THOST_FTDC_ES_Startup" #启动
    enum: ES_Initialize "THOST_FTDC_ES_Initialize" #交易开始初始化
    enum: ES_Initialized "THOST_FTDC_ES_Initialized" #交易完成初始化
    enum: ES_Close "THOST_FTDC_ES_Close" #收市开始
    enum: ES_Closed "THOST_FTDC_ES_Closed" #收市完成
    enum: ES_Settlement "THOST_FTDC_ES_Settlement" #结算
    ctypedef char TSettlementStatusType "TZQThostFtdcSettlementStatusType" #结算状态
    enum: STS_Initialize "THOST_FTDC_STS_Initialize" #初始
    enum: STS_Settlementing "THOST_FTDC_STS_Settlementing" #结算中
    enum: STS_Settlemented "THOST_FTDC_STS_Settlemented" #已结算
    enum: STS_Finished "THOST_FTDC_STS_Finished" #结算完成
    ctypedef char[33] TRangeIntTypeType "TZQThostFtdcRangeIntTypeType" #限定值类型
    ctypedef char[33] TRangeIntFromType "TZQThostFtdcRangeIntFromType" #限定值下限
    ctypedef char[33] TRangeIntToType "TZQThostFtdcRangeIntToType" #限定值上限
    ctypedef char[25] TFunctionIDType "TZQThostFtdcFunctionIDType" #功能代码
    ctypedef char[257] TFunctionValueCodeType "TZQThostFtdcFunctionValueCodeType" #功能编码
    ctypedef char[65] TFunctionNameType "TZQThostFtdcFunctionNameType" #功能名称
    ctypedef char[11] TRoleIDType "TZQThostFtdcRoleIDType" #角色编号
    ctypedef char[41] TRoleNameType "TZQThostFtdcRoleNameType" #角色名称
    ctypedef char[401] TDescriptionType "TZQThostFtdcDescriptionType" #描述
    ctypedef char[25] TCombineIDType "TZQThostFtdcCombineIDType" #组合编号
    ctypedef char[25] TCombineTypeType "TZQThostFtdcCombineTypeType" #组合类型
    ctypedef char TInvestorTypeType "TZQThostFtdcInvestorTypeType" #投资者类型
    enum: CT_Person "THOST_FTDC_CT_Person" #自然人
    enum: CT_Company "THOST_FTDC_CT_Company" #法人
    enum: CT_Fund "THOST_FTDC_CT_Fund" #投资基金
    ctypedef char TBrokerTypeType "TZQThostFtdcBrokerTypeType" #经纪公司类型
    enum: BT_Trade "THOST_FTDC_BT_Trade" #交易会员
    enum: BT_TradeSettle "THOST_FTDC_BT_TradeSettle" #交易结算会员
    ctypedef char TRiskLevelType "TZQThostFtdcRiskLevelType" #风险等级
    enum: FAS_Low "THOST_FTDC_FAS_Low" #低风险客户
    enum: FAS_Normal "THOST_FTDC_FAS_Normal" #普通客户
    enum: FAS_Focus "THOST_FTDC_FAS_Focus" #关注客户
    enum: FAS_Risk "THOST_FTDC_FAS_Risk" #风险客户
    ctypedef char TFeeAcceptStyleType "TZQThostFtdcFeeAcceptStyleType" #手续费收取方式
    enum: FAS_ByTrade "THOST_FTDC_FAS_ByTrade" #按交易收取
    enum: FAS_ByDeliv "THOST_FTDC_FAS_ByDeliv" #按交割收取
    enum: FAS_None "THOST_FTDC_FAS_None" #不收
    enum: FAS_FixFee "THOST_FTDC_FAS_FixFee" #按指定手续费收取
    ctypedef char TPasswordTypeType "TZQThostFtdcPasswordTypeType" #密码类型
    enum: PWDT_Trade "THOST_FTDC_PWDT_Trade" #交易密码
    enum: PWDT_Account "THOST_FTDC_PWDT_Account" #资金密码
    ctypedef char TAlgorithmType "TZQThostFtdcAlgorithmType" #盈亏算法
    enum: AG_All "THOST_FTDC_AG_All" #浮盈浮亏都计算
    enum: AG_OnlyLost "THOST_FTDC_AG_OnlyLost" #浮盈不计，浮亏计
    enum: AG_OnlyGain "THOST_FTDC_AG_OnlyGain" #浮盈计，浮亏不计
    enum: AG_None "THOST_FTDC_AG_None" #浮盈浮亏都不计算
    ctypedef char TIncludeCloseProfitType "TZQThostFtdcIncludeCloseProfitType" #是否包含平仓盈利
    enum: ICP_Include "THOST_FTDC_ICP_Include" #包含平仓盈利
    enum: ICP_NotInclude "THOST_FTDC_ICP_NotInclude" #不包含平仓盈利
    ctypedef char TAllWithoutTradeType "TZQThostFtdcAllWithoutTradeType" #是否受可提比例限制
    enum: AWT_Enable "THOST_FTDC_AWT_Enable" #不受可提比例限制
    enum: AWT_Disable "THOST_FTDC_AWT_Disable" #受可提比例限制
    ctypedef char[31] TCommentType "TZQThostFtdcCommentType" #盈亏算法说明
    ctypedef char[4] TVersionType "TZQThostFtdcVersionType" #版本号
    ctypedef char[7] TTradeCodeType "TZQThostFtdcTradeCodeType" #交易代码
    ctypedef char[9] TTradeDateType "TZQThostFtdcTradeDateType" #交易日期
    ctypedef char[9] TTradeTimeType "TZQThostFtdcTradeTimeType" #交易时间
    ctypedef char[9] TTradeSerialType "TZQThostFtdcTradeSerialType" #发起方流水号
    ctypedef int TTradeSerialNoType "TZQThostFtdcTradeSerialNoType" #发起方流水号
    ctypedef char[11] TFutureIDType "TZQThostFtdcFutureIDType" #期货公司代码
    ctypedef char[4] TBankIDType "TZQThostFtdcBankIDType" #银行代码
    ctypedef char[5] TBankBrchIDType "TZQThostFtdcBankBrchIDType" #银行分中心代码
    ctypedef char[11] TBankBranchIDType "TZQThostFtdcBankBranchIDType" #分中心代码
    ctypedef char[17] TOperNoType "TZQThostFtdcOperNoType" #交易柜员
    ctypedef char[3] TDeviceIDType "TZQThostFtdcDeviceIDType" #渠道标志
    ctypedef char[7] TRecordNumType "TZQThostFtdcRecordNumType" #记录数
    ctypedef char[22] TFutureAccountType "TZQThostFtdcFutureAccountType" #期货资金账号
    ctypedef char TFuturePwdFlagType "TZQThostFtdcFuturePwdFlagType" #资金密码核对标志
    enum: FPWD_UnCheck "THOST_FTDC_FPWD_UnCheck" #不核对
    enum: FPWD_Check "THOST_FTDC_FPWD_Check" #核对
    ctypedef char TTransferTypeType "TZQThostFtdcTransferTypeType" #银期转账类型
    enum: TT_BankToFuture "THOST_FTDC_TT_BankToFuture" #银行转期货
    enum: TT_FutureToBank "THOST_FTDC_TT_FutureToBank" #期货转银行
    ctypedef char[17] TFutureAccPwdType "TZQThostFtdcFutureAccPwdType" #期货资金密码
    ctypedef char[4] TCurrencyCodeType "TZQThostFtdcCurrencyCodeType" #币种
    ctypedef char[5] TRetCodeType "TZQThostFtdcRetCodeType" #响应代码
    ctypedef char[129] TRetInfoType "TZQThostFtdcRetInfoType" #响应信息
    ctypedef char[20] TTradeAmtType "TZQThostFtdcTradeAmtType" #银行总余额
    ctypedef char[20] TUseAmtType "TZQThostFtdcUseAmtType" #银行可用余额
    ctypedef char[20] TFetchAmtType "TZQThostFtdcFetchAmtType" #银行可取余额
    ctypedef char TTransferValidFlagType "TZQThostFtdcTransferValidFlagType" #转账有效标志
    enum: TVF_Invalid "THOST_FTDC_TVF_Invalid" #无效或失败
    enum: TVF_Valid "THOST_FTDC_TVF_Valid" #有效
    enum: TVF_Reverse "THOST_FTDC_TVF_Reverse" #冲正
    ctypedef char[21] TCertCodeType "TZQThostFtdcCertCodeType" #证件号码
    ctypedef char TReasonType "TZQThostFtdcReasonType" #事由
    enum: RN_CD "THOST_FTDC_RN_CD" #错单
    enum: RN_ZT "THOST_FTDC_RN_ZT" #资金在途
    enum: RN_QT "THOST_FTDC_RN_QT" #其它
    ctypedef char[5] TFundProjectIDType "TZQThostFtdcFundProjectIDType" #资金项目编号
    ctypedef char TSexType "TZQThostFtdcSexType" #性别
    enum: SEX_None "THOST_FTDC_SEX_None" #未知
    enum: SEX_Man "THOST_FTDC_SEX_Man" #男
    enum: SEX_Woman "THOST_FTDC_SEX_Woman" #女
    ctypedef char[41] TProfessionType "TZQThostFtdcProfessionType" #职业
    ctypedef char[31] TNationalType "TZQThostFtdcNationalType" #国籍
    ctypedef char[16] TProvinceType "TZQThostFtdcProvinceType" #省
    ctypedef char[16] TRegionType "TZQThostFtdcRegionType" #区
    ctypedef char[16] TCountryType "TZQThostFtdcCountryType" #国家
    ctypedef char[33] TLicenseNOType "TZQThostFtdcLicenseNOType" #营业执照
    ctypedef char[16] TCompanyTypeType "TZQThostFtdcCompanyTypeType" #企业性质
    ctypedef char[1001] TBusinessScopeType "TZQThostFtdcBusinessScopeType" #经营范围
    ctypedef char[4] TCapitalCurrencyType "TZQThostFtdcCapitalCurrencyType" #注册资本币种
    ctypedef char TUserTypeType "TZQThostFtdcUserTypeType" #用户类型
    enum: UT_Investor "THOST_FTDC_UT_Investor" #投资者
    enum: UT_Operator "THOST_FTDC_UT_Operator" #操作员
    enum: UT_SuperUser "THOST_FTDC_UT_SuperUser" #管理员
    ctypedef char TRateTypeType "TZQThostFtdcRateTypeType" #费率类型
    enum: RATETYPE_MarginRate "THOST_FTDC_RATETYPE_MarginRate" #保证金率
    enum: RATETYPE_CommRate "THOST_FTDC_RATETYPE_CommRate" #手续费率
    enum: RATETYPE_AllRate "THOST_FTDC_RATETYPE_AllRate" #所有
    ctypedef char TNoteTypeType "TZQThostFtdcNoteTypeType" #通知类型
    enum: NOTETYPE_TradeSettleBill "THOST_FTDC_NOTETYPE_TradeSettleBill" #交易结算单
    enum: NOTETYPE_TradeSettleMonth "THOST_FTDC_NOTETYPE_TradeSettleMonth" #交易结算月报
    enum: NOTETYPE_CallMarginNotes "THOST_FTDC_NOTETYPE_CallMarginNotes" #追加保证金通知书
    enum: NOTETYPE_ForceCloseNotes "THOST_FTDC_NOTETYPE_ForceCloseNotes" #强行平仓通知书
    enum: NOTETYPE_TradeNotes "THOST_FTDC_NOTETYPE_TradeNotes" #成交通知书
    enum: NOTETYPE_DelivNotes "THOST_FTDC_NOTETYPE_DelivNotes" #交割通知书
    ctypedef char TSettlementStyleType "TZQThostFtdcSettlementStyleType" #结算单方式
    enum: SBS_Day "THOST_FTDC_SBS_Day" #逐日盯市
    enum: SBS_Volume "THOST_FTDC_SBS_Volume" #逐笔对冲
    ctypedef char[256] TBrokerDNSType "TZQThostFtdcBrokerDNSType" #域名
    ctypedef char[501] TSentenceType "TZQThostFtdcSentenceType" #语句
    ctypedef char TSettlementBillTypeType "TZQThostFtdcSettlementBillTypeType" #结算单类型
    enum: ST_Day "THOST_FTDC_ST_Day" #日报
    enum: ST_Month "THOST_FTDC_ST_Month" #月报
    ctypedef char TUserRightTypeType "TZQThostFtdcUserRightTypeType" #客户权限类型
    enum: URT_Logon "THOST_FTDC_URT_Logon" #登录
    enum: URT_Transfer "THOST_FTDC_URT_Transfer" #银期转帐
    enum: URT_EMail "THOST_FTDC_URT_EMail" #邮寄结算单
    enum: URT_Fax "THOST_FTDC_URT_Fax" #传真结算单
    enum: URT_ConditionOrder "THOST_FTDC_URT_ConditionOrder" #条件单
    ctypedef char TMarginPriceTypeType "TZQThostFtdcMarginPriceTypeType" #保证金价格类型
    enum: MPT_PreSettlementPrice "THOST_FTDC_MPT_PreSettlementPrice" #昨结算价
    enum: MPT_SettlementPrice "THOST_FTDC_MPT_SettlementPrice" #最新价
    enum: MPT_AveragePrice "THOST_FTDC_MPT_AveragePrice" #成交均价
    enum: MPT_OpenPrice "THOST_FTDC_MPT_OpenPrice" #开仓价
    ctypedef char TBillGenStatusType "TZQThostFtdcBillGenStatusType" #结算单生成状态
    enum: BGS_None "THOST_FTDC_BGS_None" #不生成
    enum: BGS_NoGenerated "THOST_FTDC_BGS_NoGenerated" #未生成
    enum: BGS_Generated "THOST_FTDC_BGS_Generated" #已生成
    ctypedef char TAlgoTypeType "TZQThostFtdcAlgoTypeType" #算法类型
    enum: AT_HandlePositionAlgo "THOST_FTDC_AT_HandlePositionAlgo" #持仓处理算法
    enum: AT_FindMarginRateAlgo "THOST_FTDC_AT_FindMarginRateAlgo" #寻找保证金率算法
    ctypedef char THandlePositionAlgoIDType "TZQThostFtdcHandlePositionAlgoIDType" #持仓处理算法编号
    enum: HPA_Base "THOST_FTDC_HPA_Base" #基本
    enum: HPA_DCE "THOST_FTDC_HPA_DCE" #大连商品交易所
    enum: HPA_CZCE "THOST_FTDC_HPA_CZCE" #郑州商品交易所
    enum: HPA_NoneTrade "THOST_FTDC_HPA_NoneTrade" #非交易
    enum: HPA_Stock "THOST_FTDC_HPA_Stock" #证券
    ctypedef char TFindMarginRateAlgoIDType "TZQThostFtdcFindMarginRateAlgoIDType" #寻找保证金率算法编号
    enum: FMRA_Base "THOST_FTDC_FMRA_Base" #基本
    enum: FMRA_DCE "THOST_FTDC_FMRA_DCE" #大连商品交易所
    enum: FMRA_CZCE "THOST_FTDC_FMRA_CZCE" #郑州商品交易所
    ctypedef char THandleTradingAccountAlgoIDType "TZQThostFtdcHandleTradingAccountAlgoIDType" #资金处理算法编号
    enum: HTAA_Base "THOST_FTDC_HTAA_Base" #基本
    enum: HTAA_DCE "THOST_FTDC_HTAA_DCE" #大连商品交易所
    enum: HTAA_CZCE "THOST_FTDC_HTAA_CZCE" #郑州商品交易所
    ctypedef char TPersonTypeType "TZQThostFtdcPersonTypeType" #联系人类型
    enum: PST_Order "THOST_FTDC_PST_Order" #指定下单人
    enum: PST_Open "THOST_FTDC_PST_Open" #开户授权人
    enum: PST_Fund "THOST_FTDC_PST_Fund" #资金调拨人
    enum: PST_Settlement "THOST_FTDC_PST_Settlement" #结算单确认人
    ctypedef char TQueryInvestorRangeType "TZQThostFtdcQueryInvestorRangeType" #查询范围
    enum: QIR_All "THOST_FTDC_QIR_All" #所有
    enum: QIR_Group "THOST_FTDC_QIR_Group" #查询分类
    enum: QIR_Single "THOST_FTDC_QIR_Single" #单一投资者
    ctypedef char TInvestorRiskStatusType "TZQThostFtdcInvestorRiskStatusType" #投资者风险状态
    enum: IRS_Normal "THOST_FTDC_IRS_Normal" #正常
    enum: IRS_Warn "THOST_FTDC_IRS_Warn" #警告
    enum: IRS_Call "THOST_FTDC_IRS_Call" #追保
    enum: IRS_Force "THOST_FTDC_IRS_Force" #强平
    enum: IRS_Exception "THOST_FTDC_IRS_Exception" #异常
    ctypedef int TLegIDType "TZQThostFtdcLegIDType" #单腿编号
    ctypedef int TLegMultipleType "TZQThostFtdcLegMultipleType" #单腿乘数
    ctypedef int TImplyLevelType "TZQThostFtdcImplyLevelType" #派生层数
    ctypedef char[33] TClearAccountType "TZQThostFtdcClearAccountType" #结算账户
    ctypedef char[6] TOrganNOType "TZQThostFtdcOrganNOType" #结算账户
    ctypedef char[6] TClearbarchIDType "TZQThostFtdcClearbarchIDType" #结算账户联行号
    ctypedef char TUserEventTypeType "TZQThostFtdcUserEventTypeType" #用户事件类型
    enum: UET_All "THOST_FTDC_UET_All" #所有
    enum: UET_Login "THOST_FTDC_UET_Login" #登录
    enum: UET_Logout "THOST_FTDC_UET_Logout" #登出
    enum: UET_Trading "THOST_FTDC_UET_Trading" #交易成功
    enum: UET_TradingError "THOST_FTDC_UET_TradingError" #交易失败
    enum: UET_UpdatePassword "THOST_FTDC_UET_UpdatePassword" #修改密码
    enum: UET_Other "THOST_FTDC_UET_Other" #其他
    ctypedef char[1025] TUserEventInfoType "TZQThostFtdcUserEventInfoType" #用户事件信息
    ctypedef char TCloseStyleType "TZQThostFtdcCloseStyleType" #平仓方式
    enum: ICS_Close "THOST_FTDC_ICS_Close" #先开先平
    enum: ICS_CloseToday "THOST_FTDC_ICS_CloseToday" #先平今再平昨
    ctypedef char TStatModeType "TZQThostFtdcStatModeType" #统计方式
    enum: SM_Non "THOST_FTDC_SM_Non" #----
    enum: SM_Instrument "THOST_FTDC_SM_Instrument" #按合约统计
    enum: SM_Product "THOST_FTDC_SM_Product" #按产品统计
    enum: SM_Investor "THOST_FTDC_SM_Investor" #按投资者统计
    ctypedef char TParkedOrderStatusType "TZQThostFtdcParkedOrderStatusType" #预埋单状态
    enum: PAOS_NotSend "THOST_FTDC_PAOS_NotSend" #未发送
    enum: PAOS_Send "THOST_FTDC_PAOS_Send" #已发送
    enum: PAOS_Deleted "THOST_FTDC_PAOS_Deleted" #已删除
    ctypedef char[13] TParkedOrderIDType "TZQThostFtdcParkedOrderIDType" #预埋报单编号
    ctypedef char[13] TParkedOrderActionIDType "TZQThostFtdcParkedOrderActionIDType" #预埋撤单编号
    ctypedef char TVirDealStatusType "TZQThostFtdcVirDealStatusType" #处理状态
    enum: VDS_Dealing "THOST_FTDC_VDS_Dealing" #正在处理
    enum: VDS_DeaclSucceed "THOST_FTDC_VDS_DeaclSucceed" #处理成功
    ctypedef char TOrgSystemIDType "TZQThostFtdcOrgSystemIDType" #原有系统代码
    enum: ORGS_Standard "THOST_FTDC_ORGS_Standard" #综合交易平台
    enum: ORGS_ESunny "THOST_FTDC_ORGS_ESunny" #易盛系统
    enum: ORGS_KingStarV6 "THOST_FTDC_ORGS_KingStarV6" #金仕达V6系统
    ctypedef char TVirTradeStatusType "TZQThostFtdcVirTradeStatusType" #交易状态
    enum: VTS_NaturalDeal "THOST_FTDC_VTS_NaturalDeal" #正常处理中
    enum: VTS_SucceedEnd "THOST_FTDC_VTS_SucceedEnd" #成功结束
    enum: VTS_FailedEND "THOST_FTDC_VTS_FailedEND" #失败结束
    enum: VTS_Exception "THOST_FTDC_VTS_Exception" #异常中
    enum: VTS_ManualDeal "THOST_FTDC_VTS_ManualDeal" #已人工异常处理
    enum: VTS_MesException "THOST_FTDC_VTS_MesException" #通讯异常 ，请人工处理
    enum: VTS_SysException "THOST_FTDC_VTS_SysException" #系统出错，请人工处理
    ctypedef char TVirBankAccTypeType "TZQThostFtdcVirBankAccTypeType" #银行帐户类型
    enum: VBAT_BankBook "THOST_FTDC_VBAT_BankBook" #存折
    enum: VBAT_BankCard "THOST_FTDC_VBAT_BankCard" #储蓄卡
    enum: VBAT_CreditCard "THOST_FTDC_VBAT_CreditCard" #信用卡
    ctypedef char TVirementStatusType "TZQThostFtdcVirementStatusType" #银行帐户类型
    enum: VMS_Natural "THOST_FTDC_VMS_Natural" #正常
    enum: VMS_Canceled "THOST_FTDC_VMS_Canceled" #销户
    ctypedef char TVirementAvailAbilityType "TZQThostFtdcVirementAvailAbilityType" #有效标志
    enum: VAA_NoAvailAbility "THOST_FTDC_VAA_NoAvailAbility" #未确认
    enum: VAA_AvailAbility "THOST_FTDC_VAA_AvailAbility" #有效
    enum: VAA_Repeal "THOST_FTDC_VAA_Repeal" #冲正
    ctypedef char[7] TVirementTradeCodeType "TZQThostFtdcVirementTradeCodeType" #交易代码
    enum: VTC_BankBankToFuture "THOST_FTDC_VTC_BankBankToFuture" #银行发起银行资金转期货
    enum: VTC_BankFutureToBank "THOST_FTDC_VTC_BankFutureToBank" #银行发起期货资金转银行
    enum: VTC_FutureBankToFuture "THOST_FTDC_VTC_FutureBankToFuture" #期货发起银行资金转期货
    enum: VTC_FutureFutureToBank "THOST_FTDC_VTC_FutureFutureToBank" #期货发起期货资金转银行
    ctypedef char[41] TPhotoTypeNameType "TZQThostFtdcPhotoTypeNameType" #影像类型名称
    ctypedef char[5] TPhotoTypeIDType "TZQThostFtdcPhotoTypeIDType" #影像类型代码
    ctypedef char[161] TPhotoNameType "TZQThostFtdcPhotoNameType" #影像名称
    ctypedef int TTopicIDType "TZQThostFtdcTopicIDType" #主题代码
    ctypedef char[3] TReportTypeIDType "TZQThostFtdcReportTypeIDType" #交易报告类型标识
    ctypedef char[5] TCharacterIDType "TZQThostFtdcCharacterIDType" #交易特征代码
    ctypedef char[21] TAMLParamIDType "TZQThostFtdcAMLParamIDType" #参数代码
    ctypedef char[3] TAMLInvestorTypeType "TZQThostFtdcAMLInvestorTypeType" #投资者类型
    ctypedef char[3] TAMLIdCardTypeType "TZQThostFtdcAMLIdCardTypeType" #证件类型
    ctypedef char[3] TAMLTradeDirectType "TZQThostFtdcAMLTradeDirectType" #资金进出方向
    ctypedef char[3] TAMLTradeModelType "TZQThostFtdcAMLTradeModelType" #资金进出方式
    ctypedef char[21] TAMLParamIDType "TZQThostFtdcAMLParamIDType" #参数代码
    ctypedef double TAMLOpParamValueType "TZQThostFtdcAMLOpParamValueType" #业务参数代码值
    ctypedef char[81] TAMLCustomerCardTypeType "TZQThostFtdcAMLCustomerCardTypeType" #客户身份证件/证明文件类型
    ctypedef char[65] TAMLInstitutionNameType "TZQThostFtdcAMLInstitutionNameType" #金融机构网点名称
    ctypedef char[7] TAMLDistrictIDType "TZQThostFtdcAMLDistrictIDType" #金融机构网点所在地区行政区划代码
    ctypedef char[3] TAMLRelationShipType "TZQThostFtdcAMLRelationShipType" #金融机构网点与大额交易的关系
    ctypedef char[3] TAMLInstitutionTypeType "TZQThostFtdcAMLInstitutionTypeType" #金融机构网点代码类型
    ctypedef char[13] TAMLInstitutionIDType "TZQThostFtdcAMLInstitutionIDType" #金融机构网点代码
    ctypedef char[5] TAMLAccountTypeType "TZQThostFtdcAMLAccountTypeType" #账户类型
    ctypedef char[7] TAMLTradingTypeType "TZQThostFtdcAMLTradingTypeType" #交易方式
    ctypedef char[7] TAMLTransactClassType "TZQThostFtdcAMLTransactClassType" #涉外收支交易分类与代码
    ctypedef char[3] TAMLCapitalIOType "TZQThostFtdcAMLCapitalIOType" #资金收付标识
    ctypedef char[10] TAMLSiteType "TZQThostFtdcAMLSiteType" #交易地点
    ctypedef char[129] TAMLCapitalPurposeType "TZQThostFtdcAMLCapitalPurposeType" #资金用途
    ctypedef char[2] TAMLReportTypeType "TZQThostFtdcAMLReportTypeType" #报文类型
    ctypedef char[5] TAMLSerialNoType "TZQThostFtdcAMLSerialNoType" #编号
    ctypedef char[2] TAMLStatusType "TZQThostFtdcAMLStatusType" #状态
    ctypedef char[2] TAMLGenStatusType "TZQThostFtdcAMLGenStatusType" #状态
    ctypedef char[65] TAMLSeqCodeType "TZQThostFtdcAMLSeqCodeType" #业务标识号
    ctypedef char[257] TAMLFileNameType "TZQThostFtdcAMLFileNameType" #AML文件名
    ctypedef double TAMLMoneyType "TZQThostFtdcAMLMoneyType" #反洗钱资金
    ctypedef int TAMLFileAmountType "TZQThostFtdcAMLFileAmountType" #反洗钱资金
    ctypedef char[21] TCFMMCKeyType "TZQThostFtdcCFMMCKeyType" #密钥类型(保证金监管)
    ctypedef char TCFMMCKeyKindType "TZQThostFtdcCFMMCKeyKindType" #动态密钥类别(保证金监管)
    enum: CFMMCKK_REQUEST "THOST_FTDC_CFMMCKK_REQUEST" #主动请求更新
    enum: CFMMCKK_AUTO "THOST_FTDC_CFMMCKK_AUTO" #CFMMC自动更新
    enum: CFMMCKK_MANUAL "THOST_FTDC_CFMMCKK_MANUAL" #CFMMC手动更新
    ctypedef char[51] TIndividualNameType "TZQThostFtdcIndividualNameType" #个人姓名
    ctypedef char[4] TCurrencyIDType "TZQThostFtdcCurrencyIDType" #币种代码
    ctypedef char[36] TCustNumberType "TZQThostFtdcCustNumberType" #客户编号
    ctypedef char[36] TOrganCodeType "TZQThostFtdcOrganCodeType" #机构编码
    ctypedef char[71] TOrganNameType "TZQThostFtdcOrganNameType" #机构名称
    ctypedef char[12] TSuperOrganCodeType "TZQThostFtdcSuperOrganCodeType" #上级机构编码,即期货公司总部、银行总行
    ctypedef char[31] TSubBranchIDType "TZQThostFtdcSubBranchIDType" #分支机构
    ctypedef char[71] TSubBranchNameType "TZQThostFtdcSubBranchNameType" #分支机构名称
    ctypedef char[31] TBranchNetCodeType "TZQThostFtdcBranchNetCodeType" #机构网点号
    ctypedef char[71] TBranchNetNameType "TZQThostFtdcBranchNetNameType" #机构网点名称
    ctypedef char[2] TOrganFlagType "TZQThostFtdcOrganFlagType" #机构标识
    ctypedef char[33] TBankCodingForFutureType "TZQThostFtdcBankCodingForFutureType" #银行对期货公司的编码
    ctypedef char[7] TBankReturnCodeType "TZQThostFtdcBankReturnCodeType" #银行对返回码的定义
    ctypedef char[5] TPlateReturnCodeType "TZQThostFtdcPlateReturnCodeType" #银期转帐平台对返回码的定义
    ctypedef char[31] TBankSubBranchIDType "TZQThostFtdcBankSubBranchIDType" #银行分支机构编码
    ctypedef char[31] TFutureBranchIDType "TZQThostFtdcFutureBranchIDType" #期货分支机构编码
    ctypedef char[7] TReturnCodeType "TZQThostFtdcReturnCodeType" #返回代码
    ctypedef char[17] TOperatorCodeType "TZQThostFtdcOperatorCodeType" #操作员
    ctypedef char[6] TClearDepIDType "TZQThostFtdcClearDepIDType" #机构结算帐户机构号
    ctypedef char[6] TClearBrchIDType "TZQThostFtdcClearBrchIDType" #机构结算帐户联行号
    ctypedef char[71] TClearNameType "TZQThostFtdcClearNameType" #机构结算帐户名称
    ctypedef char[71] TBankAccountNameType "TZQThostFtdcBankAccountNameType" #银行帐户名称
    ctypedef char[6] TInvDepIDType "TZQThostFtdcInvDepIDType" #机构投资人账号机构号
    ctypedef char[6] TInvBrchIDType "TZQThostFtdcInvBrchIDType" #机构投资人联行号
    ctypedef char[36] TMessageFormatVersionType "TZQThostFtdcMessageFormatVersionType" #信息格式版本
    ctypedef char[36] TDigestType "TZQThostFtdcDigestType" #摘要
    ctypedef char[129] TAuthenticDataType "TZQThostFtdcAuthenticDataType" #认证数据
    ctypedef char[129] TPasswordKeyType "TZQThostFtdcPasswordKeyType" #密钥
    ctypedef char[129] TFutureAccountNameType "TZQThostFtdcFutureAccountNameType" #期货帐户名称
    ctypedef char[21] TMobilePhoneType "TZQThostFtdcMobilePhoneType" #手机
    ctypedef char[129] TFutureMainKeyType "TZQThostFtdcFutureMainKeyType" #期货公司主密钥
    ctypedef char[129] TFutureWorkKeyType "TZQThostFtdcFutureWorkKeyType" #期货公司工作密钥
    ctypedef char[129] TFutureTransKeyType "TZQThostFtdcFutureTransKeyType" #期货公司传输密钥
    ctypedef char[129] TBankMainKeyType "TZQThostFtdcBankMainKeyType" #银行主密钥
    ctypedef char[129] TBankWorkKeyType "TZQThostFtdcBankWorkKeyType" #银行工作密钥
    ctypedef char[129] TBankTransKeyType "TZQThostFtdcBankTransKeyType" #银行传输密钥
    ctypedef char[129] TBankServerDescriptionType "TZQThostFtdcBankServerDescriptionType" #银行服务器描述信息
    ctypedef char[129] TAddInfoType "TZQThostFtdcAddInfoType" #附加信息
    ctypedef char[129] TDescrInfoForReturnCodeType "TZQThostFtdcDescrInfoForReturnCodeType" #返回码描述
    ctypedef char[21] TCountryCodeType "TZQThostFtdcCountryCodeType" #国家代码
    ctypedef int TSerialType "TZQThostFtdcSerialType" #流水号
    ctypedef int TPlateSerialType "TZQThostFtdcPlateSerialType" #平台流水号
    ctypedef char[13] TBankSerialType "TZQThostFtdcBankSerialType" #银行流水号
    ctypedef int TCorrectSerialType "TZQThostFtdcCorrectSerialType" #被冲正交易流水号
    ctypedef int TFutureSerialType "TZQThostFtdcFutureSerialType" #期货公司流水号
    ctypedef int TApplicationIDType "TZQThostFtdcApplicationIDType" #应用标识
    ctypedef int TBankProxyIDType "TZQThostFtdcBankProxyIDType" #银行代理标识
    ctypedef int TFBTCoreIDType "TZQThostFtdcFBTCoreIDType" #银期转帐核心系统标识
    ctypedef int TServerPortType "TZQThostFtdcServerPortType" #服务端口号
    ctypedef int TRepealedTimesType "TZQThostFtdcRepealedTimesType" #已经冲正次数
    ctypedef int TRepealTimeIntervalType "TZQThostFtdcRepealTimeIntervalType" #冲正时间间隔
    ctypedef int TTotalTimesType "TZQThostFtdcTotalTimesType" #每日累计转帐次数
    ctypedef int TFBTRequestIDType "TZQThostFtdcFBTRequestIDType" #请求ID
    ctypedef int TTIDType "TZQThostFtdcTIDType" #交易ID
    ctypedef double TTradeAmountType "TZQThostFtdcTradeAmountType" #交易金额（元）
    ctypedef double TCustFeeType "TZQThostFtdcCustFeeType" #应收客户费用（元）
    ctypedef double TFutureFeeType "TZQThostFtdcFutureFeeType" #应收期货公司费用（元）
    ctypedef double TSingleMaxAmtType "TZQThostFtdcSingleMaxAmtType" #单笔最高限额
    ctypedef double TSingleMinAmtType "TZQThostFtdcSingleMinAmtType" #单笔最低限额
    ctypedef double TTotalAmtType "TZQThostFtdcTotalAmtType" #每日累计转帐额度
    ctypedef char TCertificationTypeType "TZQThostFtdcCertificationTypeType" #证件类型
    enum: CFT_IDCard "THOST_FTDC_CFT_IDCard" #身份证
    enum: CFT_Passport "THOST_FTDC_CFT_Passport" #护照
    enum: CFT_OfficerIDCard "THOST_FTDC_CFT_OfficerIDCard" #军官证
    enum: CFT_SoldierIDCard "THOST_FTDC_CFT_SoldierIDCard" #士兵证
    enum: CFT_HomeComingCard "THOST_FTDC_CFT_HomeComingCard" #回乡证
    enum: CFT_HouseholdRegister "THOST_FTDC_CFT_HouseholdRegister" #户口簿
    enum: CFT_LicenseNo "THOST_FTDC_CFT_LicenseNo" #营业执照号
    enum: CFT_InstitutionCodeCard "THOST_FTDC_CFT_InstitutionCodeCard" #组织机构代码证
    enum: CFT_TempLicenseNo "THOST_FTDC_CFT_TempLicenseNo" #临时营业执照号
    enum: CFT_NoEnterpriseLicenseNo "THOST_FTDC_CFT_NoEnterpriseLicenseNo" #民办非企业登记证书
    enum: CFT_OtherCard "THOST_FTDC_CFT_OtherCard" #其他证件
    enum: CFT_SuperDepAgree "THOST_FTDC_CFT_SuperDepAgree" #主管部门批文
    ctypedef char TFileBusinessCodeType "TZQThostFtdcFileBusinessCodeType" #文件业务功能
    enum: FBC_Others "THOST_FTDC_FBC_Others" #其他
    enum: FBC_TransferDetails "THOST_FTDC_FBC_TransferDetails" #转账交易明细对账
    enum: FBC_CustAccStatus "THOST_FTDC_FBC_CustAccStatus" #客户账户状态对账
    enum: FBC_AccountTradeDetails "THOST_FTDC_FBC_AccountTradeDetails" #账户类交易明细对账
    enum: FBC_FutureAccountChangeInfoDetails "THOST_FTDC_FBC_FutureAccountChangeInfoDetails" #期货账户信息变更明细对账
    enum: FBC_CustMoneyDetail "THOST_FTDC_FBC_CustMoneyDetail" #客户资金台账余额明细对账
    enum: FBC_CustCancelAccountInfo "THOST_FTDC_FBC_CustCancelAccountInfo" #客户销户结息明细对账
    enum: FBC_CustMoneyResult "THOST_FTDC_FBC_CustMoneyResult" #客户资金余额对账结果
    enum: FBC_OthersExceptionResult "THOST_FTDC_FBC_OthersExceptionResult" #其它对账异常结果文件
    enum: FBC_CustInterestNetMoneyDetails "THOST_FTDC_FBC_CustInterestNetMoneyDetails" #客户结息净额明细
    enum: FBC_CustMoneySendAndReceiveDetails "THOST_FTDC_FBC_CustMoneySendAndReceiveDetails" #客户资金交收明细
    enum: FBC_CorporationMoneyTotal "THOST_FTDC_FBC_CorporationMoneyTotal" #法人存管银行资金交收汇总
    enum: FBC_MainbodyMoneyTotal "THOST_FTDC_FBC_MainbodyMoneyTotal" #主体间资金交收汇总
    enum: FBC_MainPartMonitorData "THOST_FTDC_FBC_MainPartMonitorData" #总分平衡监管数据
    enum: FBC_PreparationMoney "THOST_FTDC_FBC_PreparationMoney" #存管银行备付金余额
    enum: FBC_BankMoneyMonitorData "THOST_FTDC_FBC_BankMoneyMonitorData" #协办存管银行资金监管数据
    ctypedef char TCashExchangeCodeType "TZQThostFtdcCashExchangeCodeType" #汇钞标志
    enum: CEC_Exchange "THOST_FTDC_CEC_Exchange" #汇
    enum: CEC_Cash "THOST_FTDC_CEC_Cash" #钞
    ctypedef char TYesNoIndicatorType "TZQThostFtdcYesNoIndicatorType" #是或否标识
    enum: YNI_Yes "THOST_FTDC_YNI_Yes" #是
    enum: YNI_No "THOST_FTDC_YNI_No" #否
    ctypedef char TBanlanceTypeType "TZQThostFtdcBanlanceTypeType" #余额类型
    enum: BLT_CurrentMoney "THOST_FTDC_BLT_CurrentMoney" #当前余额
    enum: BLT_UsableMoney "THOST_FTDC_BLT_UsableMoney" #可用余额
    enum: BLT_FetchableMoney "THOST_FTDC_BLT_FetchableMoney" #可取余额
    enum: BLT_FreezeMoney "THOST_FTDC_BLT_FreezeMoney" #冻结余额
    ctypedef char TGenderType "TZQThostFtdcGenderType" #性别
    enum: GD_Unknown "THOST_FTDC_GD_Unknown" #未知状态
    enum: GD_Male "THOST_FTDC_GD_Male" #男
    enum: GD_Female "THOST_FTDC_GD_Female" #女
    ctypedef char TFeePayFlagType "TZQThostFtdcFeePayFlagType" #费用支付标志
    enum: FPF_BEN "THOST_FTDC_FPF_BEN" #由受益方支付费用
    enum: FPF_OUR "THOST_FTDC_FPF_OUR" #由发送方支付费用
    enum: FPF_SHA "THOST_FTDC_FPF_SHA" #由发送方支付发起的费用，受益方支付接受的费用
    ctypedef char TPassWordKeyTypeType "TZQThostFtdcPassWordKeyTypeType" #密钥类型
    enum: PWKT_ExchangeKey "THOST_FTDC_PWKT_ExchangeKey" #交换密钥
    enum: PWKT_PassWordKey "THOST_FTDC_PWKT_PassWordKey" #密码密钥
    enum: PWKT_MACKey "THOST_FTDC_PWKT_MACKey" #MAC密钥
    enum: PWKT_MessageKey "THOST_FTDC_PWKT_MessageKey" #报文密钥
    ctypedef char TFBTPassWordTypeType "TZQThostFtdcFBTPassWordTypeType" #密码类型
    enum: PWT_Query "THOST_FTDC_PWT_Query" #查询
    enum: PWT_Fetch "THOST_FTDC_PWT_Fetch" #取款
    enum: PWT_Transfer "THOST_FTDC_PWT_Transfer" #转帐
    enum: PWT_Trade "THOST_FTDC_PWT_Trade" #交易
    ctypedef char TFBTEncryModeType "TZQThostFtdcFBTEncryModeType" #加密方式
    enum: EM_NoEncry "THOST_FTDC_EM_NoEncry" #不加密
    enum: EM_DES "THOST_FTDC_EM_DES" #DES
    enum: EM_3DES "THOST_FTDC_EM_3DES" #3DES
    ctypedef char TBankRepealFlagType "TZQThostFtdcBankRepealFlagType" #银行冲正标志
    enum: BRF_BankNotNeedRepeal "THOST_FTDC_BRF_BankNotNeedRepeal" #银行无需自动冲正
    enum: BRF_BankWaitingRepeal "THOST_FTDC_BRF_BankWaitingRepeal" #银行待自动冲正
    enum: BRF_BankBeenRepealed "THOST_FTDC_BRF_BankBeenRepealed" #银行已自动冲正
    ctypedef char TBrokerRepealFlagType "TZQThostFtdcBrokerRepealFlagType" #期商冲正标志
    enum: BRORF_BrokerNotNeedRepeal "THOST_FTDC_BRORF_BrokerNotNeedRepeal" #期商无需自动冲正
    enum: BRORF_BrokerWaitingRepeal "THOST_FTDC_BRORF_BrokerWaitingRepeal" #期商待自动冲正
    enum: BRORF_BrokerBeenRepealed "THOST_FTDC_BRORF_BrokerBeenRepealed" #期商已自动冲正
    ctypedef char TInstitutionTypeType "TZQThostFtdcInstitutionTypeType" #机构类别
    enum: TS_Bank "THOST_FTDC_TS_Bank" #银行
    enum: TS_Future "THOST_FTDC_TS_Future" #期商
    enum: TS_Store "THOST_FTDC_TS_Store" #券商
    ctypedef char TLastFragmentType "TZQThostFtdcLastFragmentType" #最后分片标志
    enum: LF_Yes "THOST_FTDC_LF_Yes" #是最后分片
    enum: LF_No "THOST_FTDC_LF_No" #不是最后分片
    ctypedef char TBankAccStatusType "TZQThostFtdcBankAccStatusType" #银行账户状态
    enum: BAS_Normal "THOST_FTDC_BAS_Normal" #正常
    enum: BAS_Freeze "THOST_FTDC_BAS_Freeze" #冻结
    enum: BAS_ReportLoss "THOST_FTDC_BAS_ReportLoss" #挂失
    ctypedef char TMoneyAccountStatusType "TZQThostFtdcMoneyAccountStatusType" #资金账户状态
    enum: MAS_Normal "THOST_FTDC_MAS_Normal" #正常
    enum: MAS_Cancel "THOST_FTDC_MAS_Cancel" #销户
    ctypedef char TManageStatusType "TZQThostFtdcManageStatusType" #存管状态
    enum: MSS_Point "THOST_FTDC_MSS_Point" #指定存管
    enum: MSS_PrePoint "THOST_FTDC_MSS_PrePoint" #预指定
    enum: MSS_CancelPoint "THOST_FTDC_MSS_CancelPoint" #撤销指定
    ctypedef char TSystemTypeType "TZQThostFtdcSystemTypeType" #应用系统类型
    enum: SYT_FutureBankTransfer "THOST_FTDC_SYT_FutureBankTransfer" #银期转帐
    enum: SYT_StockBankTransfer "THOST_FTDC_SYT_StockBankTransfer" #银证转帐
    enum: SYT_TheThirdPartStore "THOST_FTDC_SYT_TheThirdPartStore" #第三方存管
    ctypedef char TTxnEndFlagType "TZQThostFtdcTxnEndFlagType" #银期转帐划转结果标志
    enum: TEF_NormalProcessing "THOST_FTDC_TEF_NormalProcessing" #正常处理中
    enum: TEF_Success "THOST_FTDC_TEF_Success" #成功结束
    enum: TEF_Failed "THOST_FTDC_TEF_Failed" #失败结束
    enum: TEF_Abnormal "THOST_FTDC_TEF_Abnormal" #异常中
    enum: TEF_ManualProcessedForException "THOST_FTDC_TEF_ManualProcessedForException" #已人工异常处理
    enum: TEF_CommuFailedNeedManualProcess "THOST_FTDC_TEF_CommuFailedNeedManualProcess" #通讯异常 ，请人工处理
    enum: TEF_SysErrorNeedManualProcess "THOST_FTDC_TEF_SysErrorNeedManualProcess" #系统出错，请人工处理
    ctypedef char TProcessStatusType "TZQThostFtdcProcessStatusType" #银期转帐服务处理状态
    enum: PSS_NotProcess "THOST_FTDC_PSS_NotProcess" #未处理
    enum: PSS_StartProcess "THOST_FTDC_PSS_StartProcess" #开始处理
    enum: PSS_Finished "THOST_FTDC_PSS_Finished" #处理完成
    ctypedef char TCustTypeType "TZQThostFtdcCustTypeType" #客户类型
    enum: CUSTT_Person "THOST_FTDC_CUSTT_Person" #自然人
    enum: CUSTT_Institution "THOST_FTDC_CUSTT_Institution" #机构户
    ctypedef char TFBTTransferDirectionType "TZQThostFtdcFBTTransferDirectionType" #银期转帐方向
    enum: FBTTD_FromBankToFuture "THOST_FTDC_FBTTD_FromBankToFuture" #入金，银行转期货
    enum: FBTTD_FromFutureToBank "THOST_FTDC_FBTTD_FromFutureToBank" #出金，期货转银行
    ctypedef char TOpenOrDestroyType "TZQThostFtdcOpenOrDestroyType" #开销户类别
    enum: OOD_Open "THOST_FTDC_OOD_Open" #开户
    enum: OOD_Destroy "THOST_FTDC_OOD_Destroy" #销户
    ctypedef char TAvailabilityFlagType "TZQThostFtdcAvailabilityFlagType" #有效标志
    enum: AVAF_Invalid "THOST_FTDC_AVAF_Invalid" #未确认
    enum: AVAF_Valid "THOST_FTDC_AVAF_Valid" #有效
    enum: AVAF_Repeal "THOST_FTDC_AVAF_Repeal" #冲正
    ctypedef char TOrganTypeType "TZQThostFtdcOrganTypeType" #机构类型
    enum: OT_Bank "THOST_FTDC_OT_Bank" #银行代理
    enum: OT_Future "THOST_FTDC_OT_Future" #交易前置
    enum: OT_PlateForm "THOST_FTDC_OT_PlateForm" #银期转帐平台管理
    ctypedef char TOrganLevelType "TZQThostFtdcOrganLevelType" #机构级别
    enum: OL_HeadQuarters "THOST_FTDC_OL_HeadQuarters" #银行总行或期商总部
    enum: OL_Branch "THOST_FTDC_OL_Branch" #银行分中心或期货公司营业部
    ctypedef char TProtocalIDType "TZQThostFtdcProtocalIDType" #协议类型
    enum: PID_FutureProtocal "THOST_FTDC_PID_FutureProtocal" #期商协议
    enum: PID_ICBCProtocal "THOST_FTDC_PID_ICBCProtocal" #工行协议
    enum: PID_ABCProtocal "THOST_FTDC_PID_ABCProtocal" #农行协议
    enum: PID_CBCProtocal "THOST_FTDC_PID_CBCProtocal" #中国银行协议
    enum: PID_CCBProtocal "THOST_FTDC_PID_CCBProtocal" #建行协议
    enum: PID_BOCOMProtocal "THOST_FTDC_PID_BOCOMProtocal" #交行协议
    enum: PID_FBTPlateFormProtocal "THOST_FTDC_PID_FBTPlateFormProtocal" #银期转帐平台协议
    ctypedef char TConnectModeType "TZQThostFtdcConnectModeType" #套接字连接方式
    enum: CM_ShortConnect "THOST_FTDC_CM_ShortConnect" #短连接
    enum: CM_LongConnect "THOST_FTDC_CM_LongConnect" #长连接
    ctypedef char TSyncModeType "TZQThostFtdcSyncModeType" #套接字通信方式
    enum: SRM_ASync "THOST_FTDC_SRM_ASync" #异步
    enum: SRM_Sync "THOST_FTDC_SRM_Sync" #同步
    ctypedef char TBankAccTypeType "TZQThostFtdcBankAccTypeType" #银行帐号类型
    enum: BAT_BankBook "THOST_FTDC_BAT_BankBook" #银行存折
    enum: BAT_SavingCard "THOST_FTDC_BAT_SavingCard" #储蓄卡
    enum: BAT_CreditCard "THOST_FTDC_BAT_CreditCard" #信用卡
    ctypedef char TFutureAccTypeType "TZQThostFtdcFutureAccTypeType" #期货公司帐号类型
    enum: FAT_BankBook "THOST_FTDC_FAT_BankBook" #银行存折
    enum: FAT_SavingCard "THOST_FTDC_FAT_SavingCard" #储蓄卡
    enum: FAT_CreditCard "THOST_FTDC_FAT_CreditCard" #信用卡
    ctypedef char TOrganStatusType "TZQThostFtdcOrganStatusType" #接入机构状态
    enum: OS_Ready "THOST_FTDC_OS_Ready" #启用
    enum: OS_CheckIn "THOST_FTDC_OS_CheckIn" #签到
    enum: OS_CheckOut "THOST_FTDC_OS_CheckOut" #签退
    enum: OS_CheckFileArrived "THOST_FTDC_OS_CheckFileArrived" #对帐文件到达
    enum: OS_CheckDetail "THOST_FTDC_OS_CheckDetail" #对帐
    enum: OS_DayEndClean "THOST_FTDC_OS_DayEndClean" #日终清理
    enum: OS_Invalid "THOST_FTDC_OS_Invalid" #注销
    ctypedef char TCCBFeeModeType "TZQThostFtdcCCBFeeModeType" #建行收费模式
    enum: CCBFM_ByAmount "THOST_FTDC_CCBFM_ByAmount" #按金额扣收
    enum: CCBFM_ByMonth "THOST_FTDC_CCBFM_ByMonth" #按月扣收
    ctypedef char TCommApiTypeType "TZQThostFtdcCommApiTypeType" #通讯API类型
    enum: CAPIT_Client "THOST_FTDC_CAPIT_Client" #客户端
    enum: CAPIT_Server "THOST_FTDC_CAPIT_Server" #服务端
    enum: CAPIT_UserApi "THOST_FTDC_CAPIT_UserApi" #交易系统的UserApi
    ctypedef int TServiceIDType "TZQThostFtdcServiceIDType" #服务编号
    ctypedef int TServiceLineNoType "TZQThostFtdcServiceLineNoType" #服务线路编号
    ctypedef char[61] TServiceNameType "TZQThostFtdcServiceNameType" #服务名
    ctypedef char TLinkStatusType "TZQThostFtdcLinkStatusType" #连接状态
    enum: LS_Connected "THOST_FTDC_LS_Connected" #已经连接
    enum: LS_Disconnected "THOST_FTDC_LS_Disconnected" #没有连接
    ctypedef int TCommApiPointerType "TZQThostFtdcCommApiPointerType" #通讯API指针
    ctypedef char TPwdFlagType "TZQThostFtdcPwdFlagType" #密码核对标志
    enum: BPWDF_NoCheck "THOST_FTDC_BPWDF_NoCheck" #不核对
    enum: BPWDF_BlankCheck "THOST_FTDC_BPWDF_BlankCheck" #明文核对
    enum: BPWDF_EncryptCheck "THOST_FTDC_BPWDF_EncryptCheck" #密文核对
    ctypedef char TSecuAccTypeType "TZQThostFtdcSecuAccTypeType" #期货帐号类型
    enum: SAT_AccountID "THOST_FTDC_SAT_AccountID" #资金帐号
    enum: SAT_CardID "THOST_FTDC_SAT_CardID" #资金卡号
    enum: SAT_SHStockholderID "THOST_FTDC_SAT_SHStockholderID" #上海股东帐号
    enum: SAT_SZStockholderID "THOST_FTDC_SAT_SZStockholderID" #深圳股东帐号
    ctypedef char TTransferStatusType "TZQThostFtdcTransferStatusType" #转账交易状态
    enum: TRFS_Normal "THOST_FTDC_TRFS_Normal" #正常
    enum: TRFS_Repealed "THOST_FTDC_TRFS_Repealed" #被冲正
    ctypedef char TSponsorTypeType "TZQThostFtdcSponsorTypeType" #发起方
    enum: SPTYPE_Broker "THOST_FTDC_SPTYPE_Broker" #期商
    enum: SPTYPE_Bank "THOST_FTDC_SPTYPE_Bank" #银行
    ctypedef char TReqRspTypeType "TZQThostFtdcReqRspTypeType" #请求响应类别
    enum: REQRSP_Request "THOST_FTDC_REQRSP_Request" #请求
    enum: REQRSP_Response "THOST_FTDC_REQRSP_Response" #响应
    ctypedef char TFBTUserEventTypeType "TZQThostFtdcFBTUserEventTypeType" #银期转帐用户事件类型
    enum: FBTUET_SignIn "THOST_FTDC_FBTUET_SignIn" #签到
    enum: FBTUET_FromBankToFuture "THOST_FTDC_FBTUET_FromBankToFuture" #银行转期货
    enum: FBTUET_FromFutureToBank "THOST_FTDC_FBTUET_FromFutureToBank" #期货转银行
    enum: FBTUET_OpenAccount "THOST_FTDC_FBTUET_OpenAccount" #开户
    enum: FBTUET_CancelAccount "THOST_FTDC_FBTUET_CancelAccount" #销户
    enum: FBTUET_ChangeAccount "THOST_FTDC_FBTUET_ChangeAccount" #变更银行账户
    enum: FBTUET_RepealFromBankToFuture "THOST_FTDC_FBTUET_RepealFromBankToFuture" #冲正银行转期货
    enum: FBTUET_RepealFromFutureToBank "THOST_FTDC_FBTUET_RepealFromFutureToBank" #冲正期货转银行
    enum: FBTUET_QueryBankAccount "THOST_FTDC_FBTUET_QueryBankAccount" #查询银行账户
    enum: FBTUET_QueryFutureAccount "THOST_FTDC_FBTUET_QueryFutureAccount" #查询期货账户
    enum: FBTUET_SignOut "THOST_FTDC_FBTUET_SignOut" #签退
    enum: FBTUET_SyncKey "THOST_FTDC_FBTUET_SyncKey" #密钥同步
    enum: FBTUET_Other "THOST_FTDC_FBTUET_Other" #其他
    ctypedef char[21] TBankIDByBankType "TZQThostFtdcBankIDByBankType" #银行自己的编码
    ctypedef char TNotifyClassType "TZQThostFtdcNotifyClassType" #风险通知类型
    enum: NC_NOERROR "THOST_FTDC_NC_NOERROR" #正常
    enum: NC_Warn "THOST_FTDC_NC_Warn" #警示
    enum: NC_Call "THOST_FTDC_NC_Call" #追保
    enum: NC_Force "THOST_FTDC_NC_Force" #强平
    enum: NC_CHUANCANG "THOST_FTDC_NC_CHUANCANG" #穿仓
    enum: NC_Exception "THOST_FTDC_NC_Exception" #异常
    ctypedef char[257] TRiskNofityInfoType "TZQThostFtdcRiskNofityInfoType" #客户风险通知消息
    ctypedef char[24] TForceCloseSceneIdType "TZQThostFtdcForceCloseSceneIdType" #强平场景编号
    ctypedef char TForceCloseTypeType "TZQThostFtdcForceCloseTypeType" #强平单类型
    enum: FCT_Manual "THOST_FTDC_FCT_Manual" #手工强平
    enum: FCT_Single "THOST_FTDC_FCT_Single" #单一投资者辅助强平
    enum: FCT_Group "THOST_FTDC_FCT_Group" #批量投资者辅助强平
    ctypedef char[101] TInstrumentIDsType "TZQThostFtdcInstrumentIDsType" #多个产品代码,用+分隔,如cu+zn
    ctypedef char TRiskNotifyMethodType "TZQThostFtdcRiskNotifyMethodType" #风险通知途径
    enum: RNM_System "THOST_FTDC_RNM_System" #系统通知
    enum: RNM_SMS "THOST_FTDC_RNM_SMS" #短信通知
    enum: RNM_EMail "THOST_FTDC_RNM_EMail" #邮件通知
    ctypedef char TRiskNotifyStatusType "TZQThostFtdcRiskNotifyStatusType" #风险通知状态
    enum: RNS_NotGen "THOST_FTDC_RNS_NotGen" #未生成
    enum: RNS_Generated "THOST_FTDC_RNS_Generated" #已生成未发送
    enum: RNS_SendError "THOST_FTDC_RNS_SendError" #发送失败
    enum: RNS_SendOk "THOST_FTDC_RNS_SendOk" #已发送未接收
    enum: RNS_Received "THOST_FTDC_RNS_Received" #已接收未确认
    enum: RNS_Confirmed "THOST_FTDC_RNS_Confirmed" #已确认
    ctypedef char TRiskUserEventType "TZQThostFtdcRiskUserEventType" #风控用户操作事件
    enum: RUE_ExportData "THOST_FTDC_RUE_ExportData" #导出数据
    ctypedef char TConditionalOrderSortTypeType "TZQThostFtdcConditionalOrderSortTypeType" #条件单索引条件
    enum: COST_LastPriceAsc "THOST_FTDC_COST_LastPriceAsc" #使用最新价升序
    enum: COST_LastPriceDesc "THOST_FTDC_COST_LastPriceDesc" #使用最新价降序
    enum: COST_AskPriceAsc "THOST_FTDC_COST_AskPriceAsc" #使用卖价升序
    enum: COST_AskPriceDesc "THOST_FTDC_COST_AskPriceDesc" #使用卖价降序
    enum: COST_BidPriceAsc "THOST_FTDC_COST_BidPriceAsc" #使用买价升序
    enum: COST_BidPriceDesc "THOST_FTDC_COST_BidPriceDesc" #使用买价降序
    ctypedef char TSendTypeType "TZQThostFtdcSendTypeType" #报送状态
    enum: UOAST_NoSend "THOST_FTDC_UOAST_NoSend" #未发送
    enum: UOAST_Sended "THOST_FTDC_UOAST_Sended" #已发送
    enum: UOAST_Generated "THOST_FTDC_UOAST_Generated" #已生成
    enum: UOAST_SendFail "THOST_FTDC_UOAST_SendFail" #报送失败
    enum: UOAST_Success "THOST_FTDC_UOAST_Success" #接收成功
    enum: UOAST_Fail "THOST_FTDC_UOAST_Fail" #接收失败
    enum: UOAST_Cancel "THOST_FTDC_UOAST_Cancel" #取消报送
    ctypedef char TClientIDStatusType "TZQThostFtdcClientIDStatusType" #交易编码状态
    enum: UOACS_NoApply "THOST_FTDC_UOACS_NoApply" #未申请
    enum: UOACS_Submited "THOST_FTDC_UOACS_Submited" #已提交申请
    enum: UOACS_Sended "THOST_FTDC_UOACS_Sended" #已发送申请
    enum: UOACS_Success "THOST_FTDC_UOACS_Success" #完成
    enum: UOACS_Refuse "THOST_FTDC_UOACS_Refuse" #拒绝
    enum: UOACS_Cancel "THOST_FTDC_UOACS_Cancel" #已撤销编码
    ctypedef char[17] TIndustryIDType "TZQThostFtdcIndustryIDType" #行业编码
    ctypedef char[5] TQuestionIDType "TZQThostFtdcQuestionIDType" #特有信息编号
    ctypedef char[41] TQuestionContentType "TZQThostFtdcQuestionContentType" #特有信息说明
    ctypedef char[13] TOptionIDType "TZQThostFtdcOptionIDType" #选项编号
    ctypedef char[61] TOptionContentType "TZQThostFtdcOptionContentType" #选项说明
    ctypedef char TQuestionTypeType "TZQThostFtdcQuestionTypeType" #特有信息类型
    enum: QT_Radio "THOST_FTDC_QT_Radio" #单选
    enum: QT_Option "THOST_FTDC_QT_Option" #多选
    enum: QT_Blank "THOST_FTDC_QT_Blank" #填空
    ctypedef char[33] TProcessIDType "TZQThostFtdcProcessIDType" #业务流水号
    ctypedef int TSeqNoType "TZQThostFtdcSeqNoType" #流水号
    ctypedef char[3] TUOAProcessStatusType "TZQThostFtdcUOAProcessStatusType" #流程状态
    ctypedef char TProcessTypeType "TZQThostFtdcProcessTypeType" #流程功能类型
    enum: PT_ApplyTradingCode "THOST_FTDC_PT_ApplyTradingCode" #申请交易编码
    enum: PT_CancelTradingCode "THOST_FTDC_PT_CancelTradingCode" #撤销交易编码
    enum: PT_ModifyIDCard "THOST_FTDC_PT_ModifyIDCard" #修改身份信息
    enum: PT_ModifyNoIDCard "THOST_FTDC_PT_ModifyNoIDCard" #修改一般信息
    enum: PT_ExchOpenBak "THOST_FTDC_PT_ExchOpenBak" #交易所开户报备
    enum: PT_ExchCancelBak "THOST_FTDC_PT_ExchCancelBak" #交易所销户报备
    ctypedef char TBusinessTypeType "TZQThostFtdcBusinessTypeType" #业务类型
    enum: BT_Request "THOST_FTDC_BT_Request" #请求
    enum: BT_Response "THOST_FTDC_BT_Response" #应答
    enum: BT_Notice "THOST_FTDC_BT_Notice" #通知
    ctypedef char TCfmmcReturnCodeType "TZQThostFtdcCfmmcReturnCodeType" #监控中心返回码
    enum: CRC_Success "THOST_FTDC_CRC_Success" #成功
    enum: CRC_Working "THOST_FTDC_CRC_Working" #该客户已经有流程在处理中
    enum: CRC_InfoFail "THOST_FTDC_CRC_InfoFail" #监控中客户资料检查失败
    enum: CRC_IDCardFail "THOST_FTDC_CRC_IDCardFail" #监控中实名制检查失败
    enum: CRC_OtherFail "THOST_FTDC_CRC_OtherFail" #其他错误
    ctypedef int TExReturnCodeType "TZQThostFtdcExReturnCodeType" #交易所返回码
    ctypedef char TClientTypeType "TZQThostFtdcClientTypeType" #客户类型
    enum: CfMMCCT_All "THOST_FTDC_CfMMCCT_All" #所有
    enum: CfMMCCT_Person "THOST_FTDC_CfMMCCT_Person" #个人
    enum: CfMMCCT_Company "THOST_FTDC_CfMMCCT_Company" #单位
    ctypedef char TExchangeIDTypeType "TZQThostFtdcExchangeIDTypeType" #交易所编号
    enum: EIDT_SHFE "THOST_FTDC_EIDT_SHFE" #上海期货交易所
    enum: EIDT_CZCE "THOST_FTDC_EIDT_CZCE" #郑州商品交易所
    enum: EIDT_DCE "THOST_FTDC_EIDT_DCE" #大连商品交易所
    enum: EIDT_CFFEX "THOST_FTDC_EIDT_CFFEX" #中国金融期货交易所
    ctypedef char TExClientIDTypeType "TZQThostFtdcExClientIDTypeType" #交易编码类型
    enum: ECIDT_Hedge "THOST_FTDC_ECIDT_Hedge" #套保
    enum: ECIDT_Arbitrage "THOST_FTDC_ECIDT_Arbitrage" #套利
    enum: ECIDT_Speculation "THOST_FTDC_ECIDT_Speculation" #投机
    ctypedef char[11] TClientClassifyType "TZQThostFtdcClientClassifyType" #客户分类码
    ctypedef char[9] TUOAOrganTypeType "TZQThostFtdcUOAOrganTypeType" #单位性质
    ctypedef char[9] TUOACountryCodeType "TZQThostFtdcUOACountryCodeType" #国家代码
    ctypedef char[9] TAreaCodeType "TZQThostFtdcAreaCodeType" #区号
    ctypedef char[21] TFuturesIDType "TZQThostFtdcFuturesIDType" #监控中心为客户分配的代码
    ctypedef char[11] TCffmcDateType "TZQThostFtdcCffmcDateType" #日期
    ctypedef char[11] TCffmcTimeType "TZQThostFtdcCffmcTimeType" #时间
    ctypedef char[21] TNocIDType "TZQThostFtdcNocIDType" #组织机构代码
    ctypedef char TUpdateFlagType "TZQThostFtdcUpdateFlagType" #更新状态
    enum: UF_NoUpdate "THOST_FTDC_UF_NoUpdate" #未更新
    enum: UF_Success "THOST_FTDC_UF_Success" #更新全部信息成功
    enum: UF_Fail "THOST_FTDC_UF_Fail" #更新全部信息失败
    enum: UF_TCSuccess "THOST_FTDC_UF_TCSuccess" #更新交易编码成功
    enum: UF_TCFail "THOST_FTDC_UF_TCFail" #更新交易编码失败
    enum: UF_Cancel "THOST_FTDC_UF_Cancel" #已丢弃
    ctypedef char TApplyOperateIDType "TZQThostFtdcApplyOperateIDType" #申请动作
    enum: AOID_OpenInvestor "THOST_FTDC_AOID_OpenInvestor" #开户
    enum: AOID_ModifyIDCard "THOST_FTDC_AOID_ModifyIDCard" #修改身份信息
    enum: AOID_ModifyNoIDCard "THOST_FTDC_AOID_ModifyNoIDCard" #修改一般信息
    enum: AOID_ApplyTradingCode "THOST_FTDC_AOID_ApplyTradingCode" #申请交易编码
    enum: AOID_CancelTradingCode "THOST_FTDC_AOID_CancelTradingCode" #撤销交易编码
    enum: AOID_CancelInvestor "THOST_FTDC_AOID_CancelInvestor" #销户
    ctypedef char TApplyStatusIDType "TZQThostFtdcApplyStatusIDType" #申请状态
    enum: ASID_NoComplete "THOST_FTDC_ASID_NoComplete" #未补全
    enum: ASID_Submited "THOST_FTDC_ASID_Submited" #已提交
    enum: ASID_Checked "THOST_FTDC_ASID_Checked" #已审核
    enum: ASID_Refused "THOST_FTDC_ASID_Refused" #已拒绝
    enum: ASID_Deleted "THOST_FTDC_ASID_Deleted" #已删除
    ctypedef char TSendMethodType "TZQThostFtdcSendMethodType" #发送方式
    enum: UOASM_ByAPI "THOST_FTDC_UOASM_ByAPI" #电子发送
    enum: UOASM_ByFile "THOST_FTDC_UOASM_ByFile" #文件发送
    ctypedef char[33] TEventTypeType "TZQThostFtdcEventTypeType" #业务操作类型
    ctypedef char TEventModeType "TZQThostFtdcEventModeType" #操作方法
    enum: EvM_ADD "THOST_FTDC_EvM_ADD" #增加
    enum: EvM_UPDATE "THOST_FTDC_EvM_UPDATE" #修改
    enum: EvM_DELETE "THOST_FTDC_EvM_DELETE" #删除
    enum: EvM_CHECK "THOST_FTDC_EvM_CHECK" #复核
    ctypedef char TUOAAutoSendType "TZQThostFtdcUOAAutoSendType" #统一开户申请自动发送
    enum: UOAA_ASR "THOST_FTDC_UOAA_ASR" #自动发送并接收
    enum: UOAA_ASNR "THOST_FTDC_UOAA_ASNR" #自动发送，不自动接收
    enum: UOAA_NSAR "THOST_FTDC_UOAA_NSAR" #不自动发送，自动接收
    enum: UOAA_NSR "THOST_FTDC_UOAA_NSR" #不自动发送，也不自动接收
    ctypedef int TQueryDepthType "TZQThostFtdcQueryDepthType" #查询深度
    ctypedef int TDataCenterIDType "TZQThostFtdcDataCenterIDType" #数据中心代码
    ctypedef char TFlowIDType "TZQThostFtdcFlowIDType" #流程ID
    enum: EvM_InvestorGroupFlow "THOST_FTDC_EvM_InvestorGroupFlow" #投资者对应投资者组设置
    ctypedef char TCheckLevelType "TZQThostFtdcCheckLevelType" #复核级别
    enum: CL_Zero "THOST_FTDC_CL_Zero" #零级复核
    enum: CL_One "THOST_FTDC_CL_One" #一级复核
    enum: CL_Two "THOST_FTDC_CL_Two" #二级复核
    ctypedef int TCheckNoType "TZQThostFtdcCheckNoType" #操作次数
    ctypedef char TCheckStatusType "TZQThostFtdcCheckStatusType" #复核级别
    enum: CHS_Init "THOST_FTDC_CHS_Init" #未复核
    enum: CHS_Checking "THOST_FTDC_CHS_Checking" #复核中
    enum: CHS_Checked "THOST_FTDC_CHS_Checked" #已复核
    enum: CHS_Refuse "THOST_FTDC_CHS_Refuse" #拒绝
    enum: CHS_Cancel "THOST_FTDC_CHS_Cancel" #作废
    ctypedef char TUsedStatusType "TZQThostFtdcUsedStatusType" #生效状态
    enum: CHU_Unused "THOST_FTDC_CHU_Unused" #未生效
    enum: CHU_Used "THOST_FTDC_CHU_Used" #已生效
    enum: CHU_Fail "THOST_FTDC_CHU_Fail" #生效失败
    ctypedef char[61] TRateTemplateNameType "TZQThostFtdcRateTemplateNameType" #模型名称
    ctypedef char[2049] TPropertyStringType "TZQThostFtdcPropertyStringType" #用于查询的投资属性字段
    ctypedef char TBankAcountOriginType "TZQThostFtdcBankAcountOriginType" #账户来源
    enum: BAO_ByAccProperty "THOST_FTDC_BAO_ByAccProperty" #手工录入
    enum: BAO_ByFBTransfer "THOST_FTDC_BAO_ByFBTransfer" #银期转账
    ctypedef char TMonthBillTradeSumType "TZQThostFtdcMonthBillTradeSumType" #结算单月报成交汇总方式
    enum: MBTS_ByInstrument "THOST_FTDC_MBTS_ByInstrument" #同日同合约
    enum: MBTS_ByDayInsPrc "THOST_FTDC_MBTS_ByDayInsPrc" #同日同合约同价格
    enum: MBTS_ByDayIns "THOST_FTDC_MBTS_ByDayIns" #同合约
    ctypedef char[7] TFBTTradeCodeEnumType "TZQThostFtdcFBTTradeCodeEnumType" #银期交易代码枚举
    enum: FTC_BankLaunchBankToBroker "THOST_FTDC_FTC_BankLaunchBankToBroker" #银行发起银行转期货
    enum: FTC_BrokerLaunchBankToBroker "THOST_FTDC_FTC_BrokerLaunchBankToBroker" #期货发起银行转期货
    enum: FTC_BankLaunchBrokerToBank "THOST_FTDC_FTC_BankLaunchBrokerToBank" #银行发起期货转银行
    enum: FTC_BrokerLaunchBrokerToBank "THOST_FTDC_FTC_BrokerLaunchBrokerToBank" #期货发起期货转银行
    ctypedef char[9] TRateTemplateIDType "TZQThostFtdcRateTemplateIDType" #模型代码
    ctypedef char[21] TRiskRateType "TZQThostFtdcRiskRateType" #风险度
    ctypedef int TTimestampType "TZQThostFtdcTimestampType" #时间戳
    ctypedef char[61] TInvestorIDRuleNameType "TZQThostFtdcInvestorIDRuleNameType" #号段规则名称
    ctypedef char[513] TInvestorIDRuleExprType "TZQThostFtdcInvestorIDRuleExprType" #号段规则表达式
    ctypedef int TLastDriftType "TZQThostFtdcLastDriftType" #上次OTP漂移值
    ctypedef int TLastSuccessType "TZQThostFtdcLastSuccessType" #上次OTP成功值
    ctypedef char[41] TAuthKeyType "TZQThostFtdcAuthKeyType" #令牌密钥
    ctypedef char[17] TSerialNumberType "TZQThostFtdcSerialNumberType" #序列号
    ctypedef char TOTPTypeType "TZQThostFtdcOTPTypeType" #动态令牌类型
    enum: OTP_NONE "THOST_FTDC_OTP_NONE" #无动态令牌
    enum: OTP_TOTP "THOST_FTDC_OTP_TOTP" #时间令牌
    ctypedef char[2] TOTPVendorsIDType "TZQThostFtdcOTPVendorsIDType" #动态令牌提供商
    ctypedef char[61] TOTPVendorsNameType "TZQThostFtdcOTPVendorsNameType" #动态令牌提供商名称
    ctypedef char TOTPStatusType "TZQThostFtdcOTPStatusType" #动态令牌状态
    enum: OTPS_Unused "THOST_FTDC_OTPS_Unused" #未使用
    enum: OTPS_Used "THOST_FTDC_OTPS_Used" #已使用
    enum: OTPS_Disuse "THOST_FTDC_OTPS_Disuse" #注销
    ctypedef char TBrokerUserTypeType "TZQThostFtdcBrokerUserTypeType" #经济公司用户类型
    enum: BUT_Investor "THOST_FTDC_BUT_Investor" #投资者
    ctypedef char TFutureTypeType "TZQThostFtdcFutureTypeType" #期货类型
    enum: FUTT_Commodity "THOST_FTDC_FUTT_Commodity" #商品期货
    enum: FUTT_Financial "THOST_FTDC_FUTT_Financial" #金融期货
    ctypedef char TFundEventTypeType "TZQThostFtdcFundEventTypeType" #资金管理操作类型
    enum: FET_Restriction "THOST_FTDC_FET_Restriction" #转账限额
    enum: FET_TodayRestriction "THOST_FTDC_FET_TodayRestriction" #当日转账限额
    enum: FET_Transfer "THOST_FTDC_FET_Transfer" #期商流水
    enum: FET_Credit "THOST_FTDC_FET_Credit" #资金冻结
    enum: FET_InvestorWithdrawAlm "THOST_FTDC_FET_InvestorWithdrawAlm" #投资者可提资金比例
    ctypedef char TAccountSourceTypeType "TZQThostFtdcAccountSourceTypeType" #资金账户来源
    enum: AST_FBTransfer "THOST_FTDC_AST_FBTransfer" #银期同步
    enum: AST_ManualEntry "THOST_FTDC_AST_ManualEntry" #手工录入
    ctypedef char TCodeSourceTypeType "TZQThostFtdcCodeSourceTypeType" #交易编码来源
    enum: CST_UnifyAccount "THOST_FTDC_CST_UnifyAccount" #统一开户
    enum: CST_ManualEntry "THOST_FTDC_CST_ManualEntry" #手工录入
    ctypedef char TUserRangeType "TZQThostFtdcUserRangeType" #操作员范围
    enum: UR_All "THOST_FTDC_UR_All" #所有
    enum: UR_Single "THOST_FTDC_UR_Single" #单一操作员
    ctypedef char[9] TTimeSpanType "TZQThostFtdcTimeSpanType" #时间跨度
    ctypedef char[17] TImportSequenceIDType "TZQThostFtdcImportSequenceIDType" #动态令牌导入批次编号
    ctypedef char[9] TBranchIDType "TZQThostFtdcBranchIDType" #营业部编号
    ctypedef char[17] TTableNameType "TZQThostFtdcTableNameType" #和交易所交换表编号
    ctypedef char[9] TStockPriceType "TZQThostFtdcStockPriceType" #证券交易价格
    ctypedef char TStockTradeTypeType "TZQThostFtdcStockTradeTypeType" #证券交易类型
    enum: STT_Stock "THOST_FTDC_STT_Stock" #可交易证券
    enum: STT_BuyNetService "THOST_FTDC_STT_BuyNetService" #买入网络密码服务
    enum: STT_CancelRepurchase "THOST_FTDC_STT_CancelRepurchase" #回购注销
    enum: STT_CancelRegister "THOST_FTDC_STT_CancelRegister" #指定撤销
    enum: STT_Register "THOST_FTDC_STT_Register" #指定登记
    enum: STT_PurchaseIssue "THOST_FTDC_STT_PurchaseIssue" #买入发行申购
    enum: STT_Allotment "THOST_FTDC_STT_Allotment" #卖出配股
    enum: STT_SellTender "THOST_FTDC_STT_SellTender" #卖出要约收购
    enum: STT_BuyTender "THOST_FTDC_STT_BuyTender" #买入要约收购
    enum: STT_NetVote "THOST_FTDC_STT_NetVote" #网上投票
    enum: STT_SellConvertibleBonds "THOST_FTDC_STT_SellConvertibleBonds" #卖出可转债回售
    enum: STT_OptionExecute "THOST_FTDC_STT_OptionExecute" #权证行权代码
    enum: STT_PurchaseOF "THOST_FTDC_STT_PurchaseOF" #开放式基金申购
    enum: STT_RedeemOF "THOST_FTDC_STT_RedeemOF" #开放式基金赎回
    enum: STT_SubscribeOF "THOST_FTDC_STT_SubscribeOF" #开放式基金认购
    enum: STT_OFCustodianTranfer "THOST_FTDC_STT_OFCustodianTranfer" #开放式基金转托管转出
    enum: STT_OFDividendConfig "THOST_FTDC_STT_OFDividendConfig" #开放式基金分红设置
    enum: STT_OFTransfer "THOST_FTDC_STT_OFTransfer" #开放式基金转成其他基金
    enum: STT_BondsIn "THOST_FTDC_STT_BondsIn" #债券入库
    enum: STT_BondsOut "THOST_FTDC_STT_BondsOut" #债券出库
    enum: STT_PurchaseETF "THOST_FTDC_STT_PurchaseETF" #EFT申购
    enum: STT_RedeemETF "THOST_FTDC_STT_RedeemETF" #EFT赎回
    enum: STT_ConvertibleRegister "THOST_FTDC_STT_ConvertibleRegister" #可转债回售登记
    ctypedef char[11] TStockSeqType "TZQThostFtdcStockSeqType" #股票使用流水号
    ctypedef int TStockWthType "TZQThostFtdcStockWthType" #股票使用流水号
    ctypedef int TWTFSType "TZQThostFtdcWTFSType" #委托方式
    ctypedef int TWTLBType "TZQThostFtdcWTLBType" #委托类别
    ctypedef int TWTRQType "TZQThostFtdcWTRQType" #委托日期
    ctypedef char TCreationredemptionStatusType "TZQThostFtdcCreationredemptionStatusType" #基金当天申购赎回状态
    enum: CDS_Forbidden "THOST_FTDC_CDS_Forbidden" #不允许申购赎回
    enum: CDS_Allow "THOST_FTDC_CDS_Allow" #表示允许申购和赎回
    enum: CDS_OnlyPurchase "THOST_FTDC_CDS_OnlyPurchase" #允许申购、不允许赎回
    enum: CDS_OnlyRedeem "THOST_FTDC_CDS_OnlyRedeem" #不允许申购、允许赎回
    ctypedef char TETFCurrenceReplaceStatusType "TZQThostFtdcETFCurrenceReplaceStatusType" #ETF现金替代标志
    enum: ETFCRS_Forbidden "THOST_FTDC_ETFCRS_Forbidden" #禁止现金替代
    enum: ETFCRS_Allow "THOST_FTDC_ETFCRS_Allow" #可以现金替代
    enum: ETFCRS_Force "THOST_FTDC_ETFCRS_Force" #必须现金替代
    ctypedef int TINTEGERType "TZQThostFtdcINTEGERType" #一般整型
    ctypedef int TINT3Type "TZQThostFtdcINT3Type" #三位数整型
    ctypedef int TINT6Type "TZQThostFtdcINT6Type" #六位数整型
    ctypedef double TREAL9P3Type "TZQThostFtdcREAL9P3Type" #九点三实型
    ctypedef double TREAL10P4Type "TZQThostFtdcREAL10P4Type" #十点四实型
    ctypedef double TREAL16P2Type "TZQThostFtdcREAL16P2Type" #十六点二实型
    ctypedef double TREAL16P8Type "TZQThostFtdcREAL16P8Type" #十六点八实型
    ctypedef double TREAL22P2Type "TZQThostFtdcREAL22P2Type" #二十二点二实型
    ctypedef char[2] TCHAR1Type "TZQThostFtdcCHAR1Type" #一字节CHAR
    ctypedef char[3] TCHAR2Type "TZQThostFtdcCHAR2Type" #二字节CHAR
    ctypedef char[4] TCHAR3Type "TZQThostFtdcCHAR3Type" #三字节CHAR
    ctypedef char[5] TCHAR4Type "TZQThostFtdcCHAR4Type" #四字节CHAR
    ctypedef char[6] TCHAR5Type "TZQThostFtdcCHAR5Type" #五字节CHAR
    ctypedef char[7] TCHAR6Type "TZQThostFtdcCHAR6Type" #六字节CHAR
    ctypedef char[9] TCHAR8Type "TZQThostFtdcCHAR8Type" #八字节CHAR
    ctypedef char[11] TCHAR10Type "TZQThostFtdcCHAR10Type" #十字节CHAR
    ctypedef char[13] TCHAR12Type "TZQThostFtdcCHAR12Type" #十二字节CHAR
    ctypedef char[14] TCHAR13Type "TZQThostFtdcCHAR13Type" #十三字节CHAR
    ctypedef char[15] TCHAR14Type "TZQThostFtdcCHAR14Type" #十四字节CHAR
    ctypedef char[17] TCHAR16Type "TZQThostFtdcCHAR16Type" #十六字节CHAR
    ctypedef char[5] TVCHAR4Type "TZQThostFtdcVCHAR4Type" #四字节VCHAR
    ctypedef char[7] TVCHAR6Type "TZQThostFtdcVCHAR6Type" #六字节VCHAR
    ctypedef char[9] TVCHAR8Type "TZQThostFtdcVCHAR8Type" #八字节VCHAR
    ctypedef char[11] TVCHAR10Type "TZQThostFtdcVCHAR10Type" #十字节VCHAR
    ctypedef char[13] TVCHAR12Type "TZQThostFtdcVCHAR12Type" #十二字节VCHAR
    ctypedef char[17] TVCHAR16Type "TZQThostFtdcVCHAR16Type" #十六字节VCHAR
    ctypedef char[21] TVCHAR20Type "TZQThostFtdcVCHAR20Type" #二十字节VCHAR
    ctypedef char[31] TVCHAR30Type "TZQThostFtdcVCHAR30Type" #三十字节VCHAR
    ctypedef char[51] TVCHAR50Type "TZQThostFtdcVCHAR50Type" #五十字节VCHAR
    ctypedef char[61] TVCHAR60Type "TZQThostFtdcVCHAR60Type" #六十字节VCHAR
    ctypedef char[66] TVCHAR65Type "TZQThostFtdcVCHAR65Type" #六十五字节VCHAR
    ctypedef char[81] TVCHAR80Type "TZQThostFtdcVCHAR80Type" #八十字节VCHAR
    ctypedef char[256] TVCHAR255Type "TZQThostFtdcVCHAR255Type" #二五五字节VCHAR
    ctypedef char[129] TAuthInfoType "TZQThostFtdcAuthInfoType" #客户端认证信息
    ctypedef char[17] TAuthCodeType "TZQThostFtdcAuthCodeType" #客户端认证码
