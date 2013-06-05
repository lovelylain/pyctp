# -*- coding: utf8 -*-

'''
    策略
    包括紧盯的合约
    目前支持手工设定标的合约，有时间时自动盘前判断主力合约

    因为现在opener中没有做日的初始化。所以不能连续不间断运行。只能每天8:50启动下.
        不能在Agent中来重新初始化Opener,因为opener可能含有不可直接恢复的跨日状态.

'''

import logging

import UserApiType as utype


from base import *
from dac import CBASE


##策略类
#基类提供接口
    

'''
每个策略类必须实现两个方法:
    check(self,data,ctick)  #信号检查
        必须返回(开仓标志, 基准价)
        其中开仓标志:    0:不开仓, 1:开仓
                         基准价为开仓基准价，将用于计算开仓限价和开仓止损
    calc_target_price(self,base_price,tick_base) #计算开仓限价, 其中tick_base是每跳幅度
'''

####下单
class Order(object):
    def __init__(self,position,base_price,target_price,mytime,action_type):
        self.position = position
        self.base_price = base_price        #开仓基准价
        self.target_price = target_price    #开仓加价部分
        self.mytime = mytime
        ##衍生
        self.instrument = position.instrument
        self.direction = utype.THOST_FTDC_D_Buy if position.strategy.direction==LONG else utype.THOST_FTDC_D_Sell
        ##操作类型
        assert action_type == XOPEN,u'操作类型必须是开仓'
        self.action_type = action_type
        ##
        self.volume = 0 #目标成交手数,锁定总数
        self.opened_volume = 0  #实际成交手数
        self.stopers = []
        self.trade_detail = []
        self.cancelled = False  #是否已经撤单
        self.close_lock = False #平仓锁定，即已经发出平仓信号

    def on_trade(self,price,volume,trade_time):
        ''' 返回是否完全成交
        '''
        logging.info(u'成交纪录:price=%s,volume=%s,trade_time=%s' % (price,volume,trade_time))
        self.opened_volume += volume
        if self.volume < self.opened_volume:    #因为cancel和成交的时间差导致的
            self.volume = self.opened_volume
        logging.info(u'price=%s,volume=%s,self.opened_volume=%s,is_closed=%s' % (price,volume,self.opened_volume,self.is_closed()))
        self.trade_detail.append((price,volume,trade_time))
        self.position.re_calc()
        return self.opened_volume == self.volume
        
    def on_close(self,price,volume,trade_time):
        self.opened_volume -= volume
        #self.volume = self.opened_volume    #已经开始平仓，必然没有待成交的目标 #这个假设可能有问题??
        self.volume -= volume
        self.trade_detail.append((price,-volume,trade_time))
        logging.info(u'O_CLS:on close,opened_volume=%s,volume=%s,trade_time=%s' % (self.opened_volume,volume,trade_time))
        self.position.re_calc()

    def on_cancel(self):    #已经撤单
        self.cancelled = True
        self.volume = self.opened_volume    #不会再有成交回报
        logging.info('O_OC:on cancel,self.volume=%s' % (self.volume,))
        self.position.re_calc()

    def is_closed(self): #是否已经完全平仓
        return self.cancelled and self.opened_volume == 0

    def get_profit(self):
        if not self.is_closed():    #未完全平仓的，返回0
            return 0
        rp = sum([td[0]*td[1] for td in self.trade_detail])
        for td in self.trade_detail:
            logging.info(u'交易明细：%s' % self.trade_detail)
        if self.position.strategy.direction==LONG:
            return -rp
        return rp

    def get_strategy_name(self):
        return self.position.strategy.name

    def get_opener(self):
        return self.position.strategy.opener

    def init_stopers(self,data,base_price):
        self.stopers = []
        for stoper in self.position.strategy.closers:
            self.stopers.append(stoper(data,base_price))

    def check_stop(self,ctick):
        is_touched = False
        for stoper in self.stopers:
            mysignal = stoper.check(ctick)
            if mysignal[0] != 0 and not self.close_lock:
                return mysignal
            if mysignal[2] != 0:
                is_touched = True
        return (False,0,is_touched)
        
    def calc_stop_price(self,base_price,tick_base):
        return self.stopers[0].calc_target_price(base_price,tick_base) if len(self.stopers)>0 else 0;

    def set_stopers_data(self,data):
        for stoper in self.stopers:
            stoper.data = data

    def get_stopers(self):
        return self.stopers

    def get_stop_valid_length(self):
        return self.stopers[0].valid_length if len(self.stopers)>0 else 0   #只取第一个

    def get_stop_direction(self):
        return utype.THOST_FTDC_D_Sell if self.direction == utype.THOST_FTDC_D_Buy else utype.THOST_FTDC_D_Buy
        #return self.stopers[0].direction if len(self.stopers)>0 else EMPTY  #只取第一个


    def release_close_lock(self):
        logging.info(u'释放平仓锁,order=%s' % self.__str__())
        self.close_lock = False

    def __str__(self):
        return u'Order_A: 合约=%s,开仓策略=%s,方向=%s,目标数=%s,开仓数=%s,状态=%s' % (self.instrument.name,
                self.get_strategy_name(),
                u'多' if self.direction==utype.THOST_FTDC_D_Buy else u'空',
                self.volume,
                self.opened_volume,
                u'已撤' if self.cancelled else u'未撤',
            )

