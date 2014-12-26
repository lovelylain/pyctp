# -*- coding:utf-8 -*-
"""
    tick读取和播放模拟
    单品种策略模拟
"""

#通用文件
import logging
import time
import os

#配置文件
from ..my.ports import ZSUsers

#功能文件
from ..common import base
from ..trader.builder import CommonBuilder
from ..trader.environ import Environ
from ..common.utils import next_trading_day
from ..common.contract_type import M,P
from ..common.reader import read_tick
from ..common.controller import TController,Controller
from ..trader import strategy_agent
from ..trader.strategy_agent import StrategyAgent
from ..common import cjson

#夹具
from ..common.macro_command_queue import PassiveMacroCommandQueue
from ..test.account_stub import AccountStub

INIT_AVAILABLE = 1000000
TRADING_DAY = 20140101

base.DATA_PATH = base.SIMULATOR_DATA_PATH        #必须在导入其它之前
strategy_agent.STATE_FNAME = base.SIMULATOR_STATE_PATH + '/positions.%s.txt'
strategy_agent.TRADE_FNAME = base.SIMULATOR_STATE_PATH + '/trade.%s.txt'

exchange_fname = base.SIMULATOR_STATE_PATH + '/exchange.txt'

class Player(object):
    def __init__(self,triples):
        self._env = Environ(Controller=Controller,TickMCQ=PassiveMacroCommandQueue,SecMCQ=PassiveMacroCommandQueue)
        self._account = AccountStub(self._env,ZSUsers,id="acc1",available=INIT_AVAILABLE)
        self._api = self._account.api
        self._builder = CommonBuilder(self._env,triples,TRADING_DAY)
        self._contracts = set()
        self.lastday = 99999999

    def prepare(self,lastday=99999999):
        self._contracts.clear()
        self.lastday = lastday
        for agent in self._env.controller.agents:
            agent.resume(lastday)
            for c in agent.contracts:
                self._contracts.add(c)
        self._env.reset_contracts(self._contracts)
        for c in self._contracts:
            #print(c.name)
            self._env.update_instrument(c.name,"TEST",1,5,0,0)         #初始数据, 实际运行中也须对跟踪的contract设置
            #self._env.update_instrument_marginrate(c.name,0.12,0.12)   #多空保证金率均按0.12计算
            #self._env.update_limit_price() #不需要,初始化时已经搞定
            self._api._add_contract(c)
        #print(self._env.controller.agents)
        self._env._controller.reset()

        if os.path.exists(exchange_fname):
            with open(exchange_fname,'rt') as sf:
                self._api._exchange = cjson.load(sf)    #hack方式,本质上不允许直接set


        #根据coordinator中各agent的持仓，去设定trade_api_stub中的持仓
        """ #deprecated, 用stub.load
        holdings = []
        for agent in self._env.controller.agents:
            print(agent.name,[c.name for c in agent.contracts])
            if isinstance(agent,StrategyAgent):
                holdings.extend(agent.get_holding_info().values())
        mholding = {}
        for holding in holdings:
            if holding.contract_name in mholding:
                mholding[holding.contract_name].add(holding)
            elif holding.total > 0:
                mholding[holding.contract_name] = holding
        #print("mholding:",mholding.values())
        for holding in mholding.values():
            print(holding.contract_name,holding.num_long,holding.num_short)
        self._api.exchange.resume(mholding.values())
        """

        #self._env._controller.start()  #只对TController有意义

    def play(self,endday=0):    # 不包含endday
        if endday == 0:
            endday = next_trading_day(self._builder.tday)
        xday = next_trading_day(self.lastday)
        while xday < endday:
            self.play1(xday)
            with open(exchange_fname,'wt') as sf:
                cjson.dump(self._api.exchange,sf)
            xday = next_trading_day(xday)


    def play1_TController(self,xday):
        """
            执行xday的ticks数据
        """
        tickss = []
        for c in self._contracts:
            cticks = read_tick(c.name,xday)
            print("first:",c.name,len(cticks))
            tickss.extend(cticks)
        tickss.sort(key=lambda t:(t.time,t.msec))
        #print("总长度:",len(tickss))
        #print(xday)
        i = 0
        for tick in tickss:
            #print(self._env._controller)
            #print("tick-A:",i)
            #i+=1
            self._api.new_tick(tick)    #设定last_tick,只有在模拟的时候才需要
            self._env._controller.new_tick(tick)    ##如果使用TController,这里因为self._api.new_tick是直接设定,而controller.new_tick是队列处理,所以每次都会有差异
            #print("tick-B:",i)

            #print(t.instrument,t.sdate,t.time,t.msec)
        #print(list(self._env.controller.agents)[0])
        while(not self._env._controller._queue.empty()):    #等待处理完毕,只有对TController有意义
            time.sleep(0.05)
        #for c in self._contracts:
        #    print("next:",c.name,len(c.ticks))
        self._env._controller.day_finalize()

    def play1(self,xday):
        """
            执行xday的ticks数据
        """
        tickss = []
        for c in self._contracts:
            cticks = read_tick(c.name,xday)
            #print("first:",c.name,len(cticks))
            tickss.extend(cticks)
        tickss.sort(key=lambda t:(t.time,t.msec))
        #print("总长度:",len(tickss))
        #print(xday)
        i = 0
        print("trading_day:",xday,"---------------------------------------")
        for tick in tickss:
            #print(self._env._controller)
            #print("tick-A:",i)
            i+=1
            self._api.new_tick(tick)    #设定last_tick,只有在模拟的时候才需要
            self._env._controller.new_tick(tick)    #
            #print("tick-B:",i)

            #print(t.instrument,t.sdate,t.time,t.msec)
        #print(list(self._env.controller.agents)[0])
        #for c in self._contracts:
        #    print("next:",c.name,len(c.ticks))
        #print("day_finalizing:",xday)
        self._env._controller.day_finalize()
        #print("day_finalized:",xday)


