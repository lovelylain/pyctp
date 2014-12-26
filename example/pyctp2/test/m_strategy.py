# -*- coding:utf-8 -*-

"""
    双合约策略例子
"""

from ..common.base import (XOPEN,
                           XCLOSE,
                           LONG,
                           SHORT,
                           BaseObject,
                           MAX_VALUE,
                    )

from ..trader.strategy import (BaseStrategy,
                               POPEN,PCLOSE,
                    )
from ..trader.strategy_agent import StrategyAgent

from ..trader.position import (GlobalCloser, CloserParameter,Closer,LongCloserParameter2,
                    )

from ..trader.trade_command import (Instruction,
                    )

from ..core.dac import (MA,
                        UPCROSS,
                        MINUTE,
                    )

class SE_STATUS(object):
    EMPTY = 0
    STATE1 = 101
    STATE2 = 102
    FULL = 300


class SExampleAB(BaseStrategy):
    '''
        需要根据所跟踪的多个ticks,组合成目标tick
        比如跟踪CA,CB且比例为1, 则新目标的tick = CA.tick - CB.tick
        这样，实际上target的ticks的长度是 len(CA.ticks) + len(CB.ticks)
    '''
    def __init__(self,holder):
        BaseStrategy.__init__(self,holder)
        self.is_full = False
        self.max_lost = 50      #以最小跳动为单位

    def prepare(self,ctick,CA,CB):
        pass

    def check_open(self,ctick,CA,CB):
        '''
            CA为目标Contract
        '''
        #print("in check open")
        if self.is_full:
            return
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
        return [instr_a,instr_b]



