'''
    理想的策略形式
    交易端须获取所跟进的合约的当日涨跌停位置
'''

import json
from threading import Lock
from collections import OrderedDict

from ..common import base
from ..common.base import (
                           XOPEN, XCLOSE, XCLOSE_TODAY,
                           LONG, SHORT,
                           BaseObject,
                           inverse_direction,
                           MAX_VALUE,
                        )
from ..common.utils import (fcustom,
                            bound_method_name,
                        )


class ORDER_STATUS(object):
    INITIALIZED = 0
    REJECT = -1001
    ACCEPT = 1001
    NOTRADE = 2001      #未成交
    #PART_TRADED = 3001  #一体两面
    PART_SUCCESSED = 3001
    #ALL_TRADED = 3100   #一体两面
    SUCCESSED = 3100
    CANCELLED = 9001

#class ORDER_STATUS(object):
#    INITIALIZED = 100
#    ON_THE_WAY = 200
#    SUCCESSED  = 300
#    PART_SUCCESSED = 301 #部分完成部分取消
#    CANCELLED = 501  #完全取消
#    REJECTED = 502  #被交易所拒绝

class POSITION_APPROVE_STATUS:
    APPROVED = 100
    PART_APPROVED = 99  #没有实际意义
    REJECTED = -100


class Order(object):
    def __init__(self,position,atype,base_price,planned,unit,extra_hops):
        '''
            atype: XOPEN/XCLOSE/XCLOSE_TODAY 等action type
            direction: LONG/SHORT
            order中采用 planned/wanted/approved的目的是区分:
                1. unit为变动单位, 通常为1, 多策略时为比例, 可以为小数
                2. planned为倍数取整后的计划数
                3. progress是确认中间状态
            
        '''
        self._position = position
        self._atype = atype
        self._direction = position.direction if atype == XOPEN else inverse_direction(position.direction)
        self._base_price = base_price
        self._trigger_time = 0   #触发时间,为Tick.time,精确到秒
        self._planned = int(planned)
        self._unit = int(unit)
        self._extra_hops = extra_hops
        self._approved = 0   #
        self._approved_amount = 0
        self._state = ORDER_STATUS.INITIALIZED
        self._accomplished = 0
        self._accomplished2 = 0      #从on_order_done中得到的数据
        self._details = []
        self._trade_info = None  #在on_accept中被设定
        self._transfered = 0    #移转过来的仓位,只用于信息记录和核对
        self._account = ""      #account_id: 字符串
        self._target_price = 0
        self._target_price = self.calc_target_price(self.contract,self.direction,base_price,extra_hops)
        #print("in order init,target_price=",self._target_price)

    @property
    def position(self):
        return self._position

    @property
    def atype(self):
        return self._atype

    @property
    def direction(self):
        return self._direction

    @property
    def base_price(self):
        return self._base_price

    @property
    def target_price(self):
        return self._target_price

    @target_price.setter
    def target_price(self,v):
        self._target_price = v

    @property
    def unit(self):
        return self._unit

    @property
    def planned(self):
        return self._planned

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self,v):
        self._account = v

    @property
    def approved(self):
        return self._approved

    #批准动作
    def approve(self,approved_volume,approved_amount=0):
        #approved_amount仅对open_order有用,close的没有实际意义
        self._approved = int(approved_volume)
        self._approved_amount = approved_amount

    @property
    def approved_amount(self):
        return self._approved_amount

    @property
    def extra_hops(self):
        return self._extra_hops

    @property
    def accomplished2(self):
        return self._accomplished2

    @property
    def accomplished(self):
        return self._accomplished

    @property
    def trade_info(self):
        return self._trade_info

    @property
    def state(self):
        return self._state

    @property
    def trigger_time(self):
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self,ctime):
        self._trigger_time = ctime

    @property
    def contract(self):
        return self._position.contract

    @property
    def contract_name(self):
        return self._position.contract.name

    @property
    def transfered(self):
        return self._transfered

    @property
    def net_approved(self):
        return self._approved - self._transfered if self._approved > self._transfered else 0

    @property
    def true_accomplished(self):
        """
            获得与Order当前状态无关的已成交数
        """
        return self._accomplished if self._accomplished > self._accomplished2 else self._accomplished2

    @property
    def done(self):
        return self._state == ORDER_STATUS.SUCCESSED or self._state == ORDER_STATUS.PART_SUCCESSED or self._state == ORDER_STATUS.CANCELLED or self._state == ORDER_STATUS.REJECT

    @staticmethod
    def calc_target_price(contract,direction,base_price,extra_hops=MAX_VALUE):
        """
            计算开/平仓的目标价
            hops = 99999999时,表示顺向停板价格
                  -99999999时,表示用逆向停板价格
                其它值表示基价 +  hops * price_tick
        """
        #print("~~~~~~~~~~~~~~~~~~~direction=%s,base_price=%s" % (direction,base_price))
        #print("contract.limit:",contract.upperlimit_price,contract.lowerlimit_price)
        if extra_hops > MAX_VALUE - 1:   #顺向停板
            return contract.upperlimit_price if direction == LONG else contract.lowerlimit_price
        elif extra_hops < -MAX_VALUE + 1:    #逆向停板
            return contract.lowerlimit_price if direction == LONG else contract.upperlimit_price
        else:
            factor = 1 if direction == LONG else -1
            extra = extra_hops * contract.price_tick * factor
            target_price =  base_price + extra
            #print("order calc_target_price:",contract.name,extra_hops,base_price,target_price)
            #print("target price calced, target_price=%s,base_price=%s" %(target_price,base_price))
            if target_price < contract.lowerlimit_price:
                target_price = contract.lowerlimit_price
            elif target_price > contract.upperlimit_price:
                target_price = contract.upperlimit_price
            #print("after target price:",target_price)
            return target_price

    def calc_margin(self):
        return self.contract.calc_margin(self.direction,self.target_price)

    def part_accomplished(self,pacc):   #仓位转入时已部分持有,故开仓数量=approved-accomplished
        self._accomplished = self._accomplished2 = pacc
        self._transfered = pacc
        #self._state = ORDER_STATUS.PART_SUCCESSED  #这里不能设定,否则后续on_done会出错

    def on_accept(self,trade_info):
        self._trade_info = trade_info

    def on_reject(self):
        """
            不应当发生.但是一旦发生,要把状态调整到一致就非常麻烦
            需要用一个MacroCommand来专门协调这个事情
        """
        self._state = ORDER_STATUS.REJECT
        #self.accomplished2 = 0     #本就是0

    def on_progress(self,accomplished_volume,price):
        '''
            detail: BaseObject(contract_name,time,price,direction,volume,amount)
        '''
        assert self._accomplished + accomplished_volume <= self._approved
        self._accomplished += accomplished_volume
        self._details.append(BaseObject(volume=accomplished_volume,price=price))
        #assert self._accomplished2 == 0 or self._accomplished <= self._accomplished2
        #在部分移仓时会出现 _accomplished2 < self._accomplished这个情况. 如本order的仓位部分从移仓来,部分需要新开
        if self._accomplished2 < self._accomplished:
            self._accomplished2 = self._accomplished
        if self._accomplished2 >= self._approved and self._state == ORDER_STATUS.PART_SUCCESSED:
            #修正含transfer时, 在on_done中置成的PART_SUCCESSED状态. 此时因为有之前已transfer的数量垫底,accomplished数量比approved少,但实际上已经是SUCCESS
            self._state = ORDER_STATUS.SUCCESSED

    def on_done(self,accomplished_volume):
        """
            与on_progress分别调用
            这里有一个顺序问题.因为CTP的原因,先调用on_done(从RtnOrder发出),再调用on_progress(从OnTrade发出)
            所以在on_done中必须从accomplished2判断成交数量. 而不能从self.accomplished来判断
        """
        #print("POS:on_done")
        assert self._state not in (ORDER_STATUS.SUCCESSED,ORDER_STATUS.PART_SUCCESSED,ORDER_STATUS.CANCELLED,ORDER_STATUS.REJECT),"state={state}".format(state=self._state)
        #ORDER_STATUS.SUCCESSED,可能在on_progress中被赋值(transfer时)
        assert accomplished_volume <= self._approved
        if accomplished_volume >= self._approved:#后面的条件即实际上已经完成了. 用于transfer的情况
            self._state = ORDER_STATUS.SUCCESSED
        elif self._accomplished > 0:
            self._state = ORDER_STATUS.PART_SUCCESSED
        else:
            self._state = ORDER_STATUS.CANCELLED
        if accomplished_volume > self._accomplished2:   #当存在部分转移入的情况时, 会出现accomlished_volume<self._accomplished2
            self._accomplished2 = accomplished_volume


    @property
    def volume_on_the_flying(self):
        #print("get_on_the_flying,self._state=",self._state)
        if self._state in (ORDER_STATUS.SUCCESSED,ORDER_STATUS.PART_SUCCESSED,ORDER_STATUS.CANCELLED,ORDER_STATUS.REJECT):
            return self._accomplished2
        else:
            #print("get_on_the_flying,return",self._approved)
            return self._approved

    def to_dict(self):  #避免循环引用
        rev = dict(self.__dict__)
        del rev['_position']
        return rev


