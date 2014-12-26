# -*- coding:utf-8 -*-

import logging
from functools import reduce
from operator import add

from ..common.base import BaseObject,ZERO_TICK,LONG,SHORT
from ..common.utils import next_trading_day,second2time,today,Updateable
from ..common.agent import ManagedAgent
from ..common.contract_type import ContractManager
from ..trader.position import EMPTY_POSINFO,Closer,ContractCloser,GlobalCloser,Position
from ..common.macro_command_queue import MacroCommand

from ..trader.strategy import POPEN,PCLOSE
from ..trader.strategy_agent import StrategyAgent,AgentState,POSITION_APPROVE_STATUS
from ..trader.trade_command import Instruction


POSITION_HANDLE_TICK = 92900       #仓位处理时间

'''
    协调者负责管理某类StrategyAgent的生命周期
    1.根据日期, 每日收盘数据确定次日有效的合约组, 当前合约组状态(正常, 中止开仓, 即时平仓)
                对即时平仓并且自动切换的合约组, 设定次日切换时间(9:30-10:10之间random)并保存到状态文件
    2.次日9:15, 重新读取切换信息,并启动监听
    3.管理该类策略的总仓位
      确定可开仓数(独立于资金)
    4.数据恢复
    5.手工切换
    每一个策略需要有一个协调者.对于日内策略,可以一个协调者对应多个策略,但提升了复杂性,没有必要
'''

VOLUME_THRESHOLD = 240 * 60 * 1 * 2   #240*60秒,每秒1手,2为夜盘系数
UNIT_THRESHOLD = 10