class SExampleAB2(BaseStrategy):
    '''
        需要根据所跟踪的多个ticks,组合成目标tick
        比如跟踪CA,CB且比例为1, 则新目标的tick = CA.tick - CB.tick
        这样，实际上target的ticks的长度是 len(CA.ticks) + len(CB.ticks)
    '''
    def __init__(self,holder):
        BaseStrategy.__init__(self,holder)
        self.is_full = False
        self.max_lost = 50      #以最小跳动为单位

    def prepare(self,ctick,CA,CB):
        pass

    def check_open(self,ctick,CA,CB):
        '''
            CA为目标Contract
        '''
        if self.is_full:
            return
        closer_params = CloserParameter(extremum = ctick.price,stop_line = ctick.price - self.max_lost*CA.ctype.unit)
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
        ca_positions = self._holder.get_positions_by_name(instructionA.contract.name)
        cb_positions = self._holder.get_positions_by_name(instructionB.contract.name)
        ca_len = len(ca_positions)
        cb_len = len(cb_positions)
        assert ca_len == cb_len
        if ca_len == 0:
            margin_a =  instructionA.contract.calc_margin(instructionA.direction,instructionA.base_price)*2
            margin_b =  instructionB.contract.calc_margin(instructionB.direction,instructionB.base_price)
            times = int(self.available_balance // (margin_a + margin_b)) // 2
            instructionA.unit = instructionA.planned = 2 * times
            instructionB.unit = instructionB.planned = 1 * times
        elif ca_len == 1:
            instructionA.planned = instructionA.unit = ca_positions[-1].volume_holding // 2  #已有仓位的1/2
            instructionB.planned = instructionB.unit = cb_positions[-1].volume_holding // 2  #已有仓位的1/2
        else:
            instructionA.planned = instructionA.unit = 0
            instructionB.planned = instructionB.unit = 0


    def _check_close(self,ctick,position_map,params,CA,CB):
        '''
            CA,CB为目标Contract
        '''
        ca_poses = position_map[CA.name]
        cb_poses = position_map[CB.name]

        if len(ca_poses) + len(cb_poses) == 0:
            return []

        if len(ca_poses) > 0 and len(cb_poses)> 0:
            ca_pos = ca_poses[-1]
            cb_pos = cb_poses[-1]

            ca_price = CA.last_price
            cb_price = CB.last_price
            instr_a = PCLOSE(ca_pos,base_price=ca_price,volume=1,extra_hops=30)
            instr_b = PCLOSE(cb_pos,base_price=cb_price,volume=1,extra_hops=30)
            return [instr_a,instr_b]
        else:
            ca_pos = ca_poses[-1]
            ca_price = CA.last_price
            instr_a = PCLOSE(ca_pos,base_price=ca_price,volume=1,extra_hops=30)
            return [instr_a]

##单独开仓和平仓
class SExampleAB0(BaseStrategy):
    '''
        需要根据所跟踪的多个ticks,组合成目标tick
        比如跟踪CA,CB且比例为1, 则新目标的tick = CA.tick - CB.tick
        这样，实际上target的ticks的长度是 len(CA.ticks) + len(CB.ticks)
    '''
    def __init__(self,holder):
        BaseStrategy.__init__(self,holder)
        self.is_full = False
        self.max_lost = 50      #以最小跳动为单位

    def prepare(self,ctick,CA,CB):
        pass

    def check_open(self,ctick,CA,CB):
        '''
            CA为目标Contract
        '''
        if self.is_full:
            return
        if ctick.instrument == CA.name:
            closer_params = CloserParameter(extremum = ctick.price,stop_line = ctick.price - self.max_lost*CA.ctype.unit)
            closer = Closer(self._check_close,closer_params)
            cmd1 = POPEN(contract=CA,direction=LONG,base_price=CA.last_price,closers=[closer],extra_hops=30) #targe_price=baseprice+hops*tick,extra_hops=MAX_VALUE/-MAX_VALUE则为停板
            return [cmd1]
        elif ctick.instrument == CB.name:
            closer_params = CloserParameter(extremum = ctick.price,stop_line = ctick.price - self.max_lost*CA.ctype.unit)
            closer = Closer(self._check_close,closer_params)
            cmd2 = POPEN(contract=CB,direction=LONG,base_price=CB.last_price,closers=[closer],extra_hops=30) #targe_price=baseprice+hops*tick,extra_hops=MAX_VALUE/-MAX_VALUE则为停板
            return [cmd2]
        else:
            return []

    def calc_open_volume(self,instruction1):
        '''
            只有在state=SE_STATE.EMPTY时才重新计算，其余均以已有仓位为基准
            next_state用于开仓跨越状态的情况，比如正常需要state0->state1, 但实际价格波动剧烈，需要state0-->state2,这样在开仓数上应当有区别
                基本不需要
            self.cordinator
        '''
        ca_positions = self._holder.get_positions_by_name(instruction1.contract.name)
        ca_len = len(ca_positions)
        if ca_len == 0:
            #instruction1.wanted = 2 #按比例设定
            instruction1.unit = instruction1.planned = int(self.available_balance // instruction1.contract.calc_margin(instruction1.direction,instruction1.base_price))//2
            #print("+++++++++++++++++++++:",instruction1.planned)
        elif ca_len == 1:
            instruction1.planned = instruction1.unit = ca_positions[-1]._holding_volume // 2  #已有仓位的1/2
            #print("********************:",instruction1.planned)
        else:
            self.is_full = True
            instruction1.planned = instruction1.unit = 0


    def _check_close(self,ctick,position,params,CA,CB):
        '''
            CA,CB为目标Contract
            当Closer独立运行时,每个tick到达,会分别调用CA和CB的position
            这里比较诡异,但是一致
        '''
        #print("SExampleAB0:",ctick.instrument)
        if ctick.instrument == CA.name and ctick.instrument == position.contract.name:
            #print("in CA")
            return self._check_close1(ctick,[position],params,CA)
        elif ctick.instrument == CB.name and ctick.instrument == position.contract.name:
            #print("in CB")
            return self._check_close1(ctick,[position],params,CB)
        return []

    def _check_close1(self,ctick,positions,params,contract):
        #print("SExampleAB0:",positions)
        if len(positions) == 0:
            return []

        ca_pos = positions[-1]

        ca_price = contract.last_price
        #print("_cc1:",positions[-1],ca_pos.get_holding_volume())
        instr_a = PCLOSE(ca_pos,base_price=ca_price,volume=ca_pos.volume_holding,extra_hops=30)
        return [instr_a]

