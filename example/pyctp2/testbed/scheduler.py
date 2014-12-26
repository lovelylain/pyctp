# -*- coding:utf-8 -*-

import sched
import time
import threading

def ev(sobj):
    print("Current Time:", time.strftime("%y-%m-%d %H:%M:%S"))
    sobj.enter(3,1,ev,argument=(sobj,))


def tsched():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(3,1,ev,argument=(s,))
    s.run()
    print('xxxxxxxxxxxxx')


def thread_sched():
    t=threading.Thread(target=tsched)
    t.daemon = True
    t.start()
