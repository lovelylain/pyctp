# -*- coding: utf-8 -*-

'''
基于ticks的回测机制
使用方式:
In [1]: import bktest

In [2]: rtts = bktest.load_all(['IF1206','IF1207'])

In [3]: ss = bktest.cruiser1(rtts,[bktest.l_ema_sm])    #请将l_ema_sm更换成实际策略

In [4]: bktest.Trade.print_info(ss[0][1])

'''

import re
import os.path
import logging
import time


from base import *
import hreader
import strategy
from dac2 import *

LENGTH_THRESHOLD = 25000    #主力合约的ticks阈值超过


class TickAgent(object):#ticks数据管理,只管理一个合约,并最多测试一个Strategy
    def __init__(self,fname,data_path=hreader.DATA_PATH,pattern='\d{8}_tick.txt',tick_base=2):
        self.fname = fname
        self.data_path = data_path
        self.pattern = pattern
        self.rpattern = re.compile(pattern,re.IGNORECASE)
        self.mtickss = {}   #dict方式
        self.stickss = []   #顺序方式
        self.tick_base = 2  #最小行情单位
        #self.closers = []    #已经开仓后需要追踪的closer
        #self.trades = []

    def load(self):
        '''
            按顺序加载fname下的ticks数据.
            fname必须为IF1201这种格式
        '''
        sub_path = '%s%s' % (self.data_path,self.fname)
        tdates = sorted([int(os.path.splitext(name)[0][:8]) for name in os.listdir(sub_path) if self.rpattern.search(name) and name[0]!='.' and name[-1]!='~'])
        for tdate in tdates:
            cticks = hreader.read_ticks(self.fname,tdate)
            self.mtickss[tdate] = DTicks(self.fname,tdate,cticks)
            self.stickss.append(self.mtickss[tdate])

    def run(self,mystrategys,tbegin=0,tend=99999999,dfilter=lambda dt:len(dt)<LENGTH_THRESHOLD):#起止日
        if not isinstance(mystrategys,list):    #单参数转换为列表
            mystrategys = [mystrategys]
        self.trades = []
        #env = BaseObject(holdings=False,to_open=[],to_close=[],cur_inst=None,iorder=0) #holding是当前持仓，to_open/close是当前信号
        env = BaseObject(cur_inst=None,iorder=0,dmin1=BaseObject(sopen=[],   #min1结构需要遵从dac2.MINUTE的结构
                                                                sclose=[],
                                                                shigh=[],
                                                                slow=[],
                                                                svol=[],
                                                                iorder=[],
                                                                min1=[],
                                                            )) 
        for ss in mystrategys:  #初始化
            ss.holdings = False
            ss.to_open = []
            ss.to_close = []
            ss.wclosers = []
            ss.trades = []
        for dt in self.stickss:
            if dt.tdate < tbegin or dt.tdate > tend or dfilter(dt):
                continue
            ##主循环
            self.run_day(env,mystrategys,dt)
        #return self.trades#,env
        return mystrategys

    def run_day(self,env,mystrategys,dticks):#
        '''
            日回测
            todo: 适当时候整合到Agent2中去, 继承或组合Agent2的部分功能,避免重复. 有必要么?
        '''
        print 'run day:%s' % (dticks.tdate)
        tbegin = time.time()
        for ss in mystrategys:  #日初始化
            ss.opener.dreset()
        logging.info('run day:%s' % (dticks.tdate))
        popen = dticks.ticks[0].price
        env.cur_inst = BaseObject(cur_day=BaseObject(vhigh=popen,vlow=popen,vopen=popen,vclose=popen,iidhigh=0,iidlow=0),
                                 dmin1 = env.dmin1,  #之前日期的min1
                                 ticks=[],
                                 prices=[],
                                 dvols=[],
                                 vols=[],
                                 holdings=[],
                                 bids=[],
                                 asks=[],
                                 vbid=[],
                                 vask=[],
                                 tick_base=2,
                              )
        dvol = 0
        dorder = 1
        pre_tick = None
        env.iorder = 0  #日间不连续

        for ctick in dticks.ticks:
            #print ctick.time
            ctick.iorder = env.iorder
            ctick.dorder = dorder
            dorder += 1
            env.iorder += 1
            env.cur_inst.ticks.append(ctick)
            env.cur_inst.prices.append(ctick.price)
            env.cur_inst.dvols.append(ctick.dvolume)
            env.cur_inst.holdings.append(ctick.holding)
            env.cur_inst.vols.append(ctick.dvolume - pre_tick.dvolume if pre_tick else ctick.dvolume)
            env.cur_inst.bids.append(ctick.bid_price)
            env.cur_inst.asks.append(ctick.ask_price)
            env.cur_inst.vbid.append(ctick.bid_volume)
            env.cur_inst.vask.append(ctick.ask_volume)
            dvol = ctick.dvolume
            if ctick.price > env.cur_inst.cur_day.vhigh:
                env.cur_inst.cur_day.vhigh = ctick.price
                env.cur_inst.cur_day.iidhigh = ctick.iorder
            if ctick.price < env.cur_inst.cur_day.vlow:
                env.cur_inst.cur_day.vlow = ctick.price
                env.cur_inst.cur_day.iidlow = ctick.iorder
            pre_tick = ctick

            #先平后开
            self.s_match_close(mystrategys,ctick)
            self.s_match_open(mystrategys,env,ctick)  #动作
            self.s_check_close(mystrategys,env,ctick)
            self.s_check_open(mystrategys,env,ctick)
        env.cur_inst.vclose = dticks.ticks[-1].price
        print 'run tlen=%s' % (time.time()-tbegin,)

    def s_match_close(self,mystrategys,ctick):
        for ss in mystrategys:
            self.match_close(ss,ctick)

    def s_match_open(self,mystrategys,env,ctick):
        for ss in mystrategys:
            self.match_open(ss,env,ctick)
    
    def s_check_close(self,mystrategys,env,ctick):
        for ss in mystrategys:
            self.check_close(ss,env,ctick)

    def s_check_open(self,mystrategys,env,ctick):
        for ss in mystrategys:
            self.check_open(ss,env,ctick)

    def check_open(self,mystrategy,env,ctick):   #
        mysignal = mystrategy.opener.check(env.cur_inst,ctick)
        if mystrategy.holdings or mystrategy.to_open: #如果持仓或即将持仓则不发后面信号，即要求一次开齐
            return 
        if mysignal[0] != 0:#发出信号
            #print 'CB::break:',ctick.price,ctick.time
            base_price = mysignal[1] if mysignal[1]>0 else ctick.price
            base_stop = mysignal[2] if len(mysignal)>2 else 0
            mystrategy.to_open = [BaseObject(
                                         tick = ctick,
                                         strategy = mystrategy,
                                         base_price = base_price,
                                         base_stop = base_stop,
                                         target_price = mystrategy.opener.calc_target_price(base_price,self.tick_base),
                                         valid_length = mystrategy.opener.get_valid_length(), #有效的ticks数
                                         direction = mystrategy.opener.direction,
                                        )
                             ]
            #print base_price,mystrategy.opener.calc_target_price(base_price,self.tick_base)

    def check_close(self,mystrategy,env,ctick):
        if mystrategy.to_close:
            return
        for closer in mystrategy.wclosers:
            csignal = closer.check(ctick)
            base_price = csignal[1] if csignal[1]>0 else ctick.price
            if csignal[0] != 0:    #平仓
                mystrategy.to_close=[BaseObject(
                                     tick = ctick,
                                     opened = closer.opened,#closer的开仓信息
                                     base_price = base_price,
                                     target_price = closer.calc_target_price(base_price,self.tick_base),
                                     direction = closer.direction,
                                  )
                             ]
                break


    def match_close(self,mystrategy,ctick):
        #close必须成交
        if not mystrategy.to_close:
            return
        if mystrategy.to_close[0].direction == SHORT:  #以较差价格成交, 滑点不利
            pclose = ctick.price if ctick.price <= ctick.bid_price else ctick.bid_price
        else:
            pclose = ctick.price if ctick.price >= ctick.ask_price else ctick.ask_price
        opened = mystrategy.to_close[0].opened
        mytrade = Trade(opened.tick,opened.base_price,opened.price,opened.deal_tick,ctick,mystrategy.to_close[0].base_price,pclose,opened.direction)
        #self.trades.append(mytrade)
        mystrategy.trades.append(mytrade)
        mystrategy.to_close = []
        mystrategy.wclosers = []
        mystrategy.holdings = False


    def match_open(self,mystrategy,env,ctick):
        if not mystrategy.to_open:
            return
        topen = mystrategy.to_open[0]
        if ctick.iorder > topen.tick.iorder+topen.valid_length:    #有效期过
            mystrategy.to_open=[]
            return 
        dealed = False
        if topen.direction == SHORT:  #
            mk_price = ctick.price if ctick.price <= ctick.bid_price else ctick.bid_price
            if topen.target_price < mk_price:   #成交
                dealed = True
        else:   
            mk_price = ctick.price if ctick.price >= ctick.ask_price else ctick.ask_price
            if topen.target_price > mk_price:  #成交
                dealed = True
        if dealed == True:  #成交了，允许不成交
            topen.price = mk_price
            topen.deal_tick = ctick
            mystrategy.wclosers = [closer(env.cur_inst,topen.base_price,opened=topen,tick_base=self.tick_base) for closer in mystrategy.closers]
            mystrategy.holdings = True
            mystrategy.to_open = []

    def get_dticks(self,tdate):
        return self.mtickss[tdate] if tdate in self.mtickss else None