####头寸
class Position(object):
    def __init__(self,instrument,strategy):
        self.instrument = instrument
        self.strategy = strategy
        self.orders = []    #元素为Order
        self.opened_volume = 0
        self.locked_volume = 0  #被当前头寸锁定的(包括持仓的和发出未成交的)

    def calc_open_volume(self):   
        '''
            计算Position的当次可开仓数. 与保证金无关，只计算理论数
            1. 计算当前策略的剩余可开仓数
            2. 计算当前合约的剩余可开仓数
            3. 获取策略的单次开仓数
            取1,2,3的小者

        '''
        #print 'self.strategy.max_holding:%s' % (self.strategy.max_holding,)
        #print 'in calc_open_volume,self=%s,self.name=%s' % (str(self),self.instrument.name)
        logging.info(u'P_COV_1:计算头寸可开仓数,%s:Pos=%s' % (self.instrument.name,str(self)))
        self.re_calc()
        #剩余开仓总数 = 策略持仓限量 - 已开仓数，若小于0则为0
        remained = self.strategy.max_holding - self.locked_volume if self.strategy.max_holding > self.locked_volume else 0
        #print 'remained:%s' % (remained,)
        #inst_remained = self.instrument.calc_remained_volume() #因为机制原因，计算信号时没有办法确定同期锁定的数量. 故不再这里约束
        #print 'remained:%s,inst_remained:%s' % (remained,inst_remained)
        #if remained > inst_remained:
        #    remained = inst_remained
        #本次可开仓数 = 策略单次开仓数 和 剩余开仓总数 的小者
        #print 'self.strategy.open_volume:%s' % (self.strategy.open_volume,)
        can_open = self.strategy.open_volume if self.strategy.open_volume <=  remained else remained
        logging.info(u'P_COV_2:计算头寸可开仓数完成,可开数=%s,%s:Pos=%s,策略单开数=%s,总体可开数=%s' % (can_open,self.instrument.name,str(self),self.strategy.open_volume,remained))
        return can_open

    def re_calc(self): #
        #print self.orders
        self.orders = [order for order in self.orders if not order.is_closed()]
        #print self.orders
        for mo in self.orders:
            logging.info(str(mo))
        self.opened_volume = sum([order.opened_volume for order in self.orders])
        self.locked_volume = sum([order.volume for order in self.orders])
        #print u'in re_calc:opened=%s,locked=%s,self.strategy.name=%s' % (self.opened_volume,self.locked_volume,type_name(self.strategy.opener))
        logging.info(u'P_RC_1:重算头寸，已开数=%s 策略总锁定数=%s,%s' % (self.opened_volume,self.locked_volume,str(self)))

    def add_order(self,order):
        self.orders.append(order)

    def get_locked_volume(self):    #返回已经占用数
        #print u'in get locked volume self=%s,self.name=%s' % (str(self),self.instrument.name)
        logging.info(u'P_GLV:获取头寸策略的总锁定数...,%s' % str(self))
        #总锁定数 = 开仓数 + 未成交的下单数
        self.re_calc()
        return self.locked_volume,self.opened_volume

    def __str__(self):
        return u'%s:%s:%x' % (self.instrument.name,type_name(self.strategy.opener),id(self))

