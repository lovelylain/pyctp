# -*- coding: utf-8 -*-

cdef extern from "ThostFtdcLevel2UserApiDataType.h":
    cdef enum TE_RESUME_TYPE "THOST_TE_RESUME_TYPE": #流重传方式
        TERT_RESTART "THOST_TERT_RESTART" #从本交易日开始重传
        TERT_RESUME "THOST_TERT_RESUME" #从上次收到的续传
        TERT_QUICK "THOST_TERT_QUICK" #只传送登录后的流内容
    ctypedef char[11] TBrokerIDType "TThostFtdcBrokerIDType" #经纪公司代码
    ctypedef char[9] TBrokerAbbrType "TThostFtdcBrokerAbbrType" #经纪公司简称
    ctypedef char[81] TBrokerNameType "TThostFtdcBrokerNameType" #经纪公司名称
    ctypedef char[16] TUserIDType "TThostFtdcUserIDType" #用户代码
    ctypedef char[81] TUserNameType "TThostFtdcUserNameType" #用户名称
    ctypedef char[41] TPasswordType "TThostFtdcPasswordType" #密码
    ctypedef char[21] TProductNameType "TThostFtdcProductNameType" #产品名称
    ctypedef char[9] TExchangeIDType "TThostFtdcExchangeIDType" #交易所代码
    ctypedef char[31] TExchangeNameType "TThostFtdcExchangeNameType" #交易所名称
    ctypedef char[9] TExchangeAbbrType "TThostFtdcExchangeAbbrType" #交易所简称
    ctypedef char[2] TExchangeFlagType "TThostFtdcExchangeFlagType" #交易所标志
    ctypedef char[21] TMacAddressType "TThostFtdcMacAddressType" #Mac地址
    ctypedef char[9] TDateType "TThostFtdcDateType" #日期
    ctypedef char[9] TTimeType "TThostFtdcTimeType" #时间
    ctypedef char[13] TLongTimeType "TThostFtdcLongTimeType" #长时间
    ctypedef char[21] TTradeIDType "TThostFtdcTradeIDType" #成交编号
    ctypedef char[16] TIPAddressType "TThostFtdcIPAddressType" #IP地址
    ctypedef char[11] TProductInfoType "TThostFtdcProductInfoType" #产品信息
    ctypedef char[11] TProtocolInfoType "TThostFtdcProtocolInfoType" #协议信息
    ctypedef char[41] TSystemNameType "TThostFtdcSystemNameType" #系统名称
    ctypedef char TInstrumentStatusType "TThostFtdcInstrumentStatusType" #合约交易状态
    enum: IS_BeforeTrading "THOST_FTDC_IS_BeforeTrading" #开盘前
    enum: IS_NoTrading "THOST_FTDC_IS_NoTrading" #非交易
    enum: IS_Continous "THOST_FTDC_IS_Continous" #连续交易
    enum: IS_AuctionOrdering "THOST_FTDC_IS_AuctionOrdering" #集合竞价报单
    enum: IS_AuctionBalance "THOST_FTDC_IS_AuctionBalance" #集合竞价价格平衡
    enum: IS_AuctionMatch "THOST_FTDC_IS_AuctionMatch" #集合竞价撮合
    enum: IS_Closed "THOST_FTDC_IS_Closed" #收盘
    ctypedef int TInstallCountType "TThostFtdcInstallCountType" #安装数量
    ctypedef int TInstallIDType "TThostFtdcInstallIDType" #安装编号
    ctypedef int TErrorIDType "TThostFtdcErrorIDType" #错误代码
    ctypedef char[81] TErrorMsgType "TThostFtdcErrorMsgType" #错误信息
    ctypedef int TFrontIDType "TThostFtdcFrontIDType" #前置编号
    ctypedef int TSessionIDType "TThostFtdcSessionIDType" #会话编号
    ctypedef int TSequenceNoType "TThostFtdcSequenceNoType" #序号
    ctypedef int TMillisecType "TThostFtdcMillisecType" #时间（毫秒）
    ctypedef int TTradingSegmentSNType "TThostFtdcTradingSegmentSNType" #交易阶段编号
    ctypedef int TRequestIDType "TThostFtdcRequestIDType" #请求编号
    ctypedef int TYearType "TThostFtdcYearType" #年份
    ctypedef int TMonthType "TThostFtdcMonthType" #月份
    ctypedef int TBoolType "TThostFtdcBoolType" #布尔型
    ctypedef double TPriceType "TThostFtdcPriceType" #价格
    ctypedef double TRatioType "TThostFtdcRatioType" #比率
    ctypedef double TMoneyType "TThostFtdcMoneyType" #资金
    ctypedef int TVolumeType "TThostFtdcVolumeType" #数量
    ctypedef double TLargeVolumeType "TThostFtdcLargeVolumeType" #大额数量
    ctypedef short TSequenceSeriesType "TThostFtdcSequenceSeriesType" #序列系列号
    ctypedef short TCommPhaseNoType "TThostFtdcCommPhaseNoType" #通讯时段编号
    ctypedef char[2] TSequenceLabelType "TThostFtdcSequenceLabelType" #序列编号
    ctypedef char[51] TChannelType "TThostFtdcChannelType" #渠道
    ctypedef char[101] TAddressType "TThostFtdcAddressType" #通讯地址
    ctypedef char[7] TZipCodeType "TThostFtdcZipCodeType" #邮政编码
    ctypedef char[41] TTelephoneType "TThostFtdcTelephoneType" #联系电话
    ctypedef char[41] TFaxType "TThostFtdcFaxType" #传真
    ctypedef char[41] TMobileType "TThostFtdcMobileType" #手机
    ctypedef char[41] TEMailType "TThostFtdcEMailType" #电子邮件
    ctypedef char[161] TMemoType "TThostFtdcMemoType" #备注
    ctypedef char[4] TVersionType "TThostFtdcVersionType" #版本号
    ctypedef char[9] TTradeDateType "TThostFtdcTradeDateType" #交易日期
    ctypedef char[9] TTradeTimeType "TThostFtdcTradeTimeType" #交易时间
    ctypedef char[129] TAuthInfoType "TThostFtdcAuthInfoType" #客户端认证信息
    ctypedef char[17] TAuthCodeType "TThostFtdcAuthCodeType" #客户端认证码
    ctypedef char[13] TSecurityIDType "TThostFtdcSecurityIDType" #证券代码
    ctypedef int TPriceLevelType "TThostFtdcPriceLevelType" #价格深度
    ctypedef double TIndexType "TThostFtdcIndexType" #指数
