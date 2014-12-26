#-*- coding:utf-8 -*-

"""
    与底层无关的交易命令
"""

import logging

from ..common.base import Nope
from .position import POSITION_APPROVE_STATUS

LOWEST_PRIORITY = 9000000

class Command(object):
    def __init__(self,priority=LOWEST_PRIORITY):
        self._priority = priority

    @property
    def priority(self):
        return self._priority

    def __lt__(self,other):     #同优先级比较
        return self._priority < other.priority

    def __gt__(self,other):
        return self._priority > other.priority


class NormalCommand(Command):
    #不做优先级的判定
    pass

class SysCommand(Command):
    def __init__(self,priority):
        assert 100 < priority < 300,str(priority)
        Command.__init__(self,priority)


class LoginCommand(SysCommand):
    pass

class SettlementQueryCommand(SysCommand):
    pass

class SettlementConfirmCommand(SysCommand):
    pass


#priority不写在__init__函数中,目的是放在一起便于比较
#无参数的可以这么整
LOGIN_COMMAND = LoginCommand(priority=101)
SETTLEMENT_QUERY_COMMAND = SettlementQueryCommand(priority=102)
SETTLEMENT_CONFIRM_COMMAND = SettlementConfirmCommand(priority=103)


class TradeCommand(Command):
    def __init__(self,priority):
        assert 1000 < priority < 10000
        Command.__init__(self,priority)


class QueryCommand(Command):
    def __init__(self,priority):
        assert 10000 < priority < 20000
        Command.__init__(self,priority)


class TrivialCommand(Command):
    def __init__(self,priority):
        assert priority > 20000
        Command.__init__(self,priority)


class QueryAccountCommand(QueryCommand):
    pass


class QueryAccountCommand(QueryCommand):
    def __init__(self,stamp):
        Command.__init__(self,10001)
        self.stamp = stamp


class QueryInstrumentCommand(QueryCommand):
    def __init__(self,instrument_id):
        Command.__init__(self,10101)
        self.instrument_id = instrument_id


class QueryInstrumentMarginRateCommand(QueryCommand):
    def __init__(self,instrument_id):
        Command.__init__(self,10102)
        self.instrument_id = instrument_id


class QueryDepthMarketDataCommand(QueryCommand):
    def __init__(self,instrument_id):
        Command.__init__(self,10100)
        self.instrument_id = instrument_id


class QueryPositionCommand(QueryCommand):
    def __init__(self,instrument_id):
        Command.__init__(self,10103)
        self.instrument_id = instrument_id


class QueryPositionDetailCommand(QueryCommand):
    def __init__(self,instrument_id):
        Command.__init__(self,10105)
        self.instrument_id = instrument_id



class ORDER_EXECUTE_MODE:
    CONCURRENT = 0
    SEQUENT = 1


class Instruction(TradeCommand):
    '''
        PositionCommand的组成要素
    '''
    def __init__(self,order,position,priority):
        """
            holder: OpenCommand/CloseCommand
        """
        TradeCommand.__init__(self,priority)
        self._done = False
        self._order = order
        self._position = position
        self.order._trigger_time = 0       #驱动命令的tick的时间, 如果是时间驱动,则必须是最近一个tick的时间. 在下单时间错重新执行的时候用到
        self._last_update_time = 0  #最后更新时间

    @property
    def order(self):
        return self._order

    @property
    def position(self):
        return self._position

    @property
    def contract_name(self):
        return self._order.contract_name

    @property
    def contract(self):
        return self._order.contract

    @property
    def planned(self):
        return self._order.planned

    @property
    def approved(self):
        return self._order.approved

    @property
    def done(self):
        return self._done

    @property
    def trigger_time(self):
        return self._order.trigger_time

    @trigger_time.setter
    def trigger_time(self,ctime):       #驱动命令的tick的时间, 如果是时间驱动,则必须是最近一个tick的时间.
        self._order.trigger_time = ctime

    @property
    def last_update_time(self):
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self,ctime):
        self._last_update_time = ctime

    def set_callback(self,on_approved=Nope,on_reject=Nope,on_done=Nope,on_progress=Nope):
        self._on_approved = on_approved
        self._on_done = on_done
        self._on_progress = on_progress
        self._on_reject = on_reject

    def execute(self,trader):
        #print("Instr:",self.contract_name,self.order.approved)
        if self._order.approved - self._order.accomplished2> 0:
            #print("Instr put:",self.contract_name,self.order.approved)
            trader.put_command(self)

    def on_approved(self,astate=POSITION_APPROVE_STATUS.APPROVED):
        """
            调用此处时,外部已设置好order.approved的数值
        """
        self._on_approved(self,astate)

    def on_progress(self,volume,price):
        self._order.on_progress(volume,price)
        self._on_progress(self,volume,price)

    def on_done(self,volume_traded):
        #print("INSTR:ON_DONE",self.order.contract_name)
        self._done = True
        self._order.on_done(volume_traded)
        self._on_done(self,volume_traded)

    def on_cancelled(self,volume_traded):
        """
            Open/CloseCommand未完成被取消
        """
        self.on_done(volume_traded)

    def on_accept(self,trade_info):
        """
            对Open/Close, 不应当存在不能accepted的情况,故此处也无必要挂接
        """
        self._order.on_accept(trade_info)

    def on_reject(self):
        """
            不应当存在reject情况,也不知道该怎么处理
        """
        self._order.on_reject()
        self._on_reject(self)

    def on_error(self):
        """
            对Open/Close, 不应当存在Error的情况,故此处也无必要挂接
            对Cancelled,为正常情况
        """
        logging.info("执行错误: %s",type(self))
        self._on_reject(self)


class OpenInstruction(Instruction):
    def __init__(self,order,position):
        Instruction.__init__(self,order,position,1002)


class CloseInstruction(Instruction):
    def __init__(self,order,position):
        Instruction.__init__(self,order,position,1001)

class CancelInstruction(TradeCommand):
    """
        此处挂接Receiver,并无实际用处.
        Cancel的效果需要由被其Cancel的命令的RtnOrder来表现.
    """
    def __init__(self,source):
        TradeCommand.__init__(self,1003)
        self._source = source

    @property
    def order(self):
        return self._source.order

    @property
    def contract_name(self):
        return self._source.order.contract_name

    @property
    def instrument_id(self):
        return self._source.order.contract_name

    def execute(self,trader):
        #trader.put_command(self)
        if not self._source.order.done:
            trader.put_command(self)

    def on_approved(self,astate=POSITION_APPROVE_STATUS.APPROVED):  pass    # 不可能被调用
    def on_progress(self,volume,price): pass    # 不可能被调用
    def on_accept(self,trade_info):  pass        # 不可能被调用
    def on_reject(self): pass       # 不可能被调用

    def on_done(self,volume_traded): pass      #不可能被调用

    def on_cancelled(self,volume_traded): pass      #不可能被调用

    def on_error(self):
        """
            对Open/Close, 不应当存在Error的情况,故此处也无必要挂接
            对Cancelled,为正常情况
        """
        logging.info("仅当Cancel命令时,到此处正常(表示原指令已全部成交): %s",type(self))

