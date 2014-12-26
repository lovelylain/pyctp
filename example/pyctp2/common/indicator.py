# -*- coding: utf-8 -*-
"""
    通过元类实现的Indicator
"""

import inspect
from .utils import with_metaclass

#soft_hash
def soft_hash1(v):
    try:
        return hash(v)
    except TypeError:
        return id(v)
        #在测试时,这个方法有时候会引起很诡异的问题,因为同一片地址在不同测试之间不停的被重复使用,
        #       又碰巧如果正好是同一个指标在不同测试方法中被测试多次
        #       而且又正好不是每次都重现! 会连续重现,但又和系统内存情况有关
        #但在实际使用中不会出现这个问题. 因为参数在整个过程中被长期持有,不会被释放

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
        cls._has_init_func = False
        if "__init__" in dict:
            init_spec = inspect.getargspec(dict["__init__"])
            calc_spec = inspect.getargspec(dict["calc"])
            assert init_spec == calc_spec,"calc签名必须和__init__一致!"
            cls._has_init_func = True

    def __call__(cls, *args, **kwargs):
        #print(cls,args,kwargs)
        vargs = list(args)
        if kwargs:
            #vargs += [v for k,v in sorted(kwargs.items())]
            vargs += kwargs.values()     #对同样的keys,其顺序总是一致的,所以不需要特别排序
        #print(vargs)
        ids = soft_hash(vargs)
        #print("cls:id",id(cls))
        #print("cls.instrance:id",id(cls._instances))
        #print("ids:",ids)
        if ids not in cls._instances:
            #print("new_instance,ids=",ids)
            if cls._has_init_func:
                cls._instances[ids] = super(ParameterizedCached, cls).__call__(*args, **kwargs)
            else:
                cls._instances[ids] = super(ParameterizedCached, cls).__call__()
        else:
            pass
            #print("find cached instance")
        inst = cls._instances[ids]
        rev = inst.calc(*args,**kwargs)
        #return inst
        return rev  #不是返回实例,而是返回calc的返回值, 一般情况下两者相同, 特殊情况下更加符合直观.

@with_metaclass(ParameterizedCached)
class Indicator(list):
    """
        基类
        因为User-defined classes默认就是hashable的,故不需要特别处理__hash__
    """
    def __init__(self):
        pass    #子类未定义时,会到这里
        #raise NotImplementedError("不能直接初始化抽象基类")

    def calc(self):
        raise NotImplementedError("不能直接调用抽象基类calc方法")


