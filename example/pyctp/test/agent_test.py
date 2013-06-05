# -*-coding:utf-8 -*-

import unittest

from agent import *

class ModuleTest(unittest.TestCase):
    pass

class AbsAgentTest(unittest.TestCase):
    def test_inc_tick(self):
        xa = AbsAgent()
        self.assertEquals(1,xa.inc_tick())
        self.assertEquals(2,xa.inc_tick())

    def test_put_command(self):
        xa = AbsAgent()
        xa.put_command(100,None)
        self.assertEquals(1,len(xa.commands))
        self.assertEquals(100,xa.commands[0][0])
        xa.put_command(50,None)
        self.assertEquals(2,len(xa.commands))
        self.assertEquals(50,xa.commands[0][0])
        xa.put_command(75,None)
        self.assertEquals(3,len(xa.commands))
        self.assertEquals(50,xa.commands[0][0])
        self.assertEquals(75,xa.commands[1][0])
        self.assertEquals(100,xa.commands[2][0])

    def test_check_commands(self):
        xa = AbsAgent()
        xa.check_commands()
        self.gi = 100
        def command():
            self.gi += 1
        xa.put_command(3,command)
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(100,self.gi)
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(100,self.gi)
        self.assertEquals(1,len(xa.commands))
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(101,self.gi)
        self.assertEquals(0,len(xa.commands))
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(101,self.gi)  #不会重复计算

    def test_check_commands_2(self):
        #测试同一时刻的两个命令
        xa = AbsAgent()
        xa.check_commands()
        self.gi = 100
        def command():
            self.gi += 1
        xa.put_command(3,command)
        xa.put_command(3,command)
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(100,self.gi)
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(100,self.gi)
        self.assertEquals(2,len(xa.commands))
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(102,self.gi)
        self.assertEquals(0,len(xa.commands))
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(102,self.gi)  #不会重复计算

    def test_check_commands_2b(self):
        #测试不同时刻的两个命令
        xa = AbsAgent()
        xa.check_commands()
        self.gi = 100
        def command():
            self.gi += 1
        xa.put_command(2,command)
        xa.put_command(3,command)
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(2,len(xa.commands))
        self.assertEquals(100,self.gi)
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(1,len(xa.commands))
        self.assertEquals(101,self.gi)
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(102,self.gi)
        self.assertEquals(0,len(xa.commands))
        xa.inc_tick()
        xa.check_commands()
        self.assertEquals(102,self.gi)  #不会重复计算


if __name__ == "__main__":
    import logging
    logging.basicConfig(filename="test.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    
    unittest.main()
