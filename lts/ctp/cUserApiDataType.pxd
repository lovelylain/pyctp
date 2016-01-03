# -*- coding: utf-8 -*-

cdef extern from "SecurityFtdcUserApiDataType.h":
    cdef enum TE_RESUME_TYPE "SECURITY_TE_RESUME_TYPE": #流重传方式
        TERT_RESTART "SECURITY_TERT_RESTART" #从本交易日开始重传
        TERT_RESUME "SECURITY_TERT_RESUME" #从上次收到的续传
        TERT_QUICK "SECURITY_TERT_QUICK" #只传送登录后的流内容
    ctypedef int TErrorIDType "TSecurityFtdcErrorIDType" #错误代码
    ctypedef char[81] TErrorMsgType "TSecurityFtdcErrorMsgType" #错误信息
    ctypedef char[9] TExchangeIDType "TSecurityFtdcExchangeIDType" #交易所代码
    ctypedef char[31] TExchangeNameType "TSecurityFtdcExchangeNameType" #交易所名称
    ctypedef char TExchangePropertyType "TSecurityFtdcExchangePropertyType" #交易所属性
    enum: EXP_Normal "SECURITY_FTDC_EXP_Normal" #正常
    enum: EXP_GenOrderByTrade "SECURITY_FTDC_EXP_GenOrderByTrade" #根据成交生成报单
    ctypedef char TExchangeConnectStatusType "TSecurityFtdcExchangeConnectStatusType" #交易所连接状态
    enum: ECS_NoConnection "SECURITY_FTDC_ECS_NoConnection" #没有任何连接
    enum: ECS_QryInstrumentSent "SECURITY_FTDC_ECS_QryInstrumentSent" #已经发出合约查询请求
    enum: ECS_GotInformation "SECURITY_FTDC_ECS_GotInformation" #已经获取信息
    ctypedef char[9] TDateType "TSecurityFtdcDateType" #日期
    ctypedef char[9] TTimeType "TSecurityFtdcTimeType" #时间
    ctypedef char[31] TInstrumentIDType "TSecurityFtdcInstrumentIDType" #合约代码
    ctypedef char[21] TProductNameType "TSecurityFtdcProductNameType" #产品名称
    ctypedef char TProductClassType "TSecurityFtdcProductClassType" #产品类型
    enum: PC_Futures "SECURITY_FTDC_PC_Futures" #期货
    enum: PC_Options "SECURITY_FTDC_PC_Options" #期权
    enum: PC_Combination "SECURITY_FTDC_PC_Combination" #组合
    enum: PC_Spot "SECURITY_FTDC_PC_Spot" #即期
    enum: PC_EFP "SECURITY_FTDC_PC_EFP" #期转现
    enum: PC_StockA "SECURITY_FTDC_PC_StockA" #证券A股
    enum: PC_StockB "SECURITY_FTDC_PC_StockB" #证券B股
    enum: PC_ETF "SECURITY_FTDC_PC_ETF" #ETF
    enum: PC_ETFPurRed "SECURITY_FTDC_PC_ETFPurRed" #ETF申赎
    ctypedef int TVolumeMultipleType "TSecurityFtdcVolumeMultipleType" #合约数量乘数
    ctypedef double TPriceType "TSecurityFtdcPriceType" #价格
    ctypedef int TVolumeType "TSecurityFtdcVolumeType" #数量
    ctypedef char TPositionTypeType "TSecurityFtdcPositionTypeType" #持仓类型
    enum: PT_Net "SECURITY_FTDC_PT_Net" #净持仓
    enum: PT_Gross "SECURITY_FTDC_PT_Gross" #综合持仓
    ctypedef char TPositionDateTypeType "TSecurityFtdcPositionDateTypeType" #持仓日期类型
    enum: PDT_UseHistory "SECURITY_FTDC_PDT_UseHistory" #使用历史持仓
    enum: PDT_NoUseHistory "SECURITY_FTDC_PDT_NoUseHistory" #不使用历史持仓
    ctypedef char[31] TExchangeInstIDType "TSecurityFtdcExchangeInstIDType" #合约在交易所的代码
    ctypedef int TYearType "TSecurityFtdcYearType" #年份
    ctypedef int TMonthType "TSecurityFtdcMonthType" #月份
    ctypedef char TInstLifePhaseType "TSecurityFtdcInstLifePhaseType" #合约生命周期状态
    enum: IP_NotStart "SECURITY_FTDC_IP_NotStart" #未上市
    enum: IP_Started "SECURITY_FTDC_IP_Started" #上市
    enum: IP_Pause "SECURITY_FTDC_IP_Pause" #停牌
    enum: IP_Expired "SECURITY_FTDC_IP_Expired" #到期
    ctypedef int TBoolType "TSecurityFtdcBoolType" #布尔型
    ctypedef char[31] TRightModelIDType "TSecurityFtdcRightModelIDType" #股票权限模版代码
    ctypedef char[161] TRightModelNameType "TSecurityFtdcRightModelNameType" #股票权限模版名称
    ctypedef char TPosTradeTypeType "TSecurityFtdcPosTradeTypeType" #持仓交易类型
    enum: PTT_CanSelTodayPos "SECURITY_FTDC_PTT_CanSelTodayPos" #今日新增持仓能卖出
    enum: PTT_CannotSellTodayPos "SECURITY_FTDC_PTT_CannotSellTodayPos" #今日新增持仓不能卖出
    ctypedef char[21] TTraderIDType "TSecurityFtdcTraderIDType" #交易所交易员代码
    ctypedef char[11] TParticipantIDType "TSecurityFtdcParticipantIDType" #会员代码
    ctypedef char[41] TPasswordType "TSecurityFtdcPasswordType" #密码
    ctypedef char[11] TBrokerIDType "TSecurityFtdcBrokerIDType" #经纪公司代码
    ctypedef char[13] TOrderLocalIDType "TSecurityFtdcOrderLocalIDType" #本地报单编号
    ctypedef char[9] TBrokerAbbrType "TSecurityFtdcBrokerAbbrType" #经纪公司简称
    ctypedef char[81] TBrokerNameType "TSecurityFtdcBrokerNameType" #经纪公司名称
    ctypedef char[15] TInvestorIDType "TSecurityFtdcInvestorIDType" #投资者代码
    ctypedef char[81] TPartyNameType "TSecurityFtdcPartyNameType" #参与人名称
    ctypedef char TIdCardTypeType "TSecurityFtdcIdCardTypeType" #证件类型
    enum: ICT_EID "SECURITY_FTDC_ICT_EID" #组织机构代码
    enum: ICT_IDCard "SECURITY_FTDC_ICT_IDCard" #身份证
    enum: ICT_OfficerIDCard "SECURITY_FTDC_ICT_OfficerIDCard" #军官证
    enum: ICT_PoliceIDCard "SECURITY_FTDC_ICT_PoliceIDCard" #警官证
    enum: ICT_SoldierIDCard "SECURITY_FTDC_ICT_SoldierIDCard" #士兵证
    enum: ICT_HouseholdRegister "SECURITY_FTDC_ICT_HouseholdRegister" #户口簿
    enum: ICT_Passport "SECURITY_FTDC_ICT_Passport" #护照
    enum: ICT_TaiwanCompatriotIDCard "SECURITY_FTDC_ICT_TaiwanCompatriotIDCard" #台胞证
    enum: ICT_HomeComingCard "SECURITY_FTDC_ICT_HomeComingCard" #回乡证
    enum: ICT_LicenseNo "SECURITY_FTDC_ICT_LicenseNo" #营业执照号
    enum: ICT_TaxNo "SECURITY_FTDC_ICT_TaxNo" #税务登记号
    enum: ICT_OtherCard "SECURITY_FTDC_ICT_OtherCard" #其他证件
    ctypedef char[51] TIdentifiedCardNoType "TSecurityFtdcIdentifiedCardNoType" #证件号码
    ctypedef char[21] TClientIDType "TSecurityFtdcClientIDType" #交易编码
    ctypedef char[15] TAccountIDType "TSecurityFtdcAccountIDType" #投资者帐号
    ctypedef char TClientTypeType "TSecurityFtdcClientTypeType" #交易编码类型
    enum: CLT_Normal "SECURITY_FTDC_CLT_Normal" #普通
    enum: CLT_Credit "SECURITY_FTDC_CLT_Credit" #信用交易
    enum: CLT_Derive "SECURITY_FTDC_CLT_Derive" #衍生品账户
    enum: CLT_Other "SECURITY_FTDC_CLT_Other" #其他类型
    ctypedef char[41] TInvestorGroupNameType "TSecurityFtdcInvestorGroupNameType" #投资者分组名称
    ctypedef char[16] TUserIDType "TSecurityFtdcUserIDType" #用户代码
    ctypedef char[81] TUserNameType "TSecurityFtdcUserNameType" #用户名称
    ctypedef char TFunctionCodeType "TSecurityFtdcFunctionCodeType" #功能代码
    enum: FC_ForceUserLogout "SECURITY_FTDC_FC_ForceUserLogout" #强制用户登出
    enum: FC_UserPasswordUpdate "SECURITY_FTDC_FC_UserPasswordUpdate" #变更管理用户口令
    enum: FC_BrokerPasswordUpdate "SECURITY_FTDC_FC_BrokerPasswordUpdate" #变更经纪公司口令
    enum: FC_InvestorPasswordUpdate "SECURITY_FTDC_FC_InvestorPasswordUpdate" #变更投资者口令
    enum: FC_OrderInsert "SECURITY_FTDC_FC_OrderInsert" #报单插入
    enum: FC_OrderAction "SECURITY_FTDC_FC_OrderAction" #报单操作
    enum: FC_SyncSystemData "SECURITY_FTDC_FC_SyncSystemData" #同步系统数据
    enum: FC_SyncBrokerData "SECURITY_FTDC_FC_SyncBrokerData" #同步经纪公司数据
    enum: FC_SuperQuery "SECURITY_FTDC_FC_SuperQuery" #超级查询
    enum: FC_ParkedOrderInsert "SECURITY_FTDC_FC_ParkedOrderInsert" #报单插入
    enum: FC_ParkedOrderAction "SECURITY_FTDC_FC_ParkedOrderAction" #报单操作
    enum: FC_SyncOTP "SECURITY_FTDC_FC_SyncOTP" #同步动态令牌
    enum: FC_UnkownOrderAction "SECURITY_FTDC_FC_UnkownOrderAction" #未知单操作
    enum: FC_DepositoryTransfer "SECURITY_FTDC_FC_DepositoryTransfer" #转托管
    enum: FC_ExcessStockTransfer "SECURITY_FTDC_FC_ExcessStockTransfer" #余券划转
    ctypedef char TUserTypeType "TSecurityFtdcUserTypeType" #用户类型
    enum: UT_Investor "SECURITY_FTDC_UT_Investor" #投资者
    enum: UT_Operator "SECURITY_FTDC_UT_Operator" #操作员
    enum: UT_SuperUser "SECURITY_FTDC_UT_SuperUser" #管理员
    ctypedef char TBrokerFunctionCodeType "TSecurityFtdcBrokerFunctionCodeType" #经纪公司功能代码
    enum: BFC_ForceUserLogout "SECURITY_FTDC_BFC_ForceUserLogout" #强制用户登出
    enum: BFC_UserPasswordUpdate "SECURITY_FTDC_BFC_UserPasswordUpdate" #变更用户口令
    enum: BFC_SyncBrokerData "SECURITY_FTDC_BFC_SyncBrokerData" #同步经纪公司数据
    enum: BFC_OrderInsert "SECURITY_FTDC_BFC_OrderInsert" #报单插入
    enum: BFC_OrderAction "SECURITY_FTDC_BFC_OrderAction" #报单操作
    enum: BFC_AllQuery "SECURITY_FTDC_BFC_AllQuery" #全部查询
    enum: BFC_UnkownOrderAction "SECURITY_FTDC_BFC_UnkownOrderAction" #未知单操作
    enum: BFC_DepositoryTransfer "SECURITY_FTDC_BFC_DepositoryTransfer" #转托管
    enum: BFC_ExcessStockTransfer "SECURITY_FTDC_BFC_ExcessStockTransfer" #余券划转
    enum: BFC_log "SECURITY_FTDC_BFC_log" #系统功能：登入/登出/修改密码等
    enum: BFC_BaseQry "SECURITY_FTDC_BFC_BaseQry" #基本查询：查询基础数据，如合约，交易所等常量
    enum: BFC_TradeQry "SECURITY_FTDC_BFC_TradeQry" #交易查询：如查成交，委托
    enum: BFC_Trade "SECURITY_FTDC_BFC_Trade" #交易功能：报单，撤单
    enum: BFC_Virement "SECURITY_FTDC_BFC_Virement" #转账
    enum: BFC_Session "SECURITY_FTDC_BFC_Session" #查询/管理：查询会话，踢人等
    enum: BFC_SyncOTP "SECURITY_FTDC_BFC_SyncOTP" #同步动态令牌
    ctypedef char[4] TCurrencyCodeType "TSecurityFtdcCurrencyCodeType" #币种
    ctypedef double TMoneyType "TSecurityFtdcMoneyType" #资金
    ctypedef double TRatioType "TSecurityFtdcRatioType" #比率
    ctypedef char TAccountTypeType "TSecurityFtdcAccountTypeType" #账户类型
    enum: AcT_Normal "SECURITY_FTDC_AcT_Normal" #普通账户
    enum: AcT_Credit "SECURITY_FTDC_AcT_Credit" #信用账户
    enum: AcT_Derive "SECURITY_FTDC_AcT_Derive" #衍生品账户
    enum: AcT_Other "SECURITY_FTDC_AcT_Other" #其他类型
    ctypedef char TDepartmentRangeType "TSecurityFtdcDepartmentRangeType" #投资者范围
    enum: DR_All "SECURITY_FTDC_DR_All" #所有
    enum: DR_Group "SECURITY_FTDC_DR_Group" #组织架构
    enum: DR_Single "SECURITY_FTDC_DR_Single" #单一投资者
    ctypedef char TUserRightTypeType "TSecurityFtdcUserRightTypeType" #客户权限类型
    enum: URT_Logon "SECURITY_FTDC_URT_Logon" #登录
    enum: URT_Transfer "SECURITY_FTDC_URT_Transfer" #银期转帐
    enum: URT_EMail "SECURITY_FTDC_URT_EMail" #邮寄结算单
    enum: URT_Fax "SECURITY_FTDC_URT_Fax" #传真结算单
    enum: URT_ConditionOrder "SECURITY_FTDC_URT_ConditionOrder" #条件单
    ctypedef char[11] TProductInfoType "TSecurityFtdcProductInfoType" #产品信息
    ctypedef char[17] TAuthCodeType "TSecurityFtdcAuthCodeType" #客户端认证码
    ctypedef double TLargeVolumeType "TSecurityFtdcLargeVolumeType" #大额数量
    ctypedef int TMillisecType "TSecurityFtdcMillisecType" #时间（毫秒）
    ctypedef char THedgeFlagType "TSecurityFtdcHedgeFlagType" #投机套保标志
    enum: HF_Speculation "SECURITY_FTDC_HF_Speculation" #投机
    enum: HF_Hedge "SECURITY_FTDC_HF_Hedge" #套保
    ctypedef char TDirectionType "TSecurityFtdcDirectionType" #买卖方向
    enum: D_Buy "SECURITY_FTDC_D_Buy" #买
    enum: D_Sell "SECURITY_FTDC_D_Sell" #卖
    enum: D_ETFPur "SECURITY_FTDC_D_ETFPur" #ETF申购
    enum: D_ETFRed "SECURITY_FTDC_D_ETFRed" #ETF赎回
    enum: D_CashIn "SECURITY_FTDC_D_CashIn" #现金替代，只用作回报
    enum: D_PledgeBondIn "SECURITY_FTDC_D_PledgeBondIn" #债券入库
    enum: D_PledgeBondOut "SECURITY_FTDC_D_PledgeBondOut" #债券出库
    enum: D_Rationed "SECURITY_FTDC_D_Rationed" #配股
    enum: D_DepositoryTransfer "SECURITY_FTDC_D_DepositoryTransfer" #转托管
    enum: D_CreditRationed "SECURITY_FTDC_D_CreditRationed" #信用账户配股
    enum: D_BuyCollateral "SECURITY_FTDC_D_BuyCollateral" #担保品买入
    enum: D_SellCollateral "SECURITY_FTDC_D_SellCollateral" #担保品卖出
    enum: D_CollateralTransferIn "SECURITY_FTDC_D_CollateralTransferIn" #担保品转入
    enum: D_CollateralTransferOut "SECURITY_FTDC_D_CollateralTransferOut" #担保品转出
    enum: D_MarginTrade "SECURITY_FTDC_D_MarginTrade" #融资买入
    enum: D_ShortSell "SECURITY_FTDC_D_ShortSell" #融券卖出
    enum: D_RepayMargin "SECURITY_FTDC_D_RepayMargin" #卖券还款
    enum: D_RepayStock "SECURITY_FTDC_D_RepayStock" #买券还券
    enum: D_DirectRepayMargin "SECURITY_FTDC_D_DirectRepayMargin" #直接还款
    enum: D_DirectRepayStock "SECURITY_FTDC_D_DirectRepayStock" #直接还券
    enum: D_ExcessStockTransfer "SECURITY_FTDC_D_ExcessStockTransfer" #余券划转
    ctypedef char[21] TTradeIDType "TSecurityFtdcTradeIDType" #成交编号
    ctypedef char TTradeTypeType "TSecurityFtdcTradeTypeType" #成交类型
    enum: TRDT_Common "SECURITY_FTDC_TRDT_Common" #普通成交
    enum: TRDT_OptionsExecution "SECURITY_FTDC_TRDT_OptionsExecution" #期权执行
    enum: TRDT_OTC "SECURITY_FTDC_TRDT_OTC" #OTC成交
    enum: TRDT_EFPDerived "SECURITY_FTDC_TRDT_EFPDerived" #期转现衍生成交
    enum: TRDT_CombinationDerived "SECURITY_FTDC_TRDT_CombinationDerived" #组合衍生成交
    enum: TRDT_EFTPurchase "SECURITY_FTDC_TRDT_EFTPurchase" #ETF申购
    enum: TRDT_EFTRedem "SECURITY_FTDC_TRDT_EFTRedem" #ETF赎回
    ctypedef char TCreationredemptionStatusType "TSecurityFtdcCreationredemptionStatusType" #基金当天申购赎回状态
    enum: CDS_Forbidden "SECURITY_FTDC_CDS_Forbidden" #不允许申购赎回
    enum: CDS_Allow "SECURITY_FTDC_CDS_Allow" #表示允许申购和赎回
    enum: CDS_OnlyPurchase "SECURITY_FTDC_CDS_OnlyPurchase" #允许申购、不允许赎回
    enum: CDS_OnlyRedeem "SECURITY_FTDC_CDS_OnlyRedeem" #不允许申购、允许赎回
    ctypedef char TETFCurrenceReplaceStatusType "TSecurityFtdcETFCurrenceReplaceStatusType" #ETF现金替代标志
    enum: ETFCRS_Forbidden "SECURITY_FTDC_ETFCRS_Forbidden" #禁止现金替代
    enum: ETFCRS_Allow "SECURITY_FTDC_ETFCRS_Allow" #可以现金替代
    enum: ETFCRS_Force "SECURITY_FTDC_ETFCRS_Force" #必须现金替代
    ctypedef double TInterestType "TSecurityFtdcInterestType" #利息
    ctypedef double TRepurchaseMaxTimesType "TSecurityFtdcRepurchaseMaxTimesType" #正回购放大倍数
    ctypedef char TCapitalStockTypeType "TSecurityFtdcCapitalStockTypeType" #股本类型
    enum: CPTSTOCK_TOTALSTOCK "SECURITY_FTDC_CPTSTOCK_TOTALSTOCK" #总通股本
    enum: CPTSTOCK_CIRCULATION "SECURITY_FTDC_CPTSTOCK_CIRCULATION" #流通股本
    ctypedef char TMarginPriceTypeType "TSecurityFtdcMarginPriceTypeType" #保证金价格类型
    enum: MPT_PreSettlementPrice "SECURITY_FTDC_MPT_PreSettlementPrice" #昨结算价
    enum: MPT_SettlementPrice "SECURITY_FTDC_MPT_SettlementPrice" #最新价
    enum: MPT_AveragePrice "SECURITY_FTDC_MPT_AveragePrice" #成交均价
    enum: MPT_OpenPrice "SECURITY_FTDC_MPT_OpenPrice" #开仓价
    ctypedef char TAlgorithmType "TSecurityFtdcAlgorithmType" #盈亏算法
    enum: AG_All "SECURITY_FTDC_AG_All" #浮盈浮亏都计算
    enum: AG_OnlyLost "SECURITY_FTDC_AG_OnlyLost" #浮盈不计，浮亏计
    enum: AG_OnlyGain "SECURITY_FTDC_AG_OnlyGain" #浮盈计，浮亏不计
    enum: AG_None "SECURITY_FTDC_AG_None" #浮盈浮亏都不计算
    ctypedef char TIncludeCloseProfitType "TSecurityFtdcIncludeCloseProfitType" #是否包含平仓盈利
    enum: ICP_Include "SECURITY_FTDC_ICP_Include" #包含平仓盈利
    enum: ICP_NotInclude "SECURITY_FTDC_ICP_NotInclude" #不包含平仓盈利
    ctypedef char TAllWithoutTradeType "TSecurityFtdcAllWithoutTradeType" #是否受可提比例限制
    enum: AWT_Enable "SECURITY_FTDC_AWT_Enable" #不受可提比例限制
    enum: AWT_Disable "SECURITY_FTDC_AWT_Disable" #受可提比例限制
    enum: AWT_NoHoldEnable "SECURITY_FTDC_AWT_NoHoldEnable" #无仓不受可提比例限制
    ctypedef char THandlePositionAlgoIDType "TSecurityFtdcHandlePositionAlgoIDType" #持仓处理算法编号
    enum: HPA_Base "SECURITY_FTDC_HPA_Base" #基本
    enum: HPA_NoneTrade "SECURITY_FTDC_HPA_NoneTrade" #非交易
    enum: HPA_Stock "SECURITY_FTDC_HPA_Stock" #证券
    ctypedef char TTradeParamIDType "TSecurityFtdcTradeParamIDType" #交易系统参数代码
    enum: TPID_EncryptionStandard "SECURITY_FTDC_TPID_EncryptionStandard" #系统加密算法
    enum: TPID_SingleUserSessionMaxNum "SECURITY_FTDC_TPID_SingleUserSessionMaxNum" #用户最大会话数
    enum: TPID_LoginFailMaxNum "SECURITY_FTDC_TPID_LoginFailMaxNum" #最大连续登录失败数
    enum: TPID_IsAuthForce "SECURITY_FTDC_TPID_IsAuthForce" #是否强制认证
    enum: TPID_GenUserEvent "SECURITY_FTDC_TPID_GenUserEvent" #是否生成用户事件
    enum: TPID_StartOrderLocalID "SECURITY_FTDC_TPID_StartOrderLocalID" #起始报单本地编号
    enum: TPID_RepayStockAlgo "SECURITY_FTDC_TPID_RepayStockAlgo" #融资融券买券还券算法
    ctypedef char[256] TSettlementParamValueType "TSecurityFtdcSettlementParamValueType" #参数代码值
    ctypedef char[161] TMemoType "TSecurityFtdcMemoType" #备注
    ctypedef int TPriorityType "TSecurityFtdcPriorityType" #优先级
    ctypedef char[13] TOrderRefType "TSecurityFtdcOrderRefType" #报单引用
    ctypedef char[31] TMarketIDType "TSecurityFtdcMarketIDType" #市场代码
    ctypedef char[21] TMacAddressType "TSecurityFtdcMacAddressType" #Mac地址
    ctypedef char[21] TInstrumentNameType "TSecurityFtdcInstrumentNameType" #合约名称
    ctypedef char[21] TOrderSysIDType "TSecurityFtdcOrderSysIDType" #报单编号
    ctypedef char[16] TIPAddressType "TSecurityFtdcIPAddressType" #IP地址
    ctypedef char[11] TProtocolInfoType "TSecurityFtdcProtocolInfoType" #协议信息
    ctypedef char[15] TDepositSeqNoType "TSecurityFtdcDepositSeqNoType" #出入金流水号
    ctypedef char[41] TSystemNameType "TSecurityFtdcSystemNameType" #系统名称
    ctypedef char TInvestorRangeType "TSecurityFtdcInvestorRangeType" #投资者范围
    enum: IR_All "SECURITY_FTDC_IR_All" #所有
    enum: IR_Group "SECURITY_FTDC_IR_Group" #投资者组
    enum: IR_Single "SECURITY_FTDC_IR_Single" #单一投资者
    ctypedef char TDataSyncStatusType "TSecurityFtdcDataSyncStatusType" #数据同步状态
    enum: DS_Asynchronous "SECURITY_FTDC_DS_Asynchronous" #未同步
    enum: DS_Synchronizing "SECURITY_FTDC_DS_Synchronizing" #同步中
    enum: DS_Synchronized "SECURITY_FTDC_DS_Synchronized" #已同步
    ctypedef char TTraderConnectStatusType "TSecurityFtdcTraderConnectStatusType" #交易所交易员连接状态
    enum: TCS_NotConnected "SECURITY_FTDC_TCS_NotConnected" #没有任何连接
    enum: TCS_Connected "SECURITY_FTDC_TCS_Connected" #已经连接
    enum: TCS_QryInstrumentSent "SECURITY_FTDC_TCS_QryInstrumentSent" #已经发出合约查询请求
    enum: TCS_SubPrivateFlow "SECURITY_FTDC_TCS_SubPrivateFlow" #订阅私有流
    ctypedef char TOrderActionStatusType "TSecurityFtdcOrderActionStatusType" #报单操作状态
    enum: OAS_Submitted "SECURITY_FTDC_OAS_Submitted" #已经提交
    enum: OAS_Accepted "SECURITY_FTDC_OAS_Accepted" #已经接受
    enum: OAS_Rejected "SECURITY_FTDC_OAS_Rejected" #已经被拒绝
    ctypedef char TOrderStatusType "TSecurityFtdcOrderStatusType" #报单状态
    enum: OST_AllTraded "SECURITY_FTDC_OST_AllTraded" #全部成交
    enum: OST_PartTradedQueueing "SECURITY_FTDC_OST_PartTradedQueueing" #部分成交还在队列中
    enum: OST_PartTradedNotQueueing "SECURITY_FTDC_OST_PartTradedNotQueueing" #部分成交不在队列中
    enum: OST_NoTradeQueueing "SECURITY_FTDC_OST_NoTradeQueueing" #未成交还在队列中
    enum: OST_NoTradeNotQueueing "SECURITY_FTDC_OST_NoTradeNotQueueing" #未成交不在队列中
    enum: OST_Canceled "SECURITY_FTDC_OST_Canceled" #撤单
    enum: OST_Unknown "SECURITY_FTDC_OST_Unknown" #未知
    enum: OST_NotTouched "SECURITY_FTDC_OST_NotTouched" #尚未触发
    enum: OST_Touched "SECURITY_FTDC_OST_Touched" #已触发
    ctypedef char TOrderSubmitStatusType "TSecurityFtdcOrderSubmitStatusType" #报单提交状态
    enum: OSS_InsertSubmitted "SECURITY_FTDC_OSS_InsertSubmitted" #已经提交
    enum: OSS_CancelSubmitted "SECURITY_FTDC_OSS_CancelSubmitted" #撤单已经提交
    enum: OSS_ModifySubmitted "SECURITY_FTDC_OSS_ModifySubmitted" #修改已经提交
    enum: OSS_Accepted "SECURITY_FTDC_OSS_Accepted" #已经接受
    enum: OSS_InsertRejected "SECURITY_FTDC_OSS_InsertRejected" #报单已经被拒绝
    enum: OSS_CancelRejected "SECURITY_FTDC_OSS_CancelRejected" #撤单已经被拒绝
    enum: OSS_ModifyRejected "SECURITY_FTDC_OSS_ModifyRejected" #改单已经被拒绝
    ctypedef char TPositionDateType "TSecurityFtdcPositionDateType" #持仓日期
    enum: PSD_Today "SECURITY_FTDC_PSD_Today" #今日持仓
    enum: PSD_History "SECURITY_FTDC_PSD_History" #历史持仓
    ctypedef char TTradingRoleType "TSecurityFtdcTradingRoleType" #交易角色
    enum: ER_Broker "SECURITY_FTDC_ER_Broker" #代理
    enum: ER_Host "SECURITY_FTDC_ER_Host" #自营
    enum: ER_Maker "SECURITY_FTDC_ER_Maker" #做市商
    ctypedef char TPosiDirectionType "TSecurityFtdcPosiDirectionType" #持仓多空方向
    enum: PD_Net "SECURITY_FTDC_PD_Net" #净
    enum: PD_Long "SECURITY_FTDC_PD_Long" #多头
    enum: PD_Short "SECURITY_FTDC_PD_Short" #空头
    ctypedef char TOrderPriceTypeType "TSecurityFtdcOrderPriceTypeType" #报单价格条件
    enum: OPT_AnyPrice "SECURITY_FTDC_OPT_AnyPrice" #即时成交剩余撤销市价单
    enum: OPT_LimitPrice "SECURITY_FTDC_OPT_LimitPrice" #限价
    enum: OPT_BestPrice "SECURITY_FTDC_OPT_BestPrice" #最优五档即时成交剩余撤销市价单
    enum: OPT_BestLimitPrice "SECURITY_FTDC_OPT_BestLimitPrice" #最优五档即时成交剩余转限价市价单
    enum: OPT_AllPrice "SECURITY_FTDC_OPT_AllPrice" #全部成交或撤销市价单
    enum: OPT_ForwardBestPrice "SECURITY_FTDC_OPT_ForwardBestPrice" #本方最优价格市价单
    enum: OPT_ReverseBestPrice "SECURITY_FTDC_OPT_ReverseBestPrice" #对方最优价格市价单
    enum: OPT_ActiveANetPassSvrCode "SECURITY_FTDC_OPT_ActiveANetPassSvrCode" #激活A股网络密码服务代码
    enum: OPT_InactiveANetPassSvrCode "SECURITY_FTDC_OPT_InactiveANetPassSvrCode" #注销A股网络密码服务代码
    enum: OPT_ActiveBNetPassSvrCode "SECURITY_FTDC_OPT_ActiveBNetPassSvrCode" #激活B股网络密码服务代码
    enum: OPT_InactiveBNetPassSvrCode "SECURITY_FTDC_OPT_InactiveBNetPassSvrCode" #注销B股网络密码服务代码
    enum: OPT_Repurchase "SECURITY_FTDC_OPT_Repurchase" #回购注销
    enum: OPT_DesignatedCancel "SECURITY_FTDC_OPT_DesignatedCancel" #指定撤销
    enum: OPT_Designated "SECURITY_FTDC_OPT_Designated" #指定登记
    enum: OPT_SubscribingShares "SECURITY_FTDC_OPT_SubscribingShares" #证券参与申购
    enum: OPT_Split "SECURITY_FTDC_OPT_Split" #证券参与配股
    enum: OPT_TenderOffer "SECURITY_FTDC_OPT_TenderOffer" #要约收购登记
    enum: OPT_TenderOfferCancel "SECURITY_FTDC_OPT_TenderOfferCancel" #要约收购撤销
    enum: OPT_Ballot "SECURITY_FTDC_OPT_Ballot" #证券投票
    enum: OPT_ConvertibleBondsConvet "SECURITY_FTDC_OPT_ConvertibleBondsConvet" #可转债转换登记
    enum: OPT_ConvertibleBondsRepurchase "SECURITY_FTDC_OPT_ConvertibleBondsRepurchase" #可转债回售登记
    enum: OPT_Exercise "SECURITY_FTDC_OPT_Exercise" #权证行权
    enum: OPT_PurchasingFunds "SECURITY_FTDC_OPT_PurchasingFunds" #开放式基金申购
    enum: OPT_RedemingFunds "SECURITY_FTDC_OPT_RedemingFunds" #开放式基金赎回
    enum: OPT_SubscribingFunds "SECURITY_FTDC_OPT_SubscribingFunds" #开放式基金认购
    enum: OPT_LOFIssue "SECURITY_FTDC_OPT_LOFIssue" #开放式基金转托管转出
    enum: OPT_LOFSetBonusType "SECURITY_FTDC_OPT_LOFSetBonusType" #开放式基金设置分红方式
    enum: OPT_LOFConvert "SECURITY_FTDC_OPT_LOFConvert" #开放式基金转换为其他基金
    enum: OPT_DebentureStockIn "SECURITY_FTDC_OPT_DebentureStockIn" #债券入库
    enum: OPT_DebentureStockOut "SECURITY_FTDC_OPT_DebentureStockOut" #债券出库
    enum: OPT_PurchasesETF "SECURITY_FTDC_OPT_PurchasesETF" #ETF申购
    enum: OPT_RedeemETF "SECURITY_FTDC_OPT_RedeemETF" #ETF赎回
    ctypedef char TOffsetFlagType "TSecurityFtdcOffsetFlagType" #开平标志
    enum: OF_Open "SECURITY_FTDC_OF_Open" #开仓
    enum: OF_Close "SECURITY_FTDC_OF_Close" #平仓
    enum: OF_ForceClose "SECURITY_FTDC_OF_ForceClose" #强平
    enum: OF_CloseToday "SECURITY_FTDC_OF_CloseToday" #平今
    enum: OF_CloseYesterday "SECURITY_FTDC_OF_CloseYesterday" #平昨
    enum: OF_ForceOff "SECURITY_FTDC_OF_ForceOff" #强减
    enum: OF_LocalForceClose "SECURITY_FTDC_OF_LocalForceClose" #本地强平
    ctypedef char TForceCloseReasonType "TSecurityFtdcForceCloseReasonType" #强平原因
    enum: FCC_NotForceClose "SECURITY_FTDC_FCC_NotForceClose" #非强平
    enum: FCC_LackDeposit "SECURITY_FTDC_FCC_LackDeposit" #资金不足
    enum: FCC_ClientOverPositionLimit "SECURITY_FTDC_FCC_ClientOverPositionLimit" #客户超仓
    enum: FCC_MemberOverPositionLimit "SECURITY_FTDC_FCC_MemberOverPositionLimit" #会员超仓
    enum: FCC_NotMultiple "SECURITY_FTDC_FCC_NotMultiple" #持仓非整数倍
    enum: FCC_Violation "SECURITY_FTDC_FCC_Violation" #违规
    enum: FCC_Other "SECURITY_FTDC_FCC_Other" #其它
    enum: FCC_PersonDeliv "SECURITY_FTDC_FCC_PersonDeliv" #自然人临近交割
    ctypedef char TOrderTypeType "TSecurityFtdcOrderTypeType" #报单类型
    enum: ORDT_Normal "SECURITY_FTDC_ORDT_Normal" #正常
    enum: ORDT_DeriveFromQuote "SECURITY_FTDC_ORDT_DeriveFromQuote" #报价衍生
    enum: ORDT_DeriveFromCombination "SECURITY_FTDC_ORDT_DeriveFromCombination" #组合衍生
    enum: ORDT_Combination "SECURITY_FTDC_ORDT_Combination" #组合报单
    enum: ORDT_ConditionalOrder "SECURITY_FTDC_ORDT_ConditionalOrder" #条件单
    enum: ORDT_Swap "SECURITY_FTDC_ORDT_Swap" #互换单
    ctypedef char TTimeConditionType "TSecurityFtdcTimeConditionType" #有效期类型
    enum: TC_IOC "SECURITY_FTDC_TC_IOC" #立即完成，否则撤销
    enum: TC_GFS "SECURITY_FTDC_TC_GFS" #本节有效
    enum: TC_GFD "SECURITY_FTDC_TC_GFD" #当日有效
    enum: TC_GTD "SECURITY_FTDC_TC_GTD" #指定日期前有效
    enum: TC_GTC "SECURITY_FTDC_TC_GTC" #撤销前有效
    enum: TC_GFA "SECURITY_FTDC_TC_GFA" #集合竞价有效
    ctypedef char TVolumeConditionType "TSecurityFtdcVolumeConditionType" #成交量类型
    enum: VC_AV "SECURITY_FTDC_VC_AV" #任何数量
    enum: VC_MV "SECURITY_FTDC_VC_MV" #最小数量
    enum: VC_CV "SECURITY_FTDC_VC_CV" #全部数量
    ctypedef char TContingentConditionType "TSecurityFtdcContingentConditionType" #触发条件
    enum: CC_Immediately "SECURITY_FTDC_CC_Immediately" #立即
    enum: CC_Touch "SECURITY_FTDC_CC_Touch" #止损
    enum: CC_TouchProfit "SECURITY_FTDC_CC_TouchProfit" #止赢
    enum: CC_ParkedOrder "SECURITY_FTDC_CC_ParkedOrder" #预埋单
    enum: CC_LastPriceGreaterThanStopPrice "SECURITY_FTDC_CC_LastPriceGreaterThanStopPrice" #最新价大于条件价
    enum: CC_LastPriceGreaterEqualStopPrice "SECURITY_FTDC_CC_LastPriceGreaterEqualStopPrice" #最新价大于等于条件价
    enum: CC_LastPriceLesserThanStopPrice "SECURITY_FTDC_CC_LastPriceLesserThanStopPrice" #最新价小于条件价
    enum: CC_LastPriceLesserEqualStopPrice "SECURITY_FTDC_CC_LastPriceLesserEqualStopPrice" #最新价小于等于条件价
    enum: CC_AskPriceGreaterThanStopPrice "SECURITY_FTDC_CC_AskPriceGreaterThanStopPrice" #卖一价大于条件价
    enum: CC_AskPriceGreaterEqualStopPrice "SECURITY_FTDC_CC_AskPriceGreaterEqualStopPrice" #卖一价大于等于条件价
    enum: CC_AskPriceLesserThanStopPrice "SECURITY_FTDC_CC_AskPriceLesserThanStopPrice" #卖一价小于条件价
    enum: CC_AskPriceLesserEqualStopPrice "SECURITY_FTDC_CC_AskPriceLesserEqualStopPrice" #卖一价小于等于条件价
    enum: CC_BidPriceGreaterThanStopPrice "SECURITY_FTDC_CC_BidPriceGreaterThanStopPrice" #买一价大于条件价
    enum: CC_BidPriceGreaterEqualStopPrice "SECURITY_FTDC_CC_BidPriceGreaterEqualStopPrice" #买一价大于等于条件价
    enum: CC_BidPriceLesserThanStopPrice "SECURITY_FTDC_CC_BidPriceLesserThanStopPrice" #买一价小于条件价
    enum: CC_BidPriceLesserEqualStopPrice "SECURITY_FTDC_CC_BidPriceLesserEqualStopPrice" #买一价小于等于条件价
    ctypedef char TActionFlagType "TSecurityFtdcActionFlagType" #操作标志
    enum: AF_Delete "SECURITY_FTDC_AF_Delete" #删除
    enum: AF_Modify "SECURITY_FTDC_AF_Modify" #修改
    ctypedef char TTradingRightType "TSecurityFtdcTradingRightType" #交易权限
    enum: TR_Allow "SECURITY_FTDC_TR_Allow" #可以交易
    enum: TR_Forbidden "SECURITY_FTDC_TR_Forbidden" #不能交易
    ctypedef char TOrderSourceType "TSecurityFtdcOrderSourceType" #报单来源
    enum: OSRC_Participant "SECURITY_FTDC_OSRC_Participant" #来自参与者
    enum: OSRC_Administrator "SECURITY_FTDC_OSRC_Administrator" #来自管理员
    ctypedef char TPriceSourceType "TSecurityFtdcPriceSourceType" #成交价来源
    enum: PSRC_LastPrice "SECURITY_FTDC_PSRC_LastPrice" #前成交价
    enum: PSRC_Buy "SECURITY_FTDC_PSRC_Buy" #买委托价
    enum: PSRC_Sell "SECURITY_FTDC_PSRC_Sell" #卖委托价
    ctypedef int TOrderActionRefType "TSecurityFtdcOrderActionRefType" #报单操作引用
    ctypedef int TFrontIDType "TSecurityFtdcFrontIDType" #前置编号
    ctypedef int TSessionIDType "TSecurityFtdcSessionIDType" #会话编号
    ctypedef int TInstallIDType "TSecurityFtdcInstallIDType" #安装编号
    ctypedef int TSequenceNoType "TSecurityFtdcSequenceNoType" #序号
    ctypedef int TRequestIDType "TSecurityFtdcRequestIDType" #请求编号
    ctypedef char[5] TCombOffsetFlagType "TSecurityFtdcCombOffsetFlagType" #组合开平标志
    ctypedef char[5] TCombHedgeFlagType "TSecurityFtdcCombHedgeFlagType" #组合投机套保标志
    ctypedef short TSequenceSeriesType "TSecurityFtdcSequenceSeriesType" #序列系列号
    ctypedef short TCommPhaseNoType "TSecurityFtdcCommPhaseNoType" #通讯时段编号
    ctypedef char TUserEventTypeType "TSecurityFtdcUserEventTypeType" #用户事件类型
    enum: UET_Login "SECURITY_FTDC_UET_Login" #登录
    enum: UET_Logout "SECURITY_FTDC_UET_Logout" #登出
    enum: UET_Trading "SECURITY_FTDC_UET_Trading" #交易成功
    enum: UET_TradingError "SECURITY_FTDC_UET_TradingError" #交易失败
    enum: UET_UpdatePassword "SECURITY_FTDC_UET_UpdatePassword" #修改密码
    enum: UET_Authenticate "SECURITY_FTDC_UET_Authenticate" #客户端认证
    enum: UET_Other "SECURITY_FTDC_UET_Other" #其他
    ctypedef char[1025] TUserEventInfoType "TSecurityFtdcUserEventInfoType" #用户事件信息
    ctypedef char TOTPTypeType "TSecurityFtdcOTPTypeType" #动态令牌类型
    enum: OTP_NONE "SECURITY_FTDC_OTP_NONE" #无动态令牌
    enum: OTP_TOTP "SECURITY_FTDC_OTP_TOTP" #时间令牌
    ctypedef char TTradeSourceType "TSecurityFtdcTradeSourceType" #成交来源
    enum: TSRC_NORMAL "SECURITY_FTDC_TSRC_NORMAL" #来自交易所普通回报
    enum: TSRC_QUERY "SECURITY_FTDC_TSRC_QUERY" #来自查询
    ctypedef char[9] TBranchIDType "TSecurityFtdcBranchIDType" #营业部编号
    ctypedef char[16] TStockPriceType "TSecurityFtdcStockPriceType" #证券交易价格
    ctypedef char[31] TRightModelIDType "TSecurityFtdcRightModelIDType" #股票权限模版代码
    ctypedef char[17] TSerialNumberType "TSecurityFtdcSerialNumberType" #序列号
    ctypedef char TInstrumentRangeType "TSecurityFtdcInstrumentRangeType" #股票权限分类
    enum: INR_All "SECURITY_FTDC_INR_All" #所有
    enum: INR_Product "SECURITY_FTDC_INR_Product" #产品
    enum: INR_Model "SECURITY_FTDC_INR_Model" #股票权限模版
    enum: INR_Stock "SECURITY_FTDC_INR_Stock" #股票
    enum: INR_Market "SECURITY_FTDC_INR_Market" #市场
    ctypedef char[21] TBusinessUnitType "TSecurityFtdcBusinessUnitType" #业务单元
    ctypedef char[2] TOTPVendorsIDType "TSecurityFtdcOTPVendorsIDType" #动态令牌提供商
    ctypedef int TLastDriftType "TSecurityFtdcLastDriftType" #上次OTP漂移值
    ctypedef int TLastSuccessType "TSecurityFtdcLastSuccessType" #上次OTP成功值
    ctypedef char[41] TAuthKeyType "TSecurityFtdcAuthKeyType" #令牌密钥
    ctypedef int TUserSessionHashType "TSecurityFtdcUserSessionHashType" #用户会话Hash值
    ctypedef char TStockTradeTypeType "TSecurityFtdcStockTradeTypeType" #证券交易类型
    enum: STT_Stock "SECURITY_FTDC_STT_Stock" #可交易证券
    enum: STT_BuyNetService "SECURITY_FTDC_STT_BuyNetService" #买入网络密码服务
    enum: STT_CancelRepurchase "SECURITY_FTDC_STT_CancelRepurchase" #回购注销
    enum: STT_CancelRegister "SECURITY_FTDC_STT_CancelRegister" #指定撤销
    enum: STT_Register "SECURITY_FTDC_STT_Register" #指定登记
    enum: STT_PurchaseIssue "SECURITY_FTDC_STT_PurchaseIssue" #买入发行申购
    enum: STT_Allotment "SECURITY_FTDC_STT_Allotment" #卖出配股
    enum: STT_SellTender "SECURITY_FTDC_STT_SellTender" #卖出要约收购
    enum: STT_BuyTender "SECURITY_FTDC_STT_BuyTender" #买入要约收购
    enum: STT_NetVote "SECURITY_FTDC_STT_NetVote" #网上投票
    enum: STT_SellConvertibleBonds "SECURITY_FTDC_STT_SellConvertibleBonds" #卖出可转债回售
    enum: STT_OptionExecute "SECURITY_FTDC_STT_OptionExecute" #权证行权代码
    enum: STT_PurchaseOF "SECURITY_FTDC_STT_PurchaseOF" #开放式基金申购
    enum: STT_RedeemOF "SECURITY_FTDC_STT_RedeemOF" #开放式基金赎回
    enum: STT_SubscribeOF "SECURITY_FTDC_STT_SubscribeOF" #开放式基金认购
    enum: STT_OFCustodianTranfer "SECURITY_FTDC_STT_OFCustodianTranfer" #开放式基金转托管转出
    enum: STT_OFDividendConfig "SECURITY_FTDC_STT_OFDividendConfig" #开放式基金分红设置
    enum: STT_OFTransfer "SECURITY_FTDC_STT_OFTransfer" #开放式基金转成其他基金
    enum: STT_BondsIn "SECURITY_FTDC_STT_BondsIn" #债券入库
    enum: STT_BondsOut "SECURITY_FTDC_STT_BondsOut" #债券出库
    enum: STT_PurchaseETF "SECURITY_FTDC_STT_PurchaseETF" #EFT申购
    enum: STT_RedeemETF "SECURITY_FTDC_STT_RedeemETF" #EFT赎回
    enum: STT_ConvertibleRegister "SECURITY_FTDC_STT_ConvertibleRegister" #可转债回售登记
    ctypedef char THandleTradingAccountAlgoIDType "TSecurityFtdcHandleTradingAccountAlgoIDType" #资金处理算法编号
    enum: HTAA_Base "SECURITY_FTDC_HTAA_Base" #基本
    ctypedef int TStockWthType "TSecurityFtdcStockWthType" #股票使用流水号
    ctypedef char[11] TStockSeqType "TSecurityFtdcStockSeqType" #股票使用流水号
    ctypedef int TWTFSType "TSecurityFtdcWTFSType" #委托方式
    ctypedef int TWTLBType "TSecurityFtdcWTLBType" #委托类别
    ctypedef int TWTRQType "TSecurityFtdcWTRQType" #委托日期
    ctypedef int TINTEGERType "TSecurityFtdcINTEGERType" #一般整型
    ctypedef int TINT3Type "TSecurityFtdcINT3Type" #三位数整型
    ctypedef int TINT6Type "TSecurityFtdcINT6Type" #六位数整型
    ctypedef char[2] TCHAR1Type "TSecurityFtdcCHAR1Type" #一字节CHAR
    ctypedef char[3] TCHAR2Type "TSecurityFtdcCHAR2Type" #二字节CHAR
    ctypedef char[4] TCHAR3Type "TSecurityFtdcCHAR3Type" #三字节CHAR
    ctypedef char[5] TCHAR4Type "TSecurityFtdcCHAR4Type" #四字节CHAR
    ctypedef char[6] TCHAR5Type "TSecurityFtdcCHAR5Type" #五字节CHAR
    ctypedef char[7] TCHAR6Type "TSecurityFtdcCHAR6Type" #六字节CHAR
    ctypedef char[9] TCHAR8Type "TSecurityFtdcCHAR8Type" #八字节CHAR
    ctypedef char[11] TCHAR10Type "TSecurityFtdcCHAR10Type" #十字节CHAR
    ctypedef char[13] TCHAR12Type "TSecurityFtdcCHAR12Type" #十二字节CHAR
    ctypedef char[14] TCHAR13Type "TSecurityFtdcCHAR13Type" #十三字节CHAR
    ctypedef char[15] TCHAR14Type "TSecurityFtdcCHAR14Type" #十四字节CHAR
    ctypedef char[17] TCHAR16Type "TSecurityFtdcCHAR16Type" #十六字节CHAR
    ctypedef char[5] TVCHAR4Type "TSecurityFtdcVCHAR4Type" #四字节VCHAR
    ctypedef char[7] TVCHAR6Type "TSecurityFtdcVCHAR6Type" #六字节VCHAR
    ctypedef char[9] TVCHAR8Type "TSecurityFtdcVCHAR8Type" #八字节VCHAR
    ctypedef char[11] TVCHAR10Type "TSecurityFtdcVCHAR10Type" #十字节VCHAR
    ctypedef char[13] TVCHAR12Type "TSecurityFtdcVCHAR12Type" #十二字节VCHAR
    ctypedef char[17] TVCHAR16Type "TSecurityFtdcVCHAR16Type" #十六字节VCHAR
    ctypedef char[21] TVCHAR20Type "TSecurityFtdcVCHAR20Type" #二十字节VCHAR
    ctypedef char[31] TVCHAR30Type "TSecurityFtdcVCHAR30Type" #三十字节VCHAR
    ctypedef char[51] TVCHAR50Type "TSecurityFtdcVCHAR50Type" #五十字节VCHAR
    ctypedef char[61] TVCHAR60Type "TSecurityFtdcVCHAR60Type" #六十字节VCHAR
    ctypedef char[66] TVCHAR65Type "TSecurityFtdcVCHAR65Type" #六十五字节VCHAR
    ctypedef char[81] TVCHAR80Type "TSecurityFtdcVCHAR80Type" #八十字节VCHAR
    ctypedef char[256] TVCHAR255Type "TSecurityFtdcVCHAR255Type" #二五五字节VCHAR
    ctypedef double TREAL9P3Type "TSecurityFtdcREAL9P3Type" #九点三实型
    ctypedef double TREAL10P4Type "TSecurityFtdcREAL10P4Type" #十点四实型
    ctypedef double TREAL16P2Type "TSecurityFtdcREAL16P2Type" #十六点二实型
    ctypedef double TREAL16P8Type "TSecurityFtdcREAL16P8Type" #十六点八实型
    ctypedef double TREAL22P2Type "TSecurityFtdcREAL22P2Type" #二十二点二实型
    ctypedef int TCommandNoType "TSecurityFtdcCommandNoType" #DB命令序号
    ctypedef char[65] TCommandTypeType "TSecurityFtdcCommandTypeType" #DB命令类型
    ctypedef char[9] TSettlementGroupIDType "TSecurityFtdcSettlementGroupIDType" #结算组代码
    ctypedef char[2049] TFieldNameType "TSecurityFtdcFieldNameType" #字段名
    ctypedef char[2049] TFieldContentType "TSecurityFtdcFieldContentType" #字段内容
    ctypedef char[4] TBankIDType "TSecurityFtdcBankIDType" #银行代码
    ctypedef char[101] TBankNameType "TSecurityFtdcBankNameType" #银行名称
    ctypedef char[5] TBankBrchIDType "TSecurityFtdcBankBrchIDType" #银行分中心代码
    ctypedef int TLiberSerialType "TSecurityFtdcLiberSerialType" #Liber系统流水号
    ctypedef char[11] TRoleIDType "TSecurityFtdcRoleIDType" #角色编号
    ctypedef char[41] TRoleNameType "TSecurityFtdcRoleNameType" #角色名称
    ctypedef char[401] TDescriptionType "TSecurityFtdcDescriptionType" #描述
    ctypedef char[25] TFunctionIDType "TSecurityFtdcFunctionIDType" #功能代码
    ctypedef char[15] TBillNoType "TSecurityFtdcBillNoType" #票据号
    ctypedef char TFundIOTypeType "TSecurityFtdcFundIOTypeType" #出入金类型
    enum: FIOT_FundIO "SECURITY_FTDC_FIOT_FundIO" #出入金
    enum: FIOT_Transfer "SECURITY_FTDC_FIOT_Transfer" #银期转帐
    ctypedef char TFundTypeType "TSecurityFtdcFundTypeType" #资金类型
    enum: FT_Deposite "SECURITY_FTDC_FT_Deposite" #银行存款
    enum: FT_ItemFund "SECURITY_FTDC_FT_ItemFund" #分项资金
    enum: FT_Company "SECURITY_FTDC_FT_Company" #公司调整
    ctypedef char TFundDirectionType "TSecurityFtdcFundDirectionType" #出入金方向
    enum: FD_In "SECURITY_FTDC_FD_In" #入金
    enum: FD_Out "SECURITY_FTDC_FD_Out" #出金
    ctypedef char TBankFlagType "TSecurityFtdcBankFlagType" #银行统一标识类型
    enum: BF_ICBC "SECURITY_FTDC_BF_ICBC" #工商银行
    enum: BF_ABC "SECURITY_FTDC_BF_ABC" #农业银行
    enum: BF_BC "SECURITY_FTDC_BF_BC" #中国银行
    enum: BF_CBC "SECURITY_FTDC_BF_CBC" #建设银行
    enum: BF_BOC "SECURITY_FTDC_BF_BOC" #交通银行
    enum: BF_Other "SECURITY_FTDC_BF_Other" #其他银行
    ctypedef char[1025] TOperationMemoType "TSecurityFtdcOperationMemoType" #操作摘要
    ctypedef char TFundStatusType "TSecurityFtdcFundStatusType" #资金状态
    enum: FS_Record "SECURITY_FTDC_FS_Record" #已录入
    enum: FS_Check "SECURITY_FTDC_FS_Check" #已复核
    enum: FS_Charge "SECURITY_FTDC_FS_Charge" #已冲销
    ctypedef char[5] TFundProjectIDType "TSecurityFtdcFundProjectIDType" #资金项目编号
    ctypedef char[65] TOperatorIDType "TSecurityFtdcOperatorIDType" #操作员代码
    ctypedef char[33] TCounterIDType "TSecurityFtdcCounterIDType" #计数器代码
    ctypedef char[65] TFunctionNameType "TSecurityFtdcFunctionNameType" #功能名称
    ctypedef char[7] TTradeCodeType "TSecurityFtdcTradeCodeType" #交易代码
    ctypedef char[31] TBrokerBranchIDType "TSecurityFtdcBrokerBranchIDType" #经纪公司分支机构代码
    ctypedef char[9] TTradeDateType "TSecurityFtdcTradeDateType" #交易日期
    ctypedef char[9] TTradeTimeType "TSecurityFtdcTradeTimeType" #交易时间
    ctypedef char[13] TBankSerialType "TSecurityFtdcBankSerialType" #银行流水号
    ctypedef int TSerialType "TSecurityFtdcSerialType" #流水号
    ctypedef char TLastFragmentType "TSecurityFtdcLastFragmentType" #最后分片标志
    enum: LF_Yes "SECURITY_FTDC_LF_Yes" #是最后分片
    enum: LF_No "SECURITY_FTDC_LF_No" #不是最后分片
    ctypedef char[51] TIndividualNameType "TSecurityFtdcIndividualNameType" #个人姓名
    ctypedef char TCustTypeType "TSecurityFtdcCustTypeType" #客户类型
    enum: CUSTT_Person "SECURITY_FTDC_CUSTT_Person" #自然人
    enum: CUSTT_Institution "SECURITY_FTDC_CUSTT_Institution" #机构户
    ctypedef char[41] TBankAccountType "TSecurityFtdcBankAccountType" #银行账户
    ctypedef char TYesNoIndicatorType "TSecurityFtdcYesNoIndicatorType" #是或否标识
    enum: YNI_Yes "SECURITY_FTDC_YNI_Yes" #是
    enum: YNI_No "SECURITY_FTDC_YNI_No" #否
    ctypedef double TTradeAmountType "TSecurityFtdcTradeAmountType" #交易金额（元）
    ctypedef double TCustFeeType "TSecurityFtdcCustFeeType" #应收客户费用（元）
    ctypedef double TBrokerFeeType "TSecurityFtdcBrokerFeeType" #应收经纪公司费用（元）
    ctypedef char TFeePayFlagType "TSecurityFtdcFeePayFlagType" #费用支付标志
    enum: FPF_BEN "SECURITY_FTDC_FPF_BEN" #由受益方支付费用
    enum: FPF_OUR "SECURITY_FTDC_FPF_OUR" #由发送方支付费用
    enum: FPF_SHA "SECURITY_FTDC_FPF_SHA" #由发送方支付发起的费用，受益方支付接受的费用
    ctypedef char[129] TAddInfoType "TSecurityFtdcAddInfoType" #附加信息
    ctypedef char[36] TDigestType "TSecurityFtdcDigestType" #摘要
    ctypedef char TBankAccTypeType "TSecurityFtdcBankAccTypeType" #银行帐号类型
    enum: BAT_BankBook "SECURITY_FTDC_BAT_BankBook" #银行存折
    enum: BAT_SavingCard "SECURITY_FTDC_BAT_SavingCard" #储蓄卡
    enum: BAT_CreditCard "SECURITY_FTDC_BAT_CreditCard" #信用卡
    ctypedef char[3] TDeviceIDType "TSecurityFtdcDeviceIDType" #渠道标志
    ctypedef char TPwdFlagType "TSecurityFtdcPwdFlagType" #密码核对标志
    enum: BPWDF_NoCheck "SECURITY_FTDC_BPWDF_NoCheck" #不核对
    enum: BPWDF_BlankCheck "SECURITY_FTDC_BPWDF_BlankCheck" #明文核对
    enum: BPWDF_EncryptCheck "SECURITY_FTDC_BPWDF_EncryptCheck" #密文核对
    ctypedef char[33] TBankCodingForBrokerType "TSecurityFtdcBankCodingForBrokerType" #银行对经纪公司的编码
    ctypedef char[17] TOperNoType "TSecurityFtdcOperNoType" #交易柜员
    ctypedef int TTIDType "TSecurityFtdcTIDType" #交易ID
    ctypedef char TTransferStatusType "TSecurityFtdcTransferStatusType" #转账交易状态
    enum: TRFS_Normal "SECURITY_FTDC_TRFS_Normal" #正常
    enum: TRFS_Repealed "SECURITY_FTDC_TRFS_Repealed" #被冲正
    ctypedef int TPlateSerialType "TSecurityFtdcPlateSerialType" #平台流水号
    ctypedef char TAvailabilityFlagType "TSecurityFtdcAvailabilityFlagType" #有效标志
    enum: AVAF_Invalid "SECURITY_FTDC_AVAF_Invalid" #未确认
    enum: AVAF_Valid "SECURITY_FTDC_AVAF_Valid" #有效
    enum: AVAF_Repeal "SECURITY_FTDC_AVAF_Repeal" #冲正
    ctypedef char[17] TOperatorCodeType "TSecurityFtdcOperatorCodeType" #操作员
    ctypedef char TRepayStockAlgoType "TSecurityFtdcRepayStockAlgoType" #买券还券算法
    enum: RSA_Original "SECURITY_FTDC_RSA_Original" #默认算法
    enum: RSA_Ratio "SECURITY_FTDC_RSA_Ratio" #按还券比例计算
    enum: RSA_Min "SECURITY_FTDC_RSA_Min" #Min[1,2]
    ctypedef char TTradeSpanType "TSecurityFtdcTradeSpanType" #交易时间段类型
    enum: TS_Common "SECURITY_FTDC_TS_Common" #普通业务
    enum: TS_Options "SECURITY_FTDC_TS_Options" #个股期权
