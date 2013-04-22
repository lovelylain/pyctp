/////////////////////////////////////////////////////////////////////////
///@system 新一代交易所系统
///@company 上海期货信息技术有限公司
///@file ThostFtdcUserApiStruct.h
///@brief 定义了客户端接口使用的业务数据结构
///@history 
///20060106	赵鸿昊		创建该文件
/////////////////////////////////////////////////////////////////////////

#if !defined(SSE_THOST_FTDCSTRUCT_H)
#define SSE_THOST_FTDCSTRUCT_H

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "shfe_stock_ns.h"
#include "ThostFtdcUserApiDataTypeSSE.h"
_SHFE_NS_STOCK_BEGIN_

///信息分发
struct CZQThostFtdcDisseminationField
{
	///序列系列号
	TZQThostFtdcSequenceSeriesType	SequenceSeries;
	///序列号
	TZQThostFtdcSequenceNoType	SequenceNo;
};

///用户登录请求
struct CZQThostFtdcReqUserLoginField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///密码
	TZQThostFtdcPasswordType	Password;
	///用户端产品信息
	TZQThostFtdcProductInfoType	UserProductInfo;
	///接口端产品信息
	TZQThostFtdcProductInfoType	InterfaceProductInfo;
	///协议信息
	TZQThostFtdcProtocolInfoType	ProtocolInfo;
	///Mac地址
	TZQThostFtdcMacAddressType	MacAddress;
	///动态密码
	TZQThostFtdcPasswordType	OneTimePassword;
	///终端IP地址
	TZQThostFtdcIPAddressType	ClientIPAddress;
};

///用户登录应答
struct CZQThostFtdcRspUserLoginField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///登录成功时间
	TZQThostFtdcTimeType	LoginTime;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///交易系统名称
	TZQThostFtdcSystemNameType	SystemName;
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///最大报单引用
	TZQThostFtdcOrderRefType	MaxOrderRef;
	///上期所时间
	TZQThostFtdcTimeType	SHFETime;
	///大商所时间
	TZQThostFtdcTimeType	DCETime;
	///郑商所时间
	TZQThostFtdcTimeType	CZCETime;
	///中金所时间
	TZQThostFtdcTimeType	FFEXTime;
};

///用户登出请求
struct CZQThostFtdcUserLogoutField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
};

///强制交易员退出
struct CZQThostFtdcForceUserLogoutField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
};

///客户端认证请求
struct CZQThostFtdcReqAuthenticateField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///用户端产品信息
	TZQThostFtdcProductInfoType	UserProductInfo;
	///认证码
	TZQThostFtdcAuthCodeType	AuthCode;
};

///客户端认证响应
struct CZQThostFtdcRspAuthenticateField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///用户端产品信息
	TZQThostFtdcProductInfoType	UserProductInfo;
};

///客户端认证信息
struct CZQThostFtdcAuthenticationInfoField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///用户端产品信息
	TZQThostFtdcProductInfoType	UserProductInfo;
	///认证信息
	TZQThostFtdcAuthInfoType	AuthInfo;
	///是否为认证结果
	TZQThostFtdcBoolType	IsResult;
};

///银期转帐报文头
struct CZQThostFtdcTransferHeaderField
{
	///版本号，常量，1.0
	TZQThostFtdcVersionType	Version;
	///交易代码，必填
	TZQThostFtdcTradeCodeType	TradeCode;
	///交易日期，必填，格式：yyyymmdd
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间，必填，格式：hhmmss
	TZQThostFtdcTradeTimeType	TradeTime;
	///发起方流水号，N/A
	TZQThostFtdcTradeSerialType	TradeSerial;
	///期货公司代码，必填
	TZQThostFtdcFutureIDType	FutureID;
	///银行代码，根据查询银行得到，必填
	TZQThostFtdcBankIDType	BankID;
	///银行分中心代码，根据查询银行得到，必填
	TZQThostFtdcBankBrchIDType	BankBrchID;
	///操作员，N/A
	TZQThostFtdcOperNoType	OperNo;
	///交易设备类型，N/A
	TZQThostFtdcDeviceIDType	DeviceID;
	///记录数，N/A
	TZQThostFtdcRecordNumType	RecordNum;
	///会话编号，N/A
	TZQThostFtdcSessionIDType	SessionID;
	///请求编号，N/A
	TZQThostFtdcRequestIDType	RequestID;
};

///银行资金转期货请求，TradeCode=202001
struct CZQThostFtdcTransferBankToFutureReqField
{
	///期货资金账户
	TZQThostFtdcAccountIDType	FutureAccount;
	///密码标志
	TZQThostFtdcFuturePwdFlagType	FuturePwdFlag;
	///密码
	TZQThostFtdcFutureAccPwdType	FutureAccPwd;
	///转账金额
	TZQThostFtdcMoneyType	TradeAmt;
	///客户手续费
	TZQThostFtdcMoneyType	CustFee;
	///币种：RMB-人民币 USD-美圆 HKD-港元
	TZQThostFtdcCurrencyCodeType	CurrencyCode;
};

///银行资金转期货请求响应
struct CZQThostFtdcTransferBankToFutureRspField
{
	///响应代码
	TZQThostFtdcRetCodeType	RetCode;
	///响应信息
	TZQThostFtdcRetInfoType	RetInfo;
	///资金账户
	TZQThostFtdcAccountIDType	FutureAccount;
	///转帐金额
	TZQThostFtdcMoneyType	TradeAmt;
	///应收客户手续费
	TZQThostFtdcMoneyType	CustFee;
	///币种
	TZQThostFtdcCurrencyCodeType	CurrencyCode;
};

///期货资金转银行请求，TradeCode=202002
struct CZQThostFtdcTransferFutureToBankReqField
{
	///期货资金账户
	TZQThostFtdcAccountIDType	FutureAccount;
	///密码标志
	TZQThostFtdcFuturePwdFlagType	FuturePwdFlag;
	///密码
	TZQThostFtdcFutureAccPwdType	FutureAccPwd;
	///转账金额
	TZQThostFtdcMoneyType	TradeAmt;
	///客户手续费
	TZQThostFtdcMoneyType	CustFee;
	///币种：RMB-人民币 USD-美圆 HKD-港元
	TZQThostFtdcCurrencyCodeType	CurrencyCode;
};

///期货资金转银行请求响应
struct CZQThostFtdcTransferFutureToBankRspField
{
	///响应代码
	TZQThostFtdcRetCodeType	RetCode;
	///响应信息
	TZQThostFtdcRetInfoType	RetInfo;
	///资金账户
	TZQThostFtdcAccountIDType	FutureAccount;
	///转帐金额
	TZQThostFtdcMoneyType	TradeAmt;
	///应收客户手续费
	TZQThostFtdcMoneyType	CustFee;
	///币种
	TZQThostFtdcCurrencyCodeType	CurrencyCode;
};

///查询银行资金请求，TradeCode=204002
struct CZQThostFtdcTransferQryBankReqField
{
	///期货资金账户
	TZQThostFtdcAccountIDType	FutureAccount;
	///密码标志
	TZQThostFtdcFuturePwdFlagType	FuturePwdFlag;
	///密码
	TZQThostFtdcFutureAccPwdType	FutureAccPwd;
	///币种：RMB-人民币 USD-美圆 HKD-港元
	TZQThostFtdcCurrencyCodeType	CurrencyCode;
};

///查询银行资金请求响应
struct CZQThostFtdcTransferQryBankRspField
{
	///响应代码
	TZQThostFtdcRetCodeType	RetCode;
	///响应信息
	TZQThostFtdcRetInfoType	RetInfo;
	///资金账户
	TZQThostFtdcAccountIDType	FutureAccount;
	///银行余额
	TZQThostFtdcMoneyType	TradeAmt;
	///银行可用余额
	TZQThostFtdcMoneyType	UseAmt;
	///银行可取余额
	TZQThostFtdcMoneyType	FetchAmt;
	///币种
	TZQThostFtdcCurrencyCodeType	CurrencyCode;
};

///查询银行交易明细请求，TradeCode=204999
struct CZQThostFtdcTransferQryDetailReqField
{
	///期货资金账户
	TZQThostFtdcAccountIDType	FutureAccount;
};

///查询银行交易明细请求响应
struct CZQThostFtdcTransferQryDetailRspField
{
	///交易日期
	TZQThostFtdcDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///交易代码
	TZQThostFtdcTradeCodeType	TradeCode;
	///期货流水号
	TZQThostFtdcTradeSerialNoType	FutureSerial;
	///期货公司代码
	TZQThostFtdcFutureIDType	FutureID;
	///资金帐号
	TZQThostFtdcFutureAccountType	FutureAccount;
	///银行流水号
	TZQThostFtdcTradeSerialNoType	BankSerial;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分中心代码
	TZQThostFtdcBankBrchIDType	BankBrchID;
	///银行账号
	TZQThostFtdcBankAccountType	BankAccount;
	///证件号码
	TZQThostFtdcCertCodeType	CertCode;
	///货币代码
	TZQThostFtdcCurrencyCodeType	CurrencyCode;
	///发生金额
	TZQThostFtdcMoneyType	TxAmount;
	///有效标志
	TZQThostFtdcTransferValidFlagType	Flag;
};

///响应信息
struct CZQThostFtdcRspInfoField
{
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///交易所
struct CZQThostFtdcExchangeField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///交易所名称
	TZQThostFtdcExchangeNameType	ExchangeName;
	///交易所属性
	TZQThostFtdcExchangePropertyType	ExchangeProperty;
};

///产品
struct CZQThostFtdcProductField
{
	///产品代码
	TZQThostFtdcInstrumentIDType	ProductID;
	///产品名称
	TZQThostFtdcProductNameType	ProductName;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///产品类型
	TZQThostFtdcProductClassType	ProductClass;
	///合约数量乘数
	TZQThostFtdcVolumeMultipleType	VolumeMultiple;
	///最小变动价位
	TZQThostFtdcPriceType	PriceTick;
	///市价单最大下单量
	TZQThostFtdcVolumeType	MaxMarketOrderVolume;
	///市价单最小下单量
	TZQThostFtdcVolumeType	MinMarketOrderVolume;
	///限价单最大下单量
	TZQThostFtdcVolumeType	MaxLimitOrderVolume;
	///限价单最小下单量
	TZQThostFtdcVolumeType	MinLimitOrderVolume;
	///持仓类型
	TZQThostFtdcPositionTypeType	PositionType;
	///持仓日期类型
	TZQThostFtdcPositionDateTypeType	PositionDateType;
	///ETF最小交易单位
	TZQThostFtdcVolumeType	EFTMinTradeVolume;
};

///合约
struct CZQThostFtdcInstrumentField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///合约名称
	TZQThostFtdcInstrumentNameType	InstrumentName;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///产品代码
	TZQThostFtdcInstrumentIDType	ProductID;
	///产品类型
	TZQThostFtdcProductClassType	ProductClass;
	///交割年份
	TZQThostFtdcYearType	DeliveryYear;
	///交割月
	TZQThostFtdcMonthType	DeliveryMonth;
	///市价单最大下单量
	TZQThostFtdcVolumeType	MaxMarketOrderVolume;
	///市价单最小下单量
	TZQThostFtdcVolumeType	MinMarketOrderVolume;
	///限价单最大下单量
	TZQThostFtdcVolumeType	MaxLimitOrderVolume;
	///限价单最小下单量
	TZQThostFtdcVolumeType	MinLimitOrderVolume;
	///合约数量乘数
	TZQThostFtdcVolumeMultipleType	VolumeMultiple;
	///最小变动价位
	TZQThostFtdcPriceType	PriceTick;
	///创建日
	TZQThostFtdcDateType	CreateDate;
	///上市日
	TZQThostFtdcDateType	OpenDate;
	///到期日
	TZQThostFtdcDateType	ExpireDate;
	///开始交割日
	TZQThostFtdcDateType	StartDelivDate;
	///结束交割日
	TZQThostFtdcDateType	EndDelivDate;
	///合约生命周期状态
	TZQThostFtdcInstLifePhaseType	InstLifePhase;
	///当前是否交易
	TZQThostFtdcBoolType	IsTrading;
	///持仓类型
	TZQThostFtdcPositionTypeType	PositionType;
	///持仓日期类型
	TZQThostFtdcPositionDateTypeType	PositionDateType;
	///报单能否撤单
	TZQThostFtdcBoolType	OrderCanBeWithdraw;
	///最小买下单单位
	TZQThostFtdcVolumeType	MinBuyVolume;
	///最小卖下单单位
	TZQThostFtdcVolumeType	MinSellVolume;
	///股票权限模版代码
	TZQThostFtdcRightModelIDType	RightModelID;
};

///经纪公司
struct CZQThostFtdcBrokerField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///经纪公司简称
	TZQThostFtdcBrokerAbbrType	BrokerAbbr;
	///经纪公司名称
	TZQThostFtdcBrokerNameType	BrokerName;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
};

///交易所交易员
struct CZQThostFtdcTraderField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///密码
	TZQThostFtdcPasswordType	Password;
	///安装数量
	TZQThostFtdcInstallCountType	InstallCount;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
};

