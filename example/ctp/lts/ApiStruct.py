# -*- coding: utf-8 -*-

from __future__ import absolute_import as _init

T = {}
T['TE_RESUME'] = 'int' #流重传方式
TERT_RESTART = 0 #从本交易日开始重传
TERT_RESUME = 1 #从上次收到的续传
TERT_QUICK = 2 #只传送登录后的流内容
T['ErrorID'] = 'int' #错误代码
T['ErrorMsg'] = 'char[81]' #错误信息
T['ExchangeID'] = 'char[9]' #交易所代码
T['ExchangeName'] = 'char[31]' #交易所名称
T['ExchangeProperty'] = 'char' #交易所属性
EXP_Normal = '0' #正常
EXP_GenOrderByTrade = '1' #根据成交生成报单
T['ExchangeConnectStatus'] = 'char' #交易所连接状态
ECS_NoConnection = '1' #没有任何连接
ECS_QryInstrumentSent = '2' #已经发出合约查询请求
ECS_GotInformation = '9' #已经获取信息
T['Date'] = 'char[9]' #日期
T['Time'] = 'char[9]' #时间
T['InstrumentID'] = 'char[31]' #合约代码
T['ProductName'] = 'char[21]' #产品名称
T['ProductClass'] = 'char' #产品类型
PC_Futures = '1' #期货
PC_Options = '2' #期权
PC_Combination = '3' #组合
PC_Spot = '4' #即期
PC_EFP = '5' #期转现
PC_StockA = '6' #证券A股
PC_StockB = '7' #证券B股
PC_ETF = '8' #ETF
PC_ETFPurRed = '9' #ETF申赎
T['VolumeMultiple'] = 'int' #合约数量乘数
T['Price'] = 'double' #价格
T['Volume'] = 'int' #数量
T['PositionType'] = 'char' #持仓类型
PT_Net = '1' #净持仓
PT_Gross = '2' #综合持仓
T['PositionDateType'] = 'char' #持仓日期类型
PDT_UseHistory = '1' #使用历史持仓
PDT_NoUseHistory = '2' #不使用历史持仓
T['ExchangeInstID'] = 'char[31]' #合约在交易所的代码
T['Year'] = 'int' #年份
T['Month'] = 'int' #月份
T['InstLifePhase'] = 'char' #合约生命周期状态
IP_NotStart = '0' #未上市
IP_Started = '1' #上市
IP_Pause = '2' #停牌
IP_Expired = '3' #到期
T['Bool'] = 'int' #布尔型
T['RightModelID'] = 'char[31]' #股票权限模版代码
T['RightModelName'] = 'char[161]' #股票权限模版名称
T['PosTradeType'] = 'char' #持仓交易类型
PTT_CanSelTodayPos = '1' #今日新增持仓能卖出
PTT_CannotSellTodayPos = '2' #今日新增持仓不能卖出
T['TraderID'] = 'char[21]' #交易所交易员代码
T['ParticipantID'] = 'char[11]' #会员代码
T['Password'] = 'char[41]' #密码
T['BrokerID'] = 'char[11]' #经纪公司代码
T['OrderLocalID'] = 'char[13]' #本地报单编号
T['BrokerAbbr'] = 'char[9]' #经纪公司简称
T['BrokerName'] = 'char[81]' #经纪公司名称
T['InvestorID'] = 'char[15]' #投资者代码
T['PartyName'] = 'char[81]' #参与人名称
T['IdCardType'] = 'char' #证件类型
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
ICT_TaxNo = 'A' #税务登记号
ICT_OtherCard = 'x' #其他证件
T['IdentifiedCardNo'] = 'char[51]' #证件号码
T['ClientID'] = 'char[21]' #交易编码
T['AccountID'] = 'char[15]' #投资者帐号
T['ClientType'] = 'char' #交易编码类型
CLT_Normal = '1' #普通
CLT_Credit = '2' #信用交易
CLT_Derive = '3' #衍生品账户
CLT_Other = '4' #其他类型
T['InvestorGroupName'] = 'char[41]' #投资者分组名称
T['UserID'] = 'char[16]' #用户代码
T['UserName'] = 'char[81]' #用户名称
T['FunctionCode'] = 'char' #功能代码
FC_ForceUserLogout = '2' #强制用户登出
FC_UserPasswordUpdate = '3' #变更管理用户口令
FC_BrokerPasswordUpdate = '4' #变更经纪公司口令
FC_InvestorPasswordUpdate = '5' #变更投资者口令
FC_OrderInsert = '6' #报单插入
FC_OrderAction = '7' #报单操作
FC_SyncSystemData = '8' #同步系统数据
FC_SyncBrokerData = '9' #同步经纪公司数据
FC_SuperQuery = 'B' #超级查询
FC_ParkedOrderInsert = 'C' #报单插入
FC_ParkedOrderAction = 'D' #报单操作
FC_SyncOTP = 'E' #同步动态令牌
FC_UnkownOrderAction = 'F' #未知单操作
FC_DepositoryTransfer = 'G' #转托管
FC_ExcessStockTransfer = 'H' #余券划转
T['UserType'] = 'char' #用户类型
UT_Investor = '0' #投资者
UT_Operator = '1' #操作员
UT_SuperUser = '2' #管理员
T['BrokerFunctionCode'] = 'char' #经纪公司功能代码
BFC_ForceUserLogout = '1' #强制用户登出
BFC_UserPasswordUpdate = '2' #变更用户口令
BFC_SyncBrokerData = '3' #同步经纪公司数据
BFC_OrderInsert = '5' #报单插入
BFC_OrderAction = '6' #报单操作
BFC_AllQuery = '7' #全部查询
BFC_UnkownOrderAction = '8' #未知单操作
BFC_DepositoryTransfer = '9' #转托管
BFC_ExcessStockTransfer = 'A' #余券划转
BFC_log = 'a' #系统功能：登入/登出/修改密码等
BFC_BaseQry = 'b' #基本查询：查询基础数据，如合约，交易所等常量
BFC_TradeQry = 'c' #交易查询：如查成交，委托
BFC_Trade = 'd' #交易功能：报单，撤单
BFC_Virement = 'e' #转账
BFC_Session = 'g' #查询/管理：查询会话，踢人等
BFC_SyncOTP = 'E' #同步动态令牌
T['CurrencyCode'] = 'char[4]' #币种
T['Money'] = 'double' #资金
T['Ratio'] = 'double' #比率
T['AccountType'] = 'char' #账户类型
AcT_Normal = '1' #普通账户
AcT_Credit = '2' #信用账户
AcT_Derive = '3' #衍生品账户
AcT_Other = '4' #其他类型
T['DepartmentRange'] = 'char' #投资者范围
DR_All = '1' #所有
DR_Group = '2' #组织架构
DR_Single = '3' #单一投资者
T['UserRightType'] = 'char' #客户权限类型
URT_Logon = '1' #登录
URT_Transfer = '2' #银期转帐
URT_EMail = '3' #邮寄结算单
URT_Fax = '4' #传真结算单
URT_ConditionOrder = '5' #条件单
T['ProductInfo'] = 'char[11]' #产品信息
T['AuthCode'] = 'char[17]' #客户端认证码
T['LargeVolume'] = 'double' #大额数量
T['Millisec'] = 'int' #时间（毫秒）
T['HedgeFlag'] = 'char' #投机套保标志
HF_Speculation = '1' #投机
HF_Hedge = '3' #套保
T['Direction'] = 'char' #买卖方向
D_Buy = '0' #买
D_Sell = '1' #卖
D_ETFPur = '2' #ETF申购
D_ETFRed = '3' #ETF赎回
D_CashIn = '4' #现金替代，只用作回报
D_PledgeBondIn = '5' #债券入库
D_PledgeBondOut = '6' #债券出库
D_Rationed = '7' #配股
D_DepositoryTransfer = '8' #转托管
D_CreditRationed = '9' #信用账户配股
D_BuyCollateral = 'A' #担保品买入
D_SellCollateral = 'B' #担保品卖出
D_CollateralTransferIn = 'C' #担保品转入
D_CollateralTransferOut = 'D' #担保品转出
D_MarginTrade = 'E' #融资买入
D_ShortSell = 'F' #融券卖出
D_RepayMargin = 'G' #卖券还款
D_RepayStock = 'H' #买券还券
D_DirectRepayMargin = 'I' #直接还款
D_DirectRepayStock = 'J' #直接还券
D_ExcessStockTransfer = 'K' #余券划转
T['TradeID'] = 'char[21]' #成交编号
T['TradeType'] = 'char' #成交类型
TRDT_Common = '0' #普通成交
TRDT_OptionsExecution = '1' #期权执行
TRDT_OTC = '2' #OTC成交
TRDT_EFPDerived = '3' #期转现衍生成交
TRDT_CombinationDerived = '4' #组合衍生成交
TRDT_EFTPurchase = '5' #ETF申购
TRDT_EFTRedem = '6' #ETF赎回
T['CreationredemptionStatus'] = 'char' #基金当天申购赎回状态
CDS_Forbidden = '0' #不允许申购赎回
CDS_Allow = '1' #表示允许申购和赎回
CDS_OnlyPurchase = '2' #允许申购、不允许赎回
CDS_OnlyRedeem = '3' #不允许申购、允许赎回
T['ETFCurrenceReplaceStatus'] = 'char' #ETF现金替代标志
ETFCRS_Forbidden = '0' #禁止现金替代
ETFCRS_Allow = '1' #可以现金替代
ETFCRS_Force = '2' #必须现金替代
T['Interest'] = 'double' #利息
T['RepurchaseMaxTimes'] = 'double' #正回购放大倍数
T['CapitalStockType'] = 'char' #股本类型
CPTSTOCK_TOTALSTOCK = '1' #总通股本
CPTSTOCK_CIRCULATION = '2' #流通股本
T['MarginPriceType'] = 'char' #保证金价格类型
MPT_PreSettlementPrice = '1' #昨结算价
MPT_SettlementPrice = '2' #最新价
MPT_AveragePrice = '3' #成交均价
MPT_OpenPrice = '4' #开仓价
T['Algorithm'] = 'char' #盈亏算法
AG_All = '1' #浮盈浮亏都计算
AG_OnlyLost = '2' #浮盈不计，浮亏计
AG_OnlyGain = '3' #浮盈计，浮亏不计
AG_None = '4' #浮盈浮亏都不计算
T['IncludeCloseProfit'] = 'char' #是否包含平仓盈利
ICP_Include = '0' #包含平仓盈利
ICP_NotInclude = '2' #不包含平仓盈利
T['AllWithoutTrade'] = 'char' #是否受可提比例限制
AWT_Enable = '0' #不受可提比例限制
AWT_Disable = '2' #受可提比例限制
AWT_NoHoldEnable = '3' #无仓不受可提比例限制
T['HandlePositionAlgoID'] = 'char' #持仓处理算法编号
HPA_Base = '1' #基本
HPA_NoneTrade = '4' #非交易
HPA_Stock = '5' #证券
T['TradeParamID'] = 'char' #交易系统参数代码
TPID_EncryptionStandard = 'E' #系统加密算法
TPID_SingleUserSessionMaxNum = 'S' #用户最大会话数
TPID_LoginFailMaxNum = 'L' #最大连续登录失败数
TPID_IsAuthForce = 'A' #是否强制认证
TPID_GenUserEvent = 'G' #是否生成用户事件
TPID_StartOrderLocalID = 'O' #起始报单本地编号
TPID_RepayStockAlgo = 'R' #融资融券买券还券算法
T['SettlementParamValue'] = 'char[256]' #参数代码值
T['Memo'] = 'char[161]' #备注
T['Priority'] = 'int' #优先级
T['OrderRef'] = 'char[13]' #报单引用
T['MarketID'] = 'char[31]' #市场代码
T['MacAddress'] = 'char[21]' #Mac地址
T['InstrumentName'] = 'char[21]' #合约名称
T['OrderSysID'] = 'char[21]' #报单编号
T['IPAddress'] = 'char[16]' #IP地址
T['ProtocolInfo'] = 'char[11]' #协议信息
T['DepositSeqNo'] = 'char[15]' #出入金流水号
T['SystemName'] = 'char[41]' #系统名称
T['InvestorRange'] = 'char' #投资者范围
IR_All = '1' #所有
IR_Group = '2' #投资者组
IR_Single = '3' #单一投资者
T['DataSyncStatus'] = 'char' #数据同步状态
DS_Asynchronous = '1' #未同步
DS_Synchronizing = '2' #同步中
DS_Synchronized = '3' #已同步
T['TraderConnectStatus'] = 'char' #交易所交易员连接状态
TCS_NotConnected = '1' #没有任何连接
TCS_Connected = '2' #已经连接
TCS_QryInstrumentSent = '3' #已经发出合约查询请求
TCS_SubPrivateFlow = '4' #订阅私有流
T['OrderActionStatus'] = 'char' #报单操作状态
OAS_Submitted = 'a' #已经提交
OAS_Accepted = 'b' #已经接受
OAS_Rejected = 'c' #已经被拒绝
T['OrderStatus'] = 'char' #报单状态
OST_AllTraded = '0' #全部成交
OST_PartTradedQueueing = '1' #部分成交还在队列中
OST_PartTradedNotQueueing = '2' #部分成交不在队列中
OST_NoTradeQueueing = '3' #未成交还在队列中
OST_NoTradeNotQueueing = '4' #未成交不在队列中
OST_Canceled = '5' #撤单
OST_Unknown = 'a' #未知
OST_NotTouched = 'b' #尚未触发
OST_Touched = 'c' #已触发
T['OrderSubmitStatus'] = 'char' #报单提交状态
OSS_InsertSubmitted = '0' #已经提交
OSS_CancelSubmitted = '1' #撤单已经提交
OSS_ModifySubmitted = '2' #修改已经提交
OSS_Accepted = '3' #已经接受
OSS_InsertRejected = '4' #报单已经被拒绝
OSS_CancelRejected = '5' #撤单已经被拒绝
OSS_ModifyRejected = '6' #改单已经被拒绝
T['PositionDate'] = 'char' #持仓日期
PSD_Today = '1' #今日持仓
PSD_History = '2' #历史持仓
T['TradingRole'] = 'char' #交易角色
ER_Broker = '1' #代理
ER_Host = '2' #自营
ER_Maker = '3' #做市商
T['PosiDirection'] = 'char' #持仓多空方向
PD_Net = '1' #净
PD_Long = '2' #多头
PD_Short = '3' #空头
T['OrderPriceType'] = 'char' #报单价格条件
OPT_AnyPrice = '1' #即时成交剩余撤销市价单
OPT_LimitPrice = '2' #限价
OPT_BestPrice = '3' #最优五档即时成交剩余撤销市价单
OPT_BestLimitPrice = '4' #最优五档即时成交剩余转限价市价单
OPT_AllPrice = '5' #全部成交或撤销市价单
OPT_ForwardBestPrice = '6' #本方最优价格市价单
OPT_ReverseBestPrice = '7' #对方最优价格市价单
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
T['OffsetFlag'] = 'char' #开平标志
OF_Open = '0' #开仓
OF_Close = '1' #平仓
OF_ForceClose = '2' #强平
OF_CloseToday = '3' #平今
OF_CloseYesterday = '4' #平昨
OF_ForceOff = '5' #强减
OF_LocalForceClose = '6' #本地强平
T['ForceCloseReason'] = 'char' #强平原因
FCC_NotForceClose = '0' #非强平
FCC_LackDeposit = '1' #资金不足
FCC_ClientOverPositionLimit = '2' #客户超仓
FCC_MemberOverPositionLimit = '3' #会员超仓
FCC_NotMultiple = '4' #持仓非整数倍
FCC_Violation = '5' #违规
FCC_Other = '6' #其它
FCC_PersonDeliv = '7' #自然人临近交割
T['OrderType'] = 'char' #报单类型
ORDT_Normal = '0' #正常
ORDT_DeriveFromQuote = '1' #报价衍生
ORDT_DeriveFromCombination = '2' #组合衍生
ORDT_Combination = '3' #组合报单
ORDT_ConditionalOrder = '4' #条件单
ORDT_Swap = '5' #互换单
T['TimeCondition'] = 'char' #有效期类型
TC_IOC = '1' #立即完成，否则撤销
TC_GFS = '2' #本节有效
TC_GFD = '3' #当日有效
TC_GTD = '4' #指定日期前有效
TC_GTC = '5' #撤销前有效
TC_GFA = '6' #集合竞价有效
T['VolumeCondition'] = 'char' #成交量类型
VC_AV = '1' #任何数量
VC_MV = '2' #最小数量
VC_CV = '3' #全部数量
T['ContingentCondition'] = 'char' #触发条件
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
T['ActionFlag'] = 'char' #操作标志
AF_Delete = '0' #删除
AF_Modify = '3' #修改
T['TradingRight'] = 'char' #交易权限
TR_Allow = '0' #可以交易
TR_Forbidden = '2' #不能交易
T['OrderSource'] = 'char' #报单来源
OSRC_Participant = '0' #来自参与者
OSRC_Administrator = '1' #来自管理员
T['PriceSource'] = 'char' #成交价来源
PSRC_LastPrice = '0' #前成交价
PSRC_Buy = '1' #买委托价
PSRC_Sell = '2' #卖委托价
T['OrderActionRef'] = 'int' #报单操作引用
T['FrontID'] = 'int' #前置编号
T['SessionID'] = 'int' #会话编号
T['InstallID'] = 'int' #安装编号
T['SequenceNo'] = 'int' #序号
T['RequestID'] = 'int' #请求编号
T['CombOffsetFlag'] = 'char[5]' #组合开平标志
T['CombHedgeFlag'] = 'char[5]' #组合投机套保标志
T['SequenceSeries'] = 'short' #序列系列号
T['CommPhaseNo'] = 'short' #通讯时段编号
T['UserEventType'] = 'char' #用户事件类型
UET_Login = '1' #登录
UET_Logout = '2' #登出
UET_Trading = '3' #交易成功
UET_TradingError = '4' #交易失败
UET_UpdatePassword = '5' #修改密码
UET_Authenticate = '6' #客户端认证
UET_Other = '9' #其他
T['UserEventInfo'] = 'char[1025]' #用户事件信息
T['OTPType'] = 'char' #动态令牌类型
OTP_NONE = '0' #无动态令牌
OTP_TOTP = '1' #时间令牌
T['TradeSource'] = 'char' #成交来源
TSRC_NORMAL = '0' #来自交易所普通回报
TSRC_QUERY = '1' #来自查询
T['BranchID'] = 'char[9]' #营业部编号
T['StockPrice'] = 'char[16]' #证券交易价格
T['RightModelID'] = 'char[31]' #股票权限模版代码
T['SerialNumber'] = 'char[17]' #序列号
T['InstrumentRange'] = 'char' #股票权限分类
INR_All = '1' #所有
INR_Product = '2' #产品
INR_Model = '3' #股票权限模版
INR_Stock = '4' #股票
INR_Market = '5' #市场
T['BusinessUnit'] = 'char[21]' #业务单元
T['OTPVendorsID'] = 'char[2]' #动态令牌提供商
T['LastDrift'] = 'int' #上次OTP漂移值
T['LastSuccess'] = 'int' #上次OTP成功值
T['AuthKey'] = 'char[41]' #令牌密钥
T['UserSessionHash'] = 'int' #用户会话Hash值
T['StockTradeType'] = 'char' #证券交易类型
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
T['HandleTradingAccountAlgoID'] = 'char' #资金处理算法编号
HTAA_Base = '1' #基本
T['StockWth'] = 'int' #股票使用流水号
T['StockSeq'] = 'char[11]' #股票使用流水号
T['WTFS'] = 'int' #委托方式
T['WTLB'] = 'int' #委托类别
T['WTRQ'] = 'int' #委托日期
T['INTEGER'] = 'int' #一般整型
T['INT3'] = 'int' #三位数整型
T['INT6'] = 'int' #六位数整型
T['CHAR1'] = 'char[2]' #一字节CHAR
T['CHAR2'] = 'char[3]' #二字节CHAR
T['CHAR3'] = 'char[4]' #三字节CHAR
T['CHAR4'] = 'char[5]' #四字节CHAR
T['CHAR5'] = 'char[6]' #五字节CHAR
T['CHAR6'] = 'char[7]' #六字节CHAR
T['CHAR8'] = 'char[9]' #八字节CHAR
T['CHAR10'] = 'char[11]' #十字节CHAR
T['CHAR12'] = 'char[13]' #十二字节CHAR
T['CHAR13'] = 'char[14]' #十三字节CHAR
T['CHAR14'] = 'char[15]' #十四字节CHAR
T['CHAR16'] = 'char[17]' #十六字节CHAR
T['VCHAR4'] = 'char[5]' #四字节VCHAR
T['VCHAR6'] = 'char[7]' #六字节VCHAR
T['VCHAR8'] = 'char[9]' #八字节VCHAR
T['VCHAR10'] = 'char[11]' #十字节VCHAR
T['VCHAR12'] = 'char[13]' #十二字节VCHAR
T['VCHAR16'] = 'char[17]' #十六字节VCHAR
T['VCHAR20'] = 'char[21]' #二十字节VCHAR
T['VCHAR30'] = 'char[31]' #三十字节VCHAR
T['VCHAR50'] = 'char[51]' #五十字节VCHAR
T['VCHAR60'] = 'char[61]' #六十字节VCHAR
T['VCHAR65'] = 'char[66]' #六十五字节VCHAR
T['VCHAR80'] = 'char[81]' #八十字节VCHAR
T['VCHAR255'] = 'char[256]' #二五五字节VCHAR
T['REAL9P3'] = 'double' #九点三实型
T['REAL10P4'] = 'double' #十点四实型
T['REAL16P2'] = 'double' #十六点二实型
T['REAL16P8'] = 'double' #十六点八实型
T['REAL22P2'] = 'double' #二十二点二实型
T['CommandNo'] = 'int' #DB命令序号
T['CommandType'] = 'char[65]' #DB命令类型
T['SettlementGroupID'] = 'char[9]' #结算组代码
T['FieldName'] = 'char[2049]' #字段名
T['FieldContent'] = 'char[2049]' #字段内容
T['BankID'] = 'char[4]' #银行代码
T['BankName'] = 'char[101]' #银行名称
T['BankBrchID'] = 'char[5]' #银行分中心代码
T['LiberSerial'] = 'int' #Liber系统流水号
T['RoleID'] = 'char[11]' #角色编号
T['RoleName'] = 'char[41]' #角色名称
T['Description'] = 'char[401]' #描述
T['FunctionID'] = 'char[25]' #功能代码
T['BillNo'] = 'char[15]' #票据号
T['FundIOType'] = 'char' #出入金类型
FIOT_FundIO = '1' #出入金
FIOT_Transfer = '2' #银期转帐
T['FundType'] = 'char' #资金类型
FT_Deposite = '1' #银行存款
FT_ItemFund = '2' #分项资金
FT_Company = '3' #公司调整
T['FundDirection'] = 'char' #出入金方向
FD_In = '1' #入金
FD_Out = '2' #出金
T['BankFlag'] = 'char' #银行统一标识类型
BF_ICBC = '1' #工商银行
BF_ABC = '2' #农业银行
BF_BC = '3' #中国银行
BF_CBC = '4' #建设银行
BF_BOC = '5' #交通银行
BF_Other = 'Z' #其他银行
T['OperationMemo'] = 'char[1025]' #操作摘要
T['FundStatus'] = 'char' #资金状态
FS_Record = '1' #已录入
FS_Check = '2' #已复核
FS_Charge = '3' #已冲销
T['FundProjectID'] = 'char[5]' #资金项目编号
T['OperatorID'] = 'char[65]' #操作员代码
T['CounterID'] = 'char[33]' #计数器代码
T['FunctionName'] = 'char[65]' #功能名称
T['TradeCode'] = 'char[7]' #交易代码
T['BrokerBranchID'] = 'char[31]' #经纪公司分支机构代码
T['TradeDate'] = 'char[9]' #交易日期
T['TradeTime'] = 'char[9]' #交易时间
T['BankSerial'] = 'char[13]' #银行流水号
T['Serial'] = 'int' #流水号
T['LastFragment'] = 'char' #最后分片标志
LF_Yes = '0' #是最后分片
LF_No = '1' #不是最后分片
T['IndividualName'] = 'char[51]' #个人姓名
T['CustType'] = 'char' #客户类型
CUSTT_Person = '0' #自然人
CUSTT_Institution = '1' #机构户
T['BankAccount'] = 'char[41]' #银行账户
T['YesNoIndicator'] = 'char' #是或否标识
YNI_Yes = '0' #是
YNI_No = '1' #否
T['TradeAmount'] = 'double' #交易金额（元）
T['CustFee'] = 'double' #应收客户费用（元）
T['BrokerFee'] = 'double' #应收经纪公司费用（元）
T['FeePayFlag'] = 'char' #费用支付标志
FPF_BEN = '0' #由受益方支付费用
FPF_OUR = '1' #由发送方支付费用
FPF_SHA = '2' #由发送方支付发起的费用，受益方支付接受的费用
T['AddInfo'] = 'char[129]' #附加信息
T['Digest'] = 'char[36]' #摘要
T['BankAccType'] = 'char' #银行帐号类型
BAT_BankBook = '1' #银行存折
BAT_SavingCard = '2' #储蓄卡
BAT_CreditCard = '3' #信用卡
T['DeviceID'] = 'char[3]' #渠道标志
T['PwdFlag'] = 'char' #密码核对标志
BPWDF_NoCheck = '0' #不核对
BPWDF_BlankCheck = '1' #明文核对
BPWDF_EncryptCheck = '2' #密文核对
T['BankCodingForBroker'] = 'char[33]' #银行对经纪公司的编码
T['OperNo'] = 'char[17]' #交易柜员
T['TID'] = 'int' #交易ID
T['TransferStatus'] = 'char' #转账交易状态
TRFS_Normal = '0' #正常
TRFS_Repealed = '1' #被冲正
T['PlateSerial'] = 'int' #平台流水号
T['AvailabilityFlag'] = 'char' #有效标志
AVAF_Invalid = '0' #未确认
AVAF_Valid = '1' #有效
AVAF_Repeal = '2' #冲正
T['OperatorCode'] = 'char[17]' #操作员
T['RepayStockAlgo'] = 'char' #买券还券算法
RSA_Original = '0' #默认算法
RSA_Ratio = '1' #按还券比例计算
RSA_Min = '2' #Min[1,2]
T['TradeSpan'] = 'char' #交易时间段类型
TS_Common = '1' #普通业务
TS_Options = '2' #个股期权

