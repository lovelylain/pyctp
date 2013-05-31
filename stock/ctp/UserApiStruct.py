# -*- coding: utf-8 -*-

from __future__ import absolute_import as _init

__all__ = ['TERT_RESTART', 'TERT_RESUME', 'TERT_QUICK', 'IS_BeforeTrading', 'IS_NoTrading', 'IS_Continous', 'IS_AuctionOrdering', 'IS_AuctionBalance', 'IS_AuctionMatch', 'IS_Closed', 'RspInfo', 'Dissemination', 'ReqUserLogin', 'RspUserLogin', 'UserLogout', 'UserSessionRef', 'ReqAuthenticate', 'RspAuthenticate', 'AuthenticationInfo', 'Level2User', 'SpecificSecurity', 'Level2MarketData', 'L2MarketDataUpdateTime', 'L2MarketDataBid1', 'L2MarketDataOffer1', 'L2MarketDataBid2', 'L2MarketDataOffer2', 'L2MarketDataBid3', 'L2MarketDataOffer3', 'L2MarketDataBid4', 'L2MarketDataOffer4', 'L2MarketDataBid5', 'L2MarketDataOffer5', 'L2MarketDataBid6', 'L2MarketDataOffer6', 'L2MarketDataBid7', 'L2MarketDataOffer7', 'L2MarketDataBid8', 'L2MarketDataOffer8', 'L2MarketDataBid9', 'L2MarketDataOffer9', 'L2MarketDataBidA', 'L2MarketDataOfferA', 'L2MarketDataTraded', 'L2MarketDataBidOrder', 'L2MarketDataOfferOrder', 'L2MarketDataWarrant', 'L2MarketDataBase', 'L2MarketDataStatic', 'L2MarketDataPriceLevel', 'NGTSIndex']

_init = list(globals()); _init.extend(__all__)
from ctypes import c_char, c_short, c_int, c_double
from .ApiStruct import BaseStruct

TE_RESUME = c_int #流重传方式
TERT_RESTART = 0 #从本交易日开始重传
TERT_RESUME = 1 #从上次收到的续传
TERT_QUICK = 2 #只传送登录后的流内容
TBrokerID = c_char * 11 #经纪公司代码
TBrokerAbbr = c_char * 9 #经纪公司简称
TBrokerName = c_char * 81 #经纪公司名称
TUserID = c_char * 16 #用户代码
TUserName = c_char * 81 #用户名称
TPassword = c_char * 41 #密码
TProductName = c_char * 21 #产品名称
TExchangeID = c_char * 9 #交易所代码
TExchangeName = c_char * 31 #交易所名称
TExchangeAbbr = c_char * 9 #交易所简称
TExchangeFlag = c_char * 2 #交易所标志
TMacAddress = c_char * 21 #Mac地址
TDate = c_char * 9 #日期
TTime = c_char * 9 #时间
TLongTime = c_char * 13 #长时间
TTradeID = c_char * 21 #成交编号
TIPAddress = c_char * 16 #IP地址
TProductInfo = c_char * 11 #产品信息
TProtocolInfo = c_char * 11 #协议信息
TSystemName = c_char * 41 #系统名称
TInstrumentStatus = c_char #合约交易状态
IS_BeforeTrading = '0' #开盘前
IS_NoTrading = '1' #非交易
IS_Continous = '2' #连续交易
IS_AuctionOrdering = '3' #集合竞价报单
IS_AuctionBalance = '4' #集合竞价价格平衡
IS_AuctionMatch = '5' #集合竞价撮合
IS_Closed = '6' #收盘
TInstallCount = c_int #安装数量
TInstallID = c_int #安装编号
TErrorID = c_int #错误代码
TErrorMsg = c_char * 81 #错误信息
TFrontID = c_int #前置编号
TSessionID = c_int #会话编号
TSequenceNo = c_int #序号
TMillisec = c_int #时间（毫秒）
TTradingSegmentSN = c_int #交易阶段编号
TRequestID = c_int #请求编号
TYear = c_int #年份
TMonth = c_int #月份
TBool = c_int #布尔型
TPrice = c_double #价格
TRatio = c_double #比率
TMoney = c_double #资金
TVolume = c_int #数量
TLargeVolume = c_double #大额数量
TSequenceSeries = c_short #序列系列号
TCommPhaseNo = c_short #通讯时段编号
TSequenceLabel = c_char * 2 #序列编号
TChannel = c_char * 51 #渠道
TAddress = c_char * 101 #通讯地址
TZipCode = c_char * 7 #邮政编码
TTelephone = c_char * 41 #联系电话
TFax = c_char * 41 #传真
TMobile = c_char * 41 #手机
TEMail = c_char * 41 #电子邮件
TMemo = c_char * 161 #备注
TVersion = c_char * 4 #版本号
TTradeDate = c_char * 9 #交易日期
TTradeTime = c_char * 9 #交易时间
TAuthInfo = c_char * 129 #客户端认证信息
TAuthCode = c_char * 17 #客户端认证码
TSecurityID = c_char * 13 #证券代码
TPriceLevel = c_int #价格深度
TIndex = c_double #指数

