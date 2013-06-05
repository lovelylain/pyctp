# -*- coding: utf-8 -*-

'''
建立基于ticks的回测平台
    在小规模头寸的情况下，利用一般人难以处理的粒度是一种潜在的竞争优势
    这个回测平台的目标是用ticks数据来测试基于ticks的策略
    如果能找到合适的策略，则在操作上将对针对分钟切换的平台进行瘦身,加快反应速度和增强流畅性
'''

import time
import logging

import base
import dac
import hreader

TUP = 1
TDOWN = -1

OPEN_TICK = 5
OPEN_LENGTH = 5
MAX_TICK = 30   #用于确保平仓
MAX_SLIPPAGE = 500

class BUFFER(object):
    '''
        一个简单的buffer接口
    '''
    def __init__(self,length,init_v = 0):
        self.length = length
        self.data = [init_v] * length

    def append(self,v):
        self.data.append(v)

    def fetch(self):
        v = self.data[0]
        del self.data[0]
        return v

    def exchange(self,v):
        self.append(v)
        return self.fetch()

    def peek_last(self):
        return self.data[-1]

    def peek_first(self):
        return self.data[-1]

    def vmax(self):
        return max(self.data)

    def vmin(self):
        return min(self.data)

    def vavg(self):
        return sum(self.data)/self.length

    def vsum(self):
        return sum(self.data)

    def peek_mid(self):
        mid = self.length / 2
        return self.data[mid]

    def is_mid_upeak(self):
        ''' 中间数是不是高点
            对于奇数长度，mid为中间点
            偶数长度，为偏后点
        '''
        mid = self.length / 2
        vmid = self.data[mid]
        lmax = max(self.data[:mid])
        rmax = max(self.data[mid+1:])
        return vmid > lmax and vmid > rmax

    def is_mid_dpeak(self):
        ''' 中间数是不是低点
            对于奇数长度，mid为中间点
            偶数长度，为偏后点
        '''
        mid = self.length / 2
        vmid = self.data[mid]
        lmin = min(self.data[:mid])
        rmin = min(self.data[mid+1:])
        return vmid < lmin and vmid < rmin

    def is_mid_upeak2(self):
        ''' 
            中间数是不是高点,允许右边有等于存在
        '''
        mid = self.length / 2
        vmid = self.data[mid]
        lmax = max(self.data[:mid])
        rmax = max(self.data[mid+1:])
        return vmid > lmax and vmid >= rmax

    def is_mid_dpeak2(self):
        ''' 中间数是不是低点,允许右边有等于存在
        '''
        mid = self.length / 2
        vmid = self.data[mid]
        lmin = min(self.data[:mid])
        rmin = min(self.data[mid+1:])
        return vmid < lmin and vmid <= rmin

    def is_i_upeak(self,index):#无此抽象必要
        vi = self.data[index]
        lmax = max(self.data[:index]) if index > 0 else 0 
        rmax = max(self.data[index+1:]) if index < self.length - 1 else 0
        return vi > lmax and vi > rmax


class TICK_OPENER(object):
    '''
      对opener的要求
        check()方法,返回是否开仓
        xtype:开仓方向 LONG/SHORT
        open_ticks:     开仓加价
        open_length:    开仓有效期
    '''
    open_ticks = OPEN_TICK
    open_length = OPEN_LENGTH
    
    def tick(self,tick):    #灌数据
        self.cur_tick = tick

    def check(self,cur_trade):
        return False


class TICK_LONG_OPENER(TICK_OPENER):
    xtype = base.LONG

class TICK_SHORT_OPENER(TICK_OPENER):
    xtype = base.SHORT

class TICK_CLOSER(object):
    close_ticks = MAX_TICK  #没用
    def check(self,tick,cur_trade):
        return False
    
class TICK_LONG_CLOSER(TICK_CLOSER):
    xtype = base.SHORT

class TICK_SHORT_CLOSER(TICK_CLOSER):
    xtype = base.LONG


def trade1day(opener,closer,instrument_name,tday,base_unit=2,fee=4):
    ''' 
        opener: 开仓策略
        closer: 平仓策略
        instrument_name: 合约名
        tday: 交易时间
            必须保证在当前data目录下存在 instrument_name/tday.tick文件
        base_unit: tick的最小变化单位
        fee:手续费

        返回 trades. 结构见make_trades
    '''
    ticks = hreader.read_ticks(instrument_name,tday)    #不加载当日数据
    prepare_index(ticks)
    trades = make_trades(opener,closer,ticks,base_unit,fee)
    return trades

def prepare_index(ticks):
    #sprice = [t.price for t in ticks]
    #s_ma1 = dac.ma(sprice,7)
    #s_ma2 = dac.ma(sprice,13)
    #s_ma3 = dac.ma(sprice,20)
    #s_ma4 = dac.ma(sprice,30)
    #s_ma5 = dac.ma(sprice,360)
    dopen = ticks[0].price
    for i in range(len(ticks)):
        #ticks[i].ma1 = s_ma1[i]
        #ticks[i].ma2 = s_ma2[i]
        #ticks[i].ma3 = s_ma3[i]
        #ticks[i].ma4 = s_ma4[i]
        #ticks[i].ma5 = s_ma5[i]
        ticks[i].dopen = dopen
        #if i==0:
        #    ticks[i].sma1 = ticks[i].sma2 = ticks[i].sma3 = ticks[i].sma4 = ticks[i].sma5 = 0
        #else:
        #    ticks[i].sma1 = 1 if ticks[i].ma1 > ticks[i-1].ma1 else -1
        #    ticks[i].sma2 = 1 if ticks[i].ma2 > ticks[i-1].ma2 else -1
        #    ticks[i].sma3 = 1 if ticks[i].ma3 > ticks[i-1].ma3 else -1
        #    ticks[i].sma4 = 1 if ticks[i].ma4 > ticks[i-1].ma4 else -1
        #    ticks[i].sma5 = 1 if ticks[i].ma5 > ticks[i-1].ma5 else -1