class BaseStruct(object):
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join('%s=%r'%(k,getattr(self,k)) for k,t in self._fields_))

class RspInfo(BaseStruct): #响应信息
    def __init__(self, ErrorID=0, ErrorMsg=''):
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class Exchange(BaseStruct): #交易所
    def __init__(self, ExchangeID='', ExchangeName='', ExchangeProperty=EXP_Normal):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ExchangeName = '' #交易所名称, char[31]
        self.ExchangeProperty = '' #交易所属性, char

class Product(BaseStruct): #产品
    def __init__(self, ProductID='', ProductName='', ExchangeID='', ProductClass=PC_Futures, VolumeMultiple=0, PriceTick=0.0, MaxMarketOrderVolume=0, MinMarketOrderVolume=0, MaxLimitOrderVolume=0, MinLimitOrderVolume=0, PositionType=PT_Net, PositionDateType=PDT_UseHistory, EFTMinTradeVolume=0):
        self.ProductID = 'InstrumentID' #产品代码, char[31]
        self.ProductName = '' #产品名称, char[21]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ProductClass = '' #产品类型, char
        self.VolumeMultiple = '' #合约数量乘数, int
        self.PriceTick = 'Price' #最小变动价位, double
        self.MaxMarketOrderVolume = 'Volume' #市价单最大下单量, int
        self.MinMarketOrderVolume = 'Volume' #市价单最小下单量, int
        self.MaxLimitOrderVolume = 'Volume' #限价单最大下单量, int
        self.MinLimitOrderVolume = 'Volume' #限价单最小下单量, int
        self.PositionType = '' #持仓类型, char
        self.PositionDateType = '' #持仓日期类型, char
        self.EFTMinTradeVolume = 'Volume' #ETF最小交易单位, int

