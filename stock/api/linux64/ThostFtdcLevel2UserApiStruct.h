/////////////////////////////////////////////////////////////////////////
///@system Level2行情API
///@company 上海期货信息技术有限公司
///@file ThostFtdcUserApiStruct.h
///@brief 定义了客户端接口使用的业务数据结构
///@history 
///20060106	赵鸿昊		创建该文件
/////////////////////////////////////////////////////////////////////////
#ifndef THOST_FTDCLEVEL2STRUCT_H
#define THOST_FTDCLEVEL2STRUCT_H

#include "ThostFtdcLevel2UserApiDataType.h"

_LEVEL2_NS_BEGIN_

///响应信息
struct CThostFtdcRspInfoField
{
	///错误代码
	TThostFtdcErrorIDType	ErrorID;
	///错误信息
	TThostFtdcErrorMsgType	ErrorMsg;
};

///信息分发
struct CThostFtdcDisseminationField
{
	///序列系列号
	TThostFtdcSequenceSeriesType	SequenceSeries;
	///序列号
	TThostFtdcSequenceNoType	SequenceNo;
};

///用户登录请求
struct CThostFtdcReqUserLoginField
{
	///交易日
	TThostFtdcDateType	TradingDay;
	///经纪公司代码
	TThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TThostFtdcUserIDType	UserID;
	///密码
	TThostFtdcPasswordType	Password;
	///用户端产品信息
	TThostFtdcProductInfoType	UserProductInfo;
	///接口端产品信息
	TThostFtdcProductInfoType	InterfaceProductInfo;
	///协议信息
	TThostFtdcProtocolInfoType	ProtocolInfo;
	///Mac地址
	TThostFtdcMacAddressType	MacAddress;
	///动态密码
	TThostFtdcPasswordType	OneTimePassword;
	///终端IP地址
	TThostFtdcIPAddressType	ClientIPAddress;
};

///用户登录应答
struct CThostFtdcRspUserLoginField
{
	///交易日
	TThostFtdcDateType	TradingDay;
	///登录成功时间
	TThostFtdcTimeType	LoginTime;
	///经纪公司代码
	TThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TThostFtdcUserIDType	UserID;
	///交易系统名称
	TThostFtdcSystemNameType	SystemName;
	///前置编号
	TThostFtdcFrontIDType	FrontID;
	///会话编号
	TThostFtdcSessionIDType	SessionID;
	///上证所时间
	TThostFtdcTimeType	SSETime;
	///深证所时间
	TThostFtdcTimeType	SZETime;
};

///用户登出请求
struct CThostFtdcUserLogoutField
{
	///经纪公司代码
	TThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TThostFtdcUserIDType	UserID;
};

///用户会话
struct CThostFtdcUserSessionRefField
{
	///前置编号
	TThostFtdcFrontIDType	FrontID;
	///会话编号
	TThostFtdcSessionIDType	SessionID;
};

///客户端认证请求
struct CThostFtdcReqAuthenticateField
{
	///经纪公司代码
	TThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TThostFtdcUserIDType	UserID;
	///用户端产品信息
	TThostFtdcProductInfoType	UserProductInfo;
	///认证码
	TThostFtdcAuthCodeType	AuthCode;
};

///客户端认证响应
struct CThostFtdcRspAuthenticateField
{
	///经纪公司代码
	TThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TThostFtdcUserIDType	UserID;
	///用户端产品信息
	TThostFtdcProductInfoType	UserProductInfo;
};

///客户端认证信息
struct CThostFtdcAuthenticationInfoField
{
	///经纪公司代码
	TThostFtdcBrokerIDType	BrokerID;
	///用户代码
	TThostFtdcUserIDType	UserID;
	///用户端产品信息
	TThostFtdcProductInfoType	UserProductInfo;
	///认证信息
	TThostFtdcAuthInfoType	AuthInfo;
	///是否为认证结果
	TThostFtdcBoolType	IsResult;
};

///用户信息
struct CThostFtdcLevel2UserField
{
	///用户代码
	TThostFtdcUserIDType	UserID;
	///用户名称
	TThostFtdcUserNameType	UserName;
	///密码
	TThostFtdcPasswordType	Password;
	///启用日期
	TThostFtdcDateType	EffectiveDate;
};

///指定的证券
struct CThostFtdcSpecificSecurityField
{
	///证券代码
	TThostFtdcSecurityIDType	SecurityID;
	///交易所代码
	TThostFtdcExchangeIDType	ExchangeID;
};