///投资者
struct CZQThostFtdcInvestorField
{
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者分组代码
	TZQThostFtdcInvestorIDType	InvestorGroupID;
	///投资者名称
	TZQThostFtdcPartyNameType	InvestorName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdentifiedCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
	///联系电话
	TZQThostFtdcTelephoneType	Telephone;
	///通讯地址
	TZQThostFtdcAddressType	Address;
	///开户日期
	TZQThostFtdcDateType	OpenDate;
	///手机
	TZQThostFtdcMobileType	Mobile;
	///上海营业部编号
	TZQThostFtdcBranchIDType	SHBranchID;
	///深圳营业部编号
	TZQThostFtdcBranchIDType	SZBranchID;
	///是否信用账户
	TZQThostFtdcBoolType	IsCreditAccount;
};

///交易编码
struct CZQThostFtdcTradingCodeField
{
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
};

///会员编码和经纪公司编码对照表
struct CZQThostFtdcPartBrokerField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
};

///管理用户
struct CZQThostFtdcSuperUserField
{
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///用户名称
	TZQThostFtdcUserNameType	UserName;
	///密码
	TZQThostFtdcPasswordType	Password;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
};

///管理用户功能权限
struct CZQThostFtdcSuperUserFunctionField
{
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///功能代码
	TZQThostFtdcFunctionCodeType	FunctionCode;
};

///投资者组
struct CZQThostFtdcInvestorGroupField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者分组代码
	TZQThostFtdcInvestorIDType	InvestorGroupID;
	///投资者分组名称
	TZQThostFtdcInvestorGroupNameType	InvestorGroupName;
};

///资金账户
struct CZQThostFtdcTradingAccountField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///上次质押金额
	TZQThostFtdcMoneyType	PreMortgage;
	///上次信用额度
	TZQThostFtdcMoneyType	PreCredit;
	///上次存款额
	TZQThostFtdcMoneyType	PreDeposit;
	///上次结算准备金
	TZQThostFtdcMoneyType	PreBalance;
	///上次占用的保证金
	TZQThostFtdcMoneyType	PreMargin;
	///利息基数
	TZQThostFtdcMoneyType	InterestBase;
	///利息收入
	TZQThostFtdcMoneyType	Interest;
	///入金金额
	TZQThostFtdcMoneyType	Deposit;
	///出金金额
	TZQThostFtdcMoneyType	Withdraw;
	///冻结的保证金
	TZQThostFtdcMoneyType	FrozenMargin;
	///冻结的资金
	TZQThostFtdcMoneyType	FrozenCash;
	///冻结的手续费
	TZQThostFtdcMoneyType	FrozenCommission;
	///当前保证金总额
	TZQThostFtdcMoneyType	CurrMargin;
	///资金差额
	TZQThostFtdcMoneyType	CashIn;
	///手续费
	TZQThostFtdcMoneyType	Commission;
	///融券持仓盈亏
	TZQThostFtdcMoneyType	CloseProfit;
	///融资持仓盈亏
	TZQThostFtdcMoneyType	PositionProfit;
	///期货结算准备金
	TZQThostFtdcMoneyType	Balance;
	///现金
	TZQThostFtdcMoneyType	Available;
	///可取资金
	TZQThostFtdcMoneyType	WithdrawQuota;
	///基本准备金
	TZQThostFtdcMoneyType	Reserve;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///保证金可用余额
	TZQThostFtdcMoneyType	Credit;
	///质押金额
	TZQThostFtdcMoneyType	Mortgage;
	///交易所保证金
	TZQThostFtdcMoneyType	ExchangeMargin;
	///投资者交割保证金
	TZQThostFtdcMoneyType	DeliveryMargin;
	///交易所交割保证金
	TZQThostFtdcMoneyType	ExchangeDeliveryMargin;
	///冻结的过户费
	TZQThostFtdcMoneyType	FrozenTransferFee;
	///冻结的印花税
	TZQThostFtdcMoneyType	FrozenStampTax;
	///过户费
	TZQThostFtdcMoneyType	TransferFee;
	///印花税
	TZQThostFtdcMoneyType	StampTax;
	///折算金额
	TZQThostFtdcMoneyType	ConversionAmount;
	///授信额度
	TZQThostFtdcMoneyType	CreditAmount;
	///最低维持担保比例
	TZQThostFtdcRatioType	LowLimitRatio;
	///融资买入金额
	TZQThostFtdcMoneyType	MarginTradingAmount;
	///融券卖出金额
	TZQThostFtdcMoneyType	ShortSellingAmount;
	///融资买入可用金额
	TZQThostFtdcMoneyType	MarginTradingAvail;
	///融券卖出可用金额
	TZQThostFtdcMoneyType	ShortSellingAvail;
	///维持担保比例
	TZQThostFtdcRatioType	CreditRatio;
	///证券总价值
	TZQThostFtdcMoneyType	StockValue;
	///融券总市值
	TZQThostFtdcMoneyType	SSStockValue;
	///国债回购占用资金
	TZQThostFtdcMoneyType	BondRepurchaseValue;
};

///投资者持仓
struct CZQThostFtdcInvestorPositionField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///持仓多空方向
	TZQThostFtdcPosiDirectionType	PosiDirection;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///持仓日期
	TZQThostFtdcPositionDateType	PositionDate;
	///上日持仓
	TZQThostFtdcVolumeType	YdPosition;
	///今日持仓
	TZQThostFtdcVolumeType	Position;
	///多头冻结
	TZQThostFtdcVolumeType	LongFrozen;
	///空头冻结
	TZQThostFtdcVolumeType	ShortFrozen;
	///开仓冻结金额
	TZQThostFtdcMoneyType	LongFrozenAmount;
	///开仓冻结金额
	TZQThostFtdcMoneyType	ShortFrozenAmount;
	///开仓量
	TZQThostFtdcVolumeType	OpenVolume;
	///平仓量
	TZQThostFtdcVolumeType	CloseVolume;
	///开仓金额
	TZQThostFtdcMoneyType	OpenAmount;
	///平仓金额
	TZQThostFtdcMoneyType	CloseAmount;
	///持仓成本
	TZQThostFtdcMoneyType	PositionCost;
	///冻结的资金
	TZQThostFtdcMoneyType	FrozenCash;
	///资金差额
	TZQThostFtdcMoneyType	CashIn;
	///手续费
	TZQThostFtdcMoneyType	Commission;
	///平仓盈亏
	TZQThostFtdcMoneyType	CloseProfit;
	///持仓盈亏
	TZQThostFtdcMoneyType	PositionProfit;
	///上次结算价
	TZQThostFtdcPriceType	PreSettlementPrice;
	///本次结算价
	TZQThostFtdcPriceType	SettlementPrice;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///开仓成本
	TZQThostFtdcMoneyType	OpenCost;
	///交易所保证金
	TZQThostFtdcMoneyType	ExchangeMargin;
	///今日持仓
	TZQThostFtdcVolumeType	TodayPosition;
	///过户费
	TZQThostFtdcMoneyType	TransferFee;
	///印花税
	TZQThostFtdcMoneyType	StampTax;
	///今日申购赎回数量
	TZQThostFtdcVolumeType	TodayPurRedVolume;
	///折算率
	TZQThostFtdcRatioType	ConversionRate;
	///折算金额
	TZQThostFtdcMoneyType	ConversionAmount;
	///融资买入出数量
	TZQThostFtdcVolumeType	MarginTradeVolume;
	///融资买入金额
	TZQThostFtdcMoneyType	MarginTradeAmount;
	///融资买入冻结数量
	TZQThostFtdcVolumeType	MarginTradeFrozenVolume;
	///融资买入冻结金额
	TZQThostFtdcMoneyType	MarginTradeFrozenAmount;
	///融资买入盈亏
	TZQThostFtdcMoneyType	MarginTradeConversionAmount;
	///融券卖出数量
	TZQThostFtdcVolumeType	ShortSellVolume;
	///融券卖出金额
	TZQThostFtdcMoneyType	ShortSellAmount;
	///融券卖出盈亏
	TZQThostFtdcMoneyType	ShortSellConversionAmount;
	///融券卖出冻结数量
	TZQThostFtdcVolumeType	ShortSellFrozenVolume;
	///融券卖出冻结金额
	TZQThostFtdcMoneyType	ShortSellFrozenAmount;
	///证券价值
	TZQThostFtdcMoneyType	StockValue;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///今日融资持仓
	TZQThostFtdcVolumeType	TodayMTPosition;
	///今日融券持仓
	TZQThostFtdcVolumeType	TodaySSPosition;
	///融券总市值
	TZQThostFtdcMoneyType	SSStockValue;
};

///合约保证金率
struct CZQThostFtdcInstrumentMarginRateField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///多头保证金率
	TZQThostFtdcRatioType	LongMarginRatioByMoney;
	///多头保证金费
	TZQThostFtdcMoneyType	LongMarginRatioByVolume;
	///空头保证金率
	TZQThostFtdcRatioType	ShortMarginRatioByMoney;
	///空头保证金费
	TZQThostFtdcMoneyType	ShortMarginRatioByVolume;
	///是否相对交易所收取
	TZQThostFtdcBoolType	IsRelative;
};

///合约手续费率
struct CZQThostFtdcInstrumentCommissionRateField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///印花税率
	TZQThostFtdcRatioType	StampTaxRateByMoney;
	///印花税率(按手数)
	TZQThostFtdcRatioType	StampTaxRateByVolume;
	///过户费率
	TZQThostFtdcRatioType	TransferFeeRateByMoney;
	///过户费率(按手数)
	TZQThostFtdcRatioType	TransferFeeRateByVolume;
	///交易费
	TZQThostFtdcRatioType	TradeFeeByMoney;
	///交易费(按手数)
	TZQThostFtdcRatioType	TradeFeeByVolume;
	///交易附加费率
	TZQThostFtdcRatioType	MarginByMoney;
	///最小过户费
	TZQThostFtdcPriceType	MinTradeFee;
};

///深度行情
struct CZQThostFtdcDepthMarketDataField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///最新价
	TZQThostFtdcPriceType	LastPrice;
	///上次结算价
	TZQThostFtdcPriceType	PreSettlementPrice;
	///昨收盘
	TZQThostFtdcPriceType	PreClosePrice;
	///昨持仓量
	TZQThostFtdcLargeVolumeType	PreOpenInterest;
	///今开盘
	TZQThostFtdcPriceType	OpenPrice;
	///最高价
	TZQThostFtdcPriceType	HighestPrice;
	///最低价
	TZQThostFtdcPriceType	LowestPrice;
	///数量
	TZQThostFtdcVolumeType	Volume;
	///成交金额
	TZQThostFtdcMoneyType	Turnover;
	///持仓量
	TZQThostFtdcLargeVolumeType	OpenInterest;
	///今收盘
	TZQThostFtdcPriceType	ClosePrice;
	///本次结算价
	TZQThostFtdcPriceType	SettlementPrice;
	///涨停板价
	TZQThostFtdcPriceType	UpperLimitPrice;
	///跌停板价
	TZQThostFtdcPriceType	LowerLimitPrice;
	///昨虚实度
	TZQThostFtdcRatioType	PreDelta;
	///今虚实度
	TZQThostFtdcRatioType	CurrDelta;
	///最后修改时间
	TZQThostFtdcTimeType	UpdateTime;
	///最后修改毫秒
	TZQThostFtdcMillisecType	UpdateMillisec;
	///申买价一
	TZQThostFtdcPriceType	BidPrice1;
	///申买量一
	TZQThostFtdcVolumeType	BidVolume1;
	///申卖价一
	TZQThostFtdcPriceType	AskPrice1;
	///申卖量一
	TZQThostFtdcVolumeType	AskVolume1;
	///申买价二
	TZQThostFtdcPriceType	BidPrice2;
	///申买量二
	TZQThostFtdcVolumeType	BidVolume2;
	///申卖价二
	TZQThostFtdcPriceType	AskPrice2;
	///申卖量二
	TZQThostFtdcVolumeType	AskVolume2;
	///申买价三
	TZQThostFtdcPriceType	BidPrice3;
	///申买量三
	TZQThostFtdcVolumeType	BidVolume3;
	///申卖价三
	TZQThostFtdcPriceType	AskPrice3;
	///申卖量三
	TZQThostFtdcVolumeType	AskVolume3;
	///申买价四
	TZQThostFtdcPriceType	BidPrice4;
	///申买量四
	TZQThostFtdcVolumeType	BidVolume4;
	///申卖价四
	TZQThostFtdcPriceType	AskPrice4;
	///申卖量四
	TZQThostFtdcVolumeType	AskVolume4;
	///申买价五
	TZQThostFtdcPriceType	BidPrice5;
	///申买量五
	TZQThostFtdcVolumeType	BidVolume5;
	///申卖价五
	TZQThostFtdcPriceType	AskPrice5;
	///申卖量五
	TZQThostFtdcVolumeType	AskVolume5;
	///当日均价
	TZQThostFtdcPriceType	AveragePrice;
};

///投资者合约交易权限
struct CZQThostFtdcInstrumentTradingRightField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///买卖
	TZQThostFtdcDirectionType	Direction;
	///交易权限
	TZQThostFtdcTradingRightType	TradingRight;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///股票权限分类
	TZQThostFtdcInstrumentRangeType	InstrumentRange;
};

///经纪公司用户
struct CZQThostFtdcBrokerUserField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///用户名称
	TZQThostFtdcUserNameType	UserName;
	///用户类型
	TZQThostFtdcUserTypeType	UserType;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
	///是否使用令牌
	TZQThostFtdcBoolType	IsUsingOTP;
};

