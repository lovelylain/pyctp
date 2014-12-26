# -*- coding:utf-8 -*-

import datetime

from ..common import controller as ctl



def pstate():
    cur = datetime.datetime.now()
    print(str(cur))

def mytest():
    tt = ctl.TimeTrigger(225700,pstate,10)
