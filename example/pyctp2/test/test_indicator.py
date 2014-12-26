# -*- coding:utf-8 -*-

import unittest

from ..common.indicator import (soft_hash,
                                soft_hash1,
                                Indicator,
                )


class SoftHashTest(unittest.TestCase):
    def test_soft_hash1(self):
        a = [1,2,3]
        self.assertEqual(id(a),soft_hash1(a))
        self.assertEqual(hash((1,2,3)),soft_hash1((1,2,3)))
        self.assertEqual(hash(123),soft_hash1(123))
        self.assertEqual(hash("123"),soft_hash1("123"))

    def test_soft_hash(self):   #测试通道
        a=[1,2,3]
        b="123"
        c=(1,2,3)
        d=123
        self.assertTrue(soft_hash([a,b,c,d]))

class ParameterizedCachedTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_check(self):
        class TIndicatorA(Indicator):
            def __init__(self,x,y):
                self.num = 0
            def calc(self,x,y):
                self.num += 1
                return self
        pa = [1,2,3,4]
        ta = TIndicatorA(10,pa)
        self.assertEqual(1,ta.num)
        tb = TIndicatorA(10,pa)
        self.assertEqual(2,ta.num)
        self.assertEqual(id(ta),id(tb))
        TIndicatorA(10,pa)
        self.assertEqual(3,ta.num)
        td = TIndicatorA(11,pa)
        self.assertEqual(3,ta.num)
        self.assertNotEqual(id(ta),id(td))
        pa.append(5)
        te = TIndicatorA(10,pa)
        self.assertEqual(4,ta.num)
        self.assertEqual(id(ta),id(te))