class Trade(object):
    def __init__(self,open_tick,open_base_price,open_price,open_deal_tick,close_tick,close_base_price,close_price,direction,tax=2):
        self.open_tick = open_tick
        self.open_deal_tick = open_deal_tick
        self.close_tick = close_tick
        self.open_base_price = open_base_price
        self.open_price = open_price
        self.close_base_price = close_base_price
        self.close_price = close_price
        self.direction = direction
        self.tax = tax

    def get_profit(self):   #按成交的单手收益
        delta = self.close_price - self.open_price
        return delta - self.tax if self.direction==LONG else -delta - self.tax

    def get_profit2(self):  #按信号价位的单手收益
        delta = self.close_base_price - self.open_base_price
        return delta - self.tax if self.direction==LONG else -delta - self.tax

    def get_holding_length(self):
        return self.close_tick.iorder - self.open_tick.iorder

    @staticmethod
    def print_info(trades):
        sprofit = 0
        stimes = 0
        for trade in trades:
            print '%s::open:%s-%s-%s:%s-%s-%s::%s::close:%s:%s' % (trade.get_profit(),trade.open_tick.date,trade.open_tick.time%1000000,trade.open_tick.msec,trade.open_tick.iorder,trade.open_base_price,trade.open_price,trade.open_deal_tick.time%1000000,trade.close_tick.time%1000000,trade.close_price)
            sprofit += trade.get_profit()
            stimes += 1
        print 'times=%s,profit=%s' %(stimes,sprofit)

    @staticmethod
    def print_info2(trades):
        sprofit = 0
        stimes = 0
        for trade in trades:
            print '%s::open:%s-%s-%s:%s-%s-%s::%s::close:%s:%s' % (trade.get_profit(),trade.open_tick.date,trade.open_tick.time%1000000,trade.open_tick.msec,trade.open_tick.iorder,trade.open_base_price,trade.open_price,trade.open_deal_tick.time%1000000,trade.close_tick.time%1000000,trade.close_price)
            sprofit += trade.get_profit2()
            stimes += 1
        print 'times=%s,profit=%s' %(stimes,sprofit)

    @staticmethod
    def sum_info(trades):
        sprofit = 0
        stimes = 0
        for trade in trades:
            #print '%s::open:%s-%s-%s:%s-%s-%s::%s::close:%s:%s' % (trade.get_profit(),trade.open_tick.date,trade.open_tick.time%1000000,trade.open_tick.msec,trade.open_tick.iorder,trade.open_base_price,trade.open_price,trade.open_deal_tick.time%1000000,trade.close_tick.time%1000000,trade.close_price)
            sprofit += trade.get_profit()
            stimes += 1
        #return 'times=%s,profit=%s' %(stimes,sprofit)
        return (stimes,sprofit)
    
    @staticmethod
    def max_drawdown(ftrades,datefrom=20100401,dateto=20200101):
        '''
            在中间即便有盈利，但是如果累计起来仍然为负，则持续计算
        '''
        smax = 0    #最大连续回撤
        max1 = 0    #最大单笔回撤
        curs = 0
        pre_curs = 0
        mdate = 20100401
        spoint=0
        sdate = 20100401
        ssdate = sdate
        sspoint = spoint
        for func,trades in ftrades:
            for trade in trades:
                tdate = trade.open_tick.date
                if tdate > datefrom and tdate < dateto: #忽略掉小于开始时间的
                    curs += trade.get_profit()   #本为负数
                    if curs < 0 and pre_curs >= 0:
                        spoint = trade.open_tick.price
                        sdate = trade.open_tick.date
                    if curs > 0:
                        curs = 0
                    elif curs < smax:
                        smax = curs
                        mdate = trade.open_tick.date
                        ssdate = sdate
                        sspoint = spoint
                    pre_curs = curs
                    if trade.get_profit() < max1:
                        max1 = trade.get_profit()
            print func.name,(smax,max1,ssdate,mdate,sspoint)
        return