///Level2行情
struct CThostFtdcLevel2MarketDataField
{
	///交易日
	TThostFtdcDateType	TradingDay;
	///时间戳
	TThostFtdcTimeType	DataTimeStamp;
	///交易所代码
	TThostFtdcExchangeIDType	ExchangeID;
	///证券代码
	TThostFtdcSecurityIDType	SecurityID;
	///昨收盘价
	TThostFtdcPriceType	PreClosePx;
	///今开盘价
	TThostFtdcPriceType	OpenPx;
	///最高价
	TThostFtdcPriceType	HighPx;
	///最低价
	TThostFtdcPriceType	LowPx;
	///现价
	TThostFtdcPriceType	LastPx;
	///收盘价
	TThostFtdcPriceType	ClosePx;
	///成交笔数
	TThostFtdcVolumeType	NumTrades;
	///成交总量
	TThostFtdcLargeVolumeType	TotalVolumeTrade;
	///成交总金额
	TThostFtdcMoneyType	TotalValueTrade;
	///委托买入总量
	TThostFtdcLargeVolumeType	TotalBidQty;
	///加权平均委买价
	TThostFtdcPriceType	WeightedAvgBidPx;
	///债券加权平均委买价
	TThostFtdcPriceType	AltWeightedAvgBidPx;
	///委托卖出总量
	TThostFtdcLargeVolumeType	TotalOfferQty;
	///加权平均委卖价
	TThostFtdcPriceType	WeightedAvgOfferPx;
	///债券加权平均委卖价格
	TThostFtdcPriceType	AltWeightedAvgOfferPx;
	///净值估值
	TThostFtdcPriceType	IOPV;
	///到期收益率
	TThostFtdcRatioType	YieldToMaturity;
	///权证执行总数量
	TThostFtdcLargeVolumeType	TotalWarrantExecQty;
	///权证跌停价格
	TThostFtdcPriceType	WarLowerPx;
	///权证涨停价格
	TThostFtdcPriceType	WarUpperPx;
	///买价深度
	TThostFtdcPriceLevelType	BidPriceLevel;
	///申买价一
	TThostFtdcPriceType	BidPx1;
	///申买量一
	TThostFtdcVolumeType	BidOrderQty1;
	///实际买总委托笔数一
	TThostFtdcVolumeType	BidNumOrder1;
	///申买价二
	TThostFtdcPriceType	BidPx2;
	///申买量二
	TThostFtdcVolumeType	BidOrderQty2;
	///实际买总委托笔数二
	TThostFtdcVolumeType	BidNumOrder2;
	///申买价三
	TThostFtdcPriceType	BidPx3;
	///申买量三
	TThostFtdcVolumeType	BidOrderQty3;
	///实际买总委托笔数三
	TThostFtdcVolumeType	BidNumOrder3;
	///申买价四
	TThostFtdcPriceType	BidPx4;
	///申买量四
	TThostFtdcVolumeType	BidOrderQty4;
	///实际买总委托笔数四
	TThostFtdcVolumeType	BidNumOrder4;
	///申买价五
	TThostFtdcPriceType	BidPx5;
	///申买量五
	TThostFtdcVolumeType	BidOrderQty5;
	///实际买总委托笔数五
	TThostFtdcVolumeType	BidNumOrder5;
	///申买价六
	TThostFtdcPriceType	BidPx6;
	///申买量六
	TThostFtdcVolumeType	BidOrderQty6;
	///实际买总委托笔数六
	TThostFtdcVolumeType	BidNumOrder6;
	///申买价七
	TThostFtdcPriceType	BidPx7;
	///申买量七
	TThostFtdcVolumeType	BidOrderQty7;
	///实际买总委托笔数七
	TThostFtdcVolumeType	BidNumOrder7;
	///申买价八
	TThostFtdcPriceType	BidPx8;
	///申买量八
	TThostFtdcVolumeType	BidOrderQty8;
	///实际买总委托笔数八
	TThostFtdcVolumeType	BidNumOrder8;
	///申买价九
	TThostFtdcPriceType	BidPx9;
	///申买量九
	TThostFtdcVolumeType	BidOrderQty9;
	///实际买总委托笔数九
	TThostFtdcVolumeType	BidNumOrder9;
	///申买价十
	TThostFtdcPriceType	BidPxA;
	///申买量十
	TThostFtdcVolumeType	BidOrderQtyA;
	///实际买总委托笔数十
	TThostFtdcVolumeType	BidNumOrderA;
	///卖价深度
	TThostFtdcPriceLevelType	OfferPriceLevel;
	///申卖价一
	TThostFtdcPriceType	OfferPx1;
	///申卖量一
	TThostFtdcVolumeType	OfferOrderQty1;
	///实际卖总委托笔数一
	TThostFtdcVolumeType	OfferNumOrder1;
	///申卖价二
	TThostFtdcPriceType	OfferPx2;
	///申卖量二
	TThostFtdcVolumeType	OfferOrderQty2;
	///实际卖总委托笔数二
	TThostFtdcVolumeType	OfferNumOrder2;
	///申卖价三
	TThostFtdcPriceType	OfferPx3;
	///申卖量三
	TThostFtdcVolumeType	OfferOrderQty3;
	///实际卖总委托笔数三
	TThostFtdcVolumeType	OfferNumOrder3;
	///申卖价四
	TThostFtdcPriceType	OfferPx4;
	///申卖量四
	TThostFtdcVolumeType	OfferOrderQty4;
	///实际卖总委托笔数四
	TThostFtdcVolumeType	OfferNumOrder4;
	///申卖价五
	TThostFtdcPriceType	OfferPx5;
	///申卖量五
	TThostFtdcVolumeType	OfferOrderQty5;
	///实际卖总委托笔数五
	TThostFtdcVolumeType	OfferNumOrder5;
	///申卖价六
	TThostFtdcPriceType	OfferPx6;
	///申卖量六
	TThostFtdcVolumeType	OfferOrderQty6;
	///实际卖总委托笔数六
	TThostFtdcVolumeType	OfferNumOrder6;
	///申卖价七
	TThostFtdcPriceType	OfferPx7;
	///申卖量七
	TThostFtdcVolumeType	OfferOrderQty7;
	///实际卖总委托笔数七
	TThostFtdcVolumeType	OfferNumOrder7;
	///申卖价八
	TThostFtdcPriceType	OfferPx8;
	///申卖量八
	TThostFtdcVolumeType	OfferOrderQty8;
	///实际卖总委托笔数八
	TThostFtdcVolumeType	OfferNumOrder8;
	///申卖价九
	TThostFtdcPriceType	OfferPx9;
	///申卖量九
	TThostFtdcVolumeType	OfferOrderQty9;
	///实际卖总委托笔数九
	TThostFtdcVolumeType	OfferNumOrder9;
	///申卖价十
	TThostFtdcPriceType	OfferPxA;
	///申卖量十
	TThostFtdcVolumeType	OfferOrderQtyA;
	///实际卖总委托笔数十
	TThostFtdcVolumeType	OfferNumOrderA;
};

