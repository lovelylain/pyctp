# -*- coding:utf-8 -*-

import unittest
import logging
import time

from ..common.utils import (
                    next_minute,
                    pre_day,
                    next_day,
                    next_trading_day,
                    weekday,
                    second2time,
                    TList,
                    ArgsCached,
                    Updateable,
                    with_metaclass
                )

from ..common.base import TEST_PATH

class ModuleTest(unittest.TestCase):
    def test_next_minute(self):
        self.assertEqual(900,next_minute(859))
        self.assertEqual(859,next_minute(858))
        self.assertEqual(802,next_minute(801))
        self.assertEqual(1900,next_minute(1859))

    def test_pre_day(self):
        self.assertEqual(20140601,pre_day(20140602))
        self.assertEqual(20140531,pre_day(20140601))
        self.assertEqual(20140430,pre_day(20140501))

    def test_next_day(self):
        self.assertEqual(20140603,next_day(20140602))
        self.assertEqual(20140601,next_day(20140531))
        self.assertEqual(20140501,next_day(20140430))
        self.assertRaises(ValueError,next_day,20140431)

    def test_next_trading_day(self):
        self.assertEqual(20140603,next_trading_day(20140602))
        self.assertEqual(20140602,next_trading_day(20140531))
        self.assertEqual(20140602,next_trading_day(20140530))
        self.assertEqual(20140530,next_trading_day(20140529))
        self.assertEqual(20140501,next_trading_day(20140430))


    def test_day2week(self):
        self.assertEqual(1,weekday(20140602))
        self.assertEqual(7,weekday(20140601))
        self.assertEqual(6,weekday(20140531))
        self.assertEqual(2,weekday(20140603))
        self.assertEqual(3,weekday(20140604))
        self.assertEqual(4,weekday(20140605))
        self.assertEqual(5,weekday(20140606))
        self.assertEqual(6,weekday(20140607))
        self.assertEqual(7,weekday(20140608))
        self.assertEqual(1,weekday(20140609))

    def test_second2time(self):
        t1 = time.time()
        t2 = int(time.strftime('%Y%m%d%H%M%S',time.localtime()))
        #print(t1,second2time(t2))
        self.assertTrue(abs(t1 - second2time(t2))<2)


class TListTest(unittest.TestCase):
    def test_normal(self):
        a= TList()
        self.assertEqual(0,len(a))
        b=TList([1,2,3])
        self.assertEqual([1,2,3],b)
        b.remove_all()
        self.assertEqual(0,len(b))

    def test_register(self):
        a=TList()
        xa = 0
        class MyReceiver(object):
            def notify_truncated(self,truncated_size):
                nonlocal xa
                xa += truncated_size
        self.assertEqual(0,len(a._receivers))
        ra = MyReceiver()
        rb = MyReceiver()
        rc = MyReceiver()
        a.register(ra)
        self.assertEqual(1,len(a._receivers))
        a.register(rb)
        self.assertEqual(2,len(a._receivers))
        a.register(ra)
        self.assertEqual(2,len(a._receivers))
        a.unregister(ra)
        self.assertEqual(1,len(a._receivers))
        a.register(rc)
        self.assertEqual(2,len(a._receivers))
        a[0:0] = [1,2,3,4]
        self.assertEqual(4,len(a))
        a.remove_all()
        self.assertEqual(8,xa)
        a[0:0] = [1,2,3,4]
        xa = 0
        a.remove_head(2)
        self.assertEqual(4,xa)

class ArgsCacheTestCase(unittest.TestCase):
    def setUp(self):
        @with_metaclass(ArgsCached)
        class A:
            _cached_args = ["name"]
            def __init__(self,name="name1",other="other1"):
                self.name = name
                self.other = other
        self.A = A
        @with_metaclass(ArgsCached)
        class A1:
            _cached_args = ["name"]
            def __init__(self,name,other="other1"):
                self.name = name
                self.other = other
        self.A1 = A1
        @with_metaclass(ArgsCached)
        class A2:
            _cached_args = ["name","other"]
            def __init__(self,name,other="other1"):
                self.name = name
                self.other = other
        self.A2 = A2


    def test_args1(self):
        a1 = self.A()
        a2 = self.A("name1")
        self.assertEqual(a1,a2)
        a3 = self.A(name="name1")
        self.assertEqual(a1,a3)
        a4 = self.A(other="other1")
        self.assertEqual(a1,a4)
        a5 = self.A(other="other2")
        self.assertEqual(a1,a5)
        a6 = self.A(name="name2")
        self.assertNotEqual(a1,a6)

    def test_args11(self):
        a1 = self.A1("name1")
        a2 = self.A1(name="name1")
        self.assertEqual(a1,a2)
        a3 = self.A1(name="name1")
        self.assertEqual(a1,a3)
        a4 = self.A1("name1",other="other1")
        self.assertEqual(a1,a4)
        a5 = self.A1("name1",other="other2")
        self.assertEqual(a1,a5)
        a6 = self.A1(name="name2")
        self.assertNotEqual(a1,a6)
        a7 = self.A1("name2")
        self.assertEqual(a6,a7)

    def test_args2(self):
        a1 = self.A2("name1")
        a2 = self.A2(name="name1")
        self.assertEqual(a1,a2)
        a3 = self.A2(name="name1")
        self.assertEqual(a1,a3)
        a4 = self.A2("name1",other="other1")
        self.assertEqual(a1,a4)
        a5 = self.A2("name1",other="other2")
        self.assertNotEqual(a1,a5)
        a6 = self.A2(name="name2")
        self.assertNotEqual(a1,a6)
        a7 = self.A2("name2")
        self.assertEqual(a6,a7)
        a8 = self.A2("name2","other1")
        self.assertEqual(a7,a8)
        a9 = self.A2("name2","other2")
        self.assertNotEqual(a8,a9)


class UpdateableTestCase(unittest.TestCase):
    def test_base(self):
        class T(Updateable):
            def __init__(self,x,y):
                self.x = x
                self.y = y
        t = T(100,200)
        self.assertEqual(100,t.x)
        self.assertEqual(200,t.y)
        t.kv_update([("x",101),("y",102)])
        self.assertEqual(101,t.x)
        self.assertEqual(102,t.y)
        t.kv_update([("z",222),("x",111),("y",112)])        #z不存在,故会在logging中有一条记录
        self.assertEqual(111,t.x)
        self.assertEqual(112,t.y)
        self.assertRaises(AttributeError,getattr,t,"z")


if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_utils.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()