def make_trades(opener,closer,ticks,base_unit,fee):
    '''
        opener: 开仓策略
        closer: 平仓策略
        ticks:  tick行情序列
        open_skip:  开仓成交滑时，0为当前时间成交，1为延后1 tick,2为延后2 tick. 即以成交时间的价格为成交价
        close_skip: 平仓成交滑时. 
        #不设置close_ticks: 因为必须确保平仓，所以close_ticks采用30个tick. 这个是全局设置。
        base_unit: tick的基础
        返回 trades: 
          其中每个trade包括
            xtype : LONG/SHORT/EMPTY
            open_time: 开仓时间
            open_tick: 开仓点的ticks序号
            open_base_price: 发出开仓信号的当前价格
            open_price: 开仓价格(-为开多，+为开空)
            open_slippage1: 开仓滑点1，以下一tick成交
            open_slippage2: 开仓滑点2，以下第二tick成交. 不计以第三tick或之后成交的
            close_time: 平仓时间
            close_tick: 平仓点的ticks序号
            close_base_price: 发出平仓信号的当前价格
            close_price: 平仓价格
            close_slippage1:平仓滑点1, 以下一tick成交
            close_slippage2:平仓滑点2，以下第二tick成交
            profit: 利润 = open_price + close_price - 0.4(手续费)
    '''
    trades = []
    cur_trade = create_blank_trade()
    env = base.BaseObject(pdetail=[],psum=0)  #记录关于累计成交的信息,以及划点过线的数据
    cur_trade.env = env
    i = 0
    for tick in ticks[:-5]: #最后5秒不开仓
        if cur_trade.open_tick > i: #开仓时间在后面
            i += 1
            continue
        if cur_trade.xtype != base.EMPTY and closer.check(tick,cur_trade) > 0:  #平仓
            cur_trade.close_time = tick.time
            cur_trade.close_tick = i
            if cur_trade.xtype == base.LONG:
                cur_trade.close_price1 = ticks[i+1].price
                cur_trade.close_price2 = ticks[i+2].price
                base_price = tick.price
            else:
                cur_trade.close_price1 = -ticks[i+1].price
                cur_trade.close_price2 = -ticks[i+2].price
                base_price = -tick.price
            cur_trade.close_base_price = base_price
            cur_trade.close_price = cur_trade.close_price1  #以下一秒成交为准
            cur_trade.close_slippage1 = cur_trade.close_price1 - base_price 
            cur_trade.close_slippage2 = cur_trade.close_price2 - base_price             
            cur_trade.profit = cur_trade.open_price + cur_trade.close_price - fee
            trades.append(cur_trade)
            env.psum += cur_trade.profit
            env.pdetail.append(cur_trade.profit)
            cur_trade = create_blank_trade()
            cur_trade.env = env
        opener.tick(tick)
        #print 'tick.time=%s,cur_trade.xtype=%s,cur_trade.open_time=%s' % (tick.time,cur_trade.xtype,cur_trade.open_time)
        if cur_trade.xtype == base.EMPTY and tick.min1 < 1514 and opener.check(cur_trade)>0: #未开仓时才测试是否要开仓
            target_price = tick.price + opener.open_ticks * base_unit if opener.xtype==base.LONG else tick.price - opener.open_ticks * base_unit
            j = -1
            xprice = 0
            for jt in ticks[i+1:i+opener.open_length+1]:
                j += 1
                if opener.xtype == base.LONG and jt.price <= target_price or opener.xtype == base.SHORT and jt.price >= target_price:      
                    xprice = jt.price
                    break
            if xprice == 0:#未找到
                #print u'不能成交,time=%s,cur_price=%s,target_price=%s,sprice=%s' % (tick.time,tick.price,target_price,[(t.price,t.time) for t in ticks[i+1:i+opener.open_length+1]])
                continue
            cur_trade.xtype = opener.xtype
            cur_trade.open_base_price = -tick.price if opener.xtype == base.LONG else tick.price
            cur_trade.open_time = jt.time
            cur_trade.open_tick = i + 1 + j
            cur_trade.open_price = -jt.price if opener.xtype == base.LONG else jt.price
            open_price1 = first_price(opener.xtype,target_price,ticks[i+2:i+opener.open_length+2])
            open_price2 = first_price(opener.xtype,target_price,ticks[i+3:i+opener.open_length+3])
            cur_trade.open_slippage1 = open_price1 - cur_trade.open_price if open_price1!=0 else MAX_SLIPPAGE
            cur_trade.open_slippage2 = open_price2 - cur_trade.open_price if open_price2!=0 else MAX_SLIPPAGE            
        i += 1
    return trades

def first_price(xtype,target_price,ticks):
    '''
        在ticks中找到符合target_price的第一个价格
        若没找到，返回0
    '''
    price = 0
    for tick in ticks:
        if xtype == base.LONG and tick.price <= target_price or xtype==base.SHORT and tick.price >= target_price:
            price = -tick.price if xtype == base.LONG else tick.price
            break
    return price

