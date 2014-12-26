# -*- coding:utf-8 -*-

#常规导入
import logging
import unittest
import unittest.mock as mock
import time

#测试目标
from ..common.macro_command_queue import (
                                MacroCommand,
                                DeferCommand,
                                DeferTradeCommand,
                                BaseMacroCommandQueue,
                                MacroCommandQueue,
                                PassiveMacroCommandQueue,
                                SecMacroCommandQueue,
                                TickMacroCommandQueue,
                                TERMINAL_COMMAND,
                            )

#测试夹具
from ..common.base import BaseObject


class MacroCommandTestCase(unittest.TestCase):
    def test_cmp(self):
        mc1 = MacroCommand(None,None,20140101001)
        mc2 = MacroCommand(None,None,20140101002)
        self.assertTrue(mc1<mc2)
        self.assertTrue(mc2>mc1)
        self.assertFalse(mc1==mc2)
        mc3 = MacroCommand(None,1,20140101002)
        self.assertTrue(mc2==mc3)

    def test_check2exec(self):
        func = mock.Mock()
        mc1 = MacroCommand(func,None,20140101001)
        self.assertEqual(mc1.trigger_time,20140101001)
        self.assertFalse(mc1.check2exec(20140101))
        self.assertFalse(func.called)
        self.assertTrue(mc1.check2exec(20140101001))
        self.assertTrue(func.called)
        func.reset_mock()
        self.assertFalse(func.called)
        self.assertTrue(mc1.check2exec(20140101002))
        self.assertTrue(func.called)


class DeferCommandTestCase(unittest.TestCase):
    def test_init(self):
        func = mock.Mock()
        mc1 = DeferCommand(func,10000)

    def test_check2exec(self):
        func = mock.Mock()
        mc1 = DeferCommand(func,10000)
        self.assertFalse(mc1.check2exec(time.time()+1000))
        self.assertFalse(func.called)
        self.assertTrue(mc1.check2exec(time.time()+10001))
        self.assertTrue(func.called)
        func.reset_mock()
        self.assertFalse(func.called)
        self.assertTrue(mc1.check2exec(time.time()+10001))
        self.assertTrue(func.called)


class DeferTradeCommandTestCase(unittest.TestCase):
    def test_init(self):
        queue = mock.Mock()
        cmd = mock.Mock()
        mc1 = DeferTradeCommand(queue,cmd,1000)

    def test_put2trade_queue(self):
        queue = mock.Mock()
        cmd = mock.Mock()
        mc1 = DeferTradeCommand(queue,cmd,1000)
        mc1._put2trade_queue()
        queue.put_command.assert_called_once_with(cmd)

    def test_lt(self):
        queue = mock.Mock()
        cmd1 = BaseObject(priority=1)
        cmd2 = BaseObject(priority=2)
        dtc1 = DeferTradeCommand(queue,cmd1,1000)
        dtc3 = DeferTradeCommand(queue,cmd2,1000)   #这里有微妙的跨越点
        dtc4 = DeferTradeCommand(queue,cmd1,1000)
        dtc2 = DeferTradeCommand(queue,cmd1,1001)
        self.assertTrue(dtc1<dtc2)
        self.assertTrue(dtc1<dtc3)
        self.assertFalse(dtc1<dtc4)

    def test_gt(self):
        queue = mock.Mock()
        cmd1 = BaseObject(priority=1)
        cmd2 = BaseObject(priority=2)
        dtc1 = DeferTradeCommand(queue,cmd1,1000)
        dtc3 = DeferTradeCommand(queue,cmd2,1000)   #这里有微妙的跨越点
        dtc4 = DeferTradeCommand(queue,cmd1,1000)
        dtc2 = DeferTradeCommand(queue,cmd1,1001)
        self.assertTrue(dtc2>dtc1)
        self.assertTrue(dtc3>dtc1)
        self.assertFalse(dtc4>dtc1)


