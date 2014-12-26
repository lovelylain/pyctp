# -*- coding:gbk -*-
"""
        deprecated, 直接使用TraderSpiDelegate + trader_api_stub
        Mock TraderSPI, 提供统一的桩位, 用以测试TradeCommandQueue是否正确
        不验证上层参数是否正确,只提供通道

"""
import logging
from datetime import datetime

from ctp.futures import ApiStruct as UType

from ..trader import trade_command
from ..common.base import (BaseObject,
                           LONG,SHORT,
                           XCLOSE,XCLOSE_TODAY,
            )
from ..common.contract_type import CM_ALL as call
from ..trader.position import ORDER_STATUS


class TraderSpiStub(object):
    logger = logging.getLogger('ctp.TraderSpiStub')

    def __init__(self,available,margin=0,frozen_margin=0):
        self._trade_command_queue = None
        self._available = available  #可用金额
        self._margin = margin        #保证金
        self._frozen_margin = frozen_margin
        #self._macro_command_queue = macro_command_queue
        #更新数据用
        self.reset_login_info()
        #order_ref => command 的映射, 用于在回调中获取相关信息
        self._ref_map = {}
        self._first_login_time = 0
        self._infos = []
        self._exchange_id = "EX_STUB"
        self._cur_order_sys_id = 10000

    @property
    def broker(self):
        return self._broker

    @property
    def investor(self):
        return self._investor

    @property
    def balance(self):
        return self._available + self._margin + self._frozen_margin

    @property
    def front_id(self):
        return self._login_info.front_id

    @property
    def session_id(self):
        return self._login_info.session_id

    @property
    def queue(self):
        #return self._trade_command_queue
        raise TypeError("不支持读取TraderSpiDelegate的trade_command_queue")

    @queue.setter
    def queue(self,queue):
        self._trade_command_queue = queue

    @property
    def trading_day(self):
        return self._login_info.trading_day

    @trading_day.setter
    def trading_day(self,trading_day):
        self._login_info.trading_day = trading_day

    def inc_order_sys_id(self):
        self._cur_order_sys_id += 1
        return self._cur_order_sys_id

    def reset_login_info(self):
        self._login_info = BaseObject(front_id="FRONT_STUB", session_id='SS_STUB', order_ref=0,
                                      trading_day=datetime.today().strftime("%Y%m%d"),
                                      is_logged = False, is_settlement_info_confirmed = False
                )

    def inc_request_id(self):
        self._login_info.order_ref += 1
        return self._login_info.order_ref

    #def delay_command(self, command, delta):
    #    self.macro_command_queue.put_command(DelayedCommand(command, delta))

    def day_finalize(self):
        self.reset_login_info()

    #回复状态处理

    ##交易初始化
    #登陆,确认结算单
    def OnFrontConnected(self):
        """
            当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        """
        self.logger.info('TD:trader front connected')
        self._trade_command_queue.put_command(trade_command.LOGIN_COMMAND)

    def OnFrontDisconnected(self, nReason):
        self.logger.info('TD:trader front disconnected, reason=%s' % (nReason, ))

    def user_login(self):
        self.logger.info('TD:trader to login')
        ref_id = self.inc_request_id()
        self.logger.info('TD:trader to login, issued')
        self._trade_command_queue.on_login_success(datetime.today().strftime("%Y%m%d"))
        return 0


    def query_settlement_info(self):
        #不填日期表示取上一天结算单, 并在响应函数中确认
        self.logger.info('TD:取上一日结算单信息并确认, BrokerID=%s, investorID=%s' % (self.broker, self.investor))
        #time.sleep(1)   #避免流控, 因为此时ticks未必已经开始动作, 故不采用macro_command_queue方式. 这里因为不再查询结算单是否已确认, 所以已经没有流控限制
        ref_id = self.inc_request_id()
        self._trade_command_queue.put_command(trade_command.SETTLEMENT_CONFIRM_COMMAND)
        return 0

    def confirm_settlement_info(self):
        self.logger.info('TD-CSI:准备确认结算单')
        ref_id = self.inc_request_id()
        self._trade_command_queue.on_settlement_info_confirmed()
        return 0

    #交易准备
    #获取帐户资金
    def fetch_trading_account(self):
        #获取资金帐户
        logging.info('A:获取资金帐户..')
        ref_id = self.inc_request_id()
        self._trade_command_queue.on_query_trading_account(ref_id, self.get_balance(), self._available, self._margin, self._frozen_margin)
        return 0,ref_id


    # 获取持仓
    def fetch_investor_position(self, instrument_id):
        #获取合约的当前持仓
        logging.info('A:获取合约%s的当前持仓..' % (instrument_id, ))
        ref_id = self.inc_request_id()
        #logging.info('A:查询持仓, 函数发出返回值:%s' % rP)
        return 0,ref_id

    # 获取持仓明细
    def fetch_investor_position_detail(self, instrument_id):
        """
            获取合约的当前持仓明细，目前没用
        """
        logging.info('A:获取合约%s的当前持仓..' % (instrument_id, ))
        ref_id = self.inc_request_id()
        #logging.info('A:查询持仓, 函数发出返回值:%s' % r)
        return 0,ref_id

    #获取合约保证金率
    def fetch_instrument_marginrate(self, instrument_id):
        """
            保证金率都设定为0.1
        """
        ref_id = self.inc_request_id()
        self._trade_command_queue.on_query_instrument_marginrate(instrument_id, 0.1, 0.1)
        return 0

    #查询合约信息
    def fetch_instrument(self, instrument_id):
        ref_id = self.inc_request_id()
        ctype = call.cname2ctype(instrument_id)
        self._trade_command_queue.on_query_instrument(instrument_id,
                                                         ctype.exchange_name,
                                                         ctype.unit,
                                                         ctype.multiplier,
                                                         0.1,
                                                         0.1,
                                                    )
        return 0


    #获取行情信息, 目的在于获取当日涨跌停价格
    def fetch_depth_market_data(self, instrument_id):
        ref_id = self.inc_request_id()
        self._trade_command_queue.on_query_market_data(instrument_id,
                                                          self._trading_day,
                                                          99999999,
                                                          0,
                                                         )
        return 0

    #交易部分
    #开仓
    def r2uid(self,trading_day,exchange_id,order_sys_id):
        uid = "%s:%s:%s" % (trading_day,exchange_id,order_sys_id)

    def get_ctp_direction(self,direction):
        #print(direction)
        return UType.D_Buy if direction == LONG else UType.D_Sell

    def xopen(self, instrument_id, direction, volume,price):
        #print("xopen",instrument_id,volume,price)
        order_sys_id = self.inc_order_sys_id()
        uid = self.r2uid(self._trading_day,self._exchange_id,order_sys_id)
        trade_info = BaseObject(front_id=self._login_info.front_id,
                                session_id=self.get_session_id(),
                                trading_day=self._trading_day,
                                exchange_id=self._exchange_id,
                                order_sys_id=order_sys_id
                    )

        ctype = call.cname2ctype()
        self._trade_command_queue.on_accept(instrument_id, direction, volume, price,uid,trade_info)
        #print("xopen",instrument_id,volume,price)
        self._trade_command_queue.on_rtn_order(uid,ORDER_STATUS.SUCCESSED,volume)
        trade_time = datetime.now().strftime("%H%M%S")
        self._trade_command_queue.on_trade(uid,self._trading_day,trade_time,volume,price)
        return 0

    def xclose(self, instrument_id, close_type,direction, volume,price):
        """
            上期所区分平昨和平今
                搞反的话就会被CTP直接拒绝. 如平昨来平当日仓,且无足够昨仓,就会报:综合交易平台：平昨仓位不足
        """
        order_sys_id = self.inc_order_sys_id()
        uid = self.r2uid(self._trading_day,self._exchange_id,order_sys_id)
        trade_info = BaseObject(front_id=self._login_info.front_id,
                                session_id=self.get_session_id(),
                                trading_day=self._trading_day,
                                exchange_id=self._exchange_id,
                                order_sys_id=order_sys_id
                    )

        self._trade_command_queue.on_accept(instrument_id, direction, volume, price,uid,trade_info)
        self._trade_command_queue.on_rtn_order(uid,ORDER_STATUS.SUCCESSED,volume)
        trade_time = datetime.now().strftime("%H%M%S")
        self._trade_command_queue.on_trade(uid,self._trading_day,trade_time,volume,price)
        return 0

    def xcancel(self,instrument_id,exchange_id,order_sys_id,front_id,session_id,order_ref):
        """
            Mock中不会有任何效果
        """
        self.logger.info('SPI_XC:取消命令')
        ref_id = self.inc_request_id()
        #orderActionRef是一个可有可无的值,设置错了也无关紧要
        return 0