///经纪公司用户口令
struct CZQThostFtdcBrokerUserPasswordField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///密码
	TZQThostFtdcPasswordType	Password;
};

///经纪公司用户功能权限
struct CZQThostFtdcBrokerUserFunctionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///经纪公司功能代码
	TZQThostFtdcBrokerFunctionCodeType	BrokerFunctionCode;
};

///交易所交易员报盘机
struct CZQThostFtdcTraderOfferField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///密码
	TZQThostFtdcPasswordType	Password;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///交易所交易员连接状态
	TZQThostFtdcTraderConnectStatusType	TraderConnectStatus;
	///发出连接请求的日期
	TZQThostFtdcDateType	ConnectRequestDate;
	///发出连接请求的时间
	TZQThostFtdcTimeType	ConnectRequestTime;
	///上次报告日期
	TZQThostFtdcDateType	LastReportDate;
	///上次报告时间
	TZQThostFtdcTimeType	LastReportTime;
	///完成连接日期
	TZQThostFtdcDateType	ConnectDate;
	///完成连接时间
	TZQThostFtdcTimeType	ConnectTime;
	///启动日期
	TZQThostFtdcDateType	StartDate;
	///启动时间
	TZQThostFtdcTimeType	StartTime;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
};

///投资者结算结果
struct CZQThostFtdcSettlementInfoField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///序号
	TZQThostFtdcSequenceNoType	SequenceNo;
	///消息正文
	TZQThostFtdcContentType	Content;
};

///合约保证金率调整
struct CZQThostFtdcInstrumentMarginRateAdjustField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///多头保证金率
	TZQThostFtdcRatioType	LongMarginRatioByMoney;
	///多头保证金费
	TZQThostFtdcMoneyType	LongMarginRatioByVolume;
	///空头保证金率
	TZQThostFtdcRatioType	ShortMarginRatioByMoney;
	///空头保证金费
	TZQThostFtdcMoneyType	ShortMarginRatioByVolume;
	///是否相对交易所收取
	TZQThostFtdcBoolType	IsRelative;
};

///交易所保证金率
struct CZQThostFtdcExchangeMarginRateField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///多头保证金率
	TZQThostFtdcRatioType	LongMarginRatioByMoney;
	///多头保证金费
	TZQThostFtdcMoneyType	LongMarginRatioByVolume;
	///空头保证金率
	TZQThostFtdcRatioType	ShortMarginRatioByMoney;
	///空头保证金费
	TZQThostFtdcMoneyType	ShortMarginRatioByVolume;
};

///交易所保证金率调整
struct CZQThostFtdcExchangeMarginRateAdjustField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///跟随交易所投资者多头保证金率
	TZQThostFtdcRatioType	LongMarginRatioByMoney;
	///跟随交易所投资者多头保证金费
	TZQThostFtdcMoneyType	LongMarginRatioByVolume;
	///跟随交易所投资者空头保证金率
	TZQThostFtdcRatioType	ShortMarginRatioByMoney;
	///跟随交易所投资者空头保证金费
	TZQThostFtdcMoneyType	ShortMarginRatioByVolume;
	///交易所多头保证金率
	TZQThostFtdcRatioType	ExchLongMarginRatioByMoney;
	///交易所多头保证金费
	TZQThostFtdcMoneyType	ExchLongMarginRatioByVolume;
	///交易所空头保证金率
	TZQThostFtdcRatioType	ExchShortMarginRatioByMoney;
	///交易所空头保证金费
	TZQThostFtdcMoneyType	ExchShortMarginRatioByVolume;
	///不跟随交易所投资者多头保证金率
	TZQThostFtdcRatioType	NoLongMarginRatioByMoney;
	///不跟随交易所投资者多头保证金费
	TZQThostFtdcMoneyType	NoLongMarginRatioByVolume;
	///不跟随交易所投资者空头保证金率
	TZQThostFtdcRatioType	NoShortMarginRatioByMoney;
	///不跟随交易所投资者空头保证金费
	TZQThostFtdcMoneyType	NoShortMarginRatioByVolume;
};

///结算引用
struct CZQThostFtdcSettlementRefField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
};

///当前时间
struct CZQThostFtdcCurrentTimeField
{
	///当前日期
	TZQThostFtdcDateType	CurrDate;
	///当前时间
	TZQThostFtdcTimeType	CurrTime;
	///当前时间（毫秒）
	TZQThostFtdcMillisecType	CurrMillisec;
};

///通讯阶段
struct CZQThostFtdcCommPhaseField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///通讯时段编号
	TZQThostFtdcCommPhaseNoType	CommPhaseNo;
};

///登录信息
struct CZQThostFtdcLoginInfoField
{
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///登录日期
	TZQThostFtdcDateType	LoginDate;
	///登录时间
	TZQThostFtdcTimeType	LoginTime;
	///IP地址
	TZQThostFtdcIPAddressType	IPAddress;
	///用户端产品信息
	TZQThostFtdcProductInfoType	UserProductInfo;
	///接口端产品信息
	TZQThostFtdcProductInfoType	InterfaceProductInfo;
	///协议信息
	TZQThostFtdcProtocolInfoType	ProtocolInfo;
	///系统名称
	TZQThostFtdcSystemNameType	SystemName;
	///密码
	TZQThostFtdcPasswordType	Password;
	///最大报单引用
	TZQThostFtdcOrderRefType	MaxOrderRef;
	///Mac地址
	TZQThostFtdcMacAddressType	MacAddress;
	///动态密码
	TZQThostFtdcPasswordType	OneTimePassword;
};

///登录信息
struct CZQThostFtdcLogoutAllField
{
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///系统名称
	TZQThostFtdcSystemNameType	SystemName;
};

///前置状态
struct CZQThostFtdcFrontStatusField
{
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///上次报告日期
	TZQThostFtdcDateType	LastReportDate;
	///上次报告时间
	TZQThostFtdcTimeType	LastReportTime;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
};

///用户口令变更
struct CZQThostFtdcUserPasswordUpdateField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///原来的口令
	TZQThostFtdcPasswordType	OldPassword;
	///新的口令
	TZQThostFtdcPasswordType	NewPassword;
};

///输入报单
struct CZQThostFtdcInputOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单价格条件
	TZQThostFtdcOrderPriceTypeType	OrderPriceType;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///组合开平标志
	TZQThostFtdcCombOffsetFlagType	CombOffsetFlag;
	///组合投机套保标志
	TZQThostFtdcCombHedgeFlagType	CombHedgeFlag;
	///价格
	TZQThostFtdcStockPriceType	LimitPrice;
	///数量
	TZQThostFtdcVolumeType	VolumeTotalOriginal;
	///有效期类型
	TZQThostFtdcTimeConditionType	TimeCondition;
	///GTD日期
	TZQThostFtdcDateType	GTDDate;
	///成交量类型
	TZQThostFtdcVolumeConditionType	VolumeCondition;
	///最小成交量
	TZQThostFtdcVolumeType	MinVolume;
	///触发条件
	TZQThostFtdcContingentConditionType	ContingentCondition;
	///止损价
	TZQThostFtdcPriceType	StopPrice;
	///强平原因
	TZQThostFtdcForceCloseReasonType	ForceCloseReason;
	///自动挂起标志
	TZQThostFtdcBoolType	IsAutoSuspend;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///用户强评标志
	TZQThostFtdcBoolType	UserForceClose;
};

///报单
struct CZQThostFtdcOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单价格条件
	TZQThostFtdcOrderPriceTypeType	OrderPriceType;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///组合开平标志
	TZQThostFtdcCombOffsetFlagType	CombOffsetFlag;
	///组合投机套保标志
	TZQThostFtdcCombHedgeFlagType	CombHedgeFlag;
	///价格
	TZQThostFtdcStockPriceType	LimitPrice;
	///数量
	TZQThostFtdcVolumeType	VolumeTotalOriginal;
	///有效期类型
	TZQThostFtdcTimeConditionType	TimeCondition;
	///GTD日期
	TZQThostFtdcDateType	GTDDate;
	///成交量类型
	TZQThostFtdcVolumeConditionType	VolumeCondition;
	///最小成交量
	TZQThostFtdcVolumeType	MinVolume;
	///触发条件
	TZQThostFtdcContingentConditionType	ContingentCondition;
	///止损价
	TZQThostFtdcPriceType	StopPrice;
	///强平原因
	TZQThostFtdcForceCloseReasonType	ForceCloseReason;
	///自动挂起标志
	TZQThostFtdcBoolType	IsAutoSuspend;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///报单提交状态
	TZQThostFtdcOrderSubmitStatusType	OrderSubmitStatus;
	///报单提示序号
	TZQThostFtdcSequenceNoType	NotifySequence;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///报单编号
	TZQThostFtdcOrderSysIDType	OrderSysID;
	///报单来源
	TZQThostFtdcOrderSourceType	OrderSource;
	///报单状态
	TZQThostFtdcOrderStatusType	OrderStatus;
	///报单类型
	TZQThostFtdcOrderTypeType	OrderType;
	///今成交数量
	TZQThostFtdcVolumeType	VolumeTraded;
	///剩余数量
	TZQThostFtdcVolumeType	VolumeTotal;
	///报单日期
	TZQThostFtdcDateType	InsertDate;
	///委托时间
	TZQThostFtdcTimeType	InsertTime;
	///激活时间
	TZQThostFtdcTimeType	ActiveTime;
	///挂起时间
	TZQThostFtdcTimeType	SuspendTime;
	///最后修改时间
	TZQThostFtdcTimeType	UpdateTime;
	///撤销时间
	TZQThostFtdcTimeType	CancelTime;
	///最后修改交易所交易员代码
	TZQThostFtdcTraderIDType	ActiveTraderID;
	///结算会员编号
	TZQThostFtdcParticipantIDType	ClearingPartID;
	///序号
	TZQThostFtdcSequenceNoType	SequenceNo;
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///用户端产品信息
	TZQThostFtdcProductInfoType	UserProductInfo;
	///状态信息
	TZQThostFtdcErrorMsgType	StatusMsg;
	///用户强评标志
	TZQThostFtdcBoolType	UserForceClose;
	///操作用户代码
	TZQThostFtdcUserIDType	ActiveUserID;
	///经纪公司报单编号
	TZQThostFtdcSequenceNoType	BrokerOrderSeq;
	///相关报单
	TZQThostFtdcOrderSysIDType	RelativeOrderSysID;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
	///成交数量
	TZQThostFtdcMoneyType	TradeAmount;
	///是否ETF
	TZQThostFtdcBoolType	IsETF;
	///资金帐号
	TZQThostFtdcAccountIDType	AccountID;
};

///交易所报单
struct CZQThostFtdcExchangeOrderField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单价格条件
	TZQThostFtdcOrderPriceTypeType	OrderPriceType;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///组合开平标志
	TZQThostFtdcCombOffsetFlagType	CombOffsetFlag;
	///组合投机套保标志
	TZQThostFtdcCombHedgeFlagType	CombHedgeFlag;
	///价格
	TZQThostFtdcStockPriceType	LimitPrice;
	///数量
	TZQThostFtdcVolumeType	VolumeTotalOriginal;
	///有效期类型
	TZQThostFtdcTimeConditionType	TimeCondition;
	///GTD日期
	TZQThostFtdcDateType	GTDDate;
	///成交量类型
	TZQThostFtdcVolumeConditionType	VolumeCondition;
	///最小成交量
	TZQThostFtdcVolumeType	MinVolume;
	///触发条件
	TZQThostFtdcContingentConditionType	ContingentCondition;
	///止损价
	TZQThostFtdcPriceType	StopPrice;
	///强平原因
	TZQThostFtdcForceCloseReasonType	ForceCloseReason;
	///自动挂起标志
	TZQThostFtdcBoolType	IsAutoSuspend;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///报单提交状态
	TZQThostFtdcOrderSubmitStatusType	OrderSubmitStatus;
	///报单提示序号
	TZQThostFtdcSequenceNoType	NotifySequence;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///报单编号
	TZQThostFtdcOrderSysIDType	OrderSysID;
	///报单来源
	TZQThostFtdcOrderSourceType	OrderSource;
	///报单状态
	TZQThostFtdcOrderStatusType	OrderStatus;
	///报单类型
	TZQThostFtdcOrderTypeType	OrderType;
	///今成交数量
	TZQThostFtdcVolumeType	VolumeTraded;
	///剩余数量
	TZQThostFtdcVolumeType	VolumeTotal;
	///报单日期
	TZQThostFtdcDateType	InsertDate;
	///委托时间
	TZQThostFtdcTimeType	InsertTime;
	///激活时间
	TZQThostFtdcTimeType	ActiveTime;
	///挂起时间
	TZQThostFtdcTimeType	SuspendTime;
	///最后修改时间
	TZQThostFtdcTimeType	UpdateTime;
	///撤销时间
	TZQThostFtdcTimeType	CancelTime;
	///最后修改交易所交易员代码
	TZQThostFtdcTraderIDType	ActiveTraderID;
	///结算会员编号
	TZQThostFtdcParticipantIDType	ClearingPartID;
	///序号
	TZQThostFtdcSequenceNoType	SequenceNo;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
};

///交易所报单插入失败
struct CZQThostFtdcExchangeOrderInsertErrorField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///输入报单操作
struct CZQThostFtdcInputOrderActionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///报单操作引用
	TZQThostFtdcOrderActionRefType	OrderActionRef;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///操作标志
	TZQThostFtdcActionFlagType	ActionFlag;
	///价格
	TZQThostFtdcPriceType	LimitPrice;
	///数量变化
	TZQThostFtdcVolumeType	VolumeChange;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
};

