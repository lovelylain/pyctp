# -*-coding:utf-8 -*-

"""
    @deprecated
    不适合作为单元测试
    合并到player的main()中
    改名为xtest_XXXX， 避免被 -m unittest执行时，导入，进而导入Player而出现紊乱
"""



#常规导入
import unittest
import logging

#测试目标
from ..simulator.player import Player

#功能文件
from ..trader.coordinator import Coordinator
from ..common.base import TEST_PATH
from ..common.contract_type import ContractManager,M
from ..common.utils import ArgsCached

#测试夹具
from ..test.a_strategy import SExampleA

#更改路径
from ..common import base

base.DATA_PATH = base.TEST_DATA_PATH

#实质上不应该是单元测试,因为起了多条线程,没有办法合适退出

class Player1TestCase(unittest.TestCase):
    def setUp(self):
        #ArgsCached._args2obj.clear()
        pass

    def tearDown(self):
        ArgsCached._args2obj.clear()

    def _testOK_1(self):
        """
           不在 python -m unittest中执行
        """
        cm1 = ContractManager([M])
        triples = [ (Coordinator,SExampleA,cm1),
                    #(Coordinator,SExampleAB,cm1),
                ]
        player = Player(triples)
        player.prepare(20140925)
        player.play(20141009)
        #self.assertTrue(True)



if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_player.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()