class RspInfo(BaseStruct): #响应信息
    _fields_ = (
        ('ErrorID', TErrorID), #错误代码, int
        ('ErrorMsg', TErrorMsg), #错误信息, char[81]
    )
class Dissemination(BaseStruct): #信息分发
    _fields_ = (
        ('SequenceSeries', TSequenceSeries), #序列系列号, short
        ('SequenceNo', TSequenceNo), #序列号, int
    )
class ReqUserLogin(BaseStruct): #用户登录请求
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('Password', TPassword), #密码, char[41]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('InterfaceProductInfo', TProductInfo), #接口端产品信息, char[11]
        ('ProtocolInfo', TProtocolInfo), #协议信息, char[11]
        ('MacAddress', TMacAddress), #Mac地址, char[21]
        ('OneTimePassword', TPassword), #动态密码, char[41]
        ('ClientIPAddress', TIPAddress), #终端IP地址, char[16]
    )
class RspUserLogin(BaseStruct): #用户登录应答
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('LoginTime', TTime), #登录成功时间, char[9]
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('SystemName', TSystemName), #交易系统名称, char[41]
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
        ('SSETime', TTime), #上证所时间, char[9]
        ('SZETime', TTime), #深证所时间, char[9]
    )
class UserLogout(BaseStruct): #用户登出请求
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
    )
class UserSessionRef(BaseStruct): #用户会话
    _fields_ = (
        ('FrontID', TFrontID), #前置编号, int
        ('SessionID', TSessionID), #会话编号, int
    )
class ReqAuthenticate(BaseStruct): #客户端认证请求
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('AuthCode', TAuthCode), #认证码, char[17]
    )
class RspAuthenticate(BaseStruct): #客户端认证响应
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
    )
class AuthenticationInfo(BaseStruct): #客户端认证信息
    _fields_ = (
        ('BrokerID', TBrokerID), #经纪公司代码, char[11]
        ('UserID', TUserID), #用户代码, char[16]
        ('UserProductInfo', TProductInfo), #用户端产品信息, char[11]
        ('AuthInfo', TAuthInfo), #认证信息, char[129]
        ('IsResult', TBool), #是否为认证结果, int
    )
class Level2User(BaseStruct): #用户信息
    _fields_ = (
        ('UserID', TUserID), #用户代码, char[16]
        ('UserName', TUserName), #用户名称, char[81]
        ('Password', TPassword), #密码, char[41]
        ('EffectiveDate', TDate), #启用日期, char[9]
    )
class SpecificSecurity(BaseStruct): #指定的证券
    _fields_ = (
        ('SecurityID', TSecurityID), #证券代码, char[13]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
    )