from ..common.contract_type import ContractManager
from ..trader.coordinator import Coordinator
from .play_strategy import SExampleA,SExampleAB,SExampleA5,SExampleAB5

def splay1():
    logging.basicConfig(filename="%s/pyctp2_play.log" % (base.SIMULATOR_PATH, ),
                        level=logging.DEBUG,
                        format="%(module)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s"
                    )
    cm1 = ContractManager([M])
    triples = [ (Coordinator,SExampleA,cm1),
                #(Coordinator,SExampleAB,cm1),
            ]
    player = Player(triples)
    player.prepare(20140925)
    #player.play(20141009)
    #player.play(20141001)
    player.play(20140927)

def splay1_5():
    cm1 = ContractManager([M])
    triples = [ (Coordinator,SExampleA5,cm1),
                #(Coordinator,SExampleAB,cm1),
            ]
    player = Player(triples)
    player.prepare(20140925)
    #player.play(20141009)
    #player.play(20141001)
    player.play(20140927)


def splay3():
    cm1 = ContractManager([M])
    triples = [ (Coordinator,SExampleA,cm1),
                (Coordinator,SExampleA,cm1),
                (Coordinator,SExampleA,cm1),
            ]
    player = Player(triples)
    player.prepare(20140925)
    #player.play(20141009)
    #player.play(20141001)
    player.play(20140927)

def splay1b():
    cm1 = ContractManager([M,P])
    triples = [
                (Coordinator,SExampleAB,cm1),
            ]
    player = Player(triples)
    player.prepare(20140925)
    player.play(20141009)
    #player.play(20141001)
    #player.play(20140927)

def splay1b_5():
    #logging.basicConfig(filename="%s/player.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    cm1 = ContractManager([M,P])
    triples = [
                (Coordinator,SExampleAB5,cm1),
            ]
    player = Player(triples)
    player.prepare(20140925)
    #player.play(20141009)
    #player.play(20141001)
    player.play(20140927)


def splay3b():
    cm1 = ContractManager([M,P])
    triples = [ (Coordinator,SExampleAB,cm1),
                (Coordinator,SExampleAB,cm1),
                (Coordinator,SExampleAB,cm1),
            ]
    player = Player(triples)
    player.prepare(20140925)
    player.play(20141009)
    #player.play(20141001)
    #player.play(20140927)

def splay13():
    cm1 = ContractManager([M])
    cm2 = ContractManager([M,P])
    triples = [ (Coordinator,SExampleA,cm1),
                (Coordinator,SExampleAB,cm2),
            ]
    player = Player(triples)
    player.prepare(20140925)
    #player.play(20141009)
    #player.play(20141001)
    player.play(20140927)



from ..common.base import TEST_PATH

if __name__ == '__main__':
    """
        不能直接执行
        因为使用了相对路径导入,不能直接执行
        需要在quant目录下:
        python red.py pyctp2.simulator.player play
    """
    logging.basicConfig(filename="%s/pyctp2_play.log" % (base.SIMULATOR_PATH, ),
                        level=logging.DEBUG,
                        format="%(module)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s"
                    )
    splay1()