class Instrument(BaseStruct): #合约
    def __init__(self, InstrumentID='', ExchangeID='', InstrumentName='', ExchangeInstID='', ProductID='', ProductClass=PC_Futures, DeliveryYear=0, DeliveryMonth=0, MaxMarketOrderVolume=0, MinMarketOrderVolume=0, MaxLimitOrderVolume=0, MinLimitOrderVolume=0, VolumeMultiple=0, PriceTick=0.0, CreateDate='', OpenDate='', ExpireDate='', StartDelivDate='', EndDelivDate='', InstLifePhase=IP_NotStart, IsTrading=0, PositionType=PT_Net, OrderCanBeWithdraw=0, MinBuyVolume=0, MinSellVolume=0, RightModelID='', PosTradeType=PTT_CanSelTodayPos, MarketID=''):
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentName = '' #合约名称, char[21]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.ProductID = 'InstrumentID' #产品代码, char[31]
        self.ProductClass = '' #产品类型, char
        self.DeliveryYear = 'Year' #交割年份, int
        self.DeliveryMonth = 'Month' #交割月, int
        self.MaxMarketOrderVolume = 'Volume' #市价单最大下单量, int
        self.MinMarketOrderVolume = 'Volume' #市价单最小下单量, int
        self.MaxLimitOrderVolume = 'Volume' #限价单最大下单量, int
        self.MinLimitOrderVolume = 'Volume' #限价单最小下单量, int
        self.VolumeMultiple = '' #合约数量乘数, int
        self.PriceTick = 'Price' #最小变动价位, double
        self.CreateDate = 'Date' #创建日, char[9]
        self.OpenDate = 'Date' #上市日, char[9]
        self.ExpireDate = 'Date' #到期日, char[9]
        self.StartDelivDate = 'Date' #开始交割日, char[9]
        self.EndDelivDate = 'Date' #结束交割日, char[9]
        self.InstLifePhase = '' #合约生命周期状态, char
        self.IsTrading = 'Bool' #当前是否交易, int
        self.PositionType = '' #持仓类型, char
        self.OrderCanBeWithdraw = 'Bool' #报单能否撤单, int
        self.MinBuyVolume = 'Volume' #最小买下单单位, int
        self.MinSellVolume = 'Volume' #最小卖下单单位, int
        self.RightModelID = '' #股票权限模版代码, char[31]
        self.PosTradeType = '' #持仓交易类型, char
        self.MarketID = 'InstrumentID' #市场代码, char[31]