class Position(object):
    def __init__(self,contract,direction):
        """
            popen: Strategy.POPEN实例
            Position中还隐藏有外部注入的帐户编号
        """
        self._contract = contract
        self._direction = direction
        self._open_orders = []       #只允许有1个元素
        self._close_orders = []
        self._closed = False
        self._closers = set()       #仅针对本头寸的closer, 可能有Closer/ACloser/GCloser等类型的对象
        self._id = -1    #用于序列化

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,v):
        self._id = v

    @property
    def direction(self):
        return self._direction

    @property
    def contract(self):
        return self._contract

    @property
    def contract_name(self):
        return self._contract.name

    @property
    def closers(self):
        return self._closers

    @closers.setter
    def closers(self,cs):
        #仅用于反序列化
        self._closers = cs

    @property
    def open_orders(self):
        return self._open_orders

    @property
    def close_orders(self):
        return self._close_orders

    @property
    def open_order(self):   #position的创建逻辑保证len(open_orders)==1
        return self._open_orders[0] if self._open_orders else NULL_Order

    def add_open_order(self,popen):#目前一个position只建议有一个open_order
        """
            popen: Strategy.POPEN实例
            目前限定支持一个open_order
        """
        assert self._direction == popen.direction
        assert self._contract == popen.contract
        order = Order(self,XOPEN,popen.base_price,popen.planned,popen.unit,popen.extra_hops)
        self._open_orders.append(order)
        #print(popen.closers)
        self._closers.update(popen.closers)
        assert 1==len(self._open_orders)
        return order

    def add_close_order(self,pclose):
        assert pclose.unit <= self.volume_holding
        #if pclose.wanted > self.get_holding_volume():
        #    pclose.wanted = self.get_holding_volume()

        #print(type(self.open_orders[0].trade_info.trading_day),self.open_orders[0].trade_info.trading_day)
        #print(self.contract.trading_day)
        ctype = XCLOSE if self._open_orders[0].trade_info.trading_day < self._contract.trading_day else XCLOSE_TODAY
        #print("pclose:",pclose.extra_hops,pclose.direction)
        order = Order(self._open_orders[0].position,ctype,pclose.base_price,pclose.planned,pclose.unit,pclose.extra_hops)
        order.account = self.open_order.account
        self._close_orders.append(order)
        #print("-------------------in position,close_order.target_price",order.target_price)
        return order

    def _get_on_the_flying(self,orders):
        num = 0
        for order in orders:
            num += order.volume_on_the_flying
        return num

    def _get_accomplished2(self,orders):
        num = 0
        for order in orders:
            num += order.accomplished2
        return num

    def _get_approved(self,orders):
        num = 0
        for order in orders:
            #print(order.approved)
            num += order.approved
        return num

    @property
    def volume_holding(self):
        num_opening = self._get_on_the_flying(self._open_orders)
        num_closing = self._get_on_the_flying(self._close_orders)
        return num_opening - num_closing

    @property
    def volume_accomplished2(self):
        num_opened = self._get_accomplished2(self._open_orders)
        num_closed = self._get_accomplished2(self._close_orders)
        return num_opened - num_closed

    @property
    def volume_approved(self):
        num_opened = self._get_approved(self._open_orders)
        num_closed = self._get_approved(self._close_orders)
        return num_opened - num_closed

    def check_closed(self): #不考虑平仓失败的情况
        #print("in check_closed,self.closed=",self._closed)
        if self._closed:
            return True
        #if self.open_orders[0].approved == 0:
        #    self.closed = True
        num_opened = self._get_on_the_flying(self._open_orders)
        num_closed = self._get_accomplished2(self._close_orders)
        #print(id(self),num_opened,num_closed)
        assert num_opened >= num_closed
        #print(num_opened,num_closed,self.get_approved(self.open_orders))
        #if num_opened > 0 and num_opened == num_closed: #不考虑open只完成部分且仍然悬挂的情况
        #    self.closed = True
        #elif self.get_approved(self.open_orders) == 0:
        #    self.closed = True
        if num_opened <= num_closed:
            self._closed = True
        return self._closed

    def to_dict(self):  ##避免循环引用, 需要记录的是position.ID
        rev = dict(self.__dict__)
        rev["_closers"] = list(rev["_closers"])
        return rev

    @staticmethod
    def from_dict(d):   #
        sobj = Position.__new__(Position)
        sobj.__dict__.update(d)
        sobj.closers = set(sobj.closers)
        for corder in sobj.open_orders:
            corder._position = sobj
        for corder in sobj.close_orders:
            corder._position = sobj
        return sobj