##########
#策略和止损的公共基类
class Resumable(object):#可中间恢复
    #def save_parameters(self):  #保存参数. 应只允许有值参数，即字符串、数字
    #    return repr(self.__dict__)
    def save_parameters(self):  #保存参数. 只允许值参数，即字符串、数字
        parameters = []
        for key,value in self.__dict__.items():
            #print key,value,type(value)
            if type(value) == unicode:
                parameters.append(u"'%s':'%s'" % (key,value))   #这里不要多此一举，写成u"'%s':u'%s'",因为本来就是u的，如果再来一遍，就变成多搞了边encode('utf-8'),后面全乱
            elif type(value) == str:
                parameters.append(u"'%s':'%s'" % (key,value))
            elif type(value) == int:
                parameters.append(u"'%s':%d" % (key,value))
            elif type(value) == float:
                parameters.append(u"'%s':%s" % (key,value))
        return u'{%s}' % (','.join(parameters),)

    def load_parameters(self,parameters):  #重新装载参数
        #self.__dict__.update(eval(parameters))
        self.__dict__.update(parameters)

    def resume(self,data,scur_day):  #恢复opener/stop的状态,主要用于opener
        if len(data.sdate) == 0:    #史前
            return
        #elif data.sdate[-1] < scur_day:  #scur_day>data.vdate,当日还没有开始,不需要resume
        #    return
        #elif data.sdate[-1] == scur_day:
        else:
            i = len(data.sdate)-2
            while i>=0 and data.sdate[i]==scur_day:
                 i -= 1
            i += 1  #当日数据的开始
            self.dresume(data,i)
        #else:#只有在测试时可能,但也是错误情况
        #    logging.error(u'scur_day=%s,小于行情日%s' % (scur_day,data.sdate[-1]))
        pass

    def dresume(self,data,i):#min序列从i开始为当日数据
        logging.info(u'Resumable数据恢复中....')
        pass

    def dreset(self):   #日初始化动作,每日开始时系统调用,目前未实现, 目前的方式是每天初始化一个新的opener,但这样实现跨日状态就有点脱裤子放X
        pass


###突破类策略
###突破类策略以当前价为基准价，以一定额度的加价作为开仓限价以确保开仓，同时根据基准价来计算止损
'''
    check方法签名为(self,data,ctick)
    返回值为(触发标志,触发价格), 触发标志!=0时触发，触发价格==0时为当前价
'''

#MAX_OPEN_OVERFLOW = 60   #最大溢点，即开仓时加价跳数
MAX_OPEN_OVERFLOW = 30   #最大溢点，即开仓时加价跳数
MAX_CLOSE_OVERFLOW = 120
VALID_LENGTH = 120  #开仓指令持续时间.行情跳数, 至少两分钟(视行情移动为准)
STOP_VALID_LENGTH = 6   #平仓指令持续时间.最好是1秒后就撤单, 以便及时追平. 但是因为平仓回报比较慢，需要等待?

class BREAK(Resumable):    #策略标记
    pass

class LONG_BREAK(BREAK):    #多头突破策略
    direction = LONG
    def __init__(self,max_overflow=MAX_OPEN_OVERFLOW,valid_length=VALID_LENGTH):
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'多头突破基类'

    def calc_target_price(self,base_price,tick_base):    #计算开单加价
        logging.info(u'LB_CTP:base_price=%s' % base_price)
        base_price = int(base_price)
        if tick_base == 0:  #还未初始化
            return base_price + 100
        if base_price % tick_base > 0:  #取整
            base_price = (base_price / tick_base + 1) * tick_base 
        return base_price + tick_base * self.max_overflow

class SHORT_BREAK(BREAK):   #空头突破策略
    direction = SHORT
    def __init__(self,max_overflow=MAX_OPEN_OVERFLOW,valid_length=VALID_LENGTH):
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'空头突破基类'

    def calc_target_price(self,base_price,tick_base):#计算开仓加价
        logging.info(u'SB_CTP:base_price=%s' % base_price)
        base_price = int(base_price)
        if tick_base == 0:  #还未初始化
            return base_price - 100
        if base_price % tick_base > 0:
            base_price = (base_price / tick_base - 1) * tick_base
        return base_price - tick_base * self.max_overflow


###回归类策略
###回归类策略以计算所得价为基准价，并挂单来做钓鱼式成交
class ENTRY(object):    #回归策略标记
    def calc_target_price(self,base_price,tick_base):    #回归策略不加价
        base_price = int(base_price)
        return base_price

class LONG_ENTRY(ENTRY):    #多头回归策略
    def __init__(self,valid_length=VALID_LENGTH):
        self.direction = LONG
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'多头回归基类'


class SHORT_ENTRY(ENTRY):    #空头回归策略
    def __init__(self,valid_length=VALID_LENGTH):
        self.direction = SHORT
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'空头回归基类'


#####具体策略
class day_long_break(LONG_BREAK):
    def check(self,data,ctick):
        return (False,0)

class day_short_break(SHORT_BREAK):
    def check(self,data,ctick):
        return (False,0)


