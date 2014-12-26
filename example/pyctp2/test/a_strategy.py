# -*- coding:utf-8 -*-
"""
    单合约策略例子
"""
from ..common.base import (XOPEN,
                           XCLOSE,
                           LONG,
                           SHORT,
                           BaseObject,
                           MAX_VALUE,
                    )

from ..common.contract_type import ContractInfo

from ..trader.strategy import (BaseStrategy,
                    )

from ..trader.position import (Closer,
                               CloserParameter,
                               ContractCloser,
                    )

from ..trader.trade_command import (Instruction,
                    )

from ..core.dac import (MA,
                        UPCROSS,
                    )

from ..trader.strategy import POPEN,PCLOSE,PCLOSE2
from ..trader.strategy_agent import StrategyAgent


class SExampleA(BaseStrategy):
    """
        Strategy示例
        不对其状态持久化. 因此Strategy的状态只能是中间的计算状态
        同时,因为持久化的原因, close_func函数必须是Strategy的实例方法,否则无法定位
    """

    def __init__(self,holder):
        BaseStrategy.__init__(self,holder)
        self.is_full = False
        self.max_lost = 50      #以最小跳动为单位
        self.cur_day = 0
        self.cur_times = 0
        self.max_times_per_day = 50

    def check_open(self,ctick,CA):
        """
            直接发出信号
        """
        if self.is_full:
            return
        #if ctick.date > self.cur_day:
        #    self.cur_day = ctick.date
        #    self.cur_times = 0
        #if self.cur_times > self.max_times_per_day: #超出最大
        #    return []
        #self.cur_times += 1
        #print("in check_open,",ctick.instrument,ctick.time)
        closer_params = CloserParameter(extremum = ctick.price,stop_line = ctick.price - self.max_lost*CA._ctype._unit)
        closer = Closer(self._check_close,closer_params)
        cmd = POPEN(contract=CA,direction=LONG,base_price=CA.last_price,closers=[closer],extra_hops=30) #targe_price=baseprice+hops*tick,extra_hops=MAX_VALUE/-MAX_VALUE则为停板
        return [cmd]

    def calc_open_volume(self,popen):
        '''
            只有在state=SE_STATE.EMPTY时才重新计算，其余均以已有仓位为基准
            #next_state用于开仓跨越状态的情况，比如正常需要state0->state1, 但实际价格波动剧烈，需要state0-->state2,这样在开仓数上应当有区别
            #    基本不需要
            self.cordinator
        '''
        cpositions = self._holder.get_positions_by_name(popen.contract.name)
        clen = len(cpositions)
        #print("in calc_open_volume,clen=",clen)
        if clen == 0:
            #print("in COV:0")
            #print("available_balance=%d,base_price=%d,margin=%02f" % (self.available_balance,popen.base_price,popen.contract.calc_margin(popen.direction,popen.base_price)))
            popen.unit = popen.planned = int(self.available_balance // popen.contract.calc_margin(popen.direction,popen.base_price))//2
            #print("calc_open_volume: planned=",popen.planned)
        elif clen == 1:
            popen.planned = popen.unit = cpositions[-1].volume_holding // 2  #已有仓位的1/2
        else:
            self.is_full = True
            popen.planned = popen.unit = 0

    def _check_close(self,ctick,position,params,CA):
        '''
            CA为目标Contract
            params为CloserParameter对象,包含如下内容:
                stopline
                extremum:   开仓后的极值
        '''
        cur_price = CA.last_price
        cmd=PCLOSE(position,base_price=cur_price,volume=position.volume_holding,extra_hops=30)  #单合约策略，只有pst[0]有效
        return [cmd]


class SExampleA2(BaseStrategy):
    """
        Strategy示例,使用PCLOSE2
    """

    def __init__(self,holder):
        BaseStrategy.__init__(self,holder)
        self.is_full = False
        self.max_lost = 50      #以最小跳动为单位

    def check_open(self,ctick,CA):
        """
            直接发出信号
        """
        if self.is_full:
            return
        closer_params = CloserParameter(extremum = ctick.price,stop_line = ctick.price - self.max_lost*CA._ctype._unit)
        closer = ContractCloser(self._check_close,closer_params)
        cmd = POPEN(contract=CA,direction=LONG,base_price=CA.last_price,closers=[closer],extra_hops=30) ##targe_price=baseprice+hops*tick,extra_hops=MAX_VALUE/-MAX_VALUE则为停板
        return [cmd]

    def calc_open_volume(self,popen):
        '''
            只有在state=SE_STATE.EMPTY时才重新计算，其余均以已有仓位为基准
            #next_state用于开仓跨越状态的情况，比如正常需要state0->state1, 但实际价格波动剧烈，需要state0-->state2,这样在开仓数上应当有区别
            #    基本不需要
            self.cordinator
        '''
        cpositions = self._holder.get_positions_by_name(popen.contract.name)
        clen = len(cpositions)
        if clen == 0:
            #print("in COV:0")
            popen.planned = int(self.available_balance // popen.contract.calc_margin(popen.direction,popen.base_price))/2
            #popen.unit = 1
        elif clen == 1:
            #print("COV:",cpositions[-1].holding_volume)
            popen.planned = cpositions[-1].volume_holding // 2  #已有仓位的1/2
            #popen.unit = 1
            #print("COV:2:",popen.planned,popen.wanted)
        else:
            self.is_full = True
            popen.planned = 0
            popen.unit = 0

    def _check_close(self,ctick,volume,params,CA):
        '''
            CA为目标Contract
            params为CloserParameter对象,包含如下内容:
                stopline
                extremum:   开仓后的极值
        '''
        cur_price = CA.last_price
        cmd=PCLOSE2(CA,base_price=cur_price,direction=SHORT,volume=volume,extra_hops=30)
        return [cmd]


class SExampleA3(BaseStrategy):
    """
        Strategy示例,使用PCLOSE2, 且分两次close
    """

    def __init__(self,holder):
        BaseStrategy.__init__(self,holder)
        self.is_full = False
        self.max_lost = 50      #以最小跳动为单位

    def check_open(self,ctick,CA):
        """
            直接发出信号
        """
        if self.is_full:
            return
        closer_params = CloserParameter(extremum = ctick.price,stop_line = ctick.price - self.max_lost*CA._ctype._unit)
        closer = ContractCloser(self._check_close,closer_params)
        cmd = POPEN(contract=CA,direction=LONG,base_price=CA.last_price,closers=[closer],extra_hops=30) #targe_price=baseprice+hops*tick,extra_hops=MAX_VALUE/-MAX_VALUE则为停板
        return [cmd]

    def calc_open_volume(self,popen):
        '''
            只有在state=SE_STATE.EMPTY时才重新计算，其余均以已有仓位为基准
            #next_state用于开仓跨越状态的情况，比如正常需要state0->state1, 但实际价格波动剧烈，需要state0-->state2,这样在开仓数上应当有区别
            #    基本不需要
            self.cordinator
        '''
        cpositions = self._holder.get_positions_by_name(popen.contract.name)
        clen = len(cpositions)
        if clen == 0:
            popen.planned = int(self.available_balance // popen.contract.calc_margin(popen.direction,popen.base_price))/2
            #popen.unit = 1
        elif clen == 1:
            #print("COV:",cpositions[-1].holding_volume)
            popen.planned = cpositions[-1].volume_holding // 2  #已有仓位的1/2
            #popen.unit =
            #print("COV:2:",popen.planned,popen.wanted)
        else:
            self.is_full = True
            popen.planned = 0
            popen.unit = 0

    def _check_close(self,ctick,volume,params,CA):
        '''
            CA为目标Contract
            params为CloserParameter对象,包含如下内容:
                stopline
                extremum:   开仓后的极值
        '''
        cur_price = CA.last_price
        if volume > 1:
            cmd=PCLOSE2(CA,base_price=cur_price,direction=SHORT,volume=volume-1,extra_hops=30)
        else:
            cmd=PCLOSE2(CA,base_price=cur_price,direction=SHORT,volume=volume,extra_hops=30)
        return [cmd]

