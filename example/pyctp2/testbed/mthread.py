# -*- coding:utf-8 -*-

from threading import Thread,get_ident,Event
from queue import Queue
from time import time,sleep

from ..common.base import BaseObject

'''
    测试线程队列的消耗
'''

rlist = []

def worker():
    while True:
        item = q.get()
        #print(get_ident(),time() - item.begin)
        rlist.append(BaseObject(thread_id = get_ident(),twaste = time()-item.begin))
        q.task_done()

q = Queue()

num_worker_threads = 5
for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

def thru(item):
    print(get_ident(),time() - item.begin)

def rput(times = 100):
    rlist[:] = [] #不能直接rlist=[],那样相当于设置了一个局部变量
    for x in range(times):
        sleep(0.0005)
        q.put(BaseObject(begin=time()))
    sleep(0.5)
    print([x.twaste for x in rlist])
    return [x.twaste for x in rlist]



'''
    测试Event的作用
'''

evt = Event()

def driver():
    while True:
        evt.set()
        evt.clear()
        sleep(0.5)

def accepter():
    n = 1
    while True:
        evt.wait()
        print('drived : %s ' % (n,))
        n+=1
    
def evt_test():
    taccepter = Thread(target=accepter)
    tdriver = Thread(target=driver)
    taccepter.start()
    tdriver.start()
