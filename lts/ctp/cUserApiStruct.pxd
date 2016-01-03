# -*- coding: utf-8 -*-

from cUserApiDataType cimport *

cdef extern from "SecurityFtdcUserApiStruct.h":
    cdef struct CRspInfoField "CSecurityFtdcRspInfoField": #响应信息
        TErrorIDType ErrorID #错误代码, int
        TErrorMsgType ErrorMsg #错误信息, char[81]
    cdef struct CExchangeField "CSecurityFtdcExchangeField": #交易所
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TExchangeNameType ExchangeName #交易所名称, char[31]
        TExchangePropertyType ExchangeProperty #交易所属性, char
    cdef struct CProductField "CSecurityFtdcProductField": #产品
        TInstrumentIDType ProductID #产品代码, char[31]
        TProductNameType ProductName #产品名称, char[21]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TProductClassType ProductClass #产品类型, char
        TVolumeMultipleType VolumeMultiple #合约数量乘数, int
        TPriceType PriceTick #最小变动价位, double
        TVolumeType MaxMarketOrderVolume #市价单最大下单量, int
        TVolumeType MinMarketOrderVolume #市价单最小下单量, int
        TVolumeType MaxLimitOrderVolume #限价单最大下单量, int
        TVolumeType MinLimitOrderVolume #限价单最小下单量, int
        TPositionTypeType PositionType #持仓类型, char
        TPositionDateTypeType PositionDateType #持仓日期类型, char
        TVolumeType EFTMinTradeVolume #ETF最小交易单位, int
    cdef struct CInstrumentField "CSecurityFtdcInstrumentField": #合约
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TInstrumentNameType InstrumentName #合约名称, char[21]
        TExchangeInstIDType ExchangeInstID #合约在交易所的代码, char[31]
        TInstrumentIDType ProductID #产品代码, char[31]
        TProductClassType ProductClass #产品类型, char
        TYearType DeliveryYear #交割年份, int
        TMonthType DeliveryMonth #交割月, int
        TVolumeType MaxMarketOrderVolume #市价单最大下单量, int
        TVolumeType MinMarketOrderVolume #市价单最小下单量, int
        TVolumeType MaxLimitOrderVolume #限价单最大下单量, int
        TVolumeType MinLimitOrderVolume #限价单最小下单量, int
        TVolumeMultipleType VolumeMultiple #合约数量乘数, int
        TPriceType PriceTick #最小变动价位, double
        TDateType CreateDate #创建日, char[9]
        TDateType OpenDate #上市日, char[9]
        TDateType ExpireDate #到期日, char[9]
        TDateType StartDelivDate #开始交割日, char[9]
        TDateType EndDelivDate #结束交割日, char[9]
        TInstLifePhaseType InstLifePhase #合约生命周期状态, char
        TBoolType IsTrading #当前是否交易, int
        TPositionTypeType PositionType #持仓类型, char
        TBoolType OrderCanBeWithdraw #报单能否撤单, int
        TVolumeType MinBuyVolume #最小买下单单位, int
        TVolumeType MinSellVolume #最小卖下单单位, int
        TRightModelIDType RightModelID #股票权限模版代码, char[31]
        TPosTradeTypeType PosTradeType #持仓交易类型, char
        TInstrumentIDType MarketID #市场代码, char[31]
    cdef struct CBrokerField "CSecurityFtdcBrokerField": #经纪公司
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TBrokerAbbrType BrokerAbbr #经纪公司简称, char[9]
        TBrokerNameType BrokerName #经纪公司名称, char[81]
        TBoolType IsActive #是否活跃, int
    cdef struct CPartBrokerField "CSecurityFtdcPartBrokerField": #会员编码和经纪公司编码对照表
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TBoolType IsActive #是否活跃, int
    cdef struct CInvestorField "CSecurityFtdcInvestorField": #投资者
        TInvestorIDType InvestorID #投资者代码, char[15]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorGroupID #投资者分组代码, char[15]
        TPartyNameType InvestorName #投资者名称, char[81]
        TIdCardTypeType IdentifiedCardType #证件类型, char
        TIdentifiedCardNoType IdentifiedCardNo #证件号码, char[51]
        TBoolType IsActive #是否活跃, int
        TTraderIDType SHBranchID #上海营业部编号, char[21]
        TTraderIDType SZBranchID #深圳营业部编号, char[21]
    cdef struct CTradingCodeField "CSecurityFtdcTradingCodeField": #交易编码
        TInvestorIDType InvestorID #投资者代码, char[15]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TClientIDType ClientID #客户代码, char[21]
        TBoolType IsActive #是否活跃, int
        TAccountIDType AccountID #AccountID, char[15]
        TTraderIDType PBU #交易单元号, char[21]
        TClientTypeType ClientType #ClientType, char
    cdef struct CSuperUserField "CSecurityFtdcSuperUserField": #管理用户
        TUserIDType UserID #用户代码, char[16]
        TUserNameType UserName #用户名称, char[81]
        TPasswordType Password #密码, char[41]
        TBoolType IsActive #是否活跃, int
    cdef struct CSuperUserFunctionField "CSecurityFtdcSuperUserFunctionField": #管理用户功能权限
        TUserIDType UserID #用户代码, char[16]
        TFunctionCodeType FunctionCode #功能代码, char
    cdef struct CBrokerUserField "CSecurityFtdcBrokerUserField": #经纪公司用户
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TUserNameType UserName #用户名称, char[81]
        TUserTypeType UserType #用户类型, char
        TBoolType IsActive #是否活跃, int
        TBoolType IsUsingOTP #是否使用令牌, int
    cdef struct CBrokerUserFunctionField "CSecurityFtdcBrokerUserFunctionField": #经纪公司用户功能权限
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TBrokerFunctionCodeType BrokerFunctionCode #经纪公司功能代码, char
    cdef struct CTradingAccountField "CSecurityFtdcTradingAccountField": #资金账户
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TAccountIDType AccountID #投资者帐号, char[15]
        TMoneyType PreMortgage #上次质押金额, double
        TMoneyType PreCredit #上次信用额度, double
        TMoneyType PreDeposit #上次存款额, double
        TMoneyType PreBalance #上次结算准备金, double
        TMoneyType PreMargin #上次占用的保证金, double
        TMoneyType InterestBase #利息基数, double
        TMoneyType Interest #利息收入, double
        TMoneyType Deposit #入金金额, double
        TMoneyType Withdraw #出金金额, double
        TMoneyType FrozenMargin #冻结的保证金, double
        TMoneyType FrozenCash #冻结的资金, double
        TMoneyType FrozenCommission #冻结的手续费, double
        TMoneyType CurrMargin #当前保证金总额, double
        TMoneyType CashIn #资金差额, double
        TMoneyType Commission #手续费, double
        TMoneyType Balance #结算准备金, double
        TMoneyType Available #现金, double
        TMoneyType WithdrawQuota #可取资金, double
        TMoneyType Reserve #基本准备金, double
        TDateType TradingDay #交易日, char[9]
        TMoneyType Credit #保证金可用余额, double
        TMoneyType Mortgage #质押金额, double
        TMoneyType ExchangeMargin #交易所保证金, double
        TMoneyType DeliveryMargin #投资者交割保证金, double
        TMoneyType ExchangeDeliveryMargin #交易所交割保证金, double
        TMoneyType FrozenTransferFee #冻结的过户费, double
        TMoneyType FrozenStampTax #冻结的印花税, double
        TMoneyType TransferFee #过户费, double
        TMoneyType StampTax #印花税, double
        TMoneyType ConversionAmount #折算金额, double
        TMoneyType CreditAmount #授信额度, double
        TMoneyType StockValue #证券总价值, double
        TMoneyType BondRepurchaseAmount #国债回购占用资金, double
        TMoneyType ReverseRepurchaseAmount #国债逆回购占用资金, double
        TCurrencyCodeType CurrencyCode #币种, char[4]
        TAccountTypeType AccountType #账户类型, char
        TMoneyType MarginTradeAmount #融资买入金额, double
        TMoneyType ShortSellAmount #融券卖出金额, double
        TMoneyType MarginTradeProfit #融资持仓盈亏, double
        TMoneyType ShortSellProfit #融券持仓盈亏, double
        TMoneyType SSStockValue #融券总市值, double
        TRatioType CreditRatio #维持担保比例, double
    cdef struct CLoginForbiddenUserField "CSecurityFtdcLoginForbiddenUserField": #禁止登录用户
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
    cdef struct CDepthMarketDataField "CSecurityFtdcDepthMarketDataField": #深度行情
        TDateType TradingDay #交易日, char[9]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TExchangeInstIDType ExchangeInstID #合约在交易所的代码, char[31]
        TPriceType LastPrice #最新价, double
        TPriceType PreSettlementPrice #上次结算价, double
        TPriceType PreClosePrice #昨收盘, double
        TLargeVolumeType PreOpenInterest #昨持仓量, double
        TPriceType OpenPrice #今开盘, double
        TPriceType HighestPrice #最高价, double
        TPriceType LowestPrice #最低价, double
        TVolumeType Volume #数量, int
        TMoneyType Turnover #成交金额, double
        TLargeVolumeType OpenInterest #持仓量, double
        TPriceType ClosePrice #今收盘, double
        TPriceType SettlementPrice #本次结算价, double
        TPriceType UpperLimitPrice #涨停板价, double
        TPriceType LowerLimitPrice #跌停板价, double
        TRatioType PreDelta #昨虚实度, double
        TRatioType CurrDelta #今虚实度, double
        TTimeType UpdateTime #最后修改时间, char[9]
        TMillisecType UpdateMillisec #最后修改毫秒, int
        TPriceType BidPrice1 #申买价一, double
        TVolumeType BidVolume1 #申买量一, int
        TPriceType AskPrice1 #申卖价一, double
        TVolumeType AskVolume1 #申卖量一, int
        TPriceType BidPrice2 #申买价二, double
        TVolumeType BidVolume2 #申买量二, int
        TPriceType AskPrice2 #申卖价二, double
        TVolumeType AskVolume2 #申卖量二, int
        TPriceType BidPrice3 #申买价三, double
        TVolumeType BidVolume3 #申买量三, int
        TPriceType AskPrice3 #申卖价三, double
        TVolumeType AskVolume3 #申卖量三, int
        TPriceType BidPrice4 #申买价四, double
        TVolumeType BidVolume4 #申买量四, int
        TPriceType AskPrice4 #申卖价四, double
        TVolumeType AskVolume4 #申卖量四, int
        TPriceType BidPrice5 #申买价五, double
        TVolumeType BidVolume5 #申买量五, int
        TPriceType AskPrice5 #申卖价五, double
        TVolumeType AskVolume5 #申卖量五, int
        TPriceType AveragePrice #当日均价, double
        TDateType ActionDay #业务日期, char[9]
    cdef struct CInstrumentTradingRightField "CSecurityFtdcInstrumentTradingRightField": #投资者合约交易权限
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TInvestorRangeType InvestorRange #投资者范围, char
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TDirectionType Direction #买卖, char
        TTradingRightType TradingRight #交易权限, char
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TInstrumentRangeType InstrumentRange #股票权限分类, char
    cdef struct CInvestorPositionDetailField "CSecurityFtdcInvestorPositionDetailField": #投资者持仓明细
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        THedgeFlagType HedgeFlag #投机套保标志, char
        TDirectionType Direction #买卖, char
        TDateType OpenDate #开仓日期, char[9]
        TTradeIDType TradeID #成交编号, char[21]
        TVolumeType Volume #数量, int
        TPriceType OpenPrice #开仓价, double
        TDateType TradingDay #交易日, char[9]
        TTradeTypeType TradeType #成交类型, char
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TMoneyType Margin #投资者保证金, double
        TMoneyType ExchMargin #交易所保证金, double
        TPriceType LastSettlementPrice #昨结算价, double
        TPriceType SettlementPrice #结算价, double
        TVolumeType CloseVolume #平仓量, int
        TMoneyType CloseAmount #平仓金额, double
        TMoneyType TransferFee #过户费, double
        TMoneyType StampTax #印花税, double
        TMoneyType Commission #手续费, double
        TAccountIDType AccountID #AccountID, char[15]
        TVolumeType PledgeInPosition #质押入库数量, int
        TVolumeType PledgeInFrozenPosition #质押入库冻结数量, int
        TVolumeType RepurchasePosition #正回购使用的标准券数量, int
        TMoneyType Amount #融资融券金额, double
    cdef struct CBondInterestField "CSecurityFtdcBondInterestField": #债券利息
        TDateType TradingDay #交易日, char[9]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TInterestType Interest #利息, double
    cdef struct CMarketRationInfoField "CSecurityFtdcMarketRationInfoField": #市值配售信息
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TVolumeType RationVolume #可配售手数, int
    cdef struct CInstrumentCommissionRateField "CSecurityFtdcInstrumentCommissionRateField": #合约手续费率
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TInvestorRangeType InvestorRange #投资者范围, char
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TDirectionType Direction #买卖方向, char
        TRatioType StampTaxRateByMoney #印花税率, double
        TRatioType StampTaxRateByVolume #印花税率(按手数), double
        TRatioType TransferFeeRateByMoney #过户费率, double
        TRatioType TransferFeeRateByVolume #过户费率(按手数), double
        TRatioType TradeFeeByMoney #交易费, double
        TRatioType TradeFeeByVolume #交易费(按手数), double
        TRatioType MarginByMoney #交易附加费率, double
        TPriceType MinTradeFee #最小过户费, double
    cdef struct CExcessStockInfoField "CSecurityFtdcExcessStockInfoField": #余券信息
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TVolumeType ExcessVolume #余券数量, int
        TVolumeType ExcessFrozenVolume #余券冻结数量, int
    cdef struct CTraderOfferField "CSecurityFtdcTraderOfferField": #交易所交易员报盘机
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TPasswordType Password #密码, char[41]
        TInstallIDType InstallID #安装编号, int
        TOrderLocalIDType OrderLocalID #本地报单编号, char[13]
        TTraderConnectStatusType TraderConnectStatus #交易所交易员连接状态, char
        TDateType ConnectRequestDate #发出连接请求的日期, char[9]
        TTimeType ConnectRequestTime #发出连接请求的时间, char[9]
        TDateType LastReportDate #上次报告日期, char[9]
        TTimeType LastReportTime #上次报告时间, char[9]
        TDateType ConnectDate #完成连接日期, char[9]
        TTimeType ConnectTime #完成连接时间, char[9]
        TDateType StartDate #启动日期, char[9]
        TTimeType StartTime #启动时间, char[9]
        TDateType TradingDay #交易日, char[9]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
    cdef struct CMDTraderOfferField "CSecurityFtdcMDTraderOfferField": #交易所行情报盘机
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TPasswordType Password #密码, char[41]
        TInstallIDType InstallID #安装编号, int
        TOrderLocalIDType OrderLocalID #本地报单编号, char[13]
        TTraderConnectStatusType TraderConnectStatus #交易所交易员连接状态, char
        TDateType ConnectRequestDate #发出连接请求的日期, char[9]
        TTimeType ConnectRequestTime #发出连接请求的时间, char[9]
        TDateType LastReportDate #上次报告日期, char[9]
        TTimeType LastReportTime #上次报告时间, char[9]
        TDateType ConnectDate #完成连接日期, char[9]
        TTimeType ConnectTime #完成连接时间, char[9]
        TDateType StartDate #启动日期, char[9]
        TTimeType StartTime #启动时间, char[9]
        TDateType TradingDay #交易日, char[9]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
    cdef struct CFrontStatusField "CSecurityFtdcFrontStatusField": #前置状态
        TFrontIDType FrontID #前置编号, int
        TDateType LastReportDate #上次报告日期, char[9]
        TTimeType LastReportTime #上次报告时间, char[9]
        TBoolType IsActive #是否活跃, int
    cdef struct CUserSessionField "CSecurityFtdcUserSessionField": #用户会话
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TDateType LoginDate #登录日期, char[9]
        TTimeType LoginTime #登录时间, char[9]
        TIPAddressType IPAddress #IP地址, char[16]
        TProductInfoType UserProductInfo #用户端产品信息, char[11]
        TProductInfoType InterfaceProductInfo #接口端产品信息, char[11]
        TProtocolInfoType ProtocolInfo #协议信息, char[11]
        TMacAddressType MacAddress #Mac地址, char[21]
    cdef struct COrderField "CSecurityFtdcOrderField": #报单
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TOrderRefType OrderRef #报单引用, char[13]
        TUserIDType UserID #用户代码, char[16]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TOrderPriceTypeType OrderPriceType #报单价格条件, char
        TDirectionType Direction #买卖方向, char
        TCombOffsetFlagType CombOffsetFlag #组合开平标志, char[5]
        TCombHedgeFlagType CombHedgeFlag #组合投机套保标志, char[5]
        TStockPriceType LimitPrice #价格, char[16]
        TVolumeType VolumeTotalOriginal #数量, int
        TTimeConditionType TimeCondition #有效期类型, char
        TDateType GTDDate #GTD日期, char[9]
        TVolumeConditionType VolumeCondition #成交量类型, char
        TVolumeType MinVolume #最小成交量, int
        TContingentConditionType ContingentCondition #触发条件, char
        TPriceType StopPrice #止损价, double
        TForceCloseReasonType ForceCloseReason #强平原因, char
        TBoolType IsAutoSuspend #自动挂起标志, int
        TBusinessUnitType BusinessUnit #业务单元, char[21]
        TRequestIDType RequestID #请求编号, int
        TOrderLocalIDType OrderLocalID #本地报单编号, char[13]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TClientIDType ClientID #客户代码, char[21]
        TExchangeInstIDType ExchangeInstID #合约在交易所的代码, char[31]
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
        TInstallIDType InstallID #安装编号, int
        TOrderSubmitStatusType OrderSubmitStatus #报单提交状态, char
        TAccountIDType AccountID #账户代码, char[15]
        TSequenceNoType NotifySequence #报单提示序号, int
        TDateType TradingDay #交易日, char[9]
        TOrderSysIDType OrderSysID #报单编号, char[21]
        TOrderSourceType OrderSource #报单来源, char
        TOrderStatusType OrderStatus #报单状态, char
        TOrderTypeType OrderType #报单类型, char
        TVolumeType VolumeTraded #今成交数量, int
        TVolumeType VolumeTotal #剩余数量, int
        TDateType InsertDate #报单日期, char[9]
        TTimeType InsertTime #委托时间, char[9]
        TTimeType ActiveTime #激活时间, char[9]
        TTimeType SuspendTime #挂起时间, char[9]
        TTimeType UpdateTime #最后修改时间, char[9]
        TTimeType CancelTime #撤销时间, char[9]
        TTraderIDType ActiveTraderID #最后修改交易所交易员代码, char[21]
        TParticipantIDType ClearingPartID #结算会员编号, char[11]
        TSequenceNoType SequenceNo #序号, int
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TProductInfoType UserProductInfo #用户端产品信息, char[11]
        TErrorMsgType StatusMsg #状态信息, char[81]
        TBoolType UserForceClose #用户强评标志, int
        TUserIDType ActiveUserID #操作用户代码, char[16]
        TSequenceNoType BrokerOrderSeq #经纪公司报单编号, int
        TOrderSysIDType RelativeOrderSysID #相关报单, char[21]
        TBranchIDType BranchID #营业部编号, char[9]
        TMoneyType TradeAmount #成交数量, double
        TBoolType IsETF #是否ETF, int
    cdef struct COrderActionField "CSecurityFtdcOrderActionField": #报单操作
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TOrderActionRefType OrderActionRef #报单操作引用, int
        TOrderRefType OrderRef #报单引用, char[13]
        TRequestIDType RequestID #请求编号, int
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TActionFlagType ActionFlag #操作标志, char
        TPriceType LimitPrice #价格, double
        TVolumeType VolumeChange #数量变化, int
        TDateType ActionDate #操作日期, char[9]
        TTimeType ActionTime #操作时间, char[9]
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
        TInstallIDType InstallID #安装编号, int
        TOrderLocalIDType OrderLocalID #本地报单编号, char[13]
        TOrderLocalIDType ActionLocalID #操作本地编号, char[13]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TClientIDType ClientID #客户代码, char[21]
        TBusinessUnitType BusinessUnit #业务单元, char[21]
        TOrderActionStatusType OrderActionStatus #报单操作状态, char
        TUserIDType UserID #用户代码, char[16]
        TBranchIDType BranchID #营业部编号, char[9]
        TErrorMsgType StatusMsg #状态信息, char[81]
        TInstrumentIDType InstrumentID #合约代码, char[31]
    cdef struct CErrOrderField "CSecurityFtdcErrOrderField": #错误报单
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TOrderRefType OrderRef #报单引用, char[13]
        TUserIDType UserID #用户代码, char[16]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TOrderPriceTypeType OrderPriceType #报单价格条件, char
        TDirectionType Direction #买卖方向, char
        TCombOffsetFlagType CombOffsetFlag #组合开平标志, char[5]
        TCombHedgeFlagType CombHedgeFlag #组合投机套保标志, char[5]
        TStockPriceType LimitPrice #价格, char[16]
        TVolumeType VolumeTotalOriginal #数量, int
        TTimeConditionType TimeCondition #有效期类型, char
        TDateType GTDDate #GTD日期, char[9]
        TVolumeConditionType VolumeCondition #成交量类型, char
        TVolumeType MinVolume #最小成交量, int
        TContingentConditionType ContingentCondition #触发条件, char
        TPriceType StopPrice #止损价, double
        TForceCloseReasonType ForceCloseReason #强平原因, char
        TBoolType IsAutoSuspend #自动挂起标志, int
        TBusinessUnitType BusinessUnit #业务单元, char[21]
        TRequestIDType RequestID #请求编号, int
        TBoolType UserForceClose #用户强评标志, int
        TErrorIDType ErrorID #错误代码, int
        TErrorMsgType ErrorMsg #错误信息, char[81]
    cdef struct CErrOrderActionField "CSecurityFtdcErrOrderActionField": #错误报单操作
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TOrderActionRefType OrderActionRef #报单操作引用, int
        TOrderRefType OrderRef #报单引用, char[13]
        TRequestIDType RequestID #请求编号, int
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TActionFlagType ActionFlag #操作标志, char
        TPriceType LimitPrice #价格, double
        TVolumeType VolumeChange #数量变化, int
        TDateType ActionDate #操作日期, char[9]
        TTimeType ActionTime #操作时间, char[9]
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
        TInstallIDType InstallID #安装编号, int
        TOrderLocalIDType OrderLocalID #本地报单编号, char[13]
        TOrderLocalIDType ActionLocalID #操作本地编号, char[13]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TClientIDType ClientID #客户代码, char[21]
        TBusinessUnitType BusinessUnit #业务单元, char[21]
        TOrderActionStatusType OrderActionStatus #报单操作状态, char
        TUserIDType UserID #用户代码, char[16]
        TBranchIDType BranchID #营业部编号, char[9]
        TErrorMsgType StatusMsg #状态信息, char[81]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TErrorIDType ErrorID #错误代码, int
        TErrorMsgType ErrorMsg #错误信息, char[81]
    cdef struct CTradeField "CSecurityFtdcTradeField": #成交
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TOrderRefType OrderRef #报单引用, char[13]
        TUserIDType UserID #用户代码, char[16]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TTradeIDType TradeID #成交编号, char[21]
        TDirectionType Direction #买卖方向, char
        TOrderSysIDType OrderSysID #报单编号, char[21]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TClientIDType ClientID #客户代码, char[21]
        TTradingRoleType TradingRole #交易角色, char
        TExchangeInstIDType ExchangeInstID #合约在交易所的代码, char[31]
        TOffsetFlagType OffsetFlag #开平标志, char
        THedgeFlagType HedgeFlag #投机套保标志, char
        TStockPriceType Price #价格, char[16]
        TVolumeType Volume #数量, int
        TDateType TradeDate #成交时期, char[9]
        TTimeType TradeTime #成交时间, char[9]
        TTradeTypeType TradeType #成交类型, char
        TPriceSourceType PriceSource #成交价来源, char
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
        TOrderLocalIDType OrderLocalID #本地报单编号, char[13]
        TParticipantIDType ClearingPartID #结算会员编号, char[11]
        TBusinessUnitType BusinessUnit #业务单元, char[21]
        TSequenceNoType SequenceNo #序号, int
        TTradeSourceType TradeSource #成交来源, char
        TDateType TradingDay #交易日, char[9]
        TSequenceNoType BrokerOrderSeq #经纪公司报单编号, int
    cdef struct CInvestorPositionField "CSecurityFtdcInvestorPositionField": #投资者持仓
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TPosiDirectionType PosiDirection #持仓多空方向, char
        THedgeFlagType HedgeFlag #投机套保标志, char
        TPositionDateType PositionDate #持仓日期, char
        TVolumeType YdPosition #上日持仓, int
        TVolumeType Position #今日持仓, int
        TVolumeType LongFrozen #多头冻结, int
        TVolumeType ShortFrozen #空头冻结, int
        TMoneyType LongFrozenAmount #开仓冻结金额, double
        TMoneyType ShortFrozenAmount #开仓冻结金额, double
        TVolumeType OpenVolume #开仓量, int
        TVolumeType CloseVolume #平仓量, int
        TMoneyType OpenAmount #开仓金额, double
        TMoneyType CloseAmount #平仓金额, double
        TMoneyType PositionCost #持仓成本, double
        TMoneyType FrozenCash #冻结的资金, double
        TMoneyType CashIn #资金差额, double
        TMoneyType Commission #手续费, double
        TPriceType PreSettlementPrice #上次结算价, double
        TPriceType SettlementPrice #本次结算价, double
        TDateType TradingDay #交易日, char[9]
        TMoneyType OpenCost #开仓成本, double
        TMoneyType ExchangeMargin #交易所保证金, double
        TVolumeType TodayPosition #今日持仓, int
        TMoneyType TransferFee #过户费, double
        TMoneyType StampTax #印花税, double
        TVolumeType TodayPurRedVolume #今日申购赎回数量, int
        TRatioType ConversionRate #折算率, double
        TMoneyType ConversionAmount #折算金额, double
        TMoneyType StockValue #证券价值, double
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TAccountIDType AccountID #AccountID, char[15]
        TVolumeType PledgeInPosition #质押入库数量, int
        TVolumeType RepurchasePosition #正回购使用的标准券数量, int
        TVolumeType PurRedShortFrozen #ETF申赎空头冻结, int
        TVolumeType MarginTradeVolume #融资买入出数量, int
        TMoneyType MarginTradeAmount #融资买入金额, double
        TVolumeType MarginTradeFrozenVolume #融资买入冻结数量, int
        TMoneyType MarginTradeFrozenAmount #融资买入冻结金额, double
        TMoneyType MarginTradeConversionProfit #融资买入盈亏, double
        TVolumeType ShortSellVolume #融券卖出数量, int
        TMoneyType ShortSellAmount #融券卖出金额, double
        TVolumeType ShortSellFrozenVolume #融券卖出冻结数量, int
        TMoneyType ShortSellFrozenAmount #融券卖出冻结金额, double
        TMoneyType ShortSellConversionProfit #融券卖出盈亏, double
        TMoneyType SSStockValue #融券总市值, double
        TVolumeType TodayMTPosition #今日融资持仓, int
        TVolumeType TodaySSPosition #今日融券持仓, int
        TMoneyType YdOpenCost #历史持仓开仓成本, double
    cdef struct CSyncDepositField "CSecurityFtdcSyncDepositField": #出入金同步
        TDepositSeqNoType DepositSeqNo #出入金流水号, char[15]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TMoneyType Deposit #入金金额, double
        TBoolType IsForce #是否强制进行, int
        TAccountIDType AccountID #账户代, char[15]
    cdef struct CQryExchangeField "CSecurityFtdcQryExchangeField": #查询交易所
        TExchangeIDType ExchangeID #交易所代码, char[9]
    cdef struct CQryProductField "CSecurityFtdcQryProductField": #查询产品
        TInstrumentIDType ProductID #产品代码, char[31]
    cdef struct CQryInstrumentField "CSecurityFtdcQryInstrumentField": #查询合约
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TExchangeInstIDType ExchangeInstID #合约在交易所的代码, char[31]
        TInstrumentIDType ProductID #产品代码, char[31]
    cdef struct CQryBrokerField "CSecurityFtdcQryBrokerField": #查询经纪公司
        TBrokerIDType BrokerID #经纪公司代码, char[11]
    cdef struct CQryPartBrokerField "CSecurityFtdcQryPartBrokerField": #查询经纪公司会员代码
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TParticipantIDType ParticipantID #会员代码, char[11]
    cdef struct CQryInvestorField "CSecurityFtdcQryInvestorField": #查询投资者
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
    cdef struct CQryTradingCodeField "CSecurityFtdcQryTradingCodeField": #查询交易编码
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TClientIDType ClientID #客户代码, char[21]
    cdef struct CQrySuperUserField "CSecurityFtdcQrySuperUserField": #查询管理用户
        TUserIDType UserID #用户代码, char[16]
    cdef struct CQrySuperUserFunctionField "CSecurityFtdcQrySuperUserFunctionField": #查询管理用户功能权限
        TUserIDType UserID #用户代码, char[16]
    cdef struct CQryBrokerUserField "CSecurityFtdcQryBrokerUserField": #查询经纪公司用户
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
    cdef struct CQryBrokerUserFunctionField "CSecurityFtdcQryBrokerUserFunctionField": #查询经纪公司用户权限
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
    cdef struct CQryTradingAccountField "CSecurityFtdcQryTradingAccountField": #查询资金账户
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
    cdef struct CQryLoginForbiddenUserField "CSecurityFtdcQryLoginForbiddenUserField": #查询禁止登录用户
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
    cdef struct CQryDepthMarketDataField "CSecurityFtdcQryDepthMarketDataField": #查询行情
        TInstrumentIDType InstrumentID #合约代码, char[31]
    cdef struct CQryInstrumentTradingRightField "CSecurityFtdcQryInstrumentTradingRightField": #查询合约交易权限
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
    cdef struct CQryInvestorPositionDetailField "CSecurityFtdcQryInvestorPositionDetailField": #查询投资者持仓明细
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
    cdef struct CQryBondInterestField "CSecurityFtdcQryBondInterestField": #查询债券利息
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TInstrumentIDType InstrumentID #合约代码, char[31]
    cdef struct CQryMarketRationInfoField "CSecurityFtdcQryMarketRationInfoField": #查询市值配售信息
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者帐号, char[15]
        TExchangeIDType ExchangeID #交易所代码, char[9]
    cdef struct CQryInstrumentCommissionRateField "CSecurityFtdcQryInstrumentCommissionRateField": #查询合约手续费率
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TDirectionType Direction #买卖方向, char
    cdef struct CQryExcessStockInfoField "CSecurityFtdcQryExcessStockInfoField": #查询余券信息
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TInstrumentIDType InstrumentID #合约代码, char[31]
    cdef struct CQryTraderOfferField "CSecurityFtdcQryTraderOfferField": #查询交易员报盘机
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
    cdef struct CQryMDTraderOfferField "CSecurityFtdcQryMDTraderOfferField": #查询行情报盘机
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TParticipantIDType ParticipantID #会员代码, char[11]
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
    cdef struct CQryFrontStatusField "CSecurityFtdcQryFrontStatusField": #查询前置状态
        TFrontIDType FrontID #前置编号, int
    cdef struct CQryUserSessionField "CSecurityFtdcQryUserSessionField": #查询用户会话
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
    cdef struct CQryOrderField "CSecurityFtdcQryOrderField": #查询报单
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TOrderSysIDType OrderSysID #报单编号, char[21]
        TTimeType InsertTimeStart #开始时间, char[9]
        TTimeType InsertTimeEnd #结束时间, char[9]
    cdef struct CQryOrderActionField "CSecurityFtdcQryOrderActionField": #查询报单操作
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TExchangeIDType ExchangeID #交易所代码, char[9]
    cdef struct CQryErrOrderField "CSecurityFtdcQryErrOrderField": #查询错误报单
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
    cdef struct CQryErrOrderActionField "CSecurityFtdcQryErrOrderActionField": #查询错误报单操作
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
    cdef struct CQryTradeField "CSecurityFtdcQryTradeField": #查询成交
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TTradeIDType TradeID #成交编号, char[21]
        TTimeType TradeTimeStart #开始时间, char[9]
        TTimeType TradeTimeEnd #结束时间, char[9]
    cdef struct CQryInvestorPositionField "CSecurityFtdcQryInvestorPositionField": #查询投资者持仓
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
    cdef struct CQrySyncDepositField "CSecurityFtdcQrySyncDepositField": #查询出入金流水
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TDepositSeqNoType DepositSeqNo #出入金流水号, char[15]
    cdef struct CUserPasswordUpdateField "CSecurityFtdcUserPasswordUpdateField": #用户口令变更
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TPasswordType OldPassword #原来的口令, char[41]
        TPasswordType NewPassword #新的口令, char[41]
    cdef struct CTradingAccountPasswordUpdateField "CSecurityFtdcTradingAccountPasswordUpdateField": #资金账户口令变更域
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TAccountIDType AccountID #投资者帐号, char[15]
        TPasswordType OldPassword #原来的口令, char[41]
        TPasswordType NewPassword #新的口令, char[41]
    cdef struct CManualSyncBrokerUserOTPField "CSecurityFtdcManualSyncBrokerUserOTPField": #手工同步用户动态令牌
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TOTPTypeType OTPType #动态令牌类型, char
        TPasswordType FirstOTP #第一个动态密码, char[41]
        TPasswordType SecondOTP #第二个动态密码, char[41]
    cdef struct CBrokerUserPasswordField "CSecurityFtdcBrokerUserPasswordField": #经纪公司用户口令
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TPasswordType Password #密码, char[41]
    cdef struct CTradingAccountPasswordField "CSecurityFtdcTradingAccountPasswordField": #资金账户口令域
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TAccountIDType AccountID #投资者帐号, char[15]
        TPasswordType Password #密码, char[41]
    cdef struct CUserRightField "CSecurityFtdcUserRightField": #用户权限
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TUserRightTypeType UserRightType #客户权限类型, char
        TBoolType IsForbidden #是否禁止, int
    cdef struct CInvestorAccountField "CSecurityFtdcInvestorAccountField": #投资者账户
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TAccountIDType AccountID #投资者帐号, char[15]
        TBoolType IsDefault #是否主账户, int
        TAccountTypeType AccountType #账户类型, char
        TBoolType IsActive #是否活跃, int
    cdef struct CUserIPField "CSecurityFtdcUserIPField": #用户IP
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TIPAddressType IPAddress #IP地址, char[16]
        TIPAddressType IPMask #IP地址掩码, char[16]
        TMacAddressType MacAddress #Mac地址, char[21]
    cdef struct CBrokerUserOTPParamField "CSecurityFtdcBrokerUserOTPParamField": #用户动态令牌参数
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TOTPVendorsIDType OTPVendorsID #动态令牌提供商, char[2]
        TSerialNumberType SerialNumber #动态令牌序列号, char[17]
        TAuthKeyType AuthKey #令牌密钥, char[41]
        TLastDriftType LastDrift #漂移值, int
        TLastSuccessType LastSuccess #成功值, int
        TOTPTypeType OTPType #动态令牌类型, char
    cdef struct CReqUserLoginField "CSecurityFtdcReqUserLoginField": #用户登录请求
        TDateType TradingDay #交易日, char[9]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TPasswordType Password #密码, char[41]
        TProductInfoType UserProductInfo #用户端产品信息, char[11]
        TProductInfoType InterfaceProductInfo #接口端产品信息, char[11]
        TProtocolInfoType ProtocolInfo #协议信息, char[11]
        TMacAddressType MacAddress #Mac地址, char[21]
        TPasswordType OneTimePassword #动态密码, char[41]
        TIPAddressType ClientIPAddress #终端IP地址, char[16]
        TAuthCodeType AuthCode #客户端认证码, char[17]
    cdef struct CRspUserLoginField "CSecurityFtdcRspUserLoginField": #用户登录应答
        TDateType TradingDay #交易日, char[9]
        TTimeType LoginTime #登录成功时间, char[9]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TSystemNameType SystemName #交易系统名称, char[41]
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TOrderRefType MaxOrderRef #最大报单引用, char[13]
    cdef struct CUserLogoutField "CSecurityFtdcUserLogoutField": #用户登出请求
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
    cdef struct CLogoutAllField "CSecurityFtdcLogoutAllField": #全部登出信息
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TSystemNameType SystemName #系统名称, char[41]
    cdef struct CForceUserLogoutField "CSecurityFtdcForceUserLogoutField": #强制交易员退出
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
    cdef struct CInputOrderField "CSecurityFtdcInputOrderField": #输入报单
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TOrderRefType OrderRef #报单引用, char[13]
        TUserIDType UserID #用户代码, char[16]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TOrderPriceTypeType OrderPriceType #报单价格条件, char
        TDirectionType Direction #买卖方向, char
        TCombOffsetFlagType CombOffsetFlag #组合开平标志, char[5]
        TCombHedgeFlagType CombHedgeFlag #组合投机套保标志, char[5]
        TStockPriceType LimitPrice #价格, char[16]
        TVolumeType VolumeTotalOriginal #数量, int
        TTimeConditionType TimeCondition #有效期类型, char
        TDateType GTDDate #GTD日期, char[9]
        TVolumeConditionType VolumeCondition #成交量类型, char
        TVolumeType MinVolume #最小成交量, int
        TContingentConditionType ContingentCondition #触发条件, char
        TPriceType StopPrice #止损价, double
        TForceCloseReasonType ForceCloseReason #强平原因, char
        TBoolType IsAutoSuspend #自动挂起标志, int
        TBusinessUnitType BusinessUnit #业务单元, char[21]
        TRequestIDType RequestID #请求编号, int
        TBoolType UserForceClose #用户强评标志, int
    cdef struct CInputOrderActionField "CSecurityFtdcInputOrderActionField": #输入报单操作
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TOrderActionRefType OrderActionRef #报单操作引用, int
        TOrderRefType OrderRef #报单引用, char[13]
        TRequestIDType RequestID #请求编号, int
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TActionFlagType ActionFlag #操作标志, char
        TPriceType LimitPrice #价格, double
        TVolumeType VolumeChange #数量变化, int
        TUserIDType UserID #用户代码, char[16]
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TTraderIDType BranchPBU #交易所交易员代码, char[21]
        TOrderLocalIDType OrderLocalID #本地报单编号, char[13]
    cdef struct CSpecificInstrumentField "CSecurityFtdcSpecificInstrumentField": #指定的合约
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TExchangeIDType ExchangeID #交易所代码, char[9]
    cdef struct CSpecificExchangeField "CSecurityFtdcSpecificExchangeField": #指定的交易所
        TExchangeIDType ExchangeID #交易所代码, char[9]
    cdef struct CMarketDataBaseField "CSecurityFtdcMarketDataBaseField": #行情基础属性
        TDateType TradingDay #交易日, char[9]
        TPriceType PreSettlementPrice #上次结算价, double
        TPriceType PreClosePrice #昨收盘, double
        TLargeVolumeType PreOpenInterest #昨持仓量, double
        TRatioType PreDelta #昨虚实度, double
    cdef struct CMarketDataStaticField "CSecurityFtdcMarketDataStaticField": #行情静态属性
        TPriceType OpenPrice #今开盘, double
        TPriceType HighestPrice #最高价, double
        TPriceType LowestPrice #最低价, double
        TPriceType ClosePrice #今收盘, double
        TPriceType UpperLimitPrice #涨停板价, double
        TPriceType LowerLimitPrice #跌停板价, double
        TPriceType SettlementPrice #本次结算价, double
        TRatioType CurrDelta #今虚实度, double
    cdef struct CMarketDataLastMatchField "CSecurityFtdcMarketDataLastMatchField": #行情最新成交属性
        TPriceType LastPrice #最新价, double
        TVolumeType Volume #数量, int
        TMoneyType Turnover #成交金额, double
        TLargeVolumeType OpenInterest #持仓量, double
    cdef struct CMarketDataBestPriceField "CSecurityFtdcMarketDataBestPriceField": #行情最优价属性
        TPriceType BidPrice1 #申买价一, double
        TVolumeType BidVolume1 #申买量一, int
        TPriceType AskPrice1 #申卖价一, double
        TVolumeType AskVolume1 #申卖量一, int
    cdef struct CMarketDataBid23Field "CSecurityFtdcMarketDataBid23Field": #行情申买二、三属性
        TPriceType BidPrice2 #申买价二, double
        TVolumeType BidVolume2 #申买量二, int
        TPriceType BidPrice3 #申买价三, double
        TVolumeType BidVolume3 #申买量三, int
    cdef struct CMarketDataAsk23Field "CSecurityFtdcMarketDataAsk23Field": #行情申卖二、三属性
        TPriceType AskPrice2 #申卖价二, double
        TVolumeType AskVolume2 #申卖量二, int
        TPriceType AskPrice3 #申卖价三, double
        TVolumeType AskVolume3 #申卖量三, int
    cdef struct CMarketDataBid45Field "CSecurityFtdcMarketDataBid45Field": #行情申买四、五属性
        TPriceType BidPrice4 #申买价四, double
        TVolumeType BidVolume4 #申买量四, int
        TPriceType BidPrice5 #申买价五, double
        TVolumeType BidVolume5 #申买量五, int
    cdef struct CMarketDataAsk45Field "CSecurityFtdcMarketDataAsk45Field": #行情申卖四、五属性
        TPriceType AskPrice4 #申卖价四, double
        TVolumeType AskVolume4 #申卖量四, int
        TPriceType AskPrice5 #申卖价五, double
        TVolumeType AskVolume5 #申卖量五, int
    cdef struct CMarketDataUpdateTimeField "CSecurityFtdcMarketDataUpdateTimeField": #行情更新时间属性
        TInstrumentIDType InstrumentID #合约代码, char[31]
        TTimeType UpdateTime #最后修改时间, char[9]
        TMillisecType UpdateMillisec #最后修改毫秒, int
        TDateType ActionDay #业务日期, char[9]
    cdef struct CMarketDataAveragePriceField "CSecurityFtdcMarketDataAveragePriceField": #成交均价
        TPriceType AveragePrice #当日均价, double
    cdef struct CMarketDataExchangeField "CSecurityFtdcMarketDataExchangeField": #行情交易所代码属性
        TExchangeIDType ExchangeID #交易所代码, char[9]
    cdef struct CDisseminationField "CSecurityFtdcDisseminationField": #信息分发
        TSequenceSeriesType SequenceSeries #序列系列号, short
        TSequenceNoType SequenceNo #序列号, int
    cdef struct CInputFundTransferField "CSecurityFtdcInputFundTransferField": #资金转账输入
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TAccountIDType AccountID #投资者资金帐号, char[15]
        TPasswordType Password #资金帐户密码, char[41]
        TUserIDType UserID #用户代码, char[16]
        TTradeAmountType TradeAmount #交易金额, double
        TDigestType Digest #摘要, char[36]
        TAccountTypeType AccountType #账户类型, char
    cdef struct CFundTransferField "CSecurityFtdcFundTransferField": #资金转账
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TInvestorIDType InvestorID #投资者代码, char[15]
        TAccountIDType AccountID #投资者资金帐号, char[15]
        TPasswordType Password #资金帐户密码, char[41]
        TUserIDType UserID #用户代码, char[16]
        TTradeAmountType TradeAmount #交易金额, double
        TDigestType Digest #摘要, char[36]
        TSessionIDType SessionID #会话编号, int
        TLiberSerialType LiberSerial #Liber核心流水号, int
        TPlateSerialType PlateSerial #转账平台流水号, int
        TBankSerialType TransferSerial #第三方流水号, char[13]
        TDateType TradingDay #交易日, char[9]
        TTimeType TradeTime #转账时间, char[9]
        TFundDirectionType FundDirection #出入金方向, char
        TErrorIDType ErrorID #错误代码, int
        TErrorMsgType ErrorMsg #错误信息, char[81]
    cdef struct CQryFundTransferSerialField "CSecurityFtdcQryFundTransferSerialField": #资金转账查询请求
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TAccountIDType AccountID #投资者资金帐号, char[15]
        TAccountTypeType AccountType #账户类型, char