class Level2MarketData(BaseStruct): #Level2行情
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('DataTimeStamp', TTime), #时间戳, char[9]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('SecurityID', TSecurityID), #证券代码, char[13]
        ('PreClosePx', TPrice), #昨收盘价, double
        ('OpenPx', TPrice), #今开盘价, double
        ('HighPx', TPrice), #最高价, double
        ('LowPx', TPrice), #最低价, double
        ('LastPx', TPrice), #现价, double
        ('ClosePx', TPrice), #收盘价, double
        ('NumTrades', TVolume), #成交笔数, int
        ('TotalVolumeTrade', TLargeVolume), #成交总量, double
        ('TotalValueTrade', TMoney), #成交总金额, double
        ('TotalBidQty', TLargeVolume), #委托买入总量, double
        ('WeightedAvgBidPx', TPrice), #加权平均委买价, double
        ('AltWeightedAvgBidPx', TPrice), #债券加权平均委买价, double
        ('TotalOfferQty', TLargeVolume), #委托卖出总量, double
        ('WeightedAvgOfferPx', TPrice), #加权平均委卖价, double
        ('AltWeightedAvgOfferPx', TPrice), #债券加权平均委卖价格, double
        ('IOPV', TPrice), #净值估值, double
        ('YieldToMaturity', TRatio), #到期收益率, double
        ('TotalWarrantExecQty', TLargeVolume), #权证执行总数量, double
        ('WarLowerPx', TPrice), #权证跌停价格, double
        ('WarUpperPx', TPrice), #权证涨停价格, double
        ('BidPriceLevel', TPriceLevel), #买价深度, int
        ('BidPx1', TPrice), #申买价一, double
        ('BidOrderQty1', TVolume), #申买量一, int
        ('BidNumOrder1', TVolume), #实际买总委托笔数一, int
        ('BidPx2', TPrice), #申买价二, double
        ('BidOrderQty2', TVolume), #申买量二, int
        ('BidNumOrder2', TVolume), #实际买总委托笔数二, int
        ('BidPx3', TPrice), #申买价三, double
        ('BidOrderQty3', TVolume), #申买量三, int
        ('BidNumOrder3', TVolume), #实际买总委托笔数三, int
        ('BidPx4', TPrice), #申买价四, double
        ('BidOrderQty4', TVolume), #申买量四, int
        ('BidNumOrder4', TVolume), #实际买总委托笔数四, int
        ('BidPx5', TPrice), #申买价五, double
        ('BidOrderQty5', TVolume), #申买量五, int
        ('BidNumOrder5', TVolume), #实际买总委托笔数五, int
        ('BidPx6', TPrice), #申买价六, double
        ('BidOrderQty6', TVolume), #申买量六, int
        ('BidNumOrder6', TVolume), #实际买总委托笔数六, int
        ('BidPx7', TPrice), #申买价七, double
        ('BidOrderQty7', TVolume), #申买量七, int
        ('BidNumOrder7', TVolume), #实际买总委托笔数七, int
        ('BidPx8', TPrice), #申买价八, double
        ('BidOrderQty8', TVolume), #申买量八, int
        ('BidNumOrder8', TVolume), #实际买总委托笔数八, int
        ('BidPx9', TPrice), #申买价九, double
        ('BidOrderQty9', TVolume), #申买量九, int
        ('BidNumOrder9', TVolume), #实际买总委托笔数九, int
        ('BidPxA', TPrice), #申买价十, double
        ('BidOrderQtyA', TVolume), #申买量十, int
        ('BidNumOrderA', TVolume), #实际买总委托笔数十, int
        ('OfferPriceLevel', TPriceLevel), #卖价深度, int
        ('OfferPx1', TPrice), #申卖价一, double
        ('OfferOrderQty1', TVolume), #申卖量一, int
        ('OfferNumOrder1', TVolume), #实际卖总委托笔数一, int
        ('OfferPx2', TPrice), #申卖价二, double
        ('OfferOrderQty2', TVolume), #申卖量二, int
        ('OfferNumOrder2', TVolume), #实际卖总委托笔数二, int
        ('OfferPx3', TPrice), #申卖价三, double
        ('OfferOrderQty3', TVolume), #申卖量三, int
        ('OfferNumOrder3', TVolume), #实际卖总委托笔数三, int
        ('OfferPx4', TPrice), #申卖价四, double
        ('OfferOrderQty4', TVolume), #申卖量四, int
        ('OfferNumOrder4', TVolume), #实际卖总委托笔数四, int
        ('OfferPx5', TPrice), #申卖价五, double
        ('OfferOrderQty5', TVolume), #申卖量五, int
        ('OfferNumOrder5', TVolume), #实际卖总委托笔数五, int
        ('OfferPx6', TPrice), #申卖价六, double
        ('OfferOrderQty6', TVolume), #申卖量六, int
        ('OfferNumOrder6', TVolume), #实际卖总委托笔数六, int
        ('OfferPx7', TPrice), #申卖价七, double
        ('OfferOrderQty7', TVolume), #申卖量七, int
        ('OfferNumOrder7', TVolume), #实际卖总委托笔数七, int
        ('OfferPx8', TPrice), #申卖价八, double
        ('OfferOrderQty8', TVolume), #申卖量八, int
        ('OfferNumOrder8', TVolume), #实际卖总委托笔数八, int
        ('OfferPx9', TPrice), #申卖价九, double
        ('OfferOrderQty9', TVolume), #申卖量九, int
        ('OfferNumOrder9', TVolume), #实际卖总委托笔数九, int
        ('OfferPxA', TPrice), #申卖价十, double
        ('OfferOrderQtyA', TVolume), #申卖量十, int
        ('OfferNumOrderA', TVolume), #实际卖总委托笔数十, int
    )
