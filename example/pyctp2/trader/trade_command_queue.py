# -*- coding:utf-8 -*-
"""
    ctp-trade相关处理
    1. ctp trade_command_queue的处理
    2. ctp SPI -> trade_callback_queue

    #TODO:###
    0. 须处理8:59-9:00以及节间休息下单不成功的事项
        注意下 FTD(期货交易数据交换协议)
        根据文档, OnRtnInstrumentStatus是广播模式下订阅, 问题是TraderSpi的广播模式如何开启?

"""

import threading
import queue
import time
import logging

from . import trade_command
from ..common.macro_command_queue import DeferTradeCommand
from ..common.base import (XCLOSE,
                           XCLOSE_TODAY,
                           BaseObject,
)
from ..trader.position import ORDER_STATUS


class BaseTradeCommandQueue(object):
    """
        线程内模式. put_command后,由run驱动, 调用run之前命令均在队列中
        接收命令
        翻译成CTP所需的模式
        执行命令
        设置命令状态
    """
    #TODO: 须处理8:59-9:00以及节间休息下单不成功的事项, 错误信息返回值中有明确标示么?
    #       应已经处理(失败后再次发单),须确认 2014-11-23

    logger = logging.getLogger('ctp_trade.BaseTradeCommandQueue')

    def __init__(self, env, account):
        self._env = env
        self._account = account
        self._spi = account.spi
        self._queue = queue.PriorityQueue()
        self._last_query_time = 0
        self.init_command_map()
        self._tcq_initialized = False    #未正常初始化,在结算单确认后OK
        self._ref2command = {}      #用于部分需要用refid来获取原来command(中信息)的command缓存

    @property
    def account(self):
        return self._account

    def run(self):
        while not self._queue.empty():
            command = self._queue.get()[1]
            self._exec(command)
    
    def put_command(self, command):
        #print(command.priority,str(command))
        self._queue.put((command.priority, command))

    def _exec(self, command):
        """
            不去主动流控
        """
        command_type = type(command)
        self.command_map[command_type](command)

    def init_command_map(self):
        self.command_map = {
            #SYSTEM
            trade_command.LoginCommand: self.login,
            trade_command.SettlementQueryCommand: self.query_settlement_info,
            trade_command.SettlementConfirmCommand: self.confirm_settlement_info,
            #QUERY
            trade_command.QueryAccountCommand: self.query_account,
            trade_command.QueryInstrumentCommand: self.query_instrument,
            trade_command.QueryInstrumentMarginRateCommand: self.query_instrument_marginrate,  # 直接使用query_instrument, 不需要
            trade_command.QueryDepthMarketDataCommand: self.query_depth_market_data,  # 接使用query_instrument, 不需要
            trade_command.QueryPositionCommand: self.query_position,
            trade_command.QueryPositionDetailCommand: self.query_position_detail,
            trade_command.OpenInstruction:  self.t_open,
            trade_command.CloseInstruction: self.t_close,
            trade_command.CancelInstruction: self.t_cancel,
        }

    #登录与结算单
    def login(self, command):
        #print("login......")
        return self._spi.user_login()

    def on_login_success(self,trading_day):
        self._env.put_macro_command(DeferTradeCommand(self,trade_command.SETTLEMENT_QUERY_COMMAND,1))      #1s后执行查询,以避免流控
        self._env.trading_day = trading_day
        self._account.on_login()

    def query_settlement_info(self, command):
        return self._spi.query_settlement_info()
    
    def confirm_settlement_info(self, command):
        return self._spi.confirm_settlement_info()

    #回调函数
    def on_settlement_info_confirmed(self):
        self._tcq_initialized = True
        self.put_command(trade_command.QueryAccountCommand(self.account.stamp))

    #获取帐户信息
    def query_account(self, command):
        """获取帐户信息
           市值, 可用余额, 保证金等 
        """
        ret,ref_id = self._spi.fetch_trading_account()
        self._ref2command[ref_id] = command
        #print("query_account ref_id:",ref_id)
        return ret

    def on_query_trading_account(self, ref_id, balance, available, margin, locked):
        #print("on_query_account ref_id:",ref_id)
        #print(ref_id,balance,available)
        command = self._ref2command[ref_id] #用于找到时间戳
        self._env.update_account(self.account, command.stamp, balance, available, margin, locked)


    #查询合约
    def query_instrument(self, command):
        return self._spi.fetch_instrument(command.instrument_id)

    def on_query_instrument(self, instrument_id, exchange_id, price_tick, multiple, long_rate, short_rate):
        self._env.update_instrument(instrument_id, exchange_id, price_tick, multiple, long_rate, short_rate)

    def on_instrument_status(self,instrument_id,enter_time,trading_status):
        self._env.update_instrument_status(instrument_id,trading_status)

    #查询保证金
    def query_instrument_marginrate(self, command):
        return self._spi.fetch_instrument_marginrate(command.instrument_id)

    def on_query_instrument_marginrate(self, instrument_id, long_rate, short_rate):
        self._env.update_instrument_marginrate(instrument_id, long_rate, short_rate)

    #查询涨跌停价格
    def query_depth_market_data(self, command):
        return self._spi.fetch_depth_market_data(command.instrument_id)

    def on_query_market_data(self, instrument_id, trading_day, upperlimit_price, lowerlimit_price):
        self._env.update_limit_price(instrument_id, trading_day, upperlimit_price, lowerlimit_price)

    #查询头寸
    def query_position(self, command):
        return self._spi.investor_position(command.instrument_id)

    def query_position_detail(self, command):
        return self._spi.investor_position_detail(command.instrument_id)
    
    #交易处理

    def t_open(self, instruction):
        corder = instruction.order
        #print("t_open:",corder.contract.name,self._spi)
        #instrument_id = corder.get_contract_name()
        instrument_id = instruction.contract_name
        #print("topen:direction:",corder.direction)
        return self._spi.xopen(instrument_id,
                              corder.direction,
                              corder.approved - corder.accomplished2, #将已完成的剪掉
                              corder.target_price,
                              #self.env.calc_target_price(instrument_id,
                              #                           instruction.direction,
                              #                           instruction.base_price,
                              #                           instruction.extra_hops,
                              #                          ),
                            )

    def t_close(self, instruction):
        corder = instruction.order
        #instrument_id = corder.get_contract_name()
        instrument_id = instruction.contract_name
        close_type = instruction.order.atype

        # 也可由CTP自行搞定 其它交易所的平今/平仓转换
        if close_type == XCLOSE_TODAY and not self._env.is_contract_CLOSETODAY(instrument_id):
            #只有必须用CLOSE_TODAY时,才用
            close_type = XCLOSE

        return self._spi.xclose(instrument_id,
                              close_type,  #XCLOSE,XCLOSE_TODAY
                              corder.direction,
                              corder.approved,
                              corder.target_price,
                              #self.env.calc_target_price(instrument_id,corder.direction,corder.base_price,corder.extra_hops),
                            )

    def t_cancel(self, instruction):
        instrument_id = instruction.instrument_id
        trade_info = instruction.order.trade_info
        self._spi.xcancel(instrument_id,
                         trade_info.exchange_id,
                         trade_info.order_sys_id,
                         trade_info.front_id,
                         trade_info.session_id,
                         trade_info.order_ref,
            )

    def on_accept(self,instrument_id,direction,volume,price,uid,trade_info):
        self._env.matcher.on_accept(uid,instrument_id,direction,volume,price,trade_info)

    def on_reject(self,instrument_id,direction,volume,price,error_id):
        #print("TCQ:reject")
        self._env.matcher.on_reject(instrument_id,direction,volume,price,error_id)

    def on_rtn_order(self,uid,order_status,volume_traded=0):
        """委托回报
           反映执行状态
        """
        #print("tcq:on_rtn_order:uid=",uid)
        if order_status == ORDER_STATUS.CANCELLED or order_status == ORDER_STATUS.PART_SUCCESSED or order_status == ORDER_STATUS.SUCCESSED:
            #self.env.get_matcher().on_cancelled(uid,volume_traded)
            self._env.matcher.on_done(uid,volume_traded,order_status)
        #elif order_status == ORDER_STATUS.PART_TRADED:
        #    self.env.get_matcher().on_done(uid,volume_traded,order_status)
        #elif order_status == ORDER_STATUS.ALL_TRADED:
        #    self.env.get_matcher().on_done(uid,volume_traded,order_status)
        elif order_status == ORDER_STATUS.LOCAL_REJECT or order_status == ORDER_STATUS.EXCHANGE_REJECT: #不可能出现,已经走on_reject了
            #self.env.get_matcher().on_error(uid)
            pass
        else:   #等
            print("异常情况 %s:%d" % (uid,volume_traded))

    def on_trade(self,uid,trade_date,trade_time,volume,price):
        """
            volume为当次成交数,而非累积数
            在on_rtn_order中, 成交数为累积数
            只能使用OnTrade中的数据,因为RtnOrder中没有成交价格信息
        """
        self._env.matcher.on_progress(uid,volume,price,trade_date,trade_time)

    #错误处理#
    def on_error(self, ref_id, instrument_id, error_id, error_msg):
        logging.info('instrument %s: request_id %s:error_id %s:error_msg %s' % (ref_id, instrument_id, error_id, error_msg))

    #开始运行之前的委托回报,成交回报
    def on_pre_rtn_order(self,front_id,session_id,ref_id,instrument_id,insert_time,volume_total,volume_traded):
        #1. 是否需要都撤单? 对于单帐户多路值守, 撤单是不正确的
        #2. 对前次登陆时的挂单撤单时,会收到以前次登陆的front_id+session_id为关键字的on_rtn_order
        print('收到之前委托回报,front_id=%s,session_id=%s,ref_id=%s' % (front_id,session_id,ref_id))
        pass

    def on_pre_trade(self,exchange_id,order_sys_id,trade_time,instrument_id,volume,price):
        pass

    def on_other_rtn_order(self,front_id,session_id,ref_id,instrument_id,insert_time,volume_total,volume_traded):
        """
            这个现在已经不再用了
        """
        pass

    def on_other_trade(self,exchange_id,order_sys_id,trade_time,instrument_id,volume,price):
        """
            这个现在已经不再用了
        """
        pass



