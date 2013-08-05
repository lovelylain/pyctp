# -*- coding: utf-8 -*-

from __future__ import absolute_import as _init

__all__ = ['Level2ApiStruct', 'Level2Api']

if 0: from . import Level2ApiStruct
Level2ApiStruct = __import__(__name__.rsplit('.',1)[0]+'.Level2ApiStruct', None, None, 'x')

class Level2Api(object):
    def Create(self, pszFlowPath='', bIsUsingUdp=False):
        """创建UserApi
        @param pszFlowPath 存贮订阅信息文件的目录，默认为当前目录
        @return 创建出的UserApi
        modify for udp marketdata
        """

    def Release(self):
        """删除接口对象本身
        @remark 不再使用本接口对象时,调用该函数删除接口对象
        """

    def Init(self):
        """初始化
        @remark 初始化运行环境,只有调用后,接口才开始工作
        """

    def Join(self):
        """等待接口线程结束运行
        @return 线程退出代码
        """
        return 0

    def GetTradingDay(self):
        """获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        """
        return ''

    def RegisterFront(self, pszFrontAddress):
        """注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol:
        ipaddress:port”，如：”tcp:
        127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        """

    def SubscribeLevel2MarketData(self, pSecurityList, nCount):
        return 0

    def UnSubscribeLevel2MarketData(self, pSecurityList, nCount):
        return 0

    def SubscribeNGTSIndex(self, pSecurityList, nCount):
        return 0

    def UnSubscribeNGTSIndex(self, pSecurityList, nCount):
        return 0

    def SubscribePublicTopic(self, nResumeType):
        """订阅公共流。
        @param nResumeType 公共流重传方式
                THOST_TERT_RESTART:从本交易日开始重传
                THOST_TERT_RESUME:从上次收到的续传
                THOST_TERT_QUICK:只传送登录后公共流的内容
        @remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
        """

    def ReqUserLogin(self, pReqUserLogin, nRequestID):
        """用户登录请求"""
        return 0

    def ReqUserLogout(self, pUserLogout, nRequestID):
        """登出请求"""
        return 0

    def OnFrontConnected(self):
        """当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。"""

    def OnFrontDisconnected(self, nReason):
        """当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        @param nReason 错误原因
                0x1001 网络读失败
                0x1002 网络写失败
                0x2001 接收心跳超时
                0x2002 发送心跳失败
                0x2003 收到错误报文
        """

    def OnHeartBeatWarning(self, nTimeLapse):
        """心跳超时警告。当长时间未收到报文时，该方法被调用。
        @param nTimeLapse 距离上次接收报文的时间
        """

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        """登录请求响应"""

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        """登出请求响应"""

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        """错误应答"""

    def OnRspSubLevel2MarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        """订阅Level2行情应答"""

    def OnRspUnSubLevel2MarketData(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        """取消订阅Level2行情应答"""

    def OnRspSubNGTSIndex(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        """订阅Level2指数行情应答"""

    def OnRspUnSubNGTSIndex(self, pSpecificSecurity, pRspInfo, nRequestID, bIsLast):
        """取消订阅Level2指数行情应答"""

    def OnRtnLevel2MarketData(self, pLevel2MarketData):
        """Level2行情通知"""

    def OnRtnNGTSIndex(self, pNGTSIndex):
        """Level2指数行情通知"""

def _init(Level2Spi=Level2Api):
    G = globals(); del G['_init']
    Level2Spi = dict((k,v) for k,v in Level2Spi.__dict__.items() if k.startswith('On'))
    from ._Level2Api import _init, Level2Api; _init(Level2ApiStruct)
    G['Level2Api'] = type('Level2Api', (Level2Api,), Level2Spi)
_init()
