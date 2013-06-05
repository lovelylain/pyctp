#-*- coding:utf-8 -*-

IDATE,ITIME,IOPEN,ICLOSE,IHIGH,ILOW,IVOL,IHOLDING,IORDER = 0,1,2,3,4,5,6,7,8

#多空标志
LONG,SHORT,EMPTY = -1,1,0   #多仓出钱,淡仓收钱
#开平仓的标志
XOPEN,XCLOSE = -1,1 #开仓,平仓

XBASE = 100 #用于一般化的除数基数

import sys
import functools

import logging
import lib.decorator as decorator
from inspect import (
            getargspec,
        )


MY_FORMAT = '%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s'
CONSOLE_FORMAT = '**%(message)s'

#设定日志
def config_logging(filename,level=logging.DEBUG,format=MY_FORMAT,to_console=True,console_level=logging.INFO):
    logging.basicConfig(filename=filename,level=level,format=format)
    if to_console:
        add_log2console(console_level)

#将指定级别的日志同时输出到控制台
def add_log2console(level = logging.INFO):
    console = logging.StreamHandler()
    console.setLevel(level)
    # set a format which is simpler for console use
    #formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    #formatter = logging.Formatter('%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    formatter = logging.Formatter(CONSOLE_FORMAT)
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
 
def is_if(instrument):#判断是否是IF
    return instrument[:2].upper() == 'IF'

def date2week(iday):
    #http://blog.csdn.net/hawkfeifei/article/details/4337181
    year = iday/10000
    month = iday/100%100
    day = iday%100
    if month <= 2:
        month += 12
        year -= 1
    return (day+2*month+3*(month+1)/5+year+year/4-year/100+year/400)%7 + 1  #转化为1-7

def inverse_direction(direction):
    return LONG if direction == SHORT else SHORT

def fcustom(func,**kwargs):
    ''' 根据kwargs设置func的偏函数,并将此偏函数的名字设定为源函数名+所固定的关键字参数名
    '''
    pf = functools.partial(func,**kwargs)
    #pf.name = pf.func.func_name
    pf.paras = ','.join(['%s=%s' % item for item in pf.keywords.items()])
    pf.__name__ = '%s:%s' % (func.__name__,pf.paras)
    return pf

def func_name(func):    #取到真实函数名. 可能只适用于python2.x
    if 'name' in func.__dict__:
        return func.name
    cfunc = func
    while(isinstance(cfunc,functools.partial)):
        cfunc = cfunc.func
    return str(cfunc)[10:-15]

def type_name(cobj): #取到由class实例化的对象的type名
    clazz_obj = cobj
    while(isinstance(clazz_obj,functools.partial)):
        clazz_obj = clazz_obj.func
    aname = str(type(clazz_obj))[8:-2]
    return aname.split('.')[-1]

def module_name(cobj): #取到由class实例化的对象所在的模块名
    clazz_obj = cobj
    while(isinstance(clazz_obj,functools.partial)):
        clazz_obj = clazz_obj.func
    aname = str(type(clazz_obj))[8:-2]
    return aname.split('.')[0]

def class_name(cobj): #取到由class实例化的对象的模块名和type名
    clazz_obj = cobj
    while(isinstance(clazz_obj,functools.partial)):
        clazz_obj = clazz_obj.func
    aname = str(type(clazz_obj))[8:-2]
    return tuple(aname.split('.'))

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
        return 'BaseObject'


class CommonObject(BaseObject):
    def __init__(self,id,**kwargs):
        BaseObject.__init__(self,**kwargs)
        self.id = id

    def __repr__(self):
        return 'CommonObject'


LINELENGTH = 60
def linelog(msg):   #在同一行覆盖显示日志输出
    sys.stdout.write(unicode((u'\r%s%s' % (msg,' ' * (LINELENGTH - len(msg)))))) #.encode('gbk'))  #适应输出编码为gbk


##这段代码来自于回测平台。根据lvzhl的建议演化而来,主要用于方便统一计算IF和商品的3/5/10/15/30/...等周期数据
##对于1130和最后一个时点的计算与回测平台不同, 为兼容ticks处理
def calc_t2order(begin,end,(mid1,mid2)=(1130,1300)):
    ##为便于计算30分钟线，商品的节休息段仍然计算序号. 这样，1000->1029算一个30分钟段
    t2order = {}
    nbegin = begin / 100 * 60 + begin % 100
    for i in range(begin,mid1):
        if i%100 > 59:
            continue
        it = i/100 * 60 + i%100
        t2order[i] = it - nbegin
    
    it = mid1/100 * 60 + mid1%100
    t2order[mid1] = it - nbegin - 1     #中间截止时间是不存在的,比如11:30

    for i in range(mid2,end):
        it = i/100 * 60 + i%100
        if i%100 > 59:
            continue
        t2order[i] = it - nbegin - 90
        #t2order[i] = t2order[i] = it - nbegin - ((mid2/100-mid1/100)*60 +(mid2%100 - mid1%100)) 

    it = end/100 * 60 + end%100
    t2order[end] = it - nbegin - 90 - 1 #最后时间是不存在,比如15:15/15:00
    return t2order

#IF: time-->order
t2order_if = calc_t2order(914,1515)

#商品: time-->order. 中间有休息
t2order_com = calc_t2order(859,1500,(1130,1330))    #未刻意去处理1015-1029时间段

#模拟
t2order_mock = calc_t2order(1900,2330,(2115,2115))
t2order_mock2 = calc_t2order(1500,1930,(1715,1715))


