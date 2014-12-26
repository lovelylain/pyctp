# -*- coding:utf-8 -*-

import unittest
import logging

from ..common.base import TEST_PATH
from ..common.controller import Controller
from ..trader.coordinator import CashCoordinator
from ..test.test_environ import prepare_environ


class CashCoordinatorTestCase(unittest.TestCase):
    def test_base(self):
        env = prepare_environ()
        ccoordinator = CashCoordinator(env,30)
        self.assertEqual(30,ccoordinator.shares)
        self.assertEqual(0,ccoordinator.balance)
        ccoordinator.balance = 100
        self.assertEqual(1000000,ccoordinator.available_balance)
        self.assertEqual(ccoordinator.balance,ccoordinator.available_balance) #注意,只有计算之后才相等
        ccoordinator2 = CashCoordinator(env,70)
        self.assertEqual(300000,ccoordinator.available_balance)
        self.assertEqual(ccoordinator.balance,ccoordinator.available_balance) #注意,只有计算之后才相等
        env.get_account().api.exchange.finalize()

    def test_update(self):
        env = prepare_environ()
        ccoordinator = CashCoordinator(env,30)
        self.assertEqual(30,ccoordinator.shares)
        self.assertEqual(0,ccoordinator.balance)
        ccoordinator.balance = 10000
        ccoordinator.kv_update([("balance",10000)])
        self.assertEqual(30,ccoordinator.shares)
        self.assertEqual(10000,ccoordinator.balance)
        ccoordinator.kv_update([("shares",1)])
        self.assertEqual(1,ccoordinator.shares)
        self.assertEqual(10000,ccoordinator.balance)
        env.get_account().api.exchange.finalize()
        ccoordinator.kv_update([("shares",-1),("balance",10001)])
        self.assertEqual(10001,ccoordinator.balance)
        self.assertRaises(AttributeError,getattr,ccoordinator,"share")


if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_coordinator.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()

