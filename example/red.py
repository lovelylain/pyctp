# -*- coding:utf-8 -*-

'''
    redirect工具
    因为在pyctp2中使用了相对导入,故pyctp2只能作为包来使用
    不能直接执行其下的含__name__=='__main__'的文件
    故此用此工具
    需要在pyctp2的父目录下执行本文件
'''

import logging
import sys
from importlib import import_module

import time

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write('执行方式为: python red.py 模块名 函数名 位置参数')
        exit(1)
    module_name = sys.argv[1]
    func_name = sys.argv[2]
    func_param = sys.argv[3:]
    #print(module_name,func_name)
    module = import_module(module_name)
    if func_name not in module.__dict__:
        sys.stderr.write('function %s 不在模块 %s 中' % (func_name,module_name))
        exit(2)
    func = module.__dict__[func_name]
    try:
        rev = func(*func_param)
        while(True):
            #timer_info = 'awake for a while......,time trigger.id=%s,is_alive=%s,finished:%s' % (rev[2].timer.ident,rev[2].timer.is_alive(),rev[2].timer.finished.is_set())
            #print(timer_info)
            #logging.info(timer_info)
            #print('sleep for 60 seconds')
            time.sleep(60)
    except Exception as e:
        sys.stderr.write(str(e))

    
