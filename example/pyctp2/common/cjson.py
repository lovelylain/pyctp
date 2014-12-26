# -*- coding:utf-8 -*-

from json import dumps,loads,dump,load
from importlib import import_module

from .base import EPSL,EMPTY_LIST
from .utils import fcustom

def parse_float(sf):
    return round(float(sf) + EPSL,4)

def object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    #print(obj.__class__.__name__)
    d['__module__'] = obj.__module__
    if obj.__class__.__name__ == "function":
        d['func_name'] = obj.__name__
    if 'to_dict' in obj.__class__.__dict__:# 自定义转化,为普通方法
        d.update(obj.to_dict())
    else:
        d.update(obj.__dict__)
    return d
 
def dict2object(d):
    #convert dict to object
    if'__class__' in d:
        #print(d)
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = import_module(module_name)
        if class_name == "function":
            func_name = d.pop('func_name')
            inst = getattr(module,func_name)
        else:
            clazz = getattr(module,class_name)
            if 'from_dict' in clazz.__dict__:   #允许自定义创建. 为静态方法
                inst = clazz.from_dict(d)
            else:   #适用于大部分常规自定义类
                inst = clazz.__new__(clazz)
                inst.__dict__.update(d)
    else:
        inst = d
    return inst

dumps = fcustom(dumps,default = object2dict,sort_keys=True,indent=4, separators=(',', ': '))
loads = fcustom(loads,object_hook = dict2object,parse_float=parse_float)

dump = fcustom(dump,default = object2dict,sort_keys=True,indent=4, separators=(',', ': '))
load = fcustom(load,object_hook = dict2object,parse_float=parse_float)


class json_serializable(object):
    '''
        目前没用
    '''
    def __init__(self,excluded=EMPTY_LIST):
        self._excluded = excluded

    def to_dict(self):
        rev = dict(self.__dict__)
        for e in self._excluded:
            del rev[e]
        del rev['_excluded']
        return rev
