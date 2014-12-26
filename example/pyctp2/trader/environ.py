# -*- coding:utf-8 -*-

'''
    基础框架数据结构
    在此层次之上, 为策略组织层

    对于交易节的处理
        比如在8:59-9:00, 10:15-10:30, 11:30-13:30的间断时间, 通过延迟发送的方式来处理
        并订阅tick时间驱动的事件
'''

import logging
import threading
import time
import collections
from random import randint
from functools import reduce

from ..common.base import (LONG,
                           MAX_VALUE,
                          )
from ..common.macro_command_queue import (TickMacroCommandQueue,SecMacroCommandQueue,
                                          DeferTradeCommand,
                                )
from ..common.contract_type import CM_ALL
from ..trader.position import POSITION_APPROVE_STATUS
from ..common.controller import TController

from ..trader.trade_command import (QueryInstrumentCommand,
                                    QueryInstrumentMarginRateCommand,
                                    QueryDepthMarketDataCommand,
                                   )
from ..trader.trade_matcher import TradeMatcher

#from trader.account import Account


class Environ(object):
    '''
        包含内容:
            交易合约信息:
                合约, update_time, 保证金率, 涨跌停板
        Trader SPI: 

    '''
    logger = logging.getLogger('trader.Environ')

    def __init__(self,Controller=TController,TickMCQ=TickMacroCommandQueue,SecMCQ=SecMacroCommandQueue):
        '''
            MCQ: 宏命令队列类. 将此作为参数纯粹为了Stub时替换方便
            ###madd: 期货公司保证金加点. 取多个账户的最大值. 只在试算时用到. 已经用不到了,直接从合约查询中取到
        '''
        #self.account_map = {}
        self._account_map = collections.OrderedDict()    #保序dict,确保get_account(0)获得的是第一个插入的
        self._lock = threading.Lock()
        self._trading_day = 0
        #self.reset_contracts([])
        self._contracts = {}
        #self._madd = madd
        #self._cash_quotient = 3        #用CashCoordinator来稿定
        #设定MacroCommandQueue
        self._tick_macro_command_queue = TickMCQ()
        self._tick_macro_command_queue.start()
        self._second_macro_command_queue = SecMCQ()
        self._second_macro_command_queue.start()
        self._controller = Controller(self._tick_macro_command_queue) #controller
        self._matcher = TradeMatcher(self)
        ##coordinators
        self._coordinators = set()

    def initialize(self):
        """
            在外部基本初始化完成之后被调用
        """
        self._controller.reset()
        #print(self._controller._contracts)
        self.reset_contracts(self._controller.contracts)

    @property
    def controller(self):
        return self._controller

    @property
    def matcher(self):
        return self._matcher

    @property
    def trading_day(self):
        return self._trading_day

    @trading_day.setter
    def trading_day(self,tday):
        self._trading_day = tday

    def register_account(self,account):
        self._account_map[account.id] = account
        #Account的进一步初始化动作, 用MacroCommandQueue来实现

    def register_coordinator(self,coord):
        self._coordinators.add(coord)

    def unregister_coordinator(self,coord):
        if coord in self._coordinators:
            self._coordinators.remove(coord)

    def get_account(self,index=0):
        return list(self._account_map.values())[index]

    def get_account_by_name(self,acc_name):
        return self._account_map[acc_name]

    def calc_strategy_balance(self,coord):
        #获得coord相对的准备金 (注意, 准备金 = 可用资金 + 持仓保证金 + 已锁定保证金)
        if coord not in self._coordinators:
            return 0
        total_shares = sum([c.shares for c in self._coordinators])
        balances = sum([a.balance for a in self._account_map.values()])
        coord.balance = coord.shares/total_shares * balances
        return coord.balance

    def reset_contracts(self,contracts):
        """
            #必须在每日开始时调用,可用MacroCommandQueue来设定
            在完整运行后(设定了Account)才可以调用,否则 对合约的查询没法工作
        """
        assert len(self._account_map) > 0, "请至少设定一个Account后再调用本方法"
        self._contracts = dict([(c.name,c) for c in contracts])
        #print(self._contracts.keys())
        self.query_contract_info()

    def query_contract_info(self):
        account = self.get_account()    #取得第一个account
        tqueue = account.trade_queue
        defered = 10        #10秒后开始动作
        for contract in self._contracts.values():
            #print("query:",contract.name)
            qic = QueryInstrumentCommand(contract.name)
            qirc = QueryInstrumentMarginRateCommand(contract.name)
            qdc = QueryDepthMarketDataCommand(contract.name)        #获得停板价
            defered += 1
            self.put_macro_command(DeferTradeCommand(tqueue,qic,defered))
            defered += 1
            self.put_macro_command(DeferTradeCommand(tqueue,qirc,defered))
            defered += 1
            self.put_macro_command(DeferTradeCommand(tqueue,qdc,defered))

    def is_contract_CLOSETODAY(self,contract_name):
        """
            contract是否属于CLOSETODAY族
            需要测试确认exchangeID
        """
        return self._contracts[contract_name].exchange_id == "SHFE"

    @property
    def macro_queue(self):  #默认为秒驱动队列
        return self.sec_macro_queue

    def put_macro_command(self,command):    #默认为秒驱动队列
        self.put_sec_macro_command(command)

    @property
    def tick_macro_queue(self):
        return self._tick_macro_command_queue

    def put_tick_macro_command(self,command):
        #print(self._tick_macro_command_queue)
        self._tick_macro_command_queue.put_command(command)

    @property
    def sec_macro_queue(self):
        return self._second_macro_command_queue

    def put_sec_macro_command(self,command):
        self._second_macro_command_queue.put_command(command)

    def execute_trade_command(self,command):
        #print("in execute trade command")
        self._matcher.execute(command)

    def approve_open(self,orders):
        '''
            对单个order，采用修改方式
            对多个order,采用一致性的过或不过
            并设定account
            返回是否部分或全部OK
        '''
        with self._lock:
            #print("accounts[0].available:",self.get_account().available)
            #for instr in instructions:
            #    self.approve_one(instr.order)
            for order in orders:
                self.approve_one(order)
            if len(orders) == 1:
                logging.info("开仓锁定数:%d",orders[0].approved)
                return POSITION_APPROVE_STATUS.APPROVED if orders[0].approved > 0 else POSITION_APPROVE_STATUS.REJECTED
            else:
                release_flag = False
                for order in orders:
                    if order.approved < order.planned:
                        release_flag = True
                        break
                #print("release_flag:",release_flag,self.get_account().available)
                if release_flag:    #需要回滚
                    logging.info("开仓锁定失败")
                    for order in orders:
                        #print("relase amount:",order.approved_amount)
                        self.get_account_by_name(order.account).release_prelock(order.approved_amount)
                        order.approve(0,0)
                        #order.lock_time = 0
                        #order.approved_amount = 0
                    return POSITION_APPROVE_STATUS.REJECTED
                logging.info("开仓锁定成功")
                return POSITION_APPROVE_STATUS.APPROVED
        
    def approve_one(self,order):
        #target_price在Order初始化时计算
        #order.target_price = self.calc_target_price(order.contract_name,
        #                                            order.direction,
        #                                            order.base_price,
        #                                            order.extra_hops
        #                    )
        #amount1 = self._calc_margin(order.contract_name,order.direction,order.target_price)
        #amount1 = order.contract.calc_margin(order.direction,order.target_price)
        amount1 = order.calc_margin()
        wanted_amount = amount1 * order.planned
        #print(instruction.get_contract_name(),wanted_amount)
        acc,approve_amount = self._which(wanted_amount)
        #print(acc.id,approve_amount,amount1,wanted_amount)
        order.account = acc.id
        approved_volume = order.planned if approve_amount >= wanted_amount else int(approve_amount/amount1)
        real_approved_amount = approved_volume * amount1
        order.approve(approved_volume,real_approved_amount)
        #print("order.approved:",order.contract_name,approved_volume,real_approved_amount)
        logging.info("%s approved, volume= %d,amount=%02f",order.contract_name,approved_volume,real_approved_amount)
        acc.prelock(order.approved * amount1)    #里面还有一个锁，会不会死锁?
        #order.approved_amount = order.approved * amount1
        #print("order approved amount",order.approved_amount)
        #order.lock_time = time.time()

    def _calc_margin(self,instrument_id,direction,target_price):
        '''
            #deprecated, 请直接调用order.calc_margin
            计算单手保证金
        '''
        contract = self._contracts[instrument_id]
        #marginrate = contract.long_marginrate if direction==LONG else contract.short_marginrate
        #cmarginrate = marginrate + self._madd
        ####margin = contract.multiple * contract.upperlimit_price * cmarginrate
        #margin = contract.multiple * target_price * cmarginrate
        ####print(instrument_id,marginrate,cmarginrate,contract.multiple,target_price,margin)
        return contract.calc_margin(direction,target_price)

    def _which(self,amount):
        '''
            确定采用哪个spi
            必须确保单个命令由单个spi完成
            如果均不能满足，则取最大余额的账户
        '''
        accs = list(self._account_map.values())
        if len(accs) == 1:
            #print("len=1")
            acc = accs[0]
            #print("可用金额:",acc.available)
            return acc,amount if acc.available >= amount else acc.available
        ci = randint(0,len(accs)-1)
        #print(ci)
        acc = accs[ci]
        #print("可用金额:",acc.available)
        if acc.available >= amount:
            return acc,amount
        else:    # 找到第一个符合要求的,如果找不到,则返回最大的那个
            cacc = acc
            #print("before loop,cacc=",cacc.get_id(),cacc.available,amount)
            for acc2 in accs:
                if acc2.available >= amount:
                    return acc2,amount
                if acc2.available > cacc.available:
                    cacc = acc2
            return cacc,cacc.available

    def update_account(self,account,stamp,balance,available,margin,locked): 
        '''
            虽然调用者可以直接调用account.update
            但为统一起见，Account的所有update方法均从Environ发起
        '''
        account.update(stamp,balance,available,margin,locked)

    def update_instrument(self,instrument_id,exchange_id,price_tick,multiple,long_rate=0.12,short_rate=0.12):
        '''
            exchange_id:交易所编号, 用来区分平今/平仓
            price_tick:最小变动单位
            multiple:合约乘数
            long_rate:多头保证金率,原始保证金率,没有意义
            short_rate:空头保证金率,原始保证金率,没有意义
            没有加锁必要，即便被竞争，数据也应当一样
        '''
        if instrument_id not in self._contracts:
            self.logger.error("收到未注册的contract的合约更新信息:%s" % instrument_id)
            return
        c = self._contracts[instrument_id]
        c.exchange_id = exchange_id
        c.price_tick = price_tick
        c.multiple = multiple
        #c.long_marginrate = long_rate      # 这里返回的数据是原始保证金率,没有意义,需要从update_instrument_marginrate中处理
        #c.short_marginrate = short_rate

    def update_instrument_status(self,instrument_id,trading_status):
        """
            此处instrument_id是品种名字
        """
        try:
            ctype = CM_ALL.tname2ctype(instrument_id)
            ctype.trading_status = trading_status
        except KeyError:
            self.logger.error("收到未知品种的状态更新信息:%s" % instrument_id)
        #if instrument_id not in self._contracts:
        #    self.logger.error("收到未注册的contract的合约状态更新信息:%s" % instrument_id)
        #    return
        #c = self._contracts[instrument_id]
        #c.status = is_on_trading

    def update_limit_price(self,instrument_id,trading_day,upperlimit_price,lowerlimit_price):
        '''
            更新涨跌停价格
            没有加锁必要，即便被竞争，数据也应当一样
        '''
        if instrument_id not in self._contracts:
            self.logger.error("收到未注册的contract的保证金率更新信息:%s" % instrument_id)
            return
        c = self._contracts[instrument_id]
        c.trading_day = trading_day
        c.upperlimit_price = upperlimit_price
        c.lowerlimit_price = lowerlimit_price

    def update_instrument_marginrate(self,instrument_id,long_marginrate,short_marginrate):
        '''
            返回规则调整后的保证金率
        '''
        c = self._contracts[instrument_id]
        #print(id(c),c.name,c.long_marginrate,c.short_marginrate)
        c._long_marginrate = long_marginrate
        c._short_marginrate = short_marginrate
        #print(id(c),c.name,c.long_marginrate,c.short_marginrate)