#快速键值
'''
    因为这里使用了id函数，所以必须妥善处理临时的输入序列参数
        此时，某个序列对象被回收，然后会重新分配给另一个序列对象，
        而这个对象又用于同一个被indicator修饰的函数,最终导致紊乱
'''
def quick_id(v):
    '''
        对基础数据类型，返回(v,None)
        对对象类型，返回(id(v),v)
    '''
    t = type(v)
    if t == list: #用到最多
        return id(v),v
    elif t  == int or t == float: #次多
        return v,None
    elif t in [long,bool,complex,str,unicode,xrange]:
        return v,None
    #其余都为对象，用id标识
    return id(v),v

def quick_ids(vs):
    idv =  [quick_id(v) for v in vs]
    return tuple((i for i,v in idv)),[v for i,v in idv if v!=None]


def quick_objs(vs):
    return [ v for v in vs if is_obj(v) ]

import gc
class ObjHolder(object):
    '''
        用于保持对象引用，避免释放、回收后被重新分配       
    '''
    def __init__(self):
        self.holder = {}

    def register_obj(self,obj):
        if id(obj) not in self.holder:
            self.holder[id(obj)] = obj
        assert self.holder[id(obj)] is obj

    def register_objs(self,objs):
        for obj in objs:
            self.register_obj(obj)

    def reset(self):
        self.holder.clear()
        gc.collect()

#用于持有住各indicator的输入对象，避免临时对象被回收后重新分配给用于同一indicator的序列对象，从而导致隐秘错误
GLOBAL_HOLDER = ObjHolder()

def source_len(vs):
    '''
        将根据source的长度判断是否需要更新
    '''
    for v in vs:
        if type(v) == list:
            return len(v)
    return -1


def _icache(func, *args, **kw):
    '''
        icache装饰器
        根据参数中的第一个列表的长度判断是否需要重新计算
        单独使用仅用于超级简单的情况
        可以与@indicator一起使用，但提供的增益有限(因指标内部必须处理源序列增加的事宜),只减少了几个指标内部的判断语句
        ####通常，任何情况下icache都是不必要的. icache引入的开销比不上它要节省的开销, 而且引入了额外的复杂性，更不宜于理解####

        vojb用于固定住输入中用id标识的对象，防止在计算过程中被释放后重新分配给其它对象
    '''
    key = args + kw.iteritems() if kw else args
    vkey,vobjs = quick_ids(key)
    cache = func.cache # attributed added by memoize
    slen = source_len(key)
    if vkey not in cache or cache[vkey].slen < slen:
        result = func(*args, **kw)
        cache[vkey] = BaseObject(result = result,slen = slen,vobjs = vobjs,initialized=False)
    elif slen > cache[vkey].slen:#须重新计算
        cache[vkey].result = func(*args, **kw)
        cache[vkey].slen = slen
    return cache[vkey].result

def icache(f):
    f.cache = {}
    return decorator.decorator(_icache,f)

def _indicator(func, *args, **kw):
    '''
        indicator装饰器,用于常规indicator的实现
        向原函数提供暂存对象, 要求原函数的最后一个位置参数必须是_ts
        vojb用于固定住输入中用id标识的对象，防止在计算过程中被释放后重新分配给其它对象
    '''
    #print 'in _indicator'
    vargs = list(args)
    key = vargs + kw.values() if kw else vargs
    #print vargs
    vkey,vobjs = quick_ids(key)    
    storage = func.storage
    slen = source_len(key)
    if vkey not in storage:
        #storage[vkey] = BaseObject()
        storage[vkey] = BaseObject(initialized = False)
        GLOBAL_HOLDER.register_objs(vobjs)
    #print vargs
    #指标调用者直接指定_ts(用位置或命名参数)时，仍然将其替换为暂存者. 要求调用者不得指定这个参数，否则会导致莫名奇妙问题
    #vargs[-1] = storage[vkey]
    if vargs[-1] == None:  #最后一个位置参数为None,就认为是_ts；这里会略为出现紊乱，如出现刻意为None的其它参数
        vargs[func.tpos] = storage[vkey]    #允许_ts不在最后位置，以支持可变参数*args
    else:   #后面有可变位置参数, 此时,_ts被可变参数填充, 实际总长度比应当总长度少1，应将_ts插入到该位置
        vargs = vargs[:func.tpos] + [storage[vkey]] + vargs[func.tpos:]
        #print 'vargs=',vargs
    return func(*vargs,**kw)

def indicator(f):
    f.storage = {}
    aspecs = getargspec(f).args
    f.tpos = aspecs.index('_ts')
    assert f.tpos == len(aspecs)-1,'position of _ts is invalid'  #_ts必须是最后一个固定位置参数
    return decorator.decorator(_indicator,f)

##############
# 一个举例
#     可用的ma  
##############
#@icache
@indicator
def MA_EXAMPLE(src,mlen,_ts=None):
    '''
        所有指标都必须设定_ts这个参数,且默认值为None,装饰器将传入暂存对象
        #_ts必须是最后一个固定位置参数

        返回值:
            移动平均序列
            当序列中元素个数<mlen时，结果序列为到该元素为止的所有元素值的平均
    '''
    assert mlen>0,u'mlen should > 0'
    if not _ts.initialized:
        _ts.initialized = True
        _ts.sa = [0]*mlen   #哨兵
        _ts.ma = []

    slen = len(_ts.ma)
    ss = _ts.sa[-1]
    for i in range(slen,len(src)):
        ss += src[i]
        _ts.sa.append(ss)
        #print ss,_ts.sa[i-mlen]
        #当累计个数<nlen时，求其平均值，而不是累计值/mlen
        rlen = mlen if mlen < i+1 else i+1
        _ts.ma.append((ss-_ts.sa[-rlen-1]+rlen/2)/rlen) 
    #print _ts.sa
    return _ts.ma


