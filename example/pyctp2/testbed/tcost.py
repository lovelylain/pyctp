# -*- coding:utf-8 -*-

import time
import threading
import queue
import collections

def tcost(xend=999999999):
    z=1
    t=time.time()
    while z < xend:
        z += 2
    print ("time cost: " + str(time.time() - t)    + "s " +str(z))

'''
    原则上来说,在TradeCommandQueue中, Queue与deque的选择对于pyctp而言无意义
    如果使用deque,必须在每个tick周期中去触发下evt(或者判断len(deque)是否大于0)
    而使用Queue,实际上的处理时间取决于Trade操作的次数, 每天实际上<1000次,算上查询也不会超过2000次

    即便对于Tick处理,也没有必要使用deque, 每次触发效率差别只在1us, 但是编程复杂度上升不少

'''
def tqueue(times,qsize=10):
    q = queue.Queue()
    tbegin = time.clock()
    for i in range(times):
        for j in range(qsize):
            q.put(i)
        for k in range(qsize):
            q.get()
    print('tqueue cost:%f' % (time.clock()-tbegin,))
 
def tdeque(times,qsize=10):
    q = collections.deque()
    lock = threading.Lock()
    tbegin = time.clock()
    for i in range(times):
        for j in range(qsize):
            lock.acquire()
            q.append(i)
            lock.release()
        for k in range(qsize):
            lock.acquire()
            q.pop()
            lock.release()
    print('tdeque cost:%f' % (time.clock()-tbegin,))

def tdeque2(times,qsize=10):
    q = collections.deque()
    e = threading.Event()
    tbegin = time.clock()
    for i in range(times):
        for j in range(qsize):
            e.set()
            q.append(i)
            e.wait()
            e.clear()
        for k in range(qsize):
            q.pop()
    print('tdeque cost:%f' % (time.clock()-tbegin,))