def create_blank_trade():
    return base.BaseObject(xtype=base.EMPTY,
                           open_time=-1,
                           open_tick=-1,
                           open_price=0,
                           open_slippage1=0,
                           open_slippage2=0,                           
                           close_time=-1,
                           close_tick=-1,
                           close_price=0,
                           close_slippage1=0,
                           close_slippage2=0,
                           profit = 0,
                    )

def trade_log(trade):
    print trade.profit,trade.open_time,trade.open_price,trade.open_slippage1,trade.open_slippage2,trade.close_time%1000000,trade.close_price,trade.close_slippage1,trade.close_slippage2
    


class min_opener(TICK_LONG_OPENER):
    def check(self,tick,cur_trade):
        if tick.time % 100 == 0:
            return True
        return False

class min_closer(TICK_LONG_CLOSER):
    def check(self,tick,cur_trade):
        if tick.time % 100 == 5:
            return True
        return False

class lbreak_opener(TICK_LONG_OPENER):
    '''
        空头市反弹
    '''
    def __init__(self,length=200):
        self.buffer = [999999] * length
        self.poped = 0

    def tick(self,tick):
        super(lbreak_opener,self).tick(tick) 
        self.buffer.append(tick.price)
        self.poped = self.buffer[0]
        del self.buffer[0]

    def check(self,cur_trade):
        pre_high = max(self.buffer[:-1])
        pre_high = pre_high if self.poped <= pre_high else self.poped
        pre_low = min(self.buffer[:-1])
        pre_low = pre_low if self.poped >= pre_low else self.poped      
        if self.cur_tick.price > pre_high and pre_high-pre_low<self.cur_tick.dopen/720 and self.cur_tick.price < (self.cur_tick.high+self.cur_tick.low*2)/3 and self.cur_tick.price < self.cur_tick.dopen:# and tick.time % 1000000<100000:
            print self.cur_tick.time,self.cur_tick.price,pre_high#,self.buffer
            return True
        return False

class sbreak_opener(TICK_SHORT_OPENER):
    '''
        空头
    '''
    def __init__(self,length=300):
        self.buffer = [0] * length
        self.poped = 0

    def tick(self,tick):
        super(sbreak_opener,self).tick(tick) 
        self.buffer.append(tick.price)
        self.poped = self.buffer[0]
        del self.buffer[0]

    def check(self,cur_trade):
        pre_high = max(self.buffer[:-1])
        pre_high = pre_high if self.poped <= pre_high else self.poped
        pre_low = min(self.buffer[:-1])
        pre_low = pre_low if self.poped >= pre_low else self.poped      
        #print self.cur_tick.time,pre_low,self.cur_tick.price
        if self.cur_tick.price < pre_low:# and pre_high-pre_low<self.cur_tick.dopen/1000:# and pre_high < self.cur_tick.dopen:# and tick.time % 1000000<100000:
            #print self.cur_tick.time,self.cur_tick.price,pre_high#,self.buffer
            return True
        return False

class lreverse_opener(TICK_LONG_OPENER):
    '''
        转向突破
    '''
    def __init__(self,rlen=0,break_len=200):
        self.rlen = rlen
        self.break_len = break_len
        self.direction = TUP
        self.lasting = 0
        self.bbuffer = BUFFER(break_len,0)
        self.vpre = 0

    def tick(self,tick):
        vlast = self.bbuffer.peek_last()
        if tick.price > vlast and self.direction == TUP or tick.price<vlast and self.direction==TDOWN:
            self.lasting += 1
        elif tick.price > vlast and self.direction == TDOWN or tick.price<vlast and self.direction==TUP:
            self.lasting = 1
            self.direction = TUP if tick.price > vlast else TDOWN
        else: #tick.price == vlast
            pass
        super(lreverse_opener,self).tick(tick) 
        self.vmax = self.bbuffer.vmax()
        self.vpre = self.bbuffer.exchange(tick.price)

    def check(self,cur_trade):
        if self.cur_tick.price > self.vmax and self.lasting > 5:
            return True
        return False


class lpeak_opener(TICK_LONG_OPENER):
    '''
        前高突破
    '''
    def __init__(self,ulen=180,dlen=10):
        self.ulen = ulen
        self.dlen = dlen
        self.upeaks = []
        self.dpeaks = []
        self.ubuffer = BUFFER(ulen*2+1)
        self.dbuffer = BUFFER(dlen*2+1)
        self.wbuffer = BUFFER(120)

    def tick(self,tick):
        super(lpeak_opener,self).tick(tick) 
        self.ubuffer.exchange(tick.price)
        self.dbuffer.exchange(tick.price)
        self.wbuffer.exchange(tick.price)
        if self.ubuffer.is_mid_upeak():
            self.upeaks.append(self.ubuffer.peek_mid())
        if self.dbuffer.is_mid_dpeak2():
            self.dpeaks.append(self.dbuffer.peek_mid())

    def check(self,cur_trade):
        if self.cur_tick.min1 < 930:
            return False
        if cur_trade.env.psum < -100:#停摆
            return False
        mhigh = self.wbuffer.vmax()
        mlow = self.wbuffer.vmin()
        if self.cur_tick.price - self.wbuffer.data[-20] > self.cur_tick.dopen/1000:# or mhigh-mlow > self.cur_tick.dopen/300:
            return False
        #if len(self.upeaks)>=2 and self.cur_tick.price > self.upeaks[-1]+6 and self.cur_tick.price > (self.upeaks[-1] + self.upeaks[-2])/2:
        #if len(self.upeaks)>2 and self.cur_tick.price > max(self.upeaks[-3:])+6:
        if len(self.upeaks)>2 and self.cur_tick.price > max(self.upeaks[-3:])+6:
            return True
        return False