class TradeCommandQueue(threading.Thread,BaseTradeCommandQueue):
    """
        独立线程模式
        接收命令
        翻译成CTP所需的模式
        执行命令
        设置命令状态
    """

    logger = logging.getLogger('ctp_trade.CTPTradeCommandQueue')

    def __init__(self, env, account):
        threading.Thread.__init__(self)
        BaseTradeCommandQueue.__init__(self,env,account)

    def run(self):
        while 1:
            command = self._queue.get()[1]
            self._exec(command)


class TradeCommandQueueStub(BaseTradeCommandQueue):
    """
        Stub模式
        把队列绕过了,而直接在putcommand中搞定
        步子迈得有点大. 会导致在集成中测试不到队列相关语句. 和BaseTradeCommandQueue相比,优点是不需要额外调用run
            确定在策略通路测试/集成模拟/时使用Stub
        建议在 实盘行情模拟 时使用BaseTradeCommandQueue,用put_command/run组合来解决问题
    """

    logger = logging.getLogger('ctp_trade.CTPTradeCommandQueueStub')

    def __init__(self, env, account):
        BaseTradeCommandQueue.__init__(self,env,account)
        self.lock = threading.Lock()

    def start(self):    #提供一致性接口
        pass

    def run(self):      #提供一致性接口
        pass

    def put_command(self, command):
        #print("TCQStub:",command.priority,str(command))
        self._exec(command)


    #获取帐户信息
    def query_account(self, command):
        """获取帐户信息
           市值, 可用余额, 保证金等
            #所有需要设定 _ref2command[ref_id]的方法, 即返回值与时间有关的,如查询头寸等,均须先peek设定ref_id之后再调用
            #其实在实盘交易中,这么做也没啥错.就是复杂化了,所以把测试和实盘分开
        """
        #因为直通调用的关系,导致在on_query_account时,_ref2command[ref_id]还没有设定,即在测试中onXXXX是在fetch_trading_account中调用
        #如果需要用到ref_id,就会出现 Key Error
        #因此,在调用fetch_trading_account()之前必须先得到ref_id. 对于测试环境而言此为应有之义
        with self.lock:     #加锁是为了避免在 实盘行情模拟交易时  引发潜在的竞争条件
            ref_id = self._spi.peep_next_request_id()
            self._ref2command[ref_id] = command
            ret,ref_id2 = self._spi.fetch_trading_account()
        assert ref_id,ref_id2
        #print("query_account ref_id:",ref_id)
        return ret