class DTicks(object):#日tick结构
    def __init__(self,fname,tdate,ticks):
        self.fname = fname
        self.tdate = tdate
        self.ticks = ticks

    def __len__(self):
        return len(self.ticks)

    def prepare(self):
        pass


#############
#  策略基类
#############
class T_LONG(strategy.BREAK):
    direction = LONG
    def __init__(self,bid_ticks=3,valid_length=60):
        self.bid_ticks = bid_ticks  #买入超价
        self.valid_length = valid_length

    def calc_target_price(self,base_price,tick_base):
        tprice = base_price + tick_base * self.bid_ticks
        print 'target price:',tprice
        return tprice

    def get_valid_length(self):
        return self.valid_length

    def check(self,data,ctick):
        return (False,0)


class T_SHORT(strategy.BREAK):
    direction = SHORT
    def __init__(self,ask_ticks=3,valid_length=60):
        self.ask_ticks = ask_ticks  #卖出超价
        self.valid_length = valid_length

    def calc_target_price(self,base_price,tick_base):
        return base_price - tick_base * self.ask_ticks

    def get_valid_length(self):
        return self.valid_length

    def check(self,data,ctick):
        return (False,0)    

#############
# 策略示例
#############
class T_LONG_EC(T_LONG):
    '''
        EMA通道
    '''
    def __init__(self,bid_ticks=3,valid_length=10,rlen=10):
        T_LONG.__init__(self,bid_ticks=bid_ticks,valid_length=valid_length)
        self.base_line = 99999999
        self.rlen = rlen
        self.ema = None
        self.pre_tick = None

    def dreset(self):
        pass

    def check(self,data,ctick):
        if ctick.min1 <= 915 or ctick.min1 >=1100:
            return (False,0)

        ema = EMA(data.prices,29)

        hh = TMAX(data.prices,self.rlen)
        ll = TMIN(data.prices,self.rlen)
        hl = DIV1(SUB(hh,ll),2)

        rhigh = ADD(ema,hl)

        xc = UPCROSS(rhigh,data.prices)

        if xc[-1]:
            print ctick.time,ctick.msec,'xc=1',ctick.price,self.pre_tick.time,self.pre_tick.msec,self.pre_tick.price,rhigh[-1]
            bline = ctick.price - 100
            return (True,ctick.price,bline)    #(触发标志、触发价、止损)
        self.pre_tick = ctick
        return (False,0)