class L2MarketDataUpdateTime(BaseStruct): #Level2行情更新时间属性
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('DataTimeStamp', TTime), #时间戳, char[9]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('SecurityID', TSecurityID), #证券代码, char[13]
    )
class L2MarketDataBid1(BaseStruct): #Level2行情申买一属性
    _fields_ = (
        ('BidPx1', TPrice), #申买价一, double
        ('BidOrderQty1', TVolume), #申买量一, int
        ('BidNumOrder1', TVolume), #实际买总委托笔数一, int
    )
class L2MarketDataOffer1(BaseStruct): #Level2行情申卖一属性
    _fields_ = (
        ('OfferPx1', TPrice), #申卖价一, double
        ('OfferOrderQty1', TVolume), #申卖量一, int
        ('OfferNumOrder1', TVolume), #实际卖总委托笔数一, int
    )
class L2MarketDataBid2(BaseStruct): #Level2行情申买二属性
    _fields_ = (
        ('BidPx2', TPrice), #申买价二, double
        ('BidOrderQty2', TVolume), #申买量二, int
        ('BidNumOrder2', TVolume), #实际买总委托笔数二, int
    )
class L2MarketDataOffer2(BaseStruct): #Level2行情申卖二属性
    _fields_ = (
        ('OfferPx2', TPrice), #申卖价二, double
        ('OfferOrderQty2', TVolume), #申卖量二, int
        ('OfferNumOrder2', TVolume), #实际卖总委托笔数二, int
    )
class L2MarketDataBid3(BaseStruct): #Level2行情申买三属性
    _fields_ = (
        ('BidPx3', TPrice), #申买价三, double
        ('BidOrderQty3', TVolume), #申买量三, int
        ('BidNumOrder3', TVolume), #实际买总委托笔数三, int
    )
class L2MarketDataOffer3(BaseStruct): #Level2行情申卖三属性
    _fields_ = (
        ('OfferPx3', TPrice), #申卖价三, double
        ('OfferOrderQty3', TVolume), #申卖量三, int
        ('OfferNumOrder3', TVolume), #实际卖总委托笔数三, int
    )
