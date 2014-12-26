# -*- coding: utf-8 -*-

"""
    独立出从command -> 实际发出命令的衔接层
    将command的抽象执行状态放到这个层面来处理, 以统一处理多端互备
"""

import threading

from .trade_command import TradeCommand
from ..common.macro_command_queue import MacroCommand
from ..common.errors import TradeError

class TradeMatcher(object):
    """
        只有3类交易命令:
        1. Open
        2. Close
        3. Cancel   #不再有透明的主动Cancel操作,因为多合约情况下无法正常处理
    """
    def __init__(self,env):
        self._env = env
        self._wlist = {}     #未匹配的命令,已拆细
        self._mlist = {}     #已匹配的命令,已拆细
        self._rlist = {}     #已拒绝命令
        self._is_master = True   #是否是主交易端,只有主交易端才能发出实际的交易命令
        self._mylock = threading.Lock()

    def execute(self,command):
        """
            command中的Order此时已经被赋Account
        """
        #print("TradeMatcher:in execute command")
        if not isinstance(command,TradeCommand): #实际上不应当在这里出现
            #print("in trader matcher:execute: OtherCommand")
            acc = self._env.get_account_by_name(command.account)  #command必须被赋
            acc.put_command(command)
            return
        #print("in trader matcher:execute: TradeCommand",command.order.contract.name,command.order.planned)


        order = command.order
        acc = self._env.get_account_by_name(order.account)
        with self._mylock:
            mykey = self._info2key(order.contract_name,
                                             order.direction,
                                             #order.approved,
                                             order.net_approved,    #净批准数, 去除transfered的手数
                                             order.target_price,
                    )
            self._wlist.setdefault(mykey,[]).append(command)
            #print(mykey)
            #print(order.contract_name,".direction:",order.direction)
        if self._is_master:
            #print("trade_matcher:execute:",order.contract_name,".direction:",order.direction)
            command.execute(acc)


    def _info2key(self,instrument_id,direction,volume,target_price):
        mykey = "%s:%s:%d:%d" % (instrument_id,direction,volume,target_price)
        return mykey


    def on_accept(self,uid,instrument_id,direction,volume,price,trade_info):
        """
            #接收订单后的第一次调用, CTP情况下为交易所接受时调用
            可能会有两次调用, CTP接受一次,交易所接受一次. 需要兼容这个情况
        """
        ckey = self._info2key(instrument_id,direction,volume,price)
        #print(ckey,self.wlist)
        assert ckey in self._wlist,"订单接收时,必然还未关联,但已经在等待列表中,key=%s" % (ckey,)
        cinstr = None
        with self._mylock:
            mylist = self._wlist[ckey]
            if mylist:
                cinstr = mylist[0]
                del mylist[0]
                self._mlist[uid] = cinstr
        #print(cinstr,trade_info)
        if cinstr:   #减少锁的占用时间
            #cinstr.order.trade_info = trade_info
            cinstr.on_accept(trade_info)

    def on_reject(self,instrument_id,direction,volume,price,error_id):
        ckey = self._info2key(instrument_id,direction,volume,price)
        #print("ON_REJECT:",ckey,self.wlist)
        #assert ckey in self.wlist or ckey in self.rlist,"被拒绝订单应当在系统中"   #实际上有可能不成立,如手工订单
        if ckey not in self._wlist:
            #可能是手工订单被拒绝,
            #print("TM:REJECT:",ckey,",error_id:",error_id)
            return
        cinstr = None
        with self._mylock:
            mylist = self._wlist[ckey]
            if mylist:  #reject在被交易所拒绝时可能调用两次,一次OnErrRtnOrderInsert,一次OnRtnOrder(reject).第二次时mylist==[]
                cinstr = mylist[0]
                del mylist[0]
                self._rlist.setdefault(ckey,[]).append(cinstr)
        #print("TM:REJECT:2:",ckey,cinstr)
        if cinstr:  #减少锁的占用时间,此处需要根据reject原因来处理是否重新执行
            if error_id == TradeError.TIME_ERROR:
                if self.re_execute(cinstr): #重新执行部署成功
                    pass
                else:   #不能重新执行
                    cinstr.on_reject()
            else:
                cinstr.on_reject()

    def on_progress(self,uid,volume,price,trade_date,trade_time):
        """
            逐笔交易信息
        """
        #print("TM:on_progress:",uid,volume,price)
        if uid not in self._mlist:
            #需要处理交易系统外的成交?
            return
        cinstr = self._mlist[uid]
        cinstr.last_update_time = "%s%s" % (trade_date,trade_time[-6:])
        cinstr.on_progress(volume,price)

    def on_done(self,uid,volume_traded,order_status):
        """
            交易完成信息
            次序是:
                on_done =>
                最后一笔交易的on_progress
        """
        #print("TradeMatcher:On_done:",uid)
        if uid not in self._mlist:
            #需要处理交易系统外的成交?
            return
        cinstr = self._mlist[uid]
        #cinstr.order.state = order_status
        if not cinstr.done:   #可能多次被调用? 应该不可能,这里为便利测试多个分支而设定
            #print("TM:on_done")
            cinstr.on_done(volume_traded)

    def on_error(self,uid):
        pass

    def re_execute(self,cinstr):
        """
        当命令时间段错误时, 重新调度到合适的时间执行
            不支持跨交易日
            1. 不能准确算出第二个交易日, 如果计算出的正好不是交易日,则会在第一个tick到来(集合竞价)时执行,然后再拒再执行,即到第二个tick才执行
            2. 容易引起执行不了的问题, 因为会有较大的隔夜价差
        返回 True表示重新设定成功
             False表示不能重新执行(因为原触发时点无误等)
        """
        cur_time = cinstr.trigger_time%1000000
        cur_minute = cur_time//100
        next_minute = cinstr.contract.calc_next_trade_minute(cur_minute)
        if next_minute>0:
            next_time = cinstr.trigger_time - cur_time + next_minute*100
            #next_time = cinstr.trigger_time //1000000*1000000 + next_minute*100
            mc = MacroCommand(self.execute,cinstr,next_time)
            #print(cur_minute,next_minute,cur_time,next_time,cinstr.trigger_time - cur_time)
            self._env.put_tick_macro_command(mc)
            return True
        else:
            return False