###########
#  止损示例
###########
class T_LONG_FIXED_STOPER(strategy.LONG_STOPER):
    def __init__(self,data,bline,max_overflow=strategy.MAX_CLOSE_OVERFLOW,valid_length=strategy.STOP_VALID_LENGTH,opened=None,tick_base=2,base_lost=50,keeper=lambda x:80):
        strategy.LONG_STOPER.__init__(self,data,bline)
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'多头固定离场'
        self.opened = opened
        self.keeper = keeper(opened.base_price)
        self.base_stop = opened.base_stop if opened!=None else opened.base_price - base_lost*tick_base
        #self.cur_stop = self.base_stop
        self.set_base_line(self.base_stop)
        print u'原始止损:',self.get_base_line()
        self.tick_base = tick_base
        self.is_keeped = False

    def check(self,tick):
        if tick.price - self.opened.base_price > self.keeper and not self.is_keeped:
            self.set_base_line(self.opened.base_price)
            print 'moving stoper to:',self.get_base_line(),tick.time
            self.is_keeped = True
        if tick.price < self.get_base_line() or tick.min1>1500:
            return (True,tick.price,False)
        return (False,0,False)


class T_SHORT_FIXED_STOPER(strategy.SHORT_STOPER):
    def __init__(self,data,bline,max_overflow=strategy.MAX_CLOSE_OVERFLOW,valid_length=strategy.STOP_VALID_LENGTH,opened=None,tick_base=2,base_lost=50,keeper=lambda x:80):
        strategy.SHORT_STOPER.__init__(self,data,bline)
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'空头固定离场'
        #self.keeper = keeper
        self.keeper = keeper(opened.base_price)
        self.opened = opened
        self.base_stop = opened.base_stop if opened!=None else opened.base_price + base_lost*tick_base
        #self.cur_stop = self.base_stop
        self.set_base_line(self.base_stop)
        self.tlow = opened.base_price
        self.tick_base = tick_base
        self.is_keeped = False

    def check(self,tick):
        if self.opened.base_price - tick.price > self.keeper and not self.is_keeped:
            self.set_base_line(self.opened.base_price)
            print 'moving stoper to:',self.get_base_line()
            self.is_keeped = True
        if tick.price > self.get_base_line() or tick.min1>1500:
            print 'fixed stoper:',tick.time,tick.price
            return (True,tick.price,False)
        return (False,0,False)