class speak_opener(TICK_SHORT_OPENER):
    '''
        前低突破
    '''
    def __init__(self,ulen=200,dlen=200):
        self.ulen = ulen
        self.dlen = dlen
        self.upeaks = []
        self.dpeaks = []
        self.ubuffer = BUFFER(ulen*2+1)
        self.dbuffer = BUFFER(dlen*2+1)
        self.wbuffer = BUFFER(120)
        self.lbuffer = BUFFER(30)
        self.sbuffer = BUFFER(30)
        self.pre_price = 0
        self.pre_volume = 0

    def tick(self,tick):
        super(speak_opener,self).tick(tick)
        self.ubuffer.exchange(tick.price)
        self.dbuffer.exchange(tick.price)
        self.wbuffer.exchange(tick.price)
        if self.ubuffer.is_mid_upeak():
            self.upeaks.append(self.ubuffer.peek_mid())
        if self.dbuffer.is_mid_dpeak2():
            self.dpeaks.append(self.dbuffer.peek_mid())
        #成交量处理
        if self.pre_volume > 0:
            if tick.price > self.pre_price:
                self.lbuffer.exchange(tick.dvolume-self.pre_volume)
                self.sbuffer.exchange(0)
            elif tick.price < self.pre_price:
                self.sbuffer.exchange(tick.dvolume-self.pre_volume)
                self.lbuffer.exchange(0)
        self.pre_volume = tick.dvolume
        self.pre_price = tick.price
        

    def check(self,cur_trade):
        if self.cur_tick.min1 < 930:
            return False
        if cur_trade.env.psum < -120:#停摆
            return False
        #if self.cur_tick.high - self.cur_tick.low > 400 or self.cur_tick.high-self.cur_tick.low<100:
        #    return False
        #mhigh = self.wbuffer.vmax()
        #mlow = self.wbuffer.vmin()
        #if mhigh - mlow > self.cur_tick.dopen/750 or self.wbuffer.data[-10] - self.cur_tick.price > 20:
        #if self.wbuffer.data[-20] - self.cur_tick.price > self.cur_tick.dopen/1000:# or mhigh-mlow > self.cur_tick.dopen/300:
        #    return False
        
        #print 'in check,time=%s' % (self.cur_tick.time,)
        #if self.dpeaks and self.cur_tick.price < self.dpeaks[-1]:
        if self.cur_tick.price > self.cur_tick.dopen and len(self.upeaks)>=2 and self.cur_tick.price >= self.upeaks[-1] and self.dpeaks[-2] > self.dpeaks[-1]:
            #print self.sbuffer.vsum() , self.lbuffer.vsum()
            return True
        return False

class b123_opener(TICK_LONG_OPENER):
    '''
        前高突破
>>> trades = sticks.make_trades(sticks.b123_opener(),sticks.long_trailing_stop(),tickss[-1],2,4)
>>> sum([trade.profit for trade in trades])
-116
>>> len(trades)
29
>>> for trade in trades: print trade.profit,trade.open_time,trade.open_base_price,trade.open_price,trade.close_time%1000000,trade.close_price
    
    9.10合约 76.2点/109次
    8合约: -37
    '''
    def __init__(self,ulen=120,dlen=120,dfilter=16):
        '''
            在18-23(20+冲击24), 100-150(120+冲击16/30)有两个光谱带
        '''
        self.it = 0  #计数
        self.ulen = ulen
        self.dlen = dlen        
        self.dfilter = dfilter
        self.upeaks = []
        self.dpeaks = []
        self.iupeaks = []
        self.idpeaks = []
        self.ubuffer = BUFFER(ulen*2+1)
        self.dbuffer = BUFFER(dlen*2+1)        
        self.wbuffer = BUFFER(200)

    def tick(self,tick):
        super(b123_opener,self).tick(tick) 
        self.ubuffer.exchange(tick.price)
        self.dbuffer.exchange(tick.price)        
        self.wbuffer.exchange(tick.price)
        if self.ubuffer.is_mid_upeak2():
            self.upeaks.append(self.ubuffer.peek_mid())
            self.iupeaks.append(self.it - self.ulen)
        if self.dbuffer.is_mid_dpeak2():
            self.dpeaks.append(self.dbuffer.peek_mid())
            self.idpeaks.append(self.it - self.dlen)
        self.it += 1

    def check(self,cur_trade):
        if self.cur_tick.min1 < 930:
            return False
        if cur_trade.env.psum < -120:#停摆
            return False
        #mhigh = self.wbuffer.vmax()
        #mlow = self.wbuffer.vmin()
        #if mhigh - mlow > self.cur_tick.dopen/750 or self.wbuffer.data[-10] - self.cur_tick.price > 20:
        #if self.cur_tick.price - self.wbuffer.data[-180] > self.cur_tick.dopen/1500: #or mhigh-mlow < self.cur_tick.dopen/300:
        #    return False
        if len(self.upeaks)>=2 and len(self.dpeaks)>=3 and self.cur_tick.price > self.upeaks[-1]+self.dfilter and self.dpeaks[-1] > self.dpeaks[-2] and self.dpeaks[-2]<self.dpeaks[-3] and self.dpeaks[-1] > self.dpeaks[-3]:
            #print self.cur_tick.time,self.dpeaks[-5:],self.upeaks[-5:]
            return True
        return False


