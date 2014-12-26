#-*- coding:utf-8 -*-

import time
import os
import os.path

#数据和状态目录
INFO_PATH = 'info'
STATE_PATH = INFO_PATH + '/state'
DATA_PATH = INFO_PATH + '/data'
INTERNAL_PATH =  INFO_PATH + '/internal'
CONFIG_PATH = INFO_PATH + "/config"
TEST_PATH = INFO_PATH + '/test'
TEST_STATE_PATH = INFO_PATH + '/test/state'
TEST_DATA_PATH = INFO_PATH + '/test/data'
SIMULATOR_PATH = INFO_PATH + '/simulator'
SIMULATOR_STATE_PATH = INFO_PATH + '/simulator/state'
SIMULATOR_DATA_PATH = INFO_PATH + '/simulator/data'

DYNAMIC_PATH = INFO_PATH + "/dynamic"       #动态设定, 以及执行情况的记录
DYNAMIC_WAITING_PATH = DYNAMIC_PATH + "/waiting"       #等待处理的指令
DYNAMIC_FINISHED_PATH = DYNAMIC_PATH + "/finished"       #处理完成的指令

NIGHT_BEGIN = 1800  #夜盘判断时间, >= 1800

def check_path(fpath):
    if not os.path.isdir(fpath):
        os.makedirs(fpath)


#多空标志
LONG,SHORT,EMPTY = -1,1,0   #多仓出钱,淡仓收钱

def inverse_direction(direction):
    return -direction


#开平仓的标志
XOPEN,XCLOSE,XCLOSE_TODAY,XUNKNOWN = -1,1,2,0 #开仓,平仓

MAX_PRICE,MIN_PRICE = 99999999.0,0.0
MAX_VALUE = MAX_PRICE
MAX_INT = 99999999

#XBASE = 100 #用于一般化的除数基数

EMPTY_LIST = [] #空列表,用于任何不变的空列表

EPSL = 0.00000000001    #用于数字打印时的舍入


def Nope(*args,**kwargs):
    '''
        空函数
    '''
    pass

class NOPE_Queue(object):
    '''
        Nope队列
    '''
    def put(self,item):
        pass

    def get(self,):
        return None

    def qsize(self,):
        return 0

nope_queue = NOPE_Queue()

class NOPE_Event(object):
    '''
        空Event
    '''
    def set(self):
        pass

    def clear(self):
        pass


nope_event = NOPE_Event()

class BaseObject(object):
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

    #has_attr/get_attr/set_attr没有必要, 系统函数hasattr/getattr/setattr已实现这些功能
    def has_attr(self,attr_name):
        return attr_name in self.__dict__

    def get_attr(self,attr_name):
        return self.__dict__[attr_name]

    def set_attr(self,attr_name,value):
        self.__dict__[attr_name] = value

    def __repr__(self):
        return str(self.__class__)

class CN_TRADE_SECTION:
    DAY = BaseObject(begin=845,end=1520)
    NIGHT = BaseObject(begin=2045,end=300)


#DAY_FINALIZE, 用于日结. 对日结TICK的要求, 每日只能出现一个日结TICK
#DAY_FINALIZE_TICK = BaseObject(instrument='DAY_FINALIZE',date=20991231,bid_price=0,bid_volume=0,ask_price=0,ask_volume=0,
#                      min1 =0,sec=0,msec=0,holding=0,dvolume=0,price=0,high=0,low=0
#                    )



class TICK(object):
    __slots__ = ['instrument','date','sdate','tdate','min1','sec','msec','time','holding','dvolume','damount','price','high','low','bid_price','bid_volume','ask_price','ask_volume','create_time']
    #date为自然日,tdate为交易日.  在夜盘时,两者不同

    def __init__(self,instrument,date):
        self.instrument = instrument
        self.date = date
        self.time = 0
        self.create_time = time.time()
        #self.common_reset() #不必,因为会被逐一赋值

    def common_reset(self):
        self.min1 = self.sec = self.msec = self.time = 0 #
        self.holding = self.dvolume = self.damount = 0 #
        self.price = self.high = self.low = 0 #
        self.bid_price = self.bid_volume = self.ask_price = self.ask_volume = 0
        self.tdate = self.date

    @property
    def drange(self):
        return self.high - self.low

    def is_valid(self):
        """
            确认tick是否合法
            目前使用的ctp接口在7:00-7:10,以及15:20-16:00之间有非法数据出现
        """
        if (self.min1 > CN_TRADE_SECTION.DAY.begin and self.min1 < CN_TRADE_SECTION.DAY.end) or self.min1 >= CN_TRADE_SECTION.NIGHT.begin or self.min1 <= CN_TRADE_SECTION.NIGHT.end:
            return True
        return False


    def mydict(self):
        return dict([(n,self.__getattribute__(n)) for n in self.__slots__])



FINALIZE_DAY = 20991232

#DAY_FINALIZE, 用于日结. 对日结TICK的要求, 每日只能出现一个日结TICK.  该TICK除instrument和date外其余各字段均为0
DAY_FINALIZE_TICK = TICK(instrument='DAY_FINALIZE',date=FINALIZE_DAY)
DAY_FINALIZE_TICK.common_reset()    #该TICK除instrument和date外其余各字段均须为0, 尤其是min1必须为0, 以便次日比较

ZERO_TICK = TICK(instrument='ZERO',date=0)
ZERO_TICK.common_reset()

TERMINAL_TICK = TICK(instrument='TERMINAL',date=FINALIZE_DAY)
TERMINAL_TICK.common_reset()


class TMinute(object):
    __slots__ = ["sopen","sclose","shigh","slow","stime","sdate","stdate","svolume","samount","sholding"]

    def __init__(self,sopen=0,sclose=0,shigh=0,slow=0,svolume=0,samount=0,sholding=0,stime=0,sdate=0,stdate=0):
        self.sopen = sopen
        self.sclose = sclose
        self.shigh = shigh
        self.slow = slow
        self.svolume = svolume
        self.samount = samount
        self.sholding = sholding
        self.stime = stime
        self.sdate = sdate
        self.stdate = stdate


def create_day_finalize_tick(contract_name):        #创建与合约名一致的日结tick
    dft = TICK(instrument=contract_name,date=FINALIZE_DAY)
    dft.common_reset()
    return dft


