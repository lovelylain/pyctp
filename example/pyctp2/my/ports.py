# -*- coding:utf-8 -*-

from ..trader.ports_info import PortsInfo


ZSBroker = "6010"

ZSUserPort1 = "tcp://115.238.34.151:41213"
ZSUserPort2 = "tcp://140.206.112.130:41213"
ZSUserPort3 = "tcp://124.160.35.53:41213"
ZSUserPort4 = "tcp://180.166.1.17:41205"

ZSTraderPort1 = "tcp://180.166.1.17:41205"
ZSTraderPort2 = "tcp://115.238.34.151:41205"
ZSTraderPort3 = "tcp://140.206.112.130:41205"
ZSTraderPort4 = "tcp://124.160.35.53:41205"

ZSUserPortsA =[ZSUserPort1, ZSUserPort2, ZSUserPort3, ZSUserPort4]
ZSTraderPortsA = [ZSTraderPort1, ZSTraderPort2, ZSTraderPort3, ZSTraderPort4]
ZSUserPortsB =[ZSUserPort3, ZSUserPort4, ZSUserPort1, ZSUserPort2]


ZSUsers = PortsInfo("ZSUserA",ZSUserPortsA,ZSBroker)
ZSTraders = PortsInfo("ZSTraderA",ZSTraderPortsA,ZSBroker)
ZSUsersB = PortsInfo("ZSUserB",ZSUserPortsB,ZSBroker)   #更改连接顺序

ZSUsersC = PortsInfo("ZSUserA",[ZSUserPort1,ZSUserPort4],ZSBroker)