class T_SHORT_FIXED_STOPER2(strategy.SHORT_STOPER):
    def __init__(self,data,bline,max_overflow=strategy.MAX_CLOSE_OVERFLOW,valid_length=strategy.STOP_VALID_LENGTH,opened=None,tick_base=2,base_lost=50,keeper=lambda x:80):
        strategy.SHORT_STOPER.__init__(self,data,bline)
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'空头固定离场'
        #self.keeper = keeper
        self.keeper = keeper(opened.base_price)
        self.opened = opened
        self.base_stop = opened.base_stop if opened!=None else opened.base_price + base_lost*tick_base
        #self.cur_stop = self.base_stop
        self.set_base_line(self.base_stop)
        self.tlow = opened.base_price
        self.tick_base = tick_base
        self.is_keeped = False

    def check(self,tick):
        if self.get_base_line() - tick.price > self.keeper and not self.is_keeped:
            self.set_base_line(self.opened.base_price)
            print 'moving stoper to:',self.get_base_line()
            self.is_keeped = True
        if tick.price > self.get_base_line() or tick.min1>1500:
            print 'fixed stoper:',tick.time,tick.price
            return (True,tick.price,False)
        return (False,0,False)

class T_LONG_MOVING_STOPER(strategy.LONG_STOPER):
    def __init__(self,data,bline,max_overflow=strategy.MAX_CLOSE_OVERFLOW,valid_length=strategy.STOP_VALID_LENGTH,opened=None,tick_base=2,base_lost=10,mtime=2):
        strategy.LONG_STOPER.__init__(self,data,bline)
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'多头离场基类'
        self.opened = opened
        self.base_stop = opened.base_stop if opened!=None else opened.base_price - base_lost*tick_base
        #self.cur_stop = self.base_stop
        self.set_base_line(self.base_stop)
        self.thigh = opened.base_price
        self.tick_base = tick_base
        self.mtime = mtime  #移动的单位,每前进mtime,则将止损移动1/mtime
        #print opened.tick.time,opened.base_price,self.base_stop


    def check(self,tick):
        if tick.price < self.get_base_line() or tick.min1>1500:
            return (True,tick.price,False)
        #if tick.price > self.opened.base_price + 50:
        #    return (True,tick.price,False)

        bl2 = tick.price - 1000

        if tick.price >= self.thigh + self.tick_base * self.mtime:
            bl1 = self.get_base_line() + (tick.price - self.thigh)/self.mtime
            bl2 = tick.price - 15
            #self.set_base_line(bl1 if bl1 > bl2 else bl2)
            self.set_base_line(bl1)
            self.thigh = tick.price 
            return (False,0,True)

        return (False,0,False)