class hb123_opener(TICK_LONG_OPENER):
    '''
        前高突破
>>> trades = sticks.make_trades(sticks.sb123_opener(),sticks.long_trailing_stop(),tickss[-1],2,4)
>>> sum([trade.profit for trade in trades])
-116
>>> len(trades)
29
>>> for trade in trades: print trade.profit,trade.open_time,trade.open_base_price,trade.open_price,trade.close_time%1000000,trade.close_price
    
    9.10合约 76.2点/109次
    8合约: -37
    '''
    def __init__(self,ulen=60,dlen=60,dfilter=16):
        '''
            在18-23(20+冲击24), 100-150(120+冲击16/30)有两个光谱带
        '''
        self.it = 0  #计数
        self.ulen = ulen
        self.dlen = dlen        
        self.dfilter = dfilter
        self.upeaks = []
        self.dpeaks = []
        self.iupeaks = []
        self.idpeaks = []
        self.ubuffer = BUFFER(ulen*2+1)
        self.dbuffer = BUFFER(dlen*2+1)        
        self.wbuffer = BUFFER(200)

    def tick(self,tick):
        super(hb123_opener,self).tick(tick) 
        self.ubuffer.exchange(tick.price)
        self.dbuffer.exchange(tick.price)        
        self.wbuffer.exchange(tick.price)
        if self.ubuffer.is_mid_upeak2():
            self.upeaks.append(self.ubuffer.peek_mid())
            self.iupeaks.append(self.it - self.ulen)
        if self.dbuffer.is_mid_dpeak2():
            self.dpeaks.append(self.dbuffer.peek_mid())
            self.idpeaks.append(self.it - self.dlen)
        self.it += 1

    def check(self,cur_trade):
        if self.cur_tick.min1 < 930:
            return False
        if cur_trade.env.psum < -120:#停摆
            return False
        if len(self.upeaks)>=2 and len(self.dpeaks)>=3 and (
                self.cur_tick.price > self.upeaks[-1] + 4
                and self.dpeaks[-1] > self.dpeaks[-2] 
                and self.upeaks[-1] > self.upeaks[-2] 
                and self.idpeaks[-1] < self.iupeaks[-1]
                and self.idpeaks[-1] > self.iupeaks[-2]
            ):
            #print self.cur_tick.time,self.dpeaks[-5:],self.upeaks[-5:]
            return True
        return False

class s123_opener(TICK_SHORT_OPENER):
    '''
        前低突破
>>> trades = sticks.make_trades(sticks.s123_opener(),sticks.short_trailing_stop(),tickss[-1],2,4)
>>> sum([trade.profit for trade in trades])
-116
>>> len(trades)
29
>>> for trade in trades: print trade.profit,trade.open_time,trade.open_base_price,trade.open_price,trade.close_time%1000000,trade.close_price
    9-10合约 125.6点/205次
    8合约: -70
    '''
    def __init__(self,ulen=120,dlen=120):
        self.it = 0  #计数
        self.ulen = ulen
        self.dlen = dlen        
        self.upeaks = []
        self.dpeaks = []
        self.iupeaks = []
        self.idpeaks = []
        self.ubuffer = BUFFER(ulen*2+1)
        self.dbuffer = BUFFER(dlen*2+1)        
        self.wbuffer = BUFFER(120)

    def tick(self,tick):
        super(s123_opener,self).tick(tick) 
        self.ubuffer.exchange(tick.price)
        self.dbuffer.exchange(tick.price)        
        self.wbuffer.exchange(tick.price)
        if self.ubuffer.is_mid_upeak2():
            self.upeaks.append(self.ubuffer.peek_mid())
            self.iupeaks.append(self.it - self.ulen)
        if self.dbuffer.is_mid_dpeak2():
            self.dpeaks.append(self.dbuffer.peek_mid())
            self.idpeaks.append(self.it - self.dlen)
        self.it += 1

    def check(self,cur_trade):
        if self.cur_tick.min1 < 930:
            return False
        if cur_trade.env.psum < -120:#停摆
            return False
        #mhigh = self.wbuffer.vmax()
        #mlow = self.wbuffer.vmin()
        #if mhigh - mlow > self.cur_tick.dopen/750 or self.wbuffer.data[-10] - self.cur_tick.price > 20:
        #if self.wbuffer.data[-20] - self.cur_tick.price > self.cur_tick.dopen/1000:# or mhigh-mlow > self.cur_tick.dopen/300:
        #    return False
        if len(self.upeaks)>=2 and len(self.dpeaks)>=3 and self.cur_tick.price <= self.dpeaks[-1] and self.upeaks[-1] < self.upeaks[-2] and self.dpeaks[-1] > self.dpeaks[-2] and self.dpeaks[-1] - self.dpeaks[-2] > self.dpeaks[-2] - self.dpeaks[-3] and self.iupeaks[-1] > self.idpeaks[-1]:
            #if self.cur_tick.min1>1458:
            #    print self.cur_tick.time,self.dpeaks[-5:],self.upeaks[-5:]
            return True
        return False