///Level2行情更新时间属性
struct CThostFtdcL2MarketDataUpdateTimeField
{
	///交易日
	TThostFtdcDateType	TradingDay;
	///时间戳
	TThostFtdcTimeType	DataTimeStamp;
	///交易所代码
	TThostFtdcExchangeIDType	ExchangeID;
	///证券代码
	TThostFtdcSecurityIDType	SecurityID;
};

///Level2行情申买一属性
struct CThostFtdcL2MarketDataBid1Field
{
	///申买价一
	TThostFtdcPriceType	BidPx1;
	///申买量一
	TThostFtdcVolumeType	BidOrderQty1;
	///实际买总委托笔数一
	TThostFtdcVolumeType	BidNumOrder1;
};

///Level2行情申卖一属性
struct CThostFtdcL2MarketDataOffer1Field
{
	///申卖价一
	TThostFtdcPriceType	OfferPx1;
	///申卖量一
	TThostFtdcVolumeType	OfferOrderQty1;
	///实际卖总委托笔数一
	TThostFtdcVolumeType	OfferNumOrder1;
};

///Level2行情申买二属性
struct CThostFtdcL2MarketDataBid2Field
{
	///申买价二
	TThostFtdcPriceType	BidPx2;
	///申买量二
	TThostFtdcVolumeType	BidOrderQty2;
	///实际买总委托笔数二
	TThostFtdcVolumeType	BidNumOrder2;
};

///Level2行情申卖二属性
struct CThostFtdcL2MarketDataOffer2Field
{
	///申卖价二
	TThostFtdcPriceType	OfferPx2;
	///申卖量二
	TThostFtdcVolumeType	OfferOrderQty2;
	///实际卖总委托笔数二
	TThostFtdcVolumeType	OfferNumOrder2;
};

