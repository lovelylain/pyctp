# -*- coding: utf-8 -*-

from __future__ import absolute_import as _init

T = {}
T['TE_RESUME'] = 'int' #流重传方式
TERT_RESTART = 0 #从本交易日开始重传
TERT_RESUME = 1 #从上次收到的续传
TERT_QUICK = 2 #只传送登录后的流内容
T['TraderID'] = 'char[21]' #交易所交易员代码
T['InvestorID'] = 'char[15]' #投资者代码
T['BrokerID'] = 'char[11]' #经纪公司代码
T['BrokerAbbr'] = 'char[9]' #经纪公司简称
T['BrokerName'] = 'char[81]' #经纪公司名称
T['ExchangeInstID'] = 'char[31]' #合约在交易所的代码
T['OrderRef'] = 'char[13]' #报单引用
T['ParticipantID'] = 'char[11]' #会员代码
T['UserID'] = 'char[16]' #用户代码
T['Password'] = 'char[41]' #密码
T['ClientID'] = 'char[11]' #交易编码
T['InstrumentID'] = 'char[31]' #合约代码
T['MarketID'] = 'char[31]' #市场代码
T['ProductName'] = 'char[21]' #产品名称
T['ExchangeID'] = 'char[9]' #交易所代码
T['ExchangeName'] = 'char[31]' #交易所名称
T['ExchangeAbbr'] = 'char[9]' #交易所简称
T['ExchangeFlag'] = 'char[2]' #交易所标志
T['MacAddress'] = 'char[21]' #Mac地址
T['ExchangeProperty'] = 'char' #交易所属性
EXP_Normal = '0' #正常
EXP_GenOrderByTrade = '1' #根据成交生成报单
T['Date'] = 'char[9]' #日期
T['Time'] = 'char[9]' #时间
T['LongTime'] = 'char[13]' #长时间
T['InstrumentName'] = 'char[21]' #合约名称
T['SettlementGroupID'] = 'char[9]' #结算组代码
T['OrderSysID'] = 'char[21]' #报单编号
T['TradeID'] = 'char[21]' #成交编号
T['CommandType'] = 'char[65]' #DB命令类型
T['IPAddress'] = 'char[16]' #IP地址
T['ProductInfo'] = 'char[11]' #产品信息
T['ProtocolInfo'] = 'char[11]' #协议信息
T['BusinessUnit'] = 'char[21]' #业务单元
T['DepositSeqNo'] = 'char[15]' #出入金流水号
T['IdentifiedCardNo'] = 'char[51]' #证件号码
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
ICT_OtherCard = 'x' #其他证件
T['OrderLocalID'] = 'char[13]' #本地报单编号
T['UserName'] = 'char[81]' #用户名称
T['PartyName'] = 'char[81]' #参与人名称
T['ErrorMsg'] = 'char[81]' #错误信息
T['FieldName'] = 'char[2049]' #字段名
T['FieldContent'] = 'char[2049]' #字段内容
T['SystemName'] = 'char[41]' #系统名称
T['Content'] = 'char[501]' #消息正文
T['InvestorRange'] = 'char' #投资者范围
IR_All = '1' #所有
IR_Group = '2' #投资者组
IR_Single = '3' #单一投资者
T['DepartmentRange'] = 'char' #投资者范围
DR_All = '1' #所有
DR_Group = '2' #组织架构
DR_Single = '3' #单一投资者
T['DataSyncStatus'] = 'char' #数据同步状态
DS_Asynchronous = '1' #未同步
DS_Synchronizing = '2' #同步中
DS_Synchronized = '3' #已同步
T['BrokerDataSyncStatus'] = 'char' #经纪公司数据同步状态
BDS_Synchronized = '1' #已同步
BDS_Synchronizing = '2' #同步中
T['ExchangeConnectStatus'] = 'char' #交易所连接状态
ECS_NoConnection = '1' #没有任何连接
ECS_QryInstrumentSent = '2' #已经发出合约查询请求
ECS_GotInformation = '9' #已经获取信息
T['TraderConnectStatus'] = 'char' #交易所交易员连接状态
TCS_NotConnected = '1' #没有任何连接
TCS_Connected = '2' #已经连接
TCS_QryInstrumentSent = '3' #已经发出合约查询请求
TCS_SubPrivateFlow = '4' #订阅私有流
T['FunctionCode'] = 'char' #功能代码
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
T['BrokerFunctionCode'] = 'char' #经纪公司功能代码
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
T['PositionDateType'] = 'char' #持仓日期类型
PDT_UseHistory = '1' #使用历史持仓
PDT_NoUseHistory = '2' #不使用历史持仓
T['TradingRole'] = 'char' #交易角色
ER_Broker = '1' #代理
ER_Host = '2' #自营
ER_Maker = '3' #做市商
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
T['InstLifePhase'] = 'char' #合约生命周期状态
IP_NotStart = '0' #未上市
IP_Started = '1' #上市
IP_Pause = '2' #停牌
IP_Expired = '3' #到期
T['Direction'] = 'char' #买卖方向
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
D_TransferSecurities = 'a' #担保品划转
T['PositionType'] = 'char' #持仓类型
PT_Net = '1' #净持仓
PT_Gross = '2' #综合持仓
T['PosiDirection'] = 'char' #持仓多空方向
PD_Net = '1' #净
PD_Long = '2' #多头
PD_Short = '3' #空头
PD_MarginTrade = '4' #融资
PD_ShortSell = '5' #融券
T['SysSettlementStatus'] = 'char' #系统结算状态
SS_NonActive = '1' #不活跃
SS_Startup = '2' #启动
SS_Operating = '3' #操作
SS_Settlement = '4' #结算
SS_SettlementFinished = '5' #结算完成
T['RatioAttr'] = 'char' #费率属性
RA_Trade = '0' #交易费率
RA_Settlement = '1' #结算费率
T['HedgeFlag'] = 'char' #投机套保标志
HF_Speculation = '1' #投机
HF_Hedge = '3' #套保
T['OrderPriceType'] = 'char' #报单价格条件
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
T['TradeType'] = 'char' #成交类型
TRDT_Common = '0' #普通成交
TRDT_OptionsExecution = '1' #期权执行
TRDT_OTC = '2' #OTC成交
TRDT_EFPDerived = '3' #期转现衍生成交
TRDT_CombinationDerived = '4' #组合衍生成交
TRDT_EFTPurchase = '5' #ETF申购
TRDT_EFTRedem = '6' #ETF赎回
T['PriceSource'] = 'char' #成交价来源
PSRC_LastPrice = '0' #前成交价
PSRC_Buy = '1' #买委托价
PSRC_Sell = '2' #卖委托价
T['InstrumentStatus'] = 'char' #合约交易状态
IS_BeforeTrading = '0' #开盘前
IS_NoTrading = '1' #非交易
IS_Continous = '2' #连续交易
IS_AuctionOrdering = '3' #集合竞价报单
IS_AuctionBalance = '4' #集合竞价价格平衡
IS_AuctionMatch = '5' #集合竞价撮合
IS_Closed = '6' #收盘
T['InstStatusEnterReason'] = 'char' #品种进入交易状态原因
IER_Automatic = '1' #自动切换
IER_Manual = '2' #手动切换
IER_Fuse = '3' #熔断
T['OrderActionRef'] = 'int' #报单操作引用
T['InstallCount'] = 'int' #安装数量
T['InstallID'] = 'int' #安装编号
T['ErrorID'] = 'int' #错误代码
T['SettlementID'] = 'int' #结算编号
T['Volume'] = 'int' #数量
T['FrontID'] = 'int' #前置编号
T['SessionID'] = 'int' #会话编号
T['SequenceNo'] = 'int' #序号
T['CommandNo'] = 'int' #DB命令序号
T['Millisec'] = 'int' #时间（毫秒）
T['VolumeMultiple'] = 'int' #合约数量乘数
T['TradingSegmentSN'] = 'int' #交易阶段编号
T['RequestID'] = 'int' #请求编号
T['Year'] = 'int' #年份
T['Month'] = 'int' #月份
T['Bool'] = 'int' #布尔型
T['Price'] = 'double' #价格
T['CombOffsetFlag'] = 'char[5]' #组合开平标志
T['CombHedgeFlag'] = 'char[5]' #组合投机套保标志
T['Ratio'] = 'double' #比率
T['Money'] = 'double' #资金
T['LargeVolume'] = 'double' #大额数量
T['SequenceSeries'] = 'short' #序列系列号
T['CommPhaseNo'] = 'short' #通讯时段编号
T['SequenceLabel'] = 'char[2]' #序列编号
T['Priority'] = 'int' #优先级
T['ContractCode'] = 'char[41]' #合同编号
T['City'] = 'char[41]' #市
T['IsStock'] = 'char[11]' #是否股民
T['Channel'] = 'char[51]' #渠道
T['Address'] = 'char[101]' #通讯地址
T['ZipCode'] = 'char[7]' #邮政编码
T['Telephone'] = 'char[41]' #联系电话
T['Fax'] = 'char[41]' #传真
T['Mobile'] = 'char[41]' #手机
T['EMail'] = 'char[41]' #电子邮件
T['Memo'] = 'char[161]' #备注
T['CompanyCode'] = 'char[51]' #企业代码
T['Website'] = 'char[51]' #网站地址
T['TaxNo'] = 'char[31]' #税务登记号
T['BatchStatus'] = 'char' #处理状态
BS_NoUpload = '1' #未上传
BS_Uploaded = '2' #已上传
BS_Failed = '3' #审核失败
T['PropertyID'] = 'char[33]' #属性代码
T['PropertyName'] = 'char[65]' #属性名称
T['LicenseNo'] = 'char[51]' #营业执照号
T['AgentID'] = 'char[13]' #经纪人代码
T['AgentName'] = 'char[41]' #经纪人名称
T['AgentGroupID'] = 'char[13]' #经纪人组代码
T['AgentGroupName'] = 'char[41]' #经纪人组名称
T['ReturnStyle'] = 'char' #按品种返还方式
RS_All = '1' #按所有品种
RS_ByProduct = '2' #按品种
T['ReturnPattern'] = 'char' #返还模式
RP_ByVolume = '1' #按成交手数
RP_ByFeeOnHand = '2' #按留存手续费
T['ReturnLevel'] = 'char' #返还级别
RL_Level1 = '1' #级别1
RL_Level2 = '2' #级别2
RL_Level3 = '3' #级别3
RL_Level4 = '4' #级别4
RL_Level5 = '5' #级别5
RL_Level6 = '6' #级别6
RL_Level7 = '7' #级别7
RL_Level8 = '8' #级别8
RL_Level9 = '9' #级别9
T['ReturnStandard'] = 'char' #返还标准
RSD_ByPeriod = '1' #分阶段返还
RSD_ByStandard = '2' #按某一标准
T['MortgageType'] = 'char' #质押类型
MT_Out = '0' #质出
MT_In = '1' #质入
T['InvestorSettlementParamID'] = 'char' #投资者结算参数代码
ISPI_BaseMargin = '1' #基础保证金
ISPI_LowestInterest = '2' #最低权益标准
ISPI_MortgageRatio = '4' #质押比例
ISPI_MarginWay = '5' #保证金算法
ISPI_BillDeposit = '9' #结算单(盯市)权益等于结存
T['ExchangeSettlementParamID'] = 'char' #交易所结算参数代码
ESPI_MortgageRatio = '1' #质押比例
ESPI_OtherFundItem = '2' #分项资金导入项
ESPI_OtherFundImport = '3' #分项资金入交易所出入金
ESPI_SHFEDelivFee = '4' #上期所交割手续费收取方式
ESPI_DCEDelivFee = '5' #大商所交割手续费收取方式
ESPI_CFFEXMinPrepa = '6' #中金所开户最低可用金额
T['SystemParamID'] = 'char' #系统参数代码
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
T['TradeParamID'] = 'char' #交易系统参数代码
TPID_EncryptionStandard = 'E' #系统加密算法
TPID_RiskMode = 'R' #系统风险算法
TPID_RiskModeGlobal = 'G' #系统风险算法是否全局 0-否 1-是
T['SettlementParamValue'] = 'char[256]' #参数代码值
T['CounterID'] = 'char[33]' #计数器代码
T['InvestorGroupName'] = 'char[41]' #投资者分组名称
T['BrandCode'] = 'char[257]' #牌号
T['Warehouse'] = 'char[257]' #仓库
T['ProductDate'] = 'char[41]' #产期
T['Grade'] = 'char[41]' #等级
T['Classify'] = 'char[41]' #类别
T['Position'] = 'char[41]' #货位
T['Yieldly'] = 'char[41]' #产地
T['Weight'] = 'char[41]' #公定重量
T['SubEntryFundNo'] = 'int' #分项资金流水号
T['FileID'] = 'char' #文件标识
FI_SettlementFund = 'F' #资金数据
FI_Trade = 'T' #成交数据
FI_InvestorPosition = 'P' #投资者持仓数据
FI_SubEntryFund = 'O' #投资者分项资金数据
T['FileName'] = 'char[257]' #文件名称
T['FileType'] = 'char' #文件上传类型
FUT_Settlement = '0' #结算
FUT_Check = '1' #核对
T['FileFormat'] = 'char' #文件格式
FFT_Txt = '0' #文本文件(.txt)
FFT_Zip = '1' #压缩文件(.zip)
FFT_DBF = '2' #DBF文件(.dbf)
T['FileUploadStatus'] = 'char' #文件状态
FUS_SucceedUpload = '1' #上传成功
FUS_FailedUpload = '2' #上传失败
FUS_SucceedLoad = '3' #导入成功
FUS_PartSucceedLoad = '4' #导入部分成功
FUS_FailedLoad = '5' #导入失败
T['TransferDirection'] = 'char' #移仓方向
TD_Out = '0' #移出
TD_In = '1' #移入
T['UploadMode'] = 'char[21]' #上传文件类型
T['AccountID'] = 'char[15]' #投资者帐号
T['BankFlag'] = 'char' #银行统一标识类型
BF_ICBC = '1' #工商银行
BF_ABC = '2' #农业银行
BF_BC = '3' #中国银行
BF_CBC = '4' #建设银行
BF_BOC = '5' #交通银行
BF_Other = 'Z' #其他银行
T['BankAccount'] = 'char[41]' #银行账户
T['OpenName'] = 'char[61]' #银行账户的开户人名称
T['OpenBank'] = 'char[101]' #银行账户的开户行
T['BankName'] = 'char[101]' #银行名称
T['PublishPath'] = 'char[257]' #发布路径
T['OperatorID'] = 'char[65]' #操作员代码
T['MonthCount'] = 'int' #月份数量
T['AdvanceMonthArray'] = 'char[13]' #月份提前数组
T['DateExpr'] = 'char[1025]' #日期表达式
T['InstrumentIDExpr'] = 'char[41]' #合约代码表达式
T['InstrumentNameExpr'] = 'char[41]' #合约名称表达式
T['SpecialCreateRule'] = 'char' #特殊的创建规则
SC_NoSpecialRule = '0' #没有特殊创建规则
SC_NoSpringFestival = '1' #不包含春节
T['BasisPriceType'] = 'char' #挂牌基准价类型
IPT_LastSettlement = '1' #上一合约结算价
IPT_LaseClose = '2' #上一合约收盘价
T['ProductLifePhase'] = 'char' #产品生命周期状态
PLP_Active = '1' #活跃
PLP_NonActive = '2' #不活跃
PLP_Canceled = '3' #注销
T['DeliveryMode'] = 'char' #交割方式
DM_CashDeliv = '1' #现金交割
DM_CommodityDeliv = '2' #实物交割
T['LogLevel'] = 'char[33]' #日志级别
T['ProcessName'] = 'char[257]' #存储过程名称
T['OperationMemo'] = 'char[1025]' #操作摘要
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
T['FundStatus'] = 'char' #资金状态
FS_Record = '1' #已录入
FS_Check = '2' #已复核
FS_Charge = '3' #已冲销
T['BillNo'] = 'char[15]' #票据号
T['BillName'] = 'char[33]' #票据名称
T['PublishStatus'] = 'char' #发布状态
PS_None = '1' #未发布
PS_Publishing = '2' #正在发布
PS_Published = '3' #已发布
T['EnumValueID'] = 'char[65]' #枚举值代码
T['EnumValueType'] = 'char[33]' #枚举值类型
T['EnumValueLabel'] = 'char[65]' #枚举值名称
T['EnumValueResult'] = 'char[33]' #枚举值结果
T['SystemStatus'] = 'char' #系统状态
ES_NonActive = '1' #不活跃
ES_Startup = '2' #启动
ES_Initialize = '3' #交易开始初始化
ES_Initialized = '4' #交易完成初始化
ES_Close = '5' #收市开始
ES_Closed = '6' #收市完成
ES_Settlement = '7' #结算
T['SettlementStatus'] = 'char' #结算状态
STS_Initialize = '0' #初始
STS_Settlementing = '1' #结算中
STS_Settlemented = '2' #已结算
STS_Finished = '3' #结算完成
T['RangeIntType'] = 'char[33]' #限定值类型
T['RangeIntFrom'] = 'char[33]' #限定值下限
T['RangeIntTo'] = 'char[33]' #限定值上限
T['FunctionID'] = 'char[25]' #功能代码
T['FunctionValueCode'] = 'char[257]' #功能编码
T['FunctionName'] = 'char[65]' #功能名称
T['RoleID'] = 'char[11]' #角色编号
T['RoleName'] = 'char[41]' #角色名称
T['Description'] = 'char[401]' #描述
T['CombineID'] = 'char[25]' #组合编号
T['CombineType'] = 'char[25]' #组合类型
T['InvestorType'] = 'char' #投资者类型
CT_Person = '0' #自然人
CT_Company = '1' #法人
CT_Fund = '2' #投资基金
T['BrokerType'] = 'char' #经纪公司类型
BT_Trade = '0' #交易会员
BT_TradeSettle = '1' #交易结算会员
T['RiskLevel'] = 'char' #风险等级
FAS_Low = '1' #低风险客户
FAS_Normal = '2' #普通客户
FAS_Focus = '3' #关注客户
FAS_Risk = '4' #风险客户
T['FeeAcceptStyle'] = 'char' #手续费收取方式
FAS_ByTrade = '1' #按交易收取
FAS_ByDeliv = '2' #按交割收取
FAS_None = '3' #不收
FAS_FixFee = '4' #按指定手续费收取
T['PasswordType'] = 'char' #密码类型
PWDT_Trade = '1' #交易密码
PWDT_Account = '2' #资金密码
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
T['Comment'] = 'char[31]' #盈亏算法说明
T['Version'] = 'char[4]' #版本号
T['TradeCode'] = 'char[7]' #交易代码
T['TradeDate'] = 'char[9]' #交易日期
T['TradeTime'] = 'char[9]' #交易时间
T['TradeSerial'] = 'char[9]' #发起方流水号
T['TradeSerialNo'] = 'int' #发起方流水号
T['FutureID'] = 'char[11]' #期货公司代码
T['BankID'] = 'char[4]' #银行代码
T['BankBrchID'] = 'char[5]' #银行分中心代码
T['BankBranchID'] = 'char[11]' #分中心代码
T['OperNo'] = 'char[17]' #交易柜员
T['DeviceID'] = 'char[3]' #渠道标志
T['RecordNum'] = 'char[7]' #记录数
T['FutureAccount'] = 'char[22]' #期货资金账号
T['FuturePwdFlag'] = 'char' #资金密码核对标志
FPWD_UnCheck = '0' #不核对
FPWD_Check = '1' #核对
T['TransferType'] = 'char' #银期转账类型
TT_BankToFuture = '0' #银行转期货
TT_FutureToBank = '1' #期货转银行
T['FutureAccPwd'] = 'char[17]' #期货资金密码
T['CurrencyCode'] = 'char[4]' #币种
T['RetCode'] = 'char[5]' #响应代码
T['RetInfo'] = 'char[129]' #响应信息
T['TradeAmt'] = 'char[20]' #银行总余额
T['UseAmt'] = 'char[20]' #银行可用余额
T['FetchAmt'] = 'char[20]' #银行可取余额
T['TransferValidFlag'] = 'char' #转账有效标志
TVF_Invalid = '0' #无效或失败
TVF_Valid = '1' #有效
TVF_Reverse = '2' #冲正
T['CertCode'] = 'char[21]' #证件号码
T['Reason'] = 'char' #事由
RN_CD = '0' #错单
RN_ZT = '1' #资金在途
RN_QT = '2' #其它
T['FundProjectID'] = 'char[5]' #资金项目编号
T['Sex'] = 'char' #性别
SEX_None = '0' #未知
SEX_Man = '1' #男
SEX_Woman = '2' #女
T['Profession'] = 'char[41]' #职业
T['National'] = 'char[31]' #国籍
T['Province'] = 'char[16]' #省
T['Region'] = 'char[16]' #区
T['Country'] = 'char[16]' #国家
T['LicenseNO'] = 'char[33]' #营业执照
T['CompanyType'] = 'char[16]' #企业性质
T['BusinessScope'] = 'char[1001]' #经营范围
T['CapitalCurrency'] = 'char[4]' #注册资本币种
T['UserType'] = 'char' #用户类型
UT_Investor = '0' #投资者
UT_Operator = '1' #操作员
UT_SuperUser = '2' #管理员
T['RateType'] = 'char' #费率类型
RATETYPE_MarginRate = '2' #保证金率
RATETYPE_CommRate = '1' #手续费率
RATETYPE_AllRate = '0' #所有
T['NoteType'] = 'char' #通知类型
NOTETYPE_TradeSettleBill = '1' #交易结算单
NOTETYPE_TradeSettleMonth = '2' #交易结算月报
NOTETYPE_CallMarginNotes = '3' #追加保证金通知书
NOTETYPE_ForceCloseNotes = '4' #强行平仓通知书
NOTETYPE_TradeNotes = '5' #成交通知书
NOTETYPE_DelivNotes = '6' #交割通知书
T['SettlementStyle'] = 'char' #结算单方式
SBS_Day = '1' #逐日盯市
SBS_Volume = '2' #逐笔对冲
T['BrokerDNS'] = 'char[256]' #域名
T['Sentence'] = 'char[501]' #语句
T['SettlementBillType'] = 'char' #结算单类型
ST_Day = '0' #日报
ST_Month = '1' #月报
T['UserRightType'] = 'char' #客户权限类型
URT_Logon = '1' #登录
URT_Transfer = '2' #银期转帐
URT_EMail = '3' #邮寄结算单
URT_Fax = '4' #传真结算单
URT_ConditionOrder = '5' #条件单
T['MarginPriceType'] = 'char' #保证金价格类型
MPT_PreSettlementPrice = '1' #昨结算价
MPT_SettlementPrice = '2' #最新价
MPT_AveragePrice = '3' #成交均价
MPT_OpenPrice = '4' #开仓价
T['BillGenStatus'] = 'char' #结算单生成状态
BGS_None = '0' #不生成
BGS_NoGenerated = '1' #未生成
BGS_Generated = '2' #已生成
T['AlgoType'] = 'char' #算法类型
AT_HandlePositionAlgo = '1' #持仓处理算法
AT_FindMarginRateAlgo = '2' #寻找保证金率算法
T['HandlePositionAlgoID'] = 'char' #持仓处理算法编号
HPA_Base = '1' #基本
HPA_DCE = '2' #大连商品交易所
HPA_CZCE = '3' #郑州商品交易所
HPA_NoneTrade = '4' #非交易
HPA_Stock = '5' #证券
T['FindMarginRateAlgoID'] = 'char' #寻找保证金率算法编号
FMRA_Base = '1' #基本
FMRA_DCE = '2' #大连商品交易所
FMRA_CZCE = '3' #郑州商品交易所
T['HandleTradingAccountAlgoID'] = 'char' #资金处理算法编号
HTAA_Base = '1' #基本
HTAA_DCE = '2' #大连商品交易所
HTAA_CZCE = '3' #郑州商品交易所
T['PersonType'] = 'char' #联系人类型
PST_Order = '1' #指定下单人
PST_Open = '2' #开户授权人
PST_Fund = '3' #资金调拨人
PST_Settlement = '4' #结算单确认人
T['QueryInvestorRange'] = 'char' #查询范围
QIR_All = '1' #所有
QIR_Group = '2' #查询分类
QIR_Single = '3' #单一投资者
T['InvestorRiskStatus'] = 'char' #投资者风险状态
IRS_Normal = '1' #正常
IRS_Warn = '2' #警告
IRS_Call = '3' #追保
IRS_Force = '4' #强平
IRS_Exception = '5' #异常
T['LegID'] = 'int' #单腿编号
T['LegMultiple'] = 'int' #单腿乘数
T['ImplyLevel'] = 'int' #派生层数
T['ClearAccount'] = 'char[33]' #结算账户
T['OrganNO'] = 'char[6]' #结算账户
T['ClearbarchID'] = 'char[6]' #结算账户联行号
T['UserEventType'] = 'char' #用户事件类型
UET_All = ' ' #所有
UET_Login = '1' #登录
UET_Logout = '2' #登出
UET_Trading = '3' #交易成功
UET_TradingError = '4' #交易失败
UET_UpdatePassword = '5' #修改密码
UET_Other = '9' #其他
T['UserEventInfo'] = 'char[1025]' #用户事件信息
T['CloseStyle'] = 'char' #平仓方式
ICS_Close = '0' #先开先平
ICS_CloseToday = '1' #先平今再平昨
T['StatMode'] = 'char' #统计方式
SM_Non = '0' #----
SM_Instrument = '1' #按合约统计
SM_Product = '2' #按产品统计
SM_Investor = '3' #按投资者统计
T['ParkedOrderStatus'] = 'char' #预埋单状态
PAOS_NotSend = '1' #未发送
PAOS_Send = '2' #已发送
PAOS_Deleted = '3' #已删除
T['ParkedOrderID'] = 'char[13]' #预埋报单编号
T['ParkedOrderActionID'] = 'char[13]' #预埋撤单编号
T['VirDealStatus'] = 'char' #处理状态
VDS_Dealing = '1' #正在处理
VDS_DeaclSucceed = '2' #处理成功
T['OrgSystemID'] = 'char' #原有系统代码
ORGS_Standard = '0' #综合交易平台
ORGS_ESunny = '1' #易盛系统
ORGS_KingStarV6 = '2' #金仕达V6系统
T['VirTradeStatus'] = 'char' #交易状态
VTS_NaturalDeal = '0' #正常处理中
VTS_SucceedEnd = '1' #成功结束
VTS_FailedEND = '2' #失败结束
VTS_Exception = '3' #异常中
VTS_ManualDeal = '4' #已人工异常处理
VTS_MesException = '5' #通讯异常 ，请人工处理
VTS_SysException = '6' #系统出错，请人工处理
T['VirBankAccType'] = 'char' #银行帐户类型
VBAT_BankBook = '1' #存折
VBAT_BankCard = '2' #储蓄卡
VBAT_CreditCard = '3' #信用卡
T['VirementStatus'] = 'char' #银行帐户类型
VMS_Natural = '0' #正常
VMS_Canceled = '9' #销户
T['VirementAvailAbility'] = 'char' #有效标志
VAA_NoAvailAbility = '0' #未确认
VAA_AvailAbility = '1' #有效
VAA_Repeal = '2' #冲正
T['VirementTradeCode'] = 'char[7]' #交易代码
VTC_BankBankToFuture = '102001' #银行发起银行资金转期货
VTC_BankFutureToBank = '102002' #银行发起期货资金转银行
VTC_FutureBankToFuture = '202001' #期货发起银行资金转期货
VTC_FutureFutureToBank = '202002' #期货发起期货资金转银行
T['PhotoTypeName'] = 'char[41]' #影像类型名称
T['PhotoTypeID'] = 'char[5]' #影像类型代码
T['PhotoName'] = 'char[161]' #影像名称
T['TopicID'] = 'int' #主题代码
T['ReportTypeID'] = 'char[3]' #交易报告类型标识
T['CharacterID'] = 'char[5]' #交易特征代码
T['AMLParamID'] = 'char[21]' #参数代码
T['AMLInvestorType'] = 'char[3]' #投资者类型
T['AMLIdCardType'] = 'char[3]' #证件类型
T['AMLTradeDirect'] = 'char[3]' #资金进出方向
T['AMLTradeModel'] = 'char[3]' #资金进出方式
T['AMLParamID'] = 'char[21]' #参数代码
T['AMLOpParamValue'] = 'double' #业务参数代码值
T['AMLCustomerCardType'] = 'char[81]' #客户身份证件/证明文件类型
T['AMLInstitutionName'] = 'char[65]' #金融机构网点名称
T['AMLDistrictID'] = 'char[7]' #金融机构网点所在地区行政区划代码
T['AMLRelationShip'] = 'char[3]' #金融机构网点与大额交易的关系
T['AMLInstitutionType'] = 'char[3]' #金融机构网点代码类型
T['AMLInstitutionID'] = 'char[13]' #金融机构网点代码
T['AMLAccountType'] = 'char[5]' #账户类型
T['AMLTradingType'] = 'char[7]' #交易方式
T['AMLTransactClass'] = 'char[7]' #涉外收支交易分类与代码
T['AMLCapitalIO'] = 'char[3]' #资金收付标识
T['AMLSite'] = 'char[10]' #交易地点
T['AMLCapitalPurpose'] = 'char[129]' #资金用途
T['AMLReportType'] = 'char[2]' #报文类型
T['AMLSerialNo'] = 'char[5]' #编号
T['AMLStatus'] = 'char[2]' #状态
T['AMLGenStatus'] = 'char[2]' #状态
T['AMLSeqCode'] = 'char[65]' #业务标识号
T['AMLFileName'] = 'char[257]' #AML文件名
T['AMLMoney'] = 'double' #反洗钱资金
T['AMLFileAmount'] = 'int' #反洗钱资金
T['CFMMCKey'] = 'char[21]' #密钥类型(保证金监管)
T['CFMMCKeyKind'] = 'char' #动态密钥类别(保证金监管)
CFMMCKK_REQUEST = 'R' #主动请求更新
CFMMCKK_AUTO = 'A' #CFMMC自动更新
CFMMCKK_MANUAL = 'M' #CFMMC手动更新
T['IndividualName'] = 'char[51]' #个人姓名
T['CurrencyID'] = 'char[4]' #币种代码
T['CustNumber'] = 'char[36]' #客户编号
T['OrganCode'] = 'char[36]' #机构编码
T['OrganName'] = 'char[71]' #机构名称
T['SuperOrganCode'] = 'char[12]' #上级机构编码,即期货公司总部、银行总行
T['SubBranchID'] = 'char[31]' #分支机构
T['SubBranchName'] = 'char[71]' #分支机构名称
T['BranchNetCode'] = 'char[31]' #机构网点号
T['BranchNetName'] = 'char[71]' #机构网点名称
T['OrganFlag'] = 'char[2]' #机构标识
T['BankCodingForFuture'] = 'char[33]' #银行对期货公司的编码
T['BankReturnCode'] = 'char[7]' #银行对返回码的定义
T['PlateReturnCode'] = 'char[5]' #银期转帐平台对返回码的定义
T['BankSubBranchID'] = 'char[31]' #银行分支机构编码
T['FutureBranchID'] = 'char[31]' #期货分支机构编码
T['ReturnCode'] = 'char[7]' #返回代码
T['OperatorCode'] = 'char[17]' #操作员
T['ClearDepID'] = 'char[6]' #机构结算帐户机构号
T['ClearBrchID'] = 'char[6]' #机构结算帐户联行号
T['ClearName'] = 'char[71]' #机构结算帐户名称
T['BankAccountName'] = 'char[71]' #银行帐户名称
T['InvDepID'] = 'char[6]' #机构投资人账号机构号
T['InvBrchID'] = 'char[6]' #机构投资人联行号
T['MessageFormatVersion'] = 'char[36]' #信息格式版本
T['Digest'] = 'char[36]' #摘要
T['AuthenticData'] = 'char[129]' #认证数据
T['PasswordKey'] = 'char[129]' #密钥
T['FutureAccountName'] = 'char[129]' #期货帐户名称
T['MobilePhone'] = 'char[21]' #手机
T['FutureMainKey'] = 'char[129]' #期货公司主密钥
T['FutureWorkKey'] = 'char[129]' #期货公司工作密钥
T['FutureTransKey'] = 'char[129]' #期货公司传输密钥
T['BankMainKey'] = 'char[129]' #银行主密钥
T['BankWorkKey'] = 'char[129]' #银行工作密钥
T['BankTransKey'] = 'char[129]' #银行传输密钥
T['BankServerDescription'] = 'char[129]' #银行服务器描述信息
T['AddInfo'] = 'char[129]' #附加信息
T['DescrInfoForReturnCode'] = 'char[129]' #返回码描述
T['CountryCode'] = 'char[21]' #国家代码
T['Serial'] = 'int' #流水号
T['PlateSerial'] = 'int' #平台流水号
T['BankSerial'] = 'char[13]' #银行流水号
T['CorrectSerial'] = 'int' #被冲正交易流水号
T['FutureSerial'] = 'int' #期货公司流水号
T['ApplicationID'] = 'int' #应用标识
T['BankProxyID'] = 'int' #银行代理标识
T['FBTCoreID'] = 'int' #银期转帐核心系统标识
T['ServerPort'] = 'int' #服务端口号
T['RepealedTimes'] = 'int' #已经冲正次数
T['RepealTimeInterval'] = 'int' #冲正时间间隔
T['TotalTimes'] = 'int' #每日累计转帐次数
T['FBTRequestID'] = 'int' #请求ID
T['TID'] = 'int' #交易ID
T['TradeAmount'] = 'double' #交易金额（元）
T['CustFee'] = 'double' #应收客户费用（元）
T['FutureFee'] = 'double' #应收期货公司费用（元）
T['SingleMaxAmt'] = 'double' #单笔最高限额
T['SingleMinAmt'] = 'double' #单笔最低限额
T['TotalAmt'] = 'double' #每日累计转帐额度
T['CertificationType'] = 'char' #证件类型
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
T['FileBusinessCode'] = 'char' #文件业务功能
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
T['CashExchangeCode'] = 'char' #汇钞标志
CEC_Exchange = '1' #汇
CEC_Cash = '2' #钞
T['YesNoIndicator'] = 'char' #是或否标识
YNI_Yes = '0' #是
YNI_No = '1' #否
T['BanlanceType'] = 'char' #余额类型
BLT_CurrentMoney = '0' #当前余额
BLT_UsableMoney = '1' #可用余额
BLT_FetchableMoney = '2' #可取余额
BLT_FreezeMoney = '3' #冻结余额
T['Gender'] = 'char' #性别
GD_Unknown = '0' #未知状态
GD_Male = '1' #男
GD_Female = '2' #女
T['FeePayFlag'] = 'char' #费用支付标志
FPF_BEN = '0' #由受益方支付费用
FPF_OUR = '1' #由发送方支付费用
FPF_SHA = '2' #由发送方支付发起的费用，受益方支付接受的费用
T['PassWordKeyType'] = 'char' #密钥类型
PWKT_ExchangeKey = '0' #交换密钥
PWKT_PassWordKey = '1' #密码密钥
PWKT_MACKey = '2' #MAC密钥
PWKT_MessageKey = '3' #报文密钥
T['FBTPassWordType'] = 'char' #密码类型
PWT_Query = '0' #查询
PWT_Fetch = '1' #取款
PWT_Transfer = '2' #转帐
PWT_Trade = '3' #交易
T['FBTEncryMode'] = 'char' #加密方式
EM_NoEncry = '0' #不加密
EM_DES = '1' #DES
EM_3DES = '2' #3DES
T['BankRepealFlag'] = 'char' #银行冲正标志
BRF_BankNotNeedRepeal = '0' #银行无需自动冲正
BRF_BankWaitingRepeal = '1' #银行待自动冲正
BRF_BankBeenRepealed = '2' #银行已自动冲正
T['BrokerRepealFlag'] = 'char' #期商冲正标志
BRORF_BrokerNotNeedRepeal = '0' #期商无需自动冲正
BRORF_BrokerWaitingRepeal = '1' #期商待自动冲正
BRORF_BrokerBeenRepealed = '2' #期商已自动冲正
T['InstitutionType'] = 'char' #机构类别
TS_Bank = '0' #银行
TS_Future = '1' #期商
TS_Store = '2' #券商
T['LastFragment'] = 'char' #最后分片标志
LF_Yes = '0' #是最后分片
LF_No = '1' #不是最后分片
T['BankAccStatus'] = 'char' #银行账户状态
BAS_Normal = '0' #正常
BAS_Freeze = '1' #冻结
BAS_ReportLoss = '2' #挂失
T['MoneyAccountStatus'] = 'char' #资金账户状态
MAS_Normal = '0' #正常
MAS_Cancel = '1' #销户
T['ManageStatus'] = 'char' #存管状态
MSS_Point = '0' #指定存管
MSS_PrePoint = '1' #预指定
MSS_CancelPoint = '2' #撤销指定
T['SystemType'] = 'char' #应用系统类型
SYT_FutureBankTransfer = '0' #银期转帐
SYT_StockBankTransfer = '1' #银证转帐
SYT_TheThirdPartStore = '2' #第三方存管
T['TxnEndFlag'] = 'char' #银期转帐划转结果标志
TEF_NormalProcessing = '0' #正常处理中
TEF_Success = '1' #成功结束
TEF_Failed = '2' #失败结束
TEF_Abnormal = '3' #异常中
TEF_ManualProcessedForException = '4' #已人工异常处理
TEF_CommuFailedNeedManualProcess = '5' #通讯异常 ，请人工处理
TEF_SysErrorNeedManualProcess = '6' #系统出错，请人工处理
T['ProcessStatus'] = 'char' #银期转帐服务处理状态
PSS_NotProcess = '0' #未处理
PSS_StartProcess = '1' #开始处理
PSS_Finished = '2' #处理完成
T['CustType'] = 'char' #客户类型
CUSTT_Person = '0' #自然人
CUSTT_Institution = '1' #机构户
T['FBTTransferDirection'] = 'char' #银期转帐方向
FBTTD_FromBankToFuture = '1' #入金，银行转期货
FBTTD_FromFutureToBank = '2' #出金，期货转银行
T['OpenOrDestroy'] = 'char' #开销户类别
OOD_Open = '1' #开户
OOD_Destroy = '0' #销户
T['AvailabilityFlag'] = 'char' #有效标志
AVAF_Invalid = '0' #未确认
AVAF_Valid = '1' #有效
AVAF_Repeal = '2' #冲正
T['OrganType'] = 'char' #机构类型
OT_Bank = '1' #银行代理
OT_Future = '2' #交易前置
OT_PlateForm = '9' #银期转帐平台管理
T['OrganLevel'] = 'char' #机构级别
OL_HeadQuarters = '1' #银行总行或期商总部
OL_Branch = '2' #银行分中心或期货公司营业部
T['ProtocalID'] = 'char' #协议类型
PID_FutureProtocal = '0' #期商协议
PID_ICBCProtocal = '1' #工行协议
PID_ABCProtocal = '2' #农行协议
PID_CBCProtocal = '3' #中国银行协议
PID_CCBProtocal = '4' #建行协议
PID_BOCOMProtocal = '5' #交行协议
PID_FBTPlateFormProtocal = 'X' #银期转帐平台协议
T['ConnectMode'] = 'char' #套接字连接方式
CM_ShortConnect = '0' #短连接
CM_LongConnect = '1' #长连接
T['SyncMode'] = 'char' #套接字通信方式
SRM_ASync = '0' #异步
SRM_Sync = '1' #同步
T['BankAccType'] = 'char' #银行帐号类型
BAT_BankBook = '1' #银行存折
BAT_SavingCard = '2' #储蓄卡
BAT_CreditCard = '3' #信用卡
T['FutureAccType'] = 'char' #期货公司帐号类型
FAT_BankBook = '1' #银行存折
FAT_SavingCard = '2' #储蓄卡
FAT_CreditCard = '3' #信用卡
T['OrganStatus'] = 'char' #接入机构状态
OS_Ready = '0' #启用
OS_CheckIn = '1' #签到
OS_CheckOut = '2' #签退
OS_CheckFileArrived = '3' #对帐文件到达
OS_CheckDetail = '4' #对帐
OS_DayEndClean = '5' #日终清理
OS_Invalid = '9' #注销
T['CCBFeeMode'] = 'char' #建行收费模式
CCBFM_ByAmount = '1' #按金额扣收
CCBFM_ByMonth = '2' #按月扣收
T['CommApiType'] = 'char' #通讯API类型
CAPIT_Client = '1' #客户端
CAPIT_Server = '2' #服务端
CAPIT_UserApi = '3' #交易系统的UserApi
T['ServiceID'] = 'int' #服务编号
T['ServiceLineNo'] = 'int' #服务线路编号
T['ServiceName'] = 'char[61]' #服务名
T['LinkStatus'] = 'char' #连接状态
LS_Connected = '1' #已经连接
LS_Disconnected = '2' #没有连接
T['CommApiPointer'] = 'int' #通讯API指针
T['PwdFlag'] = 'char' #密码核对标志
BPWDF_NoCheck = '0' #不核对
BPWDF_BlankCheck = '1' #明文核对
BPWDF_EncryptCheck = '2' #密文核对
T['SecuAccType'] = 'char' #期货帐号类型
SAT_AccountID = '1' #资金帐号
SAT_CardID = '2' #资金卡号
SAT_SHStockholderID = '3' #上海股东帐号
SAT_SZStockholderID = '4' #深圳股东帐号
T['TransferStatus'] = 'char' #转账交易状态
TRFS_Normal = '0' #正常
TRFS_Repealed = '1' #被冲正
T['SponsorType'] = 'char' #发起方
SPTYPE_Broker = '0' #期商
SPTYPE_Bank = '1' #银行
T['ReqRspType'] = 'char' #请求响应类别
REQRSP_Request = '0' #请求
REQRSP_Response = '1' #响应
T['FBTUserEventType'] = 'char' #银期转帐用户事件类型
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
T['BankIDByBank'] = 'char[21]' #银行自己的编码
T['NotifyClass'] = 'char' #风险通知类型
NC_NOERROR = '0' #正常
NC_Warn = '1' #警示
NC_Call = '2' #追保
NC_Force = '3' #强平
NC_CHUANCANG = '4' #穿仓
NC_Exception = '5' #异常
T['RiskNofityInfo'] = 'char[257]' #客户风险通知消息
T['ForceCloseSceneId'] = 'char[24]' #强平场景编号
T['ForceCloseType'] = 'char' #强平单类型
FCT_Manual = '0' #手工强平
FCT_Single = '1' #单一投资者辅助强平
FCT_Group = '2' #批量投资者辅助强平
T['InstrumentIDs'] = 'char[101]' #多个产品代码,用+分隔,如cu+zn
T['RiskNotifyMethod'] = 'char' #风险通知途径
RNM_System = '0' #系统通知
RNM_SMS = '1' #短信通知
RNM_EMail = '2' #邮件通知
T['RiskNotifyStatus'] = 'char' #风险通知状态
RNS_NotGen = '0' #未生成
RNS_Generated = '1' #已生成未发送
RNS_SendError = '2' #发送失败
RNS_SendOk = '3' #已发送未接收
RNS_Received = '4' #已接收未确认
RNS_Confirmed = '5' #已确认
T['RiskUserEvent'] = 'char' #风控用户操作事件
RUE_ExportData = '0' #导出数据
T['ConditionalOrderSortType'] = 'char' #条件单索引条件
COST_LastPriceAsc = '0' #使用最新价升序
COST_LastPriceDesc = '1' #使用最新价降序
COST_AskPriceAsc = '2' #使用卖价升序
COST_AskPriceDesc = '3' #使用卖价降序
COST_BidPriceAsc = '4' #使用买价升序
COST_BidPriceDesc = '5' #使用买价降序
T['SendType'] = 'char' #报送状态
UOAST_NoSend = '0' #未发送
UOAST_Sended = '1' #已发送
UOAST_Generated = '2' #已生成
UOAST_SendFail = '3' #报送失败
UOAST_Success = '4' #接收成功
UOAST_Fail = '5' #接收失败
UOAST_Cancel = '6' #取消报送
T['ClientIDStatus'] = 'char' #交易编码状态
UOACS_NoApply = '1' #未申请
UOACS_Submited = '2' #已提交申请
UOACS_Sended = '3' #已发送申请
UOACS_Success = '4' #完成
UOACS_Refuse = '5' #拒绝
UOACS_Cancel = '6' #已撤销编码
T['IndustryID'] = 'char[17]' #行业编码
T['QuestionID'] = 'char[5]' #特有信息编号
T['QuestionContent'] = 'char[41]' #特有信息说明
T['OptionID'] = 'char[13]' #选项编号
T['OptionContent'] = 'char[61]' #选项说明
T['QuestionType'] = 'char' #特有信息类型
QT_Radio = '1' #单选
QT_Option = '2' #多选
QT_Blank = '3' #填空
T['ProcessID'] = 'char[33]' #业务流水号
T['SeqNo'] = 'int' #流水号
T['UOAProcessStatus'] = 'char[3]' #流程状态
T['ProcessType'] = 'char' #流程功能类型
PT_ApplyTradingCode = '1' #申请交易编码
PT_CancelTradingCode = '2' #撤销交易编码
PT_ModifyIDCard = '3' #修改身份信息
PT_ModifyNoIDCard = '4' #修改一般信息
PT_ExchOpenBak = '5' #交易所开户报备
PT_ExchCancelBak = '6' #交易所销户报备
T['BusinessType'] = 'char' #业务类型
BT_Request = '1' #请求
BT_Response = '2' #应答
BT_Notice = '3' #通知
T['CfmmcReturnCode'] = 'char' #监控中心返回码
CRC_Success = '0' #成功
CRC_Working = '1' #该客户已经有流程在处理中
CRC_InfoFail = '2' #监控中客户资料检查失败
CRC_IDCardFail = '3' #监控中实名制检查失败
CRC_OtherFail = '4' #其他错误
T['ExReturnCode'] = 'int' #交易所返回码
T['ClientType'] = 'char' #客户类型
CfMMCCT_All = '0' #所有
CfMMCCT_Person = '1' #个人
CfMMCCT_Company = '2' #单位
T['ExchangeIDType'] = 'char' #交易所编号
EIDT_SHFE = 'S' #上海期货交易所
EIDT_CZCE = 'Z' #郑州商品交易所
EIDT_DCE = 'D' #大连商品交易所
EIDT_CFFEX = 'J' #中国金融期货交易所
T['ExClientIDType'] = 'char' #交易编码类型
ECIDT_Hedge = '1' #套保
ECIDT_Arbitrage = '2' #套利
ECIDT_Speculation = '3' #投机
T['ClientClassify'] = 'char[11]' #客户分类码
T['UOAOrganType'] = 'char[9]' #单位性质
T['UOACountryCode'] = 'char[9]' #国家代码
T['AreaCode'] = 'char[9]' #区号
T['FuturesID'] = 'char[21]' #监控中心为客户分配的代码
T['CffmcDate'] = 'char[11]' #日期
T['CffmcTime'] = 'char[11]' #时间
T['NocID'] = 'char[21]' #组织机构代码
T['UpdateFlag'] = 'char' #更新状态
UF_NoUpdate = '0' #未更新
UF_Success = '1' #更新全部信息成功
UF_Fail = '2' #更新全部信息失败
UF_TCSuccess = '3' #更新交易编码成功
UF_TCFail = '4' #更新交易编码失败
UF_Cancel = '5' #已丢弃
T['ApplyOperateID'] = 'char' #申请动作
AOID_OpenInvestor = '1' #开户
AOID_ModifyIDCard = '2' #修改身份信息
AOID_ModifyNoIDCard = '3' #修改一般信息
AOID_ApplyTradingCode = '4' #申请交易编码
AOID_CancelTradingCode = '5' #撤销交易编码
AOID_CancelInvestor = '6' #销户
T['ApplyStatusID'] = 'char' #申请状态
ASID_NoComplete = '1' #未补全
ASID_Submited = '2' #已提交
ASID_Checked = '3' #已审核
ASID_Refused = '4' #已拒绝
ASID_Deleted = '5' #已删除
T['SendMethod'] = 'char' #发送方式
UOASM_ByAPI = '1' #电子发送
UOASM_ByFile = '2' #文件发送
T['EventType'] = 'char[33]' #业务操作类型
T['EventMode'] = 'char' #操作方法
EvM_ADD = '1' #增加
EvM_UPDATE = '2' #修改
EvM_DELETE = '3' #删除
EvM_CHECK = '4' #复核
T['UOAAutoSend'] = 'char' #统一开户申请自动发送
UOAA_ASR = '1' #自动发送并接收
UOAA_ASNR = '2' #自动发送，不自动接收
UOAA_NSAR = '3' #不自动发送，自动接收
UOAA_NSR = '4' #不自动发送，也不自动接收
T['QueryDepth'] = 'int' #查询深度
T['DataCenterID'] = 'int' #数据中心代码
T['FlowID'] = 'char' #流程ID
EvM_InvestorGroupFlow = '1' #投资者对应投资者组设置
T['CheckLevel'] = 'char' #复核级别
CL_Zero = '0' #零级复核
CL_One = '1' #一级复核
CL_Two = '2' #二级复核
T['CheckNo'] = 'int' #操作次数
T['CheckStatus'] = 'char' #复核级别
CHS_Init = '0' #未复核
CHS_Checking = '1' #复核中
CHS_Checked = '2' #已复核
CHS_Refuse = '3' #拒绝
CHS_Cancel = '4' #作废
T['UsedStatus'] = 'char' #生效状态
CHU_Unused = '0' #未生效
CHU_Used = '1' #已生效
CHU_Fail = '2' #生效失败
T['RateTemplateName'] = 'char[61]' #模型名称
T['PropertyString'] = 'char[2049]' #用于查询的投资属性字段
T['BankAcountOrigin'] = 'char' #账户来源
BAO_ByAccProperty = '0' #手工录入
BAO_ByFBTransfer = '1' #银期转账
T['MonthBillTradeSum'] = 'char' #结算单月报成交汇总方式
MBTS_ByInstrument = '0' #同日同合约
MBTS_ByDayInsPrc = '1' #同日同合约同价格
MBTS_ByDayIns = '2' #同合约
T['FBTTradeCodeEnum'] = 'char[7]' #银期交易代码枚举
FTC_BankLaunchBankToBroker = '102001' #银行发起银行转期货
FTC_BrokerLaunchBankToBroker = '202001' #期货发起银行转期货
FTC_BankLaunchBrokerToBank = '102002' #银行发起期货转银行
FTC_BrokerLaunchBrokerToBank = '202002' #期货发起期货转银行
T['RateTemplateID'] = 'char[9]' #模型代码
T['RiskRate'] = 'char[21]' #风险度
T['Timestamp'] = 'int' #时间戳
T['InvestorIDRuleName'] = 'char[61]' #号段规则名称
T['InvestorIDRuleExpr'] = 'char[513]' #号段规则表达式
T['LastDrift'] = 'int' #上次OTP漂移值
T['LastSuccess'] = 'int' #上次OTP成功值
T['AuthKey'] = 'char[41]' #令牌密钥
T['SerialNumber'] = 'char[17]' #序列号
T['OTPType'] = 'char' #动态令牌类型
OTP_NONE = '0' #无动态令牌
OTP_TOTP = '1' #时间令牌
T['OTPVendorsID'] = 'char[2]' #动态令牌提供商
T['OTPVendorsName'] = 'char[61]' #动态令牌提供商名称
T['OTPStatus'] = 'char' #动态令牌状态
OTPS_Unused = '0' #未使用
OTPS_Used = '1' #已使用
OTPS_Disuse = '2' #注销
T['BrokerUserType'] = 'char' #经济公司用户类型
BUT_Investor = '1' #投资者
T['FutureType'] = 'char' #期货类型
FUTT_Commodity = '1' #商品期货
FUTT_Financial = '2' #金融期货
T['FundEventType'] = 'char' #资金管理操作类型
FET_Restriction = '0' #转账限额
FET_TodayRestriction = '1' #当日转账限额
FET_Transfer = '2' #期商流水
FET_Credit = '3' #资金冻结
FET_InvestorWithdrawAlm = '4' #投资者可提资金比例
T['AccountSourceType'] = 'char' #资金账户来源
AST_FBTransfer = '0' #银期同步
AST_ManualEntry = '1' #手工录入
T['CodeSourceType'] = 'char' #交易编码来源
CST_UnifyAccount = '0' #统一开户
CST_ManualEntry = '1' #手工录入
T['UserRange'] = 'char' #操作员范围
UR_All = '0' #所有
UR_Single = '1' #单一操作员
T['TimeSpan'] = 'char[9]' #时间跨度
T['ImportSequenceID'] = 'char[17]' #动态令牌导入批次编号
T['BranchID'] = 'char[9]' #营业部编号
T['TableName'] = 'char[17]' #和交易所交换表编号
T['StockPrice'] = 'char[9]' #证券交易价格
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
T['StockSeq'] = 'char[11]' #股票使用流水号
T['StockWth'] = 'int' #股票使用流水号
T['WTFS'] = 'int' #委托方式
T['WTLB'] = 'int' #委托类别
T['WTRQ'] = 'int' #委托日期
T['CreationredemptionStatus'] = 'char' #基金当天申购赎回状态
CDS_Forbidden = '0' #不允许申购赎回
CDS_Allow = '1' #表示允许申购和赎回
CDS_OnlyPurchase = '2' #允许申购、不允许赎回
CDS_OnlyRedeem = '3' #不允许申购、允许赎回
T['ETFCurrenceReplaceStatus'] = 'char' #ETF现金替代标志
ETFCRS_Forbidden = '0' #禁止现金替代
ETFCRS_Allow = '1' #可以现金替代
ETFCRS_Force = '2' #必须现金替代
T['INTEGER'] = 'int' #一般整型
T['INT3'] = 'int' #三位数整型
T['INT6'] = 'int' #六位数整型
T['REAL9P3'] = 'double' #九点三实型
T['REAL10P4'] = 'double' #十点四实型
T['REAL16P2'] = 'double' #十六点二实型
T['REAL16P8'] = 'double' #十六点八实型
T['REAL22P2'] = 'double' #二十二点二实型
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
T['AuthInfo'] = 'char[129]' #客户端认证信息
T['AuthCode'] = 'char[17]' #客户端认证码