class s123b_opener(TICK_SHORT_OPENER):
    '''
        前低突破
>>> trades = sticks.make_trades(sticks.s123_opener(),sticks.short_trailing_stop(),tickss[-1],2,4)
>>> sum([trade.profit for trade in trades])
-116
>>> len(trades)
29
>>> for trade in trades: print trade.profit,trade.open_time,trade.open_base_price,trade.open_price,trade.close_time%1000000,trade.close_price
    
    9-10合约: 191 /729 /29个交易日
    8合约: 69 /503/26个交易日
    只有这个在3个月内都是稳定的. 但是交易次数太多
    而且总体来说,如果没有最大的1-3次收益,那么总体就是亏的
    应当说没有找到合适的可用方法.
    '''
    def __init__(self,ulen=20,dlen=20):
        self.it = 0  #计数
        self.ulen = ulen
        self.dlen = dlen        
        self.upeaks = []
        self.dpeaks = []
        self.iupeaks = []
        self.idpeaks = []
        self.ubuffer = BUFFER(ulen*2+1)
        self.dbuffer = BUFFER(dlen*2+1)        
        self.wbuffer = BUFFER(120)

    def tick(self,tick):
        super(s123b_opener,self).tick(tick) 
        self.ubuffer.exchange(tick.price)
        self.dbuffer.exchange(tick.price)        
        self.wbuffer.exchange(tick.price)
        if self.ubuffer.is_mid_upeak2():
            self.upeaks.append(self.ubuffer.peek_mid())
            self.iupeaks.append(self.it - self.ulen)
        if self.dbuffer.is_mid_dpeak2():
            self.dpeaks.append(self.dbuffer.peek_mid())
            self.idpeaks.append(self.it - self.dlen)
        self.it += 1

    def check(self,cur_trade):
        if self.cur_tick.min1 < 930:
            return False
        if cur_trade.env.psum < -120:#停摆
            return False
        #mhigh = self.wbuffer.vmax()
        #mlow = self.wbuffer.vmin()
        #if mhigh - mlow > self.cur_tick.dopen/750 or self.wbuffer.data[-10] - self.cur_tick.price > 20:
        #if self.wbuffer.data[-20] - self.cur_tick.price > self.cur_tick.dopen/1000:# or mhigh-mlow > self.cur_tick.dopen/300:
        #    return False
        if len(self.upeaks)>=2 and len(self.dpeaks)>=3 and self.cur_tick.price <= self.dpeaks[-1] and self.upeaks[-1] < self.upeaks[-2]:
            #if self.cur_tick.min1>1458:
            #    print self.cur_tick.time,self.dpeaks[-5:],self.upeaks[-5:]
            return True
        return False

class lma_opener(TICK_LONG_OPENER):
    def __init__(self,length=120):
        self.length = length
        self.wbuffer = BUFFER(length+1)
        self.spre = False

    def tick(self,tick):
        super(lma_opener,self).tick(tick)
        self.wbuffer.exchange(tick.price)

    def check(self,cur_trade):
        mcur = sum(self.wbuffer.data[:-5])/(self.length-4)
        #mhigh = max(self.wbuffer.data[:-4])
        #mlow = min(self.wbuffer.data[:-4])
        umcur = mcur + self.cur_tick.dopen/300
        #umcur = mcur + (mhigh-mlow)
        if self.spre == False and self.cur_tick.price > umcur:
            self.spre = True
            return True
        else:
            self.spre = False
        return False

class dma_opener(TICK_SHORT_OPENER):
    def __init__(self,length=200):
        self.length = length
        self.wbuffer = BUFFER(length+1)
        self.spre = False

    def tick(self,tick):
        super(dma_opener,self).tick(tick)
        self.wbuffer.exchange(tick.price)

    def check(self,cur_trade):
        mcur = sum(self.wbuffer.data[:-5])/(self.length-4)
        #mhigh = max(self.wbuffer.data[:-4])
        #mlow = min(self.wbuffer.data[:-4])
        umcur = mcur + self.cur_tick.dopen/300
        #umcur = mcur + (mhigh-mlow)
        if self.spre == False and self.cur_tick.price > umcur:
            self.spre = True
            return True
        else:
            self.spre = False
        return False

class lvama_opener(TICK_LONG_OPENER):
    def __init__(self,capacity=200,slen=3,llen=120):
        assert(slen < llen)
        self.capacity = capacity
        self.slen = slen
        self.llen = llen
        self.cbuffer = BUFFER(llen+1)   #收价序列
        self.wbuffer = BUFFER(llen+1)   #波动序列
        self.tbuffer = BUFFER(llen+1)   #时间序列
        self.sma = []
        self.lma = []
        self.chigh = 0
        self.clow = 9999999
        self.vpre = 0
        self.check_it = False

    def tick(self,tick):
        super(lvama_opener,self).tick(tick)
        if tick.price > self.chigh:
            self.chigh = tick.price
        if tick.price < self.clow:
            self.clow = tick.price
        if tick.dvolume - self.vpre > self.capacity:#假设一个ticks不会有超过capacity的交易量
            self.vpre = tick.dvolume - tick.dvolume%self.capacity
            self.check_it = True
            self.cbuffer.exchange(tick.price)
            self.wbuffer.exchange(self.chigh-self.clow)
            self.tbuffer.exchange(tick.time)
            self.chigh = 0
            self.clow = 9999999
            if len(self.cbuffer.data) >= self.slen:
                self.sma.append(sum(self.cbuffer.data[-self.slen:])/self.slen)
            if len(self.cbuffer.data) >= self.llen:
                self.lma.append(sum(self.cbuffer.data[-self.llen:])/self.llen)
        else:
            self.check_it = False
        if len(self.lma) < 2:
            self.check_it = False

    def check(self,cur_trade):
        if self.check_it == True and (self.sma[-2]<=self.lma[-2] 
                    and self.sma[-1]>self.lma[-1] 
                    and self.sma[-1]>self.sma[-2] 
                    and self.lma[-1]>=self.lma[-2]
                ):
            return True
        return False