class L2MarketDataBid4(BaseStruct): #Level2行情申买四属性
    _fields_ = (
        ('BidPx4', TPrice), #申买价四, double
        ('BidOrderQty4', TVolume), #申买量四, int
        ('BidNumOrder4', TVolume), #实际买总委托笔数四, int
    )
class L2MarketDataOffer4(BaseStruct): #Level2行情申卖四属性
    _fields_ = (
        ('OfferPx4', TPrice), #申卖价四, double
        ('OfferOrderQty4', TVolume), #申卖量四, int
        ('OfferNumOrder4', TVolume), #实际卖总委托笔数四, int
    )
class L2MarketDataBid5(BaseStruct): #Level2行情申买五属性
    _fields_ = (
        ('BidPx5', TPrice), #申买价五, double
        ('BidOrderQty5', TVolume), #申买量五, int
        ('BidNumOrder5', TVolume), #实际买总委托笔数五, int
    )
class L2MarketDataOffer5(BaseStruct): #Level2行情申卖五属性
    _fields_ = (
        ('OfferPx5', TPrice), #申卖价五, double
        ('OfferOrderQty5', TVolume), #申卖量五, int
        ('OfferNumOrder5', TVolume), #实际卖总委托笔数五, int
    )
class L2MarketDataBid6(BaseStruct): #Level2行情申买六属性
    _fields_ = (
        ('BidPx6', TPrice), #申买价六, double
        ('BidOrderQty6', TVolume), #申买量六, int
        ('BidNumOrder6', TVolume), #实际买总委托笔数六, int
    )
class L2MarketDataOffer6(BaseStruct): #Level2行情申卖六属性
    _fields_ = (
        ('OfferPx6', TPrice), #申卖价六, double
        ('OfferOrderQty6', TVolume), #申卖量六, int
        ('OfferNumOrder6', TVolume), #实际卖总委托笔数六, int
    )
class L2MarketDataBid7(BaseStruct): #Level2行情申买七属性
    _fields_ = (
        ('BidPx7', TPrice), #申买价七, double
        ('BidOrderQty7', TVolume), #申买量七, int
        ('BidNumOrder7', TVolume), #实际买总委托笔数七, int
    )
class L2MarketDataOffer7(BaseStruct): #Level2行情申卖七属性
    _fields_ = (
        ('OfferPx7', TPrice), #申卖价七, double
        ('OfferOrderQty7', TVolume), #申卖量七, int
        ('OfferNumOrder7', TVolume), #实际卖总委托笔数七, int
    )
class L2MarketDataBid8(BaseStruct): #Level2行情申买八属性
    _fields_ = (
        ('BidPx8', TPrice), #申买价八, double
        ('BidOrderQty8', TVolume), #申买量八, int
        ('BidNumOrder8', TVolume), #实际买总委托笔数八, int
    )
class L2MarketDataOffer8(BaseStruct): #Level2行情申卖八属性
    _fields_ = (
        ('OfferPx8', TPrice), #申卖价八, double
        ('OfferOrderQty8', TVolume), #申卖量八, int
        ('OfferNumOrder8', TVolume), #实际卖总委托笔数八, int
    )
class L2MarketDataBid9(BaseStruct): #Level2行情申买九属性
    _fields_ = (
        ('BidPx9', TPrice), #申买价九, double
        ('BidOrderQty9', TVolume), #申买量九, int
        ('BidNumOrder9', TVolume), #实际买总委托笔数九, int
    )
class L2MarketDataOffer9(BaseStruct): #Level2行情申卖九属性
    _fields_ = (
        ('OfferPx9', TPrice), #申卖价九, double
        ('OfferOrderQty9', TVolume), #申卖量九, int
        ('OfferNumOrder9', TVolume), #实际卖总委托笔数九, int
    )