///Level2行情申买三属性
struct CThostFtdcL2MarketDataBid3Field
{
	///申买价三
	TThostFtdcPriceType	BidPx3;
	///申买量三
	TThostFtdcVolumeType	BidOrderQty3;
	///实际买总委托笔数三
	TThostFtdcVolumeType	BidNumOrder3;
};

///Level2行情申卖三属性
struct CThostFtdcL2MarketDataOffer3Field
{
	///申卖价三
	TThostFtdcPriceType	OfferPx3;
	///申卖量三
	TThostFtdcVolumeType	OfferOrderQty3;
	///实际卖总委托笔数三
	TThostFtdcVolumeType	OfferNumOrder3;
};

///Level2行情申买四属性
struct CThostFtdcL2MarketDataBid4Field
{
	///申买价四
	TThostFtdcPriceType	BidPx4;
	///申买量四
	TThostFtdcVolumeType	BidOrderQty4;
	///实际买总委托笔数四
	TThostFtdcVolumeType	BidNumOrder4;
};

///Level2行情申卖四属性
struct CThostFtdcL2MarketDataOffer4Field
{
	///申卖价四
	TThostFtdcPriceType	OfferPx4;
	///申卖量四
	TThostFtdcVolumeType	OfferOrderQty4;
	///实际卖总委托笔数四
	TThostFtdcVolumeType	OfferNumOrder4;
};

///Level2行情申买五属性
struct CThostFtdcL2MarketDataBid5Field
{
	///申买价五
	TThostFtdcPriceType	BidPx5;
	///申买量五
	TThostFtdcVolumeType	BidOrderQty5;
	///实际买总委托笔数五
	TThostFtdcVolumeType	BidNumOrder5;
};

///Level2行情申卖五属性
struct CThostFtdcL2MarketDataOffer5Field
{
	///申卖价五
	TThostFtdcPriceType	OfferPx5;
	///申卖量五
	TThostFtdcVolumeType	OfferOrderQty5;
	///实际卖总委托笔数五
	TThostFtdcVolumeType	OfferNumOrder5;
};

///Level2行情申买六属性
struct CThostFtdcL2MarketDataBid6Field
{
	///申买价六
	TThostFtdcPriceType	BidPx6;
	///申买量六
	TThostFtdcVolumeType	BidOrderQty6;
	///实际买总委托笔数六
	TThostFtdcVolumeType	BidNumOrder6;
};

///Level2行情申卖六属性
struct CThostFtdcL2MarketDataOffer6Field
{
	///申卖价六
	TThostFtdcPriceType	OfferPx6;
	///申卖量六
	TThostFtdcVolumeType	OfferOrderQty6;
	///实际卖总委托笔数六
	TThostFtdcVolumeType	OfferNumOrder6;
};

///Level2行情申买七属性
struct CThostFtdcL2MarketDataBid7Field
{
	///申买价七
	TThostFtdcPriceType	BidPx7;
	///申买量七
	TThostFtdcVolumeType	BidOrderQty7;
	///实际买总委托笔数七
	TThostFtdcVolumeType	BidNumOrder7;
};

///Level2行情申卖七属性
struct CThostFtdcL2MarketDataOffer7Field
{
	///申卖价七
	TThostFtdcPriceType	OfferPx7;
	///申卖量七
	TThostFtdcVolumeType	OfferOrderQty7;
	///实际卖总委托笔数七
	TThostFtdcVolumeType	OfferNumOrder7;
};

///Level2行情申买八属性
struct CThostFtdcL2MarketDataBid8Field
{
	///申买价八
	TThostFtdcPriceType	BidPx8;
	///申买量八
	TThostFtdcVolumeType	BidOrderQty8;
	///实际买总委托笔数八
	TThostFtdcVolumeType	BidNumOrder8;
};

///Level2行情申卖八属性
struct CThostFtdcL2MarketDataOffer8Field
{
	///申卖价八
	TThostFtdcPriceType	OfferPx8;
	///申卖量八
	TThostFtdcVolumeType	OfferOrderQty8;
	///实际卖总委托笔数八
	TThostFtdcVolumeType	OfferNumOrder8;
};

///Level2行情申买九属性
struct CThostFtdcL2MarketDataBid9Field
{
	///申买价九
	TThostFtdcPriceType	BidPx9;
	///申买量九
	TThostFtdcVolumeType	BidOrderQty9;
	///实际买总委托笔数九
	TThostFtdcVolumeType	BidNumOrder9;
};