class svama_opener(TICK_SHORT_OPENER):
    def __init__(self,length=200):
        self.length = length
        self.wbuffer = BUFFER(length+1)
        self.spre = False

    def tick(self,tick):
        super(dma_opener,self).tick(tick)
        self.wbuffer.exchange(tick.price)

    def check(self,cur_trade):
        mcur = sum(self.wbuffer.data[:-5])/(self.length-4)
        #mhigh = max(self.wbuffer.data[:-4])
        #mlow = min(self.wbuffer.data[:-4])
        umcur = mcur + self.cur_tick.dopen/300
        #umcur = mcur + (mhigh-mlow)
        if self.spre == False and self.cur_tick.price > umcur:
            self.spre = True
            return True
        else:
            self.spre = False
        return False



class long_channel_opener(TICK_LONG_OPENER):
    def __init__(self,long_len=200,short_len=30):
        self.buffer = [999999] * long_len
        self.long_len = long_len
        self.short_len = short_len

    def check(self,tick,cur_trade):
        mv_long = self.buffer[-1] - self.buffer[0]
        mv_short = self.buffer[-1] - self.buffer[self.short_len]
        slhigh = max(self.buffer)
        sllow = min(self.buffer)
        self.buffer.append(tick.price)
        del self.buffer[0]
        if mv_long>0 and mv_short>0 and tick.price > (slhigh+sllow)/2:
            return True
        return False


class lbreak_closer(TICK_LONG_CLOSER):
    def __init__(self,length=10):
        self.buffer = [0] * length

    def check(self,tick,cur_trade):
        pre_low = min(self.buffer)
        self.buffer.append(tick.price)
        del self.buffer[0]
        if tick.price < pre_low:
            return True
        return False

class lbreak_closer_retrace(TICK_LONG_CLOSER):
    def __init__(self,retrace=20):
        self.buffer = []
        self.retrace = retrace

    def check(self,tick,cur_trade):
        if tick.time == cur_trade.open_time:
            self.buffer = [tick.price]
        elif cur_trade.xtype != base.EMPTY:
            self.buffer.append(tick.price)
        chigh = max(self.buffer)
        if tick.price < chigh-self.retrace:
            return True
        return False

class long_simple_stop(TICK_LONG_CLOSER):
    '''
        进入点 - 10或最高点-60
    '''
    def __init__(self,init_lost=10,max_retracement=60):
        self.init_lost = init_lost
        self.max_retracement = max_retracement
        self.high = 0

    def check(self,tick,cur_trade):
        if tick.price < -cur_trade.open_price - self.init_lost or tick.price < self.high - self.max_retracement:
            self.high = 0
            self.stop = 0
            return True
        if tick.price > self.high:
            self.high = tick.price
        return False

class long_trailing_stop(TICK_LONG_CLOSER):
    def __init__(self,init_lost=20,max_retracement=60,unit=4,gain=2):
        '''
            init_lost:初始止损
            max_retracement:从高点下来的最大止损
            unit: 步进的计量单位
            gain: 顺势走一个unit之后，拉升止损的点数
        '''
        self.init_lost = init_lost
        self.max_retracement = max_retracement
        self.high = 0
        self.stop = 0
        self.unit = unit
        self.gain = gain

    def check(self,tick,cur_trade):
        ''' 
            cur_trade.open_price是负的
        '''
        if tick.min1 > 1513:
            return True
        if tick.price < self.stop:   #以便重新开始计数
            self.high = 0
            self.stop = 0
            return True
        if tick.price > self.high:
            self.high = tick.price
            stop1 = -cur_trade.open_base_price - self.init_lost
            stop2 = self.high - self.max_retracement
            stop3 = stop1 + (self.high + cur_trade.open_price)/self.unit * self.gain
            stop4 = stop1 + (self.high + cur_trade.open_price)/self.unit * (self.gain + 1) if stop3 < -cur_trade.open_base_price else 0 #未保本则快拉
            self.stop = max(stop1,stop2,stop3,stop4)
        return False

class short_trailing_stop(TICK_SHORT_CLOSER):
    def __init__(self,init_lost=20,max_retracement=60,unit=4,gain=2):
        '''
            init_lost:初始止损
            max_retracement:从高点下来的最大止损
            unit: 步进的计量单位
            gain: 顺势走一个unit之后，拉升止损的点数
        '''
        self.init_lost = init_lost
        self.max_retracement = max_retracement
        self.low = 999999
        self.stop = 999999
        self.unit = unit
        self.gain = gain

    def check(self,tick,cur_trade):
        ''' 
            cur_trade.open_price为正
        '''
        if tick.min1 > 1513:
            return True
        if tick.price > self.stop:   #以便重新开始计数
            #print tick.price,self.stop
            self.low = 999999
            self.stop = 999999
            return True
        if tick.price < self.low:
            self.low = tick.price
            stop1 = cur_trade.open_base_price + self.init_lost
            stop2 = self.low + self.max_retracement
            stop3 = stop1 - (cur_trade.open_price - self.low)/self.unit * self.gain
            stop4 = stop1 - (cur_trade.open_price - self.low)/self.unit * (self.gain+1) if stop3 > cur_trade.open_base_price else 9999999   #未保本则快拉
            self.stop = min(stop1,stop2,stop3,stop4)
            #if self.stop > cur_trade.open_base_price:   #未保本, 这个太生硬
            #    self.stop  = tick.price + self.init_lost
            #print stop1,stop2,stop3
        return False