##止损类(平仓不允许钓鱼，必然直接平仓)
'''
    每个具体止损类必须实现三个方法
        __init__方法签名必须是(self,data,**kwargs),或者其它参数被fcustom化
        check方法签名为(self,ctick)
            必须返回(平仓标志, 基准价,止损变化标志)
            其中平仓标志:    False:不平仓, True:平仓
                         基准价为平仓基准价，将用于计算平仓限价
        calc_target_price(self,base_price,tick_base) #计算平仓限价, 其中tick_base是每跳幅度
'''

class STOPER(Resumable):    #离场类标记
    '''
        对于必须要实现断点恢复的stoper类，必须使用self.base_line和self.cur_stop作为判断标准
    '''
    def __init__(self,data,bline):
        self.cur_stop = 0
        self.data = data
        self.set_base_line(bline)

    def get_cur_stop(self):
        return self.cur_stop

    def set_cur_stop(self,cur_stop):
        self.cur_stop = cur_stop

    def get_base_line(self):
        return self.base_line

    def set_base_line(self,base_line):
        self.base_line = base_line

class LONG_STOPER(STOPER):
    def __init__(self,data,bline,max_overflow=MAX_CLOSE_OVERFLOW,valid_length=STOP_VALID_LENGTH):
        STOPER.__init__(self,data,bline)
        self.direction = SHORT
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'多头离场基类'

    def calc_target_price(self,base_price,tick_base):#计算多头平仓加价,
        logging.info(u'LS_CTP:base_price=%s' % base_price)
        base_price = int(base_price)
        if base_price % tick_base > 0:
            base_price = (base_price / tick_base - 1) * tick_base 
        return base_price - tick_base * self.max_overflow


    def check(self,tick):
        return (False,0,False)


class SHORT_STOPER(STOPER):
    def __init__(self,data,bline,max_overflow=MAX_CLOSE_OVERFLOW,valid_length=STOP_VALID_LENGTH):
        STOPER.__init__(self,data,bline)
        self.direction = LONG
        self.max_overflow = max_overflow    #溢点用于计算目标价
        self.valid_length = valid_length    #有效期用于计算撤单时间
        self.name = u'空头离场基类'

    def calc_target_price(self,base_price,tick_base):#计算空头平仓加价,
        logging.info(u'SS_CTP:base_price=%s' % base_price)
        base_price = int(base_price)
        if base_price % tick_base > 0:
            base_price = (base_price / tick_base + 1) * tick_base 
        return base_price + tick_base * self.max_overflow

    def check(self,tick):
        return (False,0,False)


class DATR_LONG_STOPER(LONG_STOPER):#日ATR多头止损
    def __init__(self,data,bline,rbase=0.12,rkeeper=0.2,rdrawdown = 0.4):
        '''data:行情对象
           bline: 价格基线
        '''
        LONG_STOPER.__init__(self,data,bline)
        self.thigh = bline
        self.ticks = 0
        self.name = u'多头日ATR止损,初始止损=%s,保本=%s,最大回撤=%s' % (rbase,rkeeper,rdrawdown)
        if data.atrd1:
            self.max_drawdown = int(data.atrd1[-1] * rdrawdown / CBASE + 0.5)
            self.keeper = int(data.atrd1[-1] * rkeeper / CBASE + 0.5)
            self.set_cur_stop(bline - int(data.atrd1[-1] * rbase / CBASE + 0.5))
        else:
            self.max_drawdown = data.cur_day.vopen /250
            self.keeper = int(self.max_drawdown * rkeeper / rdrawdown + 0.5)
            self.set_cur_stop(bline - int(self.max_drawdown*rbase/rdrawdown))
        logging.info(u'设定止损: max_drawdown=%s,keeper=%s,cur_stop=%s' % (self.max_drawdown,self.keeper,self.get_cur_stop()))

    def check(self,tick):
        '''
            必须返回(平仓标志, 基准价,stop变化标志)
            基准价为0则为当前价
        '''
        stop_changed = False
        if tick.price < self.get_cur_stop():
            return (True,tick.price,stop_changed)
        if self.get_cur_stop()< self.get_base_line() and tick.price > self.get_base_line() + self.keeper:
            ##提升保本
            self.set_cur_stop(self.get_base_line())
            stop_changed = True
        if tick.price > self.thigh:
            self.thigh = tick.price
            if self.thigh - self.max_drawdown > self.get_cur_stop():
                self.set_cur_stop(self.thigh - self.max_drawdown)
                stop_changed = True
        return (False,self.get_base_line(),stop_changed)