NULL_Position = Position(BaseObject(name='14PNone',price_tick=2,lowerlimit_price=0,upperlimit_price=10000),LONG)
#NULL_Position = Position(BaseObject(name='14PNone'),LONG)
NULL_Order = Order(NULL_Position,XOPEN,0,0,0,0)

class PosInfo(object):
    def __init__(self,contract_name,num_long=0,num_short=0):
        self._contract_name = contract_name
        self._num_long = num_long
        self._num_short = num_short

    def add_long(self,num):
        self._num_long += num

    def add_short(self,num):
        self._num_short += num

    def add(self,other_info):
        assert self._contract_name == other_info._contract_name,"PosInfo相加，必须相同合约"
        self._num_long  += other_info._num_long
        self._num_short += other_info._num_short

    @property
    def contract_name(self):
        return self._contract_name

    @property
    def num_long(self):
        return self._num_long

    @num_long.setter
    def num_long(self,v):
        self._num_long = v

    @property
    def num_short(self):
        return self._num_short

    @num_short.setter
    def num_short(self,v):
        self._num_short = v

    @property
    def net(self):
        return self._num_long - self._num_short

    @property
    def total(self):
        return self._num_long + self._num_short


EMPTY_POSINFO = PosInfo("CEMPTY",0,0)       #空信息

