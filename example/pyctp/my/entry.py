#-*- coding:utf-8 -*-

from base import *
import ctp_mock
import agent


'''
    行情保存
    使用demo的配置文件
    其中demo_base_ini       配置相关的服务器地址和口令
        demo_strategy.ini   配置须保存ticks的合约
'''
def save_demo():
    return agent.save_raw(base_name='demo_base.ini',base='Base',strategy_name='demo_strategy.ini')


def trade_demo():
    '''
        请先在demo_base.ini中的[REAL_TRADER]下设定相关细节
    '''
    return ctp_mock.comp_real2(base_name='demo_base.ini',base='Base_Real',strategy_name='demo_strategy_trade.ini')

def trade_mock(t2order = t2order_mock):
    '''
        交易时间请使用trade_mock(t2order=entry.t2order_if)
    '''
    return ctp_mock.comp_real2(base_name='demo_base.ini',base='Base_Mock',strategy_name='demo_strategy_trade.ini',t2order=t2order)