class BaseMacroCommandQueueTestCase(unittest.TestCase):
    def test_init(self):
        bmcq = BaseMacroCommandQueue()
        bmcq.start()
        self.assertTrue(True)

    def test_put_command(self):
        bmcq = BaseMacroCommandQueue()
        bmcq.start()
        cmd = MacroCommand(None,None,time.time())
        bmcq.put_command(cmd)
        self.assertEqual(1,len(bmcq._cqueue))
        bmcq.put_command(cmd)
        self.assertEqual(2,len(bmcq._cqueue))

    def test_trigger(self):
        bmcq = BaseMacroCommandQueue()
        bmcq.start()
        bmcq.trigger()

    def test_exec(self):
        bmcq = BaseMacroCommandQueue()
        bmcq.start()
        cmd1 = mock.Mock()
        cmd2 = mock.Mock()
        cmd3 = mock.Mock()

        ctime = time.time()
        mc1 = MacroCommand(cmd1,None,ctime+1000)
        mc2 = MacroCommand(cmd2,None,ctime+1001)
        mc3 = MacroCommand(cmd3,None,ctime+5003)
        bmcq.put_command(mc1)
        bmcq.put_command(mc2)
        bmcq.put_command(mc3)
        ftime = lambda : ctime+1000
        bmcq._time_func = ftime
        self.assertTrue(bmcq._exec())
        self.assertTrue(cmd1.called)
        self.assertFalse(cmd2.called)
        self.assertFalse(cmd3.called)
        cmd1.reset_mock()
        self.assertFalse(cmd1.called)
        self.assertEqual(2,len(bmcq._cqueue))
        ftime2 = lambda : ctime+6000
        bmcq._time_func = ftime2
        self.assertTrue(bmcq._exec())
        self.assertFalse(cmd1.called)
        self.assertTrue(cmd2.called)
        self.assertTrue(cmd3.called)
        self.assertEqual(0,len(bmcq._cqueue))
        cmd2.reset_mock()
        cmd3.reset_mock()
        bmcq.put_command(mc1)
        bmcq.put_command(mc2)
        bmcq.put_command(mc3)
        bmcq.put_command(TERMINAL_COMMAND)
        ftime = lambda : ctime+1000
        bmcq._time_func = ftime
        self.assertTrue(bmcq._exec())
        ftime = lambda : ctime+2000
        bmcq._time_func = ftime
        self.assertTrue(bmcq._exec())
        ftime = lambda : ctime+6000
        bmcq._time_func = ftime
        self.assertFalse(bmcq._exec())
        self.assertEqual(0,len(bmcq._cqueue))


class PassiveMacroCommandQueueTestCase(unittest.TestCase):
    def test_exec(self):
        #print("in PassiveMacroCommandQueue Test")
        pmcq = PassiveMacroCommandQueue()
        pmcq.start()
        cmd1 = mock.Mock()
        cmd2 = mock.Mock()
        cmd3 = mock.Mock()

        mc1 = MacroCommand(cmd1,None,1000)
        mc2 = MacroCommand(cmd2,None,1001)
        mc3 = MacroCommand(cmd3,None,5003)
        pmcq.put_command(mc1)
        pmcq.put_command(mc2)
        pmcq.put_command(mc3)

        pmcq.trigger(0)     #用time.time(),则全部激活
        self.assertTrue(cmd1.called)
        self.assertTrue(cmd2.called)
        self.assertTrue(cmd3.called)
        #
        cmd1.reset_mock()
        cmd2.reset_mock()
        cmd3.reset_mock()
        pmcq.put_command(mc1)
        pmcq.put_command(mc2)
        pmcq.put_command(mc3)
        pmcq.trigger(1)
        self.assertFalse(cmd1.called)
        self.assertFalse(cmd2.called)
        self.assertFalse(cmd3.called)
        self.assertEqual(3,len(pmcq._cqueue))
        pmcq.trigger(1000)
        self.assertTrue(cmd1.called)
        self.assertFalse(cmd2.called)
        self.assertFalse(cmd3.called)
        self.assertEqual(2,len(pmcq._cqueue))
        pmcq.trigger(5003)
        self.assertTrue(cmd2.called)
        self.assertTrue(cmd3.called)
        self.assertEqual(0,len(pmcq._cqueue))

        #print("end PassiveMacroCommandQueue Test")

class MacroCommandQueueTestCase(unittest.TestCase):
    def test_exec(self):
        mcq = MacroCommandQueue(interval=0.01)
        mcq.start()
        cmd1 = mock.Mock()
        mc1 = MacroCommand(cmd1,None,time.time()+0.02)
        mcq.put_command(mc1)
        mcq.trigger()
        mcq.put_command(TERMINAL_COMMAND)
        mcq.trigger(1000)


class SecMacroCommandQueueTestCase(unittest.TestCase):
    def test_exec(self):
        mcq = SecMacroCommandQueue(interval=0.01)
        mcq.start()
        cmd1 = mock.Mock()
        mc1 = MacroCommand(cmd1,None,time.time()+0.02)
        mcq.put_command(mc1)
        mcq.put_command(TERMINAL_COMMAND)


class TickMacroCommandQueueTestCase(unittest.TestCase):
    def test_exec(self):
        mcq = TickMacroCommandQueue()
        mcq.start()
        cmd1 = mock.Mock()
        mc1 = MacroCommand(cmd1,None,1001)
        mcq.put_command(mc1)
        mcq.put_command(TERMINAL_COMMAND)
        #print("##########################begin tick_macro_command_queue trigger")
        mcq.trigger(10)
        mcq.trigger(1000)
        mcq.trigger(1002)
        #print("##########################end tick_macro_command_queue trigger")
        time.sleep(0.01)    #等待线程完成操作
        self.assertEqual(0,len(mcq._cqueue))