class Broker(BaseStruct): #经纪公司
    def __init__(self, BrokerID='', BrokerAbbr='', BrokerName='', IsActive=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.BrokerAbbr = '' #经纪公司简称, char[9]
        self.BrokerName = '' #经纪公司名称, char[81]
        self.IsActive = 'Bool' #是否活跃, int

class PartBroker(BaseStruct): #会员编码和经纪公司编码对照表
    def __init__(self, BrokerID='', ExchangeID='', ParticipantID='', IsActive=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ParticipantID = '' #会员代码, char[11]
        self.IsActive = 'Bool' #是否活跃, int

class Investor(BaseStruct): #投资者
    def __init__(self, InvestorID='', BrokerID='', InvestorGroupID='', InvestorName='', IdentifiedCardType=ICT_EID, IdentifiedCardNo='', IsActive=0, SHBranchID='', SZBranchID=''):
        self.InvestorID = '' #投资者代码, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorGroupID = 'InvestorID' #投资者分组代码, char[15]
        self.InvestorName = 'PartyName' #投资者名称, char[81]
        self.IdentifiedCardType = 'IdCardType' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.IsActive = 'Bool' #是否活跃, int
        self.SHBranchID = 'TraderID' #上海营业部编号, char[21]
        self.SZBranchID = 'TraderID' #深圳营业部编号, char[21]

class TradingCode(BaseStruct): #交易编码
    def __init__(self, InvestorID='', BrokerID='', ExchangeID='', ClientID='', IsActive=0, AccountID='', PBU='', ClientType=CLT_Normal):
        self.InvestorID = '' #投资者代码, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ClientID = '' #客户代码, char[21]
        self.IsActive = 'Bool' #是否活跃, int
        self.AccountID = '' #AccountID, char[15]
        self.PBU = 'TraderID' #交易单元号, char[21]
        self.ClientType = '' #ClientType, char

class SuperUser(BaseStruct): #管理用户
    def __init__(self, UserID='', UserName='', Password='', IsActive=0):
        self.UserID = '' #用户代码, char[16]
        self.UserName = '' #用户名称, char[81]
        self.Password = '' #密码, char[41]
        self.IsActive = 'Bool' #是否活跃, int

class SuperUserFunction(BaseStruct): #管理用户功能权限
    def __init__(self, UserID='', FunctionCode=FC_ForceUserLogout):
        self.UserID = '' #用户代码, char[16]
        self.FunctionCode = '' #功能代码, char

class BrokerUser(BaseStruct): #经纪公司用户
    def __init__(self, BrokerID='', UserID='', UserName='', UserType=UT_Investor, IsActive=0, IsUsingOTP=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserName = '' #用户名称, char[81]
        self.UserType = '' #用户类型, char
        self.IsActive = 'Bool' #是否活跃, int
        self.IsUsingOTP = 'Bool' #是否使用令牌, int

class BrokerUserFunction(BaseStruct): #经纪公司用户功能权限
    def __init__(self, BrokerID='', UserID='', BrokerFunctionCode=BFC_ForceUserLogout):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.BrokerFunctionCode = '' #经纪公司功能代码, char

class TradingAccount(BaseStruct): #资金账户
    def __init__(self, BrokerID='', AccountID='', PreMortgage=0.0, PreCredit=0.0, PreDeposit=0.0, PreBalance=0.0, PreMargin=0.0, InterestBase=0.0, Interest=0.0, Deposit=0.0, Withdraw=0.0, FrozenMargin=0.0, FrozenCash=0.0, FrozenCommission=0.0, CurrMargin=0.0, CashIn=0.0, Commission=0.0, Balance=0.0, Available=0.0, WithdrawQuota=0.0, Reserve=0.0, TradingDay='', Credit=0.0, Mortgage=0.0, ExchangeMargin=0.0, DeliveryMargin=0.0, ExchangeDeliveryMargin=0.0, FrozenTransferFee=0.0, FrozenStampTax=0.0, TransferFee=0.0, StampTax=0.0, ConversionAmount=0.0, CreditAmount=0.0, StockValue=0.0, BondRepurchaseAmount=0.0, ReverseRepurchaseAmount=0.0, CurrencyCode='', AccountType=AcT_Normal, MarginTradeAmount=0.0, ShortSellAmount=0.0, MarginTradeProfit=0.0, ShortSellProfit=0.0, SSStockValue=0.0, CreditRatio=0.0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.AccountID = '' #投资者帐号, char[15]
        self.PreMortgage = 'Money' #上次质押金额, double
        self.PreCredit = 'Money' #上次信用额度, double
        self.PreDeposit = 'Money' #上次存款额, double
        self.PreBalance = 'Money' #上次结算准备金, double
        self.PreMargin = 'Money' #上次占用的保证金, double
        self.InterestBase = 'Money' #利息基数, double
        self.Interest = 'Money' #利息收入, double
        self.Deposit = 'Money' #入金金额, double
        self.Withdraw = 'Money' #出金金额, double
        self.FrozenMargin = 'Money' #冻结的保证金, double
        self.FrozenCash = 'Money' #冻结的资金, double
        self.FrozenCommission = 'Money' #冻结的手续费, double
        self.CurrMargin = 'Money' #当前保证金总额, double
        self.CashIn = 'Money' #资金差额, double
        self.Commission = 'Money' #手续费, double
        self.Balance = 'Money' #结算准备金, double
        self.Available = 'Money' #现金, double
        self.WithdrawQuota = 'Money' #可取资金, double
        self.Reserve = 'Money' #基本准备金, double
        self.TradingDay = 'Date' #交易日, char[9]
        self.Credit = 'Money' #保证金可用余额, double
        self.Mortgage = 'Money' #质押金额, double
        self.ExchangeMargin = 'Money' #交易所保证金, double
        self.DeliveryMargin = 'Money' #投资者交割保证金, double
        self.ExchangeDeliveryMargin = 'Money' #交易所交割保证金, double
        self.FrozenTransferFee = 'Money' #冻结的过户费, double
        self.FrozenStampTax = 'Money' #冻结的印花税, double
        self.TransferFee = 'Money' #过户费, double
        self.StampTax = 'Money' #印花税, double
        self.ConversionAmount = 'Money' #折算金额, double
        self.CreditAmount = 'Money' #授信额度, double
        self.StockValue = 'Money' #证券总价值, double
        self.BondRepurchaseAmount = 'Money' #国债回购占用资金, double
        self.ReverseRepurchaseAmount = 'Money' #国债逆回购占用资金, double
        self.CurrencyCode = '' #币种, char[4]
        self.AccountType = '' #账户类型, char
        self.MarginTradeAmount = 'Money' #融资买入金额, double
        self.ShortSellAmount = 'Money' #融券卖出金额, double
        self.MarginTradeProfit = 'Money' #融资持仓盈亏, double
        self.ShortSellProfit = 'Money' #融券持仓盈亏, double
        self.SSStockValue = 'Money' #融券总市值, double
        self.CreditRatio = 'Ratio' #维持担保比例, double

class LoginForbiddenUser(BaseStruct): #禁止登录用户
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class DepthMarketData(BaseStruct): #深度行情
    def __init__(self, TradingDay='', InstrumentID='', ExchangeID='', ExchangeInstID='', LastPrice=0.0, PreSettlementPrice=0.0, PreClosePrice=0.0, PreOpenInterest=0.0, OpenPrice=0.0, HighestPrice=0.0, LowestPrice=0.0, Volume=0, Turnover=0.0, OpenInterest=0.0, ClosePrice=0.0, SettlementPrice=0.0, UpperLimitPrice=0.0, LowerLimitPrice=0.0, PreDelta=0.0, CurrDelta=0.0, UpdateTime='', UpdateMillisec=0, BidPrice1=0.0, BidVolume1=0, AskPrice1=0.0, AskVolume1=0, BidPrice2=0.0, BidVolume2=0, AskPrice2=0.0, AskVolume2=0, BidPrice3=0.0, BidVolume3=0, AskPrice3=0.0, AskVolume3=0, BidPrice4=0.0, BidVolume4=0, AskPrice4=0.0, AskVolume4=0, BidPrice5=0.0, BidVolume5=0, AskPrice5=0.0, AskVolume5=0, AveragePrice=0.0, ActionDay=''):
        self.TradingDay = 'Date' #交易日, char[9]
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.LastPrice = 'Price' #最新价, double
        self.PreSettlementPrice = 'Price' #上次结算价, double
        self.PreClosePrice = 'Price' #昨收盘, double
        self.PreOpenInterest = 'LargeVolume' #昨持仓量, double
        self.OpenPrice = 'Price' #今开盘, double
        self.HighestPrice = 'Price' #最高价, double
        self.LowestPrice = 'Price' #最低价, double
        self.Volume = '' #数量, int
        self.Turnover = 'Money' #成交金额, double
        self.OpenInterest = 'LargeVolume' #持仓量, double
        self.ClosePrice = 'Price' #今收盘, double
        self.SettlementPrice = 'Price' #本次结算价, double
        self.UpperLimitPrice = 'Price' #涨停板价, double
        self.LowerLimitPrice = 'Price' #跌停板价, double
        self.PreDelta = 'Ratio' #昨虚实度, double
        self.CurrDelta = 'Ratio' #今虚实度, double
        self.UpdateTime = 'Time' #最后修改时间, char[9]
        self.UpdateMillisec = 'Millisec' #最后修改毫秒, int
        self.BidPrice1 = 'Price' #申买价一, double
        self.BidVolume1 = 'Volume' #申买量一, int
        self.AskPrice1 = 'Price' #申卖价一, double
        self.AskVolume1 = 'Volume' #申卖量一, int
        self.BidPrice2 = 'Price' #申买价二, double
        self.BidVolume2 = 'Volume' #申买量二, int
        self.AskPrice2 = 'Price' #申卖价二, double
        self.AskVolume2 = 'Volume' #申卖量二, int
        self.BidPrice3 = 'Price' #申买价三, double
        self.BidVolume3 = 'Volume' #申买量三, int
        self.AskPrice3 = 'Price' #申卖价三, double
        self.AskVolume3 = 'Volume' #申卖量三, int
        self.BidPrice4 = 'Price' #申买价四, double
        self.BidVolume4 = 'Volume' #申买量四, int
        self.AskPrice4 = 'Price' #申卖价四, double
        self.AskVolume4 = 'Volume' #申卖量四, int
        self.BidPrice5 = 'Price' #申买价五, double
        self.BidVolume5 = 'Volume' #申买量五, int
        self.AskPrice5 = 'Price' #申卖价五, double
        self.AskVolume5 = 'Volume' #申卖量五, int
        self.AveragePrice = 'Price' #当日均价, double
        self.ActionDay = 'Date' #业务日期, char[9]

class InstrumentTradingRight(BaseStruct): #投资者合约交易权限
    def __init__(self, InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', Direction=D_Buy, TradingRight=TR_Allow, ExchangeID='', InstrumentRange=INR_All):
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.Direction = '' #买卖, char
        self.TradingRight = '' #交易权限, char
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentRange = '' #股票权限分类, char

class InvestorPositionDetail(BaseStruct): #投资者持仓明细
    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', HedgeFlag=HF_Speculation, Direction=D_Buy, OpenDate='', TradeID='', Volume=0, OpenPrice=0.0, TradingDay='', TradeType=TRDT_Common, ExchangeID='', Margin=0.0, ExchMargin=0.0, LastSettlementPrice=0.0, SettlementPrice=0.0, CloseVolume=0, CloseAmount=0.0, TransferFee=0.0, StampTax=0.0, Commission=0.0, AccountID='', PledgeInPosition=0, PledgeInFrozenPosition=0, RepurchasePosition=0, Amount=0.0):
        self.InstrumentID = '' #合约代码, char[31]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.HedgeFlag = '' #投机套保标志, char
        self.Direction = '' #买卖, char
        self.OpenDate = 'Date' #开仓日期, char[9]
        self.TradeID = '' #成交编号, char[21]
        self.Volume = '' #数量, int
        self.OpenPrice = 'Price' #开仓价, double
        self.TradingDay = 'Date' #交易日, char[9]
        self.TradeType = '' #成交类型, char
        self.ExchangeID = '' #交易所代码, char[9]
        self.Margin = 'Money' #投资者保证金, double
        self.ExchMargin = 'Money' #交易所保证金, double
        self.LastSettlementPrice = 'Price' #昨结算价, double
        self.SettlementPrice = 'Price' #结算价, double
        self.CloseVolume = 'Volume' #平仓量, int
        self.CloseAmount = 'Money' #平仓金额, double
        self.TransferFee = 'Money' #过户费, double
        self.StampTax = 'Money' #印花税, double
        self.Commission = 'Money' #手续费, double
        self.AccountID = '' #AccountID, char[15]
        self.PledgeInPosition = 'Volume' #质押入库数量, int
        self.PledgeInFrozenPosition = 'Volume' #质押入库冻结数量, int
        self.RepurchasePosition = 'Volume' #正回购使用的标准券数量, int
        self.Amount = 'Money' #融资融券金额, double

class BondInterest(BaseStruct): #债券利息
    def __init__(self, TradingDay='', ExchangeID='', InstrumentID='', Interest=0.0):
        self.TradingDay = 'Date' #交易日, char[9]
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentID = '' #合约代码, char[31]
        self.Interest = '' #利息, double

class MarketRationInfo(BaseStruct): #市值配售信息
    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', RationVolume=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ExchangeID = '' #交易所代码, char[9]
        self.RationVolume = 'Volume' #可配售手数, int

class InstrumentCommissionRate(BaseStruct): #合约手续费率
    def __init__(self, ExchangeID='', InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', Direction=D_Buy, StampTaxRateByMoney=0.0, StampTaxRateByVolume=0.0, TransferFeeRateByMoney=0.0, TransferFeeRateByVolume=0.0, TradeFeeByMoney=0.0, TradeFeeByVolume=0.0, MarginByMoney=0.0, MinTradeFee=0.0):
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.Direction = '' #买卖方向, char
        self.StampTaxRateByMoney = 'Ratio' #印花税率, double
        self.StampTaxRateByVolume = 'Ratio' #印花税率(按手数), double
        self.TransferFeeRateByMoney = 'Ratio' #过户费率, double
        self.TransferFeeRateByVolume = 'Ratio' #过户费率(按手数), double
        self.TradeFeeByMoney = 'Ratio' #交易费, double
        self.TradeFeeByVolume = 'Ratio' #交易费(按手数), double
        self.MarginByMoney = 'Ratio' #交易附加费率, double
        self.MinTradeFee = 'Price' #最小过户费, double

class ExcessStockInfo(BaseStruct): #余券信息
    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', InstrumentID='', ExcessVolume=0, ExcessFrozenVolume=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentID = '' #合约代码, char[31]
        self.ExcessVolume = 'Volume' #余券数量, int
        self.ExcessFrozenVolume = 'Volume' #余券冻结数量, int

class TraderOffer(BaseStruct): #交易所交易员报盘机
    def __init__(self, ExchangeID='', BranchPBU='', ParticipantID='', Password='', InstallID=0, OrderLocalID='', TraderConnectStatus=TCS_NotConnected, ConnectRequestDate='', ConnectRequestTime='', LastReportDate='', LastReportTime='', ConnectDate='', ConnectTime='', StartDate='', StartTime='', TradingDay='', BrokerID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]
        self.ParticipantID = '' #会员代码, char[11]
        self.Password = '' #密码, char[41]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.TraderConnectStatus = '' #交易所交易员连接状态, char
        self.ConnectRequestDate = 'Date' #发出连接请求的日期, char[9]
        self.ConnectRequestTime = 'Time' #发出连接请求的时间, char[9]
        self.LastReportDate = 'Date' #上次报告日期, char[9]
        self.LastReportTime = 'Time' #上次报告时间, char[9]
        self.ConnectDate = 'Date' #完成连接日期, char[9]
        self.ConnectTime = 'Time' #完成连接时间, char[9]
        self.StartDate = 'Date' #启动日期, char[9]
        self.StartTime = 'Time' #启动时间, char[9]
        self.TradingDay = 'Date' #交易日, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]

class MDTraderOffer(BaseStruct): #交易所行情报盘机
    def __init__(self, ExchangeID='', BranchPBU='', ParticipantID='', Password='', InstallID=0, OrderLocalID='', TraderConnectStatus=TCS_NotConnected, ConnectRequestDate='', ConnectRequestTime='', LastReportDate='', LastReportTime='', ConnectDate='', ConnectTime='', StartDate='', StartTime='', TradingDay='', BrokerID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]
        self.ParticipantID = '' #会员代码, char[11]
        self.Password = '' #密码, char[41]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.TraderConnectStatus = '' #交易所交易员连接状态, char
        self.ConnectRequestDate = 'Date' #发出连接请求的日期, char[9]
        self.ConnectRequestTime = 'Time' #发出连接请求的时间, char[9]
        self.LastReportDate = 'Date' #上次报告日期, char[9]
        self.LastReportTime = 'Time' #上次报告时间, char[9]
        self.ConnectDate = 'Date' #完成连接日期, char[9]
        self.ConnectTime = 'Time' #完成连接时间, char[9]
        self.StartDate = 'Date' #启动日期, char[9]
        self.StartTime = 'Time' #启动时间, char[9]
        self.TradingDay = 'Date' #交易日, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]

class FrontStatus(BaseStruct): #前置状态
    def __init__(self, FrontID=0, LastReportDate='', LastReportTime='', IsActive=0):
        self.FrontID = '' #前置编号, int
        self.LastReportDate = 'Date' #上次报告日期, char[9]
        self.LastReportTime = 'Time' #上次报告时间, char[9]
        self.IsActive = 'Bool' #是否活跃, int

class UserSession(BaseStruct): #用户会话
    def __init__(self, FrontID=0, SessionID=0, BrokerID='', UserID='', LoginDate='', LoginTime='', IPAddress='', UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', MacAddress=''):
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.LoginDate = 'Date' #登录日期, char[9]
        self.LoginTime = 'Time' #登录时间, char[9]
        self.IPAddress = '' #IP地址, char[16]
        self.UserProductInfo = 'ProductInfo' #用户端产品信息, char[11]
        self.InterfaceProductInfo = 'ProductInfo' #接口端产品信息, char[11]
        self.ProtocolInfo = '' #协议信息, char[11]
        self.MacAddress = '' #Mac地址, char[21]

class Order(BaseStruct): #报单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', OrderPriceType=OPT_AnyPrice, Direction=D_Buy, CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal=0, TimeCondition=TC_IOC, GTDDate='', VolumeCondition=VC_AV, MinVolume=0, ContingentCondition=CC_Immediately, StopPrice=0.0, ForceCloseReason=FCC_NotForceClose, IsAutoSuspend=0, BusinessUnit='', RequestID=0, OrderLocalID='', ParticipantID='', ClientID='', ExchangeInstID='', BranchPBU='', InstallID=0, OrderSubmitStatus=OSS_InsertSubmitted, AccountID='', NotifySequence=0, TradingDay='', OrderSysID='', OrderSource=OSRC_Participant, OrderStatus=OST_AllTraded, OrderType=ORDT_Normal, VolumeTraded=0, VolumeTotal=0, InsertDate='', InsertTime='', ActiveTime='', SuspendTime='', UpdateTime='', CancelTime='', ActiveTraderID='', ClearingPartID='', SequenceNo=0, FrontID=0, SessionID=0, UserProductInfo='', StatusMsg='', UserForceClose=0, ActiveUserID='', BrokerOrderSeq=0, RelativeOrderSysID='', BranchID='', TradeAmount=0.0, IsETF=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.OrderRef = '' #报单引用, char[13]
        self.UserID = '' #用户代码, char[16]
        self.ExchangeID = '' #交易所代码, char[9]
        self.OrderPriceType = '' #报单价格条件, char
        self.Direction = '' #买卖方向, char
        self.CombOffsetFlag = '' #组合开平标志, char[5]
        self.CombHedgeFlag = '' #组合投机套保标志, char[5]
        self.LimitPrice = 'StockPrice' #价格, char[16]
        self.VolumeTotalOriginal = 'Volume' #数量, int
        self.TimeCondition = '' #有效期类型, char
        self.GTDDate = 'Date' #GTD日期, char[9]
        self.VolumeCondition = '' #成交量类型, char
        self.MinVolume = 'Volume' #最小成交量, int
        self.ContingentCondition = '' #触发条件, char
        self.StopPrice = 'Price' #止损价, double
        self.ForceCloseReason = '' #强平原因, char
        self.IsAutoSuspend = 'Bool' #自动挂起标志, int
        self.BusinessUnit = '' #业务单元, char[21]
        self.RequestID = '' #请求编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[21]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderSubmitStatus = '' #报单提交状态, char
        self.AccountID = '' #账户代码, char[15]
        self.NotifySequence = 'SequenceNo' #报单提示序号, int
        self.TradingDay = 'Date' #交易日, char[9]
        self.OrderSysID = '' #报单编号, char[21]
        self.OrderSource = '' #报单来源, char
        self.OrderStatus = '' #报单状态, char
        self.OrderType = '' #报单类型, char
        self.VolumeTraded = 'Volume' #今成交数量, int
        self.VolumeTotal = 'Volume' #剩余数量, int
        self.InsertDate = 'Date' #报单日期, char[9]
        self.InsertTime = 'Time' #委托时间, char[9]
        self.ActiveTime = 'Time' #激活时间, char[9]
        self.SuspendTime = 'Time' #挂起时间, char[9]
        self.UpdateTime = 'Time' #最后修改时间, char[9]
        self.CancelTime = 'Time' #撤销时间, char[9]
        self.ActiveTraderID = 'TraderID' #最后修改交易所交易员代码, char[21]
        self.ClearingPartID = 'ParticipantID' #结算会员编号, char[11]
        self.SequenceNo = '' #序号, int
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.UserProductInfo = 'ProductInfo' #用户端产品信息, char[11]
        self.StatusMsg = 'ErrorMsg' #状态信息, char[81]
        self.UserForceClose = 'Bool' #用户强评标志, int
        self.ActiveUserID = 'UserID' #操作用户代码, char[16]
        self.BrokerOrderSeq = 'SequenceNo' #经纪公司报单编号, int
        self.RelativeOrderSysID = 'OrderSysID' #相关报单, char[21]
        self.BranchID = '' #营业部编号, char[9]
        self.TradeAmount = 'Money' #成交数量, double
        self.IsETF = 'Bool' #是否ETF, int

class OrderAction(BaseStruct): #报单操作
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef=0, OrderRef='', RequestID=0, FrontID=0, SessionID=0, ExchangeID='', ActionFlag=AF_Delete, LimitPrice=0.0, VolumeChange=0, ActionDate='', ActionTime='', BranchPBU='', InstallID=0, OrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus=OAS_Submitted, UserID='', BranchID='', StatusMsg='', InstrumentID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.OrderActionRef = '' #报单操作引用, int
        self.OrderRef = '' #报单引用, char[13]
        self.RequestID = '' #请求编号, int
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.ExchangeID = '' #交易所代码, char[9]
        self.ActionFlag = '' #操作标志, char
        self.LimitPrice = 'Price' #价格, double
        self.VolumeChange = 'Volume' #数量变化, int
        self.ActionDate = 'Date' #操作日期, char[9]
        self.ActionTime = 'Time' #操作时间, char[9]
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ActionLocalID = 'OrderLocalID' #操作本地编号, char[13]
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[21]
        self.BusinessUnit = '' #业务单元, char[21]
        self.OrderActionStatus = '' #报单操作状态, char
        self.UserID = '' #用户代码, char[16]
        self.BranchID = '' #营业部编号, char[9]
        self.StatusMsg = 'ErrorMsg' #状态信息, char[81]
        self.InstrumentID = '' #合约代码, char[31]

class ErrOrder(BaseStruct): #错误报单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', OrderPriceType=OPT_AnyPrice, Direction=D_Buy, CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal=0, TimeCondition=TC_IOC, GTDDate='', VolumeCondition=VC_AV, MinVolume=0, ContingentCondition=CC_Immediately, StopPrice=0.0, ForceCloseReason=FCC_NotForceClose, IsAutoSuspend=0, BusinessUnit='', RequestID=0, UserForceClose=0, ErrorID=0, ErrorMsg=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.OrderRef = '' #报单引用, char[13]
        self.UserID = '' #用户代码, char[16]
        self.ExchangeID = '' #交易所代码, char[9]
        self.OrderPriceType = '' #报单价格条件, char
        self.Direction = '' #买卖方向, char
        self.CombOffsetFlag = '' #组合开平标志, char[5]
        self.CombHedgeFlag = '' #组合投机套保标志, char[5]
        self.LimitPrice = 'StockPrice' #价格, char[16]
        self.VolumeTotalOriginal = 'Volume' #数量, int
        self.TimeCondition = '' #有效期类型, char
        self.GTDDate = 'Date' #GTD日期, char[9]
        self.VolumeCondition = '' #成交量类型, char
        self.MinVolume = 'Volume' #最小成交量, int
        self.ContingentCondition = '' #触发条件, char
        self.StopPrice = 'Price' #止损价, double
        self.ForceCloseReason = '' #强平原因, char
        self.IsAutoSuspend = 'Bool' #自动挂起标志, int
        self.BusinessUnit = '' #业务单元, char[21]
        self.RequestID = '' #请求编号, int
        self.UserForceClose = 'Bool' #用户强评标志, int
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class ErrOrderAction(BaseStruct): #错误报单操作
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef=0, OrderRef='', RequestID=0, FrontID=0, SessionID=0, ExchangeID='', ActionFlag=AF_Delete, LimitPrice=0.0, VolumeChange=0, ActionDate='', ActionTime='', BranchPBU='', InstallID=0, OrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus=OAS_Submitted, UserID='', BranchID='', StatusMsg='', InstrumentID='', ErrorID=0, ErrorMsg=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.OrderActionRef = '' #报单操作引用, int
        self.OrderRef = '' #报单引用, char[13]
        self.RequestID = '' #请求编号, int
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.ExchangeID = '' #交易所代码, char[9]
        self.ActionFlag = '' #操作标志, char
        self.LimitPrice = 'Price' #价格, double
        self.VolumeChange = 'Volume' #数量变化, int
        self.ActionDate = 'Date' #操作日期, char[9]
        self.ActionTime = 'Time' #操作时间, char[9]
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ActionLocalID = 'OrderLocalID' #操作本地编号, char[13]
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[21]
        self.BusinessUnit = '' #业务单元, char[21]
        self.OrderActionStatus = '' #报单操作状态, char
        self.UserID = '' #用户代码, char[16]
        self.BranchID = '' #营业部编号, char[9]
        self.StatusMsg = 'ErrorMsg' #状态信息, char[81]
        self.InstrumentID = '' #合约代码, char[31]
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class Trade(BaseStruct): #成交
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', TradeID='', Direction=D_Buy, OrderSysID='', ParticipantID='', ClientID='', TradingRole=ER_Broker, ExchangeInstID='', OffsetFlag=OF_Open, HedgeFlag=HF_Speculation, Price='', Volume=0, TradeDate='', TradeTime='', TradeType=TRDT_Common, PriceSource=PSRC_LastPrice, BranchPBU='', OrderLocalID='', ClearingPartID='', BusinessUnit='', SequenceNo=0, TradeSource=TSRC_NORMAL, TradingDay='', BrokerOrderSeq=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.OrderRef = '' #报单引用, char[13]
        self.UserID = '' #用户代码, char[16]
        self.ExchangeID = '' #交易所代码, char[9]
        self.TradeID = '' #成交编号, char[21]
        self.Direction = '' #买卖方向, char
        self.OrderSysID = '' #报单编号, char[21]
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[21]
        self.TradingRole = '' #交易角色, char
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.OffsetFlag = '' #开平标志, char
        self.HedgeFlag = '' #投机套保标志, char
        self.Price = 'StockPrice' #价格, char[16]
        self.Volume = '' #数量, int
        self.TradeDate = 'Date' #成交时期, char[9]
        self.TradeTime = 'Time' #成交时间, char[9]
        self.TradeType = '' #成交类型, char
        self.PriceSource = '' #成交价来源, char
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ClearingPartID = 'ParticipantID' #结算会员编号, char[11]
        self.BusinessUnit = '' #业务单元, char[21]
        self.SequenceNo = '' #序号, int
        self.TradeSource = '' #成交来源, char
        self.TradingDay = 'Date' #交易日, char[9]
        self.BrokerOrderSeq = 'SequenceNo' #经纪公司报单编号, int

class InvestorPosition(BaseStruct): #投资者持仓
    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', PosiDirection=PD_Net, HedgeFlag=HF_Speculation, PositionDate=PSD_Today, YdPosition=0, Position=0, LongFrozen=0, ShortFrozen=0, LongFrozenAmount=0.0, ShortFrozenAmount=0.0, OpenVolume=0, CloseVolume=0, OpenAmount=0.0, CloseAmount=0.0, PositionCost=0.0, FrozenCash=0.0, CashIn=0.0, Commission=0.0, PreSettlementPrice=0.0, SettlementPrice=0.0, TradingDay='', OpenCost=0.0, ExchangeMargin=0.0, TodayPosition=0, TransferFee=0.0, StampTax=0.0, TodayPurRedVolume=0, ConversionRate=0.0, ConversionAmount=0.0, StockValue=0.0, ExchangeID='', AccountID='', PledgeInPosition=0, RepurchasePosition=0, PurRedShortFrozen=0, MarginTradeVolume=0, MarginTradeAmount=0.0, MarginTradeFrozenVolume=0, MarginTradeFrozenAmount=0.0, MarginTradeConversionProfit=0.0, ShortSellVolume=0, ShortSellAmount=0.0, ShortSellFrozenVolume=0, ShortSellFrozenAmount=0.0, ShortSellConversionProfit=0.0, SSStockValue=0.0, TodayMTPosition=0, TodaySSPosition=0, YdOpenCost=0.0):
        self.InstrumentID = '' #合约代码, char[31]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.PosiDirection = '' #持仓多空方向, char
        self.HedgeFlag = '' #投机套保标志, char
        self.PositionDate = '' #持仓日期, char
        self.YdPosition = 'Volume' #上日持仓, int
        self.Position = 'Volume' #今日持仓, int
        self.LongFrozen = 'Volume' #多头冻结, int
        self.ShortFrozen = 'Volume' #空头冻结, int
        self.LongFrozenAmount = 'Money' #开仓冻结金额, double
        self.ShortFrozenAmount = 'Money' #开仓冻结金额, double
        self.OpenVolume = 'Volume' #开仓量, int
        self.CloseVolume = 'Volume' #平仓量, int
        self.OpenAmount = 'Money' #开仓金额, double
        self.CloseAmount = 'Money' #平仓金额, double
        self.PositionCost = 'Money' #持仓成本, double
        self.FrozenCash = 'Money' #冻结的资金, double
        self.CashIn = 'Money' #资金差额, double
        self.Commission = 'Money' #手续费, double
        self.PreSettlementPrice = 'Price' #上次结算价, double
        self.SettlementPrice = 'Price' #本次结算价, double
        self.TradingDay = 'Date' #交易日, char[9]
        self.OpenCost = 'Money' #开仓成本, double
        self.ExchangeMargin = 'Money' #交易所保证金, double
        self.TodayPosition = 'Volume' #今日持仓, int
        self.TransferFee = 'Money' #过户费, double
        self.StampTax = 'Money' #印花税, double
        self.TodayPurRedVolume = 'Volume' #今日申购赎回数量, int
        self.ConversionRate = 'Ratio' #折算率, double
        self.ConversionAmount = 'Money' #折算金额, double
        self.StockValue = 'Money' #证券价值, double
        self.ExchangeID = '' #交易所代码, char[9]
        self.AccountID = '' #AccountID, char[15]
        self.PledgeInPosition = 'Volume' #质押入库数量, int
        self.RepurchasePosition = 'Volume' #正回购使用的标准券数量, int
        self.PurRedShortFrozen = 'Volume' #ETF申赎空头冻结, int
        self.MarginTradeVolume = 'Volume' #融资买入出数量, int
        self.MarginTradeAmount = 'Money' #融资买入金额, double
        self.MarginTradeFrozenVolume = 'Volume' #融资买入冻结数量, int
        self.MarginTradeFrozenAmount = 'Money' #融资买入冻结金额, double
        self.MarginTradeConversionProfit = 'Money' #融资买入盈亏, double
        self.ShortSellVolume = 'Volume' #融券卖出数量, int
        self.ShortSellAmount = 'Money' #融券卖出金额, double
        self.ShortSellFrozenVolume = 'Volume' #融券卖出冻结数量, int
        self.ShortSellFrozenAmount = 'Money' #融券卖出冻结金额, double
        self.ShortSellConversionProfit = 'Money' #融券卖出盈亏, double
        self.SSStockValue = 'Money' #融券总市值, double
        self.TodayMTPosition = 'Volume' #今日融资持仓, int
        self.TodaySSPosition = 'Volume' #今日融券持仓, int
        self.YdOpenCost = 'Money' #历史持仓开仓成本, double

class SyncDeposit(BaseStruct): #出入金同步
    def __init__(self, DepositSeqNo='', BrokerID='', InvestorID='', Deposit=0.0, IsForce=0, AccountID=''):
        self.DepositSeqNo = '' #出入金流水号, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.Deposit = 'Money' #入金金额, double
        self.IsForce = 'Bool' #是否强制进行, int
        self.AccountID = '' #账户代, char[15]

class QryExchange(BaseStruct): #查询交易所
    def __init__(self, ExchangeID=''):
        self.ExchangeID = '' #交易所代码, char[9]

class QryProduct(BaseStruct): #查询产品
    def __init__(self, ProductID=''):
        self.ProductID = 'InstrumentID' #产品代码, char[31]

class QryInstrument(BaseStruct): #查询合约
    def __init__(self, InstrumentID='', ExchangeID='', ExchangeInstID='', ProductID=''):
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.ProductID = 'InstrumentID' #产品代码, char[31]

class QryBroker(BaseStruct): #查询经纪公司
    def __init__(self, BrokerID=''):
        self.BrokerID = '' #经纪公司代码, char[11]

class QryPartBroker(BaseStruct): #查询经纪公司会员代码
    def __init__(self, ExchangeID='', BrokerID='', ParticipantID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ParticipantID = '' #会员代码, char[11]

class QryInvestor(BaseStruct): #查询投资者
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class QryTradingCode(BaseStruct): #查询交易编码
    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', ClientID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ClientID = '' #客户代码, char[21]

class QrySuperUser(BaseStruct): #查询管理用户
    def __init__(self, UserID=''):
        self.UserID = '' #用户代码, char[16]

class QrySuperUserFunction(BaseStruct): #查询管理用户功能权限
    def __init__(self, UserID=''):
        self.UserID = '' #用户代码, char[16]

class QryBrokerUser(BaseStruct): #查询经纪公司用户
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class QryBrokerUserFunction(BaseStruct): #查询经纪公司用户权限
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class QryTradingAccount(BaseStruct): #查询资金账户
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class QryLoginForbiddenUser(BaseStruct): #查询禁止登录用户
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class QryDepthMarketData(BaseStruct): #查询行情
    def __init__(self, InstrumentID=''):
        self.InstrumentID = '' #合约代码, char[31]

class QryInstrumentTradingRight(BaseStruct): #查询合约交易权限
    def __init__(self, ExchangeID='', BrokerID='', InvestorID='', InstrumentID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]

class QryInvestorPositionDetail(BaseStruct): #查询投资者持仓明细
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]

class QryBondInterest(BaseStruct): #查询债券利息
    def __init__(self, ExchangeID='', InstrumentID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentID = '' #合约代码, char[31]

class QryMarketRationInfo(BaseStruct): #查询市值配售信息
    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者帐号, char[15]
        self.ExchangeID = '' #交易所代码, char[9]

class QryInstrumentCommissionRate(BaseStruct): #查询合约手续费率
    def __init__(self, ExchangeID='', BrokerID='', InvestorID='', InstrumentID='', Direction=D_Buy):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.Direction = '' #买卖方向, char

class QryExcessStockInfo(BaseStruct): #查询余券信息
    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', InstrumentID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentID = '' #合约代码, char[31]

class QryTraderOffer(BaseStruct): #查询交易员报盘机
    def __init__(self, ExchangeID='', ParticipantID='', BranchPBU=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ParticipantID = '' #会员代码, char[11]
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]

class QryMDTraderOffer(BaseStruct): #查询行情报盘机
    def __init__(self, ExchangeID='', ParticipantID='', BranchPBU=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ParticipantID = '' #会员代码, char[11]
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]

class QryFrontStatus(BaseStruct): #查询前置状态
    def __init__(self, FrontID=0):
        self.FrontID = '' #前置编号, int

class QryUserSession(BaseStruct): #查询用户会话
    def __init__(self, FrontID=0, SessionID=0, BrokerID='', UserID=''):
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class QryOrder(BaseStruct): #查询报单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', OrderSysID='', InsertTimeStart='', InsertTimeEnd=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]
        self.OrderSysID = '' #报单编号, char[21]
        self.InsertTimeStart = 'Time' #开始时间, char[9]
        self.InsertTimeEnd = 'Time' #结束时间, char[9]

class QryOrderAction(BaseStruct): #查询报单操作
    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ExchangeID = '' #交易所代码, char[9]

class QryErrOrder(BaseStruct): #查询错误报单
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class QryErrOrderAction(BaseStruct): #查询错误报单操作
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class QryTrade(BaseStruct): #查询成交
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', TradeID='', TradeTimeStart='', TradeTimeEnd=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]
        self.TradeID = '' #成交编号, char[21]
        self.TradeTimeStart = 'Time' #开始时间, char[9]
        self.TradeTimeEnd = 'Time' #结束时间, char[9]

class QryInvestorPosition(BaseStruct): #查询投资者持仓
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]

class QrySyncDeposit(BaseStruct): #查询出入金流水
    def __init__(self, BrokerID='', DepositSeqNo=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.DepositSeqNo = '' #出入金流水号, char[15]

class UserPasswordUpdate(BaseStruct): #用户口令变更
    def __init__(self, BrokerID='', UserID='', OldPassword='', NewPassword=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.OldPassword = 'Password' #原来的口令, char[41]
        self.NewPassword = 'Password' #新的口令, char[41]

class TradingAccountPasswordUpdate(BaseStruct): #资金账户口令变更域
    def __init__(self, BrokerID='', AccountID='', OldPassword='', NewPassword=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.AccountID = '' #投资者帐号, char[15]
        self.OldPassword = 'Password' #原来的口令, char[41]
        self.NewPassword = 'Password' #新的口令, char[41]

class ManualSyncBrokerUserOTP(BaseStruct): #手工同步用户动态令牌
    def __init__(self, BrokerID='', UserID='', OTPType=OTP_NONE, FirstOTP='', SecondOTP=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.OTPType = '' #动态令牌类型, char
        self.FirstOTP = 'Password' #第一个动态密码, char[41]
        self.SecondOTP = 'Password' #第二个动态密码, char[41]

class BrokerUserPassword(BaseStruct): #经纪公司用户口令
    def __init__(self, BrokerID='', UserID='', Password=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.Password = '' #密码, char[41]

class TradingAccountPassword(BaseStruct): #资金账户口令域
    def __init__(self, BrokerID='', AccountID='', Password=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #密码, char[41]

class UserRight(BaseStruct): #用户权限
    def __init__(self, BrokerID='', UserID='', UserRightType=URT_Logon, IsForbidden=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserRightType = '' #客户权限类型, char
        self.IsForbidden = 'Bool' #是否禁止, int

class InvestorAccount(BaseStruct): #投资者账户
    def __init__(self, BrokerID='', InvestorID='', AccountID='', IsDefault=0, AccountType=AcT_Normal, IsActive=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.AccountID = '' #投资者帐号, char[15]
        self.IsDefault = 'Bool' #是否主账户, int
        self.AccountType = '' #账户类型, char
        self.IsActive = 'Bool' #是否活跃, int

class UserIP(BaseStruct): #用户IP
    def __init__(self, BrokerID='', UserID='', IPAddress='', IPMask='', MacAddress=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.IPAddress = '' #IP地址, char[16]
        self.IPMask = 'IPAddress' #IP地址掩码, char[16]
        self.MacAddress = '' #Mac地址, char[21]

class BrokerUserOTPParam(BaseStruct): #用户动态令牌参数
    def __init__(self, BrokerID='', UserID='', OTPVendorsID='', SerialNumber='', AuthKey='', LastDrift=0, LastSuccess=0, OTPType=OTP_NONE):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.OTPVendorsID = '' #动态令牌提供商, char[2]
        self.SerialNumber = '' #动态令牌序列号, char[17]
        self.AuthKey = '' #令牌密钥, char[41]
        self.LastDrift = '' #漂移值, int
        self.LastSuccess = '' #成功值, int
        self.OTPType = '' #动态令牌类型, char

class ReqUserLogin(BaseStruct): #用户登录请求
    def __init__(self, TradingDay='', BrokerID='', UserID='', Password='', UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', MacAddress='', OneTimePassword='', ClientIPAddress='', AuthCode=''):
        self.TradingDay = 'Date' #交易日, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.Password = '' #密码, char[41]
        self.UserProductInfo = 'ProductInfo' #用户端产品信息, char[11]
        self.InterfaceProductInfo = 'ProductInfo' #接口端产品信息, char[11]
        self.ProtocolInfo = '' #协议信息, char[11]
        self.MacAddress = '' #Mac地址, char[21]
        self.OneTimePassword = 'Password' #动态密码, char[41]
        self.ClientIPAddress = 'IPAddress' #终端IP地址, char[16]
        self.AuthCode = '' #客户端认证码, char[17]

class RspUserLogin(BaseStruct): #用户登录应答
    def __init__(self, TradingDay='', LoginTime='', BrokerID='', UserID='', SystemName='', FrontID=0, SessionID=0, MaxOrderRef=''):
        self.TradingDay = 'Date' #交易日, char[9]
        self.LoginTime = 'Time' #登录成功时间, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.SystemName = '' #交易系统名称, char[41]
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.MaxOrderRef = 'OrderRef' #最大报单引用, char[13]

class UserLogout(BaseStruct): #用户登出请求
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class LogoutAll(BaseStruct): #全部登出信息
    def __init__(self, FrontID=0, SessionID=0, SystemName=''):
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.SystemName = '' #系统名称, char[41]

class ForceUserLogout(BaseStruct): #强制交易员退出
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class InputOrder(BaseStruct): #输入报单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', OrderPriceType=OPT_AnyPrice, Direction=D_Buy, CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal=0, TimeCondition=TC_IOC, GTDDate='', VolumeCondition=VC_AV, MinVolume=0, ContingentCondition=CC_Immediately, StopPrice=0.0, ForceCloseReason=FCC_NotForceClose, IsAutoSuspend=0, BusinessUnit='', RequestID=0, UserForceClose=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.OrderRef = '' #报单引用, char[13]
        self.UserID = '' #用户代码, char[16]
        self.ExchangeID = '' #交易所代码, char[9]
        self.OrderPriceType = '' #报单价格条件, char
        self.Direction = '' #买卖方向, char
        self.CombOffsetFlag = '' #组合开平标志, char[5]
        self.CombHedgeFlag = '' #组合投机套保标志, char[5]
        self.LimitPrice = 'StockPrice' #价格, char[16]
        self.VolumeTotalOriginal = 'Volume' #数量, int
        self.TimeCondition = '' #有效期类型, char
        self.GTDDate = 'Date' #GTD日期, char[9]
        self.VolumeCondition = '' #成交量类型, char
        self.MinVolume = 'Volume' #最小成交量, int
        self.ContingentCondition = '' #触发条件, char
        self.StopPrice = 'Price' #止损价, double
        self.ForceCloseReason = '' #强平原因, char
        self.IsAutoSuspend = 'Bool' #自动挂起标志, int
        self.BusinessUnit = '' #业务单元, char[21]
        self.RequestID = '' #请求编号, int
        self.UserForceClose = 'Bool' #用户强评标志, int

class InputOrderAction(BaseStruct): #输入报单操作
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef=0, OrderRef='', RequestID=0, FrontID=0, SessionID=0, ExchangeID='', ActionFlag=AF_Delete, LimitPrice=0.0, VolumeChange=0, UserID='', InstrumentID='', BranchPBU='', OrderLocalID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.OrderActionRef = '' #报单操作引用, int
        self.OrderRef = '' #报单引用, char[13]
        self.RequestID = '' #请求编号, int
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.ExchangeID = '' #交易所代码, char[9]
        self.ActionFlag = '' #操作标志, char
        self.LimitPrice = 'Price' #价格, double
        self.VolumeChange = 'Volume' #数量变化, int
        self.UserID = '' #用户代码, char[16]
        self.InstrumentID = '' #合约代码, char[31]
        self.BranchPBU = 'TraderID' #交易所交易员代码, char[21]
        self.OrderLocalID = '' #本地报单编号, char[13]

class SpecificInstrument(BaseStruct): #指定的合约
    def __init__(self, InstrumentID='', ExchangeID=''):
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]

class SpecificExchange(BaseStruct): #指定的交易所
    def __init__(self, ExchangeID=''):
        self.ExchangeID = '' #交易所代码, char[9]

class MarketDataBase(BaseStruct): #行情基础属性
    def __init__(self, TradingDay='', PreSettlementPrice=0.0, PreClosePrice=0.0, PreOpenInterest=0.0, PreDelta=0.0):
        self.TradingDay = 'Date' #交易日, char[9]
        self.PreSettlementPrice = 'Price' #上次结算价, double
        self.PreClosePrice = 'Price' #昨收盘, double
        self.PreOpenInterest = 'LargeVolume' #昨持仓量, double
        self.PreDelta = 'Ratio' #昨虚实度, double

class MarketDataStatic(BaseStruct): #行情静态属性
    def __init__(self, OpenPrice=0.0, HighestPrice=0.0, LowestPrice=0.0, ClosePrice=0.0, UpperLimitPrice=0.0, LowerLimitPrice=0.0, SettlementPrice=0.0, CurrDelta=0.0):
        self.OpenPrice = 'Price' #今开盘, double
        self.HighestPrice = 'Price' #最高价, double
        self.LowestPrice = 'Price' #最低价, double
        self.ClosePrice = 'Price' #今收盘, double
        self.UpperLimitPrice = 'Price' #涨停板价, double
        self.LowerLimitPrice = 'Price' #跌停板价, double
        self.SettlementPrice = 'Price' #本次结算价, double
        self.CurrDelta = 'Ratio' #今虚实度, double

class MarketDataLastMatch(BaseStruct): #行情最新成交属性
    def __init__(self, LastPrice=0.0, Volume=0, Turnover=0.0, OpenInterest=0.0):
        self.LastPrice = 'Price' #最新价, double
        self.Volume = '' #数量, int
        self.Turnover = 'Money' #成交金额, double
        self.OpenInterest = 'LargeVolume' #持仓量, double

class MarketDataBestPrice(BaseStruct): #行情最优价属性
    def __init__(self, BidPrice1=0.0, BidVolume1=0, AskPrice1=0.0, AskVolume1=0):
        self.BidPrice1 = 'Price' #申买价一, double
        self.BidVolume1 = 'Volume' #申买量一, int
        self.AskPrice1 = 'Price' #申卖价一, double
        self.AskVolume1 = 'Volume' #申卖量一, int

class MarketDataBid23(BaseStruct): #行情申买二、三属性
    def __init__(self, BidPrice2=0.0, BidVolume2=0, BidPrice3=0.0, BidVolume3=0):
        self.BidPrice2 = 'Price' #申买价二, double
        self.BidVolume2 = 'Volume' #申买量二, int
        self.BidPrice3 = 'Price' #申买价三, double
        self.BidVolume3 = 'Volume' #申买量三, int

class MarketDataAsk23(BaseStruct): #行情申卖二、三属性
    def __init__(self, AskPrice2=0.0, AskVolume2=0, AskPrice3=0.0, AskVolume3=0):
        self.AskPrice2 = 'Price' #申卖价二, double
        self.AskVolume2 = 'Volume' #申卖量二, int
        self.AskPrice3 = 'Price' #申卖价三, double
        self.AskVolume3 = 'Volume' #申卖量三, int

class MarketDataBid45(BaseStruct): #行情申买四、五属性
    def __init__(self, BidPrice4=0.0, BidVolume4=0, BidPrice5=0.0, BidVolume5=0):
        self.BidPrice4 = 'Price' #申买价四, double
        self.BidVolume4 = 'Volume' #申买量四, int
        self.BidPrice5 = 'Price' #申买价五, double
        self.BidVolume5 = 'Volume' #申买量五, int

class MarketDataAsk45(BaseStruct): #行情申卖四、五属性
    def __init__(self, AskPrice4=0.0, AskVolume4=0, AskPrice5=0.0, AskVolume5=0):
        self.AskPrice4 = 'Price' #申卖价四, double
        self.AskVolume4 = 'Volume' #申卖量四, int
        self.AskPrice5 = 'Price' #申卖价五, double
        self.AskVolume5 = 'Volume' #申卖量五, int

class MarketDataUpdateTime(BaseStruct): #行情更新时间属性
    def __init__(self, InstrumentID='', UpdateTime='', UpdateMillisec=0, ActionDay=''):
        self.InstrumentID = '' #合约代码, char[31]
        self.UpdateTime = 'Time' #最后修改时间, char[9]
        self.UpdateMillisec = 'Millisec' #最后修改毫秒, int
        self.ActionDay = 'Date' #业务日期, char[9]

class MarketDataAveragePrice(BaseStruct): #成交均价
    def __init__(self, AveragePrice=0.0):
        self.AveragePrice = 'Price' #当日均价, double

class MarketDataExchange(BaseStruct): #行情交易所代码属性
    def __init__(self, ExchangeID=''):
        self.ExchangeID = '' #交易所代码, char[9]

class Dissemination(BaseStruct): #信息分发
    def __init__(self, SequenceSeries=0, SequenceNo=0):
        self.SequenceSeries = '' #序列系列号, short
        self.SequenceNo = '' #序列号, int

class InputFundTransfer(BaseStruct): #资金转账输入
    def __init__(self, BrokerID='', InvestorID='', AccountID='', Password='', UserID='', TradeAmount=0.0, Digest='', AccountType=AcT_Normal):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.AccountID = '' #投资者资金帐号, char[15]
        self.Password = '' #资金帐户密码, char[41]
        self.UserID = '' #用户代码, char[16]
        self.TradeAmount = '' #交易金额, double
        self.Digest = '' #摘要, char[36]
        self.AccountType = '' #账户类型, char

class FundTransfer(BaseStruct): #资金转账
    def __init__(self, BrokerID='', InvestorID='', AccountID='', Password='', UserID='', TradeAmount=0.0, Digest='', SessionID=0, LiberSerial=0, PlateSerial=0, TransferSerial='', TradingDay='', TradeTime='', FundDirection=FD_In, ErrorID=0, ErrorMsg=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.AccountID = '' #投资者资金帐号, char[15]
        self.Password = '' #资金帐户密码, char[41]
        self.UserID = '' #用户代码, char[16]
        self.TradeAmount = '' #交易金额, double
        self.Digest = '' #摘要, char[36]
        self.SessionID = '' #会话编号, int
        self.LiberSerial = '' #Liber核心流水号, int
        self.PlateSerial = '' #转账平台流水号, int
        self.TransferSerial = 'BankSerial' #第三方流水号, char[13]
        self.TradingDay = 'Date' #交易日, char[9]
        self.TradeTime = 'Time' #转账时间, char[9]
        self.FundDirection = '' #出入金方向, char
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class QryFundTransferSerial(BaseStruct): #资金转账查询请求
    def __init__(self, BrokerID='', AccountID='', AccountType=AcT_Normal):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.AccountID = '' #投资者资金帐号, char[15]
        self.AccountType = '' #账户类型, char


def _init():
    import re, sys
    from ctypes import c_char, c_short, c_int, c_double, Structure
    G = globals(); del G['_init']; T = G.pop('T'); Base = G.pop('BaseStruct')
    match = re.compile(r'(\w+)\[(\d+)\]').match
    D = {'char':c_char, 'short':c_short, 'int':c_int, 'double':c_double}
    for k,v in T.items():
        if v not in D:
            m = match(v).groups(); D[v] = D[m[0]] * int(m[1])
        T[k] = D[v]
    if sys.version_info[0] >= 3:
        for k,v in G.items():
            if isinstance(v, str) and k[1:-1].count('_') == 1: G[k] = v.encode('latin-1')
    edvs = {'ContingentCondition':CC_Immediately, 'TradeType':TRDT_Common, 'InstrumentRange':INR_All, 'TradingRight':TR_Allow, 'UserRightType':URT_Logon, 'HedgeFlag':HF_Speculation, 'TraderConnectStatus':TCS_NotConnected, 'PositionType':PT_Net, 'ProductClass':PC_Futures, 'OrderPriceType':OPT_AnyPrice, 'PositionDateType':PDT_UseHistory, 'Direction':D_Buy, 'OffsetFlag':OF_Open, 'ClientType':CLT_Normal, 'ExchangeProperty':EXP_Normal, 'UserType':UT_Investor, 'TimeCondition':TC_IOC, 'OrderStatus':OST_AllTraded, 'ActionFlag':AF_Delete, 'OrderSubmitStatus':OSS_InsertSubmitted, 'PosTradeType':PTT_CanSelTodayPos, 'PositionDate':PSD_Today, 'InvestorRange':IR_All, 'ForceCloseReason':FCC_NotForceClose, 'OrderType':ORDT_Normal, 'FunctionCode':FC_ForceUserLogout, 'OrderSource':OSRC_Participant, 'IdCardType':ICT_EID, 'PosiDirection':PD_Net, 'InstLifePhase':IP_NotStart, 'VolumeCondition':VC_AV, 'OTPType':OTP_NONE, 'FundDirection':FD_In, 'AccountType':AcT_Normal, 'TradeSource':TSRC_NORMAL, 'PriceSource':PSRC_LastPrice, 'TradingRole':ER_Broker, 'BrokerFunctionCode':BFC_ForceUserLogout, 'OrderActionStatus':OAS_Submitted}
    Structs = [v for v in G.values() if isinstance(v,type) and issubclass(v,Base)]
    Base = G['BaseStruct'] = type('BaseStruct', (Structure,), dict((k,v)
            for k,v in Base.__dict__.items() if
            k in ('__doc__', '__repr__', '__str__') or
            not (k.startswith('__') and k.endswith('__'))))
    class builder(object):
        def __setattr__(self, fn, ft):
            ft = ft or fn
            if ft in edvs: self.enums.append((len(self.fields), fn, edvs[ft]))
            self.fields.append((fn, T[ft]))
        def build(self, cls):
            self.__dict__['enums'] = []
            self.__dict__['fields'] = []
            cls.__dict__['__init__'](self)
            d = {'_fields_': tuple(self.fields)}
            if self.enums:
                enums = tuple(self.enums)
                def __init__(self, *args, **kwargs):
                    c = len(args); setdefault = kwargs.setdefault
                    for i,n,d in enums:
                        if i >= c: setdefault(n, d)
                    Base.__init__(self, *args, **kwargs)
                d['__init__'] = __init__
            G[cls.__name__] = type(cls.__name__, (Base,), d)
    builder = builder()
    for cls in Structs: builder.build(cls)
_init()
