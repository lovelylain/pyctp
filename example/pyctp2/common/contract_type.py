# -*- coding: utf-8 -*-

'''
    对监听合约进行定义
    只监听对分钟周期有意义的合约
'''

from functools import reduce
from datetime import datetime

import re
import logging
import traceback

from ..common.utils import (fcustom,
                    ArgsCached,
                    TList,
                    next_minute,
                    with_metaclass
                )
from ..core.dac import (MINUTE,
                        MINUTE2D,
                    )
from .base import BaseObject,LONG,SHORT
from ..common.reader import read_day,readn_m1


class TradingStatus:
    Unknown = -1
    #开盘前
    BeforeTrading = 0
    #非交易
    NoTrading = 1
    #连续交易
    Continous = 2
    #集合竞价报单
    AuctionOrdering = 3
    #集合竞价价格平衡
    THOST_FTDC_IS_AuctionBalance = 4
    #集合竞价撮合
    AuctionMatch = 5
    #收盘
    Closed = 6


@with_metaclass(ArgsCached)
class Base_ContractType:
    """
        这里采用ArgsCached为metaclass, 只为了在ContractInfo持续化时使用缓存
            也可采用CM_ALL来找回ctype,更加简单.但是不如这个来得完整(ctype_name+exchange_name)
    """
    _cached_args = ["name","exchange_name"]
    def __init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder):
        self._name = name
        self._exchange_name = exchange_name
        self._multiplier = multiplier
        self._unit = unit
        self._base_marginrate = marginrate
        self._contract_builder = contract_builder

    @property
    def name(self):
        return self._name

    @property
    def exchange_name(self):
        return self._exchange_name

    @property
    def multiplier(self):
        return self._multiplier

    @property
    def unit(self):
        return self._unit

    @property
    def base_marginrate(self):
        return self._base_marginrate

    @property
    def flen(self):#小数位数
        '''
            这个用于在保存数据时去掉小数的尾部零
            实际上也可以采用 round(f+epsl,4)来搞定, round+print('%s')的结果是自然去尾部0 (除了.0的第一个0不能去掉)
                不过round + print('%f')的方式,反而会打很多(6个)尾0
              采用round办法, 数据保存的处理上会麻烦不少
              故仍然采用当前方案
        '''
        if self._unit >= 1:
            return 0
        elif self._unit >=0.1:
            return 1
        elif self._unit >= 0.01:
            return 2
        elif self._unit >= 0.001:
            return 3
        else:   #都默认为0.0001级别
            return 4

#from inspect import getfullargspec


