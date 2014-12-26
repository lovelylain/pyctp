# -*- coding:utf-8 -*-

'''
测试int和float的差异
'''

import time
from random import randint

def iadd(times,ilist):
    s = 0
    for i in range(times):
        for j in ilist:
            s += (j-1)
    return s

def imul(times,ilist):
    s = 0
    for i in range(times):
        for j in ilist:
            s += (j * j + (j+1)*j)
            #s += (j-1)*j+(j-2)*(j+1)
            #s += (j-1)*(j+1)
    return s

def iamd(times,ilist):
    s = 0
    for i in range(times):
        for j in ilist:
            if j>1:
                #s += (j*j//(j-1)+j*j//(j-2)+j*j//(j-3)+j*j//(j-4))
                #s += (j*j+(j-1)*(j-1)+(j-2)*(j-2)+(j-3)*(j-3)+(j-4)*(j-4))#//(j-1)
                s += j*(j+5) // (j-1)
    return s
 
def famd(times,ilist):
    s = 0.0
    for i in range(times):
        for j in ilist:
            if j>1:
                #s += (j*j+(j-1)*(j-1)+(j-2)*(j-2)+(j-3)*(j-3)+(j-4)*(j-4))#/(j-1)
                s += j*(j+5.0) / (j-1.0)
    return s


def test():
    times = 100
    ilist = [randint(0,10000) for i in range(10000)]
    flist = [i*1.0 for i in ilist]
    b = time.time()
    s=iadd(times,ilist)
    print('iadd,1000times:%f,result=%f' % (time.time()-b,s),s)
    b = time.time()
    s=iadd(times,flist)
    print('fadd,1000times:%f,result=%f' % (time.time()-b,s),s)
    b = time.time()
    s=imul(times,ilist)
    print('imul,1000times:%f,result=%f' % (time.time()-b,s),s)
    b = time.time()
    s=imul(times,flist)
    print('fmul,1000times:%f,result=%f' % (time.time()-b,s),s)
    b = time.time()
    s=iamd(times,ilist)
    print('iamd,1000times:%f,result=%f' % (time.time()-b,s),s)
    b = time.time()
    s=famd(times,flist)
    print('famd,1000times:%f,result=%f' % (time.time()-b,s),s)




