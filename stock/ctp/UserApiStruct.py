# -*- coding: utf-8 -*-

from __future__ import absolute_import as _init

TERT_RESTART = 0 #从本交易日开始重传
TERT_RESUME = 1 #从上次收到的续传
TERT_QUICK = 2 #只传送登录后的流内容
IS_BeforeTrading = '0' #开盘前
IS_NoTrading = '1' #非交易
IS_Continous = '2' #连续交易
IS_AuctionOrdering = '3' #集合竞价报单
IS_AuctionBalance = '4' #集合竞价价格平衡
IS_AuctionMatch = '5' #集合竞价撮合
IS_Closed = '6' #收盘

class BaseStruct(object): pass

class RspInfo(BaseStruct): #响应信息
    def __init__(self, ErrorID=0, ErrorMsg=''):
        self.ErrorID = 'TErrorID' #错误代码, int
        self.ErrorMsg = 'TErrorMsg' #错误信息, char[81]

class Dissemination(BaseStruct): #信息分发
    def __init__(self, SequenceSeries=0, SequenceNo=0):
        self.SequenceSeries = 'TSequenceSeries' #序列系列号, short
        self.SequenceNo = 'TSequenceNo' #序列号, int

class ReqUserLogin(BaseStruct): #用户登录请求
    def __init__(self, TradingDay='', BrokerID='', UserID='', Password='', UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', MacAddress='', OneTimePassword='', ClientIPAddress=''):
        self.TradingDay = 'TDate' #交易日, char[9]
        self.BrokerID = 'TBrokerID' #经纪公司代码, char[11]
        self.UserID = 'TUserID' #用户代码, char[16]
        self.Password = 'TPassword' #密码, char[41]
        self.UserProductInfo = 'TProductInfo' #用户端产品信息, char[11]
        self.InterfaceProductInfo = 'TProductInfo' #接口端产品信息, char[11]
        self.ProtocolInfo = 'TProtocolInfo' #协议信息, char[11]
        self.MacAddress = 'TMacAddress' #Mac地址, char[21]
        self.OneTimePassword = 'TPassword' #动态密码, char[41]
        self.ClientIPAddress = 'TIPAddress' #终端IP地址, char[16]

class RspUserLogin(BaseStruct): #用户登录应答
    def __init__(self, TradingDay='', LoginTime='', BrokerID='', UserID='', SystemName='', FrontID=0, SessionID=0, SSETime='', SZETime=''):
        self.TradingDay = 'TDate' #交易日, char[9]
        self.LoginTime = 'TTime' #登录成功时间, char[9]
        self.BrokerID = 'TBrokerID' #经纪公司代码, char[11]
        self.UserID = 'TUserID' #用户代码, char[16]
        self.SystemName = 'TSystemName' #交易系统名称, char[41]
        self.FrontID = 'TFrontID' #前置编号, int
        self.SessionID = 'TSessionID' #会话编号, int
        self.SSETime = 'TTime' #上证所时间, char[9]
        self.SZETime = 'TTime' #深证所时间, char[9]

class UserLogout(BaseStruct): #用户登出请求
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = 'TBrokerID' #经纪公司代码, char[11]
        self.UserID = 'TUserID' #用户代码, char[16]

class UserSessionRef(BaseStruct): #用户会话
    def __init__(self, FrontID=0, SessionID=0):
        self.FrontID = 'TFrontID' #前置编号, int
        self.SessionID = 'TSessionID' #会话编号, int

class ReqAuthenticate(BaseStruct): #客户端认证请求
    def __init__(self, BrokerID='', UserID='', UserProductInfo='', AuthCode=''):
        self.BrokerID = 'TBrokerID' #经纪公司代码, char[11]
        self.UserID = 'TUserID' #用户代码, char[16]
        self.UserProductInfo = 'TProductInfo' #用户端产品信息, char[11]
        self.AuthCode = 'TAuthCode' #认证码, char[17]

class RspAuthenticate(BaseStruct): #客户端认证响应
    def __init__(self, BrokerID='', UserID='', UserProductInfo=''):
        self.BrokerID = 'TBrokerID' #经纪公司代码, char[11]
        self.UserID = 'TUserID' #用户代码, char[16]
        self.UserProductInfo = 'TProductInfo' #用户端产品信息, char[11]

class AuthenticationInfo(BaseStruct): #客户端认证信息
    def __init__(self, BrokerID='', UserID='', UserProductInfo='', AuthInfo='', IsResult=0):
        self.BrokerID = 'TBrokerID' #经纪公司代码, char[11]
        self.UserID = 'TUserID' #用户代码, char[16]
        self.UserProductInfo = 'TProductInfo' #用户端产品信息, char[11]
        self.AuthInfo = 'TAuthInfo' #认证信息, char[129]
        self.IsResult = 'TBool' #是否为认证结果, int

class Level2User(BaseStruct): #用户信息
    def __init__(self, UserID='', UserName='', Password='', EffectiveDate=''):
        self.UserID = 'TUserID' #用户代码, char[16]
        self.UserName = 'TUserName' #用户名称, char[81]
        self.Password = 'TPassword' #密码, char[41]
        self.EffectiveDate = 'TDate' #启用日期, char[9]

class SpecificSecurity(BaseStruct): #指定的证券
    def __init__(self, SecurityID='', ExchangeID=''):
        self.SecurityID = 'TSecurityID' #证券代码, char[13]
        self.ExchangeID = 'TExchangeID' #交易所代码, char[9]

class Level2MarketData(BaseStruct): #Level2行情
    def __init__(self, TradingDay='', DataTimeStamp='', ExchangeID='', SecurityID='', PreClosePx=0.0, OpenPx=0.0, HighPx=0.0, LowPx=0.0, LastPx=0.0, ClosePx=0.0, NumTrades=0, TotalVolumeTrade=0.0, TotalValueTrade=0.0, TotalBidQty=0.0, WeightedAvgBidPx=0.0, AltWeightedAvgBidPx=0.0, TotalOfferQty=0.0, WeightedAvgOfferPx=0.0, AltWeightedAvgOfferPx=0.0, IOPV=0.0, YieldToMaturity=0.0, TotalWarrantExecQty=0.0, WarLowerPx=0.0, WarUpperPx=0.0, BidPriceLevel=0, BidPx1=0.0, BidOrderQty1=0, BidNumOrder1=0, BidPx2=0.0, BidOrderQty2=0, BidNumOrder2=0, BidPx3=0.0, BidOrderQty3=0, BidNumOrder3=0, BidPx4=0.0, BidOrderQty4=0, BidNumOrder4=0, BidPx5=0.0, BidOrderQty5=0, BidNumOrder5=0, BidPx6=0.0, BidOrderQty6=0, BidNumOrder6=0, BidPx7=0.0, BidOrderQty7=0, BidNumOrder7=0, BidPx8=0.0, BidOrderQty8=0, BidNumOrder8=0, BidPx9=0.0, BidOrderQty9=0, BidNumOrder9=0, BidPxA=0.0, BidOrderQtyA=0, BidNumOrderA=0, OfferPriceLevel=0, OfferPx1=0.0, OfferOrderQty1=0, OfferNumOrder1=0, OfferPx2=0.0, OfferOrderQty2=0, OfferNumOrder2=0, OfferPx3=0.0, OfferOrderQty3=0, OfferNumOrder3=0, OfferPx4=0.0, OfferOrderQty4=0, OfferNumOrder4=0, OfferPx5=0.0, OfferOrderQty5=0, OfferNumOrder5=0, OfferPx6=0.0, OfferOrderQty6=0, OfferNumOrder6=0, OfferPx7=0.0, OfferOrderQty7=0, OfferNumOrder7=0, OfferPx8=0.0, OfferOrderQty8=0, OfferNumOrder8=0, OfferPx9=0.0, OfferOrderQty9=0, OfferNumOrder9=0, OfferPxA=0.0, OfferOrderQtyA=0, OfferNumOrderA=0):
        self.TradingDay = 'TDate' #交易日, char[9]
        self.DataTimeStamp = 'TTime' #时间戳, char[9]
        self.ExchangeID = 'TExchangeID' #交易所代码, char[9]
        self.SecurityID = 'TSecurityID' #证券代码, char[13]
        self.PreClosePx = 'TPrice' #昨收盘价, double
        self.OpenPx = 'TPrice' #今开盘价, double
        self.HighPx = 'TPrice' #最高价, double
        self.LowPx = 'TPrice' #最低价, double
        self.LastPx = 'TPrice' #现价, double
        self.ClosePx = 'TPrice' #收盘价, double
        self.NumTrades = 'TVolume' #成交笔数, int
        self.TotalVolumeTrade = 'TLargeVolume' #成交总量, double
        self.TotalValueTrade = 'TMoney' #成交总金额, double
        self.TotalBidQty = 'TLargeVolume' #委托买入总量, double
        self.WeightedAvgBidPx = 'TPrice' #加权平均委买价, double
        self.AltWeightedAvgBidPx = 'TPrice' #债券加权平均委买价, double
        self.TotalOfferQty = 'TLargeVolume' #委托卖出总量, double
        self.WeightedAvgOfferPx = 'TPrice' #加权平均委卖价, double
        self.AltWeightedAvgOfferPx = 'TPrice' #债券加权平均委卖价格, double
        self.IOPV = 'TPrice' #净值估值, double
        self.YieldToMaturity = 'TRatio' #到期收益率, double
        self.TotalWarrantExecQty = 'TLargeVolume' #权证执行总数量, double
        self.WarLowerPx = 'TPrice' #权证跌停价格, double
        self.WarUpperPx = 'TPrice' #权证涨停价格, double
        self.BidPriceLevel = 'TPriceLevel' #买价深度, int
        self.BidPx1 = 'TPrice' #申买价一, double
        self.BidOrderQty1 = 'TVolume' #申买量一, int
        self.BidNumOrder1 = 'TVolume' #实际买总委托笔数一, int
        self.BidPx2 = 'TPrice' #申买价二, double
        self.BidOrderQty2 = 'TVolume' #申买量二, int
        self.BidNumOrder2 = 'TVolume' #实际买总委托笔数二, int
        self.BidPx3 = 'TPrice' #申买价三, double
        self.BidOrderQty3 = 'TVolume' #申买量三, int
        self.BidNumOrder3 = 'TVolume' #实际买总委托笔数三, int
        self.BidPx4 = 'TPrice' #申买价四, double
        self.BidOrderQty4 = 'TVolume' #申买量四, int
        self.BidNumOrder4 = 'TVolume' #实际买总委托笔数四, int
        self.BidPx5 = 'TPrice' #申买价五, double
        self.BidOrderQty5 = 'TVolume' #申买量五, int
        self.BidNumOrder5 = 'TVolume' #实际买总委托笔数五, int
        self.BidPx6 = 'TPrice' #申买价六, double
        self.BidOrderQty6 = 'TVolume' #申买量六, int
        self.BidNumOrder6 = 'TVolume' #实际买总委托笔数六, int
        self.BidPx7 = 'TPrice' #申买价七, double
        self.BidOrderQty7 = 'TVolume' #申买量七, int
        self.BidNumOrder7 = 'TVolume' #实际买总委托笔数七, int
        self.BidPx8 = 'TPrice' #申买价八, double
        self.BidOrderQty8 = 'TVolume' #申买量八, int
        self.BidNumOrder8 = 'TVolume' #实际买总委托笔数八, int
        self.BidPx9 = 'TPrice' #申买价九, double
        self.BidOrderQty9 = 'TVolume' #申买量九, int
        self.BidNumOrder9 = 'TVolume' #实际买总委托笔数九, int
        self.BidPxA = 'TPrice' #申买价十, double
        self.BidOrderQtyA = 'TVolume' #申买量十, int
        self.BidNumOrderA = 'TVolume' #实际买总委托笔数十, int
        self.OfferPriceLevel = 'TPriceLevel' #卖价深度, int
        self.OfferPx1 = 'TPrice' #申卖价一, double
        self.OfferOrderQty1 = 'TVolume' #申卖量一, int
        self.OfferNumOrder1 = 'TVolume' #实际卖总委托笔数一, int
        self.OfferPx2 = 'TPrice' #申卖价二, double
        self.OfferOrderQty2 = 'TVolume' #申卖量二, int
        self.OfferNumOrder2 = 'TVolume' #实际卖总委托笔数二, int
        self.OfferPx3 = 'TPrice' #申卖价三, double
        self.OfferOrderQty3 = 'TVolume' #申卖量三, int
        self.OfferNumOrder3 = 'TVolume' #实际卖总委托笔数三, int
        self.OfferPx4 = 'TPrice' #申卖价四, double
        self.OfferOrderQty4 = 'TVolume' #申卖量四, int
        self.OfferNumOrder4 = 'TVolume' #实际卖总委托笔数四, int
        self.OfferPx5 = 'TPrice' #申卖价五, double
        self.OfferOrderQty5 = 'TVolume' #申卖量五, int
        self.OfferNumOrder5 = 'TVolume' #实际卖总委托笔数五, int
        self.OfferPx6 = 'TPrice' #申卖价六, double
        self.OfferOrderQty6 = 'TVolume' #申卖量六, int
        self.OfferNumOrder6 = 'TVolume' #实际卖总委托笔数六, int
        self.OfferPx7 = 'TPrice' #申卖价七, double
        self.OfferOrderQty7 = 'TVolume' #申卖量七, int
        self.OfferNumOrder7 = 'TVolume' #实际卖总委托笔数七, int
        self.OfferPx8 = 'TPrice' #申卖价八, double
        self.OfferOrderQty8 = 'TVolume' #申卖量八, int
        self.OfferNumOrder8 = 'TVolume' #实际卖总委托笔数八, int
        self.OfferPx9 = 'TPrice' #申卖价九, double
        self.OfferOrderQty9 = 'TVolume' #申卖量九, int
        self.OfferNumOrder9 = 'TVolume' #实际卖总委托笔数九, int
        self.OfferPxA = 'TPrice' #申卖价十, double
        self.OfferOrderQtyA = 'TVolume' #申卖量十, int
        self.OfferNumOrderA = 'TVolume' #实际卖总委托笔数十, int

class L2MarketDataUpdateTime(BaseStruct): #Level2行情更新时间属性
    def __init__(self, TradingDay='', DataTimeStamp='', ExchangeID='', SecurityID=''):
        self.TradingDay = 'TDate' #交易日, char[9]
        self.DataTimeStamp = 'TTime' #时间戳, char[9]
        self.ExchangeID = 'TExchangeID' #交易所代码, char[9]
        self.SecurityID = 'TSecurityID' #证券代码, char[13]

class L2MarketDataBid1(BaseStruct): #Level2行情申买一属性
    def __init__(self, BidPx1=0.0, BidOrderQty1=0, BidNumOrder1=0):
        self.BidPx1 = 'TPrice' #申买价一, double
        self.BidOrderQty1 = 'TVolume' #申买量一, int
        self.BidNumOrder1 = 'TVolume' #实际买总委托笔数一, int

class L2MarketDataOffer1(BaseStruct): #Level2行情申卖一属性
    def __init__(self, OfferPx1=0.0, OfferOrderQty1=0, OfferNumOrder1=0):
        self.OfferPx1 = 'TPrice' #申卖价一, double
        self.OfferOrderQty1 = 'TVolume' #申卖量一, int
        self.OfferNumOrder1 = 'TVolume' #实际卖总委托笔数一, int

class L2MarketDataBid2(BaseStruct): #Level2行情申买二属性
    def __init__(self, BidPx2=0.0, BidOrderQty2=0, BidNumOrder2=0):
        self.BidPx2 = 'TPrice' #申买价二, double
        self.BidOrderQty2 = 'TVolume' #申买量二, int
        self.BidNumOrder2 = 'TVolume' #实际买总委托笔数二, int

class L2MarketDataOffer2(BaseStruct): #Level2行情申卖二属性
    def __init__(self, OfferPx2=0.0, OfferOrderQty2=0, OfferNumOrder2=0):
        self.OfferPx2 = 'TPrice' #申卖价二, double
        self.OfferOrderQty2 = 'TVolume' #申卖量二, int
        self.OfferNumOrder2 = 'TVolume' #实际卖总委托笔数二, int

class L2MarketDataBid3(BaseStruct): #Level2行情申买三属性
    def __init__(self, BidPx3=0.0, BidOrderQty3=0, BidNumOrder3=0):
        self.BidPx3 = 'TPrice' #申买价三, double
        self.BidOrderQty3 = 'TVolume' #申买量三, int
        self.BidNumOrder3 = 'TVolume' #实际买总委托笔数三, int

class L2MarketDataOffer3(BaseStruct): #Level2行情申卖三属性
    def __init__(self, OfferPx3=0.0, OfferOrderQty3=0, OfferNumOrder3=0):
        self.OfferPx3 = 'TPrice' #申卖价三, double
        self.OfferOrderQty3 = 'TVolume' #申卖量三, int
        self.OfferNumOrder3 = 'TVolume' #实际卖总委托笔数三, int

class L2MarketDataBid4(BaseStruct): #Level2行情申买四属性
    def __init__(self, BidPx4=0.0, BidOrderQty4=0, BidNumOrder4=0):
        self.BidPx4 = 'TPrice' #申买价四, double
        self.BidOrderQty4 = 'TVolume' #申买量四, int
        self.BidNumOrder4 = 'TVolume' #实际买总委托笔数四, int

class L2MarketDataOffer4(BaseStruct): #Level2行情申卖四属性
    def __init__(self, OfferPx4=0.0, OfferOrderQty4=0, OfferNumOrder4=0):
        self.OfferPx4 = 'TPrice' #申卖价四, double
        self.OfferOrderQty4 = 'TVolume' #申卖量四, int
        self.OfferNumOrder4 = 'TVolume' #实际卖总委托笔数四, int

class L2MarketDataBid5(BaseStruct): #Level2行情申买五属性
    def __init__(self, BidPx5=0.0, BidOrderQty5=0, BidNumOrder5=0):
        self.BidPx5 = 'TPrice' #申买价五, double
        self.BidOrderQty5 = 'TVolume' #申买量五, int
        self.BidNumOrder5 = 'TVolume' #实际买总委托笔数五, int

class L2MarketDataOffer5(BaseStruct): #Level2行情申卖五属性
    def __init__(self, OfferPx5=0.0, OfferOrderQty5=0, OfferNumOrder5=0):
        self.OfferPx5 = 'TPrice' #申卖价五, double
        self.OfferOrderQty5 = 'TVolume' #申卖量五, int
        self.OfferNumOrder5 = 'TVolume' #实际卖总委托笔数五, int

class L2MarketDataBid6(BaseStruct): #Level2行情申买六属性
    def __init__(self, BidPx6=0.0, BidOrderQty6=0, BidNumOrder6=0):
        self.BidPx6 = 'TPrice' #申买价六, double
        self.BidOrderQty6 = 'TVolume' #申买量六, int
        self.BidNumOrder6 = 'TVolume' #实际买总委托笔数六, int

class L2MarketDataOffer6(BaseStruct): #Level2行情申卖六属性
    def __init__(self, OfferPx6=0.0, OfferOrderQty6=0, OfferNumOrder6=0):
        self.OfferPx6 = 'TPrice' #申卖价六, double
        self.OfferOrderQty6 = 'TVolume' #申卖量六, int
        self.OfferNumOrder6 = 'TVolume' #实际卖总委托笔数六, int

class L2MarketDataBid7(BaseStruct): #Level2行情申买七属性
    def __init__(self, BidPx7=0.0, BidOrderQty7=0, BidNumOrder7=0):
        self.BidPx7 = 'TPrice' #申买价七, double
        self.BidOrderQty7 = 'TVolume' #申买量七, int
        self.BidNumOrder7 = 'TVolume' #实际买总委托笔数七, int

class L2MarketDataOffer7(BaseStruct): #Level2行情申卖七属性
    def __init__(self, OfferPx7=0.0, OfferOrderQty7=0, OfferNumOrder7=0):
        self.OfferPx7 = 'TPrice' #申卖价七, double
        self.OfferOrderQty7 = 'TVolume' #申卖量七, int
        self.OfferNumOrder7 = 'TVolume' #实际卖总委托笔数七, int

class L2MarketDataBid8(BaseStruct): #Level2行情申买八属性
    def __init__(self, BidPx8=0.0, BidOrderQty8=0, BidNumOrder8=0):
        self.BidPx8 = 'TPrice' #申买价八, double
        self.BidOrderQty8 = 'TVolume' #申买量八, int
        self.BidNumOrder8 = 'TVolume' #实际买总委托笔数八, int

class L2MarketDataOffer8(BaseStruct): #Level2行情申卖八属性
    def __init__(self, OfferPx8=0.0, OfferOrderQty8=0, OfferNumOrder8=0):
        self.OfferPx8 = 'TPrice' #申卖价八, double
        self.OfferOrderQty8 = 'TVolume' #申卖量八, int
        self.OfferNumOrder8 = 'TVolume' #实际卖总委托笔数八, int

class L2MarketDataBid9(BaseStruct): #Level2行情申买九属性
    def __init__(self, BidPx9=0.0, BidOrderQty9=0, BidNumOrder9=0):
        self.BidPx9 = 'TPrice' #申买价九, double
        self.BidOrderQty9 = 'TVolume' #申买量九, int
        self.BidNumOrder9 = 'TVolume' #实际买总委托笔数九, int

class L2MarketDataOffer9(BaseStruct): #Level2行情申卖九属性
    def __init__(self, OfferPx9=0.0, OfferOrderQty9=0, OfferNumOrder9=0):
        self.OfferPx9 = 'TPrice' #申卖价九, double
        self.OfferOrderQty9 = 'TVolume' #申卖量九, int
        self.OfferNumOrder9 = 'TVolume' #实际卖总委托笔数九, int

class L2MarketDataBidA(BaseStruct): #Level2行情申买十属性
    def __init__(self, BidPxA=0.0, BidOrderQtyA=0, BidNumOrderA=0):
        self.BidPxA = 'TPrice' #申买价十, double
        self.BidOrderQtyA = 'TVolume' #申买量十, int
        self.BidNumOrderA = 'TVolume' #实际买总委托笔数十, int

class L2MarketDataOfferA(BaseStruct): #Level2行情申卖十属性
    def __init__(self, OfferPxA=0.0, OfferOrderQtyA=0, OfferNumOrderA=0):
        self.OfferPxA = 'TPrice' #申卖价十, double
        self.OfferOrderQtyA = 'TVolume' #申卖量十, int
        self.OfferNumOrderA = 'TVolume' #实际卖总委托笔数十, int

class L2MarketDataTraded(BaseStruct): #Level2成交信息
    def __init__(self, NumTrades=0, TotalVolumeTrade=0.0, TotalValueTrade=0.0):
        self.NumTrades = 'TVolume' #成交笔数, int
        self.TotalVolumeTrade = 'TLargeVolume' #成交总量, double
        self.TotalValueTrade = 'TMoney' #成交总金额, double

class L2MarketDataBidOrder(BaseStruct): #Level2委买信息
    def __init__(self, TotalBidQty=0.0, WeightedAvgBidPx=0.0, AltWeightedAvgBidPx=0.0):
        self.TotalBidQty = 'TLargeVolume' #委托买入总量, double
        self.WeightedAvgBidPx = 'TPrice' #加权平均委买价, double
        self.AltWeightedAvgBidPx = 'TPrice' #债券加权平均委买价, double

class L2MarketDataOfferOrder(BaseStruct): #Level2委卖信息
    def __init__(self, TotalOfferQty=0.0, WeightedAvgOfferPx=0.0, AltWeightedAvgOfferPx=0.0):
        self.TotalOfferQty = 'TLargeVolume' #委托卖出总量, double
        self.WeightedAvgOfferPx = 'TPrice' #加权平均委卖价, double
        self.AltWeightedAvgOfferPx = 'TPrice' #债券加权平均委卖价格, double

class L2MarketDataWarrant(BaseStruct): #Level2权证信息
    def __init__(self, TotalWarrantExecQty=0.0, WarLowerPx=0.0, WarUpperPx=0.0):
        self.TotalWarrantExecQty = 'TLargeVolume' #权证执行总数量, double
        self.WarLowerPx = 'TPrice' #权证跌停价格, double
        self.WarUpperPx = 'TPrice' #权证涨停价格, double

class L2MarketDataBase(BaseStruct): #Level2行情基本信息
    def __init__(self, LastPx=0.0):
        self.LastPx = 'TPrice' #现价, double

class L2MarketDataStatic(BaseStruct): #Level2行情静态属性
    def __init__(self, PreClosePx=0.0, OpenPx=0.0, ClosePx=0.0, HighPx=0.0, LowPx=0.0, IOPV=0.0, YieldToMaturity=0.0):
        self.PreClosePx = 'TPrice' #昨收盘价, double
        self.OpenPx = 'TPrice' #今开盘价, double
        self.ClosePx = 'TPrice' #收盘价, double
        self.HighPx = 'TPrice' #最高价, double
        self.LowPx = 'TPrice' #最低价, double
        self.IOPV = 'TPrice' #净值估值, double
        self.YieldToMaturity = 'TRatio' #到期收益率, double

class L2MarketDataPriceLevel(BaseStruct): #Level2价格深度属性
    def __init__(self, BidPriceLevel=0, OfferPriceLevel=0):
        self.BidPriceLevel = 'TPriceLevel' #买价深度, int
        self.OfferPriceLevel = 'TPriceLevel' #卖价深度, int

class NGTSIndex(BaseStruct): #Level2指数行情
    def __init__(self, TradingDay='', TimeStamp='', ExchangeID='', SecurityID='', PreCloseIndex=0.0, OpenIndex=0.0, TurnOver=0.0, HighIndex=0.0, LowIndex=0.0, LastIndex=0.0, CloseIndex=0.0, TradeTime='', TotalVolumeTraded=0.0):
        self.TradingDay = 'TDate' #交易日, char[9]
        self.TimeStamp = 'TTime' #行情时间（秒）, char[9]
        self.ExchangeID = 'TExchangeID' #交易所代码, char[9]
        self.SecurityID = 'TSecurityID' #指数代码, char[13]
        self.PreCloseIndex = 'TIndex' #前收盘指数, double
        self.OpenIndex = 'TIndex' #今开盘指数, double
        self.TurnOver = 'TMoney' #参与计算相应指数的成交金额（元）, double
        self.HighIndex = 'TIndex' #最高指数, double
        self.LowIndex = 'TIndex' #最低指数, double
        self.LastIndex = 'TIndex' #最新指数, double
        self.CloseIndex = 'TIndex' #今日收盘指数, double
        self.TradeTime = 'TTime' #成交时间, char[9]
        self.TotalVolumeTraded = 'TLargeVolume' #参与计算相应指数的交易数量（手）, double

def _init():
    from ctypes import c_char, c_short, c_int, c_double, Structure
    T = {}; G = globals(); del G['_init']

    T['TE_RESUME'] = c_int #流重传方式
    T['TBrokerID'] = c_char * 11 #经纪公司代码
    T['TBrokerAbbr'] = c_char * 9 #经纪公司简称
    T['TBrokerName'] = c_char * 81 #经纪公司名称
    T['TUserID'] = c_char * 16 #用户代码
    T['TUserName'] = c_char * 81 #用户名称
    T['TPassword'] = c_char * 41 #密码
    T['TProductName'] = c_char * 21 #产品名称
    T['TExchangeID'] = c_char * 9 #交易所代码
    T['TExchangeName'] = c_char * 31 #交易所名称
    T['TExchangeAbbr'] = c_char * 9 #交易所简称
    T['TExchangeFlag'] = c_char * 2 #交易所标志
    T['TMacAddress'] = c_char * 21 #Mac地址
    T['TDate'] = c_char * 9 #日期
    T['TTime'] = c_char * 9 #时间
    T['TLongTime'] = c_char * 13 #长时间
    T['TTradeID'] = c_char * 21 #成交编号
    T['TIPAddress'] = c_char * 16 #IP地址
    T['TProductInfo'] = c_char * 11 #产品信息
    T['TProtocolInfo'] = c_char * 11 #协议信息
    T['TSystemName'] = c_char * 41 #系统名称
    T['TInstrumentStatus'] = c_char #合约交易状态
    T['TInstallCount'] = c_int #安装数量
    T['TInstallID'] = c_int #安装编号
    T['TErrorID'] = c_int #错误代码
    T['TErrorMsg'] = c_char * 81 #错误信息
    T['TFrontID'] = c_int #前置编号
    T['TSessionID'] = c_int #会话编号
    T['TSequenceNo'] = c_int #序号
    T['TMillisec'] = c_int #时间（毫秒）
    T['TTradingSegmentSN'] = c_int #交易阶段编号
    T['TRequestID'] = c_int #请求编号
    T['TYear'] = c_int #年份
    T['TMonth'] = c_int #月份
    T['TBool'] = c_int #布尔型
    T['TPrice'] = c_double #价格
    T['TRatio'] = c_double #比率
    T['TMoney'] = c_double #资金
    T['TVolume'] = c_int #数量
    T['TLargeVolume'] = c_double #大额数量
    T['TSequenceSeries'] = c_short #序列系列号
    T['TCommPhaseNo'] = c_short #通讯时段编号
    T['TSequenceLabel'] = c_char * 2 #序列编号
    T['TChannel'] = c_char * 51 #渠道
    T['TAddress'] = c_char * 101 #通讯地址
    T['TZipCode'] = c_char * 7 #邮政编码
    T['TTelephone'] = c_char * 41 #联系电话
    T['TFax'] = c_char * 41 #传真
    T['TMobile'] = c_char * 41 #手机
    T['TEMail'] = c_char * 41 #电子邮件
    T['TMemo'] = c_char * 161 #备注
    T['TVersion'] = c_char * 4 #版本号
    T['TTradeDate'] = c_char * 9 #交易日期
    T['TTradeTime'] = c_char * 9 #交易时间
    T['TAuthInfo'] = c_char * 129 #客户端认证信息
    T['TAuthCode'] = c_char * 17 #客户端认证码
    T['TSecurityID'] = c_char * 13 #证券代码
    T['TPriceLevel'] = c_int #价格深度
    T['TIndex'] = c_double #指数

    Base = G.pop('BaseStruct')
    Structs = [v for v in G.values() if isinstance(v,type) and issubclass(v,Base)]
    from .ApiStruct import BaseStruct as Base
    class builder(object):
        def __setattr__(self, fn, ft):
            self.fields.append((fn, T[ft]))
        def build(self, cls):
            self.__dict__['fields'] = []
            cls.__dict__['__init__'](self)
            G[cls.__name__] = type(cls.__name__, (Base,), {'_fields_':tuple(self.fields)})
    builder = builder()
    for cls in Structs: builder.build(cls)
_init()
