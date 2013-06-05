# -*-coding:utf-8 -*-

import unittest

from dac import *

class ModuleTest(unittest.TestCase):

    def test_xdiff(self):
        self.assertEquals([],xdiff([]))
        self.assertEquals([0,0,1,0,0,-1],xdiff([0,0,1,0,0,-1]))
        self.assertEquals([0,0,1,0,0,-1],xdiff([0,0,1,1,0,-1]))
        self.assertEquals([0,0,1,0,0,-1],xdiff([0,0,1,0,1,-1]))
        self.assertEquals([0,0,1,0,-1,0],xdiff([0,0,1,1,-1,-1]))

    def test_cexpma(self):
        self.assertEquals([],cexpma([],6))
        source = [25000,24875,24781,24594,24500,24625,25219,27250]
        self.assertEquals([25000,24958,24899,24797,24698,24674,24856,25654],cexpma(source,5))   #相当于5日

    def test_cexpma1(self):
        #self.assertEquals(0,cexpma1([],6,[]))        
        #self.assertEquals(0,cexpma1([100],6,[0]))
        source = [25000,24875,24781,24594,24500,24625,25219,27250]
        target = [25000,24958,24899,24797,24698,24674,24856,0]
        #self.assertEquals(25654,cexpma1(source,5,target))   #相当于5日
        #self.assertEquals(25654,target[-1])
        self.assertEquals(25654,cexpma1(source[-1],5,target[-2]))   #相当于5日

    def test_tr(self):
        self.assertEquals([],tr([],[],[]))
        shigh = [200,250,200,400]
        slow = [100,200,100,200]
        sclose = [150,220,150,300]
        self.assertEquals([100*XBASE,100*XBASE,120*XBASE,250*XBASE],tr(sclose,shigh,slow))

    def test_tr1(self):
        self.assertEquals(0,tr1([],[],[],[]))
        self.assertEquals(0,tr1([200],[100],[150],[0]))        
        shigh = [200,250,200,400]
        slow = [100,200,100,200]
        sclose = [150,220,150,300]
        self.assertEquals([100*XBASE,100*XBASE,120*XBASE,250*XBASE],tr(sclose,shigh,slow))

    def test_atr(self):
        shigh = [200,250,200,400]
        slow = [100,200,100,200]
        sclose = [150,220,150,300]
        ltr = tr(sclose,shigh,slow)
        self.assertEquals([100*XBASE,100*XBASE,120*XBASE,250*XBASE],atr(ltr,1))
    
    def test_atr1(self):
        self.assertEquals(0,atr1([],[],1))
        self.assertEquals(0,atr1([100],[0],1))
        shigh = [200,250,200,400]
        slow = [100,200,100,200]
        sclose = [150,220,150,300]
        ltr = tr(sclose,shigh,slow)
        latr = [100*XBASE,100*XBASE,120*XBASE,0]
        self.assertEquals(250*XBASE,atr1(ltr,latr,1))
        self.assertEquals(250*XBASE,latr[-1])

    def test_xatr(self):
        self.assertEquals([],xatr([],[]))
        self.assertEquals([10*CBASE,20*CBASE/3],xatr([1000,2000],[100,300]))

    def test_xatr1(self):
        self.assertEquals(0,xatr1([],[],[]))
        self.assertEquals(2*CBASE,xatr1([200],[100],[100]))        
        self.assertEquals(20*CBASE/3,xatr1([1000,2000],[100,300],[10000000,0]))


    def test_sdiff(self):
        self.assertEquals([],sdiff([],[]))
        self.assertEquals([101,2],sdiff([111,12],[10,10]))
    
    def test_rsdiff(self):
        self.assertEquals([],rsdiff([],[],10))
        self.assertEquals([106,2],rsdiff([111,12],[5,10],0))
        self.assertEquals([106,7],rsdiff([111,12],[5,10],1))
        self.assertEquals([106,7],rsdiff([111,12],[5,10],2))


    def test_accumulate(self):
        self.assertEquals([],accumulate([]))
        self.assertEquals([1,11,111],accumulate([1,10,100]))

    def test_accumulate1(self):
        self.assertEquals(0,accumulate1([],[]))
        self.assertEquals(100,accumulate1([100],[0]))
        self.assertEquals(300,accumulate1([100,200],[100,0]))

    def test_ma(self):
        self.assertEquals([],ma([],3))
        a= [1,2,3,4,5,6,7,8,9,0]
        self.assertEquals([0,0,2,3,4,5,6,7,8,6],ma(a,3))

    def test_ma1(self):
        self.assertEquals(0,ma1([],3,[]))
        a= [1,2,3,4,5,6,7,8,9,0]
        t = [0,0,2,3,4,5,6,7,8,0]
        self.assertEquals(6,ma1(a,3,t))
        self.assertEquals(6,t[-1])

    def test_strend2(self):
        self.assertEquals([],strend2([]))
        self.assertEquals([0],strend2([1]))        
        source = [10,20,30,30,40,50,40,30,20,20,10,20]
        self.assertEquals([0,1,2,3,4,5,-1,-2,-3,-4,-5,1],strend2(source))

    def test_strend2_1(self):
        self.assertEquals(0,strend2_1([],[]))
        self.assertEquals(0,strend2_1([1],[0]))        
        source = [10,20,30,30,40,50,40,30,20,20,10,20]
        target = [0,1,2,3,4,5,-1,-2,-3,-4,-5,0]
        self.assertEquals(1,strend2_1(source,target))
        self.assertEquals(1,target[-1])


if __name__ == "__main__":
    import logging
    logging.basicConfig(filename="test.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    
    unittest.main()