class T_SHORT_MOVING_STOPER(strategy.SHORT_STOPER):
    def __init__(self,data,bline,max_overflow=strategy.MAX_CLOSE_OVERFLOW,valid_length=strategy.STOP_VALID_LENGTH,opened=None,tick_base=2,base_lost=10,mtime=2):
        strategy.SHORT_STOPER.__init__(self,data,bline)
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'空头离场基类'
        self.opened = opened
        self.base_stop = opened.base_stop if opened!=None else opened.base_price + base_lost*tick_base
        #self.cur_stop = self.base_stop
        self.set_base_line(self.base_stop)
        self.tlow = opened.base_price
        self.tick_base = tick_base
        self.mtime = mtime  #移动的单位,每前进mtime,则将止损移动1/mtime

    def check(self,tick):
        if tick.price > self.get_base_line() or tick.min1>1500:
            return (True,tick.price,False)
        #if self.opened.price - tick.price > 30:
        #    return (True,tick.price,False)

        stop_changed = False
        #if self.opened.price - tick.price > 20:
        #    self.set_base_line(self.get_base_line() if self.get_base_line()<self.opened.price else self.opened.price)
        #    #self.set_base_line(self.opened.price)
        #    stop_changed = True
        if tick.price <= self.tlow - self.tick_base * self.mtime:
            self.set_base_line(self.get_base_line() - (self.tlow - tick.price)/self.mtime)
            self.tlow = tick.price 
            stop_changed = True
            print 'moving stop:',tick.time,self.get_base_line(),tick.price
        return (False,0,stop_changed)

class T_SHORT_MOVING_STOPER2(strategy.SHORT_STOPER):
    def __init__(self,data,bline,max_overflow=strategy.MAX_CLOSE_OVERFLOW,valid_length=strategy.STOP_VALID_LENGTH,opened=None,tick_base=2,base_lost=10,m1=3,m2=2):
        strategy.SHORT_STOPER.__init__(self,data,bline)
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'空头离场基类'
        self.opened = opened
        self.base_stop = opened.base_stop if opened!=None else opened.base_price + base_lost*tick_base
        #self.cur_stop = self.base_stop
        self.set_base_line(self.base_stop)
        self.tlow = opened.base_price
        self.tick_base = tick_base
        self.m1 = m1    #m1/m2为移动的单位,每前进mtime,则将移动止损m2/m1
        self.m2 = m2    #

    def check(self,tick):
        if tick.price > self.get_base_line() or tick.min1>1500:
            return (True,tick.price,False)
        #if self.opened.price - tick.price > 30:
        #    return (True,tick.price,False)

        stop_changed = False
        #if self.opened.price - tick.price > 20:
        #    self.set_base_line(self.get_base_line() if self.get_base_line()<self.opened.price else self.opened.price)
        #    #self.set_base_line(self.opened.price)
        #    stop_changed = True
        if tick.price <= self.tlow - self.tick_base * self.m1/self.m2:
            self.set_base_line(self.get_base_line() - (self.tlow - tick.price)*self.m2/self.m1)
            self.tlow = tick.price 
            stop_changed = True
            #print tick.time,self.get_base_line()
        return (False,0,stop_changed)