class PositionHolder(object):
    def __init__(self):
        #self.holder = holder
        self._active_positions = []  #这是一个缓存, 在序列化时需要特别处理
        self._closed_positions = []  # active_positions中close后的保存场所
        self._name2positions = {} # name -> [position], 与active_positions一致,但是以另一种组织方式. self.active_positions = []  #这是一个缓存, 在序列化时需要特别处理
        self._max_position_id = 1
        self._lock = Lock()

    @property
    def active_positions(self):
        return self._active_positions

    @property
    def closed_positions(self):
        return self._closed_positions

    @property
    def name2positions(self):
        return self._name2positions

    @name2positions.setter
    def name2positions(self,n2p):
        self._name2positions = n2p

    def inc_position_id(self):  #仅用于序列化
        self._max_position_id += 1
        return self._max_position_id

    def add_positions(self,positions):  #针对grouped position
        #应当做一个判断, 即positions中每个contract都互不相同
        cs = set()
        with self._lock:
            for position in positions:
                self._add_position(position)
                assert position.contract not in cs, "同一个contract在同一时刻不能分为多个positions"
                cs.add(position.contract)
            self._fill_closer(positions)

    def _add_position(self,position):
        self._name2positions.setdefault(position.contract.name, []).append(position)
        self._active_positions.append(position)
        position.id = self.inc_position_id()

    def _fill_closer(self,positions):
        for position in positions:
            for closer in position.closers:
                if isinstance(closer,Closer):
                    closer.prepare(positions)
                    #print("Closer")
                elif isinstance(closer,ContractCloser):
                    closer.prepare(self,position.contract)
                    #print("ContractCloser")
                elif isinstance(closer,GlobalCloser):
                    closer.prepare(self)
                    #print("GlobalCloser")

    def add_closed_position(self,cpos): #用于transfer时的处理
        self._closed_positions.append(cpos)

    def get_volume_holding(self,contract_name):
        """
            返回 总头寸, 多空均累加
        """
        volume = 0
        for pos in self._name2positions.get(contract_name,[]):
            volume += pos.volume_holding
        return volume

    def get_net_volume_holding(self,contract_name):
        """
            返回 净头寸, 返回值>0为净多,<0为净空
        """
        volume = 0
        for pos in self._name2positions.get(contract_name,[]):
            if pos.direction == LONG:
                volume += pos.volume_holding
            else:
                volume -= pos.volume_holding
        return volume


    def get_volume_approved(self,contract_name):
        """
            返回 已批准总头寸, 多空均累加
        """
        volume = 0
        for pos in self._name2positions.get(contract_name,[]):
            volume += pos.volume_approved
        return volume

    def get_net_volume_approved(self,contract_name):
        """
            返回 已批准净头寸, 返回值>0为净多,<0为净空
        """
        volume = 0
        for pos in self._name2positions.get(contract_name,[]):
            if pos.direction == LONG:
                volume += pos.volume_holding
            else:
                volume -= pos.volume_holding
        return volume


    def get_holding_info(self,contract_name):
        pinfo = PosInfo(contract_name)
        for pos in self._name2positions.get(contract_name,[]):
            if pos.direction == LONG:
                pinfo.add_long(pos.volume_holding)
            else:
                pinfo.add_short(pos.volume_holding)
        return pinfo

    def get_approved_info(self,contract_name):
        pinfo = PosInfo(contract_name)
        for pos in self._name2positions.get(contract_name,[]):
            if pos.direction == LONG:
                pinfo.add_long(pos.volume_approved)
            else:
                pinfo.add_short(pos.volume_approved)
        return pinfo

    def get_positions_by_name(self,contract_name):
        return self._name2positions.get(contract_name,[])

    def on_order_done(self,position):
        """
            用于判定posiition状态
            position只有在close成功后才会被移出
        """
        if position.check_closed():
            with self._lock:
                self._name2positions[position.contract.name].remove(position)
                #self._closed_positions.append(position)
                self.add_closed_position(position)
                self.active_positions.remove(position)

    def to_dict(self):
        ## 有必要验证下 active_positions和name2positions的一致性?
        self.check_consistency()
        rev = dict(self.__dict__)
        del rev['_lock']
        del rev['_name2positions']
        del rev['_closed_positions']
        return rev

    @staticmethod
    def from_dict(d):   #
        sobj = PositionHolder.__new__(PositionHolder)
        sobj.__dict__.update(d)
        #设定lock
        sobj._lock = Lock()
        sobj._name2positions = {}
        sobj._closed_positions = []
        #处理closer中的position设定
        id2pos = {}
        my_closers = set()
        for pos in sobj.active_positions:
            assert pos.id not in id2pos,"active_positions中不允许出现重复的pos"
            id2pos[pos.id] = pos
            for xcloser in pos.closers:
                if isinstance(xcloser,Closer):
                    my_closers.add(xcloser)
                else:
                    xcloser._position_holder = sobj       #ContractCloser或GlobalCloser
            sobj.name2positions.setdefault(pos.contract.name, []).append(pos)
        #PositionHolder.check_repeat(mposes,sobj.active_positions)
        #print(sobj.closed_positions)
        """
        for pos in sobj.closed_positions:
            assert pos.id not in id2pos,"closed_positions中不允许出现重复的pos"
            id2pos[pos.id] = pos
            for xcloser in pos.closers:
                if isinstance(xcloser,Closer):
                    my_closers.add(xcloser)
                else:
                    xcloser._position_holder = sobj       #ContractCloser或GlobalCloser
        """
        for closer in my_closers:
            closer.positions = [id2pos[pid] for pid in closer.position_ids]
        return sobj

    def check_consistency(self):
        """
            确认 active_positions和name2positions的一致性
        """
        act_set = set(self._active_positions)
        act_set2 = set()
        for poses in self._name2positions.values():
            for pos in poses:
                assert pos in act_set,"name2position中的position必须在active_position中出现"
                act_set2.add(pos)
        assert len(act_set2) == len(act_set), "active_positions中的position也必须在name2position中出现"
        return True