///报单操作
struct CZQThostFtdcOrderActionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///报单操作引用
	TZQThostFtdcOrderActionRefType	OrderActionRef;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///操作标志
	TZQThostFtdcActionFlagType	ActionFlag;
	///价格
	TZQThostFtdcPriceType	LimitPrice;
	///数量变化
	TZQThostFtdcVolumeType	VolumeChange;
	///操作日期
	TZQThostFtdcDateType	ActionDate;
	///操作时间
	TZQThostFtdcTimeType	ActionTime;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///操作本地编号
	TZQThostFtdcOrderLocalIDType	ActionLocalID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///报单操作状态
	TZQThostFtdcOrderActionStatusType	OrderActionStatus;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
	///状态信息
	TZQThostFtdcErrorMsgType	StatusMsg;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
};

///交易所报单操作
struct CZQThostFtdcExchangeOrderActionField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///操作标志
	TZQThostFtdcActionFlagType	ActionFlag;
	///价格
	TZQThostFtdcPriceType	LimitPrice;
	///数量变化
	TZQThostFtdcVolumeType	VolumeChange;
	///操作日期
	TZQThostFtdcDateType	ActionDate;
	///操作时间
	TZQThostFtdcTimeType	ActionTime;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///操作本地编号
	TZQThostFtdcOrderLocalIDType	ActionLocalID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///报单操作状态
	TZQThostFtdcOrderActionStatusType	OrderActionStatus;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
};

///交易所报单操作失败
struct CZQThostFtdcExchangeOrderActionErrorField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单编号
	TZQThostFtdcOrderSysIDType	OrderSysID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///操作本地编号
	TZQThostFtdcOrderLocalIDType	ActionLocalID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///交易所成交
struct CZQThostFtdcExchangeTradeField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///成交编号
	TZQThostFtdcTradeIDType	TradeID;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///报单编号
	TZQThostFtdcOrderSysIDType	OrderSysID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///交易角色
	TZQThostFtdcTradingRoleType	TradingRole;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///开平标志
	TZQThostFtdcOffsetFlagType	OffsetFlag;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///价格
	TZQThostFtdcStockPriceType	Price;
	///数量
	TZQThostFtdcVolumeType	Volume;
	///成交时期
	TZQThostFtdcDateType	TradeDate;
	///成交时间
	TZQThostFtdcTimeType	TradeTime;
	///成交类型
	TZQThostFtdcTradeTypeType	TradeType;
	///成交价来源
	TZQThostFtdcPriceSourceType	PriceSource;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///结算会员编号
	TZQThostFtdcParticipantIDType	ClearingPartID;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///序号
	TZQThostFtdcSequenceNoType	SequenceNo;
};

///成交
struct CZQThostFtdcTradeField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///成交编号
	TZQThostFtdcTradeIDType	TradeID;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///报单编号
	TZQThostFtdcOrderSysIDType	OrderSysID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///交易角色
	TZQThostFtdcTradingRoleType	TradingRole;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///开平标志
	TZQThostFtdcOffsetFlagType	OffsetFlag;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///价格
	TZQThostFtdcStockPriceType	Price;
	///数量
	TZQThostFtdcVolumeType	Volume;
	///成交时期
	TZQThostFtdcDateType	TradeDate;
	///成交时间
	TZQThostFtdcTimeType	TradeTime;
	///成交类型
	TZQThostFtdcTradeTypeType	TradeType;
	///成交价来源
	TZQThostFtdcPriceSourceType	PriceSource;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///结算会员编号
	TZQThostFtdcParticipantIDType	ClearingPartID;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///序号
	TZQThostFtdcSequenceNoType	SequenceNo;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///经纪公司报单编号
	TZQThostFtdcSequenceNoType	BrokerOrderSeq;
};

///用户会话
struct CZQThostFtdcUserSessionField
{
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///登录日期
	TZQThostFtdcDateType	LoginDate;
	///登录时间
	TZQThostFtdcTimeType	LoginTime;
	///IP地址
	TZQThostFtdcIPAddressType	IPAddress;
	///用户端产品信息
	TZQThostFtdcProductInfoType	UserProductInfo;
	///接口端产品信息
	TZQThostFtdcProductInfoType	InterfaceProductInfo;
	///协议信息
	TZQThostFtdcProtocolInfoType	ProtocolInfo;
	///Mac地址
	TZQThostFtdcMacAddressType	MacAddress;
};

///查询最大报单数量
struct CZQThostFtdcQueryMaxOrderVolumeField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///开平标志
	TZQThostFtdcOffsetFlagType	OffsetFlag;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///最大允许报单数量
	TZQThostFtdcVolumeType	MaxVolume;
};

///投资者结算结果确认信息
struct CZQThostFtdcSettlementInfoConfirmField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///确认日期
	TZQThostFtdcDateType	ConfirmDate;
	///确认时间
	TZQThostFtdcTimeType	ConfirmTime;
};

///出入金同步
struct CZQThostFtdcSyncDepositField
{
	///出入金流水号
	TZQThostFtdcDepositSeqNoType	DepositSeqNo;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///入金金额
	TZQThostFtdcMoneyType	Deposit;
	///是否强制进行
	TZQThostFtdcBoolType	IsForce;
};

///经纪公司同步
struct CZQThostFtdcBrokerSyncField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
};

///正在同步中的投资者
struct CZQThostFtdcSyncingInvestorField
{
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者分组代码
	TZQThostFtdcInvestorIDType	InvestorGroupID;
	///投资者名称
	TZQThostFtdcPartyNameType	InvestorName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdentifiedCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
	///联系电话
	TZQThostFtdcTelephoneType	Telephone;
	///通讯地址
	TZQThostFtdcAddressType	Address;
	///开户日期
	TZQThostFtdcDateType	OpenDate;
	///手机
	TZQThostFtdcMobileType	Mobile;
	///上海营业部编号
	TZQThostFtdcBranchIDType	SHBranchID;
	///深圳营业部编号
	TZQThostFtdcBranchIDType	SZBranchID;
	///是否信用账户
	TZQThostFtdcBoolType	IsCreditAccount;
};

///正在同步中的交易代码
struct CZQThostFtdcSyncingTradingCodeField
{
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
};

///正在同步中的投资者分组
struct CZQThostFtdcSyncingInvestorGroupField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者分组代码
	TZQThostFtdcInvestorIDType	InvestorGroupID;
	///投资者分组名称
	TZQThostFtdcInvestorGroupNameType	InvestorGroupName;
};

///正在同步中的交易账号
struct CZQThostFtdcSyncingTradingAccountField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///上次质押金额
	TZQThostFtdcMoneyType	PreMortgage;
	///上次信用额度
	TZQThostFtdcMoneyType	PreCredit;
	///上次存款额
	TZQThostFtdcMoneyType	PreDeposit;
	///上次结算准备金
	TZQThostFtdcMoneyType	PreBalance;
	///上次占用的保证金
	TZQThostFtdcMoneyType	PreMargin;
	///利息基数
	TZQThostFtdcMoneyType	InterestBase;
	///利息收入
	TZQThostFtdcMoneyType	Interest;
	///入金金额
	TZQThostFtdcMoneyType	Deposit;
	///出金金额
	TZQThostFtdcMoneyType	Withdraw;
	///冻结的保证金
	TZQThostFtdcMoneyType	FrozenMargin;
	///冻结的资金
	TZQThostFtdcMoneyType	FrozenCash;
	///冻结的手续费
	TZQThostFtdcMoneyType	FrozenCommission;
	///当前保证金总额
	TZQThostFtdcMoneyType	CurrMargin;
	///资金差额
	TZQThostFtdcMoneyType	CashIn;
	///手续费
	TZQThostFtdcMoneyType	Commission;
	///融券持仓盈亏
	TZQThostFtdcMoneyType	CloseProfit;
	///融资持仓盈亏
	TZQThostFtdcMoneyType	PositionProfit;
	///期货结算准备金
	TZQThostFtdcMoneyType	Balance;
	///现金
	TZQThostFtdcMoneyType	Available;
	///可取资金
	TZQThostFtdcMoneyType	WithdrawQuota;
	///基本准备金
	TZQThostFtdcMoneyType	Reserve;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///保证金可用余额
	TZQThostFtdcMoneyType	Credit;
	///质押金额
	TZQThostFtdcMoneyType	Mortgage;
	///交易所保证金
	TZQThostFtdcMoneyType	ExchangeMargin;
	///投资者交割保证金
	TZQThostFtdcMoneyType	DeliveryMargin;
	///交易所交割保证金
	TZQThostFtdcMoneyType	ExchangeDeliveryMargin;
	///冻结的过户费
	TZQThostFtdcMoneyType	FrozenTransferFee;
	///冻结的印花税
	TZQThostFtdcMoneyType	FrozenStampTax;
	///过户费
	TZQThostFtdcMoneyType	TransferFee;
	///印花税
	TZQThostFtdcMoneyType	StampTax;
	///折算金额
	TZQThostFtdcMoneyType	ConversionAmount;
	///授信额度
	TZQThostFtdcMoneyType	CreditAmount;
	///最低维持担保比例
	TZQThostFtdcRatioType	LowLimitRatio;
	///融资买入金额
	TZQThostFtdcMoneyType	MarginTradingAmount;
	///融券卖出金额
	TZQThostFtdcMoneyType	ShortSellingAmount;
	///融资买入可用金额
	TZQThostFtdcMoneyType	MarginTradingAvail;
	///融券卖出可用金额
	TZQThostFtdcMoneyType	ShortSellingAvail;
	///维持担保比例
	TZQThostFtdcRatioType	CreditRatio;
	///证券总价值
	TZQThostFtdcMoneyType	StockValue;
	///融券总市值
	TZQThostFtdcMoneyType	SSStockValue;
	///国债回购占用资金
	TZQThostFtdcMoneyType	BondRepurchaseValue;
};

///正在同步中的投资者持仓
struct CZQThostFtdcSyncingInvestorPositionField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///持仓多空方向
	TZQThostFtdcPosiDirectionType	PosiDirection;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///持仓日期
	TZQThostFtdcPositionDateType	PositionDate;
	///上日持仓
	TZQThostFtdcVolumeType	YdPosition;
	///今日持仓
	TZQThostFtdcVolumeType	Position;
	///多头冻结
	TZQThostFtdcVolumeType	LongFrozen;
	///空头冻结
	TZQThostFtdcVolumeType	ShortFrozen;
	///开仓冻结金额
	TZQThostFtdcMoneyType	LongFrozenAmount;
	///开仓冻结金额
	TZQThostFtdcMoneyType	ShortFrozenAmount;
	///开仓量
	TZQThostFtdcVolumeType	OpenVolume;
	///平仓量
	TZQThostFtdcVolumeType	CloseVolume;
	///开仓金额
	TZQThostFtdcMoneyType	OpenAmount;
	///平仓金额
	TZQThostFtdcMoneyType	CloseAmount;
	///持仓成本
	TZQThostFtdcMoneyType	PositionCost;
	///冻结的资金
	TZQThostFtdcMoneyType	FrozenCash;
	///资金差额
	TZQThostFtdcMoneyType	CashIn;
	///手续费
	TZQThostFtdcMoneyType	Commission;
	///平仓盈亏
	TZQThostFtdcMoneyType	CloseProfit;
	///持仓盈亏
	TZQThostFtdcMoneyType	PositionProfit;
	///上次结算价
	TZQThostFtdcPriceType	PreSettlementPrice;
	///本次结算价
	TZQThostFtdcPriceType	SettlementPrice;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///开仓成本
	TZQThostFtdcMoneyType	OpenCost;
	///交易所保证金
	TZQThostFtdcMoneyType	ExchangeMargin;
	///今日持仓
	TZQThostFtdcVolumeType	TodayPosition;
	///过户费
	TZQThostFtdcMoneyType	TransferFee;
	///印花税
	TZQThostFtdcMoneyType	StampTax;
	///今日申购赎回数量
	TZQThostFtdcVolumeType	TodayPurRedVolume;
	///折算率
	TZQThostFtdcRatioType	ConversionRate;
	///折算金额
	TZQThostFtdcMoneyType	ConversionAmount;
	///融资买入出数量
	TZQThostFtdcVolumeType	MarginTradeVolume;
	///融资买入金额
	TZQThostFtdcMoneyType	MarginTradeAmount;
	///融资买入冻结数量
	TZQThostFtdcVolumeType	MarginTradeFrozenVolume;
	///融资买入冻结金额
	TZQThostFtdcMoneyType	MarginTradeFrozenAmount;
	///融资买入盈亏
	TZQThostFtdcMoneyType	MarginTradeConversionAmount;
	///融券卖出数量
	TZQThostFtdcVolumeType	ShortSellVolume;
	///融券卖出金额
	TZQThostFtdcMoneyType	ShortSellAmount;
	///融券卖出盈亏
	TZQThostFtdcMoneyType	ShortSellConversionAmount;
	///融券卖出冻结数量
	TZQThostFtdcVolumeType	ShortSellFrozenVolume;
	///融券卖出冻结金额
	TZQThostFtdcMoneyType	ShortSellFrozenAmount;
	///证券价值
	TZQThostFtdcMoneyType	StockValue;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///今日融资持仓
	TZQThostFtdcVolumeType	TodayMTPosition;
	///今日融券持仓
	TZQThostFtdcVolumeType	TodaySSPosition;
	///融券总市值
	TZQThostFtdcMoneyType	SSStockValue;
};