class DATR_SHORT_STOPER(SHORT_STOPER):#日ATR空头止损
    def __init__(self,data,bline,rbase=0.12,rkeeper=0.2,rdrawdown = 0.4):
        SHORT_STOPER.__init__(self,data,bline)
        self.tlow = bline
        self.itime = len(self.data.sclose)  #time的索引，用于计算耗时
        self.name = u'空头日ATR止损,初始止损=%s,保本=%s,最大回撤=%s' % (rbase,rkeeper,rdrawdown)
        if data.atrd1:
            self.max_drawdown = int(data.atrd1[-1] * rdrawdown / CBASE + 0.5)
            self.keeper = int(data.atrd1[-1] * rkeeper / CBASE + 0.5)
            self.set_cur_stop(bline + int(data.atrd1[-1] * rbase / CBASE + 0.5))
        else:
            self.max_drawdown = data.cur_day.vopen /250
            self.keeper = int(self.max_drawdown * rkeeper / rdrawdown + 0.5)
            self.set_cur_stop(bline + int(self.max_drawdown*rbase/rdrawdown))
            
    def check(self,tick):
        '''
            必须返回(平仓标志, 基准价,stop变化标志)
            基准价为0则为当前价
        '''
        stop_changed = False
        if tick.price > self.get_cur_stop():
            return (True,tick.price,stop_changed)
        if self.get_cur_stop()> self.get_base_line() and tick.price < self.get_base_line() - self.keeper:
            ##提升保本
            self.set_cur_stop(self.get_base_line())
            stop_changed = True
        if tick.price < self.tlow:
            self.tlow = tick.price
            if self.tlow + self.max_drawdown < self.get_cur_stop():
                self.set_cur_stop(self.tlow + self.max_drawdown)
                stop_changed = True
        return (False,self.get_base_line(),stop_changed)


datr_long_stoper_12 = fcustom(DATR_LONG_STOPER,rbase=0.12)
datr_short_stoper_12 = fcustom(DATR_SHORT_STOPER,rbase=0.12)

class LONG_MOVING_STOPER(LONG_STOPER):
    '''
        简化的移动跟踪止损, 达到快速提升止损和和逐步放开盈利端的平衡
    '''
    def __init__(self,data,bline,flost_base=lambda x:100,max_drawdown=360,pmax_drawdown=0.011,tstep=40,vstep=20):
        '''
           data:行情对象
           bline: 价格基线
           max_drawdown: 最大回撤
           pmax_drawdown: 最大回撤比例(相对开仓价)
        '''
        LONG_STOPER.__init__(self,data,bline)
        self.lost_base = flost_base(data.cur_day.vopen)
        self.ticks = 0
        self.set_cur_stop(bline - self.lost_base)
        self.stop0 = bline - self.lost_base
        self.name = u'多头移动止损,初始止损=%s,步长=%s/%s,最大回撤=%s' % (self.stop0,vstep,tstep,max_drawdown)
        self.thigh = bline
        self.tstep = tstep
        self.vstep = vstep

        #self.max_drawdown = max_drawdown
        #self.pmax_drawdown = pmax_drawdown
        pmd = pmax_drawdown * bline
        self.cmax_drawdown =  pmd if pmd < max_drawdown else max_drawdown   #最大回撤取小者
        logging.info(self.name)

    def check(self,tick):
        '''
            必须返回(平仓标志, 基准价,stop变化标志)
            基准价为0则为当前价
        '''
        stop_changed = False
        if tick.price < self.get_cur_stop():
            logging.info(u'LMS_C:tick.time=%s,tick.min1=%s,tick.price=%s,cur_stop=%s' % (tick.time,tick.min1,tick.price,self.get_cur_stop()))
            return (True,tick.price,stop_changed)
        if tick.price > self.thigh:
            self.thigh = tick.price
            nstop = self.stop0 + (tick.price - self.base_line) / self.tstep * self.vstep
            m_nstop = tick.price - self.cmax_drawdown
            if m_nstop > nstop:
                nstop = m_nstop
            if nstop > self.get_cur_stop():
                logging.info(u'移动平仓位置，新高点=%s,原平仓点=%s,现平仓点=%s' % (tick.price,self.get_cur_stop(),nstop))
                self.set_cur_stop(nstop)
                stop_changed = True
        return (False,self.get_base_line(),stop_changed)