class CloserParameter(object):
    """
        数据对象
    """
    def __init__(self,extremum,stop_line):
        self.extremum = extremum
        self.stop_line = stop_line

    def create_transfer_parameter(self,cfroms,ctos):
        """
            cfroms是迁出的合约列表
            ctos是迁入的合约列表
                自身的顺序非常重要!!!
            子类必须实现. 预定义了最简单的情况
            对于复杂的情况, 策略必须实现自己的CloserParameter
        """
        raise NotImplementedError


class LongCloserParameter0(CloserParameter):
    def __init__(self,extremum=0,stop_line=0):
        CloserParameter.__init__(self,extremum,stop_line)

    def create_transfer_parameter(self,cfroms,ctos):
        delta = 0
        nlcp = LongCloserParameter0(self.extremum+delta,self.stop_line+delta)
        return nlcp

class ShortCloserParameter0(CloserParameter):
    def __init__(self,extremum=99999999,stop_line=99999999):
        CloserParameter.__init__(self,extremum,stop_line)

    def create_transfer_parameter(self,cfroms,ctos):
        delta = 0
        nscp = ShortCloserParameter0(self.extremum - delta,self.stop_line - delta)
        return nscp

class LongCloserParameter1(CloserParameter):
    def __init__(self,extremum=0,stop_line=0):
        CloserParameter.__init__(self,extremum,stop_line)

    def create_transfer_parameter(self,cfroms,ctos):
        delta = ctos[0].last_price - cfroms[0].last_price
        nlcp = LongCloserParameter1(self.extremum+delta,self.stop_line+delta)
        return nlcp

