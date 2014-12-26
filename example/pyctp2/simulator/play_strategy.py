# -*- coding:utf-8 -*-
"""
    用于player的策略
"""

import logging

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

from ..trader.position import (GlobalCloser, CloserParameter,Closer,LongCloserParameter2,
                    )

from ..trader.strategy import POPEN,PCLOSE,PCLOSE2
from ..trader.strategy_agent import StrategyAgent


class SExampleA(BaseStrategy):
    """
        Strategy示例. 即刻平仓
    """

    def __init__(self,holder,max_times_per_day=5):
        BaseStrategy.__init__(self,holder)
        self.is_full = False
        self.max_lost = 50      #以最小跳动为单位
        self.cur_day = 0
        self.cur_times = 0
        self.max_times_per_day = max_times_per_day
        self.ntick = 0

    def check_open(self,ctick,CA):
        """
            直接发出信号
        """
        #print("in check_open")
        self.ntick += 1
        if self.is_full:
            #print("A: is full")
            return []
        if ctick.date > self.cur_day:
            self.cur_day = ctick.date
            self.cur_times = 0
        if self.cur_times > self.max_times_per_day: #超出最大
            #print("A: times exceed")
            return []
        self.cur_times += 1
        #print("--------------A open time:",ctick.time,self.ntick,self.cur_times)
        logging.info("SExampleA check_open time:%d,ntick=%d,cur_times=%d",ctick.time,self.ntick,self.cur_times)
        #print("in check_open,",ctick.instrument,ctick.time)
        closer_params = CloserParameter(extremum = ctick.price,stop_line = ctick.price - self.max_lost*CA._ctype._unit)
        closer = Closer(self._check_close,closer_params)
        cmd = POPEN(contract=CA,direction=LONG,base_price=CA.last_price,closers=[closer],extra_hops=30) #targe_price=baseprice+hops*tick,extra_hops=MAX_VALUE/-MAX_VALUE则为停板
        print(cmd)
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
        logging.debug("in calc_open_volume,clen=%d",clen)
        if clen == 0:
            #print("in COV:0")
            popen.unit = popen.planned = int(self.available_balance // popen.contract.calc_margin(popen.direction,popen.base_price))//2
            logging.info("开仓数>0,available_balance=%d,base_price=%d,margin=%02f,unit=%d",self.available_balance,popen.base_price,popen.contract.calc_margin(popen.direction,popen.base_price),popen.unit)
            print("available_balance=%d,base_price=%d,margin=%02f" % (self.available_balance,popen.base_price,popen.contract.calc_margin(popen.direction,popen.base_price)))
            #print("calc_open_volume: planned=",popen.planned)
        elif clen == 1:
            popen.planned = popen.unit = cpositions[-1].volume_holding // 2  #已有仓位的1/2
            logging.info("开仓数>0,available_balance=%d,base_price=%d,margin=%02f,unit=%d",self.available_balance,popen.base_price,popen.contract.calc_margin(popen.direction,popen.base_price),popen.unit)
        else:   #这一次是空转, 放这里是为了节省一次self._holder.get_positions_by_name(popen.contract.name),也可以放在前面，在open信号初步判断后再确认仓位是否已经满了,那样更加符合直觉
            logging.info("本次开仓数为0")
            self.is_full = True
            popen.planned = popen.unit = 0

    def _check_close(self,ctick,position,params,CA):
        '''
            CA为目标Contract
            params为CloserParameter对象,包含如下内容:
                stopline
                extremum:   开仓后的极值
        '''
        #return []
        cur_price = CA.last_price
        cmd=PCLOSE(position,base_price=cur_price,volume=position.volume_holding,extra_hops=30)  #单合约策略，只有pst[0]有效
        self.is_full = False
        return [cmd]


class  SExampleA5(SExampleA):
    def __init__(self,holder):
        SExampleA.__init__(self,holder)
        self.xtick = 0

    def check_open(self,ctick,CA):
        rev = SExampleA.check_open(self,ctick,CA)
        if rev:
            self.xtick = self.ntick
        return rev

    def _check_close(self,ctick,position,params,CA):
        if self.ntick > self.xtick + 5:
            print("A5 close time:",ctick.time,self.ntick)
            return SExampleA._check_close(self,ctick,position,params,CA)


class SExampleAB(BaseStrategy):
    '''
        即刻平仓
        需要根据所跟踪的多个ticks,组合成目标tick
        比如跟踪CA,CB且比例为1, 则新目标的tick = CA.tick - CB.tick
        这样，实际上target的ticks的长度是 len(CA.ticks) + len(CB.ticks)
    '''
    def __init__(self,holder):
        BaseStrategy.__init__(self,holder)
        self.is_full = False
        self.max_lost = 50      #以最小跳动为单位
        self.ntick = 0
        self.ntrade = 0
        self.max_trade = 5

    def prepare(self,ctick,CA,CB):
        pass

    def day_finalize(self):
        self.ntrade = 0

    def check_open(self,ctick,CA,CB):
        '''
            CA为目标Contract
        '''
        #print("in check open")
        self.ntick += 1
        if self.is_full or self.ntick < 3 or self.ntrade >= self.max_trade:
            return []

        print("-----------AB open time:",ctick.time,self.ntick)
        #print(CA.name,CB.name)
        closer_params = LongCloserParameter2(extremum = CA.last_price-CB.last_price,stop_line = CA.last_price-CB.last_price - self.max_lost*(CA.unit+CB.unit)/2)
        closer = GlobalCloser(self._check_close,closer_params)
        cmd1 = POPEN(contract=CA,direction=LONG,base_price=CA.last_price,closers=[closer],extra_hops=30) #targe_price=baseprice+hops*tick,extra_hops=MAX_VALUE/-MAX_VALUE则为停板
        cmd2 = POPEN(contract=CB,direction=LONG,base_price=CB.last_price,closers=[closer],extra_hops=30) #targe_price=baseprice+hops*tick,extra_hops=MAX_VALUE/-MAX_VALUE则为停板
        return [cmd1,cmd2]

    def calc_open_volume(self,instructionA,instructionB):
        '''
            只有在state=SE_STATE.EMPTY时才重新计算，其余均以已有仓位为基准
            next_state用于开仓跨越状态的情况，比如正常需要state0->state1, 但实际价格波动剧烈，需要state0-->state2,这样在开仓数上应当有区别
                基本不需要
            self.cordinator
        '''
        self.ntrade += 1
        ca_positions = self._holder.get_positions_by_name(instructionA.contract.name)
        cb_positions = self._holder.get_positions_by_name(instructionB.contract.name)
        ca_len = len(ca_positions)
        cb_len = len(cb_positions)
        assert ca_len == cb_len
        #print(instructionA.contract.name,instructionB.contract.name)
        if ca_len == 0:
            #instructionA.wanted = 2 #按比例设定
            #instructionB.wanted = 1
            margin_a =  instructionA.contract.calc_margin(instructionA.direction,instructionA.base_price) * 1.2
            margin_b =  instructionB.contract.calc_margin(instructionB.direction,instructionB.base_price)
            #print(instructionA.base_price,instructionB.base_price,margin_a,margin_b)
            times = int(self.available_balance // (margin_a + margin_b)) // 2
            instructionA.unit = instructionA.planned = 1.2 * times
            instructionB.unit = instructionB.planned = 1 * times
            #print(instructionA.planned,instructionB.planned)
            #print(instructionA.base_price,instructionB.base_price,margin_a,margin_b)
            #print("------------------times:",times)
        elif ca_len == 1:
            instructionA.planned = instructionA.unit = ca_positions[-1].volume_holding // 2  #已有仓位的1/2
            instructionB.planned = instructionB.unit = cb_positions[-1].volume_holding // 2  #已有仓位的1/2
        elif ca_len == 2:
            instructionA.planned = instructionA.unit = 19  #仅用于测试
            instructionB.planned = instructionB.unit = 29
        else:
            self.is_full = True
            instructionA.planned = instructionA.unit = 0
            instructionB.planned = instructionB.unit = 0


    def _check_close(self,ctick,position_map,params,CA,CB):
        '''
            CA,CB为目标Contract
        '''
        ca_poses = position_map[CA.name]
        cb_poses = position_map[CB.name]
        assert len(ca_poses) == len(cb_poses)
        if len(ca_poses) == 0:
            return []

        ca_pos = ca_poses[-1]
        cb_pos = cb_poses[-1]

        ca_price = CA.last_price
        cb_price = CB.last_price
        instr_a = PCLOSE(ca_pos,base_price=ca_price,volume=ca_pos.volume_holding,extra_hops=30)
        instr_b = PCLOSE(cb_pos,base_price=cb_price,volume=cb_pos.volume_holding,extra_hops=30)
        #instr_a = PCLOSE(ca_pos,base_price=ca_price,volume=1,extra_hops=30)
        #instr_b = PCLOSE(cb_pos,base_price=cb_price,volume=1,extra_hops=30)
        self.is_full = False
        return [instr_a,instr_b]


class  SExampleAB5(SExampleAB):
    def __init__(self,holder):
        SExampleAB.__init__(self,holder)
        self.xtick = 0

    def check_open(self,ctick,CA,CB):
        rev = SExampleAB.check_open(self,ctick,CA,CB)
        if rev:
            self.xtick = self.ntick
        return rev

    def _check_close(self,ctick,position_map,params,CA,CB):
        if self.ntick > self.xtick + 5:
            print("---------------A5 close time:",ctick.time,self.ntick)
            return SExampleAB._check_close(self,ctick,position_map,params,CA,CB)
