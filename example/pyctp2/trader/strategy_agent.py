# -*- coding:utf-8 -*-

import os
import os.path
from threading import Lock
import logging

from ..common.agent import BaseAgent
from ..common.base import (XOPEN,
                           XCLOSE,
                           STATE_PATH,
                           BaseObject,
                           LONG,
                           MAX_VALUE,
                        )
from ..common.reader import readn_m1,read_day
from ..core.dac import MINUTE,MINUTED,TICK_PRICE
from ..common import cjson
from ..common.utils import type_name,next_trading_day

from .position import Position,PositionHolder,POSITION_APPROVE_STATUS,BaseCloser
from .strategy import PCLOSE

from .trade_command import (OpenInstruction,
                            CloseInstruction,
                    )

STATE_FNAME = STATE_PATH + '/positions.%s.txt'
TRADE_FNAME = STATE_PATH + '/trade.%s.txt'

class AgentState:
    ACTIVE = 1
    CLOSE_ONLY = 2  #只能平仓, 即允许继续持仓
    MUST_CLOSE = 3  #准备结束
    FINISHED = 4
    TRANSFERED = 5


class StrategyAgent(BaseAgent):
    '''
        负责内务操作, 以委托方式隔离Strategy, 便于Strategy的实现
            从原则上来说,StrategyAgent和Strategy可以合二为一, 这里拆分的基准是变与不变部分
                拆分的目标是 对策略的实现者屏蔽相对稳定的那些功能
        具体功能:
        1. 管理PositionHolder和Strategy
        2. 实现force_close和force_open, 即移仓功能
        3. 衔接Controller和Strategy,
        4. 保存和恢复相关Position状态

        生命周期由coordinator(生)和controller(消)管理
    '''
    def __init__(self,coordinator,contracts):
        BaseAgent.__init__(self)
        self._coordinator = coordinator
        self._contracts = contracts
        self._strategy = coordinator.strategy_clazz(self)
        #self._is_active = True
        self._state = AgentState.ACTIVE
        self._position_holder = PositionHolder()
        #self._initialize_contract_data()
        self._lock = Lock()
        coordinator.register(self)

    #def _initialize_contract_data(self):
    #    pass #contract数据的恢复不在这里,在coordinator中
        #for c in self.contracts:
        #    c.TICK = []
        #    c.M1 = []
        #    c.DAY = []
        #    c.TPRICE = TICK_PRICE(c.TICK)

    @property
    def env(self):
        return self._coordinator.env

    #def de_active(self):
    #    self._is_active = False

    @property
    def is_active(self):
        return self._state in (AgentState.ACTIVE,AgentState.CLOSE_ONLY,AgentState.MUST_CLOSE)

    @property
    def position_holder(self):
        return self._position_holder

    @property
    def state(self):
        return self._state

    def next_state(self):
        self._state += 1

    def s2close_only(self):
        if self._state == AgentState.ACTIVE:
            self._state = AgentState.CLOSE_ONLY

    def s2must_close(self):
        if self._state in (AgentState.ACTIVE,AgentState.CLOSE_ONLY):
            self._state = AgentState.MUST_CLOSE

    def s2finished(self):
        if self._state not in (AgentState.FINISHED,AgentState.TRANSFERED):
            self._state = AgentState.FINISHED

    def s2transfered(self):
        self._state = AgentState.TRANSFERED

    @property
    def contract_names(self):
        return [c.name for c in self._contracts]

    @property
    def contracts(self):
        return self._contracts

    @property
    def name(self):
        return "%s_%s" % (type_name(self._strategy),'_'.join(self.contract_names))

    @property
    def state_path_name(self):
        return STATE_FNAME % self.name

    @property
    def trade_log_name(self):
        return TRADE_FNAME % self.name

    @property
    def available_balance(self):
        return self._coordinator.available_balance

    def _new_tick(self,ctick):
        '''
           同步处理
           创建M1 
        '''
        #print("in agent check")
        with self._lock:
            self._check(ctick)

    def get_net_holding_volume(self):
        hs = [0] * len(self.contracts)
        for i in range(len(self.contracts)):
            hs[i] = self._position_holder.get_net_volume_holding(self.contracts[i].name)
        return dict(zip(self.contract_names,hs))

    def get_holding_info(self):
        hi = [0] * len(self.contracts)
        for i in range(len(self.contracts)):
            hi[i] = self._position_holder.get_holding_info(self.contracts[i].name)
        return dict(zip(self.contract_names,hi))


    def calc_current_margin(self):
        """
            计算当前占用的保证金, 包括lock的
        """
        smargin = sum([self._position_holder.get_volume_holding(contract.name) * contract.last_price for contract in self._contracts])
        return smargin

    @property
    def active_positions(self):
        return self._position_holder.active_positions

    def get_positions_by_name(self,contract_name):
        return self._position_holder.get_positions_by_name(contract_name)

    #def get_contract_positions(self,contract_name):
    #    return self._position_holder.name2positions[contract_name]

    def get_holding_volume(self,contract_name):
        assert isinstance(contract_name,str),"strategy_agent.get_holding_volume的参数必须是 合约名"
        return self._position_holder.get_volume_holding(contract_name)

    #####################
    #   开平仓检查与执行
    #####################
    def _check(self,ctick):
        self._strategy.prepare(ctick,*self._contracts)
        '''close 处理, 因为可能有多个xpos,故可有多个close_command'''
        close_commands = self.check_close(ctick,*self.contracts)
        for close_command in close_commands:
            close_command.trigger_time = ctick.time
            self._coordinator.execute(close_command)
        '''open处理'''
        if self._state == AgentState.ACTIVE:
            open_instrs = self.check_open(ctick,*self.contracts)
            if len(open_instrs)>0:  #直接
                logging.info("open instrs不为空")
                approve_state = self._coordinator.lock_open_volume(open_instrs)
                #print(approve_state)
                if approve_state != POSITION_APPROVE_STATUS.REJECTED:
                    logging.info("开仓批准数>0")
                    for open_instr in open_instrs:
                        open_instr.on_approved(approve_state)
                        if open_instr.approved > 0:
                            open_instr.trigger_time = ctick.time
                            self._coordinator.execute(open_instr)
                else:
                    logging.info("开仓被拒绝")
                    pass

    def check_open(self,ctick,*contracts):
        popens = self._strategy.check_open(ctick,*contracts)
        #print("SA:co:",len(popens))
        if popens:
            logging.info("popens != []")
            self._strategy.calc_open_volume(*popens)
            #print(popens[0].planned)
            #print(popens,popens[0].__dict__)
            sum_unit = sum([ p.unit for p in popens ])
            logging.debug("sum_unit:%d",sum_unit)
            if sum_unit > 0:
                logging.info("popens 开仓数 > 0")
                commands = self.prepare_open_command(popens)   #计算开仓数，在positions中添加条目，并设定回调
                return commands
        return []

    def prepare_open_command(self,popens):
        instrs = []
        positions = []
        for popen in popens:
            if popen.planned <= 0:
                continue
            position = Position(popen.contract,popen.direction)
            open_order = position.add_open_order(popen)
            instr = OpenInstruction(open_order,position)
            instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
            instrs.append(instr)
            positions.append(position)
        self._position_holder.add_positions(positions)
        return instrs

    def check_close(self,ctick,*contracts):
        """
            对每个closer在每个tick到来时均调用一次
            这里没有限制:
                    1. 每个合约,是否存在多个ContractCloser. 由使用者自己管理
                    2. 是否存在多个GlobalCloser. 由使用者自己管理
        """
        commands = []
        cids = set()    #已完成的closer的id集合. 每个closer在每一轮只能调用一次.
        for position in self.active_positions:
            #需注意 从 closer.check得到的pclose, 其目标position不一定是当前position
            if position.volume_holding <= 0:  #处于正在关闭状态
                continue
            pcloses = []
            for closer in position.closers:
                if closer.id not in cids:
                    cids.add(closer.id)
                    cur_pcloses = closer.check(ctick,*contracts)
                    if cur_pcloses == None:
                        continue
                    elif not isinstance(cur_pcloses,list) and isinstance(cur_pcloses,tuple):
                        cur_pcloses = [cur_pcloses]
                    for cpclose in cur_pcloses:
                        if isinstance(cpclose,PCLOSE):
                            pcloses.append(cpclose)
                        else:   #根据合约来分派
                            spcloses = self._assign_close_volume(cpclose)
                            if cpclose.volume > 0:  #未分派数
                                logging.info("STG:CC:%s 要求平仓数大于在手数:%d" % (cpclose.contract.name,cpclose.volume))
                            pcloses.extend(spcloses)
            if pcloses:
                pcommands = self.prepare_close_command(pcloses)
                commands.extend(pcommands)
        return commands

    def _assign_close_volume(self,pclose2):
        """
            将contract的平仓手数tvolume按后进先出的顺序分配到position中
        """
        pcloses = []
        positions = self._position_holder.get_positions_by_name(pclose2.contract.name)
        for pos in reversed(positions):
            available = pos.volume_holding
            #print(available,pclose2.volume)
            if available <= 0:
                continue
            cvolume = available if available <= pclose2.volume else pclose2.volume
            pclose2.volume -= cvolume
            pcloses.append(PCLOSE(pos,pclose2.base_price,cvolume,pclose2.extra_hops))
            if pclose2.volume <= 0:
                break
        return pcloses

    def prepare_close_command(self,pcloses):
        instrs = []
        for pclose in pcloses:
            close_order = pclose.position.add_close_order(pclose)  #需要修正,以避免超仓
            instr = CloseInstruction(close_order,pclose.position)
            #print("##",instr,"##")
            instr.set_callback(self.on_approved,self.on_reject,self.on_done,self.on_progress)
            self._verify_close_volume(instr)
            instrs.append(instr)
        #print("PCC:instrs:",instrs,"#")
        return instrs

    def _verify_close_volume(self,instr):   #鉴于前面的设定办法,直接批准
        order = instr.order
        order.approve(order.planned,0)    #对于closed来说, 无所谓amount
        instr.on_approved(POSITION_APPROVE_STATUS.APPROVED)

    ##回调函数
    ##注意:   on_approved(command,POSITION_APPROVE_STATUS.REJECT)
    ##        on_reject(command)
    ##        on_done(command)
    ##        三个函数在每个command的生命周期中都只能调用其中之一,否则会引发position从active切转到closed的多次切转,从而出错
    def on_approved(self,command,astate=POSITION_APPROVE_STATUS.APPROVED):
        '''
            状态:
            APPROVED: 批准. 平仓必须是APPROVED
            PART_APPROVED: 部分批准，必须是成比例
            REJECTED: 否决
            只有开仓数被清为0时，才会导致reject = True
        '''
        if astate == POSITION_APPROVE_STATUS.REJECTED:
            self._position_holder.on_order_done(command.position)   #把开仓为0的position处理掉
        self._strategy.on_approved(command,astate)      #实际上没有意义, strategy不应该依赖于实现状态

    def on_reject(self,command):
        """
            调用到这里时,command已经调用了order.on_reject
            正常运作时不应该调用这个分支
        """
        self._position_holder.on_order_done(command.position)   #把开仓为0的position处理掉
        self._strategy.on_reject(command)           #实际上没有意义, strategy不应该依赖于实现状态

    def on_done(self,command,volume_traded):
        self._position_holder.on_order_done(command.position)
        self._strategy.on_done(command)         #实际上没有意义, strategy不应该依赖于实现状态
        if self._state == AgentState.MUST_CLOSE and len(self._position_holder._active_positions) == 0:
            #MUST_CLOSE且已完成
            if self._coordinator.is_auto_transfer:  #如果策略组是自动切换
                self._state = AgentState.TRANSFERED
            else:
                self._state = AgentState.FINISHED
        self.snapshot()

    def on_progress(self,command,volume,price):
        self._strategy.on_progress(command)     #实际上没有意义, strategy不应该依赖于实现状态
        self.log_trade(command.contract_name,command.order.atype,command.last_update_time,command.order.direction,volume,price)

    #########################
    # 内务处理
    #########################

    def day_finalize(self):
        """
            日结处理
        """
        super(StrategyAgent, self).day_finalize()  #先处理基类
        self._strategy.day_finalize()
        #self.recalc_state()        #应当由coordinator调用

    def recalc_state(self,day=0):
        """
            重新计算状态,
            前数第三月之前为ACTIVE,前一月10日之前(含10日)为CLOSE_ONLY,之后为MUST_CLOSE
            ####还有一种情况,在coordinator层面,是否出现新的agent时, 就要把已有的都设定为CLOSE_ONLY?
                留到coordinator层面解决
        """
        if self.state in (AgentState.MUST_CLOSE,AgentState.FINISHED,AgentState.TRANSFERED): #已经到达休止态
            return
        if day == 0:
            day = next_trading_day()
        mday = day % 100    #月中日
        cmonth = day % 1000000 // 100
        for contract in self._contracts:
            mdiff = contract.calc_month_distance(cmonth)
            #print(cmonth,mday,mdiff)
            if mdiff >= 2:
                continue
            elif mdiff == 1 and mday <= 10:
                self.s2close_only()
            else:
                self.s2must_close()
                break   #不会再有更进一步的结果

    def log_trade(self,contract_name,atype,last_update_time,direction,volume,price):
        dsignal = '+' if direction == LONG else '-'
        dtype = "open " if atype == XOPEN else "close"
        with open(self.trade_log_name,"at") as ff:
            ff.write("\n%s:%s,%s:%d%s,%.04f" %(contract_name,last_update_time,dtype,volume,dsignal,price))


    ############
    #   force_close/force_open对用于移仓或外部开仓
    ############
    def force_close_all(self):
        '''
            强制关闭所有position
            返回所关闭的头寸
        '''
        pcloses = []
        for position in self._position_holder._active_positions:
            available = position.volume_holding
            if  available > 0:
                pclose = PCLOSE(position,position.open_order.base_price,available,MAX_VALUE)
                pcloses.append(pclose)
        instrs = self.prepare_close_command(pcloses)

        for close_command in instrs:
            #close_command.order._target_price=0
            self._coordinator.execute(close_command)
        return instrs

    def force_open(self,popens):
        '''
            强制开启头寸
            其中positions为待开启的头寸, 其planned,unit必须已经赋值
            而popens中的closers的stop_line已被重新组织(根据相邻合约的差价)
        '''
        instrs = self.prepare_open_command(popens)
        for open_command in instrs:
            self._coordinator.execute(open_command)

    '''
        现场保存与恢复
    '''
    def snapshot(self):
        '''
            保存现场. 用于头寸变化时
        '''
        with open(self.state_path_name,'wt') as sf:
            cjson.dump(self._position_holder,sf)


    def resume(self,lastday=99999999,size=3000):
        '''
            恢复,从最新的头寸记录和M1数据中中恢复现场
        '''
        #恢复positions
        #print("in agent resume",self.name)
        self._position_holder = self._load_position_holder()
        #恢复数据: 需要在coordinator层次
        #for c in self.contracts:
        #    c.resume(mlen=size)
        #    c.TPRICE = TICK_PRICE(c.ticks)
        #    #print(len(c.M1))
            #print(len(c.DAY))

    def _load_position_holder(self):
        """
            对position_holder.active_positions下的closer进行遍历, 设定其close_func
        """
        if not(os.path.exists(self.state_path_name)):
            return PositionHolder()
        with open(self.state_path_name,'rt') as sf:
            position_holder = cjson.load(sf)
        for pos in position_holder.active_positions:
            for xcloser in pos.closers:
                #if isinstance(xcloser,Closer):
                #    xcloser._close_func = self._strategy.__getattribute__(xcloser.close_func_name)
                xcloser._close_func = self._strategy.__getattribute__(xcloser.close_func_name)
        logging.debug("StrategyAgent:%s,active_positions:%d",self.name,len(position_holder.active_positions))
        for pos in position_holder.closed_positions:    #已经不再保存closed_positions了,#其实没用，特意保存下。否则需要修改BaseCloser的to_dict
            for xcloser in pos.closers:
                #if isinstance(xcloser,Closer):
                #    xcloser._close_func = self._strategy.__getattribute__(xcloser.close_func_name)
                xcloser._close_func = self._strategy.__getattribute__(xcloser.close_func_name)
        return position_holder