///正在同步中的合约保证金率
struct CZQThostFtdcSyncingInstrumentMarginRateField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///多头保证金率
	TZQThostFtdcRatioType	LongMarginRatioByMoney;
	///多头保证金费
	TZQThostFtdcMoneyType	LongMarginRatioByVolume;
	///空头保证金率
	TZQThostFtdcRatioType	ShortMarginRatioByMoney;
	///空头保证金费
	TZQThostFtdcMoneyType	ShortMarginRatioByVolume;
	///是否相对交易所收取
	TZQThostFtdcBoolType	IsRelative;
};

///正在同步中的合约手续费率
struct CZQThostFtdcSyncingInstrumentCommissionRateField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///印花税率
	TZQThostFtdcRatioType	StampTaxRateByMoney;
	///印花税率(按手数)
	TZQThostFtdcRatioType	StampTaxRateByVolume;
	///过户费率
	TZQThostFtdcRatioType	TransferFeeRateByMoney;
	///过户费率(按手数)
	TZQThostFtdcRatioType	TransferFeeRateByVolume;
	///交易费
	TZQThostFtdcRatioType	TradeFeeByMoney;
	///交易费(按手数)
	TZQThostFtdcRatioType	TradeFeeByVolume;
	///交易附加费率
	TZQThostFtdcRatioType	MarginByMoney;
	///最小过户费
	TZQThostFtdcPriceType	MinTradeFee;
};

///正在同步中的合约交易权限
struct CZQThostFtdcSyncingInstrumentTradingRightField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///买卖
	TZQThostFtdcDirectionType	Direction;
	///交易权限
	TZQThostFtdcTradingRightType	TradingRight;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///股票权限分类
	TZQThostFtdcInstrumentRangeType	InstrumentRange;
};

///查询报单
struct CZQThostFtdcQryOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单编号
	TZQThostFtdcOrderSysIDType	OrderSysID;
	///开始时间
	TZQThostFtdcTimeType	InsertTimeStart;
	///结束时间
	TZQThostFtdcTimeType	InsertTimeEnd;
};

///查询成交
struct CZQThostFtdcQryTradeField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///成交编号
	TZQThostFtdcTradeIDType	TradeID;
	///开始时间
	TZQThostFtdcTimeType	TradeTimeStart;
	///结束时间
	TZQThostFtdcTimeType	TradeTimeEnd;
};

///查询投资者持仓
struct CZQThostFtdcQryInvestorPositionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
};

///查询资金账户
struct CZQThostFtdcQryTradingAccountField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///查询投资者
struct CZQThostFtdcQryInvestorField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///查询交易编码
struct CZQThostFtdcQryTradingCodeField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
};

///查询交易编码
struct CZQThostFtdcQryInvestorGroupField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
};

///查询交易编码
struct CZQThostFtdcQryInstrumentMarginRateField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
};

///查询交易编码
struct CZQThostFtdcQryInstrumentCommissionRateField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
};

///查询交易编码
struct CZQThostFtdcQryInstrumentTradingRightField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
};

///查询经纪公司
struct CZQThostFtdcQryBrokerField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
};

///查询交易员
struct CZQThostFtdcQryTraderField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
};

///查询经纪公司会员代码
struct CZQThostFtdcQryPartBrokerField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
};

///查询管理用户功能权限
struct CZQThostFtdcQrySuperUserFunctionField
{
	///用户代码
	TZQThostFtdcUserIDType	UserID;
};

///查询用户会话
struct CZQThostFtdcQryUserSessionField
{
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
};

///查询前置状态
struct CZQThostFtdcQryFrontStatusField
{
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
};

///查询交易所报单
struct CZQThostFtdcQryExchangeOrderField
{
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
};

///查询报单操作
struct CZQThostFtdcQryOrderActionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
};

///查询交易所报单操作
struct CZQThostFtdcQryExchangeOrderActionField
{
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
};

///查询管理用户
struct CZQThostFtdcQrySuperUserField
{
	///用户代码
	TZQThostFtdcUserIDType	UserID;
};

///查询交易所
struct CZQThostFtdcQryExchangeField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
};

///查询产品
struct CZQThostFtdcQryProductField
{
	///产品代码
	TZQThostFtdcInstrumentIDType	ProductID;
};

///查询合约
struct CZQThostFtdcQryInstrumentField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///产品代码
	TZQThostFtdcInstrumentIDType	ProductID;
};

///查询行情
struct CZQThostFtdcQryDepthMarketDataField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
};

///查询经纪公司用户
struct CZQThostFtdcQryBrokerUserField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
};

///查询经纪公司用户权限
struct CZQThostFtdcQryBrokerUserFunctionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
};

///查询交易员报盘机
struct CZQThostFtdcQryTraderOfferField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
};

///查询出入金流水
struct CZQThostFtdcQrySyncDepositField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///出入金流水号
	TZQThostFtdcDepositSeqNoType	DepositSeqNo;
};

///查询投资者结算结果
struct CZQThostFtdcQrySettlementInfoField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///交易日
	TZQThostFtdcDateType	TradingDay;
};

///查询报单
struct CZQThostFtdcQryHisOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单编号
	TZQThostFtdcOrderSysIDType	OrderSysID;
	///开始时间
	TZQThostFtdcTimeType	InsertTimeStart;
	///结束时间
	TZQThostFtdcTimeType	InsertTimeEnd;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
};

///市场行情
struct CZQThostFtdcMarketDataField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///最新价
	TZQThostFtdcPriceType	LastPrice;
	///上次结算价
	TZQThostFtdcPriceType	PreSettlementPrice;
	///昨收盘
	TZQThostFtdcPriceType	PreClosePrice;
	///昨持仓量
	TZQThostFtdcLargeVolumeType	PreOpenInterest;
	///今开盘
	TZQThostFtdcPriceType	OpenPrice;
	///最高价
	TZQThostFtdcPriceType	HighestPrice;
	///最低价
	TZQThostFtdcPriceType	LowestPrice;
	///数量
	TZQThostFtdcVolumeType	Volume;
	///成交金额
	TZQThostFtdcMoneyType	Turnover;
	///持仓量
	TZQThostFtdcLargeVolumeType	OpenInterest;
	///今收盘
	TZQThostFtdcPriceType	ClosePrice;
	///本次结算价
	TZQThostFtdcPriceType	SettlementPrice;
	///涨停板价
	TZQThostFtdcPriceType	UpperLimitPrice;
	///跌停板价
	TZQThostFtdcPriceType	LowerLimitPrice;
	///昨虚实度
	TZQThostFtdcRatioType	PreDelta;
	///今虚实度
	TZQThostFtdcRatioType	CurrDelta;
	///最后修改时间
	TZQThostFtdcTimeType	UpdateTime;
	///最后修改毫秒
	TZQThostFtdcMillisecType	UpdateMillisec;
};

///行情交易所代码属性
struct CZQThostFtdcMarketDataExchangeField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
};

///行情基础属性
struct CZQThostFtdcMarketDataBaseField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///上次结算价
	TZQThostFtdcPriceType	PreSettlementPrice;
	///昨收盘
	TZQThostFtdcPriceType	PreClosePrice;
	///昨持仓量
	TZQThostFtdcLargeVolumeType	PreOpenInterest;
	///昨虚实度
	TZQThostFtdcRatioType	PreDelta;
};

///行情静态属性
struct CZQThostFtdcMarketDataStaticField
{
	///今开盘
	TZQThostFtdcPriceType	OpenPrice;
	///最高价
	TZQThostFtdcPriceType	HighestPrice;
	///最低价
	TZQThostFtdcPriceType	LowestPrice;
	///今收盘
	TZQThostFtdcPriceType	ClosePrice;
	///涨停板价
	TZQThostFtdcPriceType	UpperLimitPrice;
	///跌停板价
	TZQThostFtdcPriceType	LowerLimitPrice;
	///本次结算价
	TZQThostFtdcPriceType	SettlementPrice;
	///今虚实度
	TZQThostFtdcRatioType	CurrDelta;
};

///行情最新成交属性
struct CZQThostFtdcMarketDataLastMatchField
{
	///最新价
	TZQThostFtdcPriceType	LastPrice;
	///数量
	TZQThostFtdcVolumeType	Volume;
	///成交金额
	TZQThostFtdcMoneyType	Turnover;
	///持仓量
	TZQThostFtdcLargeVolumeType	OpenInterest;
};

///行情最优价属性
struct CZQThostFtdcMarketDataBestPriceField
{
	///申买价一
	TZQThostFtdcPriceType	BidPrice1;
	///申买量一
	TZQThostFtdcVolumeType	BidVolume1;
	///申卖价一
	TZQThostFtdcPriceType	AskPrice1;
	///申卖量一
	TZQThostFtdcVolumeType	AskVolume1;
};

///行情申买二、三属性
struct CZQThostFtdcMarketDataBid23Field
{
	///申买价二
	TZQThostFtdcPriceType	BidPrice2;
	///申买量二
	TZQThostFtdcVolumeType	BidVolume2;
	///申买价三
	TZQThostFtdcPriceType	BidPrice3;
	///申买量三
	TZQThostFtdcVolumeType	BidVolume3;
};

///行情申卖二、三属性
struct CZQThostFtdcMarketDataAsk23Field
{
	///申卖价二
	TZQThostFtdcPriceType	AskPrice2;
	///申卖量二
	TZQThostFtdcVolumeType	AskVolume2;
	///申卖价三
	TZQThostFtdcPriceType	AskPrice3;
	///申卖量三
	TZQThostFtdcVolumeType	AskVolume3;
};

///行情申买四、五属性
struct CZQThostFtdcMarketDataBid45Field
{
	///申买价四
	TZQThostFtdcPriceType	BidPrice4;
	///申买量四
	TZQThostFtdcVolumeType	BidVolume4;
	///申买价五
	TZQThostFtdcPriceType	BidPrice5;
	///申买量五
	TZQThostFtdcVolumeType	BidVolume5;
};

///行情申卖四、五属性
struct CZQThostFtdcMarketDataAsk45Field
{
	///申卖价四
	TZQThostFtdcPriceType	AskPrice4;
	///申卖量四
	TZQThostFtdcVolumeType	AskVolume4;
	///申卖价五
	TZQThostFtdcPriceType	AskPrice5;
	///申卖量五
	TZQThostFtdcVolumeType	AskVolume5;
};

///行情更新时间属性
struct CZQThostFtdcMarketDataUpdateTimeField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///最后修改时间
	TZQThostFtdcTimeType	UpdateTime;
	///最后修改毫秒
	TZQThostFtdcMillisecType	UpdateMillisec;
};

///指定的合约
struct CZQThostFtdcSpecificInstrumentField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
};

///合约状态
struct CZQThostFtdcInstrumentStatusField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///结算组代码
	TZQThostFtdcSettlementGroupIDType	SettlementGroupID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///合约交易状态
	TZQThostFtdcInstrumentStatusType	InstrumentStatus;
	///交易阶段编号
	TZQThostFtdcTradingSegmentSNType	TradingSegmentSN;
	///进入本状态时间
	TZQThostFtdcTimeType	EnterTime;
	///进入本状态原因
	TZQThostFtdcInstStatusEnterReasonType	EnterReason;
};

///查询合约状态
struct CZQThostFtdcQryInstrumentStatusField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
};

///投资者账户
struct CZQThostFtdcInvestorAccountField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
};

///浮动盈亏算法
struct CZQThostFtdcPositionProfitAlgorithmField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///盈亏算法
	TZQThostFtdcAlgorithmType	Algorithm;
	///备注
	TZQThostFtdcMemoType	Memo;
};

///会员资金折扣
struct CZQThostFtdcDiscountField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///资金折扣比例
	TZQThostFtdcRatioType	Discount;
};

///查询转帐银行
struct CZQThostFtdcQryTransferBankField
{
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分中心代码
	TZQThostFtdcBankBrchIDType	BankBrchID;
};

///转帐银行
struct CZQThostFtdcTransferBankField
{
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分中心代码
	TZQThostFtdcBankBrchIDType	BankBrchID;
	///银行名称
	TZQThostFtdcBankNameType	BankName;
	///是否活跃
	TZQThostFtdcBoolType	IsActive;
};

///查询投资者持仓明细
struct CZQThostFtdcQryInvestorPositionDetailField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
};

///投资者持仓明细
struct CZQThostFtdcInvestorPositionDetailField
{
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///买卖
	TZQThostFtdcDirectionType	Direction;
	///开仓日期
	TZQThostFtdcDateType	OpenDate;
	///成交编号
	TZQThostFtdcTradeIDType	TradeID;
	///数量
	TZQThostFtdcVolumeType	Volume;
	///开仓价
	TZQThostFtdcPriceType	OpenPrice;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///成交类型
	TZQThostFtdcTradeTypeType	TradeType;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///投资者保证金
	TZQThostFtdcMoneyType	Margin;
	///交易所保证金
	TZQThostFtdcMoneyType	ExchMargin;
	///昨结算价
	TZQThostFtdcPriceType	LastSettlementPrice;
	///结算价
	TZQThostFtdcPriceType	SettlementPrice;
	///平仓量
	TZQThostFtdcVolumeType	CloseVolume;
	///平仓金额
	TZQThostFtdcMoneyType	CloseAmount;
	///过户费
	TZQThostFtdcMoneyType	TransferFee;
	///印花税
	TZQThostFtdcMoneyType	StampTax;
	///手续费
	TZQThostFtdcMoneyType	Commission;
	///融资融券金额
	TZQThostFtdcMoneyType	Amount;
};

