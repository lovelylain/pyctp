# -*- coding: utf8 -*-

import logging
import math

from base import *
from strategy import *
import dac

'''
为保证atrd1的准确性，必须用手工连续的最长历史数据来计算月数据
'''

class min_long_break(LONG_BREAK):#每分钟触发
    def check(self,data,ctick):
        #print u'in check,%s:%s' % (ctick.min1,ctick.sec)
        logging.info(u'in check,%s:%s:%s' % (ctick.min1,ctick.sec,ctick.msec))
        print u'in min_long_break : %s' % (ctick.time)
        #if ctick.min1 % 100 == 30 and ctick.sec>58 and ctick.msec==0:
        if ctick.sec <= 3:#and ctick.msec ==0:
            logging.info(u'S:min_long_break:发出多头信号=%s:%s %s' % (ctick.min1,ctick.sec,ctick.msec))
            return (True,0)
        return (False,0)

class day_long_stoper_35(LONG_STOPER):#触发后当分钟结束平仓
    def check(self,ctick):
        print 'DLS35A:ctick.min1 = %s' % (ctick.min1,)
        #print u'in check,%s:%s:%s' % (ctick.min1,ctick.sec,ctick.msec)
        #if ctick.min1 % 100 == 30 and ctick.sec>58 and ctick.msec==0:
        if ctick.sec==59 or ctick.min1>1500:# and ctick.msec ==0:
            print u'S:day_long_stoper_35:发出多头平仓信号=%s:%s %s' % (ctick.min1,ctick.sec,ctick.msec)
            logging.info(u'S:day_long_stoper_35:发出多头平仓信号=%s:%s %s' % (ctick.min1,ctick.sec,ctick.msec))
            return (True,ctick.low,False)
        return (False,0,False)


class lgap(LONG_BREAK): #
    '''
        向下缺口后回升
    '''
    def __init__(self):
        super(lgap,self).__init__()
        self.itick = 0
        self.last_signal = 0

    def dresume(self,data,ibegin):
        #无现场，不需要恢复. 其实因为有D1限制，还是需要判断当日有没有出现过信号
        #TODO
        pass

    def check(self,data,ctick):
        self.itick += 1
        opend = data.cur_day.vopen
        ldlow = data.d1[ILOW][-1] if data.d1[ILOW] else data.cur_day.vopen * 99/100 #如果有昨日数据，则ldlow为昨日最低点，否则为今日开盘*99%

        if opend > ldlow:            #无向下跳空
            return (False,0)

        bline = ldlow + 2

        signal = data.shigh[-1] <= bline and ctick.price > bline
        my_signal = (signal
                and ctick.min1 < 1430
            )
        if my_signal and ctick.date != self.last_signal: #同一天只取一次
            logging.info(u'发出信号:%s:%s:%s:%s,ldlow=%s,xatr1[-1]=%s' % ('lgap',ctick.time,ctick.sec,ctick.price,ldlow,data.xatr1[-1]))
            self.last_signal = ctick.date
            return (True,bline)
        return (False,0)

class hgap(SHORT_BREAK): #
    '''
        向上缺口后下跌
    '''
    def __init__(self):
        super(hgap,self).__init__()
        self.itick = 0
        self.last_signal = 0

    def dresume(self,data,ibegin):
        #无现场，不需要恢复.
        pass

    def check(self,data,ctick):
        self.itick += 1
        opend = data.cur_day.vopen
        ldhigh = data.d1[IHIGH][-1]    #昨日最低

        if opend < ldhigh:            #无向上跳空
            return (False,0)

        bline = ldhigh - 2

        signal = data.slow[-1] >= bline and ctick.price < bline
        my_signal = (signal
                and ctick.min1 > 915
                and ctick.min1 < 1445
            )
        if my_signal and ctick.min1 != self.last_signal: #同一分钟信号不重发
            logging.info(u'发出信号:%s:%s:%s:%s,ldhigh=%s' % ('lgap',ctick.time,ctick.sec,ctick.price,ldhigh))
            self.last_signal = ctick.min1
            return (True,bline)
        return (False,0)



