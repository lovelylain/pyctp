# -*- coding: utf-8 -*-

from cLevel2ApiDataType cimport *

cdef extern from "ThostFtdcLevel2UserApiStruct.h":
    cdef struct CRspInfoField "CThostFtdcRspInfoField": #响应信息
        TErrorIDType ErrorID #错误代码, int
        TErrorMsgType ErrorMsg #错误信息, char[81]
    cdef struct CDisseminationField "CThostFtdcDisseminationField": #信息分发
        TSequenceSeriesType SequenceSeries #序列系列号, short
        TSequenceNoType SequenceNo #序列号, int
    cdef struct CReqUserLoginField "CThostFtdcReqUserLoginField": #用户登录请求
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
    cdef struct CRspUserLoginField "CThostFtdcRspUserLoginField": #用户登录应答
        TDateType TradingDay #交易日, char[9]
        TTimeType LoginTime #登录成功时间, char[9]
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TSystemNameType SystemName #交易系统名称, char[41]
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
        TTimeType SSETime #上证所时间, char[9]
        TTimeType SZETime #深证所时间, char[9]
    cdef struct CUserLogoutField "CThostFtdcUserLogoutField": #用户登出请求
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
    cdef struct CUserSessionRefField "CThostFtdcUserSessionRefField": #用户会话
        TFrontIDType FrontID #前置编号, int
        TSessionIDType SessionID #会话编号, int
    cdef struct CReqAuthenticateField "CThostFtdcReqAuthenticateField": #客户端认证请求
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TProductInfoType UserProductInfo #用户端产品信息, char[11]
        TAuthCodeType AuthCode #认证码, char[17]
    cdef struct CRspAuthenticateField "CThostFtdcRspAuthenticateField": #客户端认证响应
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TProductInfoType UserProductInfo #用户端产品信息, char[11]
    cdef struct CAuthenticationInfoField "CThostFtdcAuthenticationInfoField": #客户端认证信息
        TBrokerIDType BrokerID #经纪公司代码, char[11]
        TUserIDType UserID #用户代码, char[16]
        TProductInfoType UserProductInfo #用户端产品信息, char[11]
        TAuthInfoType AuthInfo #认证信息, char[129]
        TBoolType IsResult #是否为认证结果, int
    cdef struct CLevel2UserField "CThostFtdcLevel2UserField": #用户信息
        TUserIDType UserID #用户代码, char[16]
        TUserNameType UserName #用户名称, char[81]
        TPasswordType Password #密码, char[41]
        TDateType EffectiveDate #启用日期, char[9]
    cdef struct CSpecificSecurityField "CThostFtdcSpecificSecurityField": #指定的证券
        TSecurityIDType SecurityID #证券代码, char[13]
        TExchangeIDType ExchangeID #交易所代码, char[9]
    cdef struct CLevel2MarketDataField "CThostFtdcLevel2MarketDataField": #Level2行情
        TDateType TradingDay #交易日, char[9]
        TTimeType DataTimeStamp #时间戳, char[9]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TSecurityIDType SecurityID #证券代码, char[13]
        TPriceType PreClosePx #昨收盘价, double
        TPriceType OpenPx #今开盘价, double
        TPriceType HighPx #最高价, double
        TPriceType LowPx #最低价, double
        TPriceType LastPx #现价, double
        TPriceType ClosePx #收盘价, double
        TVolumeType NumTrades #成交笔数, int
        TLargeVolumeType TotalVolumeTrade #成交总量, double
        TMoneyType TotalValueTrade #成交总金额, double
        TLargeVolumeType TotalBidQty #委托买入总量, double
        TPriceType WeightedAvgBidPx #加权平均委买价, double
        TPriceType AltWeightedAvgBidPx #债券加权平均委买价, double
        TLargeVolumeType TotalOfferQty #委托卖出总量, double
        TPriceType WeightedAvgOfferPx #加权平均委卖价, double
        TPriceType AltWeightedAvgOfferPx #债券加权平均委卖价格, double
        TPriceType IOPV #净值估值, double
        TRatioType YieldToMaturity #到期收益率, double
        TLargeVolumeType TotalWarrantExecQty #权证执行总数量, double
        TPriceType WarLowerPx #权证跌停价格, double
        TPriceType WarUpperPx #权证涨停价格, double
        TPriceLevelType BidPriceLevel #买价深度, int
        TPriceType BidPx1 #申买价一, double
        TVolumeType BidOrderQty1 #申买量一, int
        TVolumeType BidNumOrder1 #实际买总委托笔数一, int
        TPriceType BidPx2 #申买价二, double
        TVolumeType BidOrderQty2 #申买量二, int
        TVolumeType BidNumOrder2 #实际买总委托笔数二, int
        TPriceType BidPx3 #申买价三, double
        TVolumeType BidOrderQty3 #申买量三, int
        TVolumeType BidNumOrder3 #实际买总委托笔数三, int
        TPriceType BidPx4 #申买价四, double
        TVolumeType BidOrderQty4 #申买量四, int
        TVolumeType BidNumOrder4 #实际买总委托笔数四, int
        TPriceType BidPx5 #申买价五, double
        TVolumeType BidOrderQty5 #申买量五, int
        TVolumeType BidNumOrder5 #实际买总委托笔数五, int
        TPriceType BidPx6 #申买价六, double
        TVolumeType BidOrderQty6 #申买量六, int
        TVolumeType BidNumOrder6 #实际买总委托笔数六, int
        TPriceType BidPx7 #申买价七, double
        TVolumeType BidOrderQty7 #申买量七, int
        TVolumeType BidNumOrder7 #实际买总委托笔数七, int
        TPriceType BidPx8 #申买价八, double
        TVolumeType BidOrderQty8 #申买量八, int
        TVolumeType BidNumOrder8 #实际买总委托笔数八, int
        TPriceType BidPx9 #申买价九, double
        TVolumeType BidOrderQty9 #申买量九, int
        TVolumeType BidNumOrder9 #实际买总委托笔数九, int
        TPriceType BidPxA #申买价十, double
        TVolumeType BidOrderQtyA #申买量十, int
        TVolumeType BidNumOrderA #实际买总委托笔数十, int
        TPriceLevelType OfferPriceLevel #卖价深度, int
        TPriceType OfferPx1 #申卖价一, double
        TVolumeType OfferOrderQty1 #申卖量一, int
        TVolumeType OfferNumOrder1 #实际卖总委托笔数一, int
        TPriceType OfferPx2 #申卖价二, double
        TVolumeType OfferOrderQty2 #申卖量二, int
        TVolumeType OfferNumOrder2 #实际卖总委托笔数二, int
        TPriceType OfferPx3 #申卖价三, double
        TVolumeType OfferOrderQty3 #申卖量三, int
        TVolumeType OfferNumOrder3 #实际卖总委托笔数三, int
        TPriceType OfferPx4 #申卖价四, double
        TVolumeType OfferOrderQty4 #申卖量四, int
        TVolumeType OfferNumOrder4 #实际卖总委托笔数四, int
        TPriceType OfferPx5 #申卖价五, double
        TVolumeType OfferOrderQty5 #申卖量五, int
        TVolumeType OfferNumOrder5 #实际卖总委托笔数五, int
        TPriceType OfferPx6 #申卖价六, double
        TVolumeType OfferOrderQty6 #申卖量六, int
        TVolumeType OfferNumOrder6 #实际卖总委托笔数六, int
        TPriceType OfferPx7 #申卖价七, double
        TVolumeType OfferOrderQty7 #申卖量七, int
        TVolumeType OfferNumOrder7 #实际卖总委托笔数七, int
        TPriceType OfferPx8 #申卖价八, double
        TVolumeType OfferOrderQty8 #申卖量八, int
        TVolumeType OfferNumOrder8 #实际卖总委托笔数八, int
        TPriceType OfferPx9 #申卖价九, double
        TVolumeType OfferOrderQty9 #申卖量九, int
        TVolumeType OfferNumOrder9 #实际卖总委托笔数九, int
        TPriceType OfferPxA #申卖价十, double
        TVolumeType OfferOrderQtyA #申卖量十, int
        TVolumeType OfferNumOrderA #实际卖总委托笔数十, int
    cdef struct CL2MarketDataUpdateTimeField "CThostFtdcL2MarketDataUpdateTimeField": #Level2行情更新时间属性
        TDateType TradingDay #交易日, char[9]
        TTimeType DataTimeStamp #时间戳, char[9]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TSecurityIDType SecurityID #证券代码, char[13]
    cdef struct CL2MarketDataBid1Field "CThostFtdcL2MarketDataBid1Field": #Level2行情申买一属性
        TPriceType BidPx1 #申买价一, double
        TVolumeType BidOrderQty1 #申买量一, int
        TVolumeType BidNumOrder1 #实际买总委托笔数一, int
    cdef struct CL2MarketDataOffer1Field "CThostFtdcL2MarketDataOffer1Field": #Level2行情申卖一属性
        TPriceType OfferPx1 #申卖价一, double
        TVolumeType OfferOrderQty1 #申卖量一, int
        TVolumeType OfferNumOrder1 #实际卖总委托笔数一, int
    cdef struct CL2MarketDataBid2Field "CThostFtdcL2MarketDataBid2Field": #Level2行情申买二属性
        TPriceType BidPx2 #申买价二, double
        TVolumeType BidOrderQty2 #申买量二, int
        TVolumeType BidNumOrder2 #实际买总委托笔数二, int
    cdef struct CL2MarketDataOffer2Field "CThostFtdcL2MarketDataOffer2Field": #Level2行情申卖二属性
        TPriceType OfferPx2 #申卖价二, double
        TVolumeType OfferOrderQty2 #申卖量二, int
        TVolumeType OfferNumOrder2 #实际卖总委托笔数二, int
    cdef struct CL2MarketDataBid3Field "CThostFtdcL2MarketDataBid3Field": #Level2行情申买三属性
        TPriceType BidPx3 #申买价三, double
        TVolumeType BidOrderQty3 #申买量三, int
        TVolumeType BidNumOrder3 #实际买总委托笔数三, int
    cdef struct CL2MarketDataOffer3Field "CThostFtdcL2MarketDataOffer3Field": #Level2行情申卖三属性
        TPriceType OfferPx3 #申卖价三, double
        TVolumeType OfferOrderQty3 #申卖量三, int
        TVolumeType OfferNumOrder3 #实际卖总委托笔数三, int
    cdef struct CL2MarketDataBid4Field "CThostFtdcL2MarketDataBid4Field": #Level2行情申买四属性
        TPriceType BidPx4 #申买价四, double
        TVolumeType BidOrderQty4 #申买量四, int
        TVolumeType BidNumOrder4 #实际买总委托笔数四, int
    cdef struct CL2MarketDataOffer4Field "CThostFtdcL2MarketDataOffer4Field": #Level2行情申卖四属性
        TPriceType OfferPx4 #申卖价四, double
        TVolumeType OfferOrderQty4 #申卖量四, int
        TVolumeType OfferNumOrder4 #实际卖总委托笔数四, int
    cdef struct CL2MarketDataBid5Field "CThostFtdcL2MarketDataBid5Field": #Level2行情申买五属性
        TPriceType BidPx5 #申买价五, double
        TVolumeType BidOrderQty5 #申买量五, int
        TVolumeType BidNumOrder5 #实际买总委托笔数五, int
    cdef struct CL2MarketDataOffer5Field "CThostFtdcL2MarketDataOffer5Field": #Level2行情申卖五属性
        TPriceType OfferPx5 #申卖价五, double
        TVolumeType OfferOrderQty5 #申卖量五, int
        TVolumeType OfferNumOrder5 #实际卖总委托笔数五, int
    cdef struct CL2MarketDataBid6Field "CThostFtdcL2MarketDataBid6Field": #Level2行情申买六属性
        TPriceType BidPx6 #申买价六, double
        TVolumeType BidOrderQty6 #申买量六, int
        TVolumeType BidNumOrder6 #实际买总委托笔数六, int
    cdef struct CL2MarketDataOffer6Field "CThostFtdcL2MarketDataOffer6Field": #Level2行情申卖六属性
        TPriceType OfferPx6 #申卖价六, double
        TVolumeType OfferOrderQty6 #申卖量六, int
        TVolumeType OfferNumOrder6 #实际卖总委托笔数六, int
    cdef struct CL2MarketDataBid7Field "CThostFtdcL2MarketDataBid7Field": #Level2行情申买七属性
        TPriceType BidPx7 #申买价七, double
        TVolumeType BidOrderQty7 #申买量七, int
        TVolumeType BidNumOrder7 #实际买总委托笔数七, int
    cdef struct CL2MarketDataOffer7Field "CThostFtdcL2MarketDataOffer7Field": #Level2行情申卖七属性
        TPriceType OfferPx7 #申卖价七, double
        TVolumeType OfferOrderQty7 #申卖量七, int
        TVolumeType OfferNumOrder7 #实际卖总委托笔数七, int
    cdef struct CL2MarketDataBid8Field "CThostFtdcL2MarketDataBid8Field": #Level2行情申买八属性
        TPriceType BidPx8 #申买价八, double
        TVolumeType BidOrderQty8 #申买量八, int
        TVolumeType BidNumOrder8 #实际买总委托笔数八, int
    cdef struct CL2MarketDataOffer8Field "CThostFtdcL2MarketDataOffer8Field": #Level2行情申卖八属性
        TPriceType OfferPx8 #申卖价八, double
        TVolumeType OfferOrderQty8 #申卖量八, int
        TVolumeType OfferNumOrder8 #实际卖总委托笔数八, int
    cdef struct CL2MarketDataBid9Field "CThostFtdcL2MarketDataBid9Field": #Level2行情申买九属性
        TPriceType BidPx9 #申买价九, double
        TVolumeType BidOrderQty9 #申买量九, int
        TVolumeType BidNumOrder9 #实际买总委托笔数九, int
    cdef struct CL2MarketDataOffer9Field "CThostFtdcL2MarketDataOffer9Field": #Level2行情申卖九属性
        TPriceType OfferPx9 #申卖价九, double
        TVolumeType OfferOrderQty9 #申卖量九, int
        TVolumeType OfferNumOrder9 #实际卖总委托笔数九, int
    cdef struct CL2MarketDataBidAField "CThostFtdcL2MarketDataBidAField": #Level2行情申买十属性
        TPriceType BidPxA #申买价十, double
        TVolumeType BidOrderQtyA #申买量十, int
        TVolumeType BidNumOrderA #实际买总委托笔数十, int
    cdef struct CL2MarketDataOfferAField "CThostFtdcL2MarketDataOfferAField": #Level2行情申卖十属性
        TPriceType OfferPxA #申卖价十, double
        TVolumeType OfferOrderQtyA #申卖量十, int
        TVolumeType OfferNumOrderA #实际卖总委托笔数十, int
    cdef struct CL2MarketDataTradedField "CThostFtdcL2MarketDataTradedField": #Level2成交信息
        TVolumeType NumTrades #成交笔数, int
        TLargeVolumeType TotalVolumeTrade #成交总量, double
        TMoneyType TotalValueTrade #成交总金额, double
    cdef struct CL2MarketDataBidOrderField "CThostFtdcL2MarketDataBidOrderField": #Level2委买信息
        TLargeVolumeType TotalBidQty #委托买入总量, double
        TPriceType WeightedAvgBidPx #加权平均委买价, double
        TPriceType AltWeightedAvgBidPx #债券加权平均委买价, double
    cdef struct CL2MarketDataOfferOrderField "CThostFtdcL2MarketDataOfferOrderField": #Level2委卖信息
        TLargeVolumeType TotalOfferQty #委托卖出总量, double
        TPriceType WeightedAvgOfferPx #加权平均委卖价, double
        TPriceType AltWeightedAvgOfferPx #债券加权平均委卖价格, double
    cdef struct CL2MarketDataWarrantField "CThostFtdcL2MarketDataWarrantField": #Level2权证信息
        TLargeVolumeType TotalWarrantExecQty #权证执行总数量, double
        TPriceType WarLowerPx #权证跌停价格, double
        TPriceType WarUpperPx #权证涨停价格, double
    cdef struct CL2MarketDataBaseField "CThostFtdcL2MarketDataBaseField": #Level2行情基本信息
        TPriceType LastPx #现价, double
    cdef struct CL2MarketDataStaticField "CThostFtdcL2MarketDataStaticField": #Level2行情静态属性
        TPriceType PreClosePx #昨收盘价, double
        TPriceType OpenPx #今开盘价, double
        TPriceType ClosePx #收盘价, double
        TPriceType HighPx #最高价, double
        TPriceType LowPx #最低价, double
        TPriceType IOPV #净值估值, double
        TRatioType YieldToMaturity #到期收益率, double
    cdef struct CL2MarketDataPriceLevelField "CThostFtdcL2MarketDataPriceLevelField": #Level2价格深度属性
        TPriceLevelType BidPriceLevel #买价深度, int
        TPriceLevelType OfferPriceLevel #卖价深度, int
    cdef struct CNGTSIndexField "CThostFtdcNGTSIndexField": #Level2指数行情
        TDateType TradingDay #交易日, char[9]
        TTimeType TimeStamp #行情时间（秒）, char[9]
        TExchangeIDType ExchangeID #交易所代码, char[9]
        TSecurityIDType SecurityID #指数代码, char[13]
        TIndexType PreCloseIndex #前收盘指数, double
        TIndexType OpenIndex #今开盘指数, double
        TMoneyType TurnOver #参与计算相应指数的成交金额（元）, double
        TIndexType HighIndex #最高指数, double
        TIndexType LowIndex #最低指数, double
        TIndexType LastIndex #最新指数, double
        TIndexType CloseIndex #今日收盘指数, double
        TTimeType TradeTime #成交时间, char[9]
        TLargeVolumeType TotalVolumeTraded #参与计算相应指数的交易数量（手）, double