class ShortCloserParameter1(CloserParameter):
    def __init__(self,extremum=99999999,stop_line=99999999):
        CloserParameter.__init__(self,extremum,stop_line)

    def create_transfer_parameter(self,cfroms,ctos):
        delta = ctos[0].last_price - cfroms[0].last_price
        nscp = ShortCloserParameter1(self.extremum - delta,self.stop_line - delta)
        return nscp

class LongCloserParameter2(CloserParameter):
    def __init__(self,extremum=0,stop_line=0):
        CloserParameter.__init__(self,extremum,stop_line)

    def create_transfer_parameter(self,cfroms,ctos):
        """
            按 合约1-合约2 作为计算基准
        """
        delta = (ctos[0].last_price-ctos[1].last_price) - (cfroms[0].last_price-cfroms[1].last_price)
        nlcp = LongCloserParameter2(self.extremum+delta,self.stop_line+delta)
        return nlcp

class ShortCloserParameter2(CloserParameter):
    def __init__(self,extremum=99999999,stop_line=99999999):
        CloserParameter.__init__(self,extremum,stop_line)

    def create_transfer_parameter(self,cfroms,ctos):
        """
            按 合约1-合约2 作为计算基准
        """
        delta = (ctos[0].last_price-ctos[1].last_price) - (cfroms[0].last_price-cfroms[1].last_price)
        nscp = ShortCloserParameter2(self.extremum - delta,self.stop_line - delta)
        return nscp


class BaseCloser(object):   #用于序列化
    _id = 1
    def __init__(self,close_func,param_object):
        self._close_func = close_func
        self._param_object = param_object
        self._id = self.inc_id()

    @classmethod
    def create_tranfer_closer(cls,source,cfroms,ctos):
        """
            source: 源closer
            cfroms: 源contracts
            ctos: 目标contracts
        """
        nparam = source.param_object.create_transfer_parameter(cfroms,ctos)
        nc = cls(source.close_func,nparam)
        return nc

    @property
    def id(self):
        return self._id

    @property
    def close_func(self):
        return self._close_func

    @property
    def close_func_name(self):
        try:
            return self._close_func_name
        except AttributeError:
            return self._close_func.__name__

    @property
    def param_object(self):
        return self._param_object

    @param_object.setter
    def param_object(self,v):
        #self.param_object = v
        raise TypeError("不支持初始化后再设定param_object")


    @staticmethod
    def inc_id():
        BaseCloser._id += 1
        return BaseCloser._id

    def to_dict(self):  ##避免循环引用, 需要记录的是position.ID
        rev = dict(self.__dict__)
        del rev['_close_func']
        rev['_close_func_name'] = self.close_func_name  #self._close_func.__name__
        #print(rev['close_func'])
        return rev