///资金账户口令域
struct CZQThostFtdcTradingAccountPasswordField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///密码
	TZQThostFtdcPasswordType	Password;
};

///交易所行情报盘机
struct CZQThostFtdcMDTraderOfferField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///密码
	TZQThostFtdcPasswordType	Password;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///交易所交易员连接状态
	TZQThostFtdcTraderConnectStatusType	TraderConnectStatus;
	///发出连接请求的日期
	TZQThostFtdcDateType	ConnectRequestDate;
	///发出连接请求的时间
	TZQThostFtdcTimeType	ConnectRequestTime;
	///上次报告日期
	TZQThostFtdcDateType	LastReportDate;
	///上次报告时间
	TZQThostFtdcTimeType	LastReportTime;
	///完成连接日期
	TZQThostFtdcDateType	ConnectDate;
	///完成连接时间
	TZQThostFtdcTimeType	ConnectTime;
	///启动日期
	TZQThostFtdcDateType	StartDate;
	///启动时间
	TZQThostFtdcTimeType	StartTime;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
};

///查询行情报盘机
struct CZQThostFtdcQryMDTraderOfferField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
};

///查询客户通知
struct CZQThostFtdcQryNoticeField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
};

///客户通知
struct CZQThostFtdcNoticeField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///消息正文
	TZQThostFtdcContentType	Content;
	///经纪公司通知内容序列号
	TZQThostFtdcSequenceLabelType	SequenceLabel;
};

///用户权限
struct CZQThostFtdcUserRightField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///客户权限类型
	TZQThostFtdcUserRightTypeType	UserRightType;
	///是否禁止
	TZQThostFtdcBoolType	IsForbidden;
};

///查询结算信息确认域
struct CZQThostFtdcQrySettlementInfoConfirmField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///装载结算信息
struct CZQThostFtdcLoadSettlementInfoField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
};

///经纪公司可提资金算法表
struct CZQThostFtdcBrokerWithdrawAlgorithmField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///可提资金算法
	TZQThostFtdcAlgorithmType	WithdrawAlgorithm;
	///资金使用率
	TZQThostFtdcRatioType	UsingRatio;
	///可提是否包含平仓盈利
	TZQThostFtdcIncludeCloseProfitType	IncludeCloseProfit;
	///本日无仓且无成交客户是否受可提比例限制
	TZQThostFtdcAllWithoutTradeType	AllWithoutTrade;
	///可用是否包含平仓盈利
	TZQThostFtdcIncludeCloseProfitType	AvailIncludeCloseProfit;
	///是否启用用户事件
	TZQThostFtdcBoolType	IsBrokerUserEvent;
};

///资金账户口令变更域
struct CZQThostFtdcTradingAccountPasswordUpdateV1Field
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///原来的口令
	TZQThostFtdcPasswordType	OldPassword;
	///新的口令
	TZQThostFtdcPasswordType	NewPassword;
};

///资金账户口令变更域
struct CZQThostFtdcTradingAccountPasswordUpdateField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///原来的口令
	TZQThostFtdcPasswordType	OldPassword;
	///新的口令
	TZQThostFtdcPasswordType	NewPassword;
};

///查询组合合约分腿
struct CZQThostFtdcQryCombinationLegField
{
	///组合合约代码
	TZQThostFtdcInstrumentIDType	CombInstrumentID;
	///单腿编号
	TZQThostFtdcLegIDType	LegID;
	///单腿合约代码
	TZQThostFtdcInstrumentIDType	LegInstrumentID;
};

///查询组合合约分腿
struct CZQThostFtdcQrySyncStatusField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
};

///组合交易合约的单腿
struct CZQThostFtdcCombinationLegField
{
	///组合合约代码
	TZQThostFtdcInstrumentIDType	CombInstrumentID;
	///单腿编号
	TZQThostFtdcLegIDType	LegID;
	///单腿合约代码
	TZQThostFtdcInstrumentIDType	LegInstrumentID;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///单腿乘数
	TZQThostFtdcLegMultipleType	LegMultiple;
	///派生层数
	TZQThostFtdcImplyLevelType	ImplyLevel;
};

///数据同步状态
struct CZQThostFtdcSyncStatusField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///数据同步状态
	TZQThostFtdcDataSyncStatusType	DataSyncStatus;
};

///查询联系人
struct CZQThostFtdcQryLinkManField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///联系人
struct CZQThostFtdcLinkManField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///联系人类型
	TZQThostFtdcPersonTypeType	PersonType;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdentifiedCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///名称
	TZQThostFtdcPartyNameType	PersonName;
	///联系电话
	TZQThostFtdcTelephoneType	Telephone;
	///通讯地址
	TZQThostFtdcAddressType	Address;
	///邮政编码
	TZQThostFtdcZipCodeType	ZipCode;
	///优先级
	TZQThostFtdcPriorityType	Priority;
};

///查询经纪公司用户事件
struct CZQThostFtdcQryBrokerUserEventField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///用户事件类型
	TZQThostFtdcUserEventTypeType	UserEventType;
};

///查询经纪公司用户事件
struct CZQThostFtdcBrokerUserEventField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///用户事件类型
	TZQThostFtdcUserEventTypeType	UserEventType;
	///用户事件序号
	TZQThostFtdcSequenceNoType	EventSequenceNo;
	///事件发生日期
	TZQThostFtdcDateType	EventDate;
	///事件发生时间
	TZQThostFtdcTimeType	EventTime;
	///用户事件信息
	TZQThostFtdcUserEventInfoType	UserEventInfo;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
};

///查询签约银行请求
struct CZQThostFtdcQryContractBankField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分中心代码
	TZQThostFtdcBankBrchIDType	BankBrchID;
};

///查询签约银行响应
struct CZQThostFtdcContractBankField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分中心代码
	TZQThostFtdcBankBrchIDType	BankBrchID;
	///银行名称
	TZQThostFtdcBankNameType	BankName;
};

///投资者组合持仓明细
struct CZQThostFtdcInvestorPositionCombineDetailField
{
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///开仓日期
	TZQThostFtdcDateType	OpenDate;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///组合编号
	TZQThostFtdcTradeIDType	ComTradeID;
	///撮合编号
	TZQThostFtdcTradeIDType	TradeID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///买卖
	TZQThostFtdcDirectionType	Direction;
	///持仓量
	TZQThostFtdcVolumeType	TotalAmt;
	///投资者保证金
	TZQThostFtdcMoneyType	Margin;
	///交易所保证金
	TZQThostFtdcMoneyType	ExchMargin;
	///保证金率
	TZQThostFtdcRatioType	MarginRateByMoney;
	///保证金率(按手数)
	TZQThostFtdcRatioType	MarginRateByVolume;
	///单腿编号
	TZQThostFtdcLegIDType	LegID;
	///单腿乘数
	TZQThostFtdcLegMultipleType	LegMultiple;
	///组合持仓合约编码
	TZQThostFtdcInstrumentIDType	CombInstrumentID;
};

///预埋单
struct CZQThostFtdcParkedOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单价格条件
	TZQThostFtdcOrderPriceTypeType	OrderPriceType;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///组合开平标志
	TZQThostFtdcCombOffsetFlagType	CombOffsetFlag;
	///组合投机套保标志
	TZQThostFtdcCombHedgeFlagType	CombHedgeFlag;
	///价格
	TZQThostFtdcStockPriceType	LimitPrice;
	///数量
	TZQThostFtdcVolumeType	VolumeTotalOriginal;
	///有效期类型
	TZQThostFtdcTimeConditionType	TimeCondition;
	///GTD日期
	TZQThostFtdcDateType	GTDDate;
	///成交量类型
	TZQThostFtdcVolumeConditionType	VolumeCondition;
	///最小成交量
	TZQThostFtdcVolumeType	MinVolume;
	///触发条件
	TZQThostFtdcContingentConditionType	ContingentCondition;
	///止损价
	TZQThostFtdcPriceType	StopPrice;
	///强平原因
	TZQThostFtdcForceCloseReasonType	ForceCloseReason;
	///自动挂起标志
	TZQThostFtdcBoolType	IsAutoSuspend;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///用户强评标志
	TZQThostFtdcBoolType	UserForceClose;
	///预埋报单编号
	TZQThostFtdcParkedOrderIDType	ParkedOrderID;
	///用户类型
	TZQThostFtdcUserTypeType	UserType;
	///预埋单状态
	TZQThostFtdcParkedOrderStatusType	Status;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///输入预埋单操作
struct CZQThostFtdcParkedOrderActionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///报单操作引用
	TZQThostFtdcOrderActionRefType	OrderActionRef;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///操作标志
	TZQThostFtdcActionFlagType	ActionFlag;
	///价格
	TZQThostFtdcPriceType	LimitPrice;
	///数量变化
	TZQThostFtdcVolumeType	VolumeChange;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///预埋撤单单编号
	TZQThostFtdcParkedOrderActionIDType	ParkedOrderActionID;
	///用户类型
	TZQThostFtdcUserTypeType	UserType;
	///预埋撤单状态
	TZQThostFtdcParkedOrderStatusType	Status;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///查询预埋单
struct CZQThostFtdcQryParkedOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
};

///查询预埋撤单
struct CZQThostFtdcQryParkedOrderActionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
};

///删除预埋单
struct CZQThostFtdcRemoveParkedOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///预埋报单编号
	TZQThostFtdcParkedOrderIDType	ParkedOrderID;
};

///删除预埋撤单
struct CZQThostFtdcRemoveParkedOrderActionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///预埋撤单编号
	TZQThostFtdcParkedOrderActionIDType	ParkedOrderActionID;
};

///经纪公司可提资金算法表
struct CZQThostFtdcInvestorWithdrawAlgorithmField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///可提资金比例
	TZQThostFtdcRatioType	UsingRatio;
};

///查询组合持仓明细
struct CZQThostFtdcQryInvestorPositionCombineDetailField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///组合持仓合约编码
	TZQThostFtdcInstrumentIDType	CombInstrumentID;
};

///成交均价
struct CZQThostFtdcMarketDataAveragePriceField
{
	///当日均价
	TZQThostFtdcPriceType	AveragePrice;
};

///校验投资者密码
struct CZQThostFtdcVerifyInvestorPasswordField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///密码
	TZQThostFtdcPasswordType	Password;
};

///用户IP
struct CZQThostFtdcUserIPField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///IP地址
	TZQThostFtdcIPAddressType	IPAddress;
	///IP地址掩码
	TZQThostFtdcIPAddressType	IPMask;
	///Mac地址
	TZQThostFtdcMacAddressType	MacAddress;
};

///用户事件通知信息
struct CZQThostFtdcTradingNoticeInfoField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///发送时间
	TZQThostFtdcTimeType	SendTime;
	///消息正文
	TZQThostFtdcContentType	FieldContent;
	///序列系列号
	TZQThostFtdcSequenceSeriesType	SequenceSeries;
	///序列号
	TZQThostFtdcSequenceNoType	SequenceNo;
};

///用户事件通知
struct CZQThostFtdcTradingNoticeField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者范围
	TZQThostFtdcInvestorRangeType	InvestorRange;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///序列系列号
	TZQThostFtdcSequenceSeriesType	SequenceSeries;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///发送时间
	TZQThostFtdcTimeType	SendTime;
	///序列号
	TZQThostFtdcSequenceNoType	SequenceNo;
	///消息正文
	TZQThostFtdcContentType	FieldContent;
};

///查询交易事件通知
struct CZQThostFtdcQryTradingNoticeField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///查询错误报单
struct CZQThostFtdcQryErrOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///错误报单
struct CZQThostFtdcErrOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单价格条件
	TZQThostFtdcOrderPriceTypeType	OrderPriceType;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///组合开平标志
	TZQThostFtdcCombOffsetFlagType	CombOffsetFlag;
	///组合投机套保标志
	TZQThostFtdcCombHedgeFlagType	CombHedgeFlag;
	///价格
	TZQThostFtdcStockPriceType	LimitPrice;
	///数量
	TZQThostFtdcVolumeType	VolumeTotalOriginal;
	///有效期类型
	TZQThostFtdcTimeConditionType	TimeCondition;
	///GTD日期
	TZQThostFtdcDateType	GTDDate;
	///成交量类型
	TZQThostFtdcVolumeConditionType	VolumeCondition;
	///最小成交量
	TZQThostFtdcVolumeType	MinVolume;
	///触发条件
	TZQThostFtdcContingentConditionType	ContingentCondition;
	///止损价
	TZQThostFtdcPriceType	StopPrice;
	///强平原因
	TZQThostFtdcForceCloseReasonType	ForceCloseReason;
	///自动挂起标志
	TZQThostFtdcBoolType	IsAutoSuspend;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///用户强评标志
	TZQThostFtdcBoolType	UserForceClose;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///查询错误报单操作