def test2m():
    logging.basicConfig(filename="ticks_backtest.log",level=logging.INFO,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')    
    dates = [20110914,20110915,20110916,20110919,20110920,20110921,20110922,20110923,20110926,20110927,20110928,20110929,20110930]
    dates2 = [20110817,20110818,20110819,20110822,20110823,20110824,20110825,20110826,20110829,20110830,20110831,20110901,20110902,20110909,20110913,20110914]
    results = []
    #for idate in dates2:
    for idate in dates:
        trades = trade1day(lpeak_opener(),long_trailing_stop(),'IF1110',idate,fee=4)
        #trades = trade1day(lpeak_opener(),long_trailing_stop(),'IF1109',idate,fee=4)
        #trades = trade1day(speak_opener(),short_trailing_stop(),'IF1110',idate,fee=4)
        #trades = trade1day(speak_opener(),short_trailing_stop(),'IF1109',idate,fee=4)
        result = base.BaseObject(idate = idate,
                            isum = sum([trade.profit for trade in trades]),
                            isum2 = sum([trade.profit for trade in trades[:50]]),                            
                            ilen = len(trades),
                            trades = trades,
                        )
        results.append(result)
    #for result in results:print result.idate,result.isum,result.ilen
    return results

def prepare_data_201109():
    dates2 = [20110817,20110818,20110819,20110822,20110823,20110824,20110825,20110826,20110829,20110830,20110831,20110901,20110902,20110909,20110913,20110914]
    tickss = []
    for idate in dates2:
        cur_ticks = hreader.read_ticks('IF1109',idate)
        prepare_index(cur_ticks)
        tickss.append(cur_ticks)
    return tickss

def prepare_data_201110():
    dates = [20110914,20110915,20110916,20110919,20110920,20110921,20110922,20110923,20110926,20110927,20110928,20110929,20110930]
    tickss = []
    for idate in dates:
        cur_ticks = hreader.read_ticks('IF1110',idate)
        prepare_index(cur_ticks)
        tickss.append(cur_ticks)
    return tickss

def prepare_data_201108():
    dates = [20110714,20110715,20110718,20110719,20110720,20110721,20110722,20110725,20110726,20110727,20110728,20110729,20110801,20110802,20110803,20110804,20110805,20110808,20110809,20110810,20110811,20110812,20110815,20110816,20110817,20110818]
    tickss = []
    for idate in dates:
        cur_ticks = hreader.read_ticks('IF1108',idate)
        prepare_index(cur_ticks)
        tickss.append(cur_ticks)
    return tickss

def test2(tickss,opener,closer):
    '''
>>> results = sticks.test2(tickss,sticks.s123_opener(),sticks.short_trailing_stop())
>>> for result in results:print result.instrument,result.idate,result.isum,result.ilen
>>> sum([result.isum for result in results])
>>> len(results)
    '''
    results = []
    for ticks in tickss:
        print 'calc: %s:%04d' % (ticks[0].instrument,ticks[0].time/1000000)
        trades = make_trades(opener,closer,ticks,base_unit=2,fee=4)
        result = base.BaseObject(
                            instrument = ticks[0].instrument,
                            idate = ticks[0].time/1000000,
                            isum = sum([trade.profit for trade in trades]),
                            #isum2 = sum([trade.profit for trade in trades[:50]]),                            
                            ilen = len(trades),
                            trades = trades,
                        )
        results.append(result)
    #for result in results:print result.instrument,result.idate,result.isum,result.ilen
    #sum([result.isum for result in results])
    return results

def testv1(capacity=200):
    ticks = hreader.read_ticks('IF1110',20110927)    #不加载当日数据
    results = []
    for llen in range(5,500,2):
        trades=make_trades(lvama_opener(llen=llen,capacity=capacity),long_trailing_stop(),ticks,2,4)
        results.append((llen,sum([trade.profit for trade in trades]),len(trades)))
        if results[-1][1]>0:
            print results[-1]
    return results
        
def testv(tickss):
    #tickss = prepare_data_201107()
    sresults = []
    for capacity in (100,200,300,400,500,600,700,800,900,1000,1200,1500,2000):
        for llen in range(5,600,2):#:
            #print 'in capacity:%s,llen:%s' % (capacity,llen)
            results = []
            for ticks in tickss:
                trades=make_trades(lvama_opener(llen=llen,capacity=capacity),long_trailing_stop(),ticks,2,4)
                result = base.BaseObject(
                            instrument = ticks[0].instrument,
                            idate = ticks[0].time/1000000,
                            isum = sum([trade.profit for trade in trades]),
                            #isum2 = sum([trade.profit for trade in trades[:50]]),                            
                            ilen = len(trades),
                        )
                results.append(result)
            rsum = sum([result.isum for result in results])
            rlen = sum([result.ilen for result in results])
            sresults.append((capacity,llen,rsum,rlen))
            print 'calced capacity=%s,llen=%s,rlen=%s,rsum=%s' % (capacity,llen,rlen,rsum)
            if rlen < 10:
                print u'break'
                break
    return sresults

