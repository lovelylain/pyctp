# -*- coding: utf-8 -*-

import unittest

from hreader import *

class PREPARER_INST_Test(unittest.TestCase):
    def test_pd(self):
        xtimes = [1,2,3,4,5,270,2,3,2,1,2,270,3]
        self.assertEquals([],PREPARER_INST.pd([]))
        self.assertEquals([(0,5),(6,11)],PREPARER_INST.pd(xtimes))

    def test_p3(self):
        self.assertEquals([],PREPARER_INST.p3([]))
        self.assertEquals([(3,5),(6,8),(9,11),(12,14)],PREPARER_INST.p3(range(0,15)))
        self.assertEquals([(3,5),(6,9),(10,12),(13,15),(16,18)],PREPARER_INST.p3(range(0,8)+range(265,270)+range(0,8)))        
        self.assertEquals([(3,5),(6,8),(9,11),(12,14)],PREPARER_INST.p3(range(39,46)+range(46,54)))

    def test_p5(self):
        self.assertEquals([],PREPARER_INST.p5([]))
        self.assertEquals([(5,9),(10,14)],PREPARER_INST.p5(range(0,15)))
        self.assertEquals([(5,12),(13,17)],PREPARER_INST.p5(range(0,8)+range(265,270)+range(0,8)))        
        self.assertEquals([(0,5),(6,10)],PREPARER_INST.p5(range(39,46)+range(46,54)))
        self.assertEquals([(0,5),(6,10)],PREPARER_INST.p5(range(39,46)+range(46,51)))

    def test_p15(self):
        self.assertEquals([],PREPARER_INST.p15([]))
        self.assertEquals([(15,29),(30,44)],PREPARER_INST.p15(range(0,46)))
        self.assertEquals([(15,29),(30,35),(36,50),(51,65)],PREPARER_INST.p15(range(0,31)+range(265,270)+range(0,31)))        
        self.assertEquals([(4,18),(19,33)],PREPARER_INST.p15(range(26,46)+range(46,64)))
        self.assertEquals([(4,18),(19,33)],PREPARER_INST.p15(range(26,46)+range(46,61)))

    def test_p30(self):
        self.assertEquals([],PREPARER_INST.p30([]))
        self.assertEquals([(30,59),(60,89),(90,119)],PREPARER_INST.p30(range(0,46)+range(46,106)+range(106,126)))
        self.assertEquals([(30,59),(60,89),(90,135)],PREPARER_INST.p30(range(0,46)+range(46,106)+range(0,46))) 
        self.assertEquals([(30,59),(60,89),(90,119)],PREPARER_INST.p30(range(0,46)+range(46,106)+range(106,121)))


if __name__ == "__main__":
    import logging
    logging.basicConfig(filename="test.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    
    unittest.main()

