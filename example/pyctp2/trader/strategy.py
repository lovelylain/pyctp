'''
    理想的策略形式
    交易端须获取所跟进的合约的当日涨跌停位置
'''

import json
import logging

from ..common.base import BaseObject,inverse_direction

from .position import (POSITION_APPROVE_STATUS,
                       Position,
                       Closer,ContractCloser,GlobalCloser,
                    )



class POPEN(object):
    """
        数据对象
    """
    def __init__(self,contract,base_price,direction,closers,extra_hops=30):
        self.contract = contract
        self.base_price = base_price
        self.direction = direction
        self.closers = closers
        self.extra_hops = extra_hops
        self.unit = 1
        self.planned = 0

class PCLOSE(object):
    """
        根据Position来平仓
    """
    def __init__(self,position,base_price,volume,extra_hops=30):
        self.position = position
        self.base_price = base_price
        self.unit = volume      #全部成功或失败
        self.planned = volume
        self.extra_hops = extra_hops

    @property
    def contract(self):
        return self.position.contract

    @property
    def direction(self):
        return inverse_direction(self.position.direction)



class PCLOSE2(object):
    """
        根据合约来平仓. 故需要在所有position中按规定次序遍历
    """
    def __init__(self,contract,base_price,direction,volume,extra_hops=30):
        self.contract = contract
        self.base_price = base_price
        self.direction = direction
        self.extra_hops = extra_hops
        self.volume = volume


class BaseStrategy(object):
    def __init__(self,holder):
        self._holder = holder

    @classmethod
    def sname(cls):
        return cls.__name__

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def available_balance(self):
        return self._holder.available_balance

    def prepare(self,ctick,*args):
        '''子类只在必要时实现, 用于在check_open/close之前处理共同计算
        '''
        pass

    def check_open(self,ctick,*contracts):
        ''' 子类必须实现
            针对行情的open check  
            返回值为 instrs 和对应的closer
        '''
        raise NotImplementedError()

    def on_approved(self,command,astate):
        """
            子类挂接点
        """
        pass

    def on_reject(self,command):
        """
            供子类挂接
        """
        pass


    def on_done(self,command):
        """
            供子类挂接
        """
        pass

    def on_progress(self,command):
        """
            供子类挂接
        """
        pass

    def day_finalize(self):
        """
            供子类挂接
        """
        pass