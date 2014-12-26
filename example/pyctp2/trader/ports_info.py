# -*- coding: utf-8 -*-

import getpass

class PortsInfo(object):
    def __init__(self, name, ports, broker, investor=""):
        """
            CTP连接信息,
            ports为port列表, 其元素为 "tcp://aaa.bbb.ccc.ddd:ppppp"形式
            MDUser不需要输入investor

        """
        self.name = name
        self.ports = ports
        self.broker = broker
        self.investor = investor
        self.passwd = ""

    def input_account(self):
        self.investor = input("输入用户名:")
        self.passwd = getpass.getpass("输入登陆口令:")

class PortsStub(object):
    def __init__(self):
        self.name = "PortsStub"
        self.ports = []
        self.broker = "BrokerOfStub"
        self.investor = "InvestorOfStub"
        self.passwd = ""

    def input_account(self):
        pass