class SHORT_MOVING_STOPER(SHORT_STOPER):#空头移动止损
    def __init__(self,data,bline,flost_base=lambda x:100,max_drawdown=360,pmax_drawdown=0.011,tstep=40,vstep=20):
        '''
           data:行情对象
           bline: 价格基线
        '''
        SHORT_STOPER.__init__(self,data,bline)
        #self.lost_base = lost_base
        self.lost_base = flost_base(data.cur_day.vopen)
        self.ticks = 0
        self.set_cur_stop(bline + self.lost_base)
        self.stop0 = bline + self.lost_base
        self.name = u'空头移动止损,初始止损=%s,步长=%s/%s,最大回撤=%s' % (self.stop0,vstep,tstep,max_drawdown)
        self.tlow = bline
        self.vstep = vstep
        self.tstep = tstep

        #self.max_drawdown = max_drawdown
        #self.pmax_drawdown = pmax_drawdown
        pmd = pmax_drawdown * bline
        self.cmax_drawdown =  pmd if pmd < max_drawdown else max_drawdown   #最大回撤取小者
        logging.info(self.name)

    def check(self,tick):
        '''
            必须返回(平仓标志, 基准价,stop变化标志)
            基准价为0则为当前价
        '''
        stop_changed = False
        if tick.price > self.get_cur_stop():
            return (True,tick.price,stop_changed)
        if tick.price < self.tlow:
            self.tlow = tick.price
            nstop = self.stop0 - (self.base_line - tick.price) / self.tstep * self.vstep    
            m_nstop = tick.price + self.cmax_drawdown
            if m_nstop < nstop:
                nstop = m_nstop
            #nstop = self.stop0 + (tick.price - self.base_line) / self.tstep * self.vstep    #不能这样，因为tick.price<self.base_line,所以会有四舍五入问题，-0.12舍入成-1
            if nstop < self.get_cur_stop():
                logging.info(u'移动平仓位置，新低点=%s,原平仓点=%s,现平仓点=%s,cur_price=%s,self.base_line=%s,stop0=%s' % (tick.price,self.get_cur_stop(),nstop,tick.price,self.base_line,self.stop0))
                #logging.info(u'dp=%s,dp/tstep=%s' %(tick.price - self.base_line,(tick.price - self.base_line) / self.tstep))
                self.set_cur_stop(nstop)
                logging.info(u'cur_stop=%s' %(self.cur_stop,))
                stop_changed = True
        return (False,self.get_base_line(),stop_changed)

if_lmv_stoper = LONG_MOVING_STOPER
if_smv_stoper = SHORT_MOVING_STOPER

if_lmv_stoper_250_42 = fcustom(LONG_MOVING_STOPER,
                flost_base = lambda p:p/250, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 40,     
                vstep = 20,                  
            )

if_lmv_stoper_250_84 = fcustom(LONG_MOVING_STOPER,
                flost_base = lambda p:p/250, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 80,     
                vstep = 40,                  
            )

if_lmv_stoper_250_21 = fcustom(LONG_MOVING_STOPER,
                flost_base = lambda p:p/250, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 20,     
                vstep = 10,                  
            )

if_lmv_stoper_300_42 = fcustom(LONG_MOVING_STOPER,
                flost_base = lambda p:p/300, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 40,     
                vstep = 20,                  
            )


if_lmv_stoper_300_21 = fcustom(LONG_MOVING_STOPER,
                flost_base = lambda p:p/300, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 20,     
                vstep = 10,                  
            )

if_lmv_stoper_400_21 = fcustom(LONG_MOVING_STOPER,
                flost_base = lambda p:p/400, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 20,     
                vstep = 12, #特殊
            )

if_lmv_stoper_666_21 = fcustom(LONG_MOVING_STOPER,
                flost_base = lambda p:p/666, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 20,     
                vstep = 10,                  
            )

if_smv_stoper_250_42 = fcustom(SHORT_MOVING_STOPER,
                flost_base = lambda p:p/250, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 40,     
                vstep = 20,                  
            )


if_smv_stoper_250_21 = fcustom(SHORT_MOVING_STOPER,
                flost_base = lambda p:p/250, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 20,     
                vstep = 10,                  
            )

if_smv_stoper_300_42 = fcustom(SHORT_MOVING_STOPER,
                flost_base = lambda p:p/300, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 40,     
                vstep = 20,                  
            )


if_smv_stoper_300_21 = fcustom(SHORT_MOVING_STOPER,
                flost_base = lambda p:p/300, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 20,     
                vstep = 10,                  
            )

if_smv_stoper_400_21 = fcustom(SHORT_MOVING_STOPER,
                flost_base = lambda p:p/400, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 20,     
                vstep = 12, #特殊
            )

if_smv_stoper_666_21 = fcustom(SHORT_MOVING_STOPER,
                flost_base = lambda p:p/666, 
                max_drawdown = 360, 
                pmax_drawdown = 0.011, 
                tstep = 20,     
                vstep = 10,                  
            )