struct CZQThostFtdcErrorConditionalOrderField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///报单价格条件
	TZQThostFtdcOrderPriceTypeType	OrderPriceType;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///组合开平标志
	TZQThostFtdcCombOffsetFlagType	CombOffsetFlag;
	///组合投机套保标志
	TZQThostFtdcCombHedgeFlagType	CombHedgeFlag;
	///价格
	TZQThostFtdcStockPriceType	LimitPrice;
	///数量
	TZQThostFtdcVolumeType	VolumeTotalOriginal;
	///有效期类型
	TZQThostFtdcTimeConditionType	TimeCondition;
	///GTD日期
	TZQThostFtdcDateType	GTDDate;
	///成交量类型
	TZQThostFtdcVolumeConditionType	VolumeCondition;
	///最小成交量
	TZQThostFtdcVolumeType	MinVolume;
	///触发条件
	TZQThostFtdcContingentConditionType	ContingentCondition;
	///止损价
	TZQThostFtdcPriceType	StopPrice;
	///强平原因
	TZQThostFtdcForceCloseReasonType	ForceCloseReason;
	///自动挂起标志
	TZQThostFtdcBoolType	IsAutoSuspend;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///合约在交易所的代码
	TZQThostFtdcExchangeInstIDType	ExchangeInstID;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///报单提交状态
	TZQThostFtdcOrderSubmitStatusType	OrderSubmitStatus;
	///报单提示序号
	TZQThostFtdcSequenceNoType	NotifySequence;
	///交易日
	TZQThostFtdcDateType	TradingDay;
	///结算编号
	TZQThostFtdcSettlementIDType	SettlementID;
	///报单编号
	TZQThostFtdcOrderSysIDType	OrderSysID;
	///报单来源
	TZQThostFtdcOrderSourceType	OrderSource;
	///报单状态
	TZQThostFtdcOrderStatusType	OrderStatus;
	///报单类型
	TZQThostFtdcOrderTypeType	OrderType;
	///今成交数量
	TZQThostFtdcVolumeType	VolumeTraded;
	///剩余数量
	TZQThostFtdcVolumeType	VolumeTotal;
	///报单日期
	TZQThostFtdcDateType	InsertDate;
	///委托时间
	TZQThostFtdcTimeType	InsertTime;
	///激活时间
	TZQThostFtdcTimeType	ActiveTime;
	///挂起时间
	TZQThostFtdcTimeType	SuspendTime;
	///最后修改时间
	TZQThostFtdcTimeType	UpdateTime;
	///撤销时间
	TZQThostFtdcTimeType	CancelTime;
	///最后修改交易所交易员代码
	TZQThostFtdcTraderIDType	ActiveTraderID;
	///结算会员编号
	TZQThostFtdcParticipantIDType	ClearingPartID;
	///序号
	TZQThostFtdcSequenceNoType	SequenceNo;
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///用户端产品信息
	TZQThostFtdcProductInfoType	UserProductInfo;
	///状态信息
	TZQThostFtdcErrorMsgType	StatusMsg;
	///用户强评标志
	TZQThostFtdcBoolType	UserForceClose;
	///操作用户代码
	TZQThostFtdcUserIDType	ActiveUserID;
	///经纪公司报单编号
	TZQThostFtdcSequenceNoType	BrokerOrderSeq;
	///相关报单
	TZQThostFtdcOrderSysIDType	RelativeOrderSysID;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
	///成交数量
	TZQThostFtdcMoneyType	TradeAmount;
	///是否ETF
	TZQThostFtdcBoolType	IsETF;
	///资金帐号
	TZQThostFtdcAccountIDType	AccountID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///查询错误报单操作
struct CZQThostFtdcQryErrOrderActionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///错误报单操作
struct CZQThostFtdcErrOrderActionField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///报单操作引用
	TZQThostFtdcOrderActionRefType	OrderActionRef;
	///报单引用
	TZQThostFtdcOrderRefType	OrderRef;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///前置编号
	TZQThostFtdcFrontIDType	FrontID;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///操作标志
	TZQThostFtdcActionFlagType	ActionFlag;
	///价格
	TZQThostFtdcPriceType	LimitPrice;
	///数量变化
	TZQThostFtdcVolumeType	VolumeChange;
	///操作日期
	TZQThostFtdcDateType	ActionDate;
	///操作时间
	TZQThostFtdcTimeType	ActionTime;
	///交易所交易员代码
	TZQThostFtdcTraderIDType	TraderID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///本地报单编号
	TZQThostFtdcOrderLocalIDType	OrderLocalID;
	///操作本地编号
	TZQThostFtdcOrderLocalIDType	ActionLocalID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///客户代码
	TZQThostFtdcClientIDType	ClientID;
	///业务单元
	TZQThostFtdcBusinessUnitType	BusinessUnit;
	///报单操作状态
	TZQThostFtdcOrderActionStatusType	OrderActionStatus;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///营业部编号
	TZQThostFtdcBranchIDType	BranchID;
	///状态信息
	TZQThostFtdcErrorMsgType	StatusMsg;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///查询交易所状态
struct CZQThostFtdcQryExchangeSequenceField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
};

///交易所状态
struct CZQThostFtdcExchangeSequenceField
{
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///序号
	TZQThostFtdcSequenceNoType	SequenceNo;
	///合约交易状态
	TZQThostFtdcInstrumentStatusType	MarketStatus;
};

///根据价格查询最大报单数量
struct CZQThostFtdcQueryMaxOrderVolumeWithPriceField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///买卖方向
	TZQThostFtdcDirectionType	Direction;
	///开平标志
	TZQThostFtdcOffsetFlagType	OffsetFlag;
	///投机套保标志
	TZQThostFtdcHedgeFlagType	HedgeFlag;
	///最大允许报单数量
	TZQThostFtdcVolumeType	MaxVolume;
	///报单价格
	TZQThostFtdcPriceType	Price;
};

///查询经纪公司交易参数
struct CZQThostFtdcQryBrokerTradingParamsField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///经纪公司交易参数
struct CZQThostFtdcBrokerTradingParamsField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///保证金价格类型
	TZQThostFtdcMarginPriceTypeType	MarginPriceType;
	///盈亏算法
	TZQThostFtdcAlgorithmType	Algorithm;
	///可用是否包含平仓盈利
	TZQThostFtdcIncludeCloseProfitType	AvailIncludeCloseProfit;
};

///查询经纪公司交易算法
struct CZQThostFtdcQryBrokerTradingAlgosField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
};

///经纪公司交易算法
struct CZQThostFtdcBrokerTradingAlgosField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///持仓处理算法编号
	TZQThostFtdcHandlePositionAlgoIDType	HandlePositionAlgoID;
	///寻找保证金率算法编号
	TZQThostFtdcFindMarginRateAlgoIDType	FindMarginRateAlgoID;
	///资金处理算法编号
	TZQThostFtdcHandleTradingAccountAlgoIDType	HandleTradingAccountAlgoID;
};

///查询经纪公司资金
struct CZQThostFtdcQueryBrokerDepositField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
};

///经纪公司资金
struct CZQThostFtdcBrokerDepositField
{
	///交易日期
	TZQThostFtdcTradeDateType	TradingDay;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///会员代码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///交易所代码
	TZQThostFtdcExchangeIDType	ExchangeID;
	///上次结算准备金
	TZQThostFtdcMoneyType	PreBalance;
	///当前保证金总额
	TZQThostFtdcMoneyType	CurrMargin;
	///平仓盈亏
	TZQThostFtdcMoneyType	CloseProfit;
	///期货结算准备金
	TZQThostFtdcMoneyType	Balance;
	///入金金额
	TZQThostFtdcMoneyType	Deposit;
	///出金金额
	TZQThostFtdcMoneyType	Withdraw;
	///可提资金
	TZQThostFtdcMoneyType	Available;
	///基本准备金
	TZQThostFtdcMoneyType	Reserve;
	///冻结的保证金
	TZQThostFtdcMoneyType	FrozenMargin;
};

///查询保证金监管系统经纪公司密钥
struct CZQThostFtdcQryCFMMCBrokerKeyField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
};

///保证金监管系统经纪公司密钥
struct CZQThostFtdcCFMMCBrokerKeyField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///经纪公司统一编码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///密钥生成日期
	TZQThostFtdcDateType	CreateDate;
	///密钥生成时间
	TZQThostFtdcTimeType	CreateTime;
	///密钥编号
	TZQThostFtdcSequenceNoType	KeyID;
	///动态密钥
	TZQThostFtdcCFMMCKeyType	CurrentKey;
	///动态密钥类型
	TZQThostFtdcCFMMCKeyKindType	KeyKind;
};

///保证金监管系统经纪公司资金账户密钥
struct CZQThostFtdcCFMMCTradingAccountKeyField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///经纪公司统一编码
	TZQThostFtdcParticipantIDType	ParticipantID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///密钥编号
	TZQThostFtdcSequenceNoType	KeyID;
	///动态密钥
	TZQThostFtdcCFMMCKeyType	CurrentKey;
};

///请求查询保证金监管系统经纪公司资金账户密钥
struct CZQThostFtdcQryCFMMCTradingAccountKeyField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
};

///用户动态令牌参数
struct CZQThostFtdcBrokerUserOTPParamField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///动态令牌提供商
	TZQThostFtdcOTPVendorsIDType	OTPVendorsID;
	///动态令牌序列号
	TZQThostFtdcSerialNumberType	SerialNumber;
	///令牌密钥
	TZQThostFtdcAuthKeyType	AuthKey;
	///漂移值
	TZQThostFtdcLastDriftType	LastDrift;
	///成功值
	TZQThostFtdcLastSuccessType	LastSuccess;
	///动态令牌类型
	TZQThostFtdcOTPTypeType	OTPType;
};

///手工同步用户动态令牌
struct CZQThostFtdcManualSyncBrokerUserOTPField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TZQThostFtdcUserIDType	UserID;
	///动态令牌类型
	TZQThostFtdcOTPTypeType	OTPType;
	///第一个动态密码
	TZQThostFtdcPasswordType	FirstOTP;
	///第二个动态密码
	TZQThostFtdcPasswordType	SecondOTP;
};

///转帐开户请求
struct CZQThostFtdcReqOpenAccountField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///性别
	TZQThostFtdcGenderType	Gender;
	///国家代码
	TZQThostFtdcCountryCodeType	CountryCode;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///地址
	TZQThostFtdcAddressType	Address;
	///邮编
	TZQThostFtdcZipCodeType	ZipCode;
	///电话号码
	TZQThostFtdcTelephoneType	Telephone;
	///手机
	TZQThostFtdcMobilePhoneType	MobilePhone;
	///传真
	TZQThostFtdcFaxType	Fax;
	///电子邮件
	TZQThostFtdcEMailType	EMail;
	///资金账户状态
	TZQThostFtdcMoneyAccountStatusType	MoneyAccountStatus;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///汇钞标志
	TZQThostFtdcCashExchangeCodeType	CashExchangeCode;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///交易ID
	TZQThostFtdcTIDType	TID;
};

///转帐销户请求
struct CZQThostFtdcReqCancelAccountField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///性别
	TZQThostFtdcGenderType	Gender;
	///国家代码
	TZQThostFtdcCountryCodeType	CountryCode;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///地址
	TZQThostFtdcAddressType	Address;
	///邮编
	TZQThostFtdcZipCodeType	ZipCode;
	///电话号码
	TZQThostFtdcTelephoneType	Telephone;
	///手机
	TZQThostFtdcMobilePhoneType	MobilePhone;
	///传真
	TZQThostFtdcFaxType	Fax;
	///电子邮件
	TZQThostFtdcEMailType	EMail;
	///资金账户状态
	TZQThostFtdcMoneyAccountStatusType	MoneyAccountStatus;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///汇钞标志
	TZQThostFtdcCashExchangeCodeType	CashExchangeCode;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///交易ID
	TZQThostFtdcTIDType	TID;
};

///变更银行账户请求
struct CZQThostFtdcReqChangeAccountField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///性别
	TZQThostFtdcGenderType	Gender;
	///国家代码
	TZQThostFtdcCountryCodeType	CountryCode;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///地址
	TZQThostFtdcAddressType	Address;
	///邮编
	TZQThostFtdcZipCodeType	ZipCode;
	///电话号码
	TZQThostFtdcTelephoneType	Telephone;
	///手机
	TZQThostFtdcMobilePhoneType	MobilePhone;
	///传真
	TZQThostFtdcFaxType	Fax;
	///电子邮件
	TZQThostFtdcEMailType	EMail;
	///资金账户状态
	TZQThostFtdcMoneyAccountStatusType	MoneyAccountStatus;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///新银行帐号
	TZQThostFtdcBankAccountType	NewBankAccount;
	///新银行密码
	TZQThostFtdcPasswordType	NewBankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///摘要
	TZQThostFtdcDigestType	Digest;
};

///转账请求
struct CZQThostFtdcReqTransferField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///期货公司流水号
	TZQThostFtdcFutureSerialType	FutureSerial;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///转帐金额
	TZQThostFtdcTradeAmountType	TradeAmount;
	///期货可取金额
	TZQThostFtdcTradeAmountType	FutureFetchAmount;
	///费用支付标志
	TZQThostFtdcFeePayFlagType	FeePayFlag;
	///应收客户费用
	TZQThostFtdcCustFeeType	CustFee;
	///应收期货公司费用
	TZQThostFtdcFutureFeeType	BrokerFee;
	///发送方给接收方的消息
	TZQThostFtdcAddInfoType	Message;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///转账交易状态
	TZQThostFtdcTransferStatusType	TransferStatus;
};

