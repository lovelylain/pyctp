#-*- coding:utf-8 -*-

'''
主执行文件
    以后考虑把MAX_VOLUME和STRATEGY配置移到配置文件中
'''

from base import *
from strategy import *

#设定合约的策略

#[总最大持仓量,策略1,策略2...]
STRATEGY = {
        'IF1104':(  1,#总最大持仓量=1
                    STRATEGY(opener=day_long_break,
                            closer=datr_long_stoper,
                            open_volume=1,
                            max_holding=1),
                    STRATEGY(opener=day_short_break,
                            closer=datr_short_stoper,
                            open_volume=1,
                            max_holding=1),
                )
        }

#####
import agent

def main():
    pass


if __name__=="__main__":
    main()
