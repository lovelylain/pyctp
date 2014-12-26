# -*-coding:utf-8 -*-

import unittest
from ..common.utils import TList as TICKS
from ..common.base import DAY_FINALIZE_TICK

from ..core.dac import *


class ModuleTest(unittest.TestCase):

    ###基本运算
    def test_oper1(self):   #测试NEG
        self.assertEqual([],NEG([]))
        a = [1,2,-3,4,-5,6]
        self.assertEqual([-1,-2,3,-4,5,-6],NEG(a))
        r1 = NEG(a)
        a.append(7)
        a.append(-8)
        self.assertEqual([-1,-2,3,-4,5,-6,-7,8],NEG(a))
        r2 = NEG(a)
        self.assertEqual(id(r1),id(r2))


    def test_oper2(self):   #测试ADD
        self.assertEqual([],ADD([],[]))
        a = [1,2,3,4,5,6]
        b = [10,20,30,40,50,60]
        self.assertEqual([11,22,33,44,55,66],ADD(a,b))
        r1 = ADD(a,b)
        a.append(7)
        b.append(70)
        self.assertEqual([11,22,33,44,55,66,77],ADD(a,b))
        r2 = ADD(a,b)
        self.assertEqual(id(r1),id(r2))

    def test_oper21(self):   #测试ADD
        self.assertEqual([],ADD1([],0))
        a = [1,2,3,4,5,6]
        self.assertEqual([3,4,5,6,7,8],ADD1(a,2))
        r1 = ADD1(a,2)
        a.append(7)
        self.assertEqual([4,5,6,7,8,9,10],ADD1(a,3))
        r2 = ADD1(a,2)
        self.assertEqual(id(r1),id(r2))

    def test_and(self):   #测试AND
        self.assertEqual([],AND([],[]))
        a = [1,2,3,4,0,6]
        b = [10,-20,30,40,50,60]
        self.assertEqual([True,True,True,True,False,True],AND(a,b))
        r1 = AND(a,b)
        a.append(7)
        b.append(70)
        self.assertEqual([True,True,True,True,False,True,True],AND(a,b))
        a.append(9)
        b.append(0)
        self.assertEqual([True,True,True,True,False,True,True,False],AND(a,b))
        r2 = AND(a,b)
        self.assertEqual(id(r1),id(r2))

    def test_gand(self):   #测试AND
        self.assertEqual([],GAND([],[]))
        a = [1,2,3,4,0,6]
        b = [10,-20,30,40,50,60]
        self.assertEqual([True,True,True,True,False,True],GAND(a,b))
        r1 = GAND(a,b)
        a.append(7)
        b.append(70)
        self.assertEqual([True,True,True,True,False,True,True],GAND(a,b))
        a.append(9)
        b.append(0)
        self.assertEqual([True,True,True,True,False,True,True,False],GAND(a,b))
        r2 = GAND(a,b)
        self.assertEqual(id(r1),id(r2))


    def test_gor(self):   #测试AND
        self.assertEqual([],GOR([],[]))
        a = [1,0,3,0,0,6]
        b = [10,-2,30,0,50,60]
        self.assertEqual([True,True,True,False,True,True],GOR(a,b))
        r1 = GOR(a,b)
        a.append(0)
        b.append(70)
        self.assertEqual([True,True,True,False,True,True,True],GOR(a,b))
        a.append(0)
        b.append(0)
        self.assertEqual([True,True,True,False,True,True,True,False],GOR(a,b))
        r2 = GOR(a,b)
        self.assertEqual(id(r1),id(r2))


    def test_DIV(self):   
        self.assertEqual([],DIV([],[]))
        a = [10,20,30,15,50,30]
        b = [1,2,3,4,0,6]
        self.assertEqual([10,10,10,3.75,MAX_VALUE,5],DIV(a,b))
        r1 = DIV(a,b)
        a.append(7)
        b.append(70)
        self.assertEqual([10,10,10,3.75,MAX_VALUE,5,0.1],DIV(a,b))
        r2 = DIV(a,b)
        self.assertEqual(id(r1),id(r2))

    def test_DIV1(self):   
        self.assertEqual([],DIV1([],12))
        a = [10,4,30,15,50,30]
        self.assertEqual([1,0.4,3,1.5,5,3],DIV1(a,10))
        r1 = DIV1(a,10)
        a.append(7)
        self.assertEqual([1,0.4,3,1.5,5,3,0.7],DIV1(a,10))
        r2 = DIV1(a,10)
        self.assertEqual(id(r1),id(r2))

    ##常用指标
    def test_sum(self):
        #x= [1,2,3,4,5,6,7,8,9,0],[],[],{},{},[]      #在test_nsum之后执行,为避免id(a)重复(因为ACC和NSUM是同一个类共用缓存)，先分配掉这些地址
        self.assertEqual([],ACCUMULATE([]))
        a= [1,2,3,4,5,6,7,8,9,0]
        #print("in test_sum,id(a)=",id(a))
        r1 = ACCUMULATE(a)
        #print(a,r1)
        self.assertEqual([1,3,6,10,15,21,28,36,45,45],r1)
        a.append(100)
        self.assertEqual([1,3,6,10,15,21,28,36,45,45,145],ACCUMULATE(a))
        r2 = ACCUMULATE(a)
        self.assertEqual(id(r1),id(r2))
        ACCUMULATE._instances.clear()

    def test_nsum(self):
        self.assertEqual([],NSUM([]))
        a= [1,2,3,4,5,6,7,8,9,0]
        #print("in test_nsum,id(a)=",id(a))
        self.assertEqual([1,3,6,10,15,21,28,36,45,45],NSUM(a))
        r1 = NSUM(a)
        a.append(101)
        self.assertEqual([1,3,6,10,15,21,28,36,45,45,146],NSUM(a))
        r2 = NSUM(a)
        self.assertEqual(id(r1),id(r2))
        ACCUMULATE._instances.clear()

    def test_msum(self):
        self.assertEqual([],MSUM([],2))
        a= [1,2,3,4,5,6,7,8,9,0]
        self.assertEqual([1,2,3,4,5,6,7,8,9,0],MSUM(a,1))
        self.assertEqual([1,3,5,7,9,11,13,15,17,9],MSUM(a,2))
        r1 = MSUM(a,2)
        a.append(100)
        self.assertEqual([1,3,5,7,9,11,13,15,17,9,100],MSUM(a,2))
        r2 = MSUM(a,2)
        self.assertEqual(id(r1),id(r2))

    def test_ma(self):
        self.assertEqual([],MA([],3))
        a= [1,2,3,4,5,6,7,8,9,0]
        self.assertEqual([1,1.5,2,3,4,5,6,7,8,17/3],MA(a,3))
        r1 = MA(a,3)
        a.append(100)
        self.assertEqual([1,1.5,2,3,4,5,6,7,8,17/3,109/3],MA(a,3))
        r2 = MA(a,3)
        self.assertEqual(id(r1),id(r2))

    def test_ma2(self):
        self.assertEqual([],MA([],3))
        a= [1,2,3,4,5,6,7,8,9,0]
        self.assertEqual([1,1.5,2,3,4,5,6,7,8,17/3],MA2(a,3))
        r1 = MA2(a,3)
        a.append(100)
        self.assertEqual([1,1.5,2,3,4,5,6,7,8,17/3,109/3],MA2(a,3))
        r2 = MA2(a,3)
        self.assertEqual(id(r1),id(r2))

    def test_nma(self):
        self.assertEqual([],NMA([]))
        a= [1,2,3,4,5,6,7,8,9,0]
        self.assertEqual([1,1.5,2,2.5,3,3.5,4,4.5,5,4.5],NMA(a))
        r1 = NMA(a)
        a.append(100)
        self.assertEqual([1,1.5,2,2.5,3,3.5,4,4.5,5,4.5,145/11],NMA(a))
        r2 = NMA(a)
        self.assertEqual(id(r1),id(r2))

    def test_cexpma(self):
        self.assertEqual([],CEXPMA([],6))
        source = [25000,24875,24781,24594,24500,24625,25219,27250]
        self.assertEqual([25000,24958,24899,24797,24698,24674,24856,25654],[int(x+0.5) for x in CEXPMA(source,5)])   #相当于5日
        r1 = CEXPMA(source,5)
        source.append(200000)
        self.assertEqual([25000,24958,24899,24797,24698,24674,24856,25654,83769],[int(x+0.5) for x in CEXPMA(source,5)])   #相当于5日
        r2 = CEXPMA(source,5)
        self.assertEqual(id(r1),id(r2))

    def test_MACD(self):    #通道测试
        self.assertEqual([],MACD([]))
        source = [25000,24875,24781,24594,24500,24625,25219,27250]
        r1 = MACD(source)
        source.append(20000)
        r2 = MACD(source)
        self.assertEqual(id(r1),id(r2))

    def test_tr(self):
        self.assertEqual([],TR([],[],[]))
        shigh = [200,250,200,400]
        slow = [100,200,100,200]
        sclose = [150,220,150,300]
        self.assertEqual([100,100,120,250],TR(sclose,shigh,slow))
        r1 = TR(sclose,shigh,slow)
        shigh.append(1000)
        slow.append(500)
        sclose.append(700)
        self.assertEqual([100,100,120,250,700],TR(sclose,shigh,slow))
        r2 = TR(sclose,shigh,slow)
        self.assertEqual(id(r1),id(r2))

    def test_atr(self):
        shigh = [200,250,200,400]
        slow = [100,200,100,200]
        sclose = [150,220,150,300]
        self.assertEqual([100,100,120,250],ATR(sclose,shigh,slow,1))
        r1 = ATR(sclose,shigh,slow)
        shigh.append(1000)
        slow.append(500)
        sclose.append(700)
        self.assertEqual([100,100,120,250,700],ATR(sclose,shigh,slow,1))
        r2 = ATR(sclose,shigh,slow)
        self.assertEqual(id(r1),id(r2))

    def test_xatr(self):
        self.assertEqual([],XATR([],[],[]))
        shigh = [200,250,200,400]
        slow = [100,200,100,200]
        sclose = [150,220,150,300]
        self.assertEqual([666667,454545,679365,386697],[int(x*1000000+0.5) for x in XATR(sclose,shigh,slow)])
        r1 = XATR(sclose,shigh,slow)
        shigh.append(1000)
        slow.append(500)
        sclose.append(700)
        self.assertEqual([666667,454545,679365,386697,245182],[int(x*1000000+0.5) for x in XATR(sclose,shigh,slow)])
        r2 = XATR(sclose,shigh,slow)
        self.assertEqual(id(r1),id(r2))

    def test_strend(self):
        self.assertEqual([],STREND([]))
        self.assertEqual([0],STREND([1]))        
        source = [10,20,30,30,40,50,40,30,20,20,10,20]
        self.assertEqual([0,1,2,3,4,5,-1,-2,-3,-4,-5,1],STREND(source))
        r1 = STREND(source)
        source.append(20)
        self.assertEqual([0,1,2,3,4,5,-1,-2,-3,-4,-5,1,2],STREND(source))
        source.append(30)
        self.assertEqual([0,1,2,3,4,5,-1,-2,-3,-4,-5,1,2,3],STREND(source))
        source.append(20)
        self.assertEqual([0,1,2,3,4,5,-1,-2,-3,-4,-5,1,2,3,-1],STREND(source))
        source.append(10)
        self.assertEqual([0,1,2,3,4,5,-1,-2,-3,-4,-5,1,2,3,-1,-2],STREND(source))
        r2 = STREND(source)
        self.assertEqual(id(r1),id(r2))


    def test_tmax(self):
        self.assertEqual([],TMAX([],10))
        source = [10,12,3,2,5,100,0,13,16,9]
        self.assertEqual([10,12,3,2,5,100,0,13,16,9],TMAX(source,1))
        self.assertEqual([10,12,12,3,5,100,100,13,16,16],TMAX(source,2))
        r1 = TMAX(source,2)
        source.append(3)
        source.append(30)
        self.assertEqual([10,12,12,3,5,100,100,13,16,16,9,30],TMAX(source,2))
        self.assertEqual([10,12,12,12,5,100,100,100,16,16,16,30],TMAX(source,3))
        r2 = TMAX(source,2)
        r3 = TMAX(source,3)
        self.assertEqual(id(r1),id(r2))
        self.assertNotEqual(id(r1),id(r3))

    def test_tmin(self):
        self.assertEqual([],TMIN([],10))
        source = [10,12,3,2,5,100,0,13,16,9]
        self.assertEqual([10,12,3,2,5,100,0,13,16,9],TMIN(source,1))
        self.assertEqual([10,10,3,2,2,5,0,0,13,9],TMIN(source,2))
        r1 = TMIN(source,2)
        source.append(3)
        source.append(30)
        self.assertEqual([10,10,3,2,2,5,0,0,13,9,3,3],TMIN(source,2))
        self.assertEqual([10,10,3,2,2,2,0,0,0,9,3,3],TMIN(source,3))
        r2 = TMIN(source,2)
        r3 = TMIN(source,3)
        self.assertEqual(id(r1),id(r2))
        self.assertNotEqual(id(r1),id(r3))
        r4 = TMAX(source,3)
        self.assertNotEqual(id(r3),id(r4))


    def test_nmax(self):
        self.assertEqual([],NMAX([]))
        source = [10,12,3,2,5,100,0,13,16,9]
        self.assertEqual([10,12,12,12,12,100,100,100,100,100],NMAX(source))
        r1 = NMAX(source)
        source.append(3)
        source.append(103)
        self.assertEqual([10,12,12,12,12,100,100,100,100,100,100,103],NMAX(source))
        r2 = NMAX(source)
        self.assertEqual(id(r1),id(r2))

    def test_nmin(self):
        self.assertEqual([],NMIN([]))
        source = [10,12,3,2,5,100,0,13,16,9]
        self.assertEqual([10,10,3,2,2,2,0,0,0,0],NMIN(source))
        r1 = NMIN(source)
        source.append(3)
        source.append(-1)
        self.assertEqual([10,10,3,2,2,2,0,0,0,0,0,-1],NMIN(source))
        r2 = NMIN(source)
        self.assertEqual(id(r1),id(r2))

    def test_cross(self):   #
        self.assertEqual([],UPCROSS([],[]))
        target = [10,20,30,40,50,40,30,20,10,12,11,12]
        follow = [5,15,35,41,60,50,25,26,8,12,13,12]
        self.assertEqual([0,0,1,0,0,0,0,1,0,0,1,0],UPCROSS(target,follow))
        self.assertEqual([1,0,0,0,0,0,1,0,1,0,0,0],DOWNCROSS(target,follow))
        r1 = UPCROSS(target,follow)
        r2 = DOWNCROSS(target,follow)
        self.assertNotEqual(id(r1),id(r2))
        target.append(15)
        follow.append(11)
        self.assertEqual([0,0,1,0,0,0,0,1,0,0,1,0,0],UPCROSS(target,follow))
        self.assertEqual([1,0,0,0,0,0,1,0,1,0,0,0,1],DOWNCROSS(target,follow))
        target.append(13)
        follow.append(25)
        self.assertEqual([0,0,1,0,0,0,0,1,0,0,1,0,0,1],UPCROSS(target,follow))
        self.assertEqual([1,0,0,0,0,0,1,0,1,0,0,0,1,0],DOWNCROSS(target,follow))
        r3 = UPCROSS(target,follow)
        r4 = DOWNCROSS(target,follow)
        self.assertNotEqual(id(r3),id(r4))
        self.assertEqual(id(r1),id(r3))
        self.assertEqual(id(r2),id(r4))


    def test_ncross(self):   #
        self.assertEqual([],NUPCROSS([],10))
        follow = [5,15,35,41,60,50,25,26,8,12,13,12]
        self.assertEqual([0,1,0,0,0,0,0,0,0,1,0,0],NUPCROSS(follow,10))
        self.assertEqual([1,0,0,0,0,0,0,0,1,0,0,0],NDOWNCROSS(follow,10))
        r1 = NUPCROSS(follow,10)
        r2 = NDOWNCROSS(follow,10)
        self.assertNotEqual(id(r1),id(r2))
        follow.append(8)
        self.assertEqual([0,1,0,0,0,0,0,0,0,1,0,0,0],NUPCROSS(follow,10))
        self.assertEqual([1,0,0,0,0,0,0,0,1,0,0,0,1],NDOWNCROSS(follow,10))
        follow.append(25)
        self.assertEqual([0,0,1,0,0,0,0,0,0,0,0,0,0,1],NUPCROSS(follow,15))
        self.assertEqual([1,0,0,0,0,0,0,0,1,0,0,0,1,0],NDOWNCROSS(follow,10))
        r3 = NUPCROSS(follow,10)
        r4 = NDOWNCROSS(follow,10)
        self.assertNotEqual(id(r3),id(r4))
        self.assertEqual(id(r1),id(r3))
        self.assertEqual(id(r2),id(r4))

    def test_ref(self):
        self.assertEqual([],REF([]))
        a= [1,2,3,4,5,6,7,8,9,0]
        self.assertEqual([1,2,3,4,5,6,7,8,9,0],REF(a,0))
        self.assertEqual([1,1,2,3,4,5,6,7,8,9],REF(a,1))
        self.assertEqual([1,1,1,2,3,4,5,6,7,8],REF(a,2))
        self.assertEqual([1,1,1,1,1,1,1,1,1,2],REF(a,8))
        self.assertEqual([1,1,1,1,1,1,1,1,1,1],REF(a,9))
        self.assertEqual([1,1,1,1,1,1,1,1,1,1],REF(a,10))
        self.assertEqual([1,1,1,1,1,1,1,1,1,1],REF(a,11))
        self.assertEqual([1,1,1,1,1,1,1,1,1,1],REF(a,100))
        r1 = REF(a,2)
        r2 = REF(a,10)
        self.assertNotEqual(id(r1),id(r2))
        a.append(100)
        self.assertEqual([1,1,1,2,3,4,5,6,7,8,9],REF(a,2))
        r3 = REF(a,2)
        r4 = REF(a,10)
        self.assertNotEqual(id(r3),id(r4))
        self.assertEqual(id(r1),id(r3))
        self.assertEqual(id(r2),id(r4))

    def test_unit_attr(self):
        s = [BaseObject(date=20130101),BaseObject(date=20130102)]
        self.assertEqual([],TICK_DATE([]))
        self.assertEqual([20130101,20130102],TICK_DATE(s))
        r1 = TICK_DATE(s)
        s.append(BaseObject(date=20140101))
        self.assertEqual([20130101,20130102,20140101],TICK_DATE(s))
        r2 = TICK_DATE(s)
        self.assertEqual(id(r1),id(r2))


    def test_minute(self):
        #m1 = MINUTE([])
        #self.assertEqual([],m1)
        time2min = lambda t : t%1000000//100
        ticks = TICKS([TICK("X",20140101),TICK("X",20140101),TICK("X",20140101),TICK("X",20140101)])
        ticks[0].price = 100
        ticks[0].time = 111091400
        ticks[0].date = 20120111
        ticks[0].tdate = 20120111
        ticks[0].dvolume = 10
        ticks[0].damount = 10000
        ticks[0].holding = 10
        ticks[0].min1 = time2min(ticks[0].time)
        ticks[1].price = 110
        ticks[1].time = 111091500
        ticks[1].date = 20120111
        ticks[1].tdate = 20120111
        ticks[1].min1 = time2min(ticks[1].time)
        ticks[1].dvolume = 30
        ticks[1].damount = 30000
        ticks[1].holding = 11
        ticks[2].price = 115
        ticks[2].time = 111091501
        ticks[2].date = 20120111
        ticks[2].tdate = 20120111
        ticks[2].dvolume = 50
        ticks[2].damount = 50000
        ticks[2].holding = 12
        ticks[2].min1 = time2min(ticks[2].time)
        ticks[3].price = 91
        ticks[3].time = 111091600
        ticks[3].date = 20120111
        ticks[3].tdate = 20120111
        ticks[3].dvolume = 51
        ticks[3].damount = 51000
        ticks[3].holding = 13
        ticks[3].min1 = time2min(ticks[3].time)
        cm2 = MINUTE(ticks)
        #print(cm2[0],cm2[0].sdate,cm2[0].stime)
        self.assertEqual(2,len(cm2))
        self.assertEqual(100,cm2[0].sclose)
        self.assertEqual(115,cm2[1].sclose)
        self.assertEqual(100,cm2[0].slow)
        self.assertEqual(110,cm2[1].slow)
        self.assertEqual(100,cm2[0].shigh)
        self.assertEqual(115,cm2[1].shigh)
        self.assertEqual(914,cm2[0].stime)
        self.assertEqual(915,cm2[1].stime)
        self.assertEqual(10,cm2[0].svolume)
        self.assertEqual(40,cm2[1].svolume)
        self.assertEqual(10000,cm2[0].samount)
        self.assertEqual(40000,cm2[1].samount)

        self.assertTrue(cm2.modified)
        #
        ticks.extend([TICK("X",20140101),TICK("X",20140101),TICK("X",20140101)])
        ticks[4].price = 93
        ticks[4].time = 101091601
        ticks[4].date = 20120111
        ticks[4].tdate = 20120111
        ticks[4].min1 = time2min(ticks[4].time)
        ticks[4].dvolume = 80
        ticks[4].damount = 80000
        ticks[4].holding = 10
        ticks[5].price = 90
        ticks[5].time = 101091602
        ticks[5].date = 20120111
        ticks[5].tdate = 20120111
        ticks[5].dvolume = 88
        ticks[5].damount = 88000
        ticks[5].holding = 10
        ticks[5].min1 = time2min(ticks[5].time)
        ticks[6].price = 90
        ticks[6].time = 111091700
        ticks[6].date = 20120111
        ticks[6].tdate = 20120111
        ticks[6].dvolume = 89
        ticks[6].damount = 89000
        ticks[6].holding = 10
        ticks[6].min1 = time2min(ticks[6].time)

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertEqual(90,cm2[2].sclose)
        self.assertEqual(90,cm2[2].slow)
        self.assertEqual(93,cm2[2].shigh)
        self.assertEqual(916,cm2[2].stime)
        self.assertEqual(38,cm2[2].svolume)
        self.assertEqual(38000,cm2[2].samount)
        self.assertTrue(cm2.modified)
        ##
        ticks.append(TICK("X",20140101))
        ticks[7].price = 91
        ticks[7].time = 111091701
        ticks[7].date = 20120111
        ticks[7].tdate = 20120111
        ticks[7].dvolume = 99
        ticks[7].damount = 99000
        ticks[7].holding = 10
        ticks[7].min1 = time2min(ticks[7].time)

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertFalse(cm2.modified)
        self.assertEqual(916,cm2[2].stime)
        ##测试终结符
        #ticks.append(TICK("X",20140101))
        #print(DAY_FINALIZE_TICK.damount)
        ticks.append(DAY_FINALIZE_TICK)

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertTrue(cm2.modified)
        self.assertEqual(917,cm2[3].stime)
        ##测试重复的终结符
        ticks.append(DAY_FINALIZE_TICK)

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertFalse(cm2.modified)   #无变化
        self.assertEqual(917,cm2[3].stime)
        ##测试pre_min
        spre_min1 = [BaseObject(),BaseObject()] #占位
        ticks = TICKS(ticks[:4])

        cm3 = MINUTE(ticks,spre_min1=spre_min1)

        self.assertNotEqual(id(cm2),id(cm3))

        self.assertEqual(4,len(cm3))
        self.assertEqual(100,cm3[2].sclose)
        self.assertEqual(115,cm3[3].sclose)

    def test_minute_remove_0(self):
        #m1 = MINUTE([])
        #self.assertEqual([],m1)
        time2min = lambda t : t%1000000//100
        ticks = TICKS([TICK("X",20140101),TICK("X",20140101),TICK("X",20140101),TICK("X",20140101)])
        ticks[0].price = 100
        ticks[0].time = 111091400
        ticks[0].date = 20120111
        ticks[0].tdate = 20120111
        ticks[0].dvolume = 10
        ticks[0].damount = 10000
        ticks[0].holding = 10
        ticks[0].min1 = time2min(ticks[0].time)
        ticks[1].price = 110
        ticks[1].time = 111091500
        ticks[1].date = 20120111
        ticks[1].tdate = 20120111
        ticks[1].min1 = time2min(ticks[1].time)
        ticks[1].dvolume = 30
        ticks[1].damount = 30000
        ticks[1].holding = 11
        ticks[2].price = 115
        ticks[2].time = 111091501
        ticks[2].date = 20120111
        ticks[2].tdate = 20120111
        ticks[2].dvolume = 50
        ticks[2].damount = 50000
        ticks[2].holding = 12
        ticks[2].min1 = time2min(ticks[2].time)
        ticks[3].price = 91
        ticks[3].time = 111091600
        ticks[3].date = 20120111
        ticks[3].tdate = 20120111
        ticks[3].dvolume = 51
        ticks[3].damount = 51000
        ticks[3].holding = 13
        ticks[3].min1 = time2min(ticks[3].time)
        cm2 = MINUTE(ticks)
        #print(cm2[0],cm2[0].sdate,cm2[0].stime)
        self.assertEqual(2,len(cm2))
        self.assertTrue(cm2.modified)
        cm2.remove_part()
        self.assertEqual(0,len(cm2))
        #
        ticks.extend([TICK("X",20140101),TICK("X",20140101),TICK("X",20140101)])
        ticks[4].price = 93
        ticks[4].time = 101091601
        ticks[4].date = 20120111
        ticks[4].tdate = 20120111
        ticks[4].min1 = time2min(ticks[4].time)
        ticks[4].dvolume = 80
        ticks[4].damount = 80000
        ticks[4].holding = 10
        ticks[5].price = 90
        ticks[5].time = 101091602
        ticks[5].date = 20120111
        ticks[5].tdate = 20120111
        ticks[5].dvolume = 88
        ticks[5].damount = 88000
        ticks[5].holding = 10
        ticks[5].min1 = time2min(ticks[5].time)
        ticks[6].price = 90
        ticks[6].time = 111091700
        ticks[6].date = 20120111
        ticks[6].tdate = 20120111
        ticks[6].dvolume = 89
        ticks[6].damount = 89000
        ticks[6].holding = 10
        ticks[6].min1 = time2min(ticks[6].time)

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertEqual(90,cm2[0].sclose)
        self.assertEqual(90,cm2[0].slow)
        self.assertEqual(93,cm2[0].shigh)
        self.assertEqual(916,cm2[0].stime)
        self.assertEqual(38,cm2[0].svolume)
        self.assertEqual(38000,cm2[0].samount)
        self.assertTrue(cm2.modified)
        self.assertEqual(1,len(cm2))
        ##
        ticks.append(TICK("X",20140101))
        ticks[7].price = 91
        ticks[7].time = 111091701
        ticks[7].date = 20120111
        ticks[7].tdate = 20120111
        ticks[7].dvolume = 99
        ticks[7].damount = 99000
        ticks[7].holding = 10
        ticks[7].min1 = time2min(ticks[7].time)

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertFalse(cm2.modified)
        self.assertEqual(1,len(cm2))
        ##测试终结符
        #ticks.append(TICK("X",20140101))
        #print(DAY_FINALIZE_TICK.damount)
        ticks.append(DAY_FINALIZE_TICK)

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertTrue(cm2.modified)
        self.assertEqual(2,len(cm2))
        self.assertEqual(917,cm2[1].stime)
        ##测试重复的终结符
        ticks.append(DAY_FINALIZE_TICK)

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertFalse(cm2.modified)   #无变化
        self.assertEqual(917,cm2[1].stime)

        cm2.remove_part()
        self.assertEqual(0,len(cm2))

        MINUTE._instances.clear()

    def test_remove_part(self):
        ticks = TICKS([])
        cm2 = MINUTE(ticks)
        cm2[:2000] = [1]*2000
        self.assertEqual(2000,len(cm2))
        cm2.remove_part()
        self.assertEqual(0,len(cm2))
        cm2[:2000] = [1]*2000
        cm2.remove_part(500)
        self.assertEqual(500,len(cm2))
        cm2.remove_part(800)
        self.assertEqual(500,len(cm2))
        cm2.remove_part(0)
        self.assertEqual(0,len(cm2))

        MINUTE._instances.clear()

    def test_minute_000(self):
        #测试夜盘跨日 从 23:59:59 -> 0:0:0
        time2min = lambda t : t%1000000//100
        ticks = TICKS([TICK("X",20140101),TICK("X",20140101),TICK("X",20140101),TICK("X",20140101)])
        ticks[0].price = 100
        ticks[0].time = 111091400
        ticks[0].date = 20120111
        ticks[0].tdate = 20120111
        ticks[0].dvolume = 10
        ticks[0].damount = 10000
        ticks[0].holding = 10
        ticks[0].min1 = time2min(ticks[0].time)
        ticks[1].price = 110
        ticks[1].time = 111235900
        ticks[1].date = 20120111
        ticks[1].tdate = 20120112
        ticks[1].min1 = time2min(ticks[1].time)
        ticks[1].dvolume = 30
        ticks[1].damount = 30000
        ticks[1].holding = 11
        ticks[2].price = 115
        ticks[2].time = 111235959
        ticks[2].date = 20120111
        ticks[2].tdate = 20120112
        ticks[2].dvolume = 50
        ticks[2].damount = 50000
        ticks[2].holding = 12
        ticks[2].min1 = time2min(ticks[2].time)
        ticks[3].price = 91
        ticks[3].time = 112000000
        ticks[3].date = 20120112
        ticks[3].tdate = 20120112
        ticks[3].dvolume = 51
        ticks[3].damount = 51000
        ticks[3].holding = 13
        ticks[3].min1 = time2min(ticks[3].time)
        cm2 = MINUTE(ticks)
        #print(cm2[0],cm2[0].sdate,cm2[0].stime)
        self.assertEqual(2,len(cm2))
        self.assertEqual(100,cm2[0].sclose)
        self.assertEqual(115,cm2[1].sclose)
        self.assertEqual(100,cm2[0].slow)
        self.assertEqual(110,cm2[1].slow)
        self.assertEqual(100,cm2[0].shigh)
        self.assertEqual(115,cm2[1].shigh)
        self.assertEqual(914,cm2[0].stime)
        self.assertEqual(2359,cm2[1].stime)
        self.assertEqual(10,cm2[0].svolume)
        self.assertEqual(40,cm2[1].svolume)
        self.assertEqual(10000,cm2[0].samount)
        self.assertEqual(40000,cm2[1].samount)

        self.assertTrue(cm2.modified)
        #
        ticks.extend([TICK("X",20140112)])
        ticks[4].price = 93
        ticks[4].time = 112091401
        ticks[4].date = 20120112
        ticks[4].tdate = 20120112
        ticks[4].min1 = time2min(ticks[4].time)
        ticks[4].dvolume = 80
        ticks[4].damount = 80000
        ticks[4].holding = 10

        self.assertEqual(id(cm2),id(MINUTE(ticks)))

        cm2 = MINUTE(ticks)
        self.assertEqual(91,cm2[2].sclose)
        self.assertEqual(91,cm2[2].slow)
        self.assertEqual(91,cm2[2].shigh)
        self.assertEqual(0,cm2[2].stime)
        self.assertEqual(1,cm2[2].svolume)
        self.assertEqual(1000,cm2[2].samount)
        self.assertTrue(cm2.modified)
        #print(id(ticks))
        MINUTE._instances.clear()

    def test_minute_day_finalize(self):
        time2min = lambda t : t%1000000//100
        ticks = TICKS([TICK("X",20140101),TICK("X",20140101)])
        #print(id(ticks))
        ticks[0].price = 100
        ticks[0].time = 111091400
        ticks[0].date = 20120111
        ticks[0].tdate = 20120111
        ticks[0].dvolume = 10
        ticks[0].damount = 10000
        ticks[0].holding = 10
        ticks[0].min1 = time2min(ticks[0].time)
        ticks[1].price = 110
        ticks[1].time = 111091500
        ticks[1].date = 20120111
        ticks[1].tdate = 20120111
        ticks[1].min1 = time2min(ticks[1].time)
        ticks[1].dvolume = 30
        ticks[1].damount = 30000
        ticks[1].holding = 11
        ticks[1].min1 = time2min(ticks[1].time)
        cm1 = MINUTE(ticks)
        self.assertEqual(1,len(cm1))
        self.assertEqual(10,cm1[-1].svolume)
        self.assertTrue(cm1.modified)

        ticks.append(DAY_FINALIZE_TICK)
        cm2 = MINUTE(ticks)
        self.assertEqual(id(cm1),id(cm2))
        self.assertEqual(2,len(cm2))
        self.assertEqual(20,cm1[-1].svolume) #因为直接日结,所以没有svolume
        self.assertTrue(cm2._next_is_new_day)
        self.assertEqual(DAY_FINALIZE_TICK.date,cm2._cur.sdate)
        self.assertTrue(cm2.modified)

        #连续日结
        ticks.append(DAY_FINALIZE_TICK)
        cm2 = MINUTE(ticks)
        self.assertEqual(id(cm1),id(cm2))
        self.assertEqual(2,len(cm2))
        self.assertTrue(cm2._next_is_new_day)
        self.assertEqual(DAY_FINALIZE_TICK.date,cm2._cur.sdate)
        self.assertFalse(cm2.modified)

        ticks.append(TICK("X",0))
        ticks[-1].price = 91
        ticks[-1].time = 112091701
        ticks[-1].date = 20120112
        ticks[-1].tdate = 20120112
        ticks[-1].dvolume = 11
        ticks[-1].damount = 81000
        ticks[-1].holding = 10
        ticks[-1].min1 = time2min(ticks[-1].time)
        cm2 = MINUTE(ticks)
        self.assertFalse(cm2._next_is_new_day)
        #print(cm2.cur.sdvolume,cm2.cur.svolume)
        self.assertEqual(11,cm2._cur.svolume)
        self.assertFalse(cm2.modified)

        ticks.append(DAY_FINALIZE_TICK)
        cm2 = MINUTE(ticks)
        self.assertEqual(id(cm1),id(cm2))
        self.assertEqual(3,len(cm2))
        self.assertEqual(11,cm1[-1].svolume)
        self.assertTrue(cm2._next_is_new_day)
        self.assertEqual(DAY_FINALIZE_TICK.date,cm2._cur.sdate)
        self.assertTrue(cm2.modified)

        #次日第一个tick
        ticks.append(TICK("X",20140501))
        ticks[-1].price = 91
        ticks[-1].time = 112091701
        ticks[-1].date = 20120113
        ticks[-1].tdate = 20120113
        ticks[-1].dvolume = 60
        ticks[-1].damount = 81000
        ticks[-1].holding = 10
        ticks[-1].min1 = time2min(ticks[-1].time)
        #print("-----------------",ticks[2].min1,ticks[2])

        ticks.append(TICK("X",20140501))
        ticks[-1].price = 91
        ticks[-1].time = 112091801
        ticks[-1].date = 20120112
        ticks[-1].tdate = 20120112
        ticks[-1].dvolume = 71
        ticks[-1].damount = 81000
        ticks[-1].holding = 10
        ticks[-1].min1 = time2min(ticks[-1].time)

        ticks.append(TICK("X",20140501))
        ticks[-1].price = 91
        ticks[-1].time = 112091803
        ticks[-1].date = 20120112
        ticks[-1].tdate = 20120112
        ticks[-1].dvolume = 91
        ticks[-1].damount = 81000
        ticks[-1].holding = 10
        ticks[-1].min1 = time2min(ticks[-1].time)
        #print("-----------------",ticks[2].min1,ticks[2])

        cm2 = MINUTE(ticks)
        self.assertEqual(id(cm1),id(cm2))
        self.assertEqual(4,len(cm2))
        self.assertFalse(cm2._next_is_new_day)
        self.assertEqual(ticks[-1].date,cm2._cur.sdate)
        self.assertEqual(60,cm2[-1].svolume)
        self.assertFalse(cm2.modified)  #连续的ticks且跨分钟了,后一tick更改了modified状态

        ticks.append(DAY_FINALIZE_TICK)
        cm2 = MINUTE(ticks)
        self.assertEqual(id(cm1),id(cm2))
        self.assertEqual(5,len(cm2))
        self.assertEqual(31,cm2[-1].svolume)
        self.assertTrue(cm2._next_is_new_day)
        self.assertEqual(DAY_FINALIZE_TICK.date,cm2._cur.sdate)
        self.assertTrue(cm2.modified)

        MINUTE._instances.clear()       #清除缓存


    def test_xminute(self):
        class TM(list):pass
        minutes = TM()
        minutes.next_is_new_day = False

        r0 = MINUTE15(minutes)
        self.assertEqual(0,len(r0))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=914,sopen=1000,sclose=1010,shigh=1020,slow=998,
                                  svolume=30,samount=30000,sholding=200))
        r1 = MINUTE15(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=915,sopen=1001,sclose=1011,shigh=1020,slow=998,
                                  svolume=30,samount=30001,sholding=201))
        r1 = MINUTE15(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=916,sopen=1002,sclose=1012,shigh=1015,slow=999,
                                  svolume=30,samount=30002,sholding=202))
        r1 = MINUTE15(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=929,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=203))
        r1 = MINUTE15(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))

        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=930,sopen=1004,sclose=1014,shigh=1024,slow=994,
                                  svolume=34,samount=30004,sholding=204))

        r1 = MINUTE15(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(1,len(r1))
        self.assertEqual(20140105,r1[-1].sdate)
        self.assertEqual(929,r1[-1].stime)
        self.assertEqual(1000,r1[-1].sopen)
        self.assertEqual(1013,r1[-1].sclose)
        self.assertEqual(1023,r1[-1].shigh)
        self.assertEqual(995,r1[-1].slow)
        self.assertEqual(123,r1[-1].svolume)
        self.assertEqual(120006,r1[-1].samount)
        self.assertEqual(203,r1[-1].sholding)


        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=945,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=203))
        r1 = MINUTE15(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(1,len(r1))

        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=1000,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        r1 = MINUTE15(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(2,len(r1))
        self.assertEqual(945,r1[-1].stime)

        #换日
        minutes.append(BaseObject(sdate=20140106,stdate=20140106,stime=859,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=203))
        r1 = MINUTE15(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(3,len(r1))
        self.assertEqual(1000,r1[-1].stime)
        self.assertEqual(205,r1[-1].sholding)
        self.assertEqual(33,r1[-1].svolume)

        r2 = MINUTE10(minutes)
        self.assertNotEqual(id(r0),id(r2))


    def test_minuted(self):
        class TM(list):pass
        minutes = TM()
        minutes.next_is_new_day = False

        r0 = MINUTED(minutes)
        self.assertEqual(0,len(r0))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=914,sopen=1000,sclose=1010,shigh=1020,slow=998,
                                  svolume=30,samount=30000,sholding=200))
        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=915,sopen=1001,sclose=1011,shigh=1020,slow=998,
                                  svolume=30,samount=30001,sholding=201))
        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=916,sopen=1002,sclose=1012,shigh=1015,slow=999,
                                  svolume=30,samount=30002,sholding=202))
        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=929,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=203))
        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))

        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=930,sopen=1004,sclose=1014,shigh=1024,slow=994,
                                  svolume=34,samount=30004,sholding=204))

        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))

        #换日
        minutes.append(BaseObject(sdate=20140106,stdate=20140106,stime=859,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(1,len(r1))
        self.assertEqual(20140105,r1[-1].sdate)
        self.assertEqual(930,r1[-1].stime)
        self.assertEqual(1000,r1[-1].sopen)
        self.assertEqual(1014,r1[-1].sclose)
        self.assertEqual(1024,r1[-1].shigh)
        self.assertEqual(994,r1[-1].slow)
        self.assertEqual(157,r1[-1].svolume)
        self.assertEqual(150010,r1[-1].samount)
        self.assertEqual(204,r1[-1].sholding)

        minutes.append(BaseObject(sdate=20140107,stdate=20140107,stime=859,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(2,len(r1))

        #next_is_new_day = False
        r1 = MINUTED(minutes)
        minutes.append(BaseObject(sdate=20140107,stdate=20140107,stime=900,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        #print("next is new day:",minutes.next_is_new_day)
        #minutes.next_is_new_day = True
        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(2,len(r1))

        #next_is_new_day = True
        minutes.append(BaseObject(sdate=20140107,stdate=20140107,stime=901,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        #print("next is new day:",minutes.next_is_new_day)
        minutes.next_is_new_day = True
        r1 = MINUTED(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(3,len(r1))

        #测试一次性处理
        minutes2 = TM()
        minutes2.next_is_new_day = True
        minutes2[0:0] = minutes[:]
        rx = MINUTED(minutes2)
        self.assertNotEqual(id(r0),id(rx))
        self.assertEqual(3,len(rx))


    def test_minuted2(self):
        class TM(list):pass
        minutes = TM()
        minutes.next_is_new_day = False

        r0 = MINUTE2D(minutes)
        self.assertEqual(0,len(r0))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=914,sopen=1000,sclose=1010,shigh=1020,slow=998,
                                  svolume=30,samount=30000,sholding=200))
        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=915,sopen=1001,sclose=1011,shigh=1020,slow=998,
                                  svolume=30,samount=30001,sholding=201))
        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=916,sopen=1002,sclose=1012,shigh=1015,slow=999,
                                  svolume=30,samount=30002,sholding=202))
        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))
        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=929,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=203))
        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))

        minutes.append(BaseObject(sdate=20140105,stdate=20140105,stime=930,sopen=1004,sclose=1014,shigh=1024,slow=994,
                                  svolume=34,samount=30004,sholding=204))

        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(0,len(r1))

        #换日
        minutes.append(BaseObject(sdate=20140106,stdate=20140106,stime=859,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(1,len(r1))
        self.assertEqual(20140105,r1[-1].sdate)
        self.assertEqual(930,r1[-1].stime)
        self.assertEqual(1000,r1[-1].sopen)
        self.assertEqual(1014,r1[-1].sclose)
        self.assertEqual(1024,r1[-1].shigh)
        self.assertEqual(994,r1[-1].slow)
        self.assertEqual(157,r1[-1].svolume)
        self.assertEqual(150010,r1[-1].samount)
        self.assertEqual(204,r1[-1].sholding)

        minutes.append(BaseObject(sdate=20140107,stdate=20140107,stime=859,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(2,len(r1))

        #next_is_new_day = False
        r1 = MINUTE2D(minutes)
        minutes.append(BaseObject(sdate=20140107,stdate=20140107,stime=900,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        #print("next is new day:",minutes.next_is_new_day)
        #minutes.next_is_new_day = True
        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(2,len(r1))

        #next_is_new_day = True
        minutes.append(BaseObject(sdate=20140107,stdate=20140107,stime=901,sopen=1003,sclose=1013,shigh=1023,slow=995,
                                  svolume=33,samount=30003,sholding=205))
        #print("next is new day:",minutes.next_is_new_day)
        minutes.next_is_new_day = True
        r1 = MINUTE2D(minutes)
        self.assertEqual(id(r0),id(r1))
        self.assertEqual(3,len(r1))

        #测试一次性处理
        minutes2 = TM()
        minutes2.next_is_new_day = True
        minutes2[0:0] = minutes[:]
        rx = MINUTE2D(minutes2)
        self.assertNotEqual(id(r0),id(rx))
        self.assertEqual(3,len(rx))

        #测试SPRE_DAYS
        day1 = BaseObject(sdate=20140104)
        days01 = [day1]     #这里必须用变量把[day1]持住,否则会面会因为对象重新分配到同一地址而引起缓存混乱
        days02 = [day1]
        ry = MINUTE2D(minutes,days01)
        rz = MINUTE2D(minutes,days02)
        #ry = MINUTED2(minutes,[day1])  #不能这样,必须用变量把[day1]持住,否则会面会因为对象重新分配到同一地址而引起缓存混乱
        #rz = MINUTED2(minutes,[day1])  #不能这样,必须用变量把[day1]持住,否则会面会因为对象重新分配到同一地址而引起缓存混乱
        self.assertNotEqual(id(r0),id(ry))
        self.assertNotEqual(id(r0),id(rz))
        days = [day1]
        ry = MINUTE2D(minutes,days)
        rz = MINUTE2D(minutes,days)
        self.assertNotEqual(id(r0),id(ry))
        self.assertEqual(id(ry),id(rz))
        #print(ry[0].sdate,ry[1].sdate)
        self.assertEqual(4,len(ry))
        days2 = [BaseObject(sdate=20140105)]
        #print("sdate=20140105 start....")
        rz = MINUTE2D(minutes,days2)
        self.assertNotEqual(id(ry),id(rz))
        self.assertEqual(3,len(rz))
        days3 = [BaseObject(sdate=20140106)]
        #print("sdate=20140105 start....")
        rz = MINUTE2D(minutes,days3)
        self.assertNotEqual(id(ry),id(rz))
        self.assertEqual(2,len(rz))

        days4 = [BaseObject(sdate=20140108)]
        #print("sdate=20140105 start....")
        rz = MINUTE2D(minutes,days4)
        self.assertNotEqual(id(ry),id(rz))
        self.assertEqual(1,len(rz))


    def test_cur_day(self):
        time2min = lambda t : t%1000000//100
        ticks = TICKS([TICK("X",20140101),TICK("X",20140101),TICK("X",20140101),TICK("X",20140101)])
        ticks[0].price = 100
        ticks[0].time = 111091400
        ticks[0].date = 20120111
        ticks[0].tdate = 20120111
        ticks[0].dvolume = 10
        ticks[0].damount = 10000
        ticks[0].holding = 10
        ticks[0].high = 100
        ticks[0].low = 89
        ticks[0].min1 = time2min(ticks[0].time)
        ticks[1].price = 110
        ticks[1].time = 111091500
        ticks[1].date = 20120111
        ticks[1].tdate = 20120111
        ticks[1].min1 = time2min(ticks[1].time)
        ticks[1].dvolume = 30
        ticks[1].damount = 30000
        ticks[1].holding = 11
        ticks[1].high = 101
        ticks[1].low = 88
        ticks[2].price = 115
        ticks[2].time = 111091501
        ticks[2].date = 20120111
        ticks[2].tdate = 20120111
        ticks[2].dvolume = 50
        ticks[2].damount = 50000
        ticks[2].holding = 12
        ticks[2].min1 = time2min(ticks[2].time)
        ticks[2].high = 102
        ticks[2].low = 88
        ticks[3].price = 91
        ticks[3].time = 111091600
        ticks[3].date = 20120111
        ticks[3].tdate = 20120111
        ticks[3].dvolume = 51
        ticks[3].damount = 51000
        ticks[3].holding = 13
        ticks[3].min1 = time2min(ticks[3].time)
        ticks[3].high = 103
        ticks[3].low = 87
        cm2 = CUR_DAY(ticks)
        self.assertEqual(0,len(cm2))
        self.assertEqual(100,cm2.sopen)
        self.assertEqual(91,cm2.sclose)
        self.assertEqual(87,cm2.slow)
        self.assertEqual(103,cm2.shigh)
        self.assertEqual(51,cm2.svolume)
        self.assertEqual(51000,cm2.samount)

        self.assertTrue(cm2.modified)
        #
        ticks.extend([TICK("X",20140101)])
        ticks[4].price = 93
        ticks[4].time = 101091601
        ticks[4].date = 20120111
        ticks[4].tdate = 20120111
        ticks[4].min1 = time2min(ticks[4].time)
        ticks[4].dvolume = 80
        ticks[4].damount = 80000
        ticks[4].holding = 10
        ticks[4].high = 104
        ticks[4].low = 86

        self.assertEqual(id(cm2),id(CUR_DAY(ticks)))

        #cm2 = CUR_DAY(ticks)
        self.assertEqual(0,len(cm2))
        self.assertEqual(100,cm2.sopen)
        self.assertEqual(93,cm2.sclose)
        self.assertEqual(86,cm2.slow)
        self.assertEqual(104,cm2.shigh)
        self.assertEqual(80,cm2.svolume)
        self.assertEqual(80000,cm2.samount)
        self.assertEqual(10,cm2.sholding)
        ##
        ticks.append(TICK("X",20140112))
        ticks[5].price = 99
        ticks[5].time = 111091701
        ticks[5].date = 20120111
        ticks[5].tdate = 20120112
        ticks[5].dvolume = 5
        ticks[5].damount = 5000
        ticks[5].holding = 10
        ticks[5].min1 = time2min(ticks[5].time)
        ticks[5].high = 105
        ticks[5].low = 85

        self.assertEqual(id(cm2),id(CUR_DAY(ticks)))
        cm2 = CUR_DAY(ticks)
        self.assertEqual(0,len(cm2))
        self.assertEqual(99,cm2.sopen)
        self.assertEqual(99,cm2.sclose)
        self.assertEqual(85,cm2.slow)
        self.assertEqual(105,cm2.shigh)
        self.assertEqual(5,cm2.svolume)
        self.assertEqual(5000,cm2.samount)
        self.assertEqual(10,cm2.sholding)


        ticks.append(TICK("X",20140112))
        ticks[6].price = 88
        ticks[6].time = 113091701
        ticks[6].date = 20120113
        ticks[6].tdate = 20120113
        ticks[6].dvolume = 15
        ticks[6].damount = 15000
        ticks[6].holding = 110
        ticks[6].min1 = time2min(ticks[5].time)
        ticks[6].high = 115
        ticks[6].low = 75
        self.assertEqual(id(cm2),id(CUR_DAY(ticks)))
        cm2 = CUR_DAY(ticks)
        self.assertEqual(0,len(cm2))
        self.assertEqual(88,cm2.sopen)
        self.assertEqual(88,cm2.sclose)
        self.assertEqual(75,cm2.slow)
        self.assertEqual(115,cm2.shigh)
        self.assertEqual(15,cm2.svolume)
        self.assertEqual(15000,cm2.samount)
        self.assertEqual(110,cm2.sholding)


if __name__ == "__main__":
    import logging
    logging.basicConfig(filename="test_dac.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()

