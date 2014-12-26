# -*- coding:utf-8 -*-
"""
    测试集中
    所有需要测试的TestCase, 均须导入到此

    运行方法:
    在 ..\..路径下,即quant\下
    A1:
    python -m unittest -b pyctp2.test.a_test_suite
    #ipython3 -m unittest -b pyctp2.test.a_test_suite #速度略慢
    -b选项是为了抑制将logging信息输出到控制台

    #
    A2:
    python -m unittest
    则会默认搜索执行目录下所有的test. 因为本suite的名字改为a_开头,所以不会被搜集到testcase中
    如果仍然是test_开头,则收录到本suite的测试用例在这个命令下会被执行两边

    B: 推荐用法
    python -m pyctp2.test.a_test_suite
    这样的好处是 可以通过basicConfig指定 将logging信息输出到文件.

"""

import logging
import unittest

from ..common.base import TEST_PATH

##测试集合
from .test_contract_type import (ContractManagerTest,
                                 ContractInfoTest,
                                 ModuleTest as CT_ModuleTest,
                                )

from .test_controller import SyncLastMapTestCase

from .test_coordinator import CoordinatorTestCase
from .test_cash_coordinator import CashCoordinatorTestCase

from .test_dac import ModuleTest as DAC_ModuleTest

from .test_environ import EnvironTestCase

from .test_indicator import (ParameterizedCachedTest,
                             SoftHashTest,
                            )

from .test_position import (OrderTestCase,
                            CloserTestCase,
                            ContractCloserTestCase,
                            GlobalCloserTestCase,
                            PositionTestCase,
                            PosInfoTestCase,
                            PositionHolderTestCase,
                        )

from .test_strategy_agent import StrategyAgentTestCase

from .test_trade_matcher import TradeMatchTestCase

from .test_utils import (TListTest,
                         ArgsCacheTestCase,
                         UpdateableTestCase,
                         ModuleTest as Utils_ModuleTest,
                        )

from .test_wrapper import TraderSpiTestCase

from .test_macro_command_queue import (MacroCommandTestCase,
                                       DeferCommandTestCase,
                                       DeferTradeCommandTestCase,
                                       BaseMacroCommandQueueTestCase,
                                       PassiveMacroCommandQueueTestCase,
                                       MacroCommandQueueTestCase,
                                       SecMacroCommandQueueTestCase,
                                       TickMacroCommandQueueTestCase,
                        )


#集成测试?
from .test_builder import CommonBuilderTestCase
#from .test_player import Player1TestCase

if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_suite.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()
