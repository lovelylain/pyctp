# -*- coding:utf-8 -*-

import inspect
from ..common.utils import with_metaclass

def singleton(cls):
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            print("not find in singleton")
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class MyClass(object):
    a = 1
    def __init__(self, x=0):
        print("in myclass init,x=",x)
        self._x = x

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("in s_metaclass, new_instance")
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        inst = cls._instances[cls]
        inst.calc()
        return inst

@with_metaclass(Singleton)
class MyClass2:
    def __init__(self,x=0):
        print("in myclass init,x=",x)
        self._x = x

    def calc(self):
        print("in calc")

@with_metaclass(Singleton)
class BaseClass:
    pass

class MyClass3(BaseClass):
    def __init__(self,x=0):
        print("in myclass3 init,x=",x)
        self._x = x

    def calc(self):
        print("in calc")


def soft_hash1(v):
    try:
        return hash(v)
    except TypeError:
        return id(v)

def soft_hash(vs):
    idv =  tuple(soft_hash1(v) for v in vs)
    return hash(idv)

class ParameterizedCached(type):
    """
        参数化Cache. 以__init__参数为key来设定缓存
        接管类的__call__(即初始化)操作, 同参数的第一次__call__为初始化及计算,后续均为计算
        所以要求类的calc方法和__init__的签名一致


        这里的缓存其实还是有疏漏,对于 CROSS(X,Y,flag)的indicator,不同的调用方式很可能会导致无法命中:
            CROSS(x,y,True)
            CROSS(X=x,Y=y,flag=True)
            有可能正好顺序相同,也正好不同,这个无法预测
        唯一可以保证的是,因为对于同一个indicator在同一个位置的反复调用, 其参数方式是一致不变得

        为避免这个问题,要求以统一的方式来调用indicator

    """
    def __init__(cls, name, bases, dict):
        """
            验证calc和__init__签名的一致性
            因为在初始化之后, 以及后续调用中, 都必须以__init__的参数来调用calc
        """
        super(ParameterizedCached, cls).__init__(name, bases, dict)
        cls._instances = {}
        #print(inspect.getargspec(dict["__init__"]))
        #print(inspect.getargspec(dict["calc"]))
        init_spec = inspect.getargspec(dict["__init__"])
        calc_spec = inspect.getargspec(dict["calc"])
        assert init_spec == calc_spec,"calc签名必须和__init__一致!"

    def __call__(cls, *args, **kwargs):
        print(cls,args,kwargs)
        vargs = list(args)
        if kwargs:
            #vargs += [v for k,v in sorted(kwargs.items())]
            vargs += kwargs.values()     #对同样的keys,其顺序总是一致的,所以不需要特别排序
        print(vargs)
        ids = soft_hash(vargs)
        #print("cls:id",id(cls))
        #print("cls.instrance:id",id(cls._instances))
        print("ids:",ids)
        if ids not in cls._instances:
            print("new_instance,ids=",ids)
            cls._instances[ids] = super(ParameterizedCached, cls).__call__(*args, **kwargs)
        else:
            pass
            #print("find cached instance")
        inst = cls._instances[ids]
        inst.calc(*args,**kwargs)
        return inst


@with_metaclass(ParameterizedCached)
class Indicator(list):
    """
        基类
        因为User-defined classes默认就是hashable的,故不需要特别处理__hash__
    """
    def __init__(self):
        raise NotImplementedError("不能直接初始化抽象基类")

    def calc(self):
        raise NotImplementedError("不能直接调用抽象基类calc方法")


class Indicator1(Indicator):
    def __init__(self,x=0):
        print("in indicator1,x=",x)
        self._x = x

    def calc(self,x=0):
        print("in indicator1:calc,x=",x)

class Indicator2(Indicator):
    def __init__(self,z,y,x=0):
        print("in indicator2,x=",x)
        self._x = x
        self._y = y
        self._z = z

    def calc(self,z,y,x=0):
        print("in indicator2:calc,x=",x)