class Closer(BaseCloser):
    """
        作用于单/多合约单个头寸的Closer
        因为存在对positions的循环引用,故序列化需要特别处理
    """
    def __init__(self,close_func,param_object):
        """
            param_object : CloserParameter对象
        """
        BaseCloser.__init__(self,close_func,param_object)
        self._positions = []

    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self,poses):
        #仅在反序列花时使用
        self._positions = poses

    @property
    def position_ids(self):
        #仅在反序列化时使用,由from_dict设定_position_ids
        return self._position_ids

    @property
    def contracts(self):
        cs = OrderedDict([(pos.contract,pos.contract) for pos in self.positions])
        return list(cs.keys())

    def prepare(self,positions):
        self._positions = positions

    def check(self,ctick,*contract):
        if len(self._positions) == 1:        #正常情况
            return self._close_func(ctick,self._positions[0],self._param_object,*contract)
        else:#当两个position在同一tick开仓时, 有这个情况
            return self._close_func(ctick,self._positions,self._param_object,*contract)

    def to_dict(self):  ##避免循环引用, 需要记录的是position.ID
        rev = BaseCloser.to_dict(self)
        del rev['_positions']
        rev["_position_ids"] = [pos.id for pos in self._positions]
        return rev

    #Closer的加载需要在PositionHolder(设定position和holder)和StrateAgent(设定close_func)两个层面来解决


class ContractCloser(BaseCloser):
    """
        作用于PositionHolder上单合约的Closer
        因为存在对position的循环引用,故序列化需要特别处理
    """
    def __init__(self,close_func,param_object):
        """
            param_object : CloserParameter对象
        """
        BaseCloser.__init__(self,close_func,param_object)
        self._position_holder = None
        self._contract = None

    @property
    def position_holder(self):
        return self._position_holder

    @position_holder.setter
    def position_holder(self,pholder):
        self._position_holder = pholder

    @property
    def contract(self):
        return self._contract

    @contract.setter
    def contract(self,contract):
        #self._contract_name = name
        raise TypeError("不支持初始化后再单独设定contract_name,请使用prepare方法")

    @property
    def contracts(self):
        return [self.contract]

    def prepare(self,position_holder,contract):
        self._position_holder = position_holder
        self._contract = contract

    def check(self,ctick,*contract):
        holding_volume = self._position_holder.get_volume_holding(self._contract.name)
        #positions = self.position_holder.get_contracts_by_name(self.contract.name)
        return self._close_func(ctick,holding_volume,self._param_object,*contract)

    def to_dict(self):  #避免循环引用
        rev = BaseCloser.to_dict(self)
        del rev['_position_holder']
        return rev


class GlobalCloser(BaseCloser):
    """
        作用于PositionHolder的Closer
        因为存在对position的循环引用,故序列化需要特别处理
    """
    def __init__(self,close_func,param_object):
        """
            param_object : CloserParameter对象
        """
        BaseCloser.__init__(self,close_func,param_object)
        self._position_holder = None

    @property
    def position_holder(self):
        return self._position_holder

    @position_holder.setter
    def position_holder(self,pholder):
        self._position_holder = pholder

    @property
    def contracts(self):
        return list(self._position_holder.name2positions.keys())

    def prepare(self,position_holder):
        self._position_holder = position_holder

    def check(self,ctick,*contract):
        #print("GC:check:",contract)
        return self._close_func(ctick,self._position_holder.name2positions,self._param_object,*contract)

    def to_dict(self):  #避免循环引用
        rev = BaseCloser.to_dict(self)
        del rev['_position_holder']
        return rev


NULL_CLOSER = Closer(lambda x,y,*z:[],None)