from my.mydac import AVENERGY
class T_SHORT_SPREAD_STOPER(strategy.SHORT_STOPER):
    def __init__(self,data,bline,max_overflow=strategy.MAX_CLOSE_OVERFLOW,valid_length=strategy.STOP_VALID_LENGTH,opened=None,tick_base=2,base_lost=10,mtime=3):
        strategy.SHORT_STOPER.__init__(self,data,bline)
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'空头离场基类'
        self.opened = opened
        self.base_stop = opened.base_stop
        #self.cur_stop = self.base_stop
        self.set_base_line(self.base_stop)
        self.tlow = opened.base_price
        self.tick_base = tick_base
        venergy = AVENERGY(data.prices,data.dvols)
        self.vmafr = NMA(SUB(venergy.shigh,venergy.slow))
        self.mtime = mtime  #移动的单位,每前进mtime,则将止损移动1/mtime
        self.max_spread = opened.base_price + self.vmafr[-1]*10
        self.bline = bline
        #print self.base_stop,self.max_spread,bline

    def check(self,tick):
        if tick.price > self.get_base_line() or tick.min1>1500:
            print tick.time,tick.price,self.get_base_line()
            return (True,tick.price,False)
        #if self.opened.price - tick.price > 30:
        #    return (True,tick.price,False)

        stop_changed = False
        #if self.opened.price - tick.price > 20:
        #    self.set_base_line(self.get_base_line() if self.get_base_line()<self.opened.price else self.opened.price)
        #    #self.set_base_line(self.opened.price)
        #    stop_changed = True
        #if self.tlow < self.max_spread and tick.price <= self.tlow - self.tick_base * self.mtime:
        if self.get_base_line() < self.max_spread and tick.price <= self.tlow - self.tick_base * self.mtime:
            #self.set_base_line(self.get_base_line() + (self.tlow - tick.price)/self.mtime/4)
            self.set_base_line(self.base_stop + (self.bline - tick.price)/self.mtime/4)
            #print tick.time,self.get_base_line(),tick.price,self.tlow
            self.tlow = tick.price 
            stop_changed = True
            #print tick.time,self.get_base_line()
        return (False,0,stop_changed)


l_ema_sm = strategy.STRATEGY('EMA_SM',T_LONG_EC,[T_LONG_MOVING_STOPER],1,1)

def load_all(ifs=('IF1206','IF1207')):
    rtts = []
    for sii in ifs:
        rtt = TickAgent(sii)
        rtt.load()
        rtts.append(rtt)
    return rtts


def cruiser1(rtts,tfuncs,tbegin=0,tend=99999999):
    '''
        计算策略集合tfuncs
    '''
    if not isinstance(tfuncs,list):
        tfuncs = [tfuncs]
    sbegin = time.time()
    tss = [list() for v in tfuncs]  #[[]]*len(tfuncs)是浅复制,n个元素实际上指向同一个
    #print 'ids:',id(tss[0]),id(tss[1])
    for i in range(len(rtts)):
        rtt = rtts[i]
        ss = rtt.run(tfuncs,tbegin=tbegin,tend=tend)
        #print u'i=%s' % (i,)
        for j in range(len(tfuncs)):
            tss[j].extend(ss[j].trades)
            #print u'id(tss[j])=%s,j=%s,tss[j]=%s' % (id(tss[j]),j,tss[j])
    rtss = zip(tfuncs,tss)
    for tfunc,ts in rtss:
        print tfunc.name
        Trade.print_info(ts)
    print u'耗时:%s' % (time.time()-sbegin,)
    return rtss


'''
方式一:
In [1]: import bktest

In [2]: rtt1 = bktest.TickAgent('IFXXXX')

In [3]: rtt1.load()

In [4]: ss = rtt1.run([bktest.l_ema_sm],tend=20190713)

In [5]: bktest.Trade.print_info(ss[0].trades)

方式二:(推荐，可以直接使用多个合约
In [1]: import bktest

In [2]: rtts = bktest.load_all(['IF1206','IF1207'])

In [3]: ss = bktest.cruiser1(rtts,[bktest.l_ema_sm])

In [4]: bktest.Trade.print_info(ss[0][1])

'''