class Coordinator(ManagedAgent,Updateable):
    logger = logging.getLogger('trader.Environ')

    def __init__(self,env,strategy_clazz,contract_manager,tday=0):
        """
            strategy: 为策略类名,不是实例
        """
        ManagedAgent.__init__(self,contract_manager,tday)
        self._env = env
        self._strategy_clazz = strategy_clazz
        self._contracts2agent = {}   #从contract_names=>agent的映射
        self._auto_transfer = False  #自动移仓标志
        self._balance = 0    #准备金
        #向env注册
        env.register_coordinator(self)
        #向controller注册
        env.controller.register_agent(self)
        #name2contract
        self._name2contract = dict([(c.name,c) for c in self.contracts])    #self.contracts从contract_manager中来
        #print(self.contracts)
        #恢复数据
        self._initialize(tday)
        #print(list(self._name2contract.keys()))

    @property
    def name(self):
        ctype_names = [ct.name for ct in self._contract_manager.contract_types]
        return "_".join([self.__class__.__name__,self._strategy_clazz.sname()] + ctype_names)

    @property
    def is_auto_transfer(self):
        return self._auto_transfer

    @property
    def strategy_clazz(self):
        return self._strategy_clazz

    @property
    def env(self):
        return self._env

    @property
    def controller(self):
        return self._env.controller

    @property
    def agents(self):
        return list(self._contracts2agent.values())

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,v):
        self._balance = v

    @property
    def available_balance(self):
        return self.env.calc_strategy_balance(self) - self._calc_margin()

    def register(self,agent):
        name = self._contracts2name(agent.contracts)
        #if name not in self._contracts2agent:
        self._contracts2agent[name] = agent

    def _new_tick(self,ctick):
        if ctick.min1 >= 1455:       #接近收盘时才记录
            #print(self._name2contract.keys(),self._name2contract[ctick.instrument])
            self._name2contract[ctick.instrument].last_tick = ctick

    def execute(self,command):
        #print("in cood:execute",self._env)
        self._env.execute_trade_command(command)

    #初始化
    def _initialize(self,tday):
        """
            reload所有的contract的数据
            第一次初始化,或者resume
            第一次初始化时,需要 准备好contract
        """
        import time
        ta = time.time()
        #print("resume init begin")
        for contract in self.contracts:
            contract.resume()
        tb=time.time()
        #print("resume init end:",tb-ta)
        cagent = self._check_last_agent(tday)
        #print("check_last_agent:",time.time()-tb)
        #print(cagent,cagent._strategy)
        return cagent


    def resume(self,lastday=99999999,):
        """
            #恢复, 这个是和agent相一致的resume, 只能用来恢复合约数据
        """
        for contract in self.contracts:
            contract.resume(lastday)
            #print(contract.name,len(contract.minutes))

    #####
    ##仓位转移相关方法
    #####
    def day_finalize(self,tday=0):
        """
            1. 确认第二天的交易合约组以及相应的Agent
            3. 注册新的Agent
            3. 确认是否需要移仓
            4. 重新设置盯盘合约,并将last_tick设定为ZERO_TICK


        """
        self.tday = tday
        ntd = next_trading_day(tday)
        cagent = self._check_last_agent(ntd)

        #确定现有agent的状态
        self.check_agent_state(cagent)
        #强制平仓或移仓
        check_command = MacroCommand(self._position_handle,cagent,second2time(next_trading_day()*1000000+POSITION_HANDLE_TICK)) #这里next_day不能用tday为参数,而必须用当日的自然事件.否则就错乱了.或者立即执行,或者很长时间处于等待状态
        self.env.put_sec_macro_command(check_command)


    def _check_last_agent(self,tday):
        last_group = self._last_group(tday)
        if len(last_group) == 0:    #空
            #print("last_group==[]")
            cagent = None
        else:
            #创建Agent
            cname = self._contracts2name(last_group)
            #print(cname,last_group,ntd)
            if cname not in self._contracts2agent:
                #print("cagent not in map")
                cagent = StrategyAgent(self,last_group)
                #self._contracts2agent[cname] = cagent      #StrategAgent中自行register
                self._env.controller.register_agent(cagent)
            else:
                #print("find cagent")
                cagent = self._contracts2agent[cname]
        #设定last_tick
        for contract in self.contracts:     #这里重新设置之后,没有新的行情,再次调用day_finalize时, last_group就会返回[]
            contract.last_tick = ZERO_TICK
        #重新设置n2c映射
        self._name2contract = dict([(c.name,c) for c in self.contracts])
        return cagent

    def _position_handle(self,cagent):
        #首先须判断当日是否交易,如果不是,则再顺延一个交易日. #通过ticks判断
        if self.env.trading_day < today():  #当日未交易
            #print("env.trading_day < today,today=",self.env.trading_day,today())
            check_command = MacroCommand(self._position_handle,cagent,second2time(next_trading_day()*1000000+POSITION_HANDLE_TICK))
            self.env.put_sec_macro_command(check_command)
        elif self._auto_transfer and cagent != None:   #自动结转
            for agent in self.agents:
                if agent.state == AgentState.MUST_CLOSE:    #不论是不是cagent
                    self.transfer(agent,cagent)
                    agent.force_close_all()
                    agent.s2transfered()
        else:   #不自动结转
            for agent in self.agents:
                if agent.state == AgentState.MUST_CLOSE:    #不论是不是cagent
                    agent.force_close_all()
                    agent.s2finished()


    def check_agent_state(self,last_agent):
        for agent in self.agents:
            agent.recalc_state(self.tday)

    def deactive_previous_agents(self,last_agent):
        """
            仅用于只允许出现单agent的情形, 把最新agent之外的所有其它均关闭
            将所有last_group之前的agent都设定为CLOSE_ONLY
            如有必要,应该由子类继承check_agent_state时调用
        """
        for agent in self.agents:
            if agent != last_agent:
                agent.s2close_only()

    def transfer(self,agent_from,agent_to): #将仓位从agent_from移转到agent_to #TODO:TEST
        """
            其中在agent中,按 contracts的顺序对应移转的合约和仓位
        """
        cfroms = agent_from.contracts
        ctos = agent_to.contracts
        #contract_source2target = dict(zip(agent_from.contract_names,agent_to.contract_names))   #转移的contract的映射
        contract_source2target = dict(zip(agent_from.contracts,agent_to.contracts))   #转移的contract的映射
        #for c1,c2 in contract_source2target.items():
        #    print(c1.name,c2.name)
        volume_available = agent_from.get_holding_info()    #可供下一期使用的volumes, 在处理过程中被修改
        #for k,v in volume_available.items():
        #    print(k,v.num_long,v.num_short)

        poses_detail = agent_from.active_positions    #需要移转的position
        #需要处理closer: A: closer的共享
        #       B: Closer中引用到已经close的position的情况，只会出现在一个closer包含多个position且不是同生共死的情况
        #            实际上，这类情况应该使用GlobalCloser，而不是普通Closer
        #          此时，对包含这类Closer的Position,须特殊处理
        source_closers = list(set(reduce(add,[list(pos.closers) for pos in poses_detail])))    #将closers去重
        target_closers = [ c.create_tranfer_closer(c,cfroms,ctos) for c in source_closers]
        closer_source2target = dict(zip(source_closers,target_closers))
        #print("poses_detail:",len(poses_detail))
        for position in poses_detail:
            contract2 = contract_source2target[position.contract]
            vol2 = position.volume_holding
            cv_available = volume_available.get(contract2.name,EMPTY_POSINFO)
            #print(position.contract_name,"=>",contract2.name)
            #print("before pre_calc:",position.contract_name,cv_available.num_long,"vol2:",vol2)
            #print("%s 目标仓位:%d,已有仓位:%d" % (contract2.name,vol2,cv_available.num_long))
            if position.direction == LONG and cv_available.num_long > 0:
                transfer_volume = vol2 if cv_available.num_long >= vol2 else cv_available.num_long
                cv_available.num_long -= transfer_volume
            elif position.direction == SHORT and cv_available.num_short > 0:
                transfer_volume = vol2 if cv_available.num_short >= vol2 else cv_available.num_short
                cv_available.num_short -= transfer_volume
            else:
                transfer_volume = 0
            vreal_open = vol2 - transfer_volume
            closers2 = [closer_source2target[c] for c in position.closers]
            self._transfer_open(agent_to,position.direction,contract2,closers2,vol2,vreal_open)
            #print("agent_to.active_position:",len(agent_to.active_positions))
            #print("after pre_calc:",contract2.name,cv_available.num_long,"vol2:",vol2)
            #print("%s 目标仓位:%d,实际开仓:%d,须关闭仓位:%d" % (contract2.name,vol2,vreal_open,cv_available.num_long))
        poses_detail2 = agent_to.active_positions
        assert len(poses_detail) == len(poses_detail2),"转移前后头寸个数必须一致,%d!=%d" % (len(poses_detail),len(poses_detail2))
        pos_source2target = zip(poses_detail,poses_detail2)
        self._complete_target_closers(closer_source2target,pos_source2target,contract_source2target,agent_to.position_holder)

        volume_orignal = agent_from.get_holding_info()    #可供下一期使用的volumes
        #for k,v in volume_available.items():
        #    print(k,v.num_long,v.num_short)
        pcloses = []
        for cname in agent_from.contract_names: #对agent_from,剔除已移转的仓位,关闭剩余仓位
            poses = agent_from.get_positions_by_name(cname)
            vlong_transfered = volume_orignal[cname].num_long - volume_available[cname].num_long
            vshort_transfered = volume_orignal[cname].num_short - volume_available[cname].num_short
            pcloses.extend(self._check_transfer_close(poses,vlong_transfered,vshort_transfered))

        instrs = agent_from.prepare_close_command(pcloses)
        self._achieve_transfer_close(instrs)    #对移转仓位的内部一致性关闭, 非实际性关闭

    def _transfer_open(self,agent_to,direction,contract2,closers,vol_total,vol_real):
        """
            closers为已经转换为针对agent_to
            转换1个position
            其中vol_real为实际需要open的仓位,vol_total-vol_real为transfer过来的仓位
        """
        cmd = POPEN(contract=contract2,
                    direction=direction,
                    base_price=contract2.last_price,
                    closers=closers,
                    extra_hops= 30 if direction == LONG else -30,
                )
        cmd.planned = vol_total
        cmd.unit = 1
        instrs = agent_to.prepare_open_command([cmd])
        if len(instrs) == 0:
            return

        instr = instrs[0]       #必然只有1个
        #print("in transfer_open:",vol_total,instr.order.planned)
        #不校验是否能够开仓
        instr.on_approved(POSITION_APPROVE_STATUS.APPROVED)
        instr.order.part_accomplished(vol_total-vol_real)
        #instr.order.approve(vol_total,vol_total*contract2.last_price) #为完成部分处于敞口
        #assert instr.order.transfered == vol_total-vol_real
        if vol_real > 0:
            #print("in vol_real>0")
            self._env.approve_one(instr.order)
            #print("vol_real:",instr.order.approved)
            self.execute(instr) #在trade_command_queue中执行时,只开仓 approved - accomplished2
        else:   #vol_real == 0, 直接结束了
            instr.order.approve(vol_total)
            instr.on_done(vol_total)
        return instr

    def _complete_target_closers(self,closer_source2target,pos_source2target,contract_source2target,position_holder):   #TODO:TEST
        """
            填充target_closers中每个closer的position字段
            需要注意可能存在已经被关闭的position
        """
        closed_pos_source2target = {}
        for source,target in closer_source2target.items():
            if isinstance(source,Closer):
                for pos in source.positions:
                    if pos in pos_source2target:
                        #print("find in pos_source2target")
                        target.positions.append(pos_source2target[pos])
                    elif pos in closed_pos_source2target:
                        #print("find in closed_poses")
                        target.positions.append(closed_pos_source2target[pos])
                    else:   #发现已经close的position,原则上不应当出现,但也需要在这里处理
                        #print("new closed pos")
                        self.logger.info("closer中出现新的已关闭头寸,contract=%s" % (pos.contract))
                        tpos = Position(contract_source2target[pos.contract],pos.direction)
                        tpos.id = position_holder.inc_position_id()
                        target.positions.append(tpos)
                        position_holder.add_closed_position(tpos)
                        closed_pos_source2target[pos] = tpos
            elif isinstance(source,ContractCloser):
                target.prepare(position_holder,contract_source2target[source.contract])
                #print("ContractCloser")
            elif isinstance(source,GlobalCloser):
                target.prepare(position_holder)
        return closed_pos_source2target     #仅用于测试

    def _check_transfer_volume(self, pos, vclosed):
        vtransfer = vclosed if pos.volume_holding >= vclosed else pos.volume_holding
        pclose1 = PCLOSE(pos, pos.contract.last_price, vtransfer, 30)
        return pclose1,vtransfer

    def _check_transfer_close(self,positions,vlong_transfered,vshort_transfered):
        """
            按顺序从positions中创建关闭vlong_transfered和vshort_transfered对应的仓位的PCLOSE命令
        """
        pcloses = []
        for pos in positions:   #处理transfered部分
            if pos.direction == LONG and vlong_transfered > 0:
                pclose1,vtransfer = self._check_transfer_volume(pos, vlong_transfered)
                vlong_transfered -= vtransfer
                pcloses.append(pclose1)
            elif pos.direction == SHORT and vshort_transfered > 0:
                pclose1,vtransfer = self._check_transfer_volume(pos, vshort_transfered)
                vshort_transfered -= vtransfer
                pcloses.append(pclose1)
            if vlong_transfered == 0 and vshort_transfered ==0: #transfered部分处理完毕
                break
        assert vlong_transfered <=0 and vshort_transfered <=0
        return pcloses

    def _achieve_transfer_close(self,instrs):
        """
            直接完成仓位已移转的instrs CLOSE指令, 以便设定相应的position状态. 但并无实际开平仓动作
            只针对CLOSE指令,对Open指令, 还需要针对order的approve
        """
        for instr in instrs:
            #instr.on_approved()    #已经在前面on_approved了
            instr.on_progress(instr.order.approved,instr.contract.last_price)   #必然存在last_price
            instr.on_done(instr.order.approved)

    ###############
    #子类可修改的方法
    ###############
    def lock_open_volume(self,instructions):
        """
            确定每次开仓的审核数, 并暂时锁定(在下一次query后解锁)
        """
        orders = [instr.order for instr in instructions]
        return self._env.approve_open(orders)

    def _last_group(self,trading_day):
        """
            获得与trading_day相匹配的最新合约组
            这个需要子类实现
        """
        try:
            #for c in self._contract_manager.contract_types : print(c.name)
            last_contracts = [self._contracts_flying(ctype,trading_day)[-1] for ctype in self._contract_manager.contract_types]
            return last_contracts
        except IndexError as einst:      #至少有一个ctype没有满足成交量条件的可用合约
            logging.info("至少有一个ctype没有满足成交量条件的可用合约")
            return []

    @property
    def shares(self):
        """
            如果返回值>0, 则以返回值为份额
                份额用于根据保证金总数来确定每个策略的可用数
                这里可以根据实际成交量等因素来确定份额占比
            默认份额为10
        """
        return 10


    ##############
    #内务方法
    ##############
    def _contracts_flying(self,ctype,cday,volume_threshold = VOLUME_THRESHOLD,unit_threshold2=UNIT_THRESHOLD):
        """
            cday: 确定合约所用的日期
            volume_threshold:   日成交量阈值
            unit_threshold2:    单位成交量阈值, 单位成交量= 成交量/((最高价-最低价)/价格变动单位)
            返回符合 c.volume > volume_threshold and c.volume_per_unit >= unit_threshold2 的合约列表
                    且其中iv字段为从大到小的成交量序号, 成交量最大的合约序号为0,次之为1
        """
        contracts = self._contract_manager.current_contracts_by_ctype(ctype,cday//10000,cday%10000//100,cday%100)
        #print(ctype.name)
        #for c in contracts: print(c.name)
        for contract in contracts:
            #print(contract.name)
            #cday = contract.days[-1]
            #contract.volume = cday.last_dvolume
            #contract.volume = contract.last_tick.dvolume
            contract.volume = contract.last_dvolume
            drange = (contract.last_drange)/contract.ctype.unit
            contract.volume_per_unit = contract.volume / drange if drange > 0 else 0
            #print(contract.name,contract.volume,drange,contract.volume_per_unit)
        #print([(c.name,c.volume) for c in contracts])
        rev = [c for c in contracts if c.volume > volume_threshold and c.volume_per_unit >= unit_threshold2]
        #确定成交量序号
        srev = enumerate(sorted(rev,key=lambda c:c.volume,reverse=True))
        for iv,c in srev:
            c.iv = iv
        return rev


    def _calc_margin(self):
        """
            计算相关agent的保证金总和 (包括已lock的保证金)
        """
        smargin = sum([agent.calc_current_margin() for agent in self._contracts2agent.values()])
        return smargin

    def _contracts2name(self,contracts):
        return '.'.join([c.name for c in contracts])


class CashCoordinator(Updateable):  #现金份额
    """
        关于现金以及保证金比例的思考
        1. 这个位置留出的现金, 是总预备, 起到2个作用
           a. 降杠杆,作为一个稳定器
           b. 部分品种超保时的缓冲
        2. 各品种不同比例的处理
            a. 计算时均以11%, 也就是9倍为基准. 当然这个值最后被冲抵掉了
            b. 实际保证金的不同, 有几方面的原因
               (1) 节假日, 直接忽视. 必要时会用到总预备金
               (2) 交易量超限时的上调, 也忽略
               (3) 各品种/交易所 内在的保证金差异. 这个问题需要详细的考虑
                   和品种特性相关或者无关, 由策略内部处理

    """
    def __init__(self,env,shares=30):
        self._env = env
        self._shares = shares
        self._balance = 0
        env.register_coordinator(self)

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self,v):
        self._shares = v

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,v):
        self._balance = v

    @property
    def available_balance(self):
        return self._env.calc_strategy_balance(self)


