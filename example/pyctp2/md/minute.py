# -*- coding:utf-8 -*-

from ..common.base import BaseObject,DAY_FINALIZE_TICK
from ..core.dac import MINUTE

class Minutes(MINUTE):
    pass
    #def day_finalize(self):
    #    self._next_is_new_day = True


class Minutes_Previous(object):
    """
        #deprecated #2014-8-18日以前的版本
        被SaveAgent每日初始化时创建新的Minute
        故DayFinalize后的状态不重要

        不从Indicator继承, 否则每次得到同一个对象, 需要手工清除数据
    """
    def __init__(self,contract):
        self._contract = contract
        self._cur = BaseObject(sdate=-1,stime=-1,sopen=0,shigh=0,slow=0,sclose=0,
                              svolume=0,samount=0,sholding=0,sdvolume=0,sdamount=0
        )
        self._next_is_new_day = True
        self._minutes = []

    def new_tick(self,ctick):
        '''
            返回是否完成新的分钟数据的标志:
            True: 已完成新分钟数据
            False: 分钟持续中或未创建(换日第一秒)
        '''
        #print('in minute,ctick=%s,ctick.min1=%s,self.cur.stime=%s' % (ctick.time,ctick.min1,self.cur.stime))
        if ctick.min1 > self._cur.stime or ctick.date >self._cur.sdate:
            spre = self._cur
            self._cur = BaseObject(sdate=ctick.date,stime=ctick.min1,
                                  sopen=ctick.price,sclose=ctick.price,shigh=ctick.price,slow=ctick.price,
                                  svolume=0,
                                  samount = 0,
                                  sholding=ctick.holding,
                                  sdvolume = ctick.dvolume, #初始的dvolume,00:00的成交量归于上一分钟,价格归于当分钟.但这个不重要
                                  sdamount = ctick.damount,
                                )
            if self._next_is_new_day:    #每日第一秒
                self._minutes = []
                self._next_is_new_day = False
                self._cur.sdvolume = 0   #第一秒归于当日. 否则当日成交量就少了这一秒
                self._cur.sdamount = 0
                return False
            else:
                #if ctick.dvolume - spre.sdvolume > spre.svolume:
                if ctick.price > 0:#非DAY_FINAL情况
                    spre.svolume = ctick.dvolume - spre.sdvolume
                    spre.samount = ctick.damount - spre.sdamount
                self._minutes.append(spre)
                print('minute switch,contract=%s,minute=%s,spre.svolume=%s,ctick.dvolume=%s' % (ctick.instrument,spre.stime,spre.svolume,ctick.dvolume))
                return True
        else:   #未切换
            scur = self._cur
            scur.sclose = ctick.price
            scur.holding = ctick.holding
            scur.svolume = ctick.dvolume - scur.sdvolume
            scur.samount = ctick.damount - scur.sdamount
            if ctick.price > scur.shigh:
                scur.shigh = ctick.price
            elif ctick.price < scur.slow:
                scur.slow = ctick.price
            return False

    def day_finalize(self):
        self.new_tick(DAY_FINALIZE_TICK)
        self._next_is_new_day = True

    def get_minutes(self):
        return self._minutes

    def get_day(self):
        if not self._minutes:
            return BaseObject(sdate=0,sopen=0,sclose=0,shigh=0,slow=0,svolume=0,samount=0,sholding=0)
        shigh = 0
        slow = 99999999
        for minute in self._minutes:
            if minute.shigh > shigh:
                shigh = minute.shigh
            if minute.slow < slow:
                slow = minute.slow
        day = BaseObject(sdate=self._minutes[0].sdate,sopen=self._minutes[0].sopen,sclose=self._minutes[-1].sclose,
                         shigh = shigh,slow = slow,
                         svolume = self._minutes[-1].sdvolume,
                         samount = self._minutes[-1].sdamount,
                         sholding=self._minutes[-1].sholding)
        return day