class L2MarketDataBidA(BaseStruct): #Level2行情申买十属性
    _fields_ = (
        ('BidPxA', TPrice), #申买价十, double
        ('BidOrderQtyA', TVolume), #申买量十, int
        ('BidNumOrderA', TVolume), #实际买总委托笔数十, int
    )
class L2MarketDataOfferA(BaseStruct): #Level2行情申卖十属性
    _fields_ = (
        ('OfferPxA', TPrice), #申卖价十, double
        ('OfferOrderQtyA', TVolume), #申卖量十, int
        ('OfferNumOrderA', TVolume), #实际卖总委托笔数十, int
    )
class L2MarketDataTraded(BaseStruct): #Level2成交信息
    _fields_ = (
        ('NumTrades', TVolume), #成交笔数, int
        ('TotalVolumeTrade', TLargeVolume), #成交总量, double
        ('TotalValueTrade', TMoney), #成交总金额, double
    )
class L2MarketDataBidOrder(BaseStruct): #Level2委买信息
    _fields_ = (
        ('TotalBidQty', TLargeVolume), #委托买入总量, double
        ('WeightedAvgBidPx', TPrice), #加权平均委买价, double
        ('AltWeightedAvgBidPx', TPrice), #债券加权平均委买价, double
    )
class L2MarketDataOfferOrder(BaseStruct): #Level2委卖信息
    _fields_ = (
        ('TotalOfferQty', TLargeVolume), #委托卖出总量, double
        ('WeightedAvgOfferPx', TPrice), #加权平均委卖价, double
        ('AltWeightedAvgOfferPx', TPrice), #债券加权平均委卖价格, double
    )
class L2MarketDataWarrant(BaseStruct): #Level2权证信息
    _fields_ = (
        ('TotalWarrantExecQty', TLargeVolume), #权证执行总数量, double
        ('WarLowerPx', TPrice), #权证跌停价格, double
        ('WarUpperPx', TPrice), #权证涨停价格, double
    )
class L2MarketDataBase(BaseStruct): #Level2行情基本信息
    _fields_ = (
        ('LastPx', TPrice), #现价, double
    )
class L2MarketDataStatic(BaseStruct): #Level2行情静态属性
    _fields_ = (
        ('PreClosePx', TPrice), #昨收盘价, double
        ('OpenPx', TPrice), #今开盘价, double
        ('ClosePx', TPrice), #收盘价, double
        ('HighPx', TPrice), #最高价, double
        ('LowPx', TPrice), #最低价, double
        ('IOPV', TPrice), #净值估值, double
        ('YieldToMaturity', TRatio), #到期收益率, double
    )
class L2MarketDataPriceLevel(BaseStruct): #Level2价格深度属性
    _fields_ = (
        ('BidPriceLevel', TPriceLevel), #买价深度, int
        ('OfferPriceLevel', TPriceLevel), #卖价深度, int
    )
class NGTSIndex(BaseStruct): #Level2指数行情
    _fields_ = (
        ('TradingDay', TDate), #交易日, char[9]
        ('TimeStamp', TTime), #行情时间（秒）, char[9]
        ('ExchangeID', TExchangeID), #交易所代码, char[9]
        ('SecurityID', TSecurityID), #指数代码, char[13]
        ('PreCloseIndex', TIndex), #前收盘指数, double
        ('OpenIndex', TIndex), #今开盘指数, double
        ('TurnOver', TMoney), #参与计算相应指数的成交金额（元）, double
        ('HighIndex', TIndex), #最高指数, double
        ('LowIndex', TIndex), #最低指数, double
        ('LastIndex', TIndex), #最新指数, double
        ('CloseIndex', TIndex), #今日收盘指数, double
        ('TradeTime', TTime), #成交时间, char[9]
        ('TotalVolumeTraded', TLargeVolume), #参与计算相应指数的交易数量（手）, double
    )

def _init(export=_init):
    env = globals()
    for k in list(env):
        if k not in export: del env[k]
_init()
