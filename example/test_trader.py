#-*- coding:utf-8 -*-

import hashlib, os, sys, tempfile, time
from ctp.futures import ApiStruct, TraderApi

class MyTraderApi(TraderApi):
    def __init__(self, brokerID, userID, password, instIDs):
        print 'into __init__'
        self.requestID = 0
        self.brokerID = brokerID
        self.userID = userID
        self.password = password
        self.instrumentIDs = instIDs
        self.Create()

    def Create(self):
        print 'into create'
        dir = b''.join((b'ctp.futures', self.brokerID, self.userID))
        dir = hashlib.md5(dir).hexdigest()
        dir = os.path.join('./', dir, 'Trader') + os.sep
        if not os.path.isdir(dir): os.makedirs(dir)
        TraderApi.Create(self, dir)

    def RegisterFront(self, front):
        print 'into registerfront'
        if isinstance(front, bytes):
            print front
            return TraderApi.RegisterFront(self, front)
        for ifront in front:
            TraderApi.RegisterFont(self, ifront)

    def OnFrontConnected(self):
        print('OnFrontConnected: login...')
        req = ApiStruct.ReqUserLogin(BrokerID=self.brokerID,
                                     UserID=self.UserID,
                                     Password=self.password)
        self.requestID += 1
        self.ReqUserLogin(req, self.requestID)

if __name__ == '__main__':
    traderapi = MyTraderApi(b'2030', b'354079', b'481531', [b'cu1412'])
    traderapi.RegisterFront(b'tcp://asp-sim2-front1.financial-trading-platform.com:26205')
    traderapi.SubscribePublicTopic(1)
    traderapi.SubscribePrivateTopic(1)
    traderapi.Init()


    #SubscribePrivateTopic(nResumeType)
    # THOST_TERT_RESTART 从本交易日开始重传
    # THOST_TERT_RESUME 从上次收到的续传
    # THOST_TERT_QUICK 只传送登录后私有流的内容
    # before init
    #SubscribePublicTopic(nResumeType)
    # 同上

    #OnFrontConnected()
    #ReqAuthenticate(pReqAuthenticate, nRequestID)
    #OnRspAuthenticate(pRspAuthenticate, pRsqInfo, nRequestID, bIsLast)
    #ReqUserLogin(pReqUserLogin, nRequestID)
    #OnRspUserLogin(pRspUserLogin, pRspInfo, nRequestID, bIsLast)
    #ReqSettlementInfoConfirm(pSettlementInfoConfirm, nRequestID)


    #if ReqQrySettlementInfoConfirm(pQSIC, nRequestID):
    #    pass

    try:
        pass
    except KeyboardInterrupt:
        pass
