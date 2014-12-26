# -*- coding:utf-8 -*-

from ..trader.environ import Environ
from ..trader.coordinator import Coordinator,CashCoordinator
from ..common.controller import TController

class CommonBuilder(object):
    def __init__(self,env,triples,tday=0):
        """
            triples为三元组列表, 其元素三元组组成如下:
                    (Coordinator(类),Strategy(类), contract_manager(对象))
        """
        self._env = env
        self._triples = triples
        self._tday = tday
        self._coordinators = []
        self._initialize(triples)

    def _initialize(self,triples):
        for coordinator_clazz,strategy_clazz,contract_manager in triples:
            self._coordinators.append(coordinator_clazz(self._env,strategy_clazz,contract_manager,self._tday))

    @property
    def tday(self):
        return self._tday


def xbuild(env:Environ):
    pass