class BaseStruct(object):
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join('%s=%r'%(k,getattr(self,k)) for k,t in self._fields_))

class Dissemination(BaseStruct): #信息分发
    def __init__(self, SequenceSeries=0, SequenceNo=0):
        self.SequenceSeries = '' #序列系列号, short
        self.SequenceNo = '' #序列号, int

class ReqUserLogin(BaseStruct): #用户登录请求
    def __init__(self, TradingDay='', BrokerID='', UserID='', Password='', UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', MacAddress='', OneTimePassword='', ClientIPAddress=''):
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

class RspUserLogin(BaseStruct): #用户登录应答
    def __init__(self, TradingDay='', LoginTime='', BrokerID='', UserID='', SystemName='', FrontID=0, SessionID=0, MaxOrderRef='', SHFETime='', DCETime='', CZCETime='', FFEXTime=''):
        self.TradingDay = 'Date' #交易日, char[9]
        self.LoginTime = 'Time' #登录成功时间, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.SystemName = '' #交易系统名称, char[41]
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.MaxOrderRef = 'OrderRef' #最大报单引用, char[13]
        self.SHFETime = 'Time' #上期所时间, char[9]
        self.DCETime = 'Time' #大商所时间, char[9]
        self.CZCETime = 'Time' #郑商所时间, char[9]
        self.FFEXTime = 'Time' #中金所时间, char[9]

class UserLogout(BaseStruct): #用户登出请求
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class ForceUserLogout(BaseStruct): #强制交易员退出
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class ReqAuthenticate(BaseStruct): #客户端认证请求
    def __init__(self, BrokerID='', UserID='', UserProductInfo='', AuthCode=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserProductInfo = 'ProductInfo' #用户端产品信息, char[11]
        self.AuthCode = '' #认证码, char[17]

class RspAuthenticate(BaseStruct): #客户端认证响应
    def __init__(self, BrokerID='', UserID='', UserProductInfo=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserProductInfo = 'ProductInfo' #用户端产品信息, char[11]

class AuthenticationInfo(BaseStruct): #客户端认证信息
    def __init__(self, BrokerID='', UserID='', UserProductInfo='', AuthInfo='', IsResult=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserProductInfo = 'ProductInfo' #用户端产品信息, char[11]
        self.AuthInfo = '' #认证信息, char[129]
        self.IsResult = 'Bool' #是否为认证结果, int

class TransferHeader(BaseStruct): #银期转帐报文头
    def __init__(self, Version='', TradeCode='', TradeDate='', TradeTime='', TradeSerial='', FutureID='', BankID='', BankBrchID='', OperNo='', DeviceID='', RecordNum='', SessionID=0, RequestID=0):
        self.Version = '' #版本号，常量，1.0, char[4]
        self.TradeCode = '' #交易代码，必填, char[7]
        self.TradeDate = '' #交易日期，必填，格式：yyyymmdd, char[9]
        self.TradeTime = '' #交易时间，必填，格式：hhmmss, char[9]
        self.TradeSerial = '' #发起方流水号，N/A, char[9]
        self.FutureID = '' #期货公司代码，必填, char[11]
        self.BankID = '' #银行代码，根据查询银行得到，必填, char[4]
        self.BankBrchID = '' #银行分中心代码，根据查询银行得到，必填, char[5]
        self.OperNo = '' #操作员，N/A, char[17]
        self.DeviceID = '' #交易设备类型，N/A, char[3]
        self.RecordNum = '' #记录数，N/A, char[7]
        self.SessionID = '' #会话编号，N/A, int
        self.RequestID = '' #请求编号，N/A, int

class TransferBankToFutureReq(BaseStruct): #银行资金转期货请求，TradeCode=202001
    def __init__(self, FutureAccount='', FuturePwdFlag=FPWD_UnCheck, FutureAccPwd='', TradeAmt=0.0, CustFee=0.0, CurrencyCode=''):
        self.FutureAccount = 'AccountID' #期货资金账户, char[15]
        self.FuturePwdFlag = '' #密码标志, char
        self.FutureAccPwd = '' #密码, char[17]
        self.TradeAmt = 'Money' #转账金额, double
        self.CustFee = 'Money' #客户手续费, double
        self.CurrencyCode = '' #币种：RMB-人民币 USD-美圆 HKD-港元, char[4]

class TransferBankToFutureRsp(BaseStruct): #银行资金转期货请求响应
    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt=0.0, CustFee=0.0, CurrencyCode=''):
        self.RetCode = '' #响应代码, char[5]
        self.RetInfo = '' #响应信息, char[129]
        self.FutureAccount = 'AccountID' #资金账户, char[15]
        self.TradeAmt = 'Money' #转帐金额, double
        self.CustFee = 'Money' #应收客户手续费, double
        self.CurrencyCode = '' #币种, char[4]

class TransferFutureToBankReq(BaseStruct): #期货资金转银行请求，TradeCode=202002
    def __init__(self, FutureAccount='', FuturePwdFlag=FPWD_UnCheck, FutureAccPwd='', TradeAmt=0.0, CustFee=0.0, CurrencyCode=''):
        self.FutureAccount = 'AccountID' #期货资金账户, char[15]
        self.FuturePwdFlag = '' #密码标志, char
        self.FutureAccPwd = '' #密码, char[17]
        self.TradeAmt = 'Money' #转账金额, double
        self.CustFee = 'Money' #客户手续费, double
        self.CurrencyCode = '' #币种：RMB-人民币 USD-美圆 HKD-港元, char[4]

class TransferFutureToBankRsp(BaseStruct): #期货资金转银行请求响应
    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt=0.0, CustFee=0.0, CurrencyCode=''):
        self.RetCode = '' #响应代码, char[5]
        self.RetInfo = '' #响应信息, char[129]
        self.FutureAccount = 'AccountID' #资金账户, char[15]
        self.TradeAmt = 'Money' #转帐金额, double
        self.CustFee = 'Money' #应收客户手续费, double
        self.CurrencyCode = '' #币种, char[4]

class TransferQryBankReq(BaseStruct): #查询银行资金请求，TradeCode=204002
    def __init__(self, FutureAccount='', FuturePwdFlag=FPWD_UnCheck, FutureAccPwd='', CurrencyCode=''):
        self.FutureAccount = 'AccountID' #期货资金账户, char[15]
        self.FuturePwdFlag = '' #密码标志, char
        self.FutureAccPwd = '' #密码, char[17]
        self.CurrencyCode = '' #币种：RMB-人民币 USD-美圆 HKD-港元, char[4]

class TransferQryBankRsp(BaseStruct): #查询银行资金请求响应
    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt=0.0, UseAmt=0.0, FetchAmt=0.0, CurrencyCode=''):
        self.RetCode = '' #响应代码, char[5]
        self.RetInfo = '' #响应信息, char[129]
        self.FutureAccount = 'AccountID' #资金账户, char[15]
        self.TradeAmt = 'Money' #银行余额, double
        self.UseAmt = 'Money' #银行可用余额, double
        self.FetchAmt = 'Money' #银行可取余额, double
        self.CurrencyCode = '' #币种, char[4]

class TransferQryDetailReq(BaseStruct): #查询银行交易明细请求，TradeCode=204999
    def __init__(self, FutureAccount=''):
        self.FutureAccount = 'AccountID' #期货资金账户, char[15]

class TransferQryDetailRsp(BaseStruct): #查询银行交易明细请求响应
    def __init__(self, TradeDate='', TradeTime='', TradeCode='', FutureSerial=0, FutureID='', FutureAccount='', BankSerial=0, BankID='', BankBrchID='', BankAccount='', CertCode='', CurrencyCode='', TxAmount=0.0, Flag=TVF_Invalid):
        self.TradeDate = 'Date' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.TradeCode = '' #交易代码, char[7]
        self.FutureSerial = 'TradeSerialNo' #期货流水号, int
        self.FutureID = '' #期货公司代码, char[11]
        self.FutureAccount = '' #资金帐号, char[22]
        self.BankSerial = 'TradeSerialNo' #银行流水号, int
        self.BankID = '' #银行代码, char[4]
        self.BankBrchID = '' #银行分中心代码, char[5]
        self.BankAccount = '' #银行账号, char[41]
        self.CertCode = '' #证件号码, char[21]
        self.CurrencyCode = '' #货币代码, char[4]
        self.TxAmount = 'Money' #发生金额, double
        self.Flag = 'TransferValidFlag' #有效标志, char

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
    def __init__(self, InstrumentID='', ExchangeID='', InstrumentName='', ExchangeInstID='', ProductID='', ProductClass=PC_Futures, DeliveryYear=0, DeliveryMonth=0, MaxMarketOrderVolume=0, MinMarketOrderVolume=0, MaxLimitOrderVolume=0, MinLimitOrderVolume=0, VolumeMultiple=0, PriceTick=0.0, CreateDate='', OpenDate='', ExpireDate='', StartDelivDate='', EndDelivDate='', InstLifePhase=IP_NotStart, IsTrading=0, PositionType=PT_Net, PositionDateType=PDT_UseHistory, LongMarginRatio=0.0, ShortMarginRatio=0.0, OrderCanBeWithdraw=0, MinBuyVolume=0, MinSellVolume=0):
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
        self.PositionDateType = '' #持仓日期类型, char
        self.LongMarginRatio = 'Ratio' #多头保证金率, double
        self.ShortMarginRatio = 'Ratio' #空头保证金率, double
        self.OrderCanBeWithdraw = 'Bool' #报单能否撤单, int
        self.MinBuyVolume = 'Volume' #最小买下单单位, int
        self.MinSellVolume = 'Volume' #最小卖下单单位, int

class Broker(BaseStruct): #经纪公司
    def __init__(self, BrokerID='', BrokerAbbr='', BrokerName='', IsActive=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.BrokerAbbr = '' #经纪公司简称, char[9]
        self.BrokerName = '' #经纪公司名称, char[81]
        self.IsActive = 'Bool' #是否活跃, int

class Trader(BaseStruct): #交易所交易员
    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallCount=0, BrokerID='', BranchID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.TraderID = '' #交易所交易员代码, char[21]
        self.ParticipantID = '' #会员代码, char[11]
        self.Password = '' #密码, char[41]
        self.InstallCount = '' #安装数量, int
        self.BrokerID = '' #经纪公司代码, char[11]
        self.BranchID = '' #营业部编号, char[9]

class Investor(BaseStruct): #投资者
    def __init__(self, InvestorID='', BrokerID='', InvestorGroupID='', InvestorName='', IdentifiedCardType=ICT_EID, IdentifiedCardNo='', IsActive=0, Telephone='', Address='', OpenDate='', Mobile='', SHBranchID='', SZBranchID='', IsCreditAccount=0):
        self.InvestorID = '' #投资者代码, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorGroupID = 'InvestorID' #投资者分组代码, char[15]
        self.InvestorName = 'PartyName' #投资者名称, char[81]
        self.IdentifiedCardType = 'IdCardType' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.IsActive = 'Bool' #是否活跃, int
        self.Telephone = '' #联系电话, char[41]
        self.Address = '' #通讯地址, char[101]
        self.OpenDate = 'Date' #开户日期, char[9]
        self.Mobile = '' #手机, char[41]
        self.SHBranchID = 'BranchID' #上海营业部编号, char[9]
        self.SZBranchID = 'BranchID' #深圳营业部编号, char[9]
        self.IsCreditAccount = 'Bool' #是否信用账户, int

class TradingCode(BaseStruct): #交易编码
    def __init__(self, InvestorID='', BrokerID='', ExchangeID='', ClientID='', IsActive=0):
        self.InvestorID = '' #投资者代码, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ClientID = '' #客户代码, char[11]
        self.IsActive = 'Bool' #是否活跃, int

class PartBroker(BaseStruct): #会员编码和经纪公司编码对照表
    def __init__(self, BrokerID='', ExchangeID='', ParticipantID='', IsActive=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ParticipantID = '' #会员代码, char[11]
        self.IsActive = 'Bool' #是否活跃, int

class SuperUser(BaseStruct): #管理用户
    def __init__(self, UserID='', UserName='', Password='', IsActive=0):
        self.UserID = '' #用户代码, char[16]
        self.UserName = '' #用户名称, char[81]
        self.Password = '' #密码, char[41]
        self.IsActive = 'Bool' #是否活跃, int

class SuperUserFunction(BaseStruct): #管理用户功能权限
    def __init__(self, UserID='', FunctionCode=FC_DataAsync):
        self.UserID = '' #用户代码, char[16]
        self.FunctionCode = '' #功能代码, char

class InvestorGroup(BaseStruct): #投资者组
    def __init__(self, BrokerID='', InvestorGroupID='', InvestorGroupName=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorGroupID = 'InvestorID' #投资者分组代码, char[15]
        self.InvestorGroupName = '' #投资者分组名称, char[41]

class TradingAccount(BaseStruct): #资金账户
    def __init__(self, BrokerID='', AccountID='', PreMortgage=0.0, PreCredit=0.0, PreDeposit=0.0, PreBalance=0.0, PreMargin=0.0, InterestBase=0.0, Interest=0.0, Deposit=0.0, Withdraw=0.0, FrozenMargin=0.0, FrozenCash=0.0, FrozenCommission=0.0, CurrMargin=0.0, CashIn=0.0, Commission=0.0, CloseProfit=0.0, PositionProfit=0.0, Balance=0.0, Available=0.0, WithdrawQuota=0.0, Reserve=0.0, TradingDay='', SettlementID=0, Credit=0.0, Mortgage=0.0, ExchangeMargin=0.0, DeliveryMargin=0.0, ExchangeDeliveryMargin=0.0, FrozenTransferFee=0.0, FrozenStampTax=0.0, TransferFee=0.0, StampTax=0.0, ConversionAmount=0.0, CreditAmount=0.0, LowLimitRatio=0.0, MarginTradingAmount=0.0, ShortSellingAmount=0.0, MarginTradingAvail=0.0, ShortSellingAvail=0.0, CreditRatio=0.0, StockValue=0.0):
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
        self.CloseProfit = 'Money' #平仓盈亏, double
        self.PositionProfit = 'Money' #持仓盈亏, double
        self.Balance = 'Money' #期货结算准备金, double
        self.Available = 'Money' #可用资金, double
        self.WithdrawQuota = 'Money' #可取资金, double
        self.Reserve = 'Money' #基本准备金, double
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
        self.Credit = 'Money' #信用额度, double
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
        self.LowLimitRatio = 'Ratio' #最低维持担保比例, double
        self.MarginTradingAmount = 'Money' #融资买入金额, double
        self.ShortSellingAmount = 'Money' #融券卖出金额, double
        self.MarginTradingAvail = 'Money' #融资买入可用金额, double
        self.ShortSellingAvail = 'Money' #融券卖出可用金额, double
        self.CreditRatio = 'Ratio' #维持担保比例, double
        self.StockValue = 'Money' #证券总价值, double

class InvestorPosition(BaseStruct): #投资者持仓
    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', PosiDirection=PD_Net, HedgeFlag=HF_Speculation, PositionDate=PSD_Today, YdPosition=0, Position=0, LongFrozen=0, ShortFrozen=0, LongFrozenAmount=0.0, ShortFrozenAmount=0.0, OpenVolume=0, CloseVolume=0, OpenAmount=0.0, CloseAmount=0.0, PositionCost=0.0, FrozenCash=0.0, CashIn=0.0, Commission=0.0, CloseProfit=0.0, PositionProfit=0.0, PreSettlementPrice=0.0, SettlementPrice=0.0, TradingDay='', SettlementID=0, OpenCost=0.0, ExchangeMargin=0.0, TodayPosition=0, TransferFee=0.0, StampTax=0.0, TodayPurRedVolume=0, ConversionRate=0.0, ConversionAmount=0.0, MarginTradeVolume=0, MarginTradeAmount=0.0, MarginTradeFrozenVolume=0, MarginTradeFrozenAmount=0.0, MarginTradeConversionAmount=0.0, ShortSellVolume=0, ShortSellAmount=0.0, ShortSellConversionAmount=0.0, ShortSellFrozenVolume=0, ShortSellFrozenAmount=0.0, StockValue=0.0, ExchangeID=''):
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
        self.CloseProfit = 'Money' #平仓盈亏, double
        self.PositionProfit = 'Money' #持仓盈亏, double
        self.PreSettlementPrice = 'Price' #上次结算价, double
        self.SettlementPrice = 'Price' #本次结算价, double
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
        self.OpenCost = 'Money' #开仓成本, double
        self.ExchangeMargin = 'Money' #交易所保证金, double
        self.TodayPosition = 'Volume' #今日持仓, int
        self.TransferFee = 'Money' #过户费, double
        self.StampTax = 'Money' #印花税, double
        self.TodayPurRedVolume = 'Volume' #今日申购赎回数量, int
        self.ConversionRate = 'Ratio' #折算率, double
        self.ConversionAmount = 'Money' #折算金额, double
        self.MarginTradeVolume = 'Volume' #融资买入出数量, int
        self.MarginTradeAmount = 'Money' #融资买入金额, double
        self.MarginTradeFrozenVolume = 'Volume' #融资买入冻结数量, int
        self.MarginTradeFrozenAmount = 'Money' #融资买入冻结金额, double
        self.MarginTradeConversionAmount = 'Money' #融资买入折算金额, double
        self.ShortSellVolume = 'Volume' #融券卖出数量, int
        self.ShortSellAmount = 'Money' #融券卖出金额, double
        self.ShortSellConversionAmount = 'Money' #融券卖出折算金额, double
        self.ShortSellFrozenVolume = 'Volume' #融券卖出冻结数量, int
        self.ShortSellFrozenAmount = 'Money' #融券卖出冻结金额, double
        self.StockValue = 'Money' #证券价值, double
        self.ExchangeID = '' #交易所代码, char[9]

class InstrumentMarginRate(BaseStruct): #合约保证金率
    def __init__(self, InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', HedgeFlag=HF_Speculation, LongMarginRatioByMoney=0.0, LongMarginRatioByVolume=0.0, ShortMarginRatioByMoney=0.0, ShortMarginRatioByVolume=0.0, IsRelative=0):
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.HedgeFlag = '' #投机套保标志, char
        self.LongMarginRatioByMoney = 'Ratio' #多头保证金率, double
        self.LongMarginRatioByVolume = 'Money' #多头保证金费, double
        self.ShortMarginRatioByMoney = 'Ratio' #空头保证金率, double
        self.ShortMarginRatioByVolume = 'Money' #空头保证金费, double
        self.IsRelative = 'Bool' #是否相对交易所收取, int

class InstrumentCommissionRate(BaseStruct): #合约手续费率
    def __init__(self, InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', BuyStampTaxRateByMoney=0.0, BuyStampTaxRateByVolume=0.0, SellStampTaxRateByMoney=0.0, SellStampTaxRateByVolume=0.0, BuyTransferFeeRateByMoney=0.0, BuyTransferFeeRateByVolume=0.0, SellTransferFeeRateByMoney=0.0, SellTransferFeeRateByVolume=0.0, BuyTradeFeeByMoney=0.0, BuyTradeFeeByVolume=0.0, SellTradeFeeByMoney=0.0, SellTradeFeeByVolume=0.0, BuyMarginByMoney=0.0, SellMarginByMoney=0.0, MinTradeFee=0.0):
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.BuyStampTaxRateByMoney = 'Ratio' #买印花税率, double
        self.BuyStampTaxRateByVolume = 'Ratio' #买印花税率(按手数), double
        self.SellStampTaxRateByMoney = 'Ratio' #卖印花税率, double
        self.SellStampTaxRateByVolume = 'Ratio' #卖印花税率(按手数), double
        self.BuyTransferFeeRateByMoney = 'Ratio' #买过户费率, double
        self.BuyTransferFeeRateByVolume = 'Ratio' #买过户费率(按手数), double
        self.SellTransferFeeRateByMoney = 'Ratio' #卖过户费率, double
        self.SellTransferFeeRateByVolume = 'Ratio' #卖过户费率(按手数), double
        self.BuyTradeFeeByMoney = 'Ratio' #买交易费, double
        self.BuyTradeFeeByVolume = 'Ratio' #买交易费(按手数), double
        self.SellTradeFeeByMoney = 'Ratio' #卖交易费率, double
        self.SellTradeFeeByVolume = 'Ratio' #卖交易费率(按手数), double
        self.BuyMarginByMoney = 'Ratio' #买交易附加费率, double
        self.SellMarginByMoney = 'Ratio' #卖交易附加费率, double
        self.MinTradeFee = 'Price' #最小过户费, double

class DepthMarketData(BaseStruct): #深度行情
    def __init__(self, TradingDay='', InstrumentID='', ExchangeID='', ExchangeInstID='', LastPrice=0.0, PreSettlementPrice=0.0, PreClosePrice=0.0, PreOpenInterest=0.0, OpenPrice=0.0, HighestPrice=0.0, LowestPrice=0.0, Volume=0, Turnover=0.0, OpenInterest=0.0, ClosePrice=0.0, SettlementPrice=0.0, UpperLimitPrice=0.0, LowerLimitPrice=0.0, PreDelta=0.0, CurrDelta=0.0, UpdateTime='', UpdateMillisec=0, BidPrice1=0.0, BidVolume1=0, AskPrice1=0.0, AskVolume1=0, BidPrice2=0.0, BidVolume2=0, AskPrice2=0.0, AskVolume2=0, BidPrice3=0.0, BidVolume3=0, AskPrice3=0.0, AskVolume3=0, BidPrice4=0.0, BidVolume4=0, AskPrice4=0.0, AskVolume4=0, BidPrice5=0.0, BidVolume5=0, AskPrice5=0.0, AskVolume5=0, AveragePrice=0.0):
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

class InstrumentTradingRight(BaseStruct): #投资者合约交易权限
    def __init__(self, InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', Direction=D_Buy, TradingRight=TR_Allow, ExchangeID=''):
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.Direction = '' #买卖, char
        self.TradingRight = '' #交易权限, char
        self.ExchangeID = '' #交易所代码, char[9]

class BrokerUser(BaseStruct): #经纪公司用户
    def __init__(self, BrokerID='', UserID='', UserName='', UserType=UT_Investor, IsActive=0, IsUsingOTP=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserName = '' #用户名称, char[81]
        self.UserType = '' #用户类型, char
        self.IsActive = 'Bool' #是否活跃, int
        self.IsUsingOTP = 'Bool' #是否使用令牌, int

class BrokerUserPassword(BaseStruct): #经纪公司用户口令
    def __init__(self, BrokerID='', UserID='', Password=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.Password = '' #密码, char[41]

class BrokerUserFunction(BaseStruct): #经纪公司用户功能权限
    def __init__(self, BrokerID='', UserID='', BrokerFunctionCode=BFC_ForceUserLogout):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.BrokerFunctionCode = '' #经纪公司功能代码, char

class TraderOffer(BaseStruct): #交易所交易员报盘机
    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallID=0, OrderLocalID='', TraderConnectStatus=TCS_NotConnected, ConnectRequestDate='', ConnectRequestTime='', LastReportDate='', LastReportTime='', ConnectDate='', ConnectTime='', StartDate='', StartTime='', TradingDay='', BrokerID='', BranchID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.TraderID = '' #交易所交易员代码, char[21]
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
        self.BranchID = '' #营业部编号, char[9]

class SettlementInfo(BaseStruct): #投资者结算结果
    def __init__(self, TradingDay='', SettlementID=0, BrokerID='', InvestorID='', SequenceNo=0, Content=''):
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.SequenceNo = '' #序号, int
        self.Content = '' #消息正文, char[501]

class InstrumentMarginRateAdjust(BaseStruct): #合约保证金率调整
    def __init__(self, InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', HedgeFlag=HF_Speculation, LongMarginRatioByMoney=0.0, LongMarginRatioByVolume=0.0, ShortMarginRatioByMoney=0.0, ShortMarginRatioByVolume=0.0, IsRelative=0):
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.HedgeFlag = '' #投机套保标志, char
        self.LongMarginRatioByMoney = 'Ratio' #多头保证金率, double
        self.LongMarginRatioByVolume = 'Money' #多头保证金费, double
        self.ShortMarginRatioByMoney = 'Ratio' #空头保证金率, double
        self.ShortMarginRatioByVolume = 'Money' #空头保证金费, double
        self.IsRelative = 'Bool' #是否相对交易所收取, int

class ExchangeMarginRate(BaseStruct): #交易所保证金率
    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag=HF_Speculation, LongMarginRatioByMoney=0.0, LongMarginRatioByVolume=0.0, ShortMarginRatioByMoney=0.0, ShortMarginRatioByVolume=0.0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InstrumentID = '' #合约代码, char[31]
        self.HedgeFlag = '' #投机套保标志, char
        self.LongMarginRatioByMoney = 'Ratio' #多头保证金率, double
        self.LongMarginRatioByVolume = 'Money' #多头保证金费, double
        self.ShortMarginRatioByMoney = 'Ratio' #空头保证金率, double
        self.ShortMarginRatioByVolume = 'Money' #空头保证金费, double

class ExchangeMarginRateAdjust(BaseStruct): #交易所保证金率调整
    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag=HF_Speculation, LongMarginRatioByMoney=0.0, LongMarginRatioByVolume=0.0, ShortMarginRatioByMoney=0.0, ShortMarginRatioByVolume=0.0, ExchLongMarginRatioByMoney=0.0, ExchLongMarginRatioByVolume=0.0, ExchShortMarginRatioByMoney=0.0, ExchShortMarginRatioByVolume=0.0, NoLongMarginRatioByMoney=0.0, NoLongMarginRatioByVolume=0.0, NoShortMarginRatioByMoney=0.0, NoShortMarginRatioByVolume=0.0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InstrumentID = '' #合约代码, char[31]
        self.HedgeFlag = '' #投机套保标志, char
        self.LongMarginRatioByMoney = 'Ratio' #跟随交易所投资者多头保证金率, double
        self.LongMarginRatioByVolume = 'Money' #跟随交易所投资者多头保证金费, double
        self.ShortMarginRatioByMoney = 'Ratio' #跟随交易所投资者空头保证金率, double
        self.ShortMarginRatioByVolume = 'Money' #跟随交易所投资者空头保证金费, double
        self.ExchLongMarginRatioByMoney = 'Ratio' #交易所多头保证金率, double
        self.ExchLongMarginRatioByVolume = 'Money' #交易所多头保证金费, double
        self.ExchShortMarginRatioByMoney = 'Ratio' #交易所空头保证金率, double
        self.ExchShortMarginRatioByVolume = 'Money' #交易所空头保证金费, double
        self.NoLongMarginRatioByMoney = 'Ratio' #不跟随交易所投资者多头保证金率, double
        self.NoLongMarginRatioByVolume = 'Money' #不跟随交易所投资者多头保证金费, double
        self.NoShortMarginRatioByMoney = 'Ratio' #不跟随交易所投资者空头保证金率, double
        self.NoShortMarginRatioByVolume = 'Money' #不跟随交易所投资者空头保证金费, double

class SettlementRef(BaseStruct): #结算引用
    def __init__(self, TradingDay='', SettlementID=0):
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int

class CurrentTime(BaseStruct): #当前时间
    def __init__(self, CurrDate='', CurrTime='', CurrMillisec=0):
        self.CurrDate = 'Date' #当前日期, char[9]
        self.CurrTime = 'Time' #当前时间, char[9]
        self.CurrMillisec = 'Millisec' #当前时间（毫秒）, int

class CommPhase(BaseStruct): #通讯阶段
    def __init__(self, TradingDay='', CommPhaseNo=0):
        self.TradingDay = 'Date' #交易日, char[9]
        self.CommPhaseNo = '' #通讯时段编号, short

class LoginInfo(BaseStruct): #登录信息
    def __init__(self, FrontID=0, SessionID=0, BrokerID='', UserID='', LoginDate='', LoginTime='', IPAddress='', UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', SystemName='', Password='', MaxOrderRef='', MacAddress='', OneTimePassword=''):
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
        self.SystemName = '' #系统名称, char[41]
        self.Password = '' #密码, char[41]
        self.MaxOrderRef = 'OrderRef' #最大报单引用, char[13]
        self.MacAddress = '' #Mac地址, char[21]
        self.OneTimePassword = 'Password' #动态密码, char[41]

class LogoutAll(BaseStruct): #登录信息
    def __init__(self, FrontID=0, SessionID=0, SystemName=''):
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.SystemName = '' #系统名称, char[41]

class FrontStatus(BaseStruct): #前置状态
    def __init__(self, FrontID=0, LastReportDate='', LastReportTime='', IsActive=0):
        self.FrontID = '' #前置编号, int
        self.LastReportDate = 'Date' #上次报告日期, char[9]
        self.LastReportTime = 'Time' #上次报告时间, char[9]
        self.IsActive = 'Bool' #是否活跃, int

class UserPasswordUpdate(BaseStruct): #用户口令变更
    def __init__(self, BrokerID='', UserID='', OldPassword='', NewPassword=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.OldPassword = 'Password' #原来的口令, char[41]
        self.NewPassword = 'Password' #新的口令, char[41]

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
        self.LimitPrice = 'StockPrice' #价格, char[9]
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

class Order(BaseStruct): #报单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', OrderPriceType=OPT_AnyPrice, Direction=D_Buy, CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal=0, TimeCondition=TC_IOC, GTDDate='', VolumeCondition=VC_AV, MinVolume=0, ContingentCondition=CC_Immediately, StopPrice=0.0, ForceCloseReason=FCC_NotForceClose, IsAutoSuspend=0, BusinessUnit='', RequestID=0, OrderLocalID='', ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID=0, OrderSubmitStatus=OSS_InsertSubmitted, NotifySequence=0, TradingDay='', SettlementID=0, OrderSysID='', OrderSource=OSRC_Participant, OrderStatus=OST_AllTraded, OrderType=ORDT_Normal, VolumeTraded=0, VolumeTotal=0, InsertDate='', InsertTime='', ActiveTime='', SuspendTime='', UpdateTime='', CancelTime='', ActiveTraderID='', ClearingPartID='', SequenceNo=0, FrontID=0, SessionID=0, UserProductInfo='', StatusMsg='', UserForceClose=0, ActiveUserID='', BrokerOrderSeq=0, RelativeOrderSysID='', BranchID='', TradeAmount=0.0, IsETF=0, AccountID=''):
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
        self.LimitPrice = 'StockPrice' #价格, char[9]
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
        self.ClientID = '' #客户代码, char[11]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.TraderID = '' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderSubmitStatus = '' #报单提交状态, char
        self.NotifySequence = 'SequenceNo' #报单提示序号, int
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
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
        self.AccountID = '' #资金帐号, char[15]

class ExchangeOrder(BaseStruct): #交易所报单
    def __init__(self, ExchangeID='', OrderPriceType=OPT_AnyPrice, Direction=D_Buy, CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal=0, TimeCondition=TC_IOC, GTDDate='', VolumeCondition=VC_AV, MinVolume=0, ContingentCondition=CC_Immediately, StopPrice=0.0, ForceCloseReason=FCC_NotForceClose, IsAutoSuspend=0, BusinessUnit='', RequestID=0, OrderLocalID='', ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID=0, OrderSubmitStatus=OSS_InsertSubmitted, NotifySequence=0, TradingDay='', SettlementID=0, OrderSysID='', OrderSource=OSRC_Participant, OrderStatus=OST_AllTraded, OrderType=ORDT_Normal, VolumeTraded=0, VolumeTotal=0, InsertDate='', InsertTime='', ActiveTime='', SuspendTime='', UpdateTime='', CancelTime='', ActiveTraderID='', ClearingPartID='', SequenceNo=0, BranchID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.OrderPriceType = '' #报单价格条件, char
        self.Direction = '' #买卖方向, char
        self.CombOffsetFlag = '' #组合开平标志, char[5]
        self.CombHedgeFlag = '' #组合投机套保标志, char[5]
        self.LimitPrice = 'StockPrice' #价格, char[9]
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
        self.ClientID = '' #客户代码, char[11]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.TraderID = '' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderSubmitStatus = '' #报单提交状态, char
        self.NotifySequence = 'SequenceNo' #报单提示序号, int
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
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
        self.BranchID = '' #营业部编号, char[9]

class ExchangeOrderInsertError(BaseStruct): #交易所报单插入失败
    def __init__(self, ExchangeID='', ParticipantID='', TraderID='', InstallID=0, OrderLocalID='', ErrorID=0, ErrorMsg=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ParticipantID = '' #会员代码, char[11]
        self.TraderID = '' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class InputOrderAction(BaseStruct): #输入报单操作
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef=0, OrderRef='', RequestID=0, FrontID=0, SessionID=0, ExchangeID='', ActionFlag=AF_Delete, LimitPrice=0.0, VolumeChange=0, UserID='', InstrumentID='', TraderID='', OrderLocalID=''):
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
        self.TraderID = '' #交易所交易员代码, char[21]
        self.OrderLocalID = '' #本地报单编号, char[13]

class OrderAction(BaseStruct): #报单操作
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef=0, OrderRef='', RequestID=0, FrontID=0, SessionID=0, ExchangeID='', ActionFlag=AF_Delete, LimitPrice=0.0, VolumeChange=0, ActionDate='', ActionTime='', TraderID='', InstallID=0, OrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus=OAS_Submitted, UserID='', BranchID='', StatusMsg='', InstrumentID=''):
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
        self.TraderID = '' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ActionLocalID = 'OrderLocalID' #操作本地编号, char[13]
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[11]
        self.BusinessUnit = '' #业务单元, char[21]
        self.OrderActionStatus = '' #报单操作状态, char
        self.UserID = '' #用户代码, char[16]
        self.BranchID = '' #营业部编号, char[9]
        self.StatusMsg = 'ErrorMsg' #状态信息, char[81]
        self.InstrumentID = '' #合约代码, char[31]

class ExchangeOrderAction(BaseStruct): #交易所报单操作
    def __init__(self, ExchangeID='', ActionFlag=AF_Delete, LimitPrice=0.0, VolumeChange=0, ActionDate='', ActionTime='', TraderID='', InstallID=0, OrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus=OAS_Submitted, UserID='', BranchID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ActionFlag = '' #操作标志, char
        self.LimitPrice = 'Price' #价格, double
        self.VolumeChange = 'Volume' #数量变化, int
        self.ActionDate = 'Date' #操作日期, char[9]
        self.ActionTime = 'Time' #操作时间, char[9]
        self.TraderID = '' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ActionLocalID = 'OrderLocalID' #操作本地编号, char[13]
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[11]
        self.BusinessUnit = '' #业务单元, char[21]
        self.OrderActionStatus = '' #报单操作状态, char
        self.UserID = '' #用户代码, char[16]
        self.BranchID = '' #营业部编号, char[9]

class ExchangeOrderActionError(BaseStruct): #交易所报单操作失败
    def __init__(self, ExchangeID='', OrderSysID='', TraderID='', InstallID=0, OrderLocalID='', ActionLocalID='', ErrorID=0, ErrorMsg=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.OrderSysID = '' #报单编号, char[21]
        self.TraderID = '' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ActionLocalID = 'OrderLocalID' #操作本地编号, char[13]
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class ExchangeTrade(BaseStruct): #交易所成交
    def __init__(self, ExchangeID='', TradeID='', Direction=D_Buy, OrderSysID='', ParticipantID='', ClientID='', TradingRole=ER_Broker, ExchangeInstID='', OffsetFlag=OF_Open, HedgeFlag=HF_Speculation, Price='', Volume=0, TradeDate='', TradeTime='', TradeType=TRDT_Common, PriceSource=PSRC_LastPrice, TraderID='', OrderLocalID='', ClearingPartID='', BusinessUnit='', SequenceNo=0):
        self.ExchangeID = '' #交易所代码, char[9]
        self.TradeID = '' #成交编号, char[21]
        self.Direction = '' #买卖方向, char
        self.OrderSysID = '' #报单编号, char[21]
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[11]
        self.TradingRole = '' #交易角色, char
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.OffsetFlag = '' #开平标志, char
        self.HedgeFlag = '' #投机套保标志, char
        self.Price = 'StockPrice' #价格, char[9]
        self.Volume = '' #数量, int
        self.TradeDate = 'Date' #成交时期, char[9]
        self.TradeTime = 'Time' #成交时间, char[9]
        self.TradeType = '' #成交类型, char
        self.PriceSource = '' #成交价来源, char
        self.TraderID = '' #交易所交易员代码, char[21]
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ClearingPartID = 'ParticipantID' #结算会员编号, char[11]
        self.BusinessUnit = '' #业务单元, char[21]
        self.SequenceNo = '' #序号, int

class Trade(BaseStruct): #成交
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', TradeID='', Direction=D_Buy, OrderSysID='', ParticipantID='', ClientID='', TradingRole=ER_Broker, ExchangeInstID='', OffsetFlag=OF_Open, HedgeFlag=HF_Speculation, Price='', Volume=0, TradeDate='', TradeTime='', TradeType=TRDT_Common, PriceSource=PSRC_LastPrice, TraderID='', OrderLocalID='', ClearingPartID='', BusinessUnit='', SequenceNo=0, TradingDay='', SettlementID=0, BrokerOrderSeq=0):
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
        self.ClientID = '' #客户代码, char[11]
        self.TradingRole = '' #交易角色, char
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.OffsetFlag = '' #开平标志, char
        self.HedgeFlag = '' #投机套保标志, char
        self.Price = 'StockPrice' #价格, char[9]
        self.Volume = '' #数量, int
        self.TradeDate = 'Date' #成交时期, char[9]
        self.TradeTime = 'Time' #成交时间, char[9]
        self.TradeType = '' #成交类型, char
        self.PriceSource = '' #成交价来源, char
        self.TraderID = '' #交易所交易员代码, char[21]
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ClearingPartID = 'ParticipantID' #结算会员编号, char[11]
        self.BusinessUnit = '' #业务单元, char[21]
        self.SequenceNo = '' #序号, int
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
        self.BrokerOrderSeq = 'SequenceNo' #经纪公司报单编号, int

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

class QueryMaxOrderVolume(BaseStruct): #查询最大报单数量
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', Direction=D_Buy, OffsetFlag=OF_Open, HedgeFlag=HF_Speculation, MaxVolume=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.Direction = '' #买卖方向, char
        self.OffsetFlag = '' #开平标志, char
        self.HedgeFlag = '' #投机套保标志, char
        self.MaxVolume = 'Volume' #最大允许报单数量, int

class SettlementInfoConfirm(BaseStruct): #投资者结算结果确认信息
    def __init__(self, BrokerID='', InvestorID='', ConfirmDate='', ConfirmTime=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ConfirmDate = 'Date' #确认日期, char[9]
        self.ConfirmTime = 'Time' #确认时间, char[9]

class SyncDeposit(BaseStruct): #出入金同步
    def __init__(self, DepositSeqNo='', BrokerID='', InvestorID='', Deposit=0.0, IsForce=0):
        self.DepositSeqNo = '' #出入金流水号, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.Deposit = 'Money' #入金金额, double
        self.IsForce = 'Bool' #是否强制进行, int

class BrokerSync(BaseStruct): #经纪公司同步
    def __init__(self, BrokerID=''):
        self.BrokerID = '' #经纪公司代码, char[11]

class SyncingInvestor(BaseStruct): #正在同步中的投资者
    def __init__(self, InvestorID='', BrokerID='', InvestorGroupID='', InvestorName='', IdentifiedCardType=ICT_EID, IdentifiedCardNo='', IsActive=0, Telephone='', Address='', OpenDate='', Mobile='', SHBranchID='', SZBranchID='', IsCreditAccount=0):
        self.InvestorID = '' #投资者代码, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorGroupID = 'InvestorID' #投资者分组代码, char[15]
        self.InvestorName = 'PartyName' #投资者名称, char[81]
        self.IdentifiedCardType = 'IdCardType' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.IsActive = 'Bool' #是否活跃, int
        self.Telephone = '' #联系电话, char[41]
        self.Address = '' #通讯地址, char[101]
        self.OpenDate = 'Date' #开户日期, char[9]
        self.Mobile = '' #手机, char[41]
        self.SHBranchID = 'BranchID' #上海营业部编号, char[9]
        self.SZBranchID = 'BranchID' #深圳营业部编号, char[9]
        self.IsCreditAccount = 'Bool' #是否信用账户, int

class SyncingTradingCode(BaseStruct): #正在同步中的交易代码
    def __init__(self, InvestorID='', BrokerID='', ExchangeID='', ClientID='', IsActive=0):
        self.InvestorID = '' #投资者代码, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ClientID = '' #客户代码, char[11]
        self.IsActive = 'Bool' #是否活跃, int

class SyncingInvestorGroup(BaseStruct): #正在同步中的投资者分组
    def __init__(self, BrokerID='', InvestorGroupID='', InvestorGroupName=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorGroupID = 'InvestorID' #投资者分组代码, char[15]
        self.InvestorGroupName = '' #投资者分组名称, char[41]

class SyncingTradingAccount(BaseStruct): #正在同步中的交易账号
    def __init__(self, BrokerID='', AccountID='', PreMortgage=0.0, PreCredit=0.0, PreDeposit=0.0, PreBalance=0.0, PreMargin=0.0, InterestBase=0.0, Interest=0.0, Deposit=0.0, Withdraw=0.0, FrozenMargin=0.0, FrozenCash=0.0, FrozenCommission=0.0, CurrMargin=0.0, CashIn=0.0, Commission=0.0, CloseProfit=0.0, PositionProfit=0.0, Balance=0.0, Available=0.0, WithdrawQuota=0.0, Reserve=0.0, TradingDay='', SettlementID=0, Credit=0.0, Mortgage=0.0, ExchangeMargin=0.0, DeliveryMargin=0.0, ExchangeDeliveryMargin=0.0, FrozenTransferFee=0.0, FrozenStampTax=0.0, TransferFee=0.0, StampTax=0.0, ConversionAmount=0.0, CreditAmount=0.0, LowLimitRatio=0.0, MarginTradingAmount=0.0, ShortSellingAmount=0.0, MarginTradingAvail=0.0, ShortSellingAvail=0.0, CreditRatio=0.0, StockValue=0.0):
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
        self.CloseProfit = 'Money' #平仓盈亏, double
        self.PositionProfit = 'Money' #持仓盈亏, double
        self.Balance = 'Money' #期货结算准备金, double
        self.Available = 'Money' #可用资金, double
        self.WithdrawQuota = 'Money' #可取资金, double
        self.Reserve = 'Money' #基本准备金, double
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
        self.Credit = 'Money' #信用额度, double
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
        self.LowLimitRatio = 'Ratio' #最低维持担保比例, double
        self.MarginTradingAmount = 'Money' #融资买入金额, double
        self.ShortSellingAmount = 'Money' #融券卖出金额, double
        self.MarginTradingAvail = 'Money' #融资买入可用金额, double
        self.ShortSellingAvail = 'Money' #融券卖出可用金额, double
        self.CreditRatio = 'Ratio' #维持担保比例, double
        self.StockValue = 'Money' #证券总价值, double

class SyncingInvestorPosition(BaseStruct): #正在同步中的投资者持仓
    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', PosiDirection=PD_Net, HedgeFlag=HF_Speculation, PositionDate=PSD_Today, YdPosition=0, Position=0, LongFrozen=0, ShortFrozen=0, LongFrozenAmount=0.0, ShortFrozenAmount=0.0, OpenVolume=0, CloseVolume=0, OpenAmount=0.0, CloseAmount=0.0, PositionCost=0.0, FrozenCash=0.0, CashIn=0.0, Commission=0.0, CloseProfit=0.0, PositionProfit=0.0, PreSettlementPrice=0.0, SettlementPrice=0.0, TradingDay='', SettlementID=0, OpenCost=0.0, ExchangeMargin=0.0, TodayPosition=0, TransferFee=0.0, StampTax=0.0, TodayPurRedVolume=0, ConversionRate=0.0, ConversionAmount=0.0, MarginTradeVolume=0, MarginTradeAmount=0.0, MarginTradeFrozenVolume=0, MarginTradeFrozenAmount=0.0, MarginTradeConversionAmount=0.0, ShortSellVolume=0, ShortSellAmount=0.0, ShortSellConversionAmount=0.0, ShortSellFrozenVolume=0, ShortSellFrozenAmount=0.0, StockValue=0.0, ExchangeID=''):
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
        self.CloseProfit = 'Money' #平仓盈亏, double
        self.PositionProfit = 'Money' #持仓盈亏, double
        self.PreSettlementPrice = 'Price' #上次结算价, double
        self.SettlementPrice = 'Price' #本次结算价, double
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
        self.OpenCost = 'Money' #开仓成本, double
        self.ExchangeMargin = 'Money' #交易所保证金, double
        self.TodayPosition = 'Volume' #今日持仓, int
        self.TransferFee = 'Money' #过户费, double
        self.StampTax = 'Money' #印花税, double
        self.TodayPurRedVolume = 'Volume' #今日申购赎回数量, int
        self.ConversionRate = 'Ratio' #折算率, double
        self.ConversionAmount = 'Money' #折算金额, double
        self.MarginTradeVolume = 'Volume' #融资买入出数量, int
        self.MarginTradeAmount = 'Money' #融资买入金额, double
        self.MarginTradeFrozenVolume = 'Volume' #融资买入冻结数量, int
        self.MarginTradeFrozenAmount = 'Money' #融资买入冻结金额, double
        self.MarginTradeConversionAmount = 'Money' #融资买入折算金额, double
        self.ShortSellVolume = 'Volume' #融券卖出数量, int
        self.ShortSellAmount = 'Money' #融券卖出金额, double
        self.ShortSellConversionAmount = 'Money' #融券卖出折算金额, double
        self.ShortSellFrozenVolume = 'Volume' #融券卖出冻结数量, int
        self.ShortSellFrozenAmount = 'Money' #融券卖出冻结金额, double
        self.StockValue = 'Money' #证券价值, double
        self.ExchangeID = '' #交易所代码, char[9]

class SyncingInstrumentMarginRate(BaseStruct): #正在同步中的合约保证金率
    def __init__(self, InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', HedgeFlag=HF_Speculation, LongMarginRatioByMoney=0.0, LongMarginRatioByVolume=0.0, ShortMarginRatioByMoney=0.0, ShortMarginRatioByVolume=0.0, IsRelative=0):
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.HedgeFlag = '' #投机套保标志, char
        self.LongMarginRatioByMoney = 'Ratio' #多头保证金率, double
        self.LongMarginRatioByVolume = 'Money' #多头保证金费, double
        self.ShortMarginRatioByMoney = 'Ratio' #空头保证金率, double
        self.ShortMarginRatioByVolume = 'Money' #空头保证金费, double
        self.IsRelative = 'Bool' #是否相对交易所收取, int

class SyncingInstrumentCommissionRate(BaseStruct): #正在同步中的合约手续费率
    def __init__(self, InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', BuyStampTaxRateByMoney=0.0, BuyStampTaxRateByVolume=0.0, SellStampTaxRateByMoney=0.0, SellStampTaxRateByVolume=0.0, BuyTransferFeeRateByMoney=0.0, BuyTransferFeeRateByVolume=0.0, SellTransferFeeRateByMoney=0.0, SellTransferFeeRateByVolume=0.0, BuyTradeFeeByMoney=0.0, BuyTradeFeeByVolume=0.0, SellTradeFeeByMoney=0.0, SellTradeFeeByVolume=0.0, BuyMarginByMoney=0.0, SellMarginByMoney=0.0, MinTradeFee=0.0):
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.BuyStampTaxRateByMoney = 'Ratio' #买印花税率, double
        self.BuyStampTaxRateByVolume = 'Ratio' #买印花税率(按手数), double
        self.SellStampTaxRateByMoney = 'Ratio' #卖印花税率, double
        self.SellStampTaxRateByVolume = 'Ratio' #卖印花税率(按手数), double
        self.BuyTransferFeeRateByMoney = 'Ratio' #买过户费率, double
        self.BuyTransferFeeRateByVolume = 'Ratio' #买过户费率(按手数), double
        self.SellTransferFeeRateByMoney = 'Ratio' #卖过户费率, double
        self.SellTransferFeeRateByVolume = 'Ratio' #卖过户费率(按手数), double
        self.BuyTradeFeeByMoney = 'Ratio' #买交易费, double
        self.BuyTradeFeeByVolume = 'Ratio' #买交易费(按手数), double
        self.SellTradeFeeByMoney = 'Ratio' #卖交易费率, double
        self.SellTradeFeeByVolume = 'Ratio' #卖交易费率(按手数), double
        self.BuyMarginByMoney = 'Ratio' #买交易附加费率, double
        self.SellMarginByMoney = 'Ratio' #卖交易附加费率, double
        self.MinTradeFee = 'Price' #最小过户费, double

class SyncingInstrumentTradingRight(BaseStruct): #正在同步中的合约交易权限
    def __init__(self, InstrumentID='', InvestorRange=IR_All, BrokerID='', InvestorID='', Direction=D_Buy, TradingRight=TR_Allow, ExchangeID=''):
        self.InstrumentID = '' #合约代码, char[31]
        self.InvestorRange = '' #投资者范围, char
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.Direction = '' #买卖, char
        self.TradingRight = '' #交易权限, char
        self.ExchangeID = '' #交易所代码, char[9]

class QryOrder(BaseStruct): #查询报单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', OrderSysID='', InsertTimeStart='', InsertTimeEnd=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]
        self.OrderSysID = '' #报单编号, char[21]
        self.InsertTimeStart = 'Time' #开始时间, char[9]
        self.InsertTimeEnd = 'Time' #结束时间, char[9]

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

class QryTradingAccount(BaseStruct): #查询资金账户
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class QryInvestor(BaseStruct): #查询投资者
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class QryTradingCode(BaseStruct): #查询交易编码
    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', ClientID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ExchangeID = '' #交易所代码, char[9]
        self.ClientID = '' #客户代码, char[11]

class QryInvestorGroup(BaseStruct): #查询交易编码
    def __init__(self, BrokerID=''):
        self.BrokerID = '' #经纪公司代码, char[11]

class QryInstrumentMarginRate(BaseStruct): #查询交易编码
    def __init__(self, ExchangeID='', BrokerID='', InvestorID='', InstrumentID='', HedgeFlag=HF_Speculation):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.HedgeFlag = '' #投机套保标志, char

class QryInstrumentCommissionRate(BaseStruct): #查询交易编码
    def __init__(self, ExchangeID='', BrokerID='', InvestorID='', InstrumentID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]

class QryInstrumentTradingRight(BaseStruct): #查询交易编码
    def __init__(self, ExchangeID='', BrokerID='', InvestorID='', InstrumentID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]

class QryBroker(BaseStruct): #查询经纪公司
    def __init__(self, BrokerID=''):
        self.BrokerID = '' #经纪公司代码, char[11]

class QryTrader(BaseStruct): #查询交易员
    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ParticipantID = '' #会员代码, char[11]
        self.TraderID = '' #交易所交易员代码, char[21]

class QryPartBroker(BaseStruct): #查询经纪公司会员代码
    def __init__(self, ExchangeID='', BrokerID='', ParticipantID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ParticipantID = '' #会员代码, char[11]

class QrySuperUserFunction(BaseStruct): #查询管理用户功能权限
    def __init__(self, UserID=''):
        self.UserID = '' #用户代码, char[16]

class QryUserSession(BaseStruct): #查询用户会话
    def __init__(self, FrontID=0, SessionID=0, BrokerID='', UserID=''):
        self.FrontID = '' #前置编号, int
        self.SessionID = '' #会话编号, int
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class QryFrontStatus(BaseStruct): #查询前置状态
    def __init__(self, FrontID=0):
        self.FrontID = '' #前置编号, int

class QryExchangeOrder(BaseStruct): #查询交易所报单
    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[11]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]
        self.TraderID = '' #交易所交易员代码, char[21]

class QryOrderAction(BaseStruct): #查询报单操作
    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ExchangeID = '' #交易所代码, char[9]

class QryExchangeOrderAction(BaseStruct): #查询交易所报单操作
    def __init__(self, ParticipantID='', ClientID='', ExchangeID='', TraderID=''):
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.TraderID = '' #交易所交易员代码, char[21]

class QrySuperUser(BaseStruct): #查询管理用户
    def __init__(self, UserID=''):
        self.UserID = '' #用户代码, char[16]

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

class QryDepthMarketData(BaseStruct): #查询行情
    def __init__(self, InstrumentID=''):
        self.InstrumentID = '' #合约代码, char[31]

class QryBrokerUser(BaseStruct): #查询经纪公司用户
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class QryBrokerUserFunction(BaseStruct): #查询经纪公司用户权限
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]

class QryTraderOffer(BaseStruct): #查询交易员报盘机
    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ParticipantID = '' #会员代码, char[11]
        self.TraderID = '' #交易所交易员代码, char[21]

class QrySyncDeposit(BaseStruct): #查询出入金流水
    def __init__(self, BrokerID='', DepositSeqNo=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.DepositSeqNo = '' #出入金流水号, char[15]

class QrySettlementInfo(BaseStruct): #查询投资者结算结果
    def __init__(self, BrokerID='', InvestorID='', TradingDay=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.TradingDay = 'Date' #交易日, char[9]

class QryHisOrder(BaseStruct): #查询报单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', OrderSysID='', InsertTimeStart='', InsertTimeEnd='', TradingDay='', SettlementID=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]
        self.OrderSysID = '' #报单编号, char[21]
        self.InsertTimeStart = 'Time' #开始时间, char[9]
        self.InsertTimeEnd = 'Time' #结束时间, char[9]
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int

class MarketData(BaseStruct): #市场行情
    def __init__(self, TradingDay='', InstrumentID='', ExchangeID='', ExchangeInstID='', LastPrice=0.0, PreSettlementPrice=0.0, PreClosePrice=0.0, PreOpenInterest=0.0, OpenPrice=0.0, HighestPrice=0.0, LowestPrice=0.0, Volume=0, Turnover=0.0, OpenInterest=0.0, ClosePrice=0.0, SettlementPrice=0.0, UpperLimitPrice=0.0, LowerLimitPrice=0.0, PreDelta=0.0, CurrDelta=0.0, UpdateTime='', UpdateMillisec=0):
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
    def __init__(self, InstrumentID='', UpdateTime='', UpdateMillisec=0):
        self.InstrumentID = '' #合约代码, char[31]
        self.UpdateTime = 'Time' #最后修改时间, char[9]
        self.UpdateMillisec = 'Millisec' #最后修改毫秒, int

class SpecificInstrument(BaseStruct): #指定的合约
    def __init__(self, InstrumentID='', ExchangeID=''):
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]

class InstrumentStatus(BaseStruct): #合约状态
    def __init__(self, ExchangeID='', ExchangeInstID='', SettlementGroupID='', InstrumentID='', InstrumentStatus=IS_BeforeTrading, TradingSegmentSN=0, EnterTime='', EnterReason=IER_Automatic):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.SettlementGroupID = '' #结算组代码, char[9]
        self.InstrumentID = '' #合约代码, char[31]
        self.InstrumentStatus = '' #合约交易状态, char
        self.TradingSegmentSN = '' #交易阶段编号, int
        self.EnterTime = 'Time' #进入本状态时间, char[9]
        self.EnterReason = 'InstStatusEnterReason' #进入本状态原因, char

class QryInstrumentStatus(BaseStruct): #查询合约状态
    def __init__(self, ExchangeID='', ExchangeInstID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]

class InvestorAccount(BaseStruct): #投资者账户
    def __init__(self, BrokerID='', InvestorID='', AccountID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.AccountID = '' #投资者帐号, char[15]

class PositionProfitAlgorithm(BaseStruct): #浮动盈亏算法
    def __init__(self, BrokerID='', AccountID='', Algorithm=AG_All, Memo=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.AccountID = '' #投资者帐号, char[15]
        self.Algorithm = '' #盈亏算法, char
        self.Memo = '' #备注, char[161]

class Discount(BaseStruct): #会员资金折扣
    def __init__(self, BrokerID='', InvestorRange=IR_All, InvestorID='', Discount=0.0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorRange = '' #投资者范围, char
        self.InvestorID = '' #投资者代码, char[15]
        self.Discount = 'Ratio' #资金折扣比例, double

class QryTransferBank(BaseStruct): #查询转帐银行
    def __init__(self, BankID='', BankBrchID=''):
        self.BankID = '' #银行代码, char[4]
        self.BankBrchID = '' #银行分中心代码, char[5]

class TransferBank(BaseStruct): #转帐银行
    def __init__(self, BankID='', BankBrchID='', BankName='', IsActive=0):
        self.BankID = '' #银行代码, char[4]
        self.BankBrchID = '' #银行分中心代码, char[5]
        self.BankName = '' #银行名称, char[101]
        self.IsActive = 'Bool' #是否活跃, int

class QryInvestorPositionDetail(BaseStruct): #查询投资者持仓明细
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]

class InvestorPositionDetail(BaseStruct): #投资者持仓明细
    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', HedgeFlag=HF_Speculation, Direction=D_Buy, OpenDate='', TradeID='', Volume=0, OpenPrice=0.0, TradingDay='', SettlementID=0, TradeType=TRDT_Common, ExchangeID='', Margin=0.0, ExchMargin=0.0, LastSettlementPrice=0.0, SettlementPrice=0.0, CloseVolume=0, CloseAmount=0.0, TransferFee=0.0, StampTax=0.0, Commission=0.0):
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
        self.SettlementID = '' #结算编号, int
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

class TradingAccountPassword(BaseStruct): #资金账户口令域
    def __init__(self, BrokerID='', AccountID='', Password=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #密码, char[41]

class MDTraderOffer(BaseStruct): #交易所行情报盘机
    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallID=0, OrderLocalID='', TraderConnectStatus=TCS_NotConnected, ConnectRequestDate='', ConnectRequestTime='', LastReportDate='', LastReportTime='', ConnectDate='', ConnectTime='', StartDate='', StartTime='', TradingDay='', BrokerID='', BranchID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.TraderID = '' #交易所交易员代码, char[21]
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
        self.BranchID = '' #营业部编号, char[9]

class QryMDTraderOffer(BaseStruct): #查询行情报盘机
    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        self.ExchangeID = '' #交易所代码, char[9]
        self.ParticipantID = '' #会员代码, char[11]
        self.TraderID = '' #交易所交易员代码, char[21]

class QryNotice(BaseStruct): #查询客户通知
    def __init__(self, BrokerID=''):
        self.BrokerID = '' #经纪公司代码, char[11]

class Notice(BaseStruct): #客户通知
    def __init__(self, BrokerID='', Content='', SequenceLabel=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.Content = '' #消息正文, char[501]
        self.SequenceLabel = '' #经纪公司通知内容序列号, char[2]

class UserRight(BaseStruct): #用户权限
    def __init__(self, BrokerID='', UserID='', UserRightType=URT_Logon, IsForbidden=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserRightType = '' #客户权限类型, char
        self.IsForbidden = 'Bool' #是否禁止, int

class QrySettlementInfoConfirm(BaseStruct): #查询结算信息确认域
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class LoadSettlementInfo(BaseStruct): #装载结算信息
    def __init__(self, BrokerID=''):
        self.BrokerID = '' #经纪公司代码, char[11]

class BrokerWithdrawAlgorithm(BaseStruct): #经纪公司可提资金算法表
    def __init__(self, BrokerID='', WithdrawAlgorithm=AG_All, UsingRatio=0.0, IncludeCloseProfit=ICP_Include, AllWithoutTrade=AWT_Enable, AvailIncludeCloseProfit=ICP_Include, IsBrokerUserEvent=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.WithdrawAlgorithm = 'Algorithm' #可提资金算法, char
        self.UsingRatio = 'Ratio' #资金使用率, double
        self.IncludeCloseProfit = '' #可提是否包含平仓盈利, char
        self.AllWithoutTrade = '' #本日无仓且无成交客户是否受可提比例限制, char
        self.AvailIncludeCloseProfit = 'IncludeCloseProfit' #可用是否包含平仓盈利, char
        self.IsBrokerUserEvent = 'Bool' #是否启用用户事件, int

class TradingAccountPasswordUpdateV1(BaseStruct): #资金账户口令变更域
    def __init__(self, BrokerID='', InvestorID='', OldPassword='', NewPassword=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.OldPassword = 'Password' #原来的口令, char[41]
        self.NewPassword = 'Password' #新的口令, char[41]

class TradingAccountPasswordUpdate(BaseStruct): #资金账户口令变更域
    def __init__(self, BrokerID='', AccountID='', OldPassword='', NewPassword=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.AccountID = '' #投资者帐号, char[15]
        self.OldPassword = 'Password' #原来的口令, char[41]
        self.NewPassword = 'Password' #新的口令, char[41]

class QryCombinationLeg(BaseStruct): #查询组合合约分腿
    def __init__(self, CombInstrumentID='', LegID=0, LegInstrumentID=''):
        self.CombInstrumentID = 'InstrumentID' #组合合约代码, char[31]
        self.LegID = '' #单腿编号, int
        self.LegInstrumentID = 'InstrumentID' #单腿合约代码, char[31]

class QrySyncStatus(BaseStruct): #查询组合合约分腿
    def __init__(self, TradingDay=''):
        self.TradingDay = 'Date' #交易日, char[9]

class CombinationLeg(BaseStruct): #组合交易合约的单腿
    def __init__(self, CombInstrumentID='', LegID=0, LegInstrumentID='', Direction=D_Buy, LegMultiple=0, ImplyLevel=0):
        self.CombInstrumentID = 'InstrumentID' #组合合约代码, char[31]
        self.LegID = '' #单腿编号, int
        self.LegInstrumentID = 'InstrumentID' #单腿合约代码, char[31]
        self.Direction = '' #买卖方向, char
        self.LegMultiple = '' #单腿乘数, int
        self.ImplyLevel = '' #派生层数, int

class SyncStatus(BaseStruct): #数据同步状态
    def __init__(self, TradingDay='', DataSyncStatus=DS_Asynchronous):
        self.TradingDay = 'Date' #交易日, char[9]
        self.DataSyncStatus = '' #数据同步状态, char

class QryLinkMan(BaseStruct): #查询联系人
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class LinkMan(BaseStruct): #联系人
    def __init__(self, BrokerID='', InvestorID='', PersonType=PST_Order, IdentifiedCardType=ICT_EID, IdentifiedCardNo='', PersonName='', Telephone='', Address='', ZipCode='', Priority=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.PersonType = '' #联系人类型, char
        self.IdentifiedCardType = 'IdCardType' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.PersonName = 'PartyName' #名称, char[81]
        self.Telephone = '' #联系电话, char[41]
        self.Address = '' #通讯地址, char[101]
        self.ZipCode = '' #邮政编码, char[7]
        self.Priority = '' #优先级, int

class QryBrokerUserEvent(BaseStruct): #查询经纪公司用户事件
    def __init__(self, BrokerID='', UserID='', UserEventType=UET_All):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserEventType = '' #用户事件类型, char

class BrokerUserEvent(BaseStruct): #查询经纪公司用户事件
    def __init__(self, BrokerID='', UserID='', UserEventType=UET_All, EventSequenceNo=0, EventDate='', EventTime='', UserEventInfo='', InvestorID='', InstrumentID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.UserEventType = '' #用户事件类型, char
        self.EventSequenceNo = 'SequenceNo' #用户事件序号, int
        self.EventDate = 'Date' #事件发生日期, char[9]
        self.EventTime = 'Time' #事件发生时间, char[9]
        self.UserEventInfo = '' #用户事件信息, char[1025]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]

class QryContractBank(BaseStruct): #查询签约银行请求
    def __init__(self, BrokerID='', BankID='', BankBrchID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.BankID = '' #银行代码, char[4]
        self.BankBrchID = '' #银行分中心代码, char[5]

class ContractBank(BaseStruct): #查询签约银行响应
    def __init__(self, BrokerID='', BankID='', BankBrchID='', BankName=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.BankID = '' #银行代码, char[4]
        self.BankBrchID = '' #银行分中心代码, char[5]
        self.BankName = '' #银行名称, char[101]

class InvestorPositionCombineDetail(BaseStruct): #投资者组合持仓明细
    def __init__(self, TradingDay='', OpenDate='', ExchangeID='', SettlementID=0, BrokerID='', InvestorID='', ComTradeID='', TradeID='', InstrumentID='', HedgeFlag=HF_Speculation, Direction=D_Buy, TotalAmt=0, Margin=0.0, ExchMargin=0.0, MarginRateByMoney=0.0, MarginRateByVolume=0.0, LegID=0, LegMultiple=0, CombInstrumentID=''):
        self.TradingDay = 'Date' #交易日, char[9]
        self.OpenDate = 'Date' #开仓日期, char[9]
        self.ExchangeID = '' #交易所代码, char[9]
        self.SettlementID = '' #结算编号, int
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ComTradeID = 'TradeID' #组合编号, char[21]
        self.TradeID = '' #撮合编号, char[21]
        self.InstrumentID = '' #合约代码, char[31]
        self.HedgeFlag = '' #投机套保标志, char
        self.Direction = '' #买卖, char
        self.TotalAmt = 'Volume' #持仓量, int
        self.Margin = 'Money' #投资者保证金, double
        self.ExchMargin = 'Money' #交易所保证金, double
        self.MarginRateByMoney = 'Ratio' #保证金率, double
        self.MarginRateByVolume = 'Ratio' #保证金率(按手数), double
        self.LegID = '' #单腿编号, int
        self.LegMultiple = '' #单腿乘数, int
        self.CombInstrumentID = 'InstrumentID' #组合持仓合约编码, char[31]

class ParkedOrder(BaseStruct): #预埋单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', OrderPriceType=OPT_AnyPrice, Direction=D_Buy, CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal=0, TimeCondition=TC_IOC, GTDDate='', VolumeCondition=VC_AV, MinVolume=0, ContingentCondition=CC_Immediately, StopPrice=0.0, ForceCloseReason=FCC_NotForceClose, IsAutoSuspend=0, BusinessUnit='', RequestID=0, UserForceClose=0, ParkedOrderID='', UserType=UT_Investor, Status=PAOS_NotSend, ErrorID=0, ErrorMsg=''):
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
        self.LimitPrice = 'StockPrice' #价格, char[9]
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
        self.ParkedOrderID = '' #预埋报单编号, char[13]
        self.UserType = '' #用户类型, char
        self.Status = 'ParkedOrderStatus' #预埋单状态, char
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class ParkedOrderAction(BaseStruct): #输入预埋单操作
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef=0, OrderRef='', RequestID=0, FrontID=0, SessionID=0, ExchangeID='', ActionFlag=AF_Delete, LimitPrice=0.0, VolumeChange=0, UserID='', InstrumentID='', ParkedOrderActionID='', UserType=UT_Investor, Status=PAOS_NotSend, ErrorID=0, ErrorMsg=''):
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
        self.ParkedOrderActionID = '' #预埋撤单单编号, char[13]
        self.UserType = '' #用户类型, char
        self.Status = 'ParkedOrderStatus' #预埋撤单状态, char
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class QryParkedOrder(BaseStruct): #查询预埋单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]

class QryParkedOrderAction(BaseStruct): #查询预埋撤单
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.ExchangeID = '' #交易所代码, char[9]

class RemoveParkedOrder(BaseStruct): #删除预埋单
    def __init__(self, BrokerID='', InvestorID='', ParkedOrderID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ParkedOrderID = '' #预埋报单编号, char[13]

class RemoveParkedOrderAction(BaseStruct): #删除预埋撤单
    def __init__(self, BrokerID='', InvestorID='', ParkedOrderActionID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.ParkedOrderActionID = '' #预埋撤单编号, char[13]

class InvestorWithdrawAlgorithm(BaseStruct): #经纪公司可提资金算法表
    def __init__(self, BrokerID='', InvestorRange=IR_All, InvestorID='', UsingRatio=0.0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorRange = '' #投资者范围, char
        self.InvestorID = '' #投资者代码, char[15]
        self.UsingRatio = 'Ratio' #可提资金比例, double

class QryInvestorPositionCombineDetail(BaseStruct): #查询组合持仓明细
    def __init__(self, BrokerID='', InvestorID='', CombInstrumentID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.CombInstrumentID = 'InstrumentID' #组合持仓合约编码, char[31]

class MarketDataAveragePrice(BaseStruct): #成交均价
    def __init__(self, AveragePrice=0.0):
        self.AveragePrice = 'Price' #当日均价, double

class VerifyInvestorPassword(BaseStruct): #校验投资者密码
    def __init__(self, BrokerID='', InvestorID='', Password=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.Password = '' #密码, char[41]

class UserIP(BaseStruct): #用户IP
    def __init__(self, BrokerID='', UserID='', IPAddress='', IPMask='', MacAddress=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.IPAddress = '' #IP地址, char[16]
        self.IPMask = 'IPAddress' #IP地址掩码, char[16]
        self.MacAddress = '' #Mac地址, char[21]

class TradingNoticeInfo(BaseStruct): #用户事件通知信息
    def __init__(self, BrokerID='', InvestorID='', SendTime='', FieldContent='', SequenceSeries=0, SequenceNo=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.SendTime = 'Time' #发送时间, char[9]
        self.FieldContent = 'Content' #消息正文, char[501]
        self.SequenceSeries = '' #序列系列号, short
        self.SequenceNo = '' #序列号, int

class TradingNotice(BaseStruct): #用户事件通知
    def __init__(self, BrokerID='', InvestorRange=IR_All, InvestorID='', SequenceSeries=0, UserID='', SendTime='', SequenceNo=0, FieldContent=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorRange = '' #投资者范围, char
        self.InvestorID = '' #投资者代码, char[15]
        self.SequenceSeries = '' #序列系列号, short
        self.UserID = '' #用户代码, char[16]
        self.SendTime = 'Time' #发送时间, char[9]
        self.SequenceNo = '' #序列号, int
        self.FieldContent = 'Content' #消息正文, char[501]

class QryTradingNotice(BaseStruct): #查询交易事件通知
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class QryErrOrder(BaseStruct): #查询错误报单
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

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
        self.LimitPrice = 'StockPrice' #价格, char[9]
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

class ErrorConditionalOrder(BaseStruct): #查询错误报单操作
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', OrderPriceType=OPT_AnyPrice, Direction=D_Buy, CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal=0, TimeCondition=TC_IOC, GTDDate='', VolumeCondition=VC_AV, MinVolume=0, ContingentCondition=CC_Immediately, StopPrice=0.0, ForceCloseReason=FCC_NotForceClose, IsAutoSuspend=0, BusinessUnit='', RequestID=0, OrderLocalID='', ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID=0, OrderSubmitStatus=OSS_InsertSubmitted, NotifySequence=0, TradingDay='', SettlementID=0, OrderSysID='', OrderSource=OSRC_Participant, OrderStatus=OST_AllTraded, OrderType=ORDT_Normal, VolumeTraded=0, VolumeTotal=0, InsertDate='', InsertTime='', ActiveTime='', SuspendTime='', UpdateTime='', CancelTime='', ActiveTraderID='', ClearingPartID='', SequenceNo=0, FrontID=0, SessionID=0, UserProductInfo='', StatusMsg='', UserForceClose=0, ActiveUserID='', BrokerOrderSeq=0, RelativeOrderSysID='', BranchID='', TradeAmount=0.0, IsETF=0, AccountID='', ErrorID=0, ErrorMsg=''):
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
        self.LimitPrice = 'StockPrice' #价格, char[9]
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
        self.ClientID = '' #客户代码, char[11]
        self.ExchangeInstID = '' #合约在交易所的代码, char[31]
        self.TraderID = '' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderSubmitStatus = '' #报单提交状态, char
        self.NotifySequence = 'SequenceNo' #报单提示序号, int
        self.TradingDay = 'Date' #交易日, char[9]
        self.SettlementID = '' #结算编号, int
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
        self.AccountID = '' #资金帐号, char[15]
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class QryErrOrderAction(BaseStruct): #查询错误报单操作
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class ErrOrderAction(BaseStruct): #错误报单操作
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef=0, OrderRef='', RequestID=0, FrontID=0, SessionID=0, ExchangeID='', ActionFlag=AF_Delete, LimitPrice=0.0, VolumeChange=0, ActionDate='', ActionTime='', TraderID='', InstallID=0, OrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus=OAS_Submitted, UserID='', BranchID='', StatusMsg='', InstrumentID='', ErrorID=0, ErrorMsg=''):
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
        self.TraderID = '' #交易所交易员代码, char[21]
        self.InstallID = '' #安装编号, int
        self.OrderLocalID = '' #本地报单编号, char[13]
        self.ActionLocalID = 'OrderLocalID' #操作本地编号, char[13]
        self.ParticipantID = '' #会员代码, char[11]
        self.ClientID = '' #客户代码, char[11]
        self.BusinessUnit = '' #业务单元, char[21]
        self.OrderActionStatus = '' #报单操作状态, char
        self.UserID = '' #用户代码, char[16]
        self.BranchID = '' #营业部编号, char[9]
        self.StatusMsg = 'ErrorMsg' #状态信息, char[81]
        self.InstrumentID = '' #合约代码, char[31]
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class QryExchangeSequence(BaseStruct): #查询交易所状态
    def __init__(self, ExchangeID=''):
        self.ExchangeID = '' #交易所代码, char[9]

class ExchangeSequence(BaseStruct): #交易所状态
    def __init__(self, ExchangeID='', SequenceNo=0, MarketStatus=IS_BeforeTrading):
        self.ExchangeID = '' #交易所代码, char[9]
        self.SequenceNo = '' #序号, int
        self.MarketStatus = 'InstrumentStatus' #合约交易状态, char

class QueryMaxOrderVolumeWithPrice(BaseStruct): #根据价格查询最大报单数量
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', Direction=D_Buy, OffsetFlag=OF_Open, HedgeFlag=HF_Speculation, MaxVolume=0, Price=0.0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.Direction = '' #买卖方向, char
        self.OffsetFlag = '' #开平标志, char
        self.HedgeFlag = '' #投机套保标志, char
        self.MaxVolume = 'Volume' #最大允许报单数量, int
        self.Price = '' #报单价格, double

class QryBrokerTradingParams(BaseStruct): #查询经纪公司交易参数
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

class BrokerTradingParams(BaseStruct): #经纪公司交易参数
    def __init__(self, BrokerID='', InvestorID='', MarginPriceType=MPT_PreSettlementPrice, Algorithm=AG_All, AvailIncludeCloseProfit=ICP_Include):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.MarginPriceType = '' #保证金价格类型, char
        self.Algorithm = '' #盈亏算法, char
        self.AvailIncludeCloseProfit = 'IncludeCloseProfit' #可用是否包含平仓盈利, char

class QryBrokerTradingAlgos(BaseStruct): #查询经纪公司交易算法
    def __init__(self, BrokerID='', ExchangeID='', InstrumentID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentID = '' #合约代码, char[31]

class BrokerTradingAlgos(BaseStruct): #经纪公司交易算法
    def __init__(self, BrokerID='', ExchangeID='', InstrumentID='', HandlePositionAlgoID=HPA_Base, FindMarginRateAlgoID=FMRA_Base, HandleTradingAccountAlgoID=HTAA_Base):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.InstrumentID = '' #合约代码, char[31]
        self.HandlePositionAlgoID = '' #持仓处理算法编号, char
        self.FindMarginRateAlgoID = '' #寻找保证金率算法编号, char
        self.HandleTradingAccountAlgoID = '' #资金处理算法编号, char

class QueryBrokerDeposit(BaseStruct): #查询经纪公司资金
    def __init__(self, BrokerID='', ExchangeID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]

class BrokerDeposit(BaseStruct): #经纪公司资金
    def __init__(self, TradingDay='', BrokerID='', ParticipantID='', ExchangeID='', PreBalance=0.0, CurrMargin=0.0, CloseProfit=0.0, Balance=0.0, Deposit=0.0, Withdraw=0.0, Available=0.0, Reserve=0.0, FrozenMargin=0.0):
        self.TradingDay = 'TradeDate' #交易日期, char[9]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ParticipantID = '' #会员代码, char[11]
        self.ExchangeID = '' #交易所代码, char[9]
        self.PreBalance = 'Money' #上次结算准备金, double
        self.CurrMargin = 'Money' #当前保证金总额, double
        self.CloseProfit = 'Money' #平仓盈亏, double
        self.Balance = 'Money' #期货结算准备金, double
        self.Deposit = 'Money' #入金金额, double
        self.Withdraw = 'Money' #出金金额, double
        self.Available = 'Money' #可提资金, double
        self.Reserve = 'Money' #基本准备金, double
        self.FrozenMargin = 'Money' #冻结的保证金, double

class QryCFMMCBrokerKey(BaseStruct): #查询保证金监管系统经纪公司密钥
    def __init__(self, BrokerID=''):
        self.BrokerID = '' #经纪公司代码, char[11]

class CFMMCBrokerKey(BaseStruct): #保证金监管系统经纪公司密钥
    def __init__(self, BrokerID='', ParticipantID='', CreateDate='', CreateTime='', KeyID=0, CurrentKey='', KeyKind=CFMMCKK_REQUEST):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ParticipantID = '' #经纪公司统一编码, char[11]
        self.CreateDate = 'Date' #密钥生成日期, char[9]
        self.CreateTime = 'Time' #密钥生成时间, char[9]
        self.KeyID = 'SequenceNo' #密钥编号, int
        self.CurrentKey = 'CFMMCKey' #动态密钥, char[21]
        self.KeyKind = 'CFMMCKeyKind' #动态密钥类型, char

class CFMMCTradingAccountKey(BaseStruct): #保证金监管系统经纪公司资金账户密钥
    def __init__(self, BrokerID='', ParticipantID='', AccountID='', KeyID=0, CurrentKey=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.ParticipantID = '' #经纪公司统一编码, char[11]
        self.AccountID = '' #投资者帐号, char[15]
        self.KeyID = 'SequenceNo' #密钥编号, int
        self.CurrentKey = 'CFMMCKey' #动态密钥, char[21]

class QryCFMMCTradingAccountKey(BaseStruct): #请求查询保证金监管系统经纪公司资金账户密钥
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]

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

class ManualSyncBrokerUserOTP(BaseStruct): #手工同步用户动态令牌
    def __init__(self, BrokerID='', UserID='', OTPType=OTP_NONE, FirstOTP='', SecondOTP=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.UserID = '' #用户代码, char[16]
        self.OTPType = '' #动态令牌类型, char
        self.FirstOTP = 'Password' #第一个动态密码, char[41]
        self.SecondOTP = 'Password' #第二个动态密码, char[41]

class ReqOpenAccount(BaseStruct): #转帐开户请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', Gender=GD_Unknown, CountryCode='', CustType=CUSTT_Person, Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus=MAS_Normal, BankAccount='', BankPassWord='', AccountID='', Password='', InstallID=0, VerifyCertNoFlag=YNI_Yes, CurrencyID='', CashExchangeCode=CEC_Exchange, Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', TID=0):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.Gender = '' #性别, char
        self.CountryCode = '' #国家代码, char[21]
        self.CustType = '' #客户类型, char
        self.Address = '' #地址, char[101]
        self.ZipCode = '' #邮编, char[7]
        self.Telephone = '' #电话号码, char[41]
        self.MobilePhone = '' #手机, char[21]
        self.Fax = '' #传真, char[41]
        self.EMail = '' #电子邮件, char[41]
        self.MoneyAccountStatus = '' #资金账户状态, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.InstallID = '' #安装编号, int
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.CashExchangeCode = '' #汇钞标志, char
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.TID = '' #交易ID, int

class ReqCancelAccount(BaseStruct): #转帐销户请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', Gender=GD_Unknown, CountryCode='', CustType=CUSTT_Person, Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus=MAS_Normal, BankAccount='', BankPassWord='', AccountID='', Password='', InstallID=0, VerifyCertNoFlag=YNI_Yes, CurrencyID='', CashExchangeCode=CEC_Exchange, Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', TID=0):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.Gender = '' #性别, char
        self.CountryCode = '' #国家代码, char[21]
        self.CustType = '' #客户类型, char
        self.Address = '' #地址, char[101]
        self.ZipCode = '' #邮编, char[7]
        self.Telephone = '' #电话号码, char[41]
        self.MobilePhone = '' #手机, char[21]
        self.Fax = '' #传真, char[41]
        self.EMail = '' #电子邮件, char[41]
        self.MoneyAccountStatus = '' #资金账户状态, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.InstallID = '' #安装编号, int
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.CashExchangeCode = '' #汇钞标志, char
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.TID = '' #交易ID, int

class ReqChangeAccount(BaseStruct): #变更银行账户请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', Gender=GD_Unknown, CountryCode='', CustType=CUSTT_Person, Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus=MAS_Normal, BankAccount='', BankPassWord='', NewBankAccount='', NewBankPassWord='', AccountID='', Password='', BankAccType=BAT_BankBook, InstallID=0, VerifyCertNoFlag=YNI_Yes, CurrencyID='', BrokerIDByBank='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, TID=0, Digest=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.Gender = '' #性别, char
        self.CountryCode = '' #国家代码, char[21]
        self.CustType = '' #客户类型, char
        self.Address = '' #地址, char[101]
        self.ZipCode = '' #邮编, char[7]
        self.Telephone = '' #电话号码, char[41]
        self.MobilePhone = '' #手机, char[21]
        self.Fax = '' #传真, char[41]
        self.EMail = '' #电子邮件, char[41]
        self.MoneyAccountStatus = '' #资金账户状态, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.NewBankAccount = 'BankAccount' #新银行帐号, char[41]
        self.NewBankPassWord = 'Password' #新银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.BankAccType = '' #银行帐号类型, char
        self.InstallID = '' #安装编号, int
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.TID = '' #交易ID, int
        self.Digest = '' #摘要, char[36]

class ReqTransfer(BaseStruct): #转账请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, BankAccount='', BankPassWord='', AccountID='', Password='', InstallID=0, FutureSerial=0, UserID='', VerifyCertNoFlag=YNI_Yes, CurrencyID='', TradeAmount=0.0, FutureFetchAmount=0.0, FeePayFlag=FPF_BEN, CustFee=0.0, BrokerFee=0.0, Message='', Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', RequestID=0, TID=0, TransferStatus=TRFS_Normal):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.InstallID = '' #安装编号, int
        self.FutureSerial = '' #期货公司流水号, int
        self.UserID = '' #用户标识, char[16]
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.TradeAmount = '' #转帐金额, double
        self.FutureFetchAmount = 'TradeAmount' #期货可取金额, double
        self.FeePayFlag = '' #费用支付标志, char
        self.CustFee = '' #应收客户费用, double
        self.BrokerFee = 'FutureFee' #应收期货公司费用, double
        self.Message = 'AddInfo' #发送方给接收方的消息, char[129]
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.TransferStatus = '' #转账交易状态, char

class RspTransfer(BaseStruct): #银行发起银行资金转期货响应
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, BankAccount='', BankPassWord='', AccountID='', Password='', InstallID=0, FutureSerial=0, UserID='', VerifyCertNoFlag=YNI_Yes, CurrencyID='', TradeAmount=0.0, FutureFetchAmount=0.0, FeePayFlag=FPF_BEN, CustFee=0.0, BrokerFee=0.0, Message='', Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', RequestID=0, TID=0, TransferStatus=TRFS_Normal, ErrorID=0, ErrorMsg=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.InstallID = '' #安装编号, int
        self.FutureSerial = '' #期货公司流水号, int
        self.UserID = '' #用户标识, char[16]
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.TradeAmount = '' #转帐金额, double
        self.FutureFetchAmount = 'TradeAmount' #期货可取金额, double
        self.FeePayFlag = '' #费用支付标志, char
        self.CustFee = '' #应收客户费用, double
        self.BrokerFee = 'FutureFee' #应收期货公司费用, double
        self.Message = 'AddInfo' #发送方给接收方的消息, char[129]
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.TransferStatus = '' #转账交易状态, char
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class ReqRepeal(BaseStruct): #冲正请求
    def __init__(self, RepealTimeInterval=0, RepealedTimes=0, BankRepealFlag=BRF_BankNotNeedRepeal, BrokerRepealFlag=BRORF_BrokerNotNeedRepeal, PlateRepealSerial=0, BankRepealSerial='', FutureRepealSerial=0, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, BankAccount='', BankPassWord='', AccountID='', Password='', InstallID=0, FutureSerial=0, UserID='', VerifyCertNoFlag=YNI_Yes, CurrencyID='', TradeAmount=0.0, FutureFetchAmount=0.0, FeePayFlag=FPF_BEN, CustFee=0.0, BrokerFee=0.0, Message='', Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', RequestID=0, TID=0, TransferStatus=TRFS_Normal):
        self.RepealTimeInterval = '' #冲正时间间隔, int
        self.RepealedTimes = '' #已经冲正次数, int
        self.BankRepealFlag = '' #银行冲正标志, char
        self.BrokerRepealFlag = '' #期商冲正标志, char
        self.PlateRepealSerial = 'PlateSerial' #被冲正平台流水号, int
        self.BankRepealSerial = 'BankSerial' #被冲正银行流水号, char[13]
        self.FutureRepealSerial = 'FutureSerial' #被冲正期货流水号, int
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.InstallID = '' #安装编号, int
        self.FutureSerial = '' #期货公司流水号, int
        self.UserID = '' #用户标识, char[16]
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.TradeAmount = '' #转帐金额, double
        self.FutureFetchAmount = 'TradeAmount' #期货可取金额, double
        self.FeePayFlag = '' #费用支付标志, char
        self.CustFee = '' #应收客户费用, double
        self.BrokerFee = 'FutureFee' #应收期货公司费用, double
        self.Message = 'AddInfo' #发送方给接收方的消息, char[129]
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.TransferStatus = '' #转账交易状态, char

class RspRepeal(BaseStruct): #冲正响应
    def __init__(self, RepealTimeInterval=0, RepealedTimes=0, BankRepealFlag=BRF_BankNotNeedRepeal, BrokerRepealFlag=BRORF_BrokerNotNeedRepeal, PlateRepealSerial=0, BankRepealSerial='', FutureRepealSerial=0, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, BankAccount='', BankPassWord='', AccountID='', Password='', InstallID=0, FutureSerial=0, UserID='', VerifyCertNoFlag=YNI_Yes, CurrencyID='', TradeAmount=0.0, FutureFetchAmount=0.0, FeePayFlag=FPF_BEN, CustFee=0.0, BrokerFee=0.0, Message='', Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', RequestID=0, TID=0, TransferStatus=TRFS_Normal, ErrorID=0, ErrorMsg=''):
        self.RepealTimeInterval = '' #冲正时间间隔, int
        self.RepealedTimes = '' #已经冲正次数, int
        self.BankRepealFlag = '' #银行冲正标志, char
        self.BrokerRepealFlag = '' #期商冲正标志, char
        self.PlateRepealSerial = 'PlateSerial' #被冲正平台流水号, int
        self.BankRepealSerial = 'BankSerial' #被冲正银行流水号, char[13]
        self.FutureRepealSerial = 'FutureSerial' #被冲正期货流水号, int
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.InstallID = '' #安装编号, int
        self.FutureSerial = '' #期货公司流水号, int
        self.UserID = '' #用户标识, char[16]
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.TradeAmount = '' #转帐金额, double
        self.FutureFetchAmount = 'TradeAmount' #期货可取金额, double
        self.FeePayFlag = '' #费用支付标志, char
        self.CustFee = '' #应收客户费用, double
        self.BrokerFee = 'FutureFee' #应收期货公司费用, double
        self.Message = 'AddInfo' #发送方给接收方的消息, char[129]
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.TransferStatus = '' #转账交易状态, char
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class ReqQueryAccount(BaseStruct): #查询账户信息请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, BankAccount='', BankPassWord='', AccountID='', Password='', FutureSerial=0, InstallID=0, UserID='', VerifyCertNoFlag=YNI_Yes, CurrencyID='', Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', RequestID=0, TID=0):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.FutureSerial = '' #期货公司流水号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int

class RspQueryAccount(BaseStruct): #查询账户信息响应
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, BankAccount='', BankPassWord='', AccountID='', Password='', FutureSerial=0, InstallID=0, UserID='', VerifyCertNoFlag=YNI_Yes, CurrencyID='', Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', RequestID=0, TID=0, BankUseAmount=0.0, BankFetchAmount=0.0):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.FutureSerial = '' #期货公司流水号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.BankUseAmount = 'TradeAmount' #银行可用金额, double
        self.BankFetchAmount = 'TradeAmount' #银行可取金额, double

class FutureSignIO(BaseStruct): #期商签到签退
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Digest = '' #摘要, char[36]
        self.CurrencyID = '' #币种代码, char[4]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int

class RspFutureSignIn(BaseStruct): #期商签到响应
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0, ErrorID=0, ErrorMsg='', PinKey='', MacKey=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Digest = '' #摘要, char[36]
        self.CurrencyID = '' #币种代码, char[4]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]
        self.PinKey = 'PasswordKey' #PIN密钥, char[129]
        self.MacKey = 'PasswordKey' #MAC密钥, char[129]

class ReqFutureSignOut(BaseStruct): #期商签退请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Digest = '' #摘要, char[36]
        self.CurrencyID = '' #币种代码, char[4]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int

class RspFutureSignOut(BaseStruct): #期商签退响应
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0, ErrorID=0, ErrorMsg=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Digest = '' #摘要, char[36]
        self.CurrencyID = '' #币种代码, char[4]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class ReqQueryTradeResultBySerial(BaseStruct): #查询指定流水号的交易结果请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, Reference=0, RefrenceIssureType=TS_Bank, RefrenceIssure='', CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, BankAccount='', BankPassWord='', AccountID='', Password='', CurrencyID='', TradeAmount=0.0, Digest=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.Reference = 'Serial' #流水号, int
        self.RefrenceIssureType = 'InstitutionType' #本流水号发布者的机构类型, char
        self.RefrenceIssure = 'OrganCode' #本流水号发布者机构编码, char[36]
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.CurrencyID = '' #币种代码, char[4]
        self.TradeAmount = '' #转帐金额, double
        self.Digest = '' #摘要, char[36]

class RspQueryTradeResultBySerial(BaseStruct): #查询指定流水号的交易结果响应
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, ErrorID=0, ErrorMsg='', Reference=0, RefrenceIssureType=TS_Bank, RefrenceIssure='', OriginReturnCode='', OriginDescrInfoForReturnCode='', BankAccount='', BankPassWord='', AccountID='', Password='', CurrencyID='', TradeAmount=0.0, Digest=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]
        self.Reference = 'Serial' #流水号, int
        self.RefrenceIssureType = 'InstitutionType' #本流水号发布者的机构类型, char
        self.RefrenceIssure = 'OrganCode' #本流水号发布者机构编码, char[36]
        self.OriginReturnCode = 'ReturnCode' #原始返回代码, char[7]
        self.OriginDescrInfoForReturnCode = 'DescrInfoForReturnCode' #原始返回码描述, char[129]
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.CurrencyID = '' #币种代码, char[4]
        self.TradeAmount = '' #转帐金额, double
        self.Digest = '' #摘要, char[36]

class ReqDayEndFileReady(BaseStruct): #日终文件就绪请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, FileBusinessCode=FBC_Others, Digest=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.FileBusinessCode = '' #文件业务功能, char
        self.Digest = '' #摘要, char[36]

class ReturnResult(BaseStruct): #返回结果
    def __init__(self, ReturnCode='', DescrInfoForReturnCode=''):
        self.ReturnCode = '' #返回代码, char[7]
        self.DescrInfoForReturnCode = '' #返回码描述, char[129]

class VerifyFuturePassword(BaseStruct): #验证期货资金密码
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, AccountID='', Password='', BankAccount='', BankPassWord='', InstallID=0, TID=0):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.InstallID = '' #安装编号, int
        self.TID = '' #交易ID, int

class VerifyCustInfo(BaseStruct): #验证客户信息
    def __init__(self, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person):
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char

class VerifyFuturePasswordAndCustInfo(BaseStruct): #验证期货资金密码和客户信息
    def __init__(self, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, AccountID='', Password=''):
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]

class DepositResultInform(BaseStruct): #验证期货资金密码和客户信息
    def __init__(self, DepositSeqNo='', BrokerID='', InvestorID='', Deposit=0.0, RequestID=0, ReturnCode='', DescrInfoForReturnCode=''):
        self.DepositSeqNo = '' #出入金流水号，该流水号为银期报盘返回的流水号, char[15]
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.Deposit = 'Money' #入金金额, double
        self.RequestID = '' #请求编号, int
        self.ReturnCode = '' #返回代码, char[7]
        self.DescrInfoForReturnCode = '' #返回码描述, char[129]

class ReqSyncKey(BaseStruct): #交易核心向银期报盘发出密钥同步请求
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Message = 'AddInfo' #交易核心给银期报盘的消息, char[129]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int

class RspSyncKey(BaseStruct): #交易核心向银期报盘发出密钥同步响应
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0, ErrorID=0, ErrorMsg=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Message = 'AddInfo' #交易核心给银期报盘的消息, char[129]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class NotifyQueryAccount(BaseStruct): #查询账户信息通知
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, CustomerName='', IdCardType=ICT_EID, IdentifiedCardNo='', CustType=CUSTT_Person, BankAccount='', BankPassWord='', AccountID='', Password='', FutureSerial=0, InstallID=0, UserID='', VerifyCertNoFlag=YNI_Yes, CurrencyID='', Digest='', BankAccType=BAT_BankBook, DeviceID='', BankSecuAccType=BAT_BankBook, BrokerIDByBank='', BankSecuAcc='', BankPwdFlag=BPWDF_NoCheck, SecuPwdFlag=BPWDF_NoCheck, OperNo='', RequestID=0, TID=0, BankUseAmount=0.0, BankFetchAmount=0.0, ErrorID=0, ErrorMsg=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.CustomerName = 'IndividualName' #客户姓名, char[51]
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CustType = '' #客户类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankPassWord = 'Password' #银行密码, char[41]
        self.AccountID = '' #投资者帐号, char[15]
        self.Password = '' #期货密码, char[41]
        self.FutureSerial = '' #期货公司流水号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.VerifyCertNoFlag = 'YesNoIndicator' #验证客户证件号码标志, char
        self.CurrencyID = '' #币种代码, char[4]
        self.Digest = '' #摘要, char[36]
        self.BankAccType = '' #银行帐号类型, char
        self.DeviceID = '' #渠道标志, char[3]
        self.BankSecuAccType = 'BankAccType' #期货单位帐号类型, char
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.BankSecuAcc = 'BankAccount' #期货单位帐号, char[41]
        self.BankPwdFlag = 'PwdFlag' #银行密码标志, char
        self.SecuPwdFlag = 'PwdFlag' #期货资金密码核对标志, char
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.BankUseAmount = 'TradeAmount' #银行可用金额, double
        self.BankFetchAmount = 'TradeAmount' #银行可取金额, double
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class TransferSerial(BaseStruct): #银期转账交易流水表
    def __init__(self, PlateSerial=0, TradeDate='', TradingDay='', TradeTime='', TradeCode='', SessionID=0, BankID='', BankBranchID='', BankAccType=BAT_BankBook, BankAccount='', BankSerial='', BrokerID='', BrokerBranchID='', FutureAccType=FAT_BankBook, AccountID='', InvestorID='', FutureSerial=0, IdCardType=ICT_EID, IdentifiedCardNo='', CurrencyID='', TradeAmount=0.0, CustFee=0.0, BrokerFee=0.0, AvailabilityFlag=AVAF_Invalid, OperatorCode='', BankNewAccount='', ErrorID=0, ErrorMsg=''):
        self.PlateSerial = '' #平台流水号, int
        self.TradeDate = '' #交易发起方日期, char[9]
        self.TradingDay = 'Date' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.TradeCode = '' #交易代码, char[7]
        self.SessionID = '' #会话编号, int
        self.BankID = '' #银行编码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构编码, char[5]
        self.BankAccType = '' #银行帐号类型, char
        self.BankAccount = '' #银行帐号, char[41]
        self.BankSerial = '' #银行流水号, char[13]
        self.BrokerID = '' #期货公司编码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.FutureAccType = '' #期货公司帐号类型, char
        self.AccountID = '' #投资者帐号, char[15]
        self.InvestorID = '' #投资者代码, char[15]
        self.FutureSerial = '' #期货公司流水号, int
        self.IdCardType = '' #证件类型, char
        self.IdentifiedCardNo = '' #证件号码, char[51]
        self.CurrencyID = '' #币种代码, char[4]
        self.TradeAmount = '' #交易金额, double
        self.CustFee = '' #应收客户费用, double
        self.BrokerFee = 'FutureFee' #应收期货公司费用, double
        self.AvailabilityFlag = '' #有效标志, char
        self.OperatorCode = '' #操作员, char[17]
        self.BankNewAccount = 'BankAccount' #新银行帐号, char[41]
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class QryTransferSerial(BaseStruct): #请求查询转帐流水
    def __init__(self, BrokerID='', AccountID='', BankID=''):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.AccountID = '' #投资者帐号, char[15]
        self.BankID = '' #银行编码, char[4]

class NotifyFutureSignIn(BaseStruct): #期商签到通知
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0, ErrorID=0, ErrorMsg='', PinKey='', MacKey=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Digest = '' #摘要, char[36]
        self.CurrencyID = '' #币种代码, char[4]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]
        self.PinKey = 'PasswordKey' #PIN密钥, char[129]
        self.MacKey = 'PasswordKey' #MAC密钥, char[129]

class NotifyFutureSignOut(BaseStruct): #期商签退通知
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0, ErrorID=0, ErrorMsg=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Digest = '' #摘要, char[36]
        self.CurrencyID = '' #币种代码, char[4]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class NotifySyncKey(BaseStruct): #交易核心向银期报盘发出密钥同步处理结果的通知
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='', TradingDay='', PlateSerial=0, LastFragment=LF_Yes, SessionID=0, InstallID=0, UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID=0, TID=0, ErrorID=0, ErrorMsg=''):
        self.TradeCode = '' #业务功能码, char[7]
        self.BankID = '' #银行代码, char[4]
        self.BankBranchID = 'BankBrchID' #银行分支机构代码, char[5]
        self.BrokerID = '' #期商代码, char[11]
        self.BrokerBranchID = 'FutureBranchID' #期商分支机构代码, char[31]
        self.TradeDate = '' #交易日期, char[9]
        self.TradeTime = '' #交易时间, char[9]
        self.BankSerial = '' #银行流水号, char[13]
        self.TradingDay = 'TradeDate' #交易系统日期 , char[9]
        self.PlateSerial = 'Serial' #银期平台消息流水号, int
        self.LastFragment = '' #最后分片标志, char
        self.SessionID = '' #会话号, int
        self.InstallID = '' #安装编号, int
        self.UserID = '' #用户标识, char[16]
        self.Message = 'AddInfo' #交易核心给银期报盘的消息, char[129]
        self.DeviceID = '' #渠道标志, char[3]
        self.BrokerIDByBank = 'BankCodingForFuture' #期货公司银行编码, char[33]
        self.OperNo = '' #交易柜员, char[17]
        self.RequestID = '' #请求编号, int
        self.TID = '' #交易ID, int
        self.ErrorID = '' #错误代码, int
        self.ErrorMsg = '' #错误信息, char[81]

class MaxStockPositionAmount(BaseStruct): #客户最大持仓数量
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', MaxAmount=0):
        self.BrokerID = '' #经纪公司代码, char[11]
        self.InvestorID = '' #投资者代码, char[15]
        self.InstrumentID = '' #合约代码, char[31]
        self.MaxAmount = 'Volume' #最大持仓数量, int

error = {'NONE':0, 0:'综合交易平台：正确', 'INVALID_DATA_SYNC_STATUS':1, 1:'综合交易平台：不在已同步状态', 'INCONSISTENT_INFORMATION':2, 2:'综合交易平台：会话信息不一致', 'INVALID_LOGIN':3, 3:'综合交易平台：不合法的登录', 'USER_NOT_ACTIVE':4, 4:'综合交易平台：用户不活跃', 'DUPLICATE_LOGIN':5, 5:'综合交易平台：重复的登录', 'NOT_LOGIN_YET':6, 6:'综合交易平台：还没有登录', 'NOT_INITED':7, 7:'综合交易平台：还没有初始化', 'FRONT_NOT_ACTIVE':8, 8:'综合交易平台：前置不活跃', 'NO_PRIVILEGE':9, 9:'综合交易平台：无此权限', 'CHANGE_OTHER_PASSWORD':10, 10:'综合交易平台：修改别人的口令', 'USER_NOT_FOUND':11, 11:'综合交易平台：找不到该用户', 'BROKER_NOT_FOUND':12, 12:'综合交易平台：找不到该经纪公司', 'INVESTOR_NOT_FOUND':13, 13:'综合交易平台：找不到投资者', 'OLD_PASSWORD_MISMATCH':14, 14:'综合交易平台：原口令不匹配', 'BAD_FIELD':15, 15:'综合交易平台：报单字段有误', 'INSTRUMENT_NOT_FOUND':16, 16:'综合交易平台：找不到合约', 'INSTRUMENT_NOT_TRADING':17, 17:'综合交易平台：合约不能交易', 'NOT_EXCHANGE_PARTICIPANT':18, 18:'综合交易平台：经纪公司不是交易所的会员', 'INVESTOR_NOT_ACTIVE':19, 19:'综合交易平台：投资者不活跃', 'NOT_EXCHANGE_CLIENT':20, 20:'综合交易平台：投资者未在交易所开户', 'NO_VALID_TRADER_AVAILABLE':21, 21:'综合交易平台：该交易席位未连接到交易所', 'DUPLICATE_ORDER_REF':22, 22:'综合交易平台：报单错误：不允许重复报单', 'BAD_ORDER_ACTION_FIELD':23, 23:'综合交易平台：错误的报单操作字段', 'DUPLICATE_ORDER_ACTION_REF':24, 24:'综合交易平台：撤单已报送，不允许重复撤单', 'ORDER_NOT_FOUND':25, 25:'综合交易平台：撤单找不到相应报单', 'INSUITABLE_ORDER_STATUS':26, 26:'综合交易平台：报单已全成交或已撤销，不能再撤', 'UNSUPPORTED_FUNCTION':27, 27:'综合交易平台：不支持的功能', 'NO_TRADING_RIGHT':28, 28:'综合交易平台：没有报单交易权限', 'CLOSE_ONLY':29, 29:'综合交易平台：只能平仓', 'OVER_CLOSE_POSITION':30, 30:'综合交易平台：平仓量超过持仓量', 'INSUFFICIENT_MONEY':31, 31:'综合交易平台：资金不足', 'DUPLICATE_PK':32, 32:'综合交易平台：主键重复', 'CANNOT_FIND_PK':33, 33:'综合交易平台：找不到主键', 'CAN_NOT_INACTIVE_BROKER':34, 34:'综合交易平台：设置经纪公司不活跃状态失败', 'BROKER_SYNCHRONIZING':35, 35:'综合交易平台：经纪公司正在同步', 'BROKER_SYNCHRONIZED':36, 36:'综合交易平台：经纪公司已同步', 'SHORT_SELL':37, 37:'综合交易平台：可卖出数量不足', 'INVALID_SETTLEMENT_REF':38, 38:'综合交易平台：不合法的结算引用', 'CFFEX_NETWORK_ERROR':39, 39:'综合交易平台：中金所网络连接失败', 'CFFEX_OVER_REQUEST':40, 40:'综合交易平台：中金所未处理请求超过许可数', 'CFFEX_OVER_REQUEST_PER_SECOND':41, 41:'综合交易平台：中金所每秒发送请求数超过许可数', 'SETTLEMENT_INFO_NOT_CONFIRMED':42, 42:'综合交易平台：结算结果未确认', 'DEPOSIT_NOT_FOUND':43, 43:'综合交易平台：没有对应的入金记录', 'EXCHANG_TRADING':44, 44:'综合交易平台：交易所已经进入连续交易状态', 'PARKEDORDER_NOT_FOUND':45, 45:'综合交易平台：找不到预埋（撤单）单', 'PARKEDORDER_HASSENDED':46, 46:'综合交易平台：预埋（撤单）单已经发送', 'PARKEDORDER_HASDELETE':47, 47:'综合交易平台：预埋（撤单）单已经删除', 'INVALID_INVESTORIDORPASSWORD':48, 48:'综合交易平台：无效的投资者或者密码', 'INVALID_LOGIN_IPADDRESS':49, 49:'综合交易平台：不合法的登录IP地址', 'OVER_CLOSETODAY_POSITION':50, 50:'综合交易平台：平今仓位不足', 'OVER_CLOSEYESTERDAY_POSITION':51, 51:'综合交易平台：平昨仓位不足', 'BROKER_NOT_ENOUGH_CONDORDER':52, 52:'综合交易平台：经纪公司没有足够可用的条件单数量', 'INVESTOR_NOT_ENOUGH_CONDORDER':53, 53:'综合交易平台：投资者没有足够可用的条件单数量', 'BROKER_NOT_SUPPORT_CONDORDER':54, 54:'综合交易平台：经纪公司不支持条件单', 'RESEND_ORDER_BROKERINVESTOR_NOTMATCH':55, 55:'综合交易平台：重发未知单经济公司/投资者不匹配', 'SYC_OTP_FAILED':56, 56:'综合交易平台：同步动态令牌失败', 'OTP_MISMATCH':57, 57:'综合交易平台：动态令牌校验错误', 'OTPPARAM_NOT_FOUND':58, 58:'综合交易平台：找不到动态令牌配置信息', 'UNSUPPORTED_OTPTYPE':59, 59:'综合交易平台：不支持的动态令牌类型', 'MARKETDATA_NOT_FOUND':60, 60:'综合交易平台：缺少需要的证券行情', 'AUTH_FAILED':61, 61:'综合交易平台：客户端认证失败', 'NOT_AUTHENT':62, 62:'综合交易平台：客户端未认证', 'SEND_INSTITUTION_CODE_ERROR':1000, 1000:'银期转账：发送机构代码错误', 'NO_GET_PLATFORM_SN':1001, 1001:'银期转账：取平台流水号错误', 'ILLEGAL_TRANSFER_BANK':1002, 1002:'银期转账：不合法的转账银行', 'ALREADY_OPEN_ACCOUNT':1003, 1003:'银期转账：已经开户', 'NOT_OPEN_ACCOUNT':1004, 1004:'银期转账：未开户', 'PROCESSING':1005, 1005:'银期转账：处理中', 'OVERTIME':1006, 1006:'银期转账：交易超时', 'RECORD_NOT_FOUND':1007, 1007:'银期转账：找不到记录', 'NO_FOUND_REVERSAL_ORIGINAL_TRANSACTION':1008, 1008:'银期转账：找不到被冲正的原始交易', 'CONNECT_HOST_FAILED':1009, 1009:'银期转账：连接主机失败', 'SEND_FAILED':1010, 1010:'银期转账：发送失败', 'LATE_RESPONSE':1011, 1011:'银期转账：迟到应答', 'REVERSAL_BANKID_NOT_MATCH':1012, 1012:'银期转账：冲正交易银行代码错误', 'REVERSAL_BANKACCOUNT_NOT_MATCH':1013, 1013:'银期转账：冲正交易银行账户错误', 'REVERSAL_BROKERID_NOT_MATCH':1014, 1014:'银期转账：冲正交易经纪公司代码错误', 'REVERSAL_ACCOUNTID_NOT_MATCH':1015, 1015:'银期转账：冲正交易资金账户错误', 'REVERSAL_AMOUNT_NOT_MATCH':1016, 1016:'银期转账：冲正交易交易金额错误', 'DB_OPERATION_FAILED':1017, 1017:'银期转账：数据库操作错误', 'SEND_ASP_FAILURE':1018, 1018:'银期转账：发送到交易系统失败', 'NOT_SIGNIN':1019, 1019:'银期转账：没有签到', 'ALREADY_SIGNIN':1020, 1020:'银期转账：已经签到', 'AMOUNT_OR_TIMES_OVER':1021, 1021:'银期转账：金额或次数超限', 'NOT_IN_TRANSFER_TIME':1022, 1022:'银期转账：这一时间段不能转账', 'BANK_SERVER_ERROR':1023, 1023:'银行主机错', 'BANK_SERIAL_IS_REPEALED':1024, 1024:'银期转账：银行已经冲正', 'BANK_SERIAL_NOT_EXIST':1025, 1025:'银期转账：银行流水不存在', 'NOT_ORGAN_MAP':1026, 1026:'银期转账：机构没有签约', 'EXIST_TRANSFER':1027, 1027:'银期转账：存在转账，不能销户', 'BANK_FORBID_REVERSAL':1028, 1028:'银期转账：银行不支持冲正', 'DUP_BANK_SERIAL':1029, 1029:'银期转账：重复的银行流水', 'FBT_SYSTEM_BUSY':1030, 1030:'银期转账：转账系统忙，稍后再试', 'MACKEY_SYNCING':1031, 1031:'银期转账：MAC密钥正在同步', 'ACCOUNTID_ALREADY_REGISTER':1032, 1032:'银期转账：资金账户已经登记', 'BANKACCOUNT_ALREADY_REGISTER':1033, 1033:'银期转账：银行账户已经登记', 'DUP_BANK_SERIAL_REDO_OK':1034, 1034:'银期转账：重复的银行流水,重发成功', 'NO_VALID_BANKOFFER_AVAILABLE':2000, 2000:'综合交易平台：该报盘未连接到银行', 'PASSWORD_MISMATCH':2001, 2001:'综合交易平台：资金密码错误', 'DUPLATION_BANK_SERIAL':2004, 2004:'综合交易平台：银行流水号重复', 'DUPLATION_OFFER_SERIAL':2005, 2005:'综合交易平台：报盘流水号重复', 'SERIAL_NOT_EXSIT':2006, 2006:'综合交易平台：被冲正流水不存在(冲正交易)', 'SERIAL_IS_REPEALED':2007, 2007:'综合交易平台：原流水已冲正(冲正交易)', 'SERIAL_MISMATCH':2008, 2008:'综合交易平台：与原流水信息不符(冲正交易)', 'IdentifiedCardNo_MISMATCH':2009, 2009:'综合交易平台：证件号码或类型错误', 'ACCOUNT_NOT_FUND':2011, 2011:'综合交易平台：资金账户不存在', 'ACCOUNT_NOT_ACTIVE':2012, 2012:'综合交易平台：资金账户已经销户', 'NOT_ALLOW_REPEAL_BYMANUAL':2013, 2013:'综合交易平台：该交易不能执行手工冲正', 'AMOUNT_OUTOFTHEWAY':2014, 2014:'综合交易平台：转帐金额错误', 'WAITING_OFFER_RSP':999999, 999999:'综合交易平台：等待银期报盘处理结果', 'NON_TRADALE_STOCK_VOLUME_PRICE_NOTMACTH':3000, 3000:'综合交易平台：非交易报单价格数量和业务不匹配', 'INVALID_PRODUCT':3001, 3001:'综合交易平台：找不到产品信息', 'INVALID_BUY_VOLUME':3002, 3002:'综合交易平台：不合法的买入数量', 'INVALID_SELL_VOLUME':3003, 3003:'综合交易平台：不合法的卖出数量', 'ONLY_ETF_CAN_PURRED':3004, 3004:'综合交易平台：非ETF产品不能申购赎回', 'INVALID_ETF_VOLUME':3005, 3005:'综合交易平台：ETF申购赎回数量错误', 'NOT_ENOUGH_ETF_PUR_VOLUME':3006, 3006:'综合交易平台：ETF申购无足够股票', 'NOT_ENOUGH_ETF_RED_VOLUME':3007, 3007:'综合交易平台：ETF赎回无足够基金', 'UNAUTHENTNOTVALIDFORTRADE':3008, 3008:'综合交易平台：未认证的用户没有下单权限', 'OVERAMOUNTLIMIT':3009, 3009:'综合交易平台：买入超过持仓数量限制', 'OVERETFCASHRATIO':3010, 3010:'综合交易平台：现金替换金额超过限制', 'ETF_PURRED_NOTSUPCALCEL':3011, 3011:'综合交易平台：ETF申赎不能撤单', 'INVALID_FOR_CREDITACCOUNT':3012, 3012:'综合交易平台：非信用账户不支持此类交易'}

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
    else:
        for k in error:
            if not isinstance(k, str): error[k] = error[k].decode('utf-8')
    edvs = {'ContingentCondition':CC_Immediately, 'TradeType':TRDT_Common, 'AllWithoutTrade':AWT_Enable, 'PositionDateType':PDT_UseHistory, 'TradingRight':TR_Allow, 'UserRightType':URT_Logon, 'InstitutionType':TS_Bank, 'FindMarginRateAlgoID':FMRA_Base, 'HedgeFlag':HF_Speculation, 'TraderConnectStatus':TCS_NotConnected, 'CustType':CUSTT_Person, 'PositionType':PT_Net, 'ProductClass':PC_Futures, 'OrderPriceType':OPT_AnyPrice, 'ParkedOrderStatus':PAOS_NotSend, 'YesNoIndicator':YNI_Yes, 'HandlePositionAlgoID':HPA_Base, 'Direction':D_Buy, 'OffsetFlag':OF_Open, 'PosiDirection':PD_Net, 'PwdFlag':BPWDF_NoCheck, 'PersonType':PST_Order, 'ExchangeProperty':EXP_Normal, 'UserType':UT_Investor, 'TimeCondition':TC_IOC, 'OrderStatus':OST_AllTraded, 'ActionFlag':AF_Delete, 'OrderSubmitStatus':OSS_InsertSubmitted, 'DataSyncStatus':DS_Asynchronous, 'TransferValidFlag':TVF_Invalid, 'AvailabilityFlag':AVAF_Invalid, 'InstStatusEnterReason':IER_Automatic, 'PositionDate':PSD_Today, 'Algorithm':AG_All, 'ForceCloseReason':FCC_NotForceClose, 'OrderType':ORDT_Normal, 'FeePayFlag':FPF_BEN, 'FuturePwdFlag':FPWD_UnCheck, 'Gender':GD_Unknown, 'FunctionCode':FC_DataAsync, 'OrderSource':OSRC_Participant, 'CashExchangeCode':CEC_Exchange, 'BrokerRepealFlag':BRORF_BrokerNotNeedRepeal, 'InstrumentStatus':IS_BeforeTrading, 'BankRepealFlag':BRF_BankNotNeedRepeal, 'HandleTradingAccountAlgoID':HTAA_Base, 'IdCardType':ICT_EID, 'MarginPriceType':MPT_PreSettlementPrice, 'FileBusinessCode':FBC_Others, 'IncludeCloseProfit':ICP_Include, 'CFMMCKeyKind':CFMMCKK_REQUEST, 'BankAccType':BAT_BankBook, 'LastFragment':LF_Yes, 'InstLifePhase':IP_NotStart, 'FutureAccType':FAT_BankBook, 'VolumeCondition':VC_AV, 'MoneyAccountStatus':MAS_Normal, 'OTPType':OTP_NONE, 'UserEventType':UET_All, 'InvestorRange':IR_All, 'TransferStatus':TRFS_Normal, 'PriceSource':PSRC_LastPrice, 'TradingRole':ER_Broker, 'BrokerFunctionCode':BFC_ForceUserLogout, 'OrderActionStatus':OAS_Submitted}
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
