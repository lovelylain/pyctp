# -*- coding: utf-8 -*-

cdef extern from "ThostFtdcUserApiDataType.h":
    cdef enum TE_RESUME_TYPE "THOST_TE_RESUME_TYPE": #流重传方式
        TERT_RESTART "THOST_TERT_RESTART" #从本交易日开始重传
        TERT_RESUME "THOST_TERT_RESUME" #从上次收到的续传
        TERT_QUICK "THOST_TERT_QUICK" #只传送登录后的流内容
    ctypedef char[21] TTraderIDType "TThostFtdcTraderIDType" #交易所交易员代码
    ctypedef char[13] TInvestorIDType "TThostFtdcInvestorIDType" #投资者代码
    ctypedef char[11] TBrokerIDType "TThostFtdcBrokerIDType" #经纪公司代码
    ctypedef char[9] TBrokerAbbrType "TThostFtdcBrokerAbbrType" #经纪公司简称
    ctypedef char[81] TBrokerNameType "TThostFtdcBrokerNameType" #经纪公司名称
    ctypedef char[31] TExchangeInstIDType "TThostFtdcExchangeInstIDType" #合约在交易所的代码
    ctypedef char[13] TOrderRefType "TThostFtdcOrderRefType" #报单引用
    ctypedef char[11] TParticipantIDType "TThostFtdcParticipantIDType" #会员代码
    ctypedef char[16] TUserIDType "TThostFtdcUserIDType" #用户代码
    ctypedef char[41] TPasswordType "TThostFtdcPasswordType" #密码
    ctypedef char[11] TClientIDType "TThostFtdcClientIDType" #交易编码
    ctypedef char[31] TInstrumentIDType "TThostFtdcInstrumentIDType" #合约代码
    ctypedef char[31] TMarketIDType "TThostFtdcMarketIDType" #市场代码
    ctypedef char[21] TProductNameType "TThostFtdcProductNameType" #产品名称
    ctypedef char[9] TExchangeIDType "TThostFtdcExchangeIDType" #交易所代码
    ctypedef char[61] TExchangeNameType "TThostFtdcExchangeNameType" #交易所名称
    ctypedef char[9] TExchangeAbbrType "TThostFtdcExchangeAbbrType" #交易所简称
    ctypedef char[2] TExchangeFlagType "TThostFtdcExchangeFlagType" #交易所标志
    ctypedef char[21] TMacAddressType "TThostFtdcMacAddressType" #Mac地址
    ctypedef char[21] TSystemIDType "TThostFtdcSystemIDType" #系统编号
    ctypedef char TExchangePropertyType "TThostFtdcExchangePropertyType" #交易所属性
    enum: EXP_Normal "THOST_FTDC_EXP_Normal" #正常
    enum: EXP_GenOrderByTrade "THOST_FTDC_EXP_GenOrderByTrade" #根据成交生成报单
    ctypedef char[9] TDateType "TThostFtdcDateType" #日期
    ctypedef char[9] TTimeType "TThostFtdcTimeType" #时间
    ctypedef char[13] TLongTimeType "TThostFtdcLongTimeType" #长时间
    ctypedef char[21] TInstrumentNameType "TThostFtdcInstrumentNameType" #合约名称
    ctypedef char[9] TSettlementGroupIDType "TThostFtdcSettlementGroupIDType" #结算组代码
    ctypedef char[21] TOrderSysIDType "TThostFtdcOrderSysIDType" #报单编号
    ctypedef char[21] TTradeIDType "TThostFtdcTradeIDType" #成交编号
    ctypedef char[65] TCommandTypeType "TThostFtdcCommandTypeType" #DB命令类型
    ctypedef char[16] TIPAddressType "TThostFtdcIPAddressType" #IP地址
    ctypedef int TIPPortType "TThostFtdcIPPortType" #IP端口
    ctypedef char[11] TProductInfoType "TThostFtdcProductInfoType" #产品信息
    ctypedef char[11] TProtocolInfoType "TThostFtdcProtocolInfoType" #协议信息
    ctypedef char[21] TBusinessUnitType "TThostFtdcBusinessUnitType" #业务单元
    ctypedef char[15] TDepositSeqNoType "TThostFtdcDepositSeqNoType" #出入金流水号
    ctypedef char[51] TIdentifiedCardNoType "TThostFtdcIdentifiedCardNoType" #证件号码
    ctypedef char TIdCardTypeType "TThostFtdcIdCardTypeType" #证件类型
    enum: ICT_EID "THOST_FTDC_ICT_EID" #组织机构代码
    enum: ICT_IDCard "THOST_FTDC_ICT_IDCard" #中国公民身份证
    enum: ICT_OfficerIDCard "THOST_FTDC_ICT_OfficerIDCard" #军官证
    enum: ICT_PoliceIDCard "THOST_FTDC_ICT_PoliceIDCard" #警官证
    enum: ICT_SoldierIDCard "THOST_FTDC_ICT_SoldierIDCard" #士兵证
    enum: ICT_HouseholdRegister "THOST_FTDC_ICT_HouseholdRegister" #户口簿
    enum: ICT_Passport "THOST_FTDC_ICT_Passport" #护照
    enum: ICT_TaiwanCompatriotIDCard "THOST_FTDC_ICT_TaiwanCompatriotIDCard" #台胞证
    enum: ICT_HomeComingCard "THOST_FTDC_ICT_HomeComingCard" #回乡证
    enum: ICT_LicenseNo "THOST_FTDC_ICT_LicenseNo" #营业执照号
    enum: ICT_TaxNo "THOST_FTDC_ICT_TaxNo" #税务登记号/当地纳税ID
    enum: ICT_HMMainlandTravelPermit "THOST_FTDC_ICT_HMMainlandTravelPermit" #港澳居民来往内地通行证
    enum: ICT_TwMainlandTravelPermit "THOST_FTDC_ICT_TwMainlandTravelPermit" #台湾居民来往大陆通行证
    enum: ICT_DrivingLicense "THOST_FTDC_ICT_DrivingLicense" #驾照
    enum: ICT_SocialID "THOST_FTDC_ICT_SocialID" #当地社保ID
    enum: ICT_LocalID "THOST_FTDC_ICT_LocalID" #当地身份证
    enum: ICT_BusinessRegistration "THOST_FTDC_ICT_BusinessRegistration" #商业登记证
    enum: ICT_HKMCIDCard "THOST_FTDC_ICT_HKMCIDCard" #港澳永久性居民身份证
    enum: ICT_AccountsPermits "THOST_FTDC_ICT_AccountsPermits" #人行开户许可证
    enum: ICT_OtherCard "THOST_FTDC_ICT_OtherCard" #其他证件
    ctypedef char[13] TOrderLocalIDType "TThostFtdcOrderLocalIDType" #本地报单编号
    ctypedef char[81] TUserNameType "TThostFtdcUserNameType" #用户名称
    ctypedef char[81] TPartyNameType "TThostFtdcPartyNameType" #参与人名称
    ctypedef char[81] TErrorMsgType "TThostFtdcErrorMsgType" #错误信息
    ctypedef char[2049] TFieldNameType "TThostFtdcFieldNameType" #字段名
    ctypedef char[2049] TFieldContentType "TThostFtdcFieldContentType" #字段内容
    ctypedef char[41] TSystemNameType "TThostFtdcSystemNameType" #系统名称
    ctypedef char[501] TContentType "TThostFtdcContentType" #消息正文
    ctypedef char TInvestorRangeType "TThostFtdcInvestorRangeType" #投资者范围
    enum: IR_All "THOST_FTDC_IR_All" #所有
    enum: IR_Group "THOST_FTDC_IR_Group" #投资者组
    enum: IR_Single "THOST_FTDC_IR_Single" #单一投资者
    ctypedef char TDepartmentRangeType "TThostFtdcDepartmentRangeType" #投资者范围
    enum: DR_All "THOST_FTDC_DR_All" #所有
    enum: DR_Group "THOST_FTDC_DR_Group" #组织架构
    enum: DR_Single "THOST_FTDC_DR_Single" #单一投资者
    ctypedef char TDataSyncStatusType "TThostFtdcDataSyncStatusType" #数据同步状态
    enum: DS_Asynchronous "THOST_FTDC_DS_Asynchronous" #未同步
    enum: DS_Synchronizing "THOST_FTDC_DS_Synchronizing" #同步中
    enum: DS_Synchronized "THOST_FTDC_DS_Synchronized" #已同步
    ctypedef char TBrokerDataSyncStatusType "TThostFtdcBrokerDataSyncStatusType" #经纪公司数据同步状态
    enum: BDS_Synchronized "THOST_FTDC_BDS_Synchronized" #已同步
    enum: BDS_Synchronizing "THOST_FTDC_BDS_Synchronizing" #同步中
    ctypedef char TExchangeConnectStatusType "TThostFtdcExchangeConnectStatusType" #交易所连接状态
    enum: ECS_NoConnection "THOST_FTDC_ECS_NoConnection" #没有任何连接
    enum: ECS_QryInstrumentSent "THOST_FTDC_ECS_QryInstrumentSent" #已经发出合约查询请求
    enum: ECS_GotInformation "THOST_FTDC_ECS_GotInformation" #已经获取信息
    ctypedef char TTraderConnectStatusType "TThostFtdcTraderConnectStatusType" #交易所交易员连接状态
    enum: TCS_NotConnected "THOST_FTDC_TCS_NotConnected" #没有任何连接
    enum: TCS_Connected "THOST_FTDC_TCS_Connected" #已经连接
    enum: TCS_QryInstrumentSent "THOST_FTDC_TCS_QryInstrumentSent" #已经发出合约查询请求
    enum: TCS_SubPrivateFlow "THOST_FTDC_TCS_SubPrivateFlow" #订阅私有流
    ctypedef char TFunctionCodeType "TThostFtdcFunctionCodeType" #功能代码
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
    enum: FC_ParkedOrderInsert "THOST_FTDC_FC_ParkedOrderInsert" #预埋报单插入
    enum: FC_ParkedOrderAction "THOST_FTDC_FC_ParkedOrderAction" #预埋报单操作
    enum: FC_SyncOTP "THOST_FTDC_FC_SyncOTP" #同步动态令牌
    enum: FC_DeleteOrder "THOST_FTDC_FC_DeleteOrder" #删除未知单
    ctypedef char TBrokerFunctionCodeType "TThostFtdcBrokerFunctionCodeType" #经纪公司功能代码
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
    enum: BFC_MarketDataWarn "THOST_FTDC_BFC_MarketDataWarn" #行情预警
    enum: BFC_QryBizNotice "THOST_FTDC_BFC_QryBizNotice" #业务通知查询
    enum: BFC_CfgBizNotice "THOST_FTDC_BFC_CfgBizNotice" #业务通知模板设置
    enum: BFC_SyncOTP "THOST_FTDC_BFC_SyncOTP" #同步动态令牌
    enum: BFC_SendBizNotice "THOST_FTDC_BFC_SendBizNotice" #发送业务通知
    enum: BFC_CfgRiskLevelStd "THOST_FTDC_BFC_CfgRiskLevelStd" #风险级别标准设置
    enum: BFC_TbCommand "THOST_FTDC_BFC_TbCommand" #交易终端应急功能
    enum: BFC_DeleteOrder "THOST_FTDC_BFC_DeleteOrder" #删除未知单
    enum: BFC_ParkedOrderInsert "THOST_FTDC_BFC_ParkedOrderInsert" #预埋报单插入
    enum: BFC_ParkedOrderAction "THOST_FTDC_BFC_ParkedOrderAction" #预埋报单操作
    ctypedef char TOrderActionStatusType "TThostFtdcOrderActionStatusType" #报单操作状态
    enum: OAS_Submitted "THOST_FTDC_OAS_Submitted" #已经提交
    enum: OAS_Accepted "THOST_FTDC_OAS_Accepted" #已经接受
    enum: OAS_Rejected "THOST_FTDC_OAS_Rejected" #已经被拒绝
    ctypedef char TOrderStatusType "TThostFtdcOrderStatusType" #报单状态
    enum: OST_AllTraded "THOST_FTDC_OST_AllTraded" #全部成交
    enum: OST_PartTradedQueueing "THOST_FTDC_OST_PartTradedQueueing" #部分成交还在队列中
    enum: OST_PartTradedNotQueueing "THOST_FTDC_OST_PartTradedNotQueueing" #部分成交不在队列中
    enum: OST_NoTradeQueueing "THOST_FTDC_OST_NoTradeQueueing" #未成交还在队列中
    enum: OST_NoTradeNotQueueing "THOST_FTDC_OST_NoTradeNotQueueing" #未成交不在队列中
    enum: OST_Canceled "THOST_FTDC_OST_Canceled" #撤单
    enum: OST_Unknown "THOST_FTDC_OST_Unknown" #未知
    enum: OST_NotTouched "THOST_FTDC_OST_NotTouched" #尚未触发
    enum: OST_Touched "THOST_FTDC_OST_Touched" #已触发
    ctypedef char TOrderSubmitStatusType "TThostFtdcOrderSubmitStatusType" #报单提交状态
    enum: OSS_InsertSubmitted "THOST_FTDC_OSS_InsertSubmitted" #已经提交
    enum: OSS_CancelSubmitted "THOST_FTDC_OSS_CancelSubmitted" #撤单已经提交
    enum: OSS_ModifySubmitted "THOST_FTDC_OSS_ModifySubmitted" #修改已经提交
    enum: OSS_Accepted "THOST_FTDC_OSS_Accepted" #已经接受
    enum: OSS_InsertRejected "THOST_FTDC_OSS_InsertRejected" #报单已经被拒绝
    enum: OSS_CancelRejected "THOST_FTDC_OSS_CancelRejected" #撤单已经被拒绝
    enum: OSS_ModifyRejected "THOST_FTDC_OSS_ModifyRejected" #改单已经被拒绝
    ctypedef char TPositionDateType "TThostFtdcPositionDateType" #持仓日期
    enum: PSD_Today "THOST_FTDC_PSD_Today" #今日持仓
    enum: PSD_History "THOST_FTDC_PSD_History" #历史持仓
    ctypedef char TPositionDateTypeType "TThostFtdcPositionDateTypeType" #持仓日期类型
    enum: PDT_UseHistory "THOST_FTDC_PDT_UseHistory" #使用历史持仓
    enum: PDT_NoUseHistory "THOST_FTDC_PDT_NoUseHistory" #不使用历史持仓
    ctypedef char TTradingRoleType "TThostFtdcTradingRoleType" #交易角色
    enum: ER_Broker "THOST_FTDC_ER_Broker" #代理
    enum: ER_Host "THOST_FTDC_ER_Host" #自营
    enum: ER_Maker "THOST_FTDC_ER_Maker" #做市商
    ctypedef char TProductClassType "TThostFtdcProductClassType" #产品类型
    enum: PC_Futures "THOST_FTDC_PC_Futures" #期货
    enum: PC_Options "THOST_FTDC_PC_Options" #期货期权
    enum: PC_Combination "THOST_FTDC_PC_Combination" #组合
    enum: PC_Spot "THOST_FTDC_PC_Spot" #即期
    enum: PC_EFP "THOST_FTDC_PC_EFP" #期转现
    enum: PC_SpotOption "THOST_FTDC_PC_SpotOption" #现货期权
    ctypedef char TInstLifePhaseType "TThostFtdcInstLifePhaseType" #合约生命周期状态
    enum: IP_NotStart "THOST_FTDC_IP_NotStart" #未上市
    enum: IP_Started "THOST_FTDC_IP_Started" #上市
    enum: IP_Pause "THOST_FTDC_IP_Pause" #停牌
    enum: IP_Expired "THOST_FTDC_IP_Expired" #到期
    ctypedef char TDirectionType "TThostFtdcDirectionType" #买卖方向
    enum: D_Buy "THOST_FTDC_D_Buy" #买
    enum: D_Sell "THOST_FTDC_D_Sell" #卖
    ctypedef char TPositionTypeType "TThostFtdcPositionTypeType" #持仓类型
    enum: PT_Net "THOST_FTDC_PT_Net" #净持仓
    enum: PT_Gross "THOST_FTDC_PT_Gross" #综合持仓
    ctypedef char TPosiDirectionType "TThostFtdcPosiDirectionType" #持仓多空方向
    enum: PD_Net "THOST_FTDC_PD_Net" #净
    enum: PD_Long "THOST_FTDC_PD_Long" #多头
    enum: PD_Short "THOST_FTDC_PD_Short" #空头
    ctypedef char TSysSettlementStatusType "TThostFtdcSysSettlementStatusType" #系统结算状态
    enum: SS_NonActive "THOST_FTDC_SS_NonActive" #不活跃
    enum: SS_Startup "THOST_FTDC_SS_Startup" #启动
    enum: SS_Operating "THOST_FTDC_SS_Operating" #操作
    enum: SS_Settlement "THOST_FTDC_SS_Settlement" #结算
    enum: SS_SettlementFinished "THOST_FTDC_SS_SettlementFinished" #结算完成
    ctypedef char TRatioAttrType "TThostFtdcRatioAttrType" #费率属性
    enum: RA_Trade "THOST_FTDC_RA_Trade" #交易费率
    enum: RA_Settlement "THOST_FTDC_RA_Settlement" #结算费率
    ctypedef char THedgeFlagType "TThostFtdcHedgeFlagType" #投机套保标志
    enum: HF_Speculation "THOST_FTDC_HF_Speculation" #投机
    enum: HF_Arbitrage "THOST_FTDC_HF_Arbitrage" #套利
    enum: HF_Hedge "THOST_FTDC_HF_Hedge" #套保
    ctypedef char TBillHedgeFlagType "TThostFtdcBillHedgeFlagType" #投机套保标志
    enum: BHF_Speculation "THOST_FTDC_BHF_Speculation" #投机
    enum: BHF_Arbitrage "THOST_FTDC_BHF_Arbitrage" #套利
    enum: BHF_Hedge "THOST_FTDC_BHF_Hedge" #套保
    ctypedef char TClientIDTypeType "TThostFtdcClientIDTypeType" #交易编码类型
    enum: CIDT_Speculation "THOST_FTDC_CIDT_Speculation" #投机
    enum: CIDT_Arbitrage "THOST_FTDC_CIDT_Arbitrage" #套利
    enum: CIDT_Hedge "THOST_FTDC_CIDT_Hedge" #套保
    ctypedef char TOrderPriceTypeType "TThostFtdcOrderPriceTypeType" #报单价格条件
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
    enum: OPT_FiveLevelPrice "THOST_FTDC_OPT_FiveLevelPrice" #五档价
    ctypedef char TOffsetFlagType "TThostFtdcOffsetFlagType" #开平标志
    enum: OF_Open "THOST_FTDC_OF_Open" #开仓
    enum: OF_Close "THOST_FTDC_OF_Close" #平仓
    enum: OF_ForceClose "THOST_FTDC_OF_ForceClose" #强平
    enum: OF_CloseToday "THOST_FTDC_OF_CloseToday" #平今
    enum: OF_CloseYesterday "THOST_FTDC_OF_CloseYesterday" #平昨
    enum: OF_ForceOff "THOST_FTDC_OF_ForceOff" #强减
    enum: OF_LocalForceClose "THOST_FTDC_OF_LocalForceClose" #本地强平
    ctypedef char TForceCloseReasonType "TThostFtdcForceCloseReasonType" #强平原因
    enum: FCC_NotForceClose "THOST_FTDC_FCC_NotForceClose" #非强平
    enum: FCC_LackDeposit "THOST_FTDC_FCC_LackDeposit" #资金不足
    enum: FCC_ClientOverPositionLimit "THOST_FTDC_FCC_ClientOverPositionLimit" #客户超仓
    enum: FCC_MemberOverPositionLimit "THOST_FTDC_FCC_MemberOverPositionLimit" #会员超仓
    enum: FCC_NotMultiple "THOST_FTDC_FCC_NotMultiple" #持仓非整数倍
    enum: FCC_Violation "THOST_FTDC_FCC_Violation" #违规
    enum: FCC_Other "THOST_FTDC_FCC_Other" #其它
    enum: FCC_PersonDeliv "THOST_FTDC_FCC_PersonDeliv" #自然人临近交割
    ctypedef char TOrderTypeType "TThostFtdcOrderTypeType" #报单类型
    enum: ORDT_Normal "THOST_FTDC_ORDT_Normal" #正常
    enum: ORDT_DeriveFromQuote "THOST_FTDC_ORDT_DeriveFromQuote" #报价衍生
    enum: ORDT_DeriveFromCombination "THOST_FTDC_ORDT_DeriveFromCombination" #组合衍生
    enum: ORDT_Combination "THOST_FTDC_ORDT_Combination" #组合报单
    enum: ORDT_ConditionalOrder "THOST_FTDC_ORDT_ConditionalOrder" #条件单
    enum: ORDT_Swap "THOST_FTDC_ORDT_Swap" #互换单
    ctypedef char TTimeConditionType "TThostFtdcTimeConditionType" #有效期类型
    enum: TC_IOC "THOST_FTDC_TC_IOC" #立即完成，否则撤销
    enum: TC_GFS "THOST_FTDC_TC_GFS" #本节有效
    enum: TC_GFD "THOST_FTDC_TC_GFD" #当日有效
    enum: TC_GTD "THOST_FTDC_TC_GTD" #指定日期前有效
    enum: TC_GTC "THOST_FTDC_TC_GTC" #撤销前有效
    enum: TC_GFA "THOST_FTDC_TC_GFA" #集合竞价有效
    ctypedef char TVolumeConditionType "TThostFtdcVolumeConditionType" #成交量类型
    enum: VC_AV "THOST_FTDC_VC_AV" #任何数量
    enum: VC_MV "THOST_FTDC_VC_MV" #最小数量
    enum: VC_CV "THOST_FTDC_VC_CV" #全部数量
    ctypedef char TContingentConditionType "TThostFtdcContingentConditionType" #触发条件
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
    ctypedef char TActionFlagType "TThostFtdcActionFlagType" #操作标志
    enum: AF_Delete "THOST_FTDC_AF_Delete" #删除
    enum: AF_Modify "THOST_FTDC_AF_Modify" #修改
    ctypedef char TTradingRightType "TThostFtdcTradingRightType" #交易权限
    enum: TR_Allow "THOST_FTDC_TR_Allow" #可以交易
    enum: TR_CloseOnly "THOST_FTDC_TR_CloseOnly" #只能平仓
    enum: TR_Forbidden "THOST_FTDC_TR_Forbidden" #不能交易
    ctypedef char TOrderSourceType "TThostFtdcOrderSourceType" #报单来源
    enum: OSRC_Participant "THOST_FTDC_OSRC_Participant" #来自参与者
    enum: OSRC_Administrator "THOST_FTDC_OSRC_Administrator" #来自管理员
    ctypedef char TTradeTypeType "TThostFtdcTradeTypeType" #成交类型
    enum: TRDT_SplitCombination "THOST_FTDC_TRDT_SplitCombination" #组合持仓拆分为单一持仓,初始化不应包含该类型的持仓
    enum: TRDT_Common "THOST_FTDC_TRDT_Common" #普通成交
    enum: TRDT_OptionsExecution "THOST_FTDC_TRDT_OptionsExecution" #期权执行
    enum: TRDT_OTC "THOST_FTDC_TRDT_OTC" #OTC成交
    enum: TRDT_EFPDerived "THOST_FTDC_TRDT_EFPDerived" #期转现衍生成交
    enum: TRDT_CombinationDerived "THOST_FTDC_TRDT_CombinationDerived" #组合衍生成交
    ctypedef char TPriceSourceType "TThostFtdcPriceSourceType" #成交价来源
    enum: PSRC_LastPrice "THOST_FTDC_PSRC_LastPrice" #前成交价
    enum: PSRC_Buy "THOST_FTDC_PSRC_Buy" #买委托价
    enum: PSRC_Sell "THOST_FTDC_PSRC_Sell" #卖委托价
    ctypedef char TInstrumentStatusType "TThostFtdcInstrumentStatusType" #合约交易状态
    enum: IS_BeforeTrading "THOST_FTDC_IS_BeforeTrading" #开盘前
    enum: IS_NoTrading "THOST_FTDC_IS_NoTrading" #非交易
    enum: IS_Continous "THOST_FTDC_IS_Continous" #连续交易
    enum: IS_AuctionOrdering "THOST_FTDC_IS_AuctionOrdering" #集合竞价报单
    enum: IS_AuctionBalance "THOST_FTDC_IS_AuctionBalance" #集合竞价价格平衡
    enum: IS_AuctionMatch "THOST_FTDC_IS_AuctionMatch" #集合竞价撮合
    enum: IS_Closed "THOST_FTDC_IS_Closed" #收盘
    ctypedef char TInstStatusEnterReasonType "TThostFtdcInstStatusEnterReasonType" #品种进入交易状态原因
    enum: IER_Automatic "THOST_FTDC_IER_Automatic" #自动切换
    enum: IER_Manual "THOST_FTDC_IER_Manual" #手动切换
    enum: IER_Fuse "THOST_FTDC_IER_Fuse" #熔断
    ctypedef int TOrderActionRefType "TThostFtdcOrderActionRefType" #报单操作引用
    ctypedef int TInstallCountType "TThostFtdcInstallCountType" #安装数量
    ctypedef int TInstallIDType "TThostFtdcInstallIDType" #安装编号
    ctypedef int TErrorIDType "TThostFtdcErrorIDType" #错误代码
    ctypedef int TSettlementIDType "TThostFtdcSettlementIDType" #结算编号
    ctypedef int TVolumeType "TThostFtdcVolumeType" #数量
    ctypedef int TFrontIDType "TThostFtdcFrontIDType" #前置编号
    ctypedef int TSessionIDType "TThostFtdcSessionIDType" #会话编号
    ctypedef int TSequenceNoType "TThostFtdcSequenceNoType" #序号
    ctypedef int TCommandNoType "TThostFtdcCommandNoType" #DB命令序号
    ctypedef int TMillisecType "TThostFtdcMillisecType" #时间（毫秒）
    ctypedef int TVolumeMultipleType "TThostFtdcVolumeMultipleType" #合约数量乘数
    ctypedef int TTradingSegmentSNType "TThostFtdcTradingSegmentSNType" #交易阶段编号
    ctypedef int TRequestIDType "TThostFtdcRequestIDType" #请求编号
    ctypedef int TYearType "TThostFtdcYearType" #年份
    ctypedef int TMonthType "TThostFtdcMonthType" #月份
    ctypedef int TBoolType "TThostFtdcBoolType" #布尔型
    ctypedef double TPriceType "TThostFtdcPriceType" #价格
    ctypedef char[5] TCombOffsetFlagType "TThostFtdcCombOffsetFlagType" #组合开平标志
    ctypedef char[5] TCombHedgeFlagType "TThostFtdcCombHedgeFlagType" #组合投机套保标志
    ctypedef double TRatioType "TThostFtdcRatioType" #比率
    ctypedef double TMoneyType "TThostFtdcMoneyType" #资金
    ctypedef double TLargeVolumeType "TThostFtdcLargeVolumeType" #大额数量
    ctypedef short TSequenceSeriesType "TThostFtdcSequenceSeriesType" #序列系列号
    ctypedef short TCommPhaseNoType "TThostFtdcCommPhaseNoType" #通讯时段编号
    ctypedef char[2] TSequenceLabelType "TThostFtdcSequenceLabelType" #序列编号
    ctypedef double TUnderlyingMultipleType "TThostFtdcUnderlyingMultipleType" #基础商品乘数
    ctypedef int TPriorityType "TThostFtdcPriorityType" #优先级
    ctypedef char[41] TContractCodeType "TThostFtdcContractCodeType" #合同编号
    ctypedef char[51] TCityType "TThostFtdcCityType" #市
    ctypedef char[11] TIsStockType "TThostFtdcIsStockType" #是否股民
    ctypedef char[51] TChannelType "TThostFtdcChannelType" #渠道
    ctypedef char[101] TAddressType "TThostFtdcAddressType" #通讯地址
    ctypedef char[7] TZipCodeType "TThostFtdcZipCodeType" #邮政编码
    ctypedef char[41] TTelephoneType "TThostFtdcTelephoneType" #联系电话
    ctypedef char[41] TFaxType "TThostFtdcFaxType" #传真
    ctypedef char[41] TMobileType "TThostFtdcMobileType" #手机
    ctypedef char[41] TEMailType "TThostFtdcEMailType" #电子邮件
    ctypedef char[161] TMemoType "TThostFtdcMemoType" #备注
    ctypedef char[51] TCompanyCodeType "TThostFtdcCompanyCodeType" #企业代码
    ctypedef char[51] TWebsiteType "TThostFtdcWebsiteType" #网站地址
    ctypedef char[31] TTaxNoType "TThostFtdcTaxNoType" #税务登记号
    ctypedef char TBatchStatusType "TThostFtdcBatchStatusType" #处理状态
    enum: BS_NoUpload "THOST_FTDC_BS_NoUpload" #未上传
    enum: BS_Uploaded "THOST_FTDC_BS_Uploaded" #已上传
    enum: BS_Failed "THOST_FTDC_BS_Failed" #审核失败
    ctypedef char[33] TPropertyIDType "TThostFtdcPropertyIDType" #属性代码
    ctypedef char[65] TPropertyNameType "TThostFtdcPropertyNameType" #属性名称
    ctypedef char[51] TLicenseNoType "TThostFtdcLicenseNoType" #营业执照号
    ctypedef char[13] TAgentIDType "TThostFtdcAgentIDType" #经纪人代码
    ctypedef char[41] TAgentNameType "TThostFtdcAgentNameType" #经纪人名称
    ctypedef char[13] TAgentGroupIDType "TThostFtdcAgentGroupIDType" #经纪人组代码
    ctypedef char[41] TAgentGroupNameType "TThostFtdcAgentGroupNameType" #经纪人组名称
    ctypedef char TReturnStyleType "TThostFtdcReturnStyleType" #按品种返还方式
    enum: RS_All "THOST_FTDC_RS_All" #按所有品种
    enum: RS_ByProduct "THOST_FTDC_RS_ByProduct" #按品种
    ctypedef char TReturnPatternType "TThostFtdcReturnPatternType" #返还模式
    enum: RP_ByVolume "THOST_FTDC_RP_ByVolume" #按成交手数
    enum: RP_ByFeeOnHand "THOST_FTDC_RP_ByFeeOnHand" #按留存手续费
    ctypedef char TReturnLevelType "TThostFtdcReturnLevelType" #返还级别
    enum: RL_Level1 "THOST_FTDC_RL_Level1" #级别1
    enum: RL_Level2 "THOST_FTDC_RL_Level2" #级别2
    enum: RL_Level3 "THOST_FTDC_RL_Level3" #级别3
    enum: RL_Level4 "THOST_FTDC_RL_Level4" #级别4
    enum: RL_Level5 "THOST_FTDC_RL_Level5" #级别5
    enum: RL_Level6 "THOST_FTDC_RL_Level6" #级别6
    enum: RL_Level7 "THOST_FTDC_RL_Level7" #级别7
    enum: RL_Level8 "THOST_FTDC_RL_Level8" #级别8
    enum: RL_Level9 "THOST_FTDC_RL_Level9" #级别9
    ctypedef char TReturnStandardType "TThostFtdcReturnStandardType" #返还标准
    enum: RSD_ByPeriod "THOST_FTDC_RSD_ByPeriod" #分阶段返还
    enum: RSD_ByStandard "THOST_FTDC_RSD_ByStandard" #按某一标准
    ctypedef char TMortgageTypeType "TThostFtdcMortgageTypeType" #质押类型
    enum: MT_Out "THOST_FTDC_MT_Out" #质出
    enum: MT_In "THOST_FTDC_MT_In" #质入
    ctypedef char TInvestorSettlementParamIDType "TThostFtdcInvestorSettlementParamIDType" #投资者结算参数代码
    enum: ISPI_MortgageRatio "THOST_FTDC_ISPI_MortgageRatio" #质押比例
    enum: ISPI_MarginWay "THOST_FTDC_ISPI_MarginWay" #保证金算法
    enum: ISPI_BillDeposit "THOST_FTDC_ISPI_BillDeposit" #结算单结存是否包含质押
    ctypedef char TExchangeSettlementParamIDType "TThostFtdcExchangeSettlementParamIDType" #交易所结算参数代码
    enum: ESPI_MortgageRatio "THOST_FTDC_ESPI_MortgageRatio" #质押比例
    enum: ESPI_OtherFundItem "THOST_FTDC_ESPI_OtherFundItem" #分项资金导入项
    enum: ESPI_OtherFundImport "THOST_FTDC_ESPI_OtherFundImport" #分项资金入交易所出入金
    enum: ESPI_CFFEXMinPrepa "THOST_FTDC_ESPI_CFFEXMinPrepa" #中金所开户最低可用金额
    enum: ESPI_CZCESettlementType "THOST_FTDC_ESPI_CZCESettlementType" #郑商所结算方式
    enum: ESPI_ExchDelivFeeMode "THOST_FTDC_ESPI_ExchDelivFeeMode" #交易所交割手续费收取方式
    enum: ESPI_DelivFeeMode "THOST_FTDC_ESPI_DelivFeeMode" #投资者交割手续费收取方式
    enum: ESPI_CZCEComMarginType "THOST_FTDC_ESPI_CZCEComMarginType" #郑商所组合持仓保证金收取方式
    enum: ESPI_DceComMarginType "THOST_FTDC_ESPI_DceComMarginType" #大商所套利保证金是否优惠
    enum: ESPI_OptOutDisCountRate "THOST_FTDC_ESPI_OptOutDisCountRate" #虚值期权保证金优惠比率
    enum: ESPI_OptMiniGuarantee "THOST_FTDC_ESPI_OptMiniGuarantee" #最低保障系数
    ctypedef char TSystemParamIDType "TThostFtdcSystemParamIDType" #系统参数代码
    enum: SPI_InvestorIDMinLength "THOST_FTDC_SPI_InvestorIDMinLength" #投资者代码最小长度
    enum: SPI_AccountIDMinLength "THOST_FTDC_SPI_AccountIDMinLength" #投资者帐号代码最小长度
    enum: SPI_UserRightLogon "THOST_FTDC_SPI_UserRightLogon" #投资者开户默认登录权限
    enum: SPI_SettlementBillTrade "THOST_FTDC_SPI_SettlementBillTrade" #投资者交易结算单成交汇总方式
    enum: SPI_TradingCode "THOST_FTDC_SPI_TradingCode" #统一开户更新交易编码方式
    enum: SPI_CheckFund "THOST_FTDC_SPI_CheckFund" #结算是否判断存在未复核的出入金和分项资金
    enum: SPI_CommModelRight "THOST_FTDC_SPI_CommModelRight" #是否启用手续费模板数据权限
    enum: SPI_MarginModelRight "THOST_FTDC_SPI_MarginModelRight" #是否启用保证金率模板数据权限
    enum: SPI_IsStandardActive "THOST_FTDC_SPI_IsStandardActive" #是否规范用户才能激活
    enum: SPI_UploadSettlementFile "THOST_FTDC_SPI_UploadSettlementFile" #上传的交易所结算文件路径
    enum: SPI_DownloadCSRCFile "THOST_FTDC_SPI_DownloadCSRCFile" #上报保证金监控中心文件路径
    enum: SPI_SettlementBillFile "THOST_FTDC_SPI_SettlementBillFile" #生成的结算单文件路径
    enum: SPI_CSRCOthersFile "THOST_FTDC_SPI_CSRCOthersFile" #证监会文件标识
    enum: SPI_InvestorPhoto "THOST_FTDC_SPI_InvestorPhoto" #投资者照片路径
    enum: SPI_CSRCData "THOST_FTDC_SPI_CSRCData" #全结经纪公司上传文件路径
    enum: SPI_InvestorPwdModel "THOST_FTDC_SPI_InvestorPwdModel" #开户密码录入方式
    enum: SPI_CFFEXInvestorSettleFile "THOST_FTDC_SPI_CFFEXInvestorSettleFile" #投资者中金所结算文件下载路径
    enum: SPI_InvestorIDType "THOST_FTDC_SPI_InvestorIDType" #投资者代码编码方式
    enum: SPI_FreezeMaxReMain "THOST_FTDC_SPI_FreezeMaxReMain" #休眠户最高权益
    enum: SPI_IsSync "THOST_FTDC_SPI_IsSync" #手续费相关操作实时上场开关
    enum: SPI_RelieveOpenLimit "THOST_FTDC_SPI_RelieveOpenLimit" #解除开仓权限限制
    enum: SPI_IsStandardFreeze "THOST_FTDC_SPI_IsStandardFreeze" #是否规范用户才能休眠
    enum: SPI_CZCENormalProductHedge "THOST_FTDC_SPI_CZCENormalProductHedge" #郑商所是否开放所有品种套保交易
    ctypedef char TTradeParamIDType "TThostFtdcTradeParamIDType" #交易系统参数代码
    enum: TPID_EncryptionStandard "THOST_FTDC_TPID_EncryptionStandard" #系统加密算法
    enum: TPID_RiskMode "THOST_FTDC_TPID_RiskMode" #系统风险算法
    enum: TPID_RiskModeGlobal "THOST_FTDC_TPID_RiskModeGlobal" #系统风险算法是否全局 0-否 1-是
    enum: TPID_modeEncode "THOST_FTDC_TPID_modeEncode" #密码加密算法
    enum: TPID_tickMode "THOST_FTDC_TPID_tickMode" #价格小数位数参数
    enum: TPID_SingleUserSessionMaxNum "THOST_FTDC_TPID_SingleUserSessionMaxNum" #用户最大会话数
    enum: TPID_LoginFailMaxNum "THOST_FTDC_TPID_LoginFailMaxNum" #最大连续登录失败数
    enum: TPID_IsAuthForce "THOST_FTDC_TPID_IsAuthForce" #是否强制认证
    ctypedef char[256] TSettlementParamValueType "TThostFtdcSettlementParamValueType" #参数代码值
    ctypedef char[33] TCounterIDType "TThostFtdcCounterIDType" #计数器代码
    ctypedef char[41] TInvestorGroupNameType "TThostFtdcInvestorGroupNameType" #投资者分组名称
    ctypedef char[257] TBrandCodeType "TThostFtdcBrandCodeType" #牌号
    ctypedef char[257] TWarehouseType "TThostFtdcWarehouseType" #仓库
    ctypedef char[41] TProductDateType "TThostFtdcProductDateType" #产期
    ctypedef char[41] TGradeType "TThostFtdcGradeType" #等级
    ctypedef char[41] TClassifyType "TThostFtdcClassifyType" #类别
    ctypedef char[41] TPositionType "TThostFtdcPositionType" #货位
    ctypedef char[41] TYieldlyType "TThostFtdcYieldlyType" #产地
    ctypedef char[41] TWeightType "TThostFtdcWeightType" #公定重量
    ctypedef int TSubEntryFundNoType "TThostFtdcSubEntryFundNoType" #分项资金流水号
    ctypedef char TFileIDType "TThostFtdcFileIDType" #文件标识
    enum: FI_SettlementFund "THOST_FTDC_FI_SettlementFund" #资金数据
    enum: FI_Trade "THOST_FTDC_FI_Trade" #成交数据
    enum: FI_InvestorPosition "THOST_FTDC_FI_InvestorPosition" #投资者持仓数据
    enum: FI_SubEntryFund "THOST_FTDC_FI_SubEntryFund" #投资者分项资金数据
    enum: FI_CZCECombinationPos "THOST_FTDC_FI_CZCECombinationPos" #组合持仓数据
    enum: FI_CSRCData "THOST_FTDC_FI_CSRCData" #上报保证金监控中心数据
    enum: FI_CZCEClose "THOST_FTDC_FI_CZCEClose" #郑商所平仓了结数据
    enum: FI_CZCENoClose "THOST_FTDC_FI_CZCENoClose" #郑商所非平仓了结数据
    enum: FI_PositionDtl "THOST_FTDC_FI_PositionDtl" #持仓明细数据
    enum: FI_OptionStrike "THOST_FTDC_FI_OptionStrike" #期权执行文件
    enum: FI_SettlementPriceComparison "THOST_FTDC_FI_SettlementPriceComparison" #结算价比对文件
    enum: FI_NonTradePosChange "THOST_FTDC_FI_NonTradePosChange" #上期所非持仓变动明细
    ctypedef char[257] TFileNameType "TThostFtdcFileNameType" #文件名称
    ctypedef char TFileTypeType "TThostFtdcFileTypeType" #文件上传类型
    enum: FUT_Settlement "THOST_FTDC_FUT_Settlement" #结算
    enum: FUT_Check "THOST_FTDC_FUT_Check" #核对
    ctypedef char TFileFormatType "TThostFtdcFileFormatType" #文件格式
    enum: FFT_Txt "THOST_FTDC_FFT_Txt" #文本文件(.txt)
    enum: FFT_Zip "THOST_FTDC_FFT_Zip" #压缩文件(.zip)
    enum: FFT_DBF "THOST_FTDC_FFT_DBF" #DBF文件(.dbf)
    ctypedef char TFileUploadStatusType "TThostFtdcFileUploadStatusType" #文件状态
    enum: FUS_SucceedUpload "THOST_FTDC_FUS_SucceedUpload" #上传成功
    enum: FUS_FailedUpload "THOST_FTDC_FUS_FailedUpload" #上传失败
    enum: FUS_SucceedLoad "THOST_FTDC_FUS_SucceedLoad" #导入成功
    enum: FUS_PartSucceedLoad "THOST_FTDC_FUS_PartSucceedLoad" #导入部分成功
    enum: FUS_FailedLoad "THOST_FTDC_FUS_FailedLoad" #导入失败
    ctypedef char TTransferDirectionType "TThostFtdcTransferDirectionType" #移仓方向
    enum: TD_Out "THOST_FTDC_TD_Out" #移出
    enum: TD_In "THOST_FTDC_TD_In" #移入
    ctypedef char[21] TUploadModeType "TThostFtdcUploadModeType" #上传文件类型
    ctypedef char[13] TAccountIDType "TThostFtdcAccountIDType" #投资者帐号
    ctypedef char[4] TBankFlagType "TThostFtdcBankFlagType" #银行统一标识类型
    ctypedef char[41] TBankAccountType "TThostFtdcBankAccountType" #银行账户
    ctypedef char[61] TOpenNameType "TThostFtdcOpenNameType" #银行账户的开户人名称
    ctypedef char[101] TOpenBankType "TThostFtdcOpenBankType" #银行账户的开户行
    ctypedef char[101] TBankNameType "TThostFtdcBankNameType" #银行名称
    ctypedef char[257] TPublishPathType "TThostFtdcPublishPathType" #发布路径
    ctypedef char[65] TOperatorIDType "TThostFtdcOperatorIDType" #操作员代码
    ctypedef int TMonthCountType "TThostFtdcMonthCountType" #月份数量
    ctypedef char[13] TAdvanceMonthArrayType "TThostFtdcAdvanceMonthArrayType" #月份提前数组
    ctypedef char[1025] TDateExprType "TThostFtdcDateExprType" #日期表达式
    ctypedef char[41] TInstrumentIDExprType "TThostFtdcInstrumentIDExprType" #合约代码表达式
    ctypedef char[41] TInstrumentNameExprType "TThostFtdcInstrumentNameExprType" #合约名称表达式
    ctypedef char TSpecialCreateRuleType "TThostFtdcSpecialCreateRuleType" #特殊的创建规则
    enum: SC_NoSpecialRule "THOST_FTDC_SC_NoSpecialRule" #没有特殊创建规则
    enum: SC_NoSpringFestival "THOST_FTDC_SC_NoSpringFestival" #不包含春节
    ctypedef char TBasisPriceTypeType "TThostFtdcBasisPriceTypeType" #挂牌基准价类型
    enum: IPT_LastSettlement "THOST_FTDC_IPT_LastSettlement" #上一合约结算价
    enum: IPT_LaseClose "THOST_FTDC_IPT_LaseClose" #上一合约收盘价
    ctypedef char TProductLifePhaseType "TThostFtdcProductLifePhaseType" #产品生命周期状态
    enum: PLP_Active "THOST_FTDC_PLP_Active" #活跃
    enum: PLP_NonActive "THOST_FTDC_PLP_NonActive" #不活跃
    enum: PLP_Canceled "THOST_FTDC_PLP_Canceled" #注销
    ctypedef char TDeliveryModeType "TThostFtdcDeliveryModeType" #交割方式
    enum: DM_CashDeliv "THOST_FTDC_DM_CashDeliv" #现金交割
    enum: DM_CommodityDeliv "THOST_FTDC_DM_CommodityDeliv" #实物交割
    ctypedef char[33] TLogLevelType "TThostFtdcLogLevelType" #日志级别
    ctypedef char[257] TProcessNameType "TThostFtdcProcessNameType" #存储过程名称
    ctypedef char[1025] TOperationMemoType "TThostFtdcOperationMemoType" #操作摘要
    ctypedef char TFundIOTypeType "TThostFtdcFundIOTypeType" #出入金类型
    enum: FIOT_FundIO "THOST_FTDC_FIOT_FundIO" #出入金
    enum: FIOT_Transfer "THOST_FTDC_FIOT_Transfer" #银期转帐
    enum: FIOT_SwapCurrency "THOST_FTDC_FIOT_SwapCurrency" #银期换汇
    ctypedef char TFundTypeType "TThostFtdcFundTypeType" #资金类型
    enum: FT_Deposite "THOST_FTDC_FT_Deposite" #银行存款
    enum: FT_ItemFund "THOST_FTDC_FT_ItemFund" #分项资金
    enum: FT_Company "THOST_FTDC_FT_Company" #公司调整
    enum: FT_InnerTransfer "THOST_FTDC_FT_InnerTransfer" #资金内转
    ctypedef char TFundDirectionType "TThostFtdcFundDirectionType" #出入金方向
    enum: FD_In "THOST_FTDC_FD_In" #入金
    enum: FD_Out "THOST_FTDC_FD_Out" #出金
    ctypedef char TFundStatusType "TThostFtdcFundStatusType" #资金状态
    enum: FS_Record "THOST_FTDC_FS_Record" #已录入
    enum: FS_Check "THOST_FTDC_FS_Check" #已复核
    enum: FS_Charge "THOST_FTDC_FS_Charge" #已冲销
    ctypedef char[15] TBillNoType "TThostFtdcBillNoType" #票据号
    ctypedef char[33] TBillNameType "TThostFtdcBillNameType" #票据名称
    ctypedef char TPublishStatusType "TThostFtdcPublishStatusType" #发布状态
    enum: PS_None "THOST_FTDC_PS_None" #未发布
    enum: PS_Publishing "THOST_FTDC_PS_Publishing" #正在发布
    enum: PS_Published "THOST_FTDC_PS_Published" #已发布
    ctypedef char[65] TEnumValueIDType "TThostFtdcEnumValueIDType" #枚举值代码
    ctypedef char[33] TEnumValueTypeType "TThostFtdcEnumValueTypeType" #枚举值类型
    ctypedef char[65] TEnumValueLabelType "TThostFtdcEnumValueLabelType" #枚举值名称
    ctypedef char[33] TEnumValueResultType "TThostFtdcEnumValueResultType" #枚举值结果
    ctypedef char TSystemStatusType "TThostFtdcSystemStatusType" #系统状态
    enum: ES_NonActive "THOST_FTDC_ES_NonActive" #不活跃
    enum: ES_Startup "THOST_FTDC_ES_Startup" #启动
    enum: ES_Initialize "THOST_FTDC_ES_Initialize" #交易开始初始化
    enum: ES_Initialized "THOST_FTDC_ES_Initialized" #交易完成初始化
    enum: ES_Close "THOST_FTDC_ES_Close" #收市开始
    enum: ES_Closed "THOST_FTDC_ES_Closed" #收市完成
    enum: ES_Settlement "THOST_FTDC_ES_Settlement" #结算
    ctypedef char TSettlementStatusType "TThostFtdcSettlementStatusType" #结算状态
    enum: STS_Initialize "THOST_FTDC_STS_Initialize" #初始
    enum: STS_Settlementing "THOST_FTDC_STS_Settlementing" #结算中
    enum: STS_Settlemented "THOST_FTDC_STS_Settlemented" #已结算
    enum: STS_Finished "THOST_FTDC_STS_Finished" #结算完成
    ctypedef char[33] TRangeIntTypeType "TThostFtdcRangeIntTypeType" #限定值类型
    ctypedef char[33] TRangeIntFromType "TThostFtdcRangeIntFromType" #限定值下限
    ctypedef char[33] TRangeIntToType "TThostFtdcRangeIntToType" #限定值上限
    ctypedef char[25] TFunctionIDType "TThostFtdcFunctionIDType" #功能代码
    ctypedef char[257] TFunctionValueCodeType "TThostFtdcFunctionValueCodeType" #功能编码
    ctypedef char[65] TFunctionNameType "TThostFtdcFunctionNameType" #功能名称
    ctypedef char[11] TRoleIDType "TThostFtdcRoleIDType" #角色编号
    ctypedef char[41] TRoleNameType "TThostFtdcRoleNameType" #角色名称
    ctypedef char[401] TDescriptionType "TThostFtdcDescriptionType" #描述
    ctypedef char[25] TCombineIDType "TThostFtdcCombineIDType" #组合编号
    ctypedef char[25] TCombineTypeType "TThostFtdcCombineTypeType" #组合类型
    ctypedef char TInvestorTypeType "TThostFtdcInvestorTypeType" #投资者类型
    enum: CT_Person "THOST_FTDC_CT_Person" #自然人
    enum: CT_Company "THOST_FTDC_CT_Company" #法人
    enum: CT_Fund "THOST_FTDC_CT_Fund" #投资基金
    enum: CT_SpecialOrgan "THOST_FTDC_CT_SpecialOrgan" #特殊法人
    enum: CT_Asset "THOST_FTDC_CT_Asset" #资管户
    ctypedef char TBrokerTypeType "TThostFtdcBrokerTypeType" #经纪公司类型
    enum: BT_Trade "THOST_FTDC_BT_Trade" #交易会员
    enum: BT_TradeSettle "THOST_FTDC_BT_TradeSettle" #交易结算会员
    ctypedef char TRiskLevelType "TThostFtdcRiskLevelType" #风险等级
    enum: FAS_Low "THOST_FTDC_FAS_Low" #低风险客户
    enum: FAS_Normal "THOST_FTDC_FAS_Normal" #普通客户
    enum: FAS_Focus "THOST_FTDC_FAS_Focus" #关注客户
    enum: FAS_Risk "THOST_FTDC_FAS_Risk" #风险客户
    ctypedef char TFeeAcceptStyleType "TThostFtdcFeeAcceptStyleType" #手续费收取方式
    enum: FAS_ByTrade "THOST_FTDC_FAS_ByTrade" #按交易收取
    enum: FAS_ByDeliv "THOST_FTDC_FAS_ByDeliv" #按交割收取
    enum: FAS_None "THOST_FTDC_FAS_None" #不收
    enum: FAS_FixFee "THOST_FTDC_FAS_FixFee" #按指定手续费收取
    ctypedef char TPasswordTypeType "TThostFtdcPasswordTypeType" #密码类型
    enum: PWDT_Trade "THOST_FTDC_PWDT_Trade" #交易密码
    enum: PWDT_Account "THOST_FTDC_PWDT_Account" #资金密码
    ctypedef char TAlgorithmType "TThostFtdcAlgorithmType" #盈亏算法
    enum: AG_All "THOST_FTDC_AG_All" #浮盈浮亏都计算
    enum: AG_OnlyLost "THOST_FTDC_AG_OnlyLost" #浮盈不计，浮亏计
    enum: AG_OnlyGain "THOST_FTDC_AG_OnlyGain" #浮盈计，浮亏不计
    enum: AG_None "THOST_FTDC_AG_None" #浮盈浮亏都不计算
    ctypedef char TIncludeCloseProfitType "TThostFtdcIncludeCloseProfitType" #是否包含平仓盈利
    enum: ICP_Include "THOST_FTDC_ICP_Include" #包含平仓盈利
    enum: ICP_NotInclude "THOST_FTDC_ICP_NotInclude" #不包含平仓盈利
    ctypedef char TAllWithoutTradeType "TThostFtdcAllWithoutTradeType" #是否受可提比例限制
    enum: AWT_Enable "THOST_FTDC_AWT_Enable" #无仓无成交不受可提比例限制
    enum: AWT_Disable "THOST_FTDC_AWT_Disable" #受可提比例限制
    enum: AWT_NoHoldEnable "THOST_FTDC_AWT_NoHoldEnable" #无仓不受可提比例限制
    ctypedef char[31] TCommentType "TThostFtdcCommentType" #盈亏算法说明
    ctypedef char[4] TVersionType "TThostFtdcVersionType" #版本号
    ctypedef char[7] TTradeCodeType "TThostFtdcTradeCodeType" #交易代码
    ctypedef char[9] TTradeDateType "TThostFtdcTradeDateType" #交易日期
    ctypedef char[9] TTradeTimeType "TThostFtdcTradeTimeType" #交易时间
    ctypedef char[9] TTradeSerialType "TThostFtdcTradeSerialType" #发起方流水号
    ctypedef int TTradeSerialNoType "TThostFtdcTradeSerialNoType" #发起方流水号
    ctypedef char[11] TFutureIDType "TThostFtdcFutureIDType" #期货公司代码
    ctypedef char[4] TBankIDType "TThostFtdcBankIDType" #银行代码
    ctypedef char[5] TBankBrchIDType "TThostFtdcBankBrchIDType" #银行分中心代码
    ctypedef char[11] TBankBranchIDType "TThostFtdcBankBranchIDType" #分中心代码
    ctypedef char[17] TOperNoType "TThostFtdcOperNoType" #交易柜员
    ctypedef char[3] TDeviceIDType "TThostFtdcDeviceIDType" #渠道标志
    ctypedef char[7] TRecordNumType "TThostFtdcRecordNumType" #记录数
    ctypedef char[22] TFutureAccountType "TThostFtdcFutureAccountType" #期货资金账号
    ctypedef char TFuturePwdFlagType "TThostFtdcFuturePwdFlagType" #资金密码核对标志
    enum: FPWD_UnCheck "THOST_FTDC_FPWD_UnCheck" #不核对
    enum: FPWD_Check "THOST_FTDC_FPWD_Check" #核对
    ctypedef char TTransferTypeType "TThostFtdcTransferTypeType" #银期转账类型
    enum: TT_BankToFuture "THOST_FTDC_TT_BankToFuture" #银行转期货
    enum: TT_FutureToBank "THOST_FTDC_TT_FutureToBank" #期货转银行
    ctypedef char[17] TFutureAccPwdType "TThostFtdcFutureAccPwdType" #期货资金密码
    ctypedef char[4] TCurrencyCodeType "TThostFtdcCurrencyCodeType" #币种
    ctypedef char[5] TRetCodeType "TThostFtdcRetCodeType" #响应代码
    ctypedef char[129] TRetInfoType "TThostFtdcRetInfoType" #响应信息
    ctypedef char[20] TTradeAmtType "TThostFtdcTradeAmtType" #银行总余额
    ctypedef char[20] TUseAmtType "TThostFtdcUseAmtType" #银行可用余额
    ctypedef char[20] TFetchAmtType "TThostFtdcFetchAmtType" #银行可取余额
    ctypedef char TTransferValidFlagType "TThostFtdcTransferValidFlagType" #转账有效标志
    enum: TVF_Invalid "THOST_FTDC_TVF_Invalid" #无效或失败
    enum: TVF_Valid "THOST_FTDC_TVF_Valid" #有效
    enum: TVF_Reverse "THOST_FTDC_TVF_Reverse" #冲正
    ctypedef char[21] TCertCodeType "TThostFtdcCertCodeType" #证件号码
    ctypedef char TReasonType "TThostFtdcReasonType" #事由
    enum: RN_CD "THOST_FTDC_RN_CD" #错单
    enum: RN_ZT "THOST_FTDC_RN_ZT" #资金在途
    enum: RN_QT "THOST_FTDC_RN_QT" #其它
    ctypedef char[5] TFundProjectIDType "TThostFtdcFundProjectIDType" #资金项目编号
    ctypedef char TSexType "TThostFtdcSexType" #性别
    enum: SEX_None "THOST_FTDC_SEX_None" #未知
    enum: SEX_Man "THOST_FTDC_SEX_Man" #男
    enum: SEX_Woman "THOST_FTDC_SEX_Woman" #女
    ctypedef char[101] TProfessionType "TThostFtdcProfessionType" #职业
    ctypedef char[31] TNationalType "TThostFtdcNationalType" #国籍
    ctypedef char[51] TProvinceType "TThostFtdcProvinceType" #省
    ctypedef char[16] TRegionType "TThostFtdcRegionType" #区
    ctypedef char[16] TCountryType "TThostFtdcCountryType" #国家
    ctypedef char[33] TLicenseNOType "TThostFtdcLicenseNOType" #营业执照
    ctypedef char[16] TCompanyTypeType "TThostFtdcCompanyTypeType" #企业性质
    ctypedef char[1001] TBusinessScopeType "TThostFtdcBusinessScopeType" #经营范围
    ctypedef char[4] TCapitalCurrencyType "TThostFtdcCapitalCurrencyType" #注册资本币种
    ctypedef char TUserTypeType "TThostFtdcUserTypeType" #用户类型
    enum: UT_Investor "THOST_FTDC_UT_Investor" #投资者
    enum: UT_Operator "THOST_FTDC_UT_Operator" #操作员
    enum: UT_SuperUser "THOST_FTDC_UT_SuperUser" #管理员
    ctypedef char TRateTypeType "TThostFtdcRateTypeType" #费率类型
    enum: RATETYPE_MarginRate "THOST_FTDC_RATETYPE_MarginRate" #保证金率
    ctypedef char TNoteTypeType "TThostFtdcNoteTypeType" #通知类型
    enum: NOTETYPE_TradeSettleBill "THOST_FTDC_NOTETYPE_TradeSettleBill" #交易结算单
    enum: NOTETYPE_TradeSettleMonth "THOST_FTDC_NOTETYPE_TradeSettleMonth" #交易结算月报
    enum: NOTETYPE_CallMarginNotes "THOST_FTDC_NOTETYPE_CallMarginNotes" #追加保证金通知书
    enum: NOTETYPE_ForceCloseNotes "THOST_FTDC_NOTETYPE_ForceCloseNotes" #强行平仓通知书
    enum: NOTETYPE_TradeNotes "THOST_FTDC_NOTETYPE_TradeNotes" #成交通知书
    enum: NOTETYPE_DelivNotes "THOST_FTDC_NOTETYPE_DelivNotes" #交割通知书
    ctypedef char TSettlementStyleType "TThostFtdcSettlementStyleType" #结算单方式
    enum: SBS_Day "THOST_FTDC_SBS_Day" #逐日盯市
    enum: SBS_Volume "THOST_FTDC_SBS_Volume" #逐笔对冲
    ctypedef char[256] TBrokerDNSType "TThostFtdcBrokerDNSType" #域名
    ctypedef char[501] TSentenceType "TThostFtdcSentenceType" #语句
    ctypedef char TSettlementBillTypeType "TThostFtdcSettlementBillTypeType" #结算单类型
    enum: ST_Day "THOST_FTDC_ST_Day" #日报
    enum: ST_Month "THOST_FTDC_ST_Month" #月报
    ctypedef char TUserRightTypeType "TThostFtdcUserRightTypeType" #客户权限类型
    enum: URT_Logon "THOST_FTDC_URT_Logon" #登录
    enum: URT_Transfer "THOST_FTDC_URT_Transfer" #银期转帐
    enum: URT_EMail "THOST_FTDC_URT_EMail" #邮寄结算单
    enum: URT_Fax "THOST_FTDC_URT_Fax" #传真结算单
    enum: URT_ConditionOrder "THOST_FTDC_URT_ConditionOrder" #条件单
    ctypedef char TMarginPriceTypeType "TThostFtdcMarginPriceTypeType" #保证金价格类型
    enum: MPT_PreSettlementPrice "THOST_FTDC_MPT_PreSettlementPrice" #昨结算价
    enum: MPT_SettlementPrice "THOST_FTDC_MPT_SettlementPrice" #最新价
    enum: MPT_AveragePrice "THOST_FTDC_MPT_AveragePrice" #成交均价
    enum: MPT_OpenPrice "THOST_FTDC_MPT_OpenPrice" #开仓价
    ctypedef char TBillGenStatusType "TThostFtdcBillGenStatusType" #结算单生成状态
    enum: BGS_None "THOST_FTDC_BGS_None" #未生成
    enum: BGS_NoGenerated "THOST_FTDC_BGS_NoGenerated" #生成中
    enum: BGS_Generated "THOST_FTDC_BGS_Generated" #已生成
    ctypedef char TAlgoTypeType "TThostFtdcAlgoTypeType" #算法类型
    enum: AT_HandlePositionAlgo "THOST_FTDC_AT_HandlePositionAlgo" #持仓处理算法
    enum: AT_FindMarginRateAlgo "THOST_FTDC_AT_FindMarginRateAlgo" #寻找保证金率算法
    ctypedef char THandlePositionAlgoIDType "TThostFtdcHandlePositionAlgoIDType" #持仓处理算法编号
    enum: HPA_Base "THOST_FTDC_HPA_Base" #基本
    enum: HPA_DCE "THOST_FTDC_HPA_DCE" #大连商品交易所
    enum: HPA_CZCE "THOST_FTDC_HPA_CZCE" #郑州商品交易所
    ctypedef char TFindMarginRateAlgoIDType "TThostFtdcFindMarginRateAlgoIDType" #寻找保证金率算法编号
    enum: FMRA_Base "THOST_FTDC_FMRA_Base" #基本
    enum: FMRA_DCE "THOST_FTDC_FMRA_DCE" #大连商品交易所
    enum: FMRA_CZCE "THOST_FTDC_FMRA_CZCE" #郑州商品交易所
    ctypedef char THandleTradingAccountAlgoIDType "TThostFtdcHandleTradingAccountAlgoIDType" #资金处理算法编号
    enum: HTAA_Base "THOST_FTDC_HTAA_Base" #基本
    enum: HTAA_DCE "THOST_FTDC_HTAA_DCE" #大连商品交易所
    enum: HTAA_CZCE "THOST_FTDC_HTAA_CZCE" #郑州商品交易所
    ctypedef char TPersonTypeType "TThostFtdcPersonTypeType" #联系人类型
    enum: PST_Order "THOST_FTDC_PST_Order" #指定下单人
    enum: PST_Open "THOST_FTDC_PST_Open" #开户授权人
    enum: PST_Fund "THOST_FTDC_PST_Fund" #资金调拨人
    enum: PST_Settlement "THOST_FTDC_PST_Settlement" #结算单确认人
    enum: PST_Company "THOST_FTDC_PST_Company" #法人
    enum: PST_Corporation "THOST_FTDC_PST_Corporation" #法人代表
    enum: PST_LinkMan "THOST_FTDC_PST_LinkMan" #投资者联系人
    enum: PST_Ledger "THOST_FTDC_PST_Ledger" #分户管理资产负责人
    enum: PST_Trustee "THOST_FTDC_PST_Trustee" #托（保）管人
    enum: PST_TrusteeCorporation "THOST_FTDC_PST_TrusteeCorporation" #托（保）管机构法人代表
    enum: PST_TrusteeOpen "THOST_FTDC_PST_TrusteeOpen" #托（保）管机构开户授权人
    enum: PST_TrusteeContact "THOST_FTDC_PST_TrusteeContact" #托（保）管机构联系人
    enum: PST_ForeignerRefer "THOST_FTDC_PST_ForeignerRefer" #境外自然人参考证件
    enum: PST_CorporationRefer "THOST_FTDC_PST_CorporationRefer" #法人代表参考证件
    ctypedef char TQueryInvestorRangeType "TThostFtdcQueryInvestorRangeType" #查询范围
    enum: QIR_All "THOST_FTDC_QIR_All" #所有
    enum: QIR_Group "THOST_FTDC_QIR_Group" #查询分类
    enum: QIR_Single "THOST_FTDC_QIR_Single" #单一投资者
    ctypedef char TInvestorRiskStatusType "TThostFtdcInvestorRiskStatusType" #投资者风险状态
    enum: IRS_Normal "THOST_FTDC_IRS_Normal" #正常
    enum: IRS_Warn "THOST_FTDC_IRS_Warn" #警告
    enum: IRS_Call "THOST_FTDC_IRS_Call" #追保
    enum: IRS_Force "THOST_FTDC_IRS_Force" #强平
    enum: IRS_Exception "THOST_FTDC_IRS_Exception" #异常
    ctypedef int TLegIDType "TThostFtdcLegIDType" #单腿编号
    ctypedef int TLegMultipleType "TThostFtdcLegMultipleType" #单腿乘数
    ctypedef int TImplyLevelType "TThostFtdcImplyLevelType" #派生层数
    ctypedef char[33] TClearAccountType "TThostFtdcClearAccountType" #结算账户
    ctypedef char[6] TOrganNOType "TThostFtdcOrganNOType" #结算账户
    ctypedef char[6] TClearbarchIDType "TThostFtdcClearbarchIDType" #结算账户联行号
    ctypedef char TUserEventTypeType "TThostFtdcUserEventTypeType" #用户事件类型
    enum: UET_Login "THOST_FTDC_UET_Login" #登录
    enum: UET_Logout "THOST_FTDC_UET_Logout" #登出
    enum: UET_Trading "THOST_FTDC_UET_Trading" #交易成功
    enum: UET_TradingError "THOST_FTDC_UET_TradingError" #交易失败
    enum: UET_UpdatePassword "THOST_FTDC_UET_UpdatePassword" #修改密码
    enum: UET_Authenticate "THOST_FTDC_UET_Authenticate" #客户端认证
    enum: UET_Other "THOST_FTDC_UET_Other" #其他
    ctypedef char[1025] TUserEventInfoType "TThostFtdcUserEventInfoType" #用户事件信息
    ctypedef char TCloseStyleType "TThostFtdcCloseStyleType" #平仓方式
    enum: ICS_Close "THOST_FTDC_ICS_Close" #先开先平
    enum: ICS_CloseToday "THOST_FTDC_ICS_CloseToday" #先平今再平昨
    ctypedef char TStatModeType "TThostFtdcStatModeType" #统计方式
    enum: SM_Non "THOST_FTDC_SM_Non" #----
    enum: SM_Instrument "THOST_FTDC_SM_Instrument" #按合约统计
    enum: SM_Product "THOST_FTDC_SM_Product" #按产品统计
    enum: SM_Investor "THOST_FTDC_SM_Investor" #按投资者统计
    ctypedef char TParkedOrderStatusType "TThostFtdcParkedOrderStatusType" #预埋单状态
    enum: PAOS_NotSend "THOST_FTDC_PAOS_NotSend" #未发送
    enum: PAOS_Send "THOST_FTDC_PAOS_Send" #已发送
    enum: PAOS_Deleted "THOST_FTDC_PAOS_Deleted" #已删除
    ctypedef char[13] TParkedOrderIDType "TThostFtdcParkedOrderIDType" #预埋报单编号
    ctypedef char[13] TParkedOrderActionIDType "TThostFtdcParkedOrderActionIDType" #预埋撤单编号
    ctypedef char TVirDealStatusType "TThostFtdcVirDealStatusType" #处理状态
    enum: VDS_Dealing "THOST_FTDC_VDS_Dealing" #正在处理
    enum: VDS_DeaclSucceed "THOST_FTDC_VDS_DeaclSucceed" #处理成功
    ctypedef char TOrgSystemIDType "TThostFtdcOrgSystemIDType" #原有系统代码
    enum: ORGS_Standard "THOST_FTDC_ORGS_Standard" #综合交易平台
    enum: ORGS_ESunny "THOST_FTDC_ORGS_ESunny" #易盛系统
    enum: ORGS_KingStarV6 "THOST_FTDC_ORGS_KingStarV6" #金仕达V6系统
    ctypedef char TVirTradeStatusType "TThostFtdcVirTradeStatusType" #交易状态
    enum: VTS_NaturalDeal "THOST_FTDC_VTS_NaturalDeal" #正常处理中
    enum: VTS_SucceedEnd "THOST_FTDC_VTS_SucceedEnd" #成功结束
    enum: VTS_FailedEND "THOST_FTDC_VTS_FailedEND" #失败结束
    enum: VTS_Exception "THOST_FTDC_VTS_Exception" #异常中
    enum: VTS_ManualDeal "THOST_FTDC_VTS_ManualDeal" #已人工异常处理
    enum: VTS_MesException "THOST_FTDC_VTS_MesException" #通讯异常 ，请人工处理
    enum: VTS_SysException "THOST_FTDC_VTS_SysException" #系统出错，请人工处理
    ctypedef char TVirBankAccTypeType "TThostFtdcVirBankAccTypeType" #银行帐户类型
    enum: VBAT_BankBook "THOST_FTDC_VBAT_BankBook" #存折
    enum: VBAT_BankCard "THOST_FTDC_VBAT_BankCard" #储蓄卡
    enum: VBAT_CreditCard "THOST_FTDC_VBAT_CreditCard" #信用卡
    ctypedef char TVirementStatusType "TThostFtdcVirementStatusType" #银行帐户类型
    enum: VMS_Natural "THOST_FTDC_VMS_Natural" #正常
    enum: VMS_Canceled "THOST_FTDC_VMS_Canceled" #销户
    ctypedef char TVirementAvailAbilityType "TThostFtdcVirementAvailAbilityType" #有效标志
    enum: VAA_NoAvailAbility "THOST_FTDC_VAA_NoAvailAbility" #未确认
    enum: VAA_AvailAbility "THOST_FTDC_VAA_AvailAbility" #有效
    enum: VAA_Repeal "THOST_FTDC_VAA_Repeal" #冲正
    ctypedef char[7] TVirementTradeCodeType "TThostFtdcVirementTradeCodeType" #交易代码
    enum: VTC_BankBankToFuture "THOST_FTDC_VTC_BankBankToFuture" #银行发起银行资金转期货
    enum: VTC_BankFutureToBank "THOST_FTDC_VTC_BankFutureToBank" #银行发起期货资金转银行
    enum: VTC_FutureBankToFuture "THOST_FTDC_VTC_FutureBankToFuture" #期货发起银行资金转期货
    enum: VTC_FutureFutureToBank "THOST_FTDC_VTC_FutureFutureToBank" #期货发起期货资金转银行
    ctypedef char[41] TPhotoTypeNameType "TThostFtdcPhotoTypeNameType" #影像类型名称
    ctypedef char[5] TPhotoTypeIDType "TThostFtdcPhotoTypeIDType" #影像类型代码
    ctypedef char[161] TPhotoNameType "TThostFtdcPhotoNameType" #影像名称
    ctypedef int TTopicIDType "TThostFtdcTopicIDType" #主题代码
    ctypedef char[3] TReportTypeIDType "TThostFtdcReportTypeIDType" #交易报告类型标识
    ctypedef char[5] TCharacterIDType "TThostFtdcCharacterIDType" #交易特征代码
    ctypedef char[21] TAMLParamIDType "TThostFtdcAMLParamIDType" #参数代码
    ctypedef char[3] TAMLInvestorTypeType "TThostFtdcAMLInvestorTypeType" #投资者类型
    ctypedef char[3] TAMLIdCardTypeType "TThostFtdcAMLIdCardTypeType" #证件类型
    ctypedef char[3] TAMLTradeDirectType "TThostFtdcAMLTradeDirectType" #资金进出方向
    ctypedef char[3] TAMLTradeModelType "TThostFtdcAMLTradeModelType" #资金进出方式
    ctypedef char[21] TAMLParamIDType "TThostFtdcAMLParamIDType" #参数代码
    ctypedef double TAMLOpParamValueType "TThostFtdcAMLOpParamValueType" #业务参数代码值
    ctypedef char[81] TAMLCustomerCardTypeType "TThostFtdcAMLCustomerCardTypeType" #客户身份证件/证明文件类型
    ctypedef char[65] TAMLInstitutionNameType "TThostFtdcAMLInstitutionNameType" #金融机构网点名称
    ctypedef char[7] TAMLDistrictIDType "TThostFtdcAMLDistrictIDType" #金融机构网点所在地区行政区划代码
    ctypedef char[3] TAMLRelationShipType "TThostFtdcAMLRelationShipType" #金融机构网点与大额交易的关系
    ctypedef char[3] TAMLInstitutionTypeType "TThostFtdcAMLInstitutionTypeType" #金融机构网点代码类型
    ctypedef char[13] TAMLInstitutionIDType "TThostFtdcAMLInstitutionIDType" #金融机构网点代码
    ctypedef char[5] TAMLAccountTypeType "TThostFtdcAMLAccountTypeType" #账户类型
    ctypedef char[7] TAMLTradingTypeType "TThostFtdcAMLTradingTypeType" #交易方式
    ctypedef char[7] TAMLTransactClassType "TThostFtdcAMLTransactClassType" #涉外收支交易分类与代码
    ctypedef char[3] TAMLCapitalIOType "TThostFtdcAMLCapitalIOType" #资金收付标识
    ctypedef char[10] TAMLSiteType "TThostFtdcAMLSiteType" #交易地点
    ctypedef char[129] TAMLCapitalPurposeType "TThostFtdcAMLCapitalPurposeType" #资金用途
    ctypedef char[2] TAMLReportTypeType "TThostFtdcAMLReportTypeType" #报文类型
    ctypedef char[5] TAMLSerialNoType "TThostFtdcAMLSerialNoType" #编号
    ctypedef char[2] TAMLStatusType "TThostFtdcAMLStatusType" #状态
    ctypedef char TAMLGenStatusType "TThostFtdcAMLGenStatusType" #Aml生成方式
    enum: GEN_Program "THOST_FTDC_GEN_Program" #程序生成
    enum: GEN_HandWork "THOST_FTDC_GEN_HandWork" #人工生成
    ctypedef char[65] TAMLSeqCodeType "TThostFtdcAMLSeqCodeType" #业务标识号
    ctypedef char[257] TAMLFileNameType "TThostFtdcAMLFileNameType" #AML文件名
    ctypedef double TAMLMoneyType "TThostFtdcAMLMoneyType" #反洗钱资金
    ctypedef int TAMLFileAmountType "TThostFtdcAMLFileAmountType" #反洗钱资金
    ctypedef char[21] TCFMMCKeyType "TThostFtdcCFMMCKeyType" #密钥类型(保证金监管)
    ctypedef char[21] TCFMMCTokenType "TThostFtdcCFMMCTokenType" #令牌类型(保证金监管)
    ctypedef char TCFMMCKeyKindType "TThostFtdcCFMMCKeyKindType" #动态密钥类别(保证金监管)
    enum: CFMMCKK_REQUEST "THOST_FTDC_CFMMCKK_REQUEST" #主动请求更新
    enum: CFMMCKK_AUTO "THOST_FTDC_CFMMCKK_AUTO" #CFMMC自动更新
    enum: CFMMCKK_MANUAL "THOST_FTDC_CFMMCKK_MANUAL" #CFMMC手动更新
    ctypedef char[81] TAMLReportNameType "TThostFtdcAMLReportNameType" #报文名称
    ctypedef char[51] TIndividualNameType "TThostFtdcIndividualNameType" #个人姓名
    ctypedef char[4] TCurrencyIDType "TThostFtdcCurrencyIDType" #币种代码
    ctypedef char[36] TCustNumberType "TThostFtdcCustNumberType" #客户编号
    ctypedef char[36] TOrganCodeType "TThostFtdcOrganCodeType" #机构编码
    ctypedef char[71] TOrganNameType "TThostFtdcOrganNameType" #机构名称
    ctypedef char[12] TSuperOrganCodeType "TThostFtdcSuperOrganCodeType" #上级机构编码,即期货公司总部、银行总行
    ctypedef char[31] TSubBranchIDType "TThostFtdcSubBranchIDType" #分支机构
    ctypedef char[71] TSubBranchNameType "TThostFtdcSubBranchNameType" #分支机构名称
    ctypedef char[31] TBranchNetCodeType "TThostFtdcBranchNetCodeType" #机构网点号
    ctypedef char[71] TBranchNetNameType "TThostFtdcBranchNetNameType" #机构网点名称
    ctypedef char[2] TOrganFlagType "TThostFtdcOrganFlagType" #机构标识
    ctypedef char[33] TBankCodingForFutureType "TThostFtdcBankCodingForFutureType" #银行对期货公司的编码
    ctypedef char[7] TBankReturnCodeType "TThostFtdcBankReturnCodeType" #银行对返回码的定义
    ctypedef char[5] TPlateReturnCodeType "TThostFtdcPlateReturnCodeType" #银期转帐平台对返回码的定义
    ctypedef char[31] TBankSubBranchIDType "TThostFtdcBankSubBranchIDType" #银行分支机构编码
    ctypedef char[31] TFutureBranchIDType "TThostFtdcFutureBranchIDType" #期货分支机构编码
    ctypedef char[7] TReturnCodeType "TThostFtdcReturnCodeType" #返回代码
    ctypedef char[17] TOperatorCodeType "TThostFtdcOperatorCodeType" #操作员
    ctypedef char[6] TClearDepIDType "TThostFtdcClearDepIDType" #机构结算帐户机构号
    ctypedef char[6] TClearBrchIDType "TThostFtdcClearBrchIDType" #机构结算帐户联行号
    ctypedef char[71] TClearNameType "TThostFtdcClearNameType" #机构结算帐户名称
    ctypedef char[71] TBankAccountNameType "TThostFtdcBankAccountNameType" #银行帐户名称
    ctypedef char[6] TInvDepIDType "TThostFtdcInvDepIDType" #机构投资人账号机构号
    ctypedef char[6] TInvBrchIDType "TThostFtdcInvBrchIDType" #机构投资人联行号
    ctypedef char[36] TMessageFormatVersionType "TThostFtdcMessageFormatVersionType" #信息格式版本
    ctypedef char[36] TDigestType "TThostFtdcDigestType" #摘要
    ctypedef char[129] TAuthenticDataType "TThostFtdcAuthenticDataType" #认证数据
    ctypedef char[129] TPasswordKeyType "TThostFtdcPasswordKeyType" #密钥
    ctypedef char[129] TFutureAccountNameType "TThostFtdcFutureAccountNameType" #期货帐户名称
    ctypedef char[21] TMobilePhoneType "TThostFtdcMobilePhoneType" #手机
    ctypedef char[129] TFutureMainKeyType "TThostFtdcFutureMainKeyType" #期货公司主密钥
    ctypedef char[129] TFutureWorkKeyType "TThostFtdcFutureWorkKeyType" #期货公司工作密钥
    ctypedef char[129] TFutureTransKeyType "TThostFtdcFutureTransKeyType" #期货公司传输密钥
    ctypedef char[129] TBankMainKeyType "TThostFtdcBankMainKeyType" #银行主密钥
    ctypedef char[129] TBankWorkKeyType "TThostFtdcBankWorkKeyType" #银行工作密钥
    ctypedef char[129] TBankTransKeyType "TThostFtdcBankTransKeyType" #银行传输密钥
    ctypedef char[129] TBankServerDescriptionType "TThostFtdcBankServerDescriptionType" #银行服务器描述信息
    ctypedef char[129] TAddInfoType "TThostFtdcAddInfoType" #附加信息
    ctypedef char[129] TDescrInfoForReturnCodeType "TThostFtdcDescrInfoForReturnCodeType" #返回码描述
    ctypedef char[21] TCountryCodeType "TThostFtdcCountryCodeType" #国家代码
    ctypedef int TSerialType "TThostFtdcSerialType" #流水号
    ctypedef int TPlateSerialType "TThostFtdcPlateSerialType" #平台流水号
    ctypedef char[13] TBankSerialType "TThostFtdcBankSerialType" #银行流水号
    ctypedef int TCorrectSerialType "TThostFtdcCorrectSerialType" #被冲正交易流水号
    ctypedef int TFutureSerialType "TThostFtdcFutureSerialType" #期货公司流水号
    ctypedef int TApplicationIDType "TThostFtdcApplicationIDType" #应用标识
    ctypedef int TBankProxyIDType "TThostFtdcBankProxyIDType" #银行代理标识
    ctypedef int TFBTCoreIDType "TThostFtdcFBTCoreIDType" #银期转帐核心系统标识
    ctypedef int TServerPortType "TThostFtdcServerPortType" #服务端口号
    ctypedef int TRepealedTimesType "TThostFtdcRepealedTimesType" #已经冲正次数
    ctypedef int TRepealTimeIntervalType "TThostFtdcRepealTimeIntervalType" #冲正时间间隔
    ctypedef int TTotalTimesType "TThostFtdcTotalTimesType" #每日累计转帐次数
    ctypedef int TFBTRequestIDType "TThostFtdcFBTRequestIDType" #请求ID
    ctypedef int TTIDType "TThostFtdcTIDType" #交易ID
    ctypedef double TTradeAmountType "TThostFtdcTradeAmountType" #交易金额（元）
    ctypedef double TCustFeeType "TThostFtdcCustFeeType" #应收客户费用（元）
    ctypedef double TFutureFeeType "TThostFtdcFutureFeeType" #应收期货公司费用（元）
    ctypedef double TSingleMaxAmtType "TThostFtdcSingleMaxAmtType" #单笔最高限额
    ctypedef double TSingleMinAmtType "TThostFtdcSingleMinAmtType" #单笔最低限额
    ctypedef double TTotalAmtType "TThostFtdcTotalAmtType" #每日累计转帐额度
    ctypedef char TCertificationTypeType "TThostFtdcCertificationTypeType" #证件类型
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
    ctypedef char TFileBusinessCodeType "TThostFtdcFileBusinessCodeType" #文件业务功能
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
    ctypedef char TCashExchangeCodeType "TThostFtdcCashExchangeCodeType" #汇钞标志
    enum: CEC_Exchange "THOST_FTDC_CEC_Exchange" #汇
    enum: CEC_Cash "THOST_FTDC_CEC_Cash" #钞
    ctypedef char TYesNoIndicatorType "TThostFtdcYesNoIndicatorType" #是或否标识
    enum: YNI_Yes "THOST_FTDC_YNI_Yes" #是
    enum: YNI_No "THOST_FTDC_YNI_No" #否
    ctypedef char TBanlanceTypeType "TThostFtdcBanlanceTypeType" #余额类型
    enum: BLT_CurrentMoney "THOST_FTDC_BLT_CurrentMoney" #当前余额
    enum: BLT_UsableMoney "THOST_FTDC_BLT_UsableMoney" #可用余额
    enum: BLT_FetchableMoney "THOST_FTDC_BLT_FetchableMoney" #可取余额
    enum: BLT_FreezeMoney "THOST_FTDC_BLT_FreezeMoney" #冻结余额
    ctypedef char TGenderType "TThostFtdcGenderType" #性别
    enum: GD_Unknown "THOST_FTDC_GD_Unknown" #未知状态
    enum: GD_Male "THOST_FTDC_GD_Male" #男
    enum: GD_Female "THOST_FTDC_GD_Female" #女
    ctypedef char TFeePayFlagType "TThostFtdcFeePayFlagType" #费用支付标志
    enum: FPF_BEN "THOST_FTDC_FPF_BEN" #由受益方支付费用
    enum: FPF_OUR "THOST_FTDC_FPF_OUR" #由发送方支付费用
    enum: FPF_SHA "THOST_FTDC_FPF_SHA" #由发送方支付发起的费用，受益方支付接受的费用
    ctypedef char TPassWordKeyTypeType "TThostFtdcPassWordKeyTypeType" #密钥类型
    enum: PWKT_ExchangeKey "THOST_FTDC_PWKT_ExchangeKey" #交换密钥
    enum: PWKT_PassWordKey "THOST_FTDC_PWKT_PassWordKey" #密码密钥
    enum: PWKT_MACKey "THOST_FTDC_PWKT_MACKey" #MAC密钥
    enum: PWKT_MessageKey "THOST_FTDC_PWKT_MessageKey" #报文密钥
    ctypedef char TFBTPassWordTypeType "TThostFtdcFBTPassWordTypeType" #密码类型
    enum: PWT_Query "THOST_FTDC_PWT_Query" #查询
    enum: PWT_Fetch "THOST_FTDC_PWT_Fetch" #取款
    enum: PWT_Transfer "THOST_FTDC_PWT_Transfer" #转帐
    enum: PWT_Trade "THOST_FTDC_PWT_Trade" #交易
    ctypedef char TFBTEncryModeType "TThostFtdcFBTEncryModeType" #加密方式
    enum: EM_NoEncry "THOST_FTDC_EM_NoEncry" #不加密
    enum: EM_DES "THOST_FTDC_EM_DES" #DES
    enum: EM_3DES "THOST_FTDC_EM_3DES" #3DES
    ctypedef char TBankRepealFlagType "TThostFtdcBankRepealFlagType" #银行冲正标志
    enum: BRF_BankNotNeedRepeal "THOST_FTDC_BRF_BankNotNeedRepeal" #银行无需自动冲正
    enum: BRF_BankWaitingRepeal "THOST_FTDC_BRF_BankWaitingRepeal" #银行待自动冲正
    enum: BRF_BankBeenRepealed "THOST_FTDC_BRF_BankBeenRepealed" #银行已自动冲正
    ctypedef char TBrokerRepealFlagType "TThostFtdcBrokerRepealFlagType" #期商冲正标志
    enum: BRORF_BrokerNotNeedRepeal "THOST_FTDC_BRORF_BrokerNotNeedRepeal" #期商无需自动冲正
    enum: BRORF_BrokerWaitingRepeal "THOST_FTDC_BRORF_BrokerWaitingRepeal" #期商待自动冲正
    enum: BRORF_BrokerBeenRepealed "THOST_FTDC_BRORF_BrokerBeenRepealed" #期商已自动冲正
    ctypedef char TInstitutionTypeType "TThostFtdcInstitutionTypeType" #机构类别
    enum: TS_Bank "THOST_FTDC_TS_Bank" #银行
    enum: TS_Future "THOST_FTDC_TS_Future" #期商
    enum: TS_Store "THOST_FTDC_TS_Store" #券商
    ctypedef char TLastFragmentType "TThostFtdcLastFragmentType" #最后分片标志
    enum: LF_Yes "THOST_FTDC_LF_Yes" #是最后分片
    enum: LF_No "THOST_FTDC_LF_No" #不是最后分片
    ctypedef char TBankAccStatusType "TThostFtdcBankAccStatusType" #银行账户状态
    enum: BAS_Normal "THOST_FTDC_BAS_Normal" #正常
    enum: BAS_Freeze "THOST_FTDC_BAS_Freeze" #冻结
    enum: BAS_ReportLoss "THOST_FTDC_BAS_ReportLoss" #挂失
    ctypedef char TMoneyAccountStatusType "TThostFtdcMoneyAccountStatusType" #资金账户状态
    enum: MAS_Normal "THOST_FTDC_MAS_Normal" #正常
    enum: MAS_Cancel "THOST_FTDC_MAS_Cancel" #销户
    ctypedef char TManageStatusType "TThostFtdcManageStatusType" #存管状态
    enum: MSS_Point "THOST_FTDC_MSS_Point" #指定存管
    enum: MSS_PrePoint "THOST_FTDC_MSS_PrePoint" #预指定
    enum: MSS_CancelPoint "THOST_FTDC_MSS_CancelPoint" #撤销指定
    ctypedef char TSystemTypeType "TThostFtdcSystemTypeType" #应用系统类型
    enum: SYT_FutureBankTransfer "THOST_FTDC_SYT_FutureBankTransfer" #银期转帐
    enum: SYT_StockBankTransfer "THOST_FTDC_SYT_StockBankTransfer" #银证转帐
    enum: SYT_TheThirdPartStore "THOST_FTDC_SYT_TheThirdPartStore" #第三方存管
    ctypedef char TTxnEndFlagType "TThostFtdcTxnEndFlagType" #银期转帐划转结果标志
    enum: TEF_NormalProcessing "THOST_FTDC_TEF_NormalProcessing" #正常处理中
    enum: TEF_Success "THOST_FTDC_TEF_Success" #成功结束
    enum: TEF_Failed "THOST_FTDC_TEF_Failed" #失败结束
    enum: TEF_Abnormal "THOST_FTDC_TEF_Abnormal" #异常中
    enum: TEF_ManualProcessedForException "THOST_FTDC_TEF_ManualProcessedForException" #已人工异常处理
    enum: TEF_CommuFailedNeedManualProcess "THOST_FTDC_TEF_CommuFailedNeedManualProcess" #通讯异常 ，请人工处理
    enum: TEF_SysErrorNeedManualProcess "THOST_FTDC_TEF_SysErrorNeedManualProcess" #系统出错，请人工处理
    ctypedef char TProcessStatusType "TThostFtdcProcessStatusType" #银期转帐服务处理状态
    enum: PSS_NotProcess "THOST_FTDC_PSS_NotProcess" #未处理
    enum: PSS_StartProcess "THOST_FTDC_PSS_StartProcess" #开始处理
    enum: PSS_Finished "THOST_FTDC_PSS_Finished" #处理完成
    ctypedef char TCustTypeType "TThostFtdcCustTypeType" #客户类型
    enum: CUSTT_Person "THOST_FTDC_CUSTT_Person" #自然人
    enum: CUSTT_Institution "THOST_FTDC_CUSTT_Institution" #机构户
    ctypedef char TFBTTransferDirectionType "TThostFtdcFBTTransferDirectionType" #银期转帐方向
    enum: FBTTD_FromBankToFuture "THOST_FTDC_FBTTD_FromBankToFuture" #入金，银行转期货
    enum: FBTTD_FromFutureToBank "THOST_FTDC_FBTTD_FromFutureToBank" #出金，期货转银行
    ctypedef char TOpenOrDestroyType "TThostFtdcOpenOrDestroyType" #开销户类别
    enum: OOD_Open "THOST_FTDC_OOD_Open" #开户
    enum: OOD_Destroy "THOST_FTDC_OOD_Destroy" #销户
    ctypedef char TAvailabilityFlagType "TThostFtdcAvailabilityFlagType" #有效标志
    enum: AVAF_Invalid "THOST_FTDC_AVAF_Invalid" #未确认
    enum: AVAF_Valid "THOST_FTDC_AVAF_Valid" #有效
    enum: AVAF_Repeal "THOST_FTDC_AVAF_Repeal" #冲正
    ctypedef char TOrganTypeType "TThostFtdcOrganTypeType" #机构类型
    enum: OT_Bank "THOST_FTDC_OT_Bank" #银行代理
    enum: OT_Future "THOST_FTDC_OT_Future" #交易前置
    enum: OT_PlateForm "THOST_FTDC_OT_PlateForm" #银期转帐平台管理
    ctypedef char TOrganLevelType "TThostFtdcOrganLevelType" #机构级别
    enum: OL_HeadQuarters "THOST_FTDC_OL_HeadQuarters" #银行总行或期商总部
    enum: OL_Branch "THOST_FTDC_OL_Branch" #银行分中心或期货公司营业部
    ctypedef char TProtocalIDType "TThostFtdcProtocalIDType" #协议类型
    enum: PID_FutureProtocal "THOST_FTDC_PID_FutureProtocal" #期商协议
    enum: PID_ICBCProtocal "THOST_FTDC_PID_ICBCProtocal" #工行协议
    enum: PID_ABCProtocal "THOST_FTDC_PID_ABCProtocal" #农行协议
    enum: PID_CBCProtocal "THOST_FTDC_PID_CBCProtocal" #中国银行协议
    enum: PID_CCBProtocal "THOST_FTDC_PID_CCBProtocal" #建行协议
    enum: PID_BOCOMProtocal "THOST_FTDC_PID_BOCOMProtocal" #交行协议
    enum: PID_FBTPlateFormProtocal "THOST_FTDC_PID_FBTPlateFormProtocal" #银期转帐平台协议
    ctypedef char TConnectModeType "TThostFtdcConnectModeType" #套接字连接方式
    enum: CM_ShortConnect "THOST_FTDC_CM_ShortConnect" #短连接
    enum: CM_LongConnect "THOST_FTDC_CM_LongConnect" #长连接
    ctypedef char TSyncModeType "TThostFtdcSyncModeType" #套接字通信方式
    enum: SRM_ASync "THOST_FTDC_SRM_ASync" #异步
    enum: SRM_Sync "THOST_FTDC_SRM_Sync" #同步
    ctypedef char TBankAccTypeType "TThostFtdcBankAccTypeType" #银行帐号类型
    enum: BAT_BankBook "THOST_FTDC_BAT_BankBook" #银行存折
    enum: BAT_SavingCard "THOST_FTDC_BAT_SavingCard" #储蓄卡
    enum: BAT_CreditCard "THOST_FTDC_BAT_CreditCard" #信用卡
    ctypedef char TFutureAccTypeType "TThostFtdcFutureAccTypeType" #期货公司帐号类型
    enum: FAT_BankBook "THOST_FTDC_FAT_BankBook" #银行存折
    enum: FAT_SavingCard "THOST_FTDC_FAT_SavingCard" #储蓄卡
    enum: FAT_CreditCard "THOST_FTDC_FAT_CreditCard" #信用卡
    ctypedef char TOrganStatusType "TThostFtdcOrganStatusType" #接入机构状态
    enum: OS_Ready "THOST_FTDC_OS_Ready" #启用
    enum: OS_CheckIn "THOST_FTDC_OS_CheckIn" #签到
    enum: OS_CheckOut "THOST_FTDC_OS_CheckOut" #签退
    enum: OS_CheckFileArrived "THOST_FTDC_OS_CheckFileArrived" #对帐文件到达
    enum: OS_CheckDetail "THOST_FTDC_OS_CheckDetail" #对帐
    enum: OS_DayEndClean "THOST_FTDC_OS_DayEndClean" #日终清理
    enum: OS_Invalid "THOST_FTDC_OS_Invalid" #注销
    ctypedef char TCCBFeeModeType "TThostFtdcCCBFeeModeType" #建行收费模式
    enum: CCBFM_ByAmount "THOST_FTDC_CCBFM_ByAmount" #按金额扣收
    enum: CCBFM_ByMonth "THOST_FTDC_CCBFM_ByMonth" #按月扣收
    ctypedef char TCommApiTypeType "TThostFtdcCommApiTypeType" #通讯API类型
    enum: CAPIT_Client "THOST_FTDC_CAPIT_Client" #客户端
    enum: CAPIT_Server "THOST_FTDC_CAPIT_Server" #服务端
    enum: CAPIT_UserApi "THOST_FTDC_CAPIT_UserApi" #交易系统的UserApi
    ctypedef int TServiceIDType "TThostFtdcServiceIDType" #服务编号
    ctypedef int TServiceLineNoType "TThostFtdcServiceLineNoType" #服务线路编号
    ctypedef char[61] TServiceNameType "TThostFtdcServiceNameType" #服务名
    ctypedef char TLinkStatusType "TThostFtdcLinkStatusType" #连接状态
    enum: LS_Connected "THOST_FTDC_LS_Connected" #已经连接
    enum: LS_Disconnected "THOST_FTDC_LS_Disconnected" #没有连接
    ctypedef int TCommApiPointerType "TThostFtdcCommApiPointerType" #通讯API指针
    ctypedef char TPwdFlagType "TThostFtdcPwdFlagType" #密码核对标志
    enum: BPWDF_NoCheck "THOST_FTDC_BPWDF_NoCheck" #不核对
    enum: BPWDF_BlankCheck "THOST_FTDC_BPWDF_BlankCheck" #明文核对
    enum: BPWDF_EncryptCheck "THOST_FTDC_BPWDF_EncryptCheck" #密文核对
    ctypedef char TSecuAccTypeType "TThostFtdcSecuAccTypeType" #期货帐号类型
    enum: SAT_AccountID "THOST_FTDC_SAT_AccountID" #资金帐号
    enum: SAT_CardID "THOST_FTDC_SAT_CardID" #资金卡号
    enum: SAT_SHStockholderID "THOST_FTDC_SAT_SHStockholderID" #上海股东帐号
    enum: SAT_SZStockholderID "THOST_FTDC_SAT_SZStockholderID" #深圳股东帐号
    ctypedef char TTransferStatusType "TThostFtdcTransferStatusType" #转账交易状态
    enum: TRFS_Normal "THOST_FTDC_TRFS_Normal" #正常
    enum: TRFS_Repealed "THOST_FTDC_TRFS_Repealed" #被冲正
    ctypedef char TSponsorTypeType "TThostFtdcSponsorTypeType" #发起方
    enum: SPTYPE_Broker "THOST_FTDC_SPTYPE_Broker" #期商
    enum: SPTYPE_Bank "THOST_FTDC_SPTYPE_Bank" #银行
    ctypedef char TReqRspTypeType "TThostFtdcReqRspTypeType" #请求响应类别
    enum: REQRSP_Request "THOST_FTDC_REQRSP_Request" #请求
    enum: REQRSP_Response "THOST_FTDC_REQRSP_Response" #响应
    ctypedef char TFBTUserEventTypeType "TThostFtdcFBTUserEventTypeType" #银期转帐用户事件类型
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
    ctypedef char[21] TBankIDByBankType "TThostFtdcBankIDByBankType" #银行自己的编码
    ctypedef char[4] TBankOperNoType "TThostFtdcBankOperNoType" #银行操作员号
    ctypedef char[21] TBankCustNoType "TThostFtdcBankCustNoType" #银行客户号
    ctypedef int TDBOPSeqNoType "TThostFtdcDBOPSeqNoType" #递增的序列号
    ctypedef char[61] TTableNameType "TThostFtdcTableNameType" #FBT表名
    ctypedef char[201] TPKNameType "TThostFtdcPKNameType" #FBT表操作主键名
    ctypedef char[501] TPKValueType "TThostFtdcPKValueType" #FBT表操作主键值
    ctypedef char TDBOperationType "TThostFtdcDBOperationType" #记录操作类型
    enum: DBOP_Insert "THOST_FTDC_DBOP_Insert" #插入
    enum: DBOP_Update "THOST_FTDC_DBOP_Update" #更新
    enum: DBOP_Delete "THOST_FTDC_DBOP_Delete" #删除
    ctypedef char TSyncFlagType "TThostFtdcSyncFlagType" #同步标记
    enum: SYNF_Yes "THOST_FTDC_SYNF_Yes" #已同步
    enum: SYNF_No "THOST_FTDC_SYNF_No" #未同步
    ctypedef char[4] TTargetIDType "TThostFtdcTargetIDType" #同步目标编号
    ctypedef char TSyncTypeType "TThostFtdcSyncTypeType" #同步类型
    enum: SYNT_OneOffSync "THOST_FTDC_SYNT_OneOffSync" #一次同步
    enum: SYNT_TimerSync "THOST_FTDC_SYNT_TimerSync" #定时同步
    enum: SYNT_TimerFullSync "THOST_FTDC_SYNT_TimerFullSync" #定时完全同步
    ctypedef char[7] TFBETimeType "TThostFtdcFBETimeType" #各种换汇时间
    ctypedef char[13] TFBEBankNoType "TThostFtdcFBEBankNoType" #换汇银行行号
    ctypedef char[13] TFBECertNoType "TThostFtdcFBECertNoType" #换汇凭证号
    ctypedef char TExDirectionType "TThostFtdcExDirectionType" #换汇方向
    enum: FBEDIR_Settlement "THOST_FTDC_FBEDIR_Settlement" #结汇
    enum: FBEDIR_Sale "THOST_FTDC_FBEDIR_Sale" #售汇
    ctypedef char[33] TFBEBankAccountType "TThostFtdcFBEBankAccountType" #换汇银行账户
    ctypedef char[61] TFBEBankAccountNameType "TThostFtdcFBEBankAccountNameType" #换汇银行账户名
    ctypedef double TFBEAmtType "TThostFtdcFBEAmtType" #各种换汇金额
    ctypedef char[3] TFBEBusinessTypeType "TThostFtdcFBEBusinessTypeType" #换汇业务类型
    ctypedef char[61] TFBEPostScriptType "TThostFtdcFBEPostScriptType" #换汇附言
    ctypedef char[71] TFBERemarkType "TThostFtdcFBERemarkType" #换汇备注
    ctypedef double TExRateType "TThostFtdcExRateType" #换汇汇率
    ctypedef char TFBEResultFlagType "TThostFtdcFBEResultFlagType" #换汇成功标志
    enum: FBERES_Success "THOST_FTDC_FBERES_Success" #成功
    enum: FBERES_InsufficientBalance "THOST_FTDC_FBERES_InsufficientBalance" #账户余额不足
    enum: FBERES_UnknownTrading "THOST_FTDC_FBERES_UnknownTrading" #交易结果未知
    enum: FBERES_Fail "THOST_FTDC_FBERES_Fail" #失败
    ctypedef char[61] TFBERtnMsgType "TThostFtdcFBERtnMsgType" #换汇返回信息
    ctypedef char[61] TFBEExtendMsgType "TThostFtdcFBEExtendMsgType" #换汇扩展信息
    ctypedef char[31] TFBEBusinessSerialType "TThostFtdcFBEBusinessSerialType" #换汇记账流水号
    ctypedef char[21] TFBESystemSerialType "TThostFtdcFBESystemSerialType" #换汇流水号
    ctypedef int TFBETotalExCntType "TThostFtdcFBETotalExCntType" #换汇交易总笔数
    ctypedef char TFBEExchStatusType "TThostFtdcFBEExchStatusType" #换汇交易状态
    enum: FBEES_Normal "THOST_FTDC_FBEES_Normal" #正常
    enum: FBEES_ReExchange "THOST_FTDC_FBEES_ReExchange" #交易重发
    ctypedef char TFBEFileFlagType "TThostFtdcFBEFileFlagType" #换汇文件标志
    enum: FBEFG_DataPackage "THOST_FTDC_FBEFG_DataPackage" #数据包
    enum: FBEFG_File "THOST_FTDC_FBEFG_File" #文件
    ctypedef char TFBEAlreadyTradeType "TThostFtdcFBEAlreadyTradeType" #换汇已交易标志
    enum: FBEAT_NotTrade "THOST_FTDC_FBEAT_NotTrade" #未交易
    enum: FBEAT_Trade "THOST_FTDC_FBEAT_Trade" #已交易
    ctypedef char[61] TFBEOpenBankType "TThostFtdcFBEOpenBankType" #换汇账户开户行
    ctypedef char TFBEUserEventTypeType "TThostFtdcFBEUserEventTypeType" #银期换汇用户事件类型
    enum: FBEUET_SignIn "THOST_FTDC_FBEUET_SignIn" #签到
    enum: FBEUET_Exchange "THOST_FTDC_FBEUET_Exchange" #换汇
    enum: FBEUET_ReExchange "THOST_FTDC_FBEUET_ReExchange" #换汇重发
    enum: FBEUET_QueryBankAccount "THOST_FTDC_FBEUET_QueryBankAccount" #银行账户查询
    enum: FBEUET_QueryExchDetial "THOST_FTDC_FBEUET_QueryExchDetial" #换汇明细查询
    enum: FBEUET_QueryExchSummary "THOST_FTDC_FBEUET_QueryExchSummary" #换汇汇总查询
    enum: FBEUET_QueryExchRate "THOST_FTDC_FBEUET_QueryExchRate" #换汇汇率查询
    enum: FBEUET_CheckBankAccount "THOST_FTDC_FBEUET_CheckBankAccount" #对账文件通知
    enum: FBEUET_SignOut "THOST_FTDC_FBEUET_SignOut" #签退
    enum: FBEUET_Other "THOST_FTDC_FBEUET_Other" #其他
    ctypedef char[21] TFBEFileNameType "TThostFtdcFBEFileNameType" #换汇相关文件名
    ctypedef char[21] TFBEBatchSerialType "TThostFtdcFBEBatchSerialType" #换汇批次号
    ctypedef char TFBEReqFlagType "TThostFtdcFBEReqFlagType" #换汇发送标志
    enum: FBERF_UnProcessed "THOST_FTDC_FBERF_UnProcessed" #未处理
    enum: FBERF_WaitSend "THOST_FTDC_FBERF_WaitSend" #等待发送
    enum: FBERF_SendSuccess "THOST_FTDC_FBERF_SendSuccess" #发送成功
    enum: FBERF_SendFailed "THOST_FTDC_FBERF_SendFailed" #发送失败
    enum: FBERF_WaitReSend "THOST_FTDC_FBERF_WaitReSend" #等待重发
    ctypedef char TNotifyClassType "TThostFtdcNotifyClassType" #风险通知类型
    enum: NC_NOERROR "THOST_FTDC_NC_NOERROR" #正常
    enum: NC_Warn "THOST_FTDC_NC_Warn" #警示
    enum: NC_Call "THOST_FTDC_NC_Call" #追保
    enum: NC_Force "THOST_FTDC_NC_Force" #强平
    enum: NC_CHUANCANG "THOST_FTDC_NC_CHUANCANG" #穿仓
    enum: NC_Exception "THOST_FTDC_NC_Exception" #异常
    ctypedef char[257] TRiskNofityInfoType "TThostFtdcRiskNofityInfoType" #客户风险通知消息
    ctypedef char[24] TForceCloseSceneIdType "TThostFtdcForceCloseSceneIdType" #强平场景编号
    ctypedef char TForceCloseTypeType "TThostFtdcForceCloseTypeType" #强平单类型
    enum: FCT_Manual "THOST_FTDC_FCT_Manual" #手工强平
    enum: FCT_Single "THOST_FTDC_FCT_Single" #单一投资者辅助强平
    enum: FCT_Group "THOST_FTDC_FCT_Group" #批量投资者辅助强平
    ctypedef char[101] TInstrumentIDsType "TThostFtdcInstrumentIDsType" #多个产品代码,用+分隔,如cu+zn
    ctypedef char TRiskNotifyMethodType "TThostFtdcRiskNotifyMethodType" #风险通知途径
    enum: RNM_System "THOST_FTDC_RNM_System" #系统通知
    enum: RNM_SMS "THOST_FTDC_RNM_SMS" #短信通知
    enum: RNM_EMail "THOST_FTDC_RNM_EMail" #邮件通知
    enum: RNM_Manual "THOST_FTDC_RNM_Manual" #人工通知
    ctypedef char TRiskNotifyStatusType "TThostFtdcRiskNotifyStatusType" #风险通知状态
    enum: RNS_NotGen "THOST_FTDC_RNS_NotGen" #未生成
    enum: RNS_Generated "THOST_FTDC_RNS_Generated" #已生成未发送
    enum: RNS_SendError "THOST_FTDC_RNS_SendError" #发送失败
    enum: RNS_SendOk "THOST_FTDC_RNS_SendOk" #已发送未接收
    enum: RNS_Received "THOST_FTDC_RNS_Received" #已接收未确认
    enum: RNS_Confirmed "THOST_FTDC_RNS_Confirmed" #已确认
    ctypedef char TRiskUserEventType "TThostFtdcRiskUserEventType" #风控用户操作事件
    enum: RUE_ExportData "THOST_FTDC_RUE_ExportData" #导出数据
    ctypedef int TParamIDType "TThostFtdcParamIDType" #参数代码
    ctypedef char[41] TParamNameType "TThostFtdcParamNameType" #参数名
    ctypedef char[41] TParamValueType "TThostFtdcParamValueType" #参数值
    ctypedef char TConditionalOrderSortTypeType "TThostFtdcConditionalOrderSortTypeType" #条件单索引条件
    enum: COST_LastPriceAsc "THOST_FTDC_COST_LastPriceAsc" #使用最新价升序
    enum: COST_LastPriceDesc "THOST_FTDC_COST_LastPriceDesc" #使用最新价降序
    enum: COST_AskPriceAsc "THOST_FTDC_COST_AskPriceAsc" #使用卖价升序
    enum: COST_AskPriceDesc "THOST_FTDC_COST_AskPriceDesc" #使用卖价降序
    enum: COST_BidPriceAsc "THOST_FTDC_COST_BidPriceAsc" #使用买价升序
    enum: COST_BidPriceDesc "THOST_FTDC_COST_BidPriceDesc" #使用买价降序
    ctypedef char TSendTypeType "TThostFtdcSendTypeType" #报送状态
    enum: UOAST_NoSend "THOST_FTDC_UOAST_NoSend" #未发送
    enum: UOAST_Sended "THOST_FTDC_UOAST_Sended" #已发送
    enum: UOAST_Generated "THOST_FTDC_UOAST_Generated" #已生成
    enum: UOAST_SendFail "THOST_FTDC_UOAST_SendFail" #报送失败
    enum: UOAST_Success "THOST_FTDC_UOAST_Success" #接收成功
    enum: UOAST_Fail "THOST_FTDC_UOAST_Fail" #接收失败
    enum: UOAST_Cancel "THOST_FTDC_UOAST_Cancel" #取消报送
    ctypedef char TClientIDStatusType "TThostFtdcClientIDStatusType" #交易编码状态
    enum: UOACS_NoApply "THOST_FTDC_UOACS_NoApply" #未申请
    enum: UOACS_Submited "THOST_FTDC_UOACS_Submited" #已提交申请
    enum: UOACS_Sended "THOST_FTDC_UOACS_Sended" #已发送申请
    enum: UOACS_Success "THOST_FTDC_UOACS_Success" #完成
    enum: UOACS_Refuse "THOST_FTDC_UOACS_Refuse" #拒绝
    enum: UOACS_Cancel "THOST_FTDC_UOACS_Cancel" #已撤销编码
    ctypedef char[17] TIndustryIDType "TThostFtdcIndustryIDType" #行业编码
    ctypedef char[5] TQuestionIDType "TThostFtdcQuestionIDType" #特有信息编号
    ctypedef char[41] TQuestionContentType "TThostFtdcQuestionContentType" #特有信息说明
    ctypedef char[13] TOptionIDType "TThostFtdcOptionIDType" #选项编号
    ctypedef char[61] TOptionContentType "TThostFtdcOptionContentType" #选项说明
    ctypedef char TQuestionTypeType "TThostFtdcQuestionTypeType" #特有信息类型
    enum: QT_Radio "THOST_FTDC_QT_Radio" #单选
    enum: QT_Option "THOST_FTDC_QT_Option" #多选
    enum: QT_Blank "THOST_FTDC_QT_Blank" #填空
    ctypedef char[33] TProcessIDType "TThostFtdcProcessIDType" #业务流水号
    ctypedef int TSeqNoType "TThostFtdcSeqNoType" #流水号
    ctypedef char[3] TUOAProcessStatusType "TThostFtdcUOAProcessStatusType" #流程状态
    ctypedef char[3] TProcessTypeType "TThostFtdcProcessTypeType" #流程功能类型
    ctypedef char TBusinessTypeType "TThostFtdcBusinessTypeType" #业务类型
    enum: BT_Request "THOST_FTDC_BT_Request" #请求
    enum: BT_Response "THOST_FTDC_BT_Response" #应答
    enum: BT_Notice "THOST_FTDC_BT_Notice" #通知
    ctypedef char TCfmmcReturnCodeType "TThostFtdcCfmmcReturnCodeType" #监控中心返回码
    enum: CRC_Success "THOST_FTDC_CRC_Success" #成功
    enum: CRC_Working "THOST_FTDC_CRC_Working" #该客户已经有流程在处理中
    enum: CRC_InfoFail "THOST_FTDC_CRC_InfoFail" #监控中客户资料检查失败
    enum: CRC_IDCardFail "THOST_FTDC_CRC_IDCardFail" #监控中实名制检查失败
    enum: CRC_OtherFail "THOST_FTDC_CRC_OtherFail" #其他错误
    ctypedef int TExReturnCodeType "TThostFtdcExReturnCodeType" #交易所返回码
    ctypedef char TClientTypeType "TThostFtdcClientTypeType" #客户类型
    enum: CfMMCCT_All "THOST_FTDC_CfMMCCT_All" #所有
    enum: CfMMCCT_Person "THOST_FTDC_CfMMCCT_Person" #个人
    enum: CfMMCCT_Company "THOST_FTDC_CfMMCCT_Company" #单位
    enum: CfMMCCT_Other "THOST_FTDC_CfMMCCT_Other" #其他
    enum: CfMMCCT_SpecialOrgan "THOST_FTDC_CfMMCCT_SpecialOrgan" #特殊法人
    enum: CfMMCCT_Asset "THOST_FTDC_CfMMCCT_Asset" #资管户
    ctypedef char TExchangeIDTypeType "TThostFtdcExchangeIDTypeType" #交易所编号
    enum: EIDT_SHFE "THOST_FTDC_EIDT_SHFE" #上海期货交易所
    enum: EIDT_CZCE "THOST_FTDC_EIDT_CZCE" #郑州商品交易所
    enum: EIDT_DCE "THOST_FTDC_EIDT_DCE" #大连商品交易所
    enum: EIDT_CFFEX "THOST_FTDC_EIDT_CFFEX" #中国金融期货交易所
    enum: EIDT_INE "THOST_FTDC_EIDT_INE" #上海国际能源交易中心股份有限公司
    ctypedef char TExClientIDTypeType "TThostFtdcExClientIDTypeType" #交易编码类型
    enum: ECIDT_Hedge "THOST_FTDC_ECIDT_Hedge" #套保
    enum: ECIDT_Arbitrage "THOST_FTDC_ECIDT_Arbitrage" #套利
    enum: ECIDT_Speculation "THOST_FTDC_ECIDT_Speculation" #投机
    ctypedef char[11] TClientClassifyType "TThostFtdcClientClassifyType" #客户分类码
    ctypedef char[11] TUOAOrganTypeType "TThostFtdcUOAOrganTypeType" #单位性质
    ctypedef char[11] TUOACountryCodeType "TThostFtdcUOACountryCodeType" #国家代码
    ctypedef char[11] TAreaCodeType "TThostFtdcAreaCodeType" #区号
    ctypedef char[21] TFuturesIDType "TThostFtdcFuturesIDType" #监控中心为客户分配的代码
    ctypedef char[11] TCffmcDateType "TThostFtdcCffmcDateType" #日期
    ctypedef char[11] TCffmcTimeType "TThostFtdcCffmcTimeType" #时间
    ctypedef char[21] TNocIDType "TThostFtdcNocIDType" #组织机构代码
    ctypedef char TUpdateFlagType "TThostFtdcUpdateFlagType" #更新状态
    enum: UF_NoUpdate "THOST_FTDC_UF_NoUpdate" #未更新
    enum: UF_Success "THOST_FTDC_UF_Success" #更新全部信息成功
    enum: UF_Fail "THOST_FTDC_UF_Fail" #更新全部信息失败
    enum: UF_TCSuccess "THOST_FTDC_UF_TCSuccess" #更新交易编码成功
    enum: UF_TCFail "THOST_FTDC_UF_TCFail" #更新交易编码失败
    enum: UF_Cancel "THOST_FTDC_UF_Cancel" #已丢弃
    ctypedef char TApplyOperateIDType "TThostFtdcApplyOperateIDType" #申请动作
    enum: AOID_OpenInvestor "THOST_FTDC_AOID_OpenInvestor" #开户
    enum: AOID_ModifyIDCard "THOST_FTDC_AOID_ModifyIDCard" #修改身份信息
    enum: AOID_ModifyNoIDCard "THOST_FTDC_AOID_ModifyNoIDCard" #修改一般信息
    enum: AOID_ApplyTradingCode "THOST_FTDC_AOID_ApplyTradingCode" #申请交易编码
    enum: AOID_CancelTradingCode "THOST_FTDC_AOID_CancelTradingCode" #撤销交易编码
    enum: AOID_CancelInvestor "THOST_FTDC_AOID_CancelInvestor" #销户
    enum: AOID_FreezeAccount "THOST_FTDC_AOID_FreezeAccount" #账户休眠
    enum: AOID_ActiveFreezeAccount "THOST_FTDC_AOID_ActiveFreezeAccount" #激活休眠账户
    ctypedef char TApplyStatusIDType "TThostFtdcApplyStatusIDType" #申请状态
    enum: ASID_NoComplete "THOST_FTDC_ASID_NoComplete" #未补全
    enum: ASID_Submited "THOST_FTDC_ASID_Submited" #已提交
    enum: ASID_Checked "THOST_FTDC_ASID_Checked" #已审核
    enum: ASID_Refused "THOST_FTDC_ASID_Refused" #已拒绝
    enum: ASID_Deleted "THOST_FTDC_ASID_Deleted" #已删除
    ctypedef char TSendMethodType "TThostFtdcSendMethodType" #发送方式
    enum: UOASM_ByAPI "THOST_FTDC_UOASM_ByAPI" #文件发送
    enum: UOASM_ByFile "THOST_FTDC_UOASM_ByFile" #电子发送
    ctypedef char[33] TEventTypeType "TThostFtdcEventTypeType" #业务操作类型
    ctypedef char TEventModeType "TThostFtdcEventModeType" #操作方法
    enum: EvM_ADD "THOST_FTDC_EvM_ADD" #增加
    enum: EvM_UPDATE "THOST_FTDC_EvM_UPDATE" #修改
    enum: EvM_DELETE "THOST_FTDC_EvM_DELETE" #删除
    enum: EvM_CHECK "THOST_FTDC_EvM_CHECK" #复核
    enum: EvM_COPY "THOST_FTDC_EvM_COPY" #复制
    enum: EvM_CANCEL "THOST_FTDC_EvM_CANCEL" #注销
    enum: EvM_Reverse "THOST_FTDC_EvM_Reverse" #冲销
    ctypedef char TUOAAutoSendType "TThostFtdcUOAAutoSendType" #统一开户申请自动发送
    enum: UOAA_ASR "THOST_FTDC_UOAA_ASR" #自动发送并接收
    enum: UOAA_ASNR "THOST_FTDC_UOAA_ASNR" #自动发送，不自动接收
    enum: UOAA_NSAR "THOST_FTDC_UOAA_NSAR" #不自动发送，自动接收
    enum: UOAA_NSR "THOST_FTDC_UOAA_NSR" #不自动发送，也不自动接收
    ctypedef int TQueryDepthType "TThostFtdcQueryDepthType" #查询深度
    ctypedef int TDataCenterIDType "TThostFtdcDataCenterIDType" #数据中心代码
    ctypedef char TFlowIDType "TThostFtdcFlowIDType" #流程ID
    enum: EvM_InvestorGroupFlow "THOST_FTDC_EvM_InvestorGroupFlow" #投资者对应投资者组设置
    enum: EvM_InvestorRate "THOST_FTDC_EvM_InvestorRate" #投资者手续费率设置
    enum: EvM_InvestorCommRateModel "THOST_FTDC_EvM_InvestorCommRateModel" #投资者手续费率模板关系设置
    ctypedef char TCheckLevelType "TThostFtdcCheckLevelType" #复核级别
    enum: CL_Zero "THOST_FTDC_CL_Zero" #零级复核
    enum: CL_One "THOST_FTDC_CL_One" #一级复核
    enum: CL_Two "THOST_FTDC_CL_Two" #二级复核
    ctypedef int TCheckNoType "TThostFtdcCheckNoType" #操作次数
    ctypedef char TCheckStatusType "TThostFtdcCheckStatusType" #复核级别
    enum: CHS_Init "THOST_FTDC_CHS_Init" #未复核
    enum: CHS_Checking "THOST_FTDC_CHS_Checking" #复核中
    enum: CHS_Checked "THOST_FTDC_CHS_Checked" #已复核
    enum: CHS_Refuse "THOST_FTDC_CHS_Refuse" #拒绝
    enum: CHS_Cancel "THOST_FTDC_CHS_Cancel" #作废
    ctypedef char TUsedStatusType "TThostFtdcUsedStatusType" #生效状态
    enum: CHU_Unused "THOST_FTDC_CHU_Unused" #未生效
    enum: CHU_Used "THOST_FTDC_CHU_Used" #已生效
    enum: CHU_Fail "THOST_FTDC_CHU_Fail" #生效失败
    ctypedef char[61] TRateTemplateNameType "TThostFtdcRateTemplateNameType" #模型名称
    ctypedef char[2049] TPropertyStringType "TThostFtdcPropertyStringType" #用于查询的投资属性字段
    ctypedef char TBankAcountOriginType "TThostFtdcBankAcountOriginType" #账户来源
    enum: BAO_ByAccProperty "THOST_FTDC_BAO_ByAccProperty" #手工录入
    enum: BAO_ByFBTransfer "THOST_FTDC_BAO_ByFBTransfer" #银期转账
    ctypedef char TMonthBillTradeSumType "TThostFtdcMonthBillTradeSumType" #结算单月报成交汇总方式
    enum: MBTS_ByInstrument "THOST_FTDC_MBTS_ByInstrument" #同日同合约
    enum: MBTS_ByDayInsPrc "THOST_FTDC_MBTS_ByDayInsPrc" #同日同合约同价格
    enum: MBTS_ByDayIns "THOST_FTDC_MBTS_ByDayIns" #同合约
    ctypedef char[7] TFBTTradeCodeEnumType "TThostFtdcFBTTradeCodeEnumType" #银期交易代码枚举
    enum: FTC_BankLaunchBankToBroker "THOST_FTDC_FTC_BankLaunchBankToBroker" #银行发起银行转期货
    enum: FTC_BrokerLaunchBankToBroker "THOST_FTDC_FTC_BrokerLaunchBankToBroker" #期货发起银行转期货
    enum: FTC_BankLaunchBrokerToBank "THOST_FTDC_FTC_BankLaunchBrokerToBank" #银行发起期货转银行
    enum: FTC_BrokerLaunchBrokerToBank "THOST_FTDC_FTC_BrokerLaunchBrokerToBank" #期货发起期货转银行
    ctypedef char[9] TRateTemplateIDType "TThostFtdcRateTemplateIDType" #模型代码
    ctypedef char[21] TRiskRateType "TThostFtdcRiskRateType" #风险度
    ctypedef int TTimestampType "TThostFtdcTimestampType" #时间戳
    ctypedef char[61] TInvestorIDRuleNameType "TThostFtdcInvestorIDRuleNameType" #号段规则名称
    ctypedef char[513] TInvestorIDRuleExprType "TThostFtdcInvestorIDRuleExprType" #号段规则表达式
    ctypedef int TLastDriftType "TThostFtdcLastDriftType" #上次OTP漂移值
    ctypedef int TLastSuccessType "TThostFtdcLastSuccessType" #上次OTP成功值
    ctypedef char[41] TAuthKeyType "TThostFtdcAuthKeyType" #令牌密钥
    ctypedef char[17] TSerialNumberType "TThostFtdcSerialNumberType" #序列号
    ctypedef char TOTPTypeType "TThostFtdcOTPTypeType" #动态令牌类型
    enum: OTP_NONE "THOST_FTDC_OTP_NONE" #无动态令牌
    enum: OTP_TOTP "THOST_FTDC_OTP_TOTP" #时间令牌
    ctypedef char[2] TOTPVendorsIDType "TThostFtdcOTPVendorsIDType" #动态令牌提供商
    ctypedef char[61] TOTPVendorsNameType "TThostFtdcOTPVendorsNameType" #动态令牌提供商名称
    ctypedef char TOTPStatusType "TThostFtdcOTPStatusType" #动态令牌状态
    enum: OTPS_Unused "THOST_FTDC_OTPS_Unused" #未使用
    enum: OTPS_Used "THOST_FTDC_OTPS_Used" #已使用
    enum: OTPS_Disuse "THOST_FTDC_OTPS_Disuse" #注销
    ctypedef char TBrokerUserTypeType "TThostFtdcBrokerUserTypeType" #经济公司用户类型
    enum: BUT_Investor "THOST_FTDC_BUT_Investor" #投资者
    enum: BUT_BrokerUser "THOST_FTDC_BUT_BrokerUser" #操作员
    ctypedef char TFutureTypeType "TThostFtdcFutureTypeType" #期货类型
    enum: FUTT_Commodity "THOST_FTDC_FUTT_Commodity" #商品期货
    enum: FUTT_Financial "THOST_FTDC_FUTT_Financial" #金融期货
    ctypedef char TFundEventTypeType "TThostFtdcFundEventTypeType" #资金管理操作类型
    enum: FET_Restriction "THOST_FTDC_FET_Restriction" #转账限额
    enum: FET_TodayRestriction "THOST_FTDC_FET_TodayRestriction" #当日转账限额
    enum: FET_Transfer "THOST_FTDC_FET_Transfer" #期商流水
    enum: FET_Credit "THOST_FTDC_FET_Credit" #资金冻结
    enum: FET_InvestorWithdrawAlm "THOST_FTDC_FET_InvestorWithdrawAlm" #投资者可提资金比例
    enum: FET_BankRestriction "THOST_FTDC_FET_BankRestriction" #单个银行帐户转账限额
    enum: FET_Accountregister "THOST_FTDC_FET_Accountregister" #银期签约账户
    enum: FET_ExchangeFundIO "THOST_FTDC_FET_ExchangeFundIO" #交易所出入金
    enum: FET_InvestorFundIO "THOST_FTDC_FET_InvestorFundIO" #投资者出入金
    ctypedef char TAccountSourceTypeType "TThostFtdcAccountSourceTypeType" #资金账户来源
    enum: AST_FBTransfer "THOST_FTDC_AST_FBTransfer" #银期同步
    enum: AST_ManualEntry "THOST_FTDC_AST_ManualEntry" #手工录入
    ctypedef char TCodeSourceTypeType "TThostFtdcCodeSourceTypeType" #交易编码来源
    enum: CST_UnifyAccount "THOST_FTDC_CST_UnifyAccount" #统一开户(已规范)
    enum: CST_ManualEntry "THOST_FTDC_CST_ManualEntry" #手工录入(未规范)
    ctypedef char TUserRangeType "TThostFtdcUserRangeType" #操作员范围
    enum: UR_All "THOST_FTDC_UR_All" #所有
    enum: UR_Single "THOST_FTDC_UR_Single" #单一操作员
    ctypedef char[9] TTimeSpanType "TThostFtdcTimeSpanType" #时间跨度
    ctypedef char[17] TImportSequenceIDType "TThostFtdcImportSequenceIDType" #动态令牌导入批次编号
    ctypedef char TByGroupType "TThostFtdcByGroupType" #交易统计表按客户统计方式
    enum: BG_Investor "THOST_FTDC_BG_Investor" #按投资者统计
    enum: BG_Group "THOST_FTDC_BG_Group" #按类统计
    ctypedef char TTradeSumStatModeType "TThostFtdcTradeSumStatModeType" #交易统计表按范围统计方式
    enum: TSSM_Instrument "THOST_FTDC_TSSM_Instrument" #按合约统计
    enum: TSSM_Product "THOST_FTDC_TSSM_Product" #按产品统计
    enum: TSSM_Exchange "THOST_FTDC_TSSM_Exchange" #按交易所统计
    ctypedef int TComTypeType "TThostFtdcComTypeType" #组合成交类型
    ctypedef char[33] TUserProductIDType "TThostFtdcUserProductIDType" #产品标识
    ctypedef char[65] TUserProductNameType "TThostFtdcUserProductNameType" #产品名称
    ctypedef char[129] TUserProductMemoType "TThostFtdcUserProductMemoType" #产品说明
    ctypedef char[2] TCSRCCancelFlagType "TThostFtdcCSRCCancelFlagType" #新增或变更标志
    ctypedef char[11] TCSRCDateType "TThostFtdcCSRCDateType" #日期
    ctypedef char[201] TCSRCInvestorNameType "TThostFtdcCSRCInvestorNameType" #客户名称
    ctypedef char[101] TCSRCOpenInvestorNameType "TThostFtdcCSRCOpenInvestorNameType" #客户名称
    ctypedef char[13] TCSRCInvestorIDType "TThostFtdcCSRCInvestorIDType" #客户代码
    ctypedef char[51] TCSRCIdentifiedCardNoType "TThostFtdcCSRCIdentifiedCardNoType" #证件号码
    ctypedef char[11] TCSRCClientIDType "TThostFtdcCSRCClientIDType" #交易编码
    ctypedef char[3] TCSRCBankFlagType "TThostFtdcCSRCBankFlagType" #银行标识
    ctypedef char[23] TCSRCBankAccountType "TThostFtdcCSRCBankAccountType" #银行账户
    ctypedef char[401] TCSRCOpenNameType "TThostFtdcCSRCOpenNameType" #开户人
    ctypedef char[101] TCSRCMemoType "TThostFtdcCSRCMemoType" #说明
    ctypedef char[11] TCSRCTimeType "TThostFtdcCSRCTimeType" #时间
    ctypedef char[21] TCSRCTradeIDType "TThostFtdcCSRCTradeIDType" #成交流水号
    ctypedef char[31] TCSRCExchangeInstIDType "TThostFtdcCSRCExchangeInstIDType" #合约代码
    ctypedef char[7] TCSRCMortgageNameType "TThostFtdcCSRCMortgageNameType" #质押品名称
    ctypedef char[3] TCSRCReasonType "TThostFtdcCSRCReasonType" #事由
    ctypedef char[2] TIsSettlementType "TThostFtdcIsSettlementType" #是否为非结算会员
    ctypedef double TCSRCMoneyType "TThostFtdcCSRCMoneyType" #资金
    ctypedef double TCSRCPriceType "TThostFtdcCSRCPriceType" #价格
    ctypedef char[2] TCSRCOptionsTypeType "TThostFtdcCSRCOptionsTypeType" #期权类型
    ctypedef double TCSRCStrikePriceType "TThostFtdcCSRCStrikePriceType" #执行价
    ctypedef char[3] TCSRCTargetProductIDType "TThostFtdcCSRCTargetProductIDType" #标的品种
    ctypedef char[31] TCSRCTargetInstrIDType "TThostFtdcCSRCTargetInstrIDType" #标的合约
    ctypedef char[161] TCommModelNameType "TThostFtdcCommModelNameType" #手续费率模板名称
    ctypedef char[1025] TCommModelMemoType "TThostFtdcCommModelMemoType" #手续费率模板备注
    ctypedef char TExprSetModeType "TThostFtdcExprSetModeType" #日期表达式设置类型
    enum: ESM_Relative "THOST_FTDC_ESM_Relative" #相对已有规则设置
    enum: ESM_Typical "THOST_FTDC_ESM_Typical" #典型设置
    ctypedef char TRateInvestorRangeType "TThostFtdcRateInvestorRangeType" #投资者范围
    enum: RIR_All "THOST_FTDC_RIR_All" #公司标准
    enum: RIR_Model "THOST_FTDC_RIR_Model" #模板
    enum: RIR_Single "THOST_FTDC_RIR_Single" #单一投资者
    ctypedef char[13] TAgentBrokerIDType "TThostFtdcAgentBrokerIDType" #代理经纪公司代码
    ctypedef int TDRIdentityIDType "TThostFtdcDRIdentityIDType" #交易中心代码
    ctypedef char[65] TDRIdentityNameType "TThostFtdcDRIdentityNameType" #交易中心名称
    ctypedef char[31] TDBLinkIDType "TThostFtdcDBLinkIDType" #DBLink标识号
    ctypedef char TSyncDataStatusType "TThostFtdcSyncDataStatusType" #主次用系统数据同步状态
    enum: SDS_Initialize "THOST_FTDC_SDS_Initialize" #未同步
    enum: SDS_Settlementing "THOST_FTDC_SDS_Settlementing" #同步中
    enum: SDS_Settlemented "THOST_FTDC_SDS_Settlemented" #已同步
    ctypedef char TTradeSourceType "TThostFtdcTradeSourceType" #成交来源
    enum: TSRC_NORMAL "THOST_FTDC_TSRC_NORMAL" #来自交易所普通回报
    enum: TSRC_QUERY "THOST_FTDC_TSRC_QUERY" #来自查询
    ctypedef char TFlexStatModeType "TThostFtdcFlexStatModeType" #产品合约统计方式
    enum: FSM_Product "THOST_FTDC_FSM_Product" #产品统计
    enum: FSM_Exchange "THOST_FTDC_FSM_Exchange" #交易所统计
    enum: FSM_All "THOST_FTDC_FSM_All" #统计所有
    ctypedef char TByInvestorRangeType "TThostFtdcByInvestorRangeType" #投资者范围统计方式
    enum: BIR_Property "THOST_FTDC_BIR_Property" #属性统计
    enum: BIR_All "THOST_FTDC_BIR_All" #统计所有
    ctypedef char[21] TSRiskRateType "TThostFtdcSRiskRateType" #风险度
    ctypedef int TSequenceNo12Type "TThostFtdcSequenceNo12Type" #序号
    ctypedef char TPropertyInvestorRangeType "TThostFtdcPropertyInvestorRangeType" #投资者范围
    enum: PIR_All "THOST_FTDC_PIR_All" #所有
    enum: PIR_Property "THOST_FTDC_PIR_Property" #投资者属性
    enum: PIR_Single "THOST_FTDC_PIR_Single" #单一投资者
    ctypedef char TFileStatusType "TThostFtdcFileStatusType" #文件状态
    enum: FIS_NoCreate "THOST_FTDC_FIS_NoCreate" #未生成
    enum: FIS_Created "THOST_FTDC_FIS_Created" #已生成
    enum: FIS_Failed "THOST_FTDC_FIS_Failed" #生成失败
    ctypedef char TFileGenStyleType "TThostFtdcFileGenStyleType" #文件生成方式
    enum: FGS_FileTransmit "THOST_FTDC_FGS_FileTransmit" #下发
    enum: FGS_FileGen "THOST_FTDC_FGS_FileGen" #生成
    ctypedef char TSysOperModeType "TThostFtdcSysOperModeType" #系统日志操作方法
    enum: SoM_Add "THOST_FTDC_SoM_Add" #增加
    enum: SoM_Update "THOST_FTDC_SoM_Update" #修改
    enum: SoM_Delete "THOST_FTDC_SoM_Delete" #删除
    enum: SoM_Copy "THOST_FTDC_SoM_Copy" #复制
    enum: SoM_AcTive "THOST_FTDC_SoM_AcTive" #激活
    enum: SoM_CanCel "THOST_FTDC_SoM_CanCel" #注销
    enum: SoM_ReSet "THOST_FTDC_SoM_ReSet" #重置
    ctypedef char TSysOperTypeType "TThostFtdcSysOperTypeType" #系统日志操作类型
    enum: SoT_UpdatePassword "THOST_FTDC_SoT_UpdatePassword" #修改操作员密码
    enum: SoT_UserDepartment "THOST_FTDC_SoT_UserDepartment" #操作员组织架构关系
    enum: SoT_RoleManager "THOST_FTDC_SoT_RoleManager" #角色管理
    enum: SoT_RoleFunction "THOST_FTDC_SoT_RoleFunction" #角色功能设置
    enum: SoT_BaseParam "THOST_FTDC_SoT_BaseParam" #基础参数设置
    enum: SoT_SetUserID "THOST_FTDC_SoT_SetUserID" #设置操作员
    enum: SoT_SetUserRole "THOST_FTDC_SoT_SetUserRole" #用户角色设置
    enum: SoT_UserIpRestriction "THOST_FTDC_SoT_UserIpRestriction" #用户IP限制
    enum: SoT_DepartmentManager "THOST_FTDC_SoT_DepartmentManager" #组织架构管理
    enum: SoT_DepartmentCopy "THOST_FTDC_SoT_DepartmentCopy" #组织架构向查询分类复制
    enum: SoT_Tradingcode "THOST_FTDC_SoT_Tradingcode" #交易编码管理
    enum: SoT_InvestorStatus "THOST_FTDC_SoT_InvestorStatus" #投资者状态维护
    enum: SoT_InvestorAuthority "THOST_FTDC_SoT_InvestorAuthority" #投资者权限管理
    enum: SoT_PropertySet "THOST_FTDC_SoT_PropertySet" #属性设置
    enum: SoT_ReSetInvestorPasswd "THOST_FTDC_SoT_ReSetInvestorPasswd" #重置投资者密码
    enum: SoT_InvestorPersonalityInfo "THOST_FTDC_SoT_InvestorPersonalityInfo" #投资者个性信息维护
    ctypedef char TCSRCDataQueyTypeType "TThostFtdcCSRCDataQueyTypeType" #上报数据查询类型
    enum: CSRCQ_Current "THOST_FTDC_CSRCQ_Current" #查询当前交易日报送的数据
    enum: CSRCQ_History "THOST_FTDC_CSRCQ_History" #查询历史报送的代理经纪公司的数据
    ctypedef char TFreezeStatusType "TThostFtdcFreezeStatusType" #休眠状态
    enum: FRS_Normal "THOST_FTDC_FRS_Normal" #活跃
    enum: FRS_Freeze "THOST_FTDC_FRS_Freeze" #休眠
    ctypedef char TStandardStatusType "TThostFtdcStandardStatusType" #规范状态
    enum: STST_Standard "THOST_FTDC_STST_Standard" #已规范
    enum: STST_NonStandard "THOST_FTDC_STST_NonStandard" #未规范
    ctypedef char[2] TCSRCFreezeStatusType "TThostFtdcCSRCFreezeStatusType" #休眠状态
    ctypedef char TRightParamTypeType "TThostFtdcRightParamTypeType" #配置类型
    enum: RPT_Freeze "THOST_FTDC_RPT_Freeze" #休眠户
    enum: RPT_FreezeActive "THOST_FTDC_RPT_FreezeActive" #激活休眠户
    enum: RPT_OpenLimit "THOST_FTDC_RPT_OpenLimit" #开仓权限限制
    enum: RPT_RelieveOpenLimit "THOST_FTDC_RPT_RelieveOpenLimit" #解除开仓权限限制
    ctypedef char[9] TRightTemplateIDType "TThostFtdcRightTemplateIDType" #模板代码
    ctypedef char[61] TRightTemplateNameType "TThostFtdcRightTemplateNameType" #模板名称
    ctypedef char TDataStatusType "TThostFtdcDataStatusType" #反洗钱审核表数据状态
    enum: AMLDS_Normal "THOST_FTDC_AMLDS_Normal" #正常
    enum: AMLDS_Deleted "THOST_FTDC_AMLDS_Deleted" #已删除
    ctypedef char TAMLCheckStatusType "TThostFtdcAMLCheckStatusType" #审核状态
    enum: AMLCHS_Init "THOST_FTDC_AMLCHS_Init" #未复核
    enum: AMLCHS_Checking "THOST_FTDC_AMLCHS_Checking" #复核中
    enum: AMLCHS_Checked "THOST_FTDC_AMLCHS_Checked" #已复核
    enum: AMLCHS_RefuseReport "THOST_FTDC_AMLCHS_RefuseReport" #拒绝上报
    ctypedef char TAmlDateTypeType "TThostFtdcAmlDateTypeType" #日期类型
    enum: AMLDT_DrawDay "THOST_FTDC_AMLDT_DrawDay" #检查日期
    enum: AMLDT_TouchDay "THOST_FTDC_AMLDT_TouchDay" #发生日期
    ctypedef char TAmlCheckLevelType "TThostFtdcAmlCheckLevelType" #审核级别
    enum: AMLCL_CheckLevel0 "THOST_FTDC_AMLCL_CheckLevel0" #零级审核
    enum: AMLCL_CheckLevel1 "THOST_FTDC_AMLCL_CheckLevel1" #一级审核
    enum: AMLCL_CheckLevel2 "THOST_FTDC_AMLCL_CheckLevel2" #二级审核
    enum: AMLCL_CheckLevel3 "THOST_FTDC_AMLCL_CheckLevel3" #三级审核
    ctypedef char[2] TAmlCheckFlowType "TThostFtdcAmlCheckFlowType" #反洗钱数据抽取审核流程
    ctypedef char[129] TDataTypeType "TThostFtdcDataTypeType" #数据类型
    ctypedef char TExportFileTypeType "TThostFtdcExportFileTypeType" #导出文件类型
    enum: EFT_CSV "THOST_FTDC_EFT_CSV" #CSV
    enum: EFT_EXCEL "THOST_FTDC_EFT_EXCEL" #Excel
    enum: EFT_DBF "THOST_FTDC_EFT_DBF" #DBF
    ctypedef char TSettleManagerTypeType "TThostFtdcSettleManagerTypeType" #结算配置类型
    enum: SMT_Before "THOST_FTDC_SMT_Before" #结算前准备
    enum: SMT_Settlement "THOST_FTDC_SMT_Settlement" #结算
    enum: SMT_After "THOST_FTDC_SMT_After" #结算后核对
    enum: SMT_Settlemented "THOST_FTDC_SMT_Settlemented" #结算后处理
    ctypedef char[33] TSettleManagerIDType "TThostFtdcSettleManagerIDType" #结算配置代码
    ctypedef char[129] TSettleManagerNameType "TThostFtdcSettleManagerNameType" #结算配置名称
    ctypedef char TSettleManagerLevelType "TThostFtdcSettleManagerLevelType" #结算配置等级
    enum: SML_Must "THOST_FTDC_SML_Must" #必要
    enum: SML_Alarm "THOST_FTDC_SML_Alarm" #警告
    enum: SML_Prompt "THOST_FTDC_SML_Prompt" #提示
    enum: SML_Ignore "THOST_FTDC_SML_Ignore" #不检查
    ctypedef char TSettleManagerGroupType "TThostFtdcSettleManagerGroupType" #模块分组
    enum: SMG_Exhcange "THOST_FTDC_SMG_Exhcange" #交易所核对
    enum: SMG_ASP "THOST_FTDC_SMG_ASP" #内部核对
    enum: SMG_CSRC "THOST_FTDC_SMG_CSRC" #上报数据核对
    ctypedef char[1025] TCheckResultMemoType "TThostFtdcCheckResultMemoType" #核对结果说明
    ctypedef char[1025] TFunctionUrlType "TThostFtdcFunctionUrlType" #功能链接
    ctypedef char[129] TAuthInfoType "TThostFtdcAuthInfoType" #客户端认证信息
    ctypedef char[17] TAuthCodeType "TThostFtdcAuthCodeType" #客户端认证码
    ctypedef char TLimitUseTypeType "TThostFtdcLimitUseTypeType" #保值额度使用类型
    enum: LUT_Repeatable "THOST_FTDC_LUT_Repeatable" #可重复使用
    enum: LUT_Unrepeatable "THOST_FTDC_LUT_Unrepeatable" #不可重复使用
    ctypedef char TDataResourceType "TThostFtdcDataResourceType" #数据来源
    enum: DAR_Settle "THOST_FTDC_DAR_Settle" #本系统
    enum: DAR_Exchange "THOST_FTDC_DAR_Exchange" #交易所
    enum: DAR_CSRC "THOST_FTDC_DAR_CSRC" #报送数据
    ctypedef char TMarginTypeType "TThostFtdcMarginTypeType" #保证金类型
    enum: MGT_ExchMarginRate "THOST_FTDC_MGT_ExchMarginRate" #交易所保证金率
    enum: MGT_InstrMarginRate "THOST_FTDC_MGT_InstrMarginRate" #投资者保证金率
    enum: MGT_InstrMarginRateTrade "THOST_FTDC_MGT_InstrMarginRateTrade" #投资者交易保证金率
    ctypedef char TActiveTypeType "TThostFtdcActiveTypeType" #生效类型
    enum: ACT_Intraday "THOST_FTDC_ACT_Intraday" #仅当日生效
    enum: ACT_Long "THOST_FTDC_ACT_Long" #长期生效
    ctypedef char TMarginRateTypeType "TThostFtdcMarginRateTypeType" #冲突保证金率类型
    enum: MRT_Exchange "THOST_FTDC_MRT_Exchange" #交易所保证金率
    enum: MRT_Investor "THOST_FTDC_MRT_Investor" #投资者保证金率
    enum: MRT_InvestorTrade "THOST_FTDC_MRT_InvestorTrade" #投资者交易保证金率
    ctypedef char TBackUpStatusType "TThostFtdcBackUpStatusType" #备份数据状态
    enum: BUS_UnBak "THOST_FTDC_BUS_UnBak" #未生成备份数据
    enum: BUS_BakUp "THOST_FTDC_BUS_BakUp" #备份数据生成中
    enum: BUS_BakUped "THOST_FTDC_BUS_BakUped" #已生成备份数据
    enum: BUS_BakFail "THOST_FTDC_BUS_BakFail" #备份数据失败
    ctypedef char TInitSettlementType "TThostFtdcInitSettlementType" #结算初始化状态
    enum: SIS_UnInitialize "THOST_FTDC_SIS_UnInitialize" #结算初始化未开始
    enum: SIS_Initialize "THOST_FTDC_SIS_Initialize" #结算初始化中
    enum: SIS_Initialized "THOST_FTDC_SIS_Initialized" #结算初始化完成
    ctypedef char TReportStatusType "TThostFtdcReportStatusType" #报表数据生成状态
    enum: SRS_NoCreate "THOST_FTDC_SRS_NoCreate" #未生成报表数据
    enum: SRS_Create "THOST_FTDC_SRS_Create" #报表数据生成中
    enum: SRS_Created "THOST_FTDC_SRS_Created" #已生成报表数据
    enum: SRS_CreateFail "THOST_FTDC_SRS_CreateFail" #生成报表数据失败
    ctypedef char TSaveStatusType "TThostFtdcSaveStatusType" #数据归档状态
    enum: SSS_UnSaveData "THOST_FTDC_SSS_UnSaveData" #归档未完成
    enum: SSS_SaveDatad "THOST_FTDC_SSS_SaveDatad" #归档完成
    ctypedef char TSettArchiveStatusType "TThostFtdcSettArchiveStatusType" #结算确认数据归档状态
    enum: SAS_UnArchived "THOST_FTDC_SAS_UnArchived" #未归档数据
    enum: SAS_Archiving "THOST_FTDC_SAS_Archiving" #数据归档中
    enum: SAS_Archived "THOST_FTDC_SAS_Archived" #已归档数据
    enum: SAS_ArchiveFail "THOST_FTDC_SAS_ArchiveFail" #归档数据失败
    ctypedef char TCTPTypeType "TThostFtdcCTPTypeType" #CTP交易系统类型
    enum: CTPT_Unkown "THOST_FTDC_CTPT_Unkown" #未知类型
    enum: CTPT_MainCenter "THOST_FTDC_CTPT_MainCenter" #主中心
    enum: CTPT_BackUp "THOST_FTDC_CTPT_BackUp" #备中心
    ctypedef char[9] TToolIDType "TThostFtdcToolIDType" #工具代码
    ctypedef char[81] TToolNameType "TThostFtdcToolNameType" #工具名称
    ctypedef char TCloseDealTypeType "TThostFtdcCloseDealTypeType" #平仓处理类型
    enum: CDT_Normal "THOST_FTDC_CDT_Normal" #正常
    enum: CDT_SpecFirst "THOST_FTDC_CDT_SpecFirst" #投机平仓优先
    ctypedef char TMortgageFundUseRangeType "TThostFtdcMortgageFundUseRangeType" #货币质押资金可用范围
    enum: MFUR_None "THOST_FTDC_MFUR_None" #不能使用
    enum: MFUR_Margin "THOST_FTDC_MFUR_Margin" #用于保证金
    enum: MFUR_All "THOST_FTDC_MFUR_All" #用于手续费、盈亏、保证金
    ctypedef double TCurrencyUnitType "TThostFtdcCurrencyUnitType" #币种单位数量
    ctypedef double TExchangeRateType "TThostFtdcExchangeRateType" #汇率
    ctypedef char TSpecProductTypeType "TThostFtdcSpecProductTypeType" #特殊产品类型
    enum: SPT_CzceHedge "THOST_FTDC_SPT_CzceHedge" #郑商所套保产品
    enum: SPT_IneForeignCurrency "THOST_FTDC_SPT_IneForeignCurrency" #货币质押产品
    enum: SPT_DceOpenClose "THOST_FTDC_SPT_DceOpenClose" #大连短线开平仓产品
    ctypedef char TFundMortgageTypeType "TThostFtdcFundMortgageTypeType" #货币质押类型
    enum: FMT_Mortgage "THOST_FTDC_FMT_Mortgage" #质押
    enum: FMT_Redemption "THOST_FTDC_FMT_Redemption" #解质
    ctypedef char TAccountSettlementParamIDType "TThostFtdcAccountSettlementParamIDType" #投资者账户结算参数代码
    enum: ASPI_BaseMargin "THOST_FTDC_ASPI_BaseMargin" #基础保证金
    enum: ASPI_LowestInterest "THOST_FTDC_ASPI_LowestInterest" #最低权益标准
    ctypedef char[31] TCurrencyNameType "TThostFtdcCurrencyNameType" #币种名称
    ctypedef char[4] TCurrencySignType "TThostFtdcCurrencySignType" #币种符号
    ctypedef char TFundMortDirectionType "TThostFtdcFundMortDirectionType" #货币质押方向
    enum: FMD_In "THOST_FTDC_FMD_In" #货币质入
    enum: FMD_Out "THOST_FTDC_FMD_Out" #货币质出
    ctypedef char TBusinessClassType "TThostFtdcBusinessClassType" #换汇类别
    enum: BT_Profit "THOST_FTDC_BT_Profit" #盈利
    enum: BT_Loss "THOST_FTDC_BT_Loss" #亏损
    enum: BT_Other "THOST_FTDC_BT_Other" #其他
    ctypedef char TSwapSourceTypeType "TThostFtdcSwapSourceTypeType" #换汇数据来源
    enum: SST_Manual "THOST_FTDC_SST_Manual" #手工
    enum: SST_Automatic "THOST_FTDC_SST_Automatic" #自动生成
    ctypedef char TCurrExDirectionType "TThostFtdcCurrExDirectionType" #换汇类型
    enum: CED_Settlement "THOST_FTDC_CED_Settlement" #结汇
    enum: CED_Sale "THOST_FTDC_CED_Sale" #售汇
    ctypedef char TCurrencySwapStatusType "TThostFtdcCurrencySwapStatusType" #申请状态
    enum: CSS_Entry "THOST_FTDC_CSS_Entry" #已录入
    enum: CSS_Approve "THOST_FTDC_CSS_Approve" #已审核
    enum: CSS_Refuse "THOST_FTDC_CSS_Refuse" #已拒绝
    enum: CSS_Revoke "THOST_FTDC_CSS_Revoke" #已撤销
    enum: CSS_Send "THOST_FTDC_CSS_Send" #已发送
    enum: CSS_Success "THOST_FTDC_CSS_Success" #换汇成功
    enum: CSS_Failure "THOST_FTDC_CSS_Failure" #换汇失败
    ctypedef char[13] TCurrExchCertNoType "TThostFtdcCurrExchCertNoType" #凭证号
    ctypedef char[21] TBatchSerialNoType "TThostFtdcBatchSerialNoType" #批次号
    ctypedef char TReqFlagType "TThostFtdcReqFlagType" #换汇发送标志
    enum: REQF_NoSend "THOST_FTDC_REQF_NoSend" #未发送
    enum: REQF_SendSuccess "THOST_FTDC_REQF_SendSuccess" #发送成功
    enum: REQF_SendFailed "THOST_FTDC_REQF_SendFailed" #发送失败
    enum: REQF_WaitReSend "THOST_FTDC_REQF_WaitReSend" #等待重发
    ctypedef char TResFlagType "TThostFtdcResFlagType" #换汇返回成功标志
    enum: RESF_Success "THOST_FTDC_RESF_Success" #成功
    enum: RESF_InsuffiCient "THOST_FTDC_RESF_InsuffiCient" #账户余额不足
    enum: RESF_UnKnown "THOST_FTDC_RESF_UnKnown" #交易结果未知
    ctypedef char[2] TPageControlType "TThostFtdcPageControlType" #换汇页面控制
    ctypedef int TRecordCountType "TThostFtdcRecordCountType" #记录数
    ctypedef char[101] TCurrencySwapMemoType "TThostFtdcCurrencySwapMemoType" #换汇需确认信息
    ctypedef char TExStatusType "TThostFtdcExStatusType" #修改状态
    enum: EXS_Before "THOST_FTDC_EXS_Before" #修改前
    enum: EXS_After "THOST_FTDC_EXS_After" #修改后
    ctypedef char TClientRegionType "TThostFtdcClientRegionType" #开户客户地域
    enum: CR_Domestic "THOST_FTDC_CR_Domestic" #国内客户
    enum: CR_GMT "THOST_FTDC_CR_GMT" #港澳台客户
    enum: CR_Foreign "THOST_FTDC_CR_Foreign" #国外客户
    ctypedef char[101] TWorkPlaceType "TThostFtdcWorkPlaceType" #工作单位
    ctypedef char[21] TBusinessPeriodType "TThostFtdcBusinessPeriodType" #经营期限
    ctypedef char[101] TWebSiteType "TThostFtdcWebSiteType" #网址
    ctypedef char[3] TUOAIdCardTypeType "TThostFtdcUOAIdCardTypeType" #统一开户证件类型
    ctypedef char[3] TClientModeType "TThostFtdcClientModeType" #开户模式
    ctypedef char[101] TInvestorFullNameType "TThostFtdcInvestorFullNameType" #投资者全称
    ctypedef char[11] TUOABrokerIDType "TThostFtdcUOABrokerIDType" #境外中介机构ID
    ctypedef char[11] TUOAZipCodeType "TThostFtdcUOAZipCodeType" #邮政编码
    ctypedef char[101] TUOAEMailType "TThostFtdcUOAEMailType" #电子邮箱
    ctypedef char[41] TOldCityType "TThostFtdcOldCityType" #城市
    ctypedef char[101] TCorporateIdentifiedCardNoType "TThostFtdcCorporateIdentifiedCardNoType" #法人代表证件号码
    ctypedef char THasBoardType "TThostFtdcHasBoardType" #是否有董事会
    enum: HB_No "THOST_FTDC_HB_No" #没有
    enum: HB_Yes "THOST_FTDC_HB_Yes" #有
    ctypedef char TStartModeType "TThostFtdcStartModeType" #启动模式
    enum: SM_Normal "THOST_FTDC_SM_Normal" #正常
    enum: SM_Emerge "THOST_FTDC_SM_Emerge" #应急
    enum: SM_Restore "THOST_FTDC_SM_Restore" #恢复
    ctypedef char TTemplateTypeType "TThostFtdcTemplateTypeType" #模型类型
    enum: TPT_Full "THOST_FTDC_TPT_Full" #全量
    enum: TPT_Increment "THOST_FTDC_TPT_Increment" #增量
    enum: TPT_BackUp "THOST_FTDC_TPT_BackUp" #备份
    ctypedef char TLoginModeType "TThostFtdcLoginModeType" #登录模式
    enum: LM_Trade "THOST_FTDC_LM_Trade" #交易
    enum: LM_Transfer "THOST_FTDC_LM_Transfer" #转账
    ctypedef char TPromptTypeType "TThostFtdcPromptTypeType" #日历提示类型
    enum: CPT_Instrument "THOST_FTDC_CPT_Instrument" #合约上下市
    enum: CPT_Margin "THOST_FTDC_CPT_Margin" #保证金分段生效
    ctypedef char[51] TLedgerManageIDType "TThostFtdcLedgerManageIDType" #分户管理资产编码
    ctypedef char[101] TInvestVarietyType "TThostFtdcInvestVarietyType" #投资品种
    ctypedef char[2] TBankAccountTypeType "TThostFtdcBankAccountTypeType" #账户类别
    ctypedef char[101] TLedgerManageBankType "TThostFtdcLedgerManageBankType" #开户银行
    ctypedef char[101] TCffexDepartmentNameType "TThostFtdcCffexDepartmentNameType" #开户营业部
    ctypedef char[9] TCffexDepartmentCodeType "TThostFtdcCffexDepartmentCodeType" #营业部代码
    ctypedef char THasTrusteeType "TThostFtdcHasTrusteeType" #是否有托管人
    enum: HT_Yes "THOST_FTDC_HT_Yes" #有
    enum: HT_No "THOST_FTDC_HT_No" #没有
    ctypedef char[41] TCSRCMemo1Type "TThostFtdcCSRCMemo1Type" #说明
    ctypedef char[101] TAssetmgrCFullNameType "TThostFtdcAssetmgrCFullNameType" #代理资产管理业务的期货公司全称
    ctypedef char[51] TAssetmgrApprovalNOType "TThostFtdcAssetmgrApprovalNOType" #资产管理业务批文号
    ctypedef char[401] TAssetmgrMgrNameType "TThostFtdcAssetmgrMgrNameType" #资产管理业务负责人姓名
    ctypedef char TAmTypeType "TThostFtdcAmTypeType" #机构类型
    enum: AMT_Bank "THOST_FTDC_AMT_Bank" #银行
    enum: AMT_Securities "THOST_FTDC_AMT_Securities" #证券公司
    enum: AMT_Fund "THOST_FTDC_AMT_Fund" #基金公司
    enum: AMT_Insurance "THOST_FTDC_AMT_Insurance" #保险公司
    enum: AMT_Trust "THOST_FTDC_AMT_Trust" #信托公司
    enum: AMT_Other "THOST_FTDC_AMT_Other" #其他
    ctypedef char[5] TCSRCAmTypeType "TThostFtdcCSRCAmTypeType" #机构类型
    ctypedef char TCSRCFundIOTypeType "TThostFtdcCSRCFundIOTypeType" #出入金类型
    enum: CFIOT_FundIO "THOST_FTDC_CFIOT_FundIO" #出入金
    enum: CFIOT_SwapCurrency "THOST_FTDC_CFIOT_SwapCurrency" #银期换汇
    ctypedef char TCusAccountTypeType "TThostFtdcCusAccountTypeType" #结算账户类型
    enum: CAT_Futures "THOST_FTDC_CAT_Futures" #期货结算账户
    enum: CAT_AssetmgrFuture "THOST_FTDC_CAT_AssetmgrFuture" #纯期货资管业务下的资管结算账户
    enum: CAT_AssetmgrTrustee "THOST_FTDC_CAT_AssetmgrTrustee" #综合类资管业务下的期货资管托管账户
    enum: CAT_AssetmgrTransfer "THOST_FTDC_CAT_AssetmgrTransfer" #综合类资管业务下的资金中转账户
    ctypedef char[4] TCSRCNationalType "TThostFtdcCSRCNationalType" #国籍
    ctypedef char[11] TCSRCSecAgentIDType "TThostFtdcCSRCSecAgentIDType" #二级代理ID
    ctypedef char TLanguageTypeType "TThostFtdcLanguageTypeType" #通知语言类型
    enum: LT_Chinese "THOST_FTDC_LT_Chinese" #中文
    enum: LT_English "THOST_FTDC_LT_English" #英文
    ctypedef char[23] TAmAccountType "TThostFtdcAmAccountType" #投资账户
    ctypedef char TAssetmgrClientTypeType "TThostFtdcAssetmgrClientTypeType" #资产管理客户类型
    enum: AMCT_Person "THOST_FTDC_AMCT_Person" #个人资管客户
    enum: AMCT_Organ "THOST_FTDC_AMCT_Organ" #单位资管客户
    enum: AMCT_SpecialOrgan "THOST_FTDC_AMCT_SpecialOrgan" #特殊单位资管客户
    ctypedef char TAssetmgrTypeType "TThostFtdcAssetmgrTypeType" #投资类型
    enum: ASST_Futures "THOST_FTDC_ASST_Futures" #期货类
    enum: ASST_SpecialOrgan "THOST_FTDC_ASST_SpecialOrgan" #综合类
    ctypedef char[11] TUOMType "TThostFtdcUOMType" #计量单位
    ctypedef char[3] TSHFEInstLifePhaseType "TThostFtdcSHFEInstLifePhaseType" #上期所合约生命周期状态
    ctypedef char[11] TSHFEProductClassType "TThostFtdcSHFEProductClassType" #产品类型
    ctypedef char[2] TPriceDecimalType "TThostFtdcPriceDecimalType" #价格小数位
    ctypedef char[2] TInTheMoneyFlagType "TThostFtdcInTheMoneyFlagType" #平值期权标志
    ctypedef char TCheckInstrTypeType "TThostFtdcCheckInstrTypeType" #合约比较类型
    enum: CIT_HasExch "THOST_FTDC_CIT_HasExch" #合约交易所不存在
    enum: CIT_HasATP "THOST_FTDC_CIT_HasATP" #合约本系统不存在
    enum: CIT_HasDiff "THOST_FTDC_CIT_HasDiff" #合约比较不一致
    ctypedef char TDeliveryTypeType "TThostFtdcDeliveryTypeType" #交割类型
    enum: DT_HandDeliv "THOST_FTDC_DT_HandDeliv" #手工交割
    enum: DT_PersonDeliv "THOST_FTDC_DT_PersonDeliv" #到期交割
    ctypedef double TBigMoneyType "TThostFtdcBigMoneyType" #资金
    ctypedef char TMaxMarginSideAlgorithmType "TThostFtdcMaxMarginSideAlgorithmType" #大额单边保证金算法
    enum: MMSA_NO "THOST_FTDC_MMSA_NO" #不使用大额单边保证金算法
    enum: MMSA_YES "THOST_FTDC_MMSA_YES" #使用大额单边保证金算法
    ctypedef char TDAClientTypeType "TThostFtdcDAClientTypeType" #资产管理客户类型
    enum: CACT_Person "THOST_FTDC_CACT_Person" #自然人
    enum: CACT_Company "THOST_FTDC_CACT_Company" #法人
    enum: CACT_Other "THOST_FTDC_CACT_Other" #其他
    ctypedef char[61] TCombinInstrIDType "TThostFtdcCombinInstrIDType" #套利合约代码
    ctypedef char[61] TCombinSettlePriceType "TThostFtdcCombinSettlePriceType" #各腿结算价
    ctypedef int TDCEPriorityType "TThostFtdcDCEPriorityType" #优先级
    ctypedef int TTradeGroupIDType "TThostFtdcTradeGroupIDType" #成交组号
    ctypedef int TIsCheckPrepaType "TThostFtdcIsCheckPrepaType" #是否校验开户可用资金
    ctypedef char TUOAAssetmgrTypeType "TThostFtdcUOAAssetmgrTypeType" #投资类型
    enum: UOAAT_Futures "THOST_FTDC_UOAAT_Futures" #期货类
    enum: UOAAT_SpecialOrgan "THOST_FTDC_UOAAT_SpecialOrgan" #综合类
    ctypedef char TDirectionEnType "TThostFtdcDirectionEnType" #买卖方向
    enum: DEN_Buy "THOST_FTDC_DEN_Buy" #Buy
    enum: DEN_Sell "THOST_FTDC_DEN_Sell" #Sell
    ctypedef char TOffsetFlagEnType "TThostFtdcOffsetFlagEnType" #开平标志
    enum: OFEN_Open "THOST_FTDC_OFEN_Open" #Position Opening
    enum: OFEN_Close "THOST_FTDC_OFEN_Close" #Position Close
    enum: OFEN_ForceClose "THOST_FTDC_OFEN_ForceClose" #Forced Liquidation
    enum: OFEN_CloseToday "THOST_FTDC_OFEN_CloseToday" #Close Today
    enum: OFEN_CloseYesterday "THOST_FTDC_OFEN_CloseYesterday" #Close Prev.
    enum: OFEN_ForceOff "THOST_FTDC_OFEN_ForceOff" #Forced Reduction
    enum: OFEN_LocalForceClose "THOST_FTDC_OFEN_LocalForceClose" #Local Forced Liquidation
    ctypedef char THedgeFlagEnType "TThostFtdcHedgeFlagEnType" #投机套保标志
    enum: HFEN_Speculation "THOST_FTDC_HFEN_Speculation" #Speculation
    enum: HFEN_Arbitrage "THOST_FTDC_HFEN_Arbitrage" #Arbitrage
    enum: HFEN_Hedge "THOST_FTDC_HFEN_Hedge" #Hedge
    ctypedef char TFundIOTypeEnType "TThostFtdcFundIOTypeEnType" #出入金类型
    enum: FIOTEN_FundIO "THOST_FTDC_FIOTEN_FundIO" #Deposit/Withdrawal
    enum: FIOTEN_Transfer "THOST_FTDC_FIOTEN_Transfer" #Bank-Futures Transfer
    enum: FIOTEN_SwapCurrency "THOST_FTDC_FIOTEN_SwapCurrency" #Bank-Futures FX Exchange
    ctypedef char TFundTypeEnType "TThostFtdcFundTypeEnType" #资金类型
    enum: FTEN_Deposite "THOST_FTDC_FTEN_Deposite" #Bank Deposit
    enum: FTEN_ItemFund "THOST_FTDC_FTEN_ItemFund" #Payment/Fee
    enum: FTEN_Company "THOST_FTDC_FTEN_Company" #Brokerage Adj
    enum: FTEN_InnerTransfer "THOST_FTDC_FTEN_InnerTransfer" #Internal Transfer
    ctypedef char TFundDirectionEnType "TThostFtdcFundDirectionEnType" #出入金方向
    enum: FDEN_In "THOST_FTDC_FDEN_In" #Deposit
    enum: FDEN_Out "THOST_FTDC_FDEN_Out" #Withdrawal
    ctypedef char TFundMortDirectionEnType "TThostFtdcFundMortDirectionEnType" #货币质押方向
    enum: FMDEN_In "THOST_FTDC_FMDEN_In" #Pledge
    enum: FMDEN_Out "THOST_FTDC_FMDEN_Out" #Redemption
    ctypedef char[3] TSwapBusinessTypeType "TThostFtdcSwapBusinessTypeType" #换汇业务种类
    ctypedef char TOptionsTypeType "TThostFtdcOptionsTypeType" #期权类型
    enum: CP_CallOptions "THOST_FTDC_CP_CallOptions" #看涨
    enum: CP_PutOptions "THOST_FTDC_CP_PutOptions" #看跌
    ctypedef char TStrikeModeType "TThostFtdcStrikeModeType" #执行方式
    enum: STM_Continental "THOST_FTDC_STM_Continental" #欧式
    enum: STM_American "THOST_FTDC_STM_American" #美式
    enum: STM_Bermuda "THOST_FTDC_STM_Bermuda" #百慕大
    ctypedef char TStrikeTypeType "TThostFtdcStrikeTypeType" #执行类型
    enum: STT_Hedge "THOST_FTDC_STT_Hedge" #自身对冲
    enum: STT_Match "THOST_FTDC_STT_Match" #匹配执行
    ctypedef char TApplyTypeType "TThostFtdcApplyTypeType" #中金所期权放弃执行申请类型
    enum: APPT_NotStrikeNum "THOST_FTDC_APPT_NotStrikeNum" #不执行数量
    ctypedef char TGiveUpDataSourceType "TThostFtdcGiveUpDataSourceType" #放弃执行申请数据来源
    enum: GUDS_Gen "THOST_FTDC_GUDS_Gen" #系统生成
    enum: GUDS_Hand "THOST_FTDC_GUDS_Hand" #手工添加
    ctypedef char[21] TExecOrderSysIDType "TThostFtdcExecOrderSysIDType" #执行宣告系统编号
    ctypedef char TExecResultType "TThostFtdcExecResultType" #执行结果
    enum: OER_NoExec "THOST_FTDC_OER_NoExec" #没有执行
    enum: OER_Canceled "THOST_FTDC_OER_Canceled" #已经取消
    enum: OER_OK "THOST_FTDC_OER_OK" #执行成功
    enum: OER_NoPosition "THOST_FTDC_OER_NoPosition" #期权持仓不够
    enum: OER_NoDeposit "THOST_FTDC_OER_NoDeposit" #资金不够
    enum: OER_NoParticipant "THOST_FTDC_OER_NoParticipant" #会员不存在
    enum: OER_NoClient "THOST_FTDC_OER_NoClient" #客户不存在
    enum: OER_NoInstrument "THOST_FTDC_OER_NoInstrument" #合约不存在
    enum: OER_NoRight "THOST_FTDC_OER_NoRight" #没有执行权限
    enum: OER_InvalidVolume "THOST_FTDC_OER_InvalidVolume" #不合理的数量
    enum: OER_NoEnoughHistoryTrade "THOST_FTDC_OER_NoEnoughHistoryTrade" #没有足够的历史成交
    enum: OER_Unknown "THOST_FTDC_OER_Unknown" #未知
    ctypedef int TStrikeSequenceType "TThostFtdcStrikeSequenceType" #执行序号
    ctypedef char[13] TStrikeTimeType "TThostFtdcStrikeTimeType" #执行时间
    ctypedef char TCombinationTypeType "TThostFtdcCombinationTypeType" #组合类型
    enum: COMBT_Future "THOST_FTDC_COMBT_Future" #期货组合
    enum: COMBT_BUL "THOST_FTDC_COMBT_BUL" #垂直价差BUL
    enum: COMBT_BER "THOST_FTDC_COMBT_BER" #垂直价差BER
    enum: COMBT_STD "THOST_FTDC_COMBT_STD" #跨式组合
    enum: COMBT_STG "THOST_FTDC_COMBT_STG" #宽跨式组合
    enum: COMBT_PRT "THOST_FTDC_COMBT_PRT" #备兑组合
    enum: COMBT_CLD "THOST_FTDC_COMBT_CLD" #时间价差组合
    ctypedef char TOptionRoyaltyPriceTypeType "TThostFtdcOptionRoyaltyPriceTypeType" #期权权利金价格类型
    enum: ORPT_PreSettlementPrice "THOST_FTDC_ORPT_PreSettlementPrice" #昨结算价
    enum: ORPT_OpenPrice "THOST_FTDC_ORPT_OpenPrice" #开仓价
    ctypedef char TBalanceAlgorithmType "TThostFtdcBalanceAlgorithmType" #权益算法
    enum: BLAG_Default "THOST_FTDC_BLAG_Default" #不计算期权市值盈亏
    enum: BLAG_IncludeOptValLost "THOST_FTDC_BLAG_IncludeOptValLost" #计算期权市值亏损
    ctypedef char TActionTypeType "TThostFtdcActionTypeType" #执行类型
    enum: ACTP_Exec "THOST_FTDC_ACTP_Exec" #执行
    enum: ACTP_Abandon "THOST_FTDC_ACTP_Abandon" #放弃
    ctypedef char TForQuoteStatusType "TThostFtdcForQuoteStatusType" #询价状态
    enum: FQST_Submitted "THOST_FTDC_FQST_Submitted" #已经提交
    enum: FQST_Accepted "THOST_FTDC_FQST_Accepted" #已经接受
    enum: FQST_Rejected "THOST_FTDC_FQST_Rejected" #已经被拒绝
    ctypedef char TValueMethodType "TThostFtdcValueMethodType" #取值方式
    enum: VM_Absolute "THOST_FTDC_VM_Absolute" #按绝对值
    enum: VM_Ratio "THOST_FTDC_VM_Ratio" #按比率
    ctypedef char TExecOrderPositionFlagType "TThostFtdcExecOrderPositionFlagType" #期权行权后是否保留期货头寸的标记
    enum: EOPF_Reserve "THOST_FTDC_EOPF_Reserve" #保留
    enum: EOPF_UnReserve "THOST_FTDC_EOPF_UnReserve" #不保留
    ctypedef char TExecOrderCloseFlagType "TThostFtdcExecOrderCloseFlagType" #期权行权后生成的头寸是否自动平仓
    enum: EOCF_AutoClose "THOST_FTDC_EOCF_AutoClose" #自动平仓
    enum: EOCF_NotToClose "THOST_FTDC_EOCF_NotToClose" #免于自动平仓
    ctypedef char TProductTypeType "TThostFtdcProductTypeType" #产品类型
    enum: PTE_Futures "THOST_FTDC_PTE_Futures" #期货
    enum: PTE_Options "THOST_FTDC_PTE_Options" #期权
    ctypedef char TCZCEUploadFileNameType "TThostFtdcCZCEUploadFileNameType" #郑商所结算文件名
    enum: CUFN_CUFN_O "THOST_FTDC_CUFN_CUFN_O" #^\d{8}_zz_\d{4}
    enum: CUFN_CUFN_T "THOST_FTDC_CUFN_CUFN_T" #^\d{8}成交表
    enum: CUFN_CUFN_P "THOST_FTDC_CUFN_CUFN_P" #^\d{8}单腿持仓表new
    enum: CUFN_CUFN_N "THOST_FTDC_CUFN_CUFN_N" #^\d{8}非平仓了结表
    enum: CUFN_CUFN_L "THOST_FTDC_CUFN_CUFN_L" #^\d{8}平仓表
    enum: CUFN_CUFN_F "THOST_FTDC_CUFN_CUFN_F" #^\d{8}资金表
    enum: CUFN_CUFN_C "THOST_FTDC_CUFN_CUFN_C" #^\d{8}组合持仓表
    enum: CUFN_CUFN_M "THOST_FTDC_CUFN_CUFN_M" #^\d{8}保证金参数表
    ctypedef char TDCEUploadFileNameType "TThostFtdcDCEUploadFileNameType" #大商所结算文件名
    enum: DUFN_DUFN_O "THOST_FTDC_DUFN_DUFN_O" #^\d{8}_dl_\d{3}
    enum: DUFN_DUFN_T "THOST_FTDC_DUFN_DUFN_T" #^\d{8}_成交表
    enum: DUFN_DUFN_P "THOST_FTDC_DUFN_DUFN_P" #^\d{8}_持仓表
    enum: DUFN_DUFN_F "THOST_FTDC_DUFN_DUFN_F" #^\d{8}_资金结算表
    enum: DUFN_DUFN_C "THOST_FTDC_DUFN_DUFN_C" #^\d{8}_优惠组合持仓明细表
    enum: DUFN_DUFN_D "THOST_FTDC_DUFN_DUFN_D" #^\d{8}_持仓明细表
    enum: DUFN_DUFN_M "THOST_FTDC_DUFN_DUFN_M" #^\d{8}_保证金参数表
    enum: DUFN_DUFN_S "THOST_FTDC_DUFN_DUFN_S" #^\d{8}_期权执行表
    ctypedef char TSHFEUploadFileNameType "TThostFtdcSHFEUploadFileNameType" #上期所结算文件名
    enum: SUFN_SUFN_O "THOST_FTDC_SUFN_SUFN_O" #^\d{4}_\d{8}_\d{8}_DailyFundChg
    enum: SUFN_SUFN_T "THOST_FTDC_SUFN_SUFN_T" #^\d{4}_\d{8}_\d{8}_Trade
    enum: SUFN_SUFN_P "THOST_FTDC_SUFN_SUFN_P" #^\d{4}_\d{8}_\d{8}_SettlementDetail
    enum: SUFN_SUFN_F "THOST_FTDC_SUFN_SUFN_F" #^\d{4}_\d{8}_\d{8}_Capital
    ctypedef char TCFFEXUploadFileNameType "TThostFtdcCFFEXUploadFileNameType" #中金所结算文件名
    enum: CFUFN_SUFN_T "THOST_FTDC_CFUFN_SUFN_T" #^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade
    enum: CFUFN_SUFN_P "THOST_FTDC_CFUFN_SUFN_P" #^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail
    enum: CFUFN_SUFN_F "THOST_FTDC_CFUFN_SUFN_F" #^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital
    enum: CFUFN_SUFN_S "THOST_FTDC_CFUFN_SUFN_S" #^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec
    ctypedef char TCombDirectionType "TThostFtdcCombDirectionType" #组合指令方向
    enum: CMDR_Comb "THOST_FTDC_CMDR_Comb" #申请组合
    enum: CMDR_UnComb "THOST_FTDC_CMDR_UnComb" #申请拆分