class LONG_TIME_STOPER(LONG_STOPER):
    '''
        时间平仓,多
    '''
    def __init__(self,data,bline,stime=1500):
        '''
           data:行情对象
           bline: 价格基线
        '''
        LONG_STOPER.__init__(self,data,bline)
        self.stime = stime
        self.name = u'多头时间离场'
        logging.info(self.name)

    def check(self,tick):
        '''
            必须返回(平仓标志, 基准价,stop变化标志)
            基准价为0则为当前价
        '''
        if tick.min1 >= self.stime:
            logging.info(u'LTS_C:tick.time=%s,tick.min1=%s,tick.price=%s,cur_stop=%s' % (tick.time,tick.min1,tick.price,self.get_cur_stop()))
            return (True,tick.price,False)
        return (False,self.get_base_line(),False)

if_ltime_stoper = fcustom(LONG_TIME_STOPER,stime=1459)
c_ltime_stoper = fcustom(LONG_TIME_STOPER,stime=1444)

class SHORT_TIME_STOPER(SHORT_STOPER):
    '''
        时间平仓, 空
    '''
    def __init__(self,data,bline,stime=1500):
        '''
           data:行情对象
           bline: 价格基线
        '''
        SHORT_STOPER.__init__(self,data,bline)
        self.stime = stime
        self.name = u'空头时间离场'
        logging.info(self.name)

    def check(self,tick):
        '''
            必须返回(平仓标志, 基准价,stop变化标志)
            基准价为0则为当前价
        '''
        if tick.min1 >= self.stime:
            logging.info(u'LTS_C:tick.time=%s,tick.min1=%s,tick.price=%s,cur_stop=%s' % (tick.time,tick.min1,tick.price,self.get_cur_stop()))
            return (True,tick.price,False)
        return (False,self.get_base_line(),False)

if_stime_stoper = fcustom(SHORT_TIME_STOPER,stime=1459)
c_stime_stoper = fcustom(SHORT_TIME_STOPER,stime=1444)

class LONG_LAST_STOPER(LONG_STOPER):
    '''
        时间平仓,多
    '''
    def __init__(self,data,bline,ttrace=240,tend=266,vbegin=0.01,vmm=30):
        '''
           data:行情对象
           bline: 价格基线
           ttrace: 开始线 iorder
           tend: 中止线 iorder
           vbegin:止损比例
        '''
        LONG_STOPER.__init__(self,data,bline)
        self.ttrace = ttrace
        self.tend = tend
        self.vbegin = vbegin
        self.vmm = vmm
        opend = data.cur_day.vopen
        self.vmax_stop = opend * vbegin
        self.vstep = self.vmax_stop / (tend - ttrace)
        self.htrace = self.calc_htrace(data)
        self.set_cur_stop(self.htrace -  (self.vmax_stop - (data.siorder[-1]+1-self.ttrace+1) * self.vstep) #+1成为当前iorder
                if data.siorder[-1] >= ttrace else 0
            )
        self.name = u'多头直线离场'
        logging.info(self.name)

    def check(self,tick):
        '''
            必须返回(平仓标志, 基准价,stop变化标志)
            基准价为0则为当前价
        '''
        stop_changed = False
        if tick.iorder < self.ttrace + 1:
            return (False,tick.price,False)
        if tick.price < self.get_cur_stop() or tick.iorder >= self.tend-1:
            return (True,tick.price,False)
            #return (True,self.get_cur_stop(),False)    #不能用这个，这个有小数风险
        if tick.switch_min:
            if tick.iorder-1 == self.ttrace:
                self.htrace = self.calc_htrace(self.data)
            self.set_cur_stop(self.htrace -  (self.vmax_stop - (tick.iorder-self.ttrace+1) * self.vstep) 
                    #if tick.iorder-1 >= self.ttrace else 0
                )
            stop_changed = True
            logging.info(u'LLS:C1 止损位变化:%s' % (self.get_cur_stop(),))
            #print tick.iorder,self.data.siorder[-1],self.ttrace,self.htrace,self.vmax_stop,self.vstep,self.get_cur_stop(),(tick.iorder-1-self.ttrace+1) * self.vstep
        if tick.price > self.htrace:
            self.htrace = tick.price
            self.set_cur_stop(self.htrace -  (self.vmax_stop - (tick.iorder-self.ttrace+1) * self.vstep) 
                    #if tick.iorder-1 >= self.ttrace else 0
                )
            logging.info(u'LLS:C2 止损位变化:%s' % (self.get_cur_stop(),))
            stop_changed = True
        return (False,self.get_base_line(),stop_changed)

    def calc_htrace(self,data):
        if data.siorder[-1] < self.ttrace:
            return 0
        elif data.siorder[-1] == self.ttrace:#可以合入下一判断
            return max(data.shigh[-self.vmm:])
        elif data.siorder[-1] > self.ttrace:
            i = len(data.siorder) - 1
            while data.siorder[i] > self.ttrace and i>0:
                i -= 1
            if i < 0:   #不应当出现
                return 0
            return max(data.shigh[i-30+1:i+1])