///Level2行情申卖九属性
struct CThostFtdcL2MarketDataOffer9Field
{
	///申卖价九
	TThostFtdcPriceType	OfferPx9;
	///申卖量九
	TThostFtdcVolumeType	OfferOrderQty9;
	///实际卖总委托笔数九
	TThostFtdcVolumeType	OfferNumOrder9;
};

///Level2行情申买十属性
struct CThostFtdcL2MarketDataBidAField
{
	///申买价十
	TThostFtdcPriceType	BidPxA;
	///申买量十
	TThostFtdcVolumeType	BidOrderQtyA;
	///实际买总委托笔数十
	TThostFtdcVolumeType	BidNumOrderA;
};

///Level2行情申卖十属性
struct CThostFtdcL2MarketDataOfferAField
{
	///申卖价十
	TThostFtdcPriceType	OfferPxA;
	///申卖量十
	TThostFtdcVolumeType	OfferOrderQtyA;
	///实际卖总委托笔数十
	TThostFtdcVolumeType	OfferNumOrderA;
};

///Level2成交信息
struct CThostFtdcL2MarketDataTradedField
{
	///成交笔数
	TThostFtdcVolumeType	NumTrades;
	///成交总量
	TThostFtdcLargeVolumeType	TotalVolumeTrade;
	///成交总金额
	TThostFtdcMoneyType	TotalValueTrade;
};

///Level2委买信息
struct CThostFtdcL2MarketDataBidOrderField
{
	///委托买入总量
	TThostFtdcLargeVolumeType	TotalBidQty;
	///加权平均委买价
	TThostFtdcPriceType	WeightedAvgBidPx;
	///债券加权平均委买价
	TThostFtdcPriceType	AltWeightedAvgBidPx;
};

///Level2委卖信息
struct CThostFtdcL2MarketDataOfferOrderField
{
	///委托卖出总量
	TThostFtdcLargeVolumeType	TotalOfferQty;
	///加权平均委卖价
	TThostFtdcPriceType	WeightedAvgOfferPx;
	///债券加权平均委卖价格
	TThostFtdcPriceType	AltWeightedAvgOfferPx;
};

///Level2权证信息
struct CThostFtdcL2MarketDataWarrantField
{
	///权证执行总数量
	TThostFtdcLargeVolumeType	TotalWarrantExecQty;
	///权证跌停价格
	TThostFtdcPriceType	WarLowerPx;
	///权证涨停价格
	TThostFtdcPriceType	WarUpperPx;
};

///Level2行情基本信息
struct CThostFtdcL2MarketDataBaseField
{
	///现价
	TThostFtdcPriceType	LastPx;
};

///Level2行情静态属性
struct CThostFtdcL2MarketDataStaticField
{
	///昨收盘价
	TThostFtdcPriceType	PreClosePx;
	///今开盘价
	TThostFtdcPriceType	OpenPx;
	///收盘价
	TThostFtdcPriceType	ClosePx;
	///最高价
	TThostFtdcPriceType	HighPx;
	///最低价
	TThostFtdcPriceType	LowPx;
	///净值估值
	TThostFtdcPriceType	IOPV;
	///到期收益率
	TThostFtdcRatioType	YieldToMaturity;
};

///Level2价格深度属性
struct CThostFtdcL2MarketDataPriceLevelField
{
	///买价深度
	TThostFtdcPriceLevelType	BidPriceLevel;
	///卖价深度
	TThostFtdcPriceLevelType	OfferPriceLevel;
};

///Level2指数行情
struct CThostFtdcNGTSIndexField
{
	///交易日
	TThostFtdcDateType	TradingDay;
	///行情时间（秒）
	TThostFtdcTimeType	TimeStamp;
	///交易所代码
	TThostFtdcExchangeIDType	ExchangeID;
	///指数代码
	TThostFtdcSecurityIDType	SecurityID;
	///前收盘指数
	TThostFtdcIndexType	PreCloseIndex;
	///今开盘指数
	TThostFtdcIndexType	OpenIndex;
	///参与计算相应指数的成交金额（元）
	TThostFtdcMoneyType	TurnOver;
	///最高指数
	TThostFtdcIndexType	HighIndex;
	///最低指数
	TThostFtdcIndexType	LowIndex;
	///最新指数
	TThostFtdcIndexType	LastIndex;
	///今日收盘指数
	TThostFtdcIndexType	CloseIndex;
	///成交时间
	TThostFtdcTimeType	TradeTime;
	///参与计算相应指数的交易数量（手）
	TThostFtdcLargeVolumeType	TotalVolumeTraded;
};


_LEVEL2_NS_END_

#endif