@with_metaclass(ArgsCached)
class ContractInfo:
    """
        同name的ContractInfo只会被创建一次.
        因此,如果存在 名字相同而ymonth不同的合约,就会出现混乱
    """
    _cached_args = ["name"]
    def __init__(self,name,ymonth,ctype):
        """
            ymonth: yyMM表示的月份
        """
        #print("in contract_info init,name=",name)
        #print(name,ymonth)
        self._name = name
        self._ymonth = ymonth
        self._ctype = ctype
        self._trading_day = -1   #在environ中赋值
        self._ticks = TList()
        self._exchange_id = ""
        self._price_tick = 1    #最小价格跳动单位,默认为1
        self._multiple = 4.5      #合约乘数,默认为4.5,表示未精确化
        self._trading_status = None
        self._upperlimit_price = 99999999 #0      #默认为最大值,然后被精确化
        self._lowerlimit_price = 0  #99999999   #默认为最小值,然后被精确化
        self._long_marginrate = 0.12    #默认值
        self._short_marginrate = 0.12   #默认值
        #self._minutes = MINUTE(self._ticks)
        #self._days = MINUTED(self.minutes)
        self._minutes = None
        self._days = None

    @property
    def name(self):
        return self._name

    @property
    def month(self):
        return self._ymonth % 100

    @property
    def ymonth(self):
        return self._ymonth

    @property
    def ctype(self):
        return self._ctype

    @property
    def ticks(self):
        return self._ticks

    @property
    def minutes(self):
        return self._minutes

    @property
    def days(self):
        return self._days

    @property
    def trading_day(self):
        return self._trading_day

    @trading_day.setter
    def trading_day(self,trading_day):
        self._trading_day = trading_day

    @property
    def exchange_id(self):
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self,exchange_id):
        self._exchange_id = exchange_id

    @property
    def price_tick(self):
        return self._price_tick

    @price_tick.setter
    def price_tick(self,price_tick):
        self._price_tick = price_tick

    @property
    def multiple(self):
        return self._multiple

    @multiple.setter
    def multiple(self,multiple):
        self._multiple = multiple

    @property
    def unit(self):
        return self._ctype.unit

    @property
    def trading_status(self):
        return self._trading_status

    @trading_status.setter
    def trading_status(self, status):
        self.trading_status = status

    @property
    def upperlimit_price(self):
        return self._upperlimit_price

    @upperlimit_price.setter
    def upperlimit_price(self, ul_price):
        #print("set upper_limit_price",ul_price)
        self._upperlimit_price = ul_price

    @property
    def lowerlimit_price(self):
        return self._lowerlimit_price

    @lowerlimit_price.setter
    def lowerlimit_price(self, ll_price):
        self._lowerlimit_price = ll_price

    @property
    def long_marginrate(self):
        return self._long_marginrate

    @long_marginrate.setter
    def long_marginrate(self, marginrate):
        self._long_marginrate = marginrate

    @property
    def short_marginrate(self):
        return self._short_marginrate

    @short_marginrate.setter
    def short_marginrate(self, marginrate):
        self._short_marginrate = marginrate

    @property
    def last_price(self):
        if self._ticks:
            #print(self.ticks[-1])
            return self._ticks[-1].price
        elif self._minutes:
            return self._minutes[-1].sclose
        elif self._days:
            return self._days[-1].sclose
        else:
            raise IndexError

    @property
    def last_dvolume(self):
        if self.ticks:
            return self.ticks[-1].dvolume
        elif self.days:
            return self.days[-1].svolume
        else:
            raise IndexError

    @property
    def last_drange(self):
        if self.days:
            #print(self.days[-1].__dict__)
            return self.days[-1].shigh - self.days[-1].slow
        elif self.ticks:    #这个可能是当日的数据,在中间恢复时
            return self.ticks[-1].drange
        else:
            raise IndexError

    @property
    def last_day(self):
        if self.days:
            return self.days[-1]
        else:
            raise IndexError

    def calc_margin(self,direction,price):
        #print("id=%d,name=%s,long_marginrate:%02f,short_marginrate=%02f" % (id(self),self.name,self.long_marginrate,self.short_marginrate))
        cmarginrate = self.long_marginrate if direction == LONG else self.short_marginrate
        #print("cmarginrate:",cmarginrate)
        margin = self.multiple * price * cmarginrate
        #print(self.multiple,price,cmarginrate)
        logging.debug("margin:%02f",margin)
        return margin

    def calc_month_distance(self,cmonth):
        #print("%s.month=%d" % (self._name,self._ymonth))
        return (self._ymonth // 100 * 12 + self._ymonth%100) - (cmonth//100*12 + cmonth%100)

    def _wipeoff(self,seq,lastday=99999999):
        #print(len(seq),seq[-1])
        #print("wipeoff:lastday=%s,last_seq=%s"%(lastday,seq[-1].sdate))
        i = len(seq) - 1
        while i>=0 and seq[i].sdate > lastday:
            #print(lastday,seq[i].sdate)
            i = i-1
        if i==-1:
            seq[:] = []
        else:
            seq[i+1:] = []
        #print(len(seq),seq[-1])

    def resume_old(self,lastday=99999999,mlen=99999999):   #恢复minutes和days, 不恢复ticks
        """
            先读再去掉,这个是不正确的使用方式
        """
        if self._minutes:   #已经恢复
            print("already resumed")
            return
        try:
            pre_minutes = readn_m1(self.name,size=mlen)
            #print(len(pre_minutes))
            self._wipeoff(pre_minutes,lastday)
            #print("len(preminutes):",len(pre_minutes))
            pre_days = read_day(self.name)
            self._wipeoff(pre_days,lastday)
            #print(len(pre_days),len(pre_minutes))
            #print(len(pre_minutes),pre_minutes[-1])
            self._minutes = MINUTE(self.ticks,pre_minutes)
            #self._days = MINUTE2D(self._minutes,pre_days)
            self._days = pre_days
            #print("self._minutes:",len(self._minutes),len(pre_minutes))
        except FileNotFoundError as fnfe:
            #logging.error("Contract %s resume Error, 找不到相关文件, %s,%s" % (self.name,fnfe,traceback.format_exc))
            logging.exception("Contract %s resume Error, 找不到相关文件, %s" % (self.name,fnfe,))

    def resume(self,lastday=99999999,mlen=99999999):   #恢复minutes和days, 不恢复ticks
        if self._minutes:   #已经恢复
            #print("already resumed")
            return
        try:
            #import time
            #ta = time.time()
            #print("resume load data",self.name)
            pre_minutes = readn_m1(self.name,up2day=lastday,size=mlen)
            pre_days = read_day(self.name,up2day=lastday)
            self._minutes = MINUTE(self.ticks,pre_minutes)
            #self._days = MINUTE2D(self._minutes,pre_days)
            self._days = pre_days
            #print("self._minutes:",len(self._minutes),len(pre_minutes))
            #print("resume:",self.name,time.time()-ta)
        except FileNotFoundError as fnfe:
            #logging.error("Contract %s resume Error, 找不到相关文件, %s,%s" % (self.name,fnfe,traceback.format_exc))
            logging.exception("Contract %s resume Error, 找不到相关文件, %s" % (self.name,fnfe,))


    def calc_next_trade_minute(self,cur_minute):    #计算因非交易时段不能下单而引起的延后交易
        return calc_next_trade_minute(self,cur_minute)

    def to_dict(self):      #
        rev = dict(_name=self._name,_exchange_name=self._ctype._exchange_name)
        return rev

    @staticmethod
    def from_dict(d):
        name = d["_name"]
        type_name = name[0] if name[1].isdigit() else name[:2]
        exchange_name = d["_exchange_name"]
        ctype = Base_ContractType(type_name,exchange_name,0,0,0,None)   #利用Base_ContractType中的缓存, 只需要设定两个关键字
        contract = ContractInfo(name,ctype)
        return contract


def build_contract(ctype,tname,year,months):
    return [ContractInfo(ymonth=year%100*100+m,ctype=ctype,name='%s%s%02d' % (tname,year%100 + (m-1)//12, (m-1)%12+1)) for m in months]

def build_contract1(ctype,tname,year,months):    #郑商所品种
    return [ContractInfo(ymonth=year%100*100+m,ctype=ctype,name='%s%s%02d' % (tname,year%10 + (m-1)//12, (m-1)%12+1)) for m in months]



class ContractType_None(Base_ContractType):
    '''
        空合约类型, 成交稀少或已失效品种, 如线材
    '''
    def __init__(self,name,exchange_name,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)

    def calc_contracts(self,year=0,month=0,day=0):
        return []


class ContractType_a2n(Base_ContractType):
    '''
        一般金属类型
        只监听 C+1->N 共N个周期的合约.
    '''
    def __init__(self,name,exchange_name,num,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        '''
           num: 顺延的合约数
           multiplier: 合约乘数 
           unit: 合约单位
        '''
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)
        self._num = num

    def calc_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        listened = range(month+1,month+self._num+1)
        return self._contract_builder(self,self._name,year,listened)
        
class ContractType_6_12(Base_ContractType):
    '''
        贵金属类型
        只监听 6/12两个周期的合约
    '''
    def __init__(self,name,exchange_name,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)

    def calc_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        if month <= 6:
            listened = [6,12,18]
        else:
            listened = [12,18,24]
        return self._contract_builder(self,self._name,year,listened)


class ContractType_5_10_1(Base_ContractType):
    '''
        5,10,1类型, 如rb
    '''
    def __init__(self,name,exchange_name,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)

    def calc_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        if month < 5:
            listened = [5,10,13]    #13未必有,但不必太纠结
        elif month < 10:
            listened = [10,13,17]
        else:   #9-12
            listened = [13,17,22]   #此时1还在,所以不可能出现25
        return self._contract_builder(self,self._name,year,listened)


class ContractType_5_9_1(Base_ContractType):
    '''
        5-9-1
        农产品及大商所均为此类,郑商所部分为此类
    '''
    def __init__(self,name,exchange_name,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)

    def calc_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        if month < 5:
            listened = [5,9,13]    #13未必有,但不必太纠结
        elif month < 9:
            listened = [9,13,17]
        else:   #9-12
            listened = [13,17,21]   #此时1还在,所以不可能出现25
        return self._contract_builder(self,self._name,year,listened)

ZSS_5_9_1 = fcustom(ContractType_5_9_1,contract_builder = build_contract1)


class ContractType_5_9_1_5(Base_ContractType):
    '''
        5-9-13-17 两轮， 再往下无操作意义
        郑商所部分为此类
    '''
    def __init__(self,name,exchange_name,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)

    def calc_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        if month < 5:
            listened = [5,9,13,17]    #13未必有,但不必太纠结
        elif month < 9:
            listened = [9,13,17,21]
        else:   #9-12
            listened = [13,17,21,25]   #此时1还在,所以不可能出现25
        return self._contract_builder(self,self._name,year,listened)

ZSS_5_9_1_5 = fcustom(ContractType_5_9_1_5,contract_builder = build_contract1)


class ContractType_quarter(Base_ContractType):
    '''
        季度合约，目前仅TF
    '''
    def __init__(self,name,exchange_name,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)

    def calc_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        if month < 3:
            listened = [3,6,9,12]    #13未必有,但不必太纠结
        elif month < 6:
            listened = [6,9,12,15]
        elif month < 9:
            listened = [9,12,15,18]
        else:
            listened = [12,15,18,21]   #此时1还在,所以不可能出现25
        return self._contract_builder(self,self._name,year,listened)


class ContractType_0136(Base_ContractType):
    '''
        当(月)下(月)季(月)半年(月), 仅IF
    '''
    def __init__(self,name,exchange_name,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)
        '''
        self.cmap = dict([ (1,[1,2,3,6,9]),
                           (2,[2,3,4,6,9]),
                           (3,[3,4,5,6,9]),
                           (4,[4,5,6,9,12]),
                           (5,[5,6,7,9,12]),
                           (6,[6,7,8,9,12]),
                           (7,[7,8,9,12,15]),
                           (8,[8,9,10,12,15]),
                           (9,[9,10,11,12,15]),
                           (10,[10,11,12,15,18]),
                           (11,[11,12,13,15,18]),
                           (12,[12,13,14,15,18])
                        ])
        '''

    def calc_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        #listened = self.cmap[month]
        listened = [month,month+1,month+2,((month-1)//3+2)*3,((month-1)//3+3)*3]
        return self._contract_builder(self,self._name,year,listened)

class ContractType_odd(Base_ContractType):
    '''
        单数月, Ru也归入此列(目前以5-9-1为主)
        num为展望期(1年为12)
    '''
    def __init__(self,name,exchange_name,num,multiplier,unit=1,marginrate=0.1,contract_builder=build_contract):
        Base_ContractType.__init__(self,name,exchange_name,multiplier,unit,marginrate,contract_builder)
        self._num = num

    def calc_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        if month % 2 == 1: #奇数月
            listened = range(month+2,month+self._num+1)
        else:#偶数月
            listened = range(month+1,month+self._num)
        return self._contract_builder(self,self._name,year,listened)

#上海
RB = ContractType_5_10_1('rb','SHFE',multiplier=10,unit=1)
CU = ContractType_a2n('cu','SHFE',6,multiplier=5,unit=10)
AL = ContractType_a2n('al','SHFE',4,multiplier=5,unit=5)
ZN = ContractType_a2n('zn','SHFE',4,multiplier=5,unit=5)
AG = ContractType_6_12('ag','SHFE',multiplier=1000,unit=1)
AU = ContractType_6_12('au','SHFE',multiplier=15,unit=0.05)
BU = ContractType_6_12('bu','SHFE',multiplier=10,unit=2)
RU = ContractType_5_9_1('ru','SHFE',multiplier=10,unit=5)

XH = ContractType_5_9_1('XH','SHFE',multiplier=10,unit=5)   #测试用
#大连
M = ContractType_5_9_1('m','DCE',multiplier=10,unit=1)
A = ContractType_5_9_1('a','DCE',multiplier=10,unit=1)
C = ContractType_5_9_1('c','DCE',multiplier=10,unit=1)
Y = ContractType_5_9_1('y','DCE',multiplier=10,unit=2)
L = ContractType_5_9_1('l','DCE',multiplier=5,unit=5)
P = ContractType_5_9_1('p','DCE',multiplier=10,unit=2)
V = ContractType_5_9_1('v','DCE',multiplier=5,unit=5)
J = ContractType_5_9_1('j','DCE',multiplier=100,unit=1)
JM = ContractType_5_9_1('jm','DCE',multiplier=60,unit=1)
I = ContractType_5_9_1('i','DCE',multiplier=100,unit=1)
JD = ContractType_5_9_1('jd','DCE',multiplier=5,unit=1)
FB = ContractType_5_9_1('fb','DCE',multiplier=500,unit=0.05)
BB = ContractType_5_9_1('bb','DCE',multiplier=500,unit=0.05)
PP = ContractType_5_9_1('pp','DCE',multiplier=5,unit=1)
#郑州
#SR = ContractType_5_9_1_5('SR','CZCE',multiplier=10,unit=1)
#WH = ContractType_5_9_1('WH','CZCE',multiplier=20,unit=2)
#CF = ContractType_5_9_1('CF','CZCE',multiplier=5,unit=5)
#TA = ContractType_5_9_1('TA','CZCE',multiplier=5,unit=2)
#OI = ContractType_5_9_1('OI','CZCE',multiplier=10,unit=2)
#RI = ContractType_5_9_1('RI','CZCE',multiplier=20,unit=1)
#ME = ContractType_5_9_1('ME','CZCE',multiplier=50,unit=1)
#FG = ContractType_5_9_1('FG','CZCE',multiplier=20,unit=1)
#RM = ContractType_5_9_1('RM','CZCE',multiplier=10,unit=1)
#TC = ContractType_5_9_1('TC','CZCE',multiplier=200,unit=0.2)
#RS = ContractType_5_9_1('RS','CZCE',multiplier=10,unit=1)

SR = ZSS_5_9_1_5('SR','CZCE',multiplier=10,unit=1)
WH = ZSS_5_9_1('WH','CZCE',multiplier=20,unit=2)
CF = ZSS_5_9_1('CF','CZCE',multiplier=5,unit=5)
TA = ZSS_5_9_1('TA','CZCE',multiplier=5,unit=2)
OI = ZSS_5_9_1('OI','CZCE',multiplier=10,unit=2)
RI = ZSS_5_9_1('RI','CZCE',multiplier=20,unit=1)
ME = ZSS_5_9_1('ME','CZCE',multiplier=50,unit=1)
FG = ZSS_5_9_1('FG','CZCE',multiplier=20,unit=1)
RM = ZSS_5_9_1('RM','CZCE',multiplier=10,unit=1)
TC = ZSS_5_9_1('TC','CZCE',multiplier=200,unit=0.2)
RS = ZSS_5_9_1('RS','CZCE',multiplier=10,unit=1)

XX = ZSS_5_9_1('XX','CZCE',multiplier=10,unit=1)    #测试用

#中金
IF = ContractType_0136('IF','CFFEX',multiplier=300,unit=0.2)
TF = ContractType_quarter('TF','CFFEX',multiplier=10000,unit=0.002)


class ContractManager(object):
    '''
        管理Contract的设定
        用于行情存储与策略合约监控
    '''
    def __init__(self,contract_types):
        self._contract_types = contract_types
        self._name2type = self._name2type()
        self._name_pattern = re.compile("([a-zA-Z]{1,2})(\d{3,4})")
        self.current_contracts()        #设定Contracts, 建立缓存

    @property
    def contract_types(self):
        return self._contract_types

    def current_contracts(self,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        contractss = [ ct.calc_contracts(year,month,day) for ct in self._contract_types ]
        return reduce(lambda x,y:x+y,contractss)

    @staticmethod
    def current_contracts_by_ctype(ctype,year=0,month=0,day=0):
        if year == 0:
            today = datetime.today()
            year,month,day = today.year,today.month,today.day
        contracts = ctype.calc_contracts(year,month,day)
        return contracts

    def cname2ctype(self,contract_name):
        r = self._name_pattern.match(contract_name)
        ctype_name = r.group(1)
        return self._name2type[ctype_name]

    def tname2ctype(self,tname):
        return self._name2type[tname]

    def _name2type(self):
        n2t = {}
        for ct in self._contract_types:
            n2t[ct.name] = ct
        return n2t


CM_ALL = ContractManager([RB,CU,AL,ZN,AG,AU,BU,RU,M,A,C,Y,L,P,V,J,JM,I,JD,FB,BB,PP,SR,WH,CF,TA,OI,RI,ME,FG,RM,TC,IF,TF])
CM_SH = ContractManager([RB,CU,AL,ZN,AG,AU,BU,RU])
CM_DL = ContractManager([M,A,C,Y,L,P,V,J,JM,I,JD,FB,BB,PP])
CM_ZZ = ContractManager([SR,WH,CF,TA,OI,RI,ME,FG,RM,TC])
CM_ZJ = ContractManager([IF,TF])

CM_TEST = ContractManager([IF,M])

CM_CU = ContractManager([CU])
CM_AL = ContractManager([AL])
CM_ZN = ContractManager([ZN])
CM_AG = ContractManager([AG])
CM_AU = ContractManager([AU])

CM_ALL_TEST = ContractManager([RB,CU,AL,ZN,AG,AU,BU,RU,M,A,C,Y,L,P,V,J,JM,I,JD,FB,BB,PP,SR,WH,CF,TA,OI,RI,ME,FG,RM,TC,IF,TF,XX,XH])


###########
# 计算因非交易时段不能下单而引起的延后交易
###########
#从非交易时间到交易时间的映射
def calc_delay_map(trade_ranges):
    empty_pairs = zip(trade_ranges,trade_ranges[1:])
    delay_map = {}
    for er in empty_pairs:
        mstart = er[0][1]
        mend = er[1][0]
        delay_map[mstart] = mend
        mnext = next_minute(mstart)
        if mnext < mend or mstart > mend:
            #冗余, 避免因为数据错误带来的误伤,如经常出现101500,113000,151500这样的错误ticks
            # or mstart > mend 是为了筛出最后一个交易分钟, 便于跨交易日计算
            delay_map[mnext] = mend
    return delay_map

#不支持跨交易日
FINANCIAL_DELAY_MAP = calc_delay_map([(910,914),(915,1129),(1300,1514)])
COMMODITY_DELAY_MAP = calc_delay_map([(855,859),(900,1014),(1030,1129),(1330,1459)])
#支持跨交易日
#FINANCIAL_DELAY_MAP2 = calc_delay_map([(910,914),(915,1129),(1300,1514),(929,0)])
#COMMODITY_DELAY_MAP2 = calc_delay_map([(855,859),(900,1014),(1030,1129),(1330,1459),(914,0)])

def calc_next_trade_minute(contract,cur_minute):
    """
        返回 下一交易时段的第一分钟
        跨日时返回下一交易日首个连续交易时段的第14分钟
        或者-1
    """
    try:
        if contract.ctype.exchange_name == "CFFEX":
            next = FINANCIAL_DELAY_MAP[cur_minute]
        else:
            next = COMMODITY_DELAY_MAP[cur_minute]
        return next
    except KeyError:        #不是因为非交易时间段引起的问题
        return -1   #出错


