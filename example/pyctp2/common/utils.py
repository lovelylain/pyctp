#-*- coding:utf-8 -*-

import functools
import datetime
import time
import logging

from inspect import getargspec

from types import GetSetDescriptorType, MemberDescriptorType
def with_metaclass(metaclass):
    """Return a decorator to create a new class with metaclass."""
    def decorator(cls):
        d = dict((k,v) for k,v in cls.__dict__.items() if
            not isinstance(v, GetSetDescriptorType) and
            not isinstance(v, MemberDescriptorType))
        return metaclass(cls.__name__, cls.__bases__, d)
    return decorator

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

def fcustom(func,**kwargs):
    ''' 根据kwargs设置func的偏函数,并将此偏函数的名字设定为源函数名+所固定的关键字参数名
    '''
    pf = functools.partial(func,**kwargs)
    #pf.name = pf.func.func_name
    pf.paras = ','.join(['%s=%s' % item for item in pf.keywords.items()])
    pf.__name__ = '%s:%s' % (func.__name__,pf.paras)
    return pf

def func_name(func):    #取到真实函数名. 可能只适用于python2.x
    if 'name' in func.__dict__:         #自主设定
        return func.name
    if '__name__' in func.__dict__:
        return func.__name__

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

def bound_method_name(cmethod): #取到由class实例化的对象的方法名
    if '__name__' in cmethod.__dict__:
        return cmethod.name
    try:
        ctxt = str(cmethod)
        return ctxt.split(sep=' ')[2].split('.')[1]
    except:
        return "******************it is not a bound method********************"

def now2next(fhour,fminute,fsecond):
    ''' 
        到下一个完结点的秒数
        完结点用fhour,fminute,fsecond表示
    '''
    cur = datetime.datetime.now()
    print(cur,fhour,fminute,fsecond)
    if cur.hour*10000 + cur.minute*100 + cur.second >= fhour*10000 + fminute*100 + fsecond:
        #需要到第二天
        fhour += 24
    return (fhour - cur.hour)*3600 + (fminute - cur.minute) * 60 + fsecond - cur.second

def today():    #返回YYYYMMDD表示的整型日期
    td = datetime.datetime.today()
    return td.year * 10000 + td.month * 100 + td.day

def second2time(second):
    """
        将 YYYYMMDDhhmmss格式的second转化为与time.time()相一致的EPOCH起的秒数
    """
    year = second // 10000000000
    month = second % 10000000000 // 100000000
    day = second % 100000000 // 1000000
    hour = second % 1000000 // 10000
    minute = second % 10000 // 100
    sec = second % 100
    return time.mktime((year,month,day,hour,minute,sec,0,0,0))

def delta_day(cur_day,delta):
    year = cur_day // 10000
    month = cur_day % 10000 // 100
    day = cur_day % 100
    cday = datetime.date(year,month,day)
    delta = datetime.timedelta(days=delta)
    dday = cday + delta
    return dday.year * 10000 + dday.month * 100 + dday.day

pre_day = fcustom(delta_day,delta=-1)
next_day = fcustom(delta_day,delta=1)

def next_trading_day(cur_day=0):
    #返回剔除周6和日后的next_day
    if cur_day == 0:
        cur_day = today()
    nd = next_day(cur_day)
    wd = weekday(nd)
    #print(wd)
    while(wd==6 or wd==7):
        nd = next_day(nd)
        wd = weekday(nd)
        #print(nd)
    return nd

def weekday(iday):
    #返回转化为1-7的weekday
    #http://blog.csdn.net/hawkfeifei/article/details/4337181
    year = iday//10000
    month = iday//100%100
    day = iday%100
    if month <= 2:
        month += 12
        year -= 1
    return (day+2*month+3*(month+1)//5+year+year//4-year//100+year//400)%7 + 1  #转化为1-7


def next_minute(cur_minute):
    return cur_minute+1 if cur_minute%100 !=59 else (cur_minute//100+1)*100 #分钟进位

class ArgsCached(type): #TODO:TEST, 用在ContractInfo的缓存上
    """
        metaclass
        根据类的__init__方法中name参数来判断是否需要缓存
        实体类必须在类层次上定义 _cached_args, 来指定用于cache的属性,这些属性必须都是str类型
    """
    _args2obj = {}  #通用的缓存,通过cls找到这里

    def __call__(cls, *args, **kwargs):
        pairs = cls._match_init_args(cls,*args,**kwargs)
        #print("pairs=",pairs)
        skey = '-'.join([pairs[n] for n in cls._cached_args])
        #print(cls._name2obj)

        if skey not in cls._args2obj:
            #print("new_instance,name=",name)
            cls._args2obj[skey] = super(ArgsCached, cls).__call__(*args, **kwargs)
            #print(name,cls._name2obj)
        inst = cls._args2obj[skey]
        return inst

    def _match_init_args(cls,*args,**kwargs):
        fspec = getargspec(cls.__init__)
        if fspec.defaults:
            pairs = dict(zip(fspec.args[-len(fspec.defaults):],fspec.defaults))
        else:
            pairs = {}
        #print(spec_args)
        #pairs = dict(zip(fspec.args,args))
        #print(pairs,default_args,fspec.)
        #print(pairs)
        pairs.update(zip(fspec.args,args))
        #print("set args",pairs,"spec_args:",spec_args,"args:",args)
        #print("kwargs:",kwargs)
        pairs.update(kwargs)
        #print(pairs)
        return pairs

    @staticmethod
    def clear():
        #ArgsCached._args2obj = {}
        ArgsCached._args2obj.clear()

class TList(list):
    """
        仅用于Ticks
        以在截断时通知调用者知晓被截断数
    """
    def __init__(self,*args,**kwargs):
        super(TList, self).__init__(*args,**kwargs)
        self._receivers = {}

    def remove_all(self):
        truncated_size = len(self)
        self[:] = []
        self.notify(truncated_size)
        logging.info("TList remove_all:%d,size=%d" % (id(self),truncated_size))
        #print("TList remove_all:%d,removed=%d,remains=%s" % (id(self),truncated_size,len(self)))

    def remove_head(self,size):
        if size >= len(self):
            size = len(self)
        self[:size] = []
        self.notify(size)
        logging.info("TList remove_head:%d,size=%d" % (id(self),size))
        #print("TList remove_head:%d,size=%d" % (id(self),size))

    def register(self,receiver):
        self._receivers[id(receiver)] = receiver

    def unregister(self,receiver):
        if id(receiver) in self._receivers:
            del self._receivers[id(receiver)]

    def notify(self,truncated_size):
        if truncated_size > 0:
            for receiver in self._receivers.values():
                receiver.notify_truncated(truncated_size)


class Updateable(object):
    """
        可更新的类
    """
    def kv_update(self,kv_pairs):
        for key,v in kv_pairs:
            try:
                getattr(self,key)
                setattr(self,key,v)
            except:
                logging.error("update %s.%s=%s error!,%s不存在" % (self.__class__.__name__,key,v,key))