if_llast_stoper = fcustom(LONG_LAST_STOPER,ttrace=240,tend=266,vbegin=0.02,vmm=30)

class SHORT_LAST_STOPER(SHORT_STOPER):
    '''
        时间平仓,多
    '''
    def __init__(self,data,bline,ttrace=240,tend=266,vbegin=0.01,vmm=30):
        '''
           data:行情对象
           bline: 价格基线
           ttrace: 开始线 iorder
           tend: 中止线 iorder
           vbegin:止损比例
        '''
        SHORT_STOPER.__init__(self,data,bline)
        self.ttrace = ttrace
        self.tend = tend
        self.vbegin = vbegin
        self.vmm = vmm
        opend = data.cur_day.vopen
        self.vmax_stop = opend * vbegin
        self.vstep = self.vmax_stop / (tend - ttrace)
        self.ltrace = self.calc_ltrace(data)
        self.set_cur_stop(self.ltrace +  (self.vmax_stop - (data.siorder[-1]+1-self.ttrace+1) * self.vstep) #+1成为当前iorder
                if data.siorder[-1] >= ttrace else 99999999
            )
        self.name = u'空头直线离场'
        logging.info(self.name)

    def check(self,tick):
        '''
            必须返回(平仓标志, 基准价,stop变化标志)
            基准价为0则为当前价
        '''
        if tick.iorder < self.ttrace + 1:
            return (False,tick.price,False)
        if tick.price > self.get_cur_stop() or tick.iorder >= self.tend-1:
            return (True,tick.price,False)
            #return (True,self.get_cur_stop(),False)    #不能用这个，这个有小数风险
        if tick.switch_min:
            if tick.iorder-1 == self.ttrace:
                self.ltrace = self.calc_ltrace(self.data)
            self.set_cur_stop(self.ltrace +  (self.vmax_stop - (tick.iorder-self.ttrace+1) * self.vstep)
                    #if tick.iorder-1 >= self.ttrace else 99999999
                )
            #print tick.iorder,self.data.siorder[-1],self.ttrace,self.ltrace,self.vmax_stop,self.vstep,self.get_cur_stop(),(tick.iorder-1-self.ttrace+1) * self.vstep
            logging.info(u'SLS:C1 止损位变化:%s' % (self.get_cur_stop(),))
        if tick.price < self.ltrace:
            self.ltrace = tick.price
            self.set_cur_stop(self.ltrace +  (self.vmax_stop - (tick.iorder-self.ttrace+1) * self.vstep)
                    #if tick.iorder-1 >= self.ttrace else 99999999
                )
            logging.info(u'SLS:C2 止损位变化:%s' % (self.get_cur_stop(),))
            #print tick.iorder,self.data.siorder[-1],self.ttrace,self.ltrace,self.vmax_stop,self.vstep,self.get_cur_stop(),(tick.iorder-1-self.ttrace+1) * self.vstep
        return (False,self.get_base_line(),False)

    def calc_ltrace(self,data):
        if data.siorder[-1] < self.ttrace:
            return 99999999
        elif data.siorder[-1] == self.ttrace:#可以合入下一判断
            return min(data.slow[-self.vmm:])
        elif data.siorder[-1] > self.ttrace:
            i = len(data.siorder) - 1
            while data.siorder[i] > self.ttrace and i>0:
                i -= 1
            if i < 0:   #不应当出现
                return 99999999
            return min(data.slow[i-30+1:i+1])

if_slast_stoper = fcustom(SHORT_LAST_STOPER,ttrace=250,tend=266,vbegin=0.02,vmm=30)


class STRATEGY(object):#策略基类, 单纯包装
    def __init__(self,
                name,
                opener, #开仓类(注意，不是对象)
                closers, #平仓类(注意，不是对象)
                open_volume, #每次开仓手数   
                max_holding, #最大持仓手数 
            ):
        self.name = name
        self.opener_class = opener
        self.opener = opener()  #单一策略可共享开仓对象
        self.closers = closers    #平仓对象必须用开仓时的上下文初始化
        self.open_volume = open_volume
        self.max_holding = max_holding
        self.direction = self.opener.direction

    def get_name(self):
        return u'%s_%s_%s_%s' % (self.opener.name,self.closer.name,self.open_volume,self.max_holding)
