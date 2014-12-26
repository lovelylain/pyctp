# -*- coding:utf-8 -*-
'''
 同步排序队列的测试:
        实际上, PriorityQueue就是用heapq实现的阻塞式队列
'''

import time
import bisect
from heapq import *
import threading
import queue
from collections import deque

"""
    在满足功能要求的情况下, heapq的方式最快也最简洁效率最稳定
    均为 100次循环,每次循环先插入1000个,然后弹出所有 #这个不是使用环境
        在正式使用环境下,因为排序方式不需要全部检查,所以开销会比测试的要小
    heapq: 1.4s
    priorityQueue: 5.5s
    list,每次插入后重新排队,且未lock: 75s
        线程同步: 75s #基本一样?,说明时间主要耗在sort上,加锁与否影响很小
    bisect insort: 1.9s (未线程同步)
    bisect 手工连接: 4.4s(未线程同步)
    bisect insort: 2.4s (线程同步)

    附:
    duque: 0.5s (未做排序)
    list: 0.58s (未做lock)
    list: 0.95s (做同步)
    说明同步开销在0.5s

    当测试为10000次,每次循环插入30个时:
    heapq: 3.7s
    priorityQueue: 17s
    list,每次插入后重新排队,且未lock: 8s    #说明数量少时list sort效率很高
        10.21
    bisect insort: 3.9s (未线程同步)
    bisect 手工连接: 4.96s(未线程同步)
    bisect insort: 5.22s (线程同步)

    附未做排序的方法:
    duque: 1.56s (,线程安全)
    list: 1.87s (未做lock)
    list: 3.34s (做同步)
    

    当测试为20000次,每次循环插入5个时:
    heapq: 1.16s
    priorityQueue: 6.5s
    list,每次插入后重新排队,且未lock: 1.14s    #说明数量少时list sort效率很高
        #同步 1.95s
    bisect insort: 1.0s (未线程同步)
    bisect 手工连接: 1.37s(未线程同步)
    bisect insort: 1.35s (线程同步)

    附未做排序的方法:
    duque: 0.59s (,线程安全)
    list: 0.67s (未做lock)
    list: 1.12s (做同步)


"""

QSIZE = 6

class Command(object):
    def __init__(self,etime):
        self._exec_time = etime

    def exec(self,itime):
        if itime > self._exec_time:
            print('error!')
 
    def key(self):
        return self._exec_time

    def __lt__(self,other):
        return self._exec_time < other.exec_time

    def __gt__(self,other):
        return self._exec_time > other.exec_time

def qcost(times=100000):
    tbegin = time.time()
    for i in range(times):
        q = deque()
        for it in range(QSIZE):
            q.append(Command(it))
        while len(q) > 0:
            it = q.pop()
            it.exec(0)
    print('qcost:%f' % (time.time()-tbegin))
lock = threading.Lock()

def lcost(times=100000):
    tbegin = time.time()
    for i in range(times):
        q = []
        for it in range(QSIZE):
            q.append(Command(it))
        while len(q) > 0:
            it = q.pop()
            it.exec(0)
    print('lcost:%f' % (time.time()-tbegin))

def lcost0(times=100000):
    tbegin = time.time()
    for i in range(times):
        q = []
        for it in range(QSIZE):
            lock.acquire()  #比with开销要少总的10%
            q.append(Command(it))
            lock.release() 
        while len(q) > 0:
            lock.acquire()  #比with开销要少总的10%
            it = q.pop()
            lock.release() 
            it.exec(0)
    print('lcost:%f' % (time.time()-tbegin))


def hcost(times=100000):
    tbegin = time.time()
    for i in range(times):
        h = []
        for it in range(QSIZE):
            lock.acquire()  #比with开销要少总的10%
            heappush(h,(it,Command(it)))
            #heappush(h,Command(it))
            lock.release() 
        while len(h) > 0:
            lock.acquire()
            it = heappop(h)
            lock.release()
            it[1].exec(0)
    print('hcost:%f' % (time.time()-tbegin))

def hcost1(times=100000):
    '''
        比host0慢20%以上
    '''
    tbegin = time.time()
    for i in range(times):
        h = []
        for it in range(QSIZE):
            lock.acquire()  #比with开销要少总的10%
            heappush(h,Command(it))
            lock.release() 
        while len(h) > 0:
            lock.acquire()
            it = heappop(h)
            lock.release()
            it.exec(0)
    print('hcost:%f' % (time.time()-tbegin))


def pcost(times=100000):
    tbegin = time.time()
    for i in range(times):
        p = queue.PriorityQueue()
        for it in range(QSIZE):
            p.put(Command(it))
        while p.qsize() > 0:
            it = p.get()
            it.exec(0)
    print('pcost:%f' % (time.time()-tbegin))


def scost(times=100000):
    tbegin = time.time()
    for i in range(times):
        q = []
        for it in range(QSIZE):
            q.append(Command(it))
            q.sort()
        while len(q) > 0:
            it = q.pop()
            it.exec(0)
    print('scost:%f' % (time.time()-tbegin))

def scost0(times=100000):
    tbegin = time.time()
    for i in range(times):
        q = []
        for it in range(QSIZE):
            lock.acquire()  #比with开销要少总的10%
            q.append(Command(it))
            q.sort()
            lock.release()
        while len(q) > 0:
            lock.acquire()  #比with开销要少总的10%
            it = q.pop()
            lock.release()
            it.exec(0)
    print('scost:%f' % (time.time()-tbegin))

def bcost(times=100000):
    tbegin = time.time()
    for i in range(times):
        q = []
        for it in range(QSIZE):
            #q.append(Command(it))
            bisect.insort_left(q,Command(it))
        while len(q) > 000:
            it = q.pop()
            it.exec(0)
    print('bcost:%f' % (time.time()-tbegin))

def bcost0(times=100000):
    tbegin = time.time()
    for i in range(times):
        q = []
        for it in range(QSIZE):
            lock.acquire()
            bisect.insort_left(q,Command(it))
            lock.release()
        while len(q) > 000:
            lock.acquire()
            it = q.pop()
            lock.release()
            it.exec(0)
    print('bcost:%f' % (time.time()-tbegin))


def bcost2(times=100000):
    tbegin = time.time()
    for i in range(times):
        q = []
        for it in range(QSIZE):
            #q.append(Command(it))
            cit = Command(it)
            i = bisect.bisect_left(q,cit)
            q = q[:i] + [cit] + q[i:]
        while len(q) > 000:
            it = q.pop()
            it.exec(0)
    print('bcost:%f' % (time.time()-tbegin))