///银行发起银行资金转期货响应
struct CZQThostFtdcRspTransferField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///期货公司流水号
	TZQThostFtdcFutureSerialType	FutureSerial;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///转帐金额
	TZQThostFtdcTradeAmountType	TradeAmount;
	///期货可取金额
	TZQThostFtdcTradeAmountType	FutureFetchAmount;
	///费用支付标志
	TZQThostFtdcFeePayFlagType	FeePayFlag;
	///应收客户费用
	TZQThostFtdcCustFeeType	CustFee;
	///应收期货公司费用
	TZQThostFtdcFutureFeeType	BrokerFee;
	///发送方给接收方的消息
	TZQThostFtdcAddInfoType	Message;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///转账交易状态
	TZQThostFtdcTransferStatusType	TransferStatus;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///冲正请求
struct CZQThostFtdcReqRepealField
{
	///冲正时间间隔
	TZQThostFtdcRepealTimeIntervalType	RepealTimeInterval;
	///已经冲正次数
	TZQThostFtdcRepealedTimesType	RepealedTimes;
	///银行冲正标志
	TZQThostFtdcBankRepealFlagType	BankRepealFlag;
	///期商冲正标志
	TZQThostFtdcBrokerRepealFlagType	BrokerRepealFlag;
	///被冲正平台流水号
	TZQThostFtdcPlateSerialType	PlateRepealSerial;
	///被冲正银行流水号
	TZQThostFtdcBankSerialType	BankRepealSerial;
	///被冲正期货流水号
	TZQThostFtdcFutureSerialType	FutureRepealSerial;
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///期货公司流水号
	TZQThostFtdcFutureSerialType	FutureSerial;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///转帐金额
	TZQThostFtdcTradeAmountType	TradeAmount;
	///期货可取金额
	TZQThostFtdcTradeAmountType	FutureFetchAmount;
	///费用支付标志
	TZQThostFtdcFeePayFlagType	FeePayFlag;
	///应收客户费用
	TZQThostFtdcCustFeeType	CustFee;
	///应收期货公司费用
	TZQThostFtdcFutureFeeType	BrokerFee;
	///发送方给接收方的消息
	TZQThostFtdcAddInfoType	Message;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///转账交易状态
	TZQThostFtdcTransferStatusType	TransferStatus;
};

///冲正响应
struct CZQThostFtdcRspRepealField
{
	///冲正时间间隔
	TZQThostFtdcRepealTimeIntervalType	RepealTimeInterval;
	///已经冲正次数
	TZQThostFtdcRepealedTimesType	RepealedTimes;
	///银行冲正标志
	TZQThostFtdcBankRepealFlagType	BankRepealFlag;
	///期商冲正标志
	TZQThostFtdcBrokerRepealFlagType	BrokerRepealFlag;
	///被冲正平台流水号
	TZQThostFtdcPlateSerialType	PlateRepealSerial;
	///被冲正银行流水号
	TZQThostFtdcBankSerialType	BankRepealSerial;
	///被冲正期货流水号
	TZQThostFtdcFutureSerialType	FutureRepealSerial;
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///期货公司流水号
	TZQThostFtdcFutureSerialType	FutureSerial;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///转帐金额
	TZQThostFtdcTradeAmountType	TradeAmount;
	///期货可取金额
	TZQThostFtdcTradeAmountType	FutureFetchAmount;
	///费用支付标志
	TZQThostFtdcFeePayFlagType	FeePayFlag;
	///应收客户费用
	TZQThostFtdcCustFeeType	CustFee;
	///应收期货公司费用
	TZQThostFtdcFutureFeeType	BrokerFee;
	///发送方给接收方的消息
	TZQThostFtdcAddInfoType	Message;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///转账交易状态
	TZQThostFtdcTransferStatusType	TransferStatus;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///查询账户信息请求
struct CZQThostFtdcReqQueryAccountField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///期货公司流水号
	TZQThostFtdcFutureSerialType	FutureSerial;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
};

///查询账户信息响应
struct CZQThostFtdcRspQueryAccountField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///期货公司流水号
	TZQThostFtdcFutureSerialType	FutureSerial;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///银行可用金额
	TZQThostFtdcTradeAmountType	BankUseAmount;
	///银行可取金额
	TZQThostFtdcTradeAmountType	BankFetchAmount;
};

///期商签到签退
struct CZQThostFtdcFutureSignIOField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
};

///期商签到响应
struct CZQThostFtdcRspFutureSignInField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
	///PIN密钥
	TZQThostFtdcPasswordKeyType	PinKey;
	///MAC密钥
	TZQThostFtdcPasswordKeyType	MacKey;
};

///期商签退请求
struct CZQThostFtdcReqFutureSignOutField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
};

///期商签退响应
struct CZQThostFtdcRspFutureSignOutField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///查询指定流水号的交易结果请求
struct CZQThostFtdcReqQueryTradeResultBySerialField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///流水号
	TZQThostFtdcSerialType	Reference;
	///本流水号发布者的机构类型
	TZQThostFtdcInstitutionTypeType	RefrenceIssureType;
	///本流水号发布者机构编码
	TZQThostFtdcOrganCodeType	RefrenceIssure;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///转帐金额
	TZQThostFtdcTradeAmountType	TradeAmount;
	///摘要
	TZQThostFtdcDigestType	Digest;
};

///查询指定流水号的交易结果响应
struct CZQThostFtdcRspQueryTradeResultBySerialField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
	///流水号
	TZQThostFtdcSerialType	Reference;
	///本流水号发布者的机构类型
	TZQThostFtdcInstitutionTypeType	RefrenceIssureType;
	///本流水号发布者机构编码
	TZQThostFtdcOrganCodeType	RefrenceIssure;
	///原始返回代码
	TZQThostFtdcReturnCodeType	OriginReturnCode;
	///原始返回码描述
	TZQThostFtdcDescrInfoForReturnCodeType	OriginDescrInfoForReturnCode;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///转帐金额
	TZQThostFtdcTradeAmountType	TradeAmount;
	///摘要
	TZQThostFtdcDigestType	Digest;
};

///日终文件就绪请求
struct CZQThostFtdcReqDayEndFileReadyField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///文件业务功能
	TZQThostFtdcFileBusinessCodeType	FileBusinessCode;
	///摘要
	TZQThostFtdcDigestType	Digest;
};

///返回结果
struct CZQThostFtdcReturnResultField
{
	///返回代码
	TZQThostFtdcReturnCodeType	ReturnCode;
	///返回码描述
	TZQThostFtdcDescrInfoForReturnCodeType	DescrInfoForReturnCode;
};

///验证期货资金密码
struct CZQThostFtdcVerifyFuturePasswordField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///交易ID
	TZQThostFtdcTIDType	TID;
};

///验证客户信息
struct CZQThostFtdcVerifyCustInfoField
{
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
};

///验证期货资金密码和客户信息
struct CZQThostFtdcVerifyFuturePasswordAndCustInfoField
{
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
};

///验证期货资金密码和客户信息
struct CZQThostFtdcDepositResultInformField
{
	///出入金流水号，该流水号为银期报盘返回的流水号
	TZQThostFtdcDepositSeqNoType	DepositSeqNo;
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///入金金额
	TZQThostFtdcMoneyType	Deposit;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///返回代码
	TZQThostFtdcReturnCodeType	ReturnCode;
	///返回码描述
	TZQThostFtdcDescrInfoForReturnCodeType	DescrInfoForReturnCode;
};

///交易核心向银期报盘发出密钥同步请求
struct CZQThostFtdcReqSyncKeyField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///交易核心给银期报盘的消息
	TZQThostFtdcAddInfoType	Message;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
};

///交易核心向银期报盘发出密钥同步响应
struct CZQThostFtdcRspSyncKeyField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///交易核心给银期报盘的消息
	TZQThostFtdcAddInfoType	Message;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///查询账户信息通知
struct CZQThostFtdcNotifyQueryAccountField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///客户姓名
	TZQThostFtdcIndividualNameType	CustomerName;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///客户类型
	TZQThostFtdcCustTypeType	CustType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行密码
	TZQThostFtdcPasswordType	BankPassWord;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///期货密码
	TZQThostFtdcPasswordType	Password;
	///期货公司流水号
	TZQThostFtdcFutureSerialType	FutureSerial;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///验证客户证件号码标志
	TZQThostFtdcYesNoIndicatorType	VerifyCertNoFlag;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货单位帐号类型
	TZQThostFtdcBankAccTypeType	BankSecuAccType;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///期货单位帐号
	TZQThostFtdcBankAccountType	BankSecuAcc;
	///银行密码标志
	TZQThostFtdcPwdFlagType	BankPwdFlag;
	///期货资金密码核对标志
	TZQThostFtdcPwdFlagType	SecuPwdFlag;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///银行可用金额
	TZQThostFtdcTradeAmountType	BankUseAmount;
	///银行可取金额
	TZQThostFtdcTradeAmountType	BankFetchAmount;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///银期转账交易流水表
struct CZQThostFtdcTransferSerialField
{
	///平台流水号
	TZQThostFtdcPlateSerialType	PlateSerial;
	///交易发起方日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易日期
	TZQThostFtdcDateType	TradingDay;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///交易代码
	TZQThostFtdcTradeCodeType	TradeCode;
	///会话编号
	TZQThostFtdcSessionIDType	SessionID;
	///银行编码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构编码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///银行帐号类型
	TZQThostFtdcBankAccTypeType	BankAccType;
	///银行帐号
	TZQThostFtdcBankAccountType	BankAccount;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///期货公司编码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///期货公司帐号类型
	TZQThostFtdcFutureAccTypeType	FutureAccType;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///期货公司流水号
	TZQThostFtdcFutureSerialType	FutureSerial;
	///证件类型
	TZQThostFtdcIdCardTypeType	IdCardType;
	///证件号码
	TZQThostFtdcIdentifiedCardNoType	IdentifiedCardNo;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///交易金额
	TZQThostFtdcTradeAmountType	TradeAmount;
	///应收客户费用
	TZQThostFtdcCustFeeType	CustFee;
	///应收期货公司费用
	TZQThostFtdcFutureFeeType	BrokerFee;
	///有效标志
	TZQThostFtdcAvailabilityFlagType	AvailabilityFlag;
	///操作员
	TZQThostFtdcOperatorCodeType	OperatorCode;
	///新银行帐号
	TZQThostFtdcBankAccountType	BankNewAccount;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///请求查询转帐流水
struct CZQThostFtdcQryTransferSerialField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者帐号
	TZQThostFtdcAccountIDType	AccountID;
	///银行编码
	TZQThostFtdcBankIDType	BankID;
};

///期商签到通知
struct CZQThostFtdcNotifyFutureSignInField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
	///PIN密钥
	TZQThostFtdcPasswordKeyType	PinKey;
	///MAC密钥
	TZQThostFtdcPasswordKeyType	MacKey;
};

///期商签退通知
struct CZQThostFtdcNotifyFutureSignOutField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///摘要
	TZQThostFtdcDigestType	Digest;
	///币种代码
	TZQThostFtdcCurrencyIDType	CurrencyID;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///交易核心向银期报盘发出密钥同步处理结果的通知
struct CZQThostFtdcNotifySyncKeyField
{
	///业务功能码
	TZQThostFtdcTradeCodeType	TradeCode;
	///银行代码
	TZQThostFtdcBankIDType	BankID;
	///银行分支机构代码
	TZQThostFtdcBankBrchIDType	BankBranchID;
	///期商代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///期商分支机构代码
	TZQThostFtdcFutureBranchIDType	BrokerBranchID;
	///交易日期
	TZQThostFtdcTradeDateType	TradeDate;
	///交易时间
	TZQThostFtdcTradeTimeType	TradeTime;
	///银行流水号
	TZQThostFtdcBankSerialType	BankSerial;
	///交易系统日期 
	TZQThostFtdcTradeDateType	TradingDay;
	///银期平台消息流水号
	TZQThostFtdcSerialType	PlateSerial;
	///最后分片标志
	TZQThostFtdcLastFragmentType	LastFragment;
	///会话号
	TZQThostFtdcSessionIDType	SessionID;
	///安装编号
	TZQThostFtdcInstallIDType	InstallID;
	///用户标识
	TZQThostFtdcUserIDType	UserID;
	///交易核心给银期报盘的消息
	TZQThostFtdcAddInfoType	Message;
	///渠道标志
	TZQThostFtdcDeviceIDType	DeviceID;
	///期货公司银行编码
	TZQThostFtdcBankCodingForFutureType	BrokerIDByBank;
	///交易柜员
	TZQThostFtdcOperNoType	OperNo;
	///请求编号
	TZQThostFtdcRequestIDType	RequestID;
	///交易ID
	TZQThostFtdcTIDType	TID;
	///错误代码
	TZQThostFtdcErrorIDType	ErrorID;
	///错误信息
	TZQThostFtdcErrorMsgType	ErrorMsg;
};

///客户最大持仓数量
struct CZQThostFtdcMaxStockPositionAmountField
{
	///经纪公司代码
	TZQThostFtdcBrokerIDType	BrokerID;
	///投资者代码
	TZQThostFtdcInvestorIDType	InvestorID;
	///合约代码
	TZQThostFtdcInstrumentIDType	InstrumentID;
	///最大持仓数量
	TZQThostFtdcVolumeType	MaxAmount;
};


_SHFE_NS_STOCK_END_
#endif
