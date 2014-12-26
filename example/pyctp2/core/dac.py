#-*- coding: utf-8 -*-

import operator

from collections import (
        deque,
    )


from ..common.base import (
        BaseObject,
        TICK,
        MAX_VALUE,
        FINALIZE_DAY,
        ZERO_TICK,
        TMinute,
    )

#from ..common.indicator_pre import indicator
from ..common.indicator import Indicator

from ..common.utils import (
        fcustom,
    )


###############
# 基本序列运算
###############

class OPER1(Indicator):
    def __init__(self,source,oper):
        """
            没有用处,便于理解
            如果去掉,则后面的
                NEG = fcustom(OPER1,oper=operator.neg)
                则很难理解
        """
        pass

    def calc(self,source,oper):
        for i in range(len(self),len(source)):
            self.append(oper(source[i]))

        return self

'''
    不同的operator.xxx, 使OPER1下缓存的key不同，不会导致混淆
'''
NEG = fcustom(OPER1,oper=operator.neg)
ABS = fcustom(OPER1,oper=operator.abs)
NOT = fcustom(OPER1,oper=operator.not_)

class OPER2(Indicator):
    def __init__(self,source1,source2,oper):
        """
            没有用处,便于理解
            如果去掉,则后面的
                NEG = fcustom(OPER1,oper=operator.neg)
                则很难理解
        """
        pass

    def calc(self,source1,source2,oper):
        len1,len2 = len(source1),len(source2)
        clen = len1 if len1 <= len2 else len2
        for i in range(len(self),clen):
            self.append(oper(source1[i],source2[i]))
        return self


ADD = fcustom(OPER2,oper=operator.add)
SUB = fcustom(OPER2,oper=operator.sub)
MUL = fcustom(OPER2,oper=operator.mul)
#AND = fcustom(OPER2,oper=operator.and_)    #这个是位操作
#OR = fcustom(OPER2,oper=operator.or_)      #这个是位操作
#XOR = fcustom(OPER2,oper=operator.xor)     #这个是位操作
LT = fcustom(OPER2,oper=operator.lt)
LE = fcustom(OPER2,oper=operator.le)
EQ = fcustom(OPER2,oper=operator.eq)
GT = fcustom(OPER2,oper=operator.gt)
GE = fcustom(OPER2,oper=operator.ge)

class OPER21(Indicator):
    def __init__(self,source1,vs,oper):
        """
            没有用处,便于理解
            如果去掉,则后面的
                NEG = fcustom(OPER1,oper=operator.neg)
                则很难理解
        """
        pass

    def calc(self,source1,vs,oper):
        for i in range(len(self),len(source1)):
            #print('new data:',source1[i])
            self.append(oper(source1[i],vs))

        return self

ADD1 = fcustom(OPER21,oper=operator.add)
SUB1 = fcustom(OPER21,oper=operator.sub)
MUL1 = fcustom(OPER21,oper=operator.mul)
#AND1 = fcustom(OPER21,oper=operator.and_)  #这个是位操作
#OR1 = fcustom(OPER21,oper=operator.or_)    #这个是位操作
#XOR1 = fcustom(OPER21,oper=operator.xor)   #这个是位操作
LT1 = fcustom(OPER21,oper=operator.lt)
LE1 = fcustom(OPER21,oper=operator.le)
EQ1 = fcustom(OPER21,oper=operator.eq)
GT1 = fcustom(OPER21,oper=operator.gt)
GE1 = fcustom(OPER21,oper=operator.ge)

class AND(Indicator):
    def calc(self,source1,source2):
        len1,len2 = len(source1),len(source2)
        clen = len1 if len1 <= len2 else len2
        for i in range(len(self),clen):
            #print('new data:',source1[i],source2[i])
            self.append((source1[i] and source2[i])!=0)
        return self

class GAND(Indicator):
    def __init__(self,*args):
        assert len(args)>0,'GAND params number must more than 0'
        pass

    def calc(self,*args):
        mlen = min([len(a) for a in args])
        for i in range(len(self),mlen):
            rv = all([vs[i] for vs in args])
            self.append(rv!=0)
        return self


class GOR(Indicator):
    def __init__(self,*args):
        assert len(args)>0,'GAND params number must more than 0'
        pass

    def calc(self,*args):
        mlen = min([len(a) for a in args])
        for i in range(len(self),mlen):
            rv = any([vs[i] for vs in args])
            self.append(rv!=0)
        return self

class DIV(Indicator):
    def calc(self,source1,source2):
        len1,len2 = len(source1),len(source2)
        clen = len1 if len1 <= len2 else len2
        for i in range(len(self),clen):
            r = source1[i]/source2[i] if source2[i] != 0 else MAX_VALUE
            self.append(r)
        return self


class DIV1(Indicator):
    def __init__(self,source1,vs):
        assert vs!=0,'divisor vs == 0'

    def calc(self,source1,vs):
        for i in range(len(self),len(source1)):
            r = source1[i]/vs
            self.append(r)
        return self

############
# 常用指标
############

class ACCUMULATE(Indicator):
    def calc(self,source):
        mylen = len(self)
        ss = self[-1] if mylen>0 else 0
        #print(len(source),mylen,ss,self,id(source))
        for i in range(mylen,len(source)):
            ss += source[i]
            self.append(ss)
        #print(id(_ts),id(source),source,_ts.sa)
        return self


NSUM = ACCUMULATE
#class NSUM(ACCUMULATE):pass     #避免unittest中缓存冲突,但这个不是本质解决办法.

class MSUM(Indicator):
    def calc(self,source,mlen):
        ss = ACCUMULATE(source)
        for i in range(len(self),len(source)):
            v = ss[i] - ss[i-mlen] if i>=mlen else ss[i]
            self.append(v)
        return self


class MA(Indicator):
    def __init__(self,source,mlen):
        assert mlen>0,'mlen should > 0'
        pass

    def calc(self,source,mlen):
        ms = MSUM(source,mlen)
        for i in range(len(self),len(source)):
            #当累计个数<nlen时，求其平均值，而不是累计值/mlen
            rlen = mlen if i>=mlen else i+1
            self.append(ms[i]/rlen)
        return self

class MA2(Indicator):
    def __init__(self,source,mlen):
        assert mlen>0,'mlen should > 0'
        self.sa = [0] * mlen

    def calc(self,source,mlen):
        slen = len(self)
        ss = self.sa[-1]
        for i in range(slen,len(source)):
            ss += source[i]
            self.sa.append(ss)
            #print(ss,_ts.sa[i-mlen])
            #当累计个数<nlen时，求其平均值，而不是累计值/mlen
            rlen = mlen if mlen < i+1 else i+1
            self.append((ss-self.sa[-rlen-1])/rlen)
        #print(_ts.sa)
        return self

class NMA(Indicator):
    def __init__(self,source):
        self._sa = [0]

    def calc(self,source):
        mylen = len(self)
        ss = self._sa[-1]
        for i in range(mylen,len(source)):
            ss += source[i]
            self._sa.append(ss)
            #print(ss,_ts.sa[-1])
            self.append(ss/(i+1))
        #print(_ts.sa)
        return self


class CEXPMA(Indicator):
    def __init__(self,source,mlen):
        assert mlen>0,'mlen should > 0'
        pass

    def calc(self,source,mlen):
        if len(source) == 0:
            return self
        cur = self[-1] if len(self)>0 else source[0]    #哨兵元素是source[0]，确保计算得到的值在<mlen元素的情况下也正确
        for i in range(len(self),len(source)):
            cur = (source[i]*2 + cur*(mlen-1))/(mlen+1)
            self.append(cur)
        return self

EMA = CEXPMA


class MACD(Indicator):
    def __init__(self,source,ifast=12,islow=26,idiff=9):
        self._diff = []
        self._dea = []

    def calc(self,source,ifast=12,islow=26,idiff=9):
        sfast = EMA(source,ifast)
        sslow = EMA(source,islow)
        self._diff = SUB(sfast,sslow)
        self._dea = EMA(self._diff,idiff)
        return self

    @property
    def diff(self):
        return self._diff

    @property
    def dea(self):
        return self._dea


class TR(Indicator):
    def calc(self,sclose,shigh,slow):
        assert len(sclose) == len(shigh) == len(slow),"sclose,shigh,slow等项数据必须同步"
        if len(sclose) == 0:
            return self
        if len(self) == 0:
            self.append(shigh[0]-slow[0])
        for i in range(len(self),len(sclose)):
            #c,h,l = sclose[slen-1],shigh[slen],sclose[slen]
            hh = shigh[i] if shigh[i] > sclose[i-1] else sclose[i-1]
            ll = slow[i] if slow[i] < sclose[i-1] else sclose[i-1]
            self.append(hh-ll)
        return self


class ATR(Indicator):
    def calc(self,sclose,shigh,slow,length=20):
        ltr = TR(sclose,shigh,slow)
        atr =  CEXPMA(ltr,length)
        #for i in range(len(self),len(atr)):
        #    self.append(atr[i])
        return atr

class XATR(Indicator):
    def calc(self,sclose,shigh,slow,length=20):
        latr = ATR(sclose,shigh,slow,length)
        return DIV(latr,sclose)


class STREND(Indicator):
    """
        简单累积趋势2
        与strend相比，上升过程中，平也当作上,下降中平作下
        若当前趋势为上升或0，trend值为n>0
        则新trend值为：
            n+1 当前值 >= pre
            -1  当前值 < pre
        若当前趋势为下降，trend值为n(负数)
        则下一trend值为：
            n-1 当前值 <= pre
            1   当前值 > pre
        0为初始趋势(缺少判断时)
    """
    def calc(self,source):
        if len(source) == 0:
            return self
        if len(self) == 0:
            self.append(0)

        slen = len(self)
        scur = self[-1]
        vpre = source[slen-1]
        for i in range(slen,len(source)):
            vcur = source[i]
            if vcur > vpre:
                scur = scur + 1 if scur > 0 else 1
            elif vcur < vpre:
                scur = scur - 1 if scur < 0 else -1
            else: #curv == pre_v
                scur = scur + 1 if scur >= 0 else scur-1 #最初为0时，也算上升
            self.append(scur)
            vpre = vcur
        return self


class TMM(Indicator):
    def __init__(self,source,covered,vmm,fcmp,fgroup):
        self._buffer = None

    def calc(self,source,covered,vmm,fcmp,fgroup):
        if len(source) == 0:
            return self
        slen = len(source)
        pre_len = slen if slen <= covered else covered
        cmm = self[-1] if self else vmm
        for i in range(len(self),pre_len):
            if fcmp(source[i],cmm):
                cmm = source[i]
            self.append(cmm)
        if slen <= covered:
            return self
        tlen = len(self)
        if self._buffer:
            buffer = self._buffer
        else:
            buffer = self._buffer = deque(source[tlen-covered:tlen])
        #print('in tmm:tlen=%s,len(source)=%s' % (tlen,len(source)))
        for i in range(tlen,len(source)):
            v = source[i]
            buffer.append(v)
            vquit=buffer.popleft()
            if fcmp(v,cmm):
                cmm = v
            if cmm == vquit and v != cmm: #退出的正好是最大值,计算前covered-1个元素的最大值, pre=source[i-1]
                #cmm = fgroup(source[i-covered+1:i+1])
                cmm = fgroup(buffer)
            self.append(cmm)
        return self

TMAX = fcustom(TMM,vmm=-MAX_VALUE,fcmp=operator.gt,fgroup=max)
TMIN = fcustom(TMM,vmm=MAX_VALUE,fcmp=operator.lt,fgroup=min)

class NMM(Indicator):
    """
        从index0算起的极值.
        相当于covered取最大值时的TMM
    """
    def calc(self,source,vmm,fcmp):
        if len(source) == 0:
            return self
        slen = len(source)
        cmm = self[-1] if self else vmm
        for i in range(len(self),len(source)):
            if fcmp(source[i],cmm):
                cmm = source[i]
            self.append(cmm)
        return self

NMAX = fcustom(NMM,vmm=-MAX_VALUE,fcmp=operator.gt)
NMIN = fcustom(NMM,vmm=MAX_VALUE,fcmp=operator.lt)

class CROSS(Indicator):
    def calc(self,source1,source2,rcmp):
        len1,len2 = len(source1),len(source2)
        clen = len1 if len1 <= len2 else len2
        if clen == 0:
            return self
        if len(self) == 0:
            self.append(1 if rcmp(source2[0],source1[0]) else 0)   #第一个取决于状态，如果为已×，则为1
        ps = self[-1]
        for i in range(len(self),len(source1)):
            cs = rcmp(source2[i],source1[i])
            self.append(1 if not ps and cs else 0)
            ps = cs
        return self

UPCROSS = fcustom(CROSS,rcmp = operator.gt) #追击-平-平-超越，以及超越-平-超越均算×
DOWNCROSS = fcustom(CROSS,rcmp = operator.lt) #追击-平-平-超越，以及超越-平-超越均算×


class NCROSS(Indicator):
    def calc(self,source,target,rcmp):
        if len(source) == 0:
            return self
        if len(self) == 0:
            self.append(1 if rcmp(source[0],target) else 0)   #第一个取决于状态，如果为已×，则为1
        ps = self[-1]
        for i in range(len(self),len(source)):
            cs = rcmp(source[i],target)
            self.append(1 if not ps and cs else 0)
            ps = cs
        return self

NUPCROSS = fcustom(NCROSS,rcmp = operator.gt) #追击-平-平-超越，以及超越-平-超越均算×
NDOWNCROSS = fcustom(NCROSS,rcmp = operator.lt) #追击-平-平-超越，以及超越-平-超越均算×


class REF(Indicator):
    """
        取得偏移为offset的序列
        前offset部分用第一元素填充
        如果仅用于比较,不建议用这个函数,而直接用[-1]下标比较
        只有在偏移CROSS时才有意义
    """
    def calc(self,source,offset=1):
        if len(source) == 0:
            return self
        if len(self) == 0:
            self.append(source[0])
        for i in range(len(self),offset if offset <= len(source) else len(source)):
            self.append(source[0])

        for i in range(len(self),len(source)):
            self.append(source[i-offset])

        return self

class UNIT_ATTR(Indicator):
    def calc(self,units,afunc):
        for i in range(len(self),len(units)):
            self.append(afunc(units[i]))

        return self


UNIT_instrument = lambda unit:unit.instrument
UNIT_date = lambda unit:unit.date
UNIT_price = lambda unit:unit.price
UNIT_min1 = lambda unit:unit.min1
UNIT_sec = lambda unit:unit.sec
UNIT_msec = lambda unit:unit.msec
UNIT_time = lambda unit:unit.time
UNIT_dvolume = lambda unit:unit.dvolume
UNIT_damount = lambda unit:unit.damount
UNIT_holding = lambda unit:unit.holding
UNIT_high = lambda unit:unit.high
UNIT_low = lambda unit:unit.low
UNIT_bid_price = lambda unit:unit.bid_price
UNIT_bid_volume = lambda unit:unit.bid_volume
UNIT_ask_price = lambda unit:unit.ask_price
UNIT_ask_volume = lambda unit:unit.ask_volume

TICK_INSTRUMENT = fcustom(UNIT_ATTR,afunc=UNIT_instrument)
TICK_DATE = fcustom(UNIT_ATTR,afunc=UNIT_date)
TICK_PRICE = fcustom(UNIT_ATTR,afunc=UNIT_price)
TICK_MIN1 = fcustom(UNIT_ATTR,afunc=UNIT_min1)
TICK_SEC = fcustom(UNIT_ATTR,afunc=UNIT_sec)
TICK_MSEC = fcustom(UNIT_ATTR,afunc=UNIT_msec)
TICK_TIME = fcustom(UNIT_ATTR,afunc=UNIT_time)
TICK_DVOLUME = fcustom(UNIT_ATTR,afunc=UNIT_dvolume)
TICK_DAMOUNT = fcustom(UNIT_ATTR,afunc=UNIT_damount)
TICK_HOLDING = fcustom(UNIT_ATTR,afunc=UNIT_holding)
TICK_HIGH = fcustom(UNIT_ATTR,afunc=UNIT_high)
TICK_LOW = fcustom(UNIT_ATTR,afunc=UNIT_low)
TICK_BID_PRICE = fcustom(UNIT_ATTR,afunc=UNIT_bid_price)
TICK_BID_VOLUME = fcustom(UNIT_ATTR,afunc=UNIT_bid_volume)
TICK_ASK_PRICE = fcustom(UNIT_ATTR,afunc=UNIT_ask_price)
TICK_ASK_VOLUME = fcustom(UNIT_ATTR,afunc=UNIT_ask_volume)

"""
    周期缩放示例
"""
class MINUTE(Indicator):
    def __init__(self,ticks,spre_min1=None):
        """
            如果spre_min1不为None，调用者需保证ticks[0].min1 > spre_min1.stime

            分钟第一tick的新增成交量归于本分钟

            特别注意modified只在处理基准为离散的ticks时才有意义
            如果调用期间有多个ticks连续到达且跨分钟,就会导致modified标志错误
            实际使用中如果从ticks为基准订阅数据,则不会存在这个问题. 也就是说跨周期计算必须从ticks为起点
        """
        #assert len(ticks) > 0
        ticks.register(self)
        if spre_min1:
            self.extend(spre_min1)
        self._ilast = 0      #指向ticks中已计算过元素的后一个位置
        self._next_is_new_day = False #日结束后的重置标志
        self._modified = False    #上周期完成标志
        self._last_dvolume = 0
        self._last_damount = 0
        self._cur = ZERO_TICK

    @property
    def modified(self):
        return self._modified

    @property
    def next_is_new_day(self):
        return self._next_is_new_day

    def notify_truncated(self,truncated_size):
        self._ilast -= truncated_size
        if self._ilast < 0:
            self._ilast = 0

    def remove_part(self,remains=0):
        if remains == 0:    #全部删除
            self[:] = []
        elif remains < len(self):
            self[:-remains] = []
        elif remains >= len(self):  #减少思考代价,和条件2可以合一
            pass

    def calc(self,ticks,spre_min1=None):
        if len(ticks) == 0:
            return self
        if self._cur == ZERO_TICK:
            #self._cur = BaseObject(sopen = ticks[0].price,
            self._cur = TMinute(sopen = ticks[0].price,
                             sclose = ticks[0].price,
                             shigh=ticks[0].price,
                             slow=ticks[0].price,
                             svolume = 0,
                             samount = 0,
                             sholding = ticks[0].holding,
                             stime=ticks[0].min1,    #当日第一min1
                             sdate=ticks[0].date,
                             stdate = ticks[0].tdate,
                     )

        cur_minute = self._cur
        for i in range(self._ilast,len(ticks)):
            tcur = ticks[i]
            #print(tcur.date,tcur.min1,cur_minute.stime)
            #print("++++++++++++",tcur.date,tcur.time,tcur.min1)
            #if tcur.min1 > cur_minute.stime or tcur.tdate > cur_minute.stdate:
            if tcur.min1 > cur_minute.stime or tcur.date > cur_minute.sdate:
                pre_minute = cur_minute
                #cur_minute = BaseObject(sdate=tcur.date,stime=tcur.min1,stdate=tcur.tdate,
                cur_minute = TMinute(sdate=tcur.date,stime=tcur.min1,stdate=tcur.tdate,
                                      sopen=tcur.price,sclose=tcur.price,shigh=tcur.price,slow=tcur.price,
                                      svolume= tcur.dvolume - self._last_dvolume,
                                      samount = tcur.damount - self._last_damount,
                                      sholding=tcur.holding,
                                )

                if self._next_is_new_day: #因为有日结TICK的存在, 故须滤掉. 这个是连续日结或当前第一秒的情况
                    self._next_is_new_day = False
                    cur_minute.svolume = tcur.dvolume
                    cur_minute.samount = tcur.damount
                    #cur_minute.sdate = tcur.date    #日期从日结日期改回实际日期
                    self._modified = False
                else:   #正常分钟结束或日结
                    self.append(pre_minute)
                    self._modified = True
                if tcur.date == FINALIZE_DAY:  #日结束TICK,可以豁免连续的日结(进入else分支,但 next_is_new_day仍然为True
                    #这里利用了DAY_FINALIZE_TICK.min1 == 0, 下一循环直接进入分钟切换分支
                    self._next_is_new_day = True
                self._cur = cur_minute
            else:   #未切换
                cur_minute.sclose = tcur.price
                cur_minute.sholding = tcur.holding
                cur_minute.svolume += tcur.dvolume - self._last_dvolume
                cur_minute.samount += tcur.damount - self._last_damount
                #print(cur_minute.stime,'close:',cur_minute.sclose)
                if tcur.price > cur_minute.shigh:
                    cur_minute.shigh = tcur.price
                elif tcur.price < cur_minute.slow:
                    cur_minute.slow = tcur.price
                self._modified = False
            self._last_dvolume = tcur.dvolume
            self._last_damount = tcur.damount

        self._ilast = len(ticks)
        return self

SDATE = fcustom(UNIT_ATTR,afunc=lambda unit:unit.sdate)
STIME = fcustom(UNIT_ATTR,afunc=lambda unit:unit.stime)
SOPEN = fcustom(UNIT_ATTR,afunc=lambda unit:unit.sopen)
SCLOSE = fcustom(UNIT_ATTR,afunc=lambda unit:unit.sclose)
SHIGH = fcustom(UNIT_ATTR,afunc=lambda unit:unit.shigh)
SLOW = fcustom(UNIT_ATTR,afunc=lambda unit:unit.slow)
SVOLUME = fcustom(UNIT_ATTR,afunc=lambda unit:unit.svolume)
SHOLDING = fcustom(UNIT_ATTR,afunc=lambda unit:unit.sholding)
SAMOUNT = fcustom(UNIT_ATTR,afunc=lambda unit:unit.samount)

##以下为确认周期结束的函数
XS3 = lambda x:x%100%3== 0
XS5 = lambda x: x%100%5== 0
XS10 = lambda x: x%100%10== 0
XS15 = lambda x:x%100%15 == 0
XS30 = lambda x:x%100%30 == 0
XS60 = lambda x:x%100 == 0
XSDAY = lambda x:False      #只有换日才能触发

class XMINUTE(Indicator):
    """
        将分钟数据切成N分钟数据
        如果分钟数据不连续,这个切分存在错误
    """
    def __init__(self,m1,sfunc):
        self._cur = None
        self._num = 0    #当周期的归入数. 小于1的不切换
        self._ilast = 0


    def calc(self,m1,sfunc):
        self.modified = False    #上周期完成标志
        m1len = len(m1)
        for i in range(self._ilast,m1len):
            cminute = m1[i]
            #print(cminute.stime,sfunc(cminute.stime),self.num)
            if self._cur == None:    #这样判断最安心
                self._cur = self._create_new_record(cminute)
                self._num = 1
            elif (sfunc(cminute.stime) and self._num > 1) or cminute.stdate > self._cur.stdate or (m1.next_is_new_day and i == m1len-1):
                #完成当前周期且包含分钟数>1, 或者日期切换, 或者最后一个分钟是日结分钟
                self.append(self._cur)
                self._cur = self._create_new_record(cminute)
                self._num = 1
                self.modified = True
            else:
                self._cur.stime = cminute.stime
                self._cur.sclose = cminute.sclose
                self._cur.svolume += cminute.svolume
                self._cur.samount += cminute.samount
                self._cur.sholding = cminute.sholding
                if cminute.shigh > self._cur.shigh:
                    self._cur.shigh = cminute.shigh
                if cminute.slow < self._cur.slow:
                    self._cur.slow = cminute.slow
                self._num += 1
                self.modified = False

        self._ilast = len(m1)
        return self

    def _create_new_record(self,cminute):
        return BaseObject(sopen = cminute.sopen,
                     sclose = cminute.sclose,
                     shigh = cminute.shigh,
                     slow = cminute.slow,
                     svolume = cminute.svolume,
                     samount = cminute.samount,
                     sholding = cminute.sholding,
                     stime = cminute.stime,
                     sdate = cminute.sdate,
                     stdate = cminute.stdate,
            )


MINUTE3 = fcustom(XMINUTE,sfunc=XS3)
MINUTE5 = fcustom(XMINUTE,sfunc=XS5)
MINUTE10 = fcustom(XMINUTE,sfunc=XS10)
MINUTE15 = fcustom(XMINUTE,sfunc=XS15)
MINUTE30 = fcustom(XMINUTE,sfunc=XS30)
MINUTE60 = fcustom(XMINUTE,sfunc=XS60)
MINUTED = fcustom(XMINUTE,sfunc=XSDAY)      #不能延续之前的日数剧

NullXMinute = XMINUTE([],XSDAY)

class MINUTE2D(Indicator):
    """
        将分钟数据切成日数据
        为了处理MINUTED不能解决的两个问题:
        1. 延续已有的日数据
        2. 添加日数据时,做比较
    """
    def __init__(self,m1,spre_days=None):
        self._cur = None
        self._ilast = 0
        if spre_days:
            self.extend(spre_days)
            self._last_day = spre_days[-1].sdate
        else:
            self._last_day = 0


    def calc(self,m1,spre_days=None):
        self.modified = False    #上周期完成标志
        m1len = len(m1)
        for i in range(self._ilast,m1len):
            cminute = m1[i]
            #print(cminute.stime,sfunc(cminute.stime),self.num)
            #print(i,len(m1),cminute,self._cur)
            if self._cur == None:    #这样判断最安心
                self._cur = self._create_new_record(cminute)
            elif cminute.stdate > self._cur.stdate or (m1.next_is_new_day and i == m1len-1):
                #完成当前周期且包含分钟数>1, 或者日期切换, 或者最后一个分钟是日结分钟
                if self._cur.stdate > self._last_day:
                    #print(self._cur.stdate,self._last_day)
                    self.append(self._cur)
                elif self._cur.stdate == self._last_day:    #同一天,则用新数据替换
                    self[-1] = self._cur
                self._cur = self._create_new_record(cminute)
                self.modified = True
            else:
                self._cur.stime = cminute.stime
                self._cur.sclose = cminute.sclose
                self._cur.svolume += cminute.svolume
                self._cur.samount += cminute.samount
                self._cur.sholding = cminute.sholding
                if cminute.shigh > self._cur.shigh:
                    self._cur.shigh = cminute.shigh
                if cminute.slow < self._cur.slow:
                    self._cur.slow = cminute.slow
                self.modified = False

        self._ilast = len(m1)
        return self

    def _create_new_record(self,cminute):
        return BaseObject(sopen = cminute.sopen,
                     sclose = cminute.sclose,
                     shigh = cminute.shigh,
                     slow = cminute.slow,
                     svolume = cminute.svolume,
                     samount = cminute.samount,
                     sholding = cminute.sholding,
                     stime = cminute.stime,
                     sdate = cminute.sdate,
                     stdate = cminute.stdate,
            )



class CUR_DAY(Indicator):
    """
        当前日的相关信息
    """
    def __init__(self,ticks):
        """
            假设ticks是连续的
        """
        assert len(ticks) > 0
        self._cur = BaseObject(sopen = ticks[0].price,
                               stdate = ticks[0].tdate
                        )

        self._modified = True    #只要有ticks到来,就是True
        self._ilast = 0
        self._last_tick = ticks[0]

    @property
    def modified(self):     #没有实际意义
        return self._modified

    @property
    def sopen(self):
        return self._cur.sopen

    @property
    def shigh(self):
        return self._last_tick.high

    @property
    def slow(self):
        return self._last_tick.low

    @property
    def sclose(self):
        return self._last_tick.price

    @property
    def svolume(self):
        return self._last_tick.dvolume

    @property
    def samount(self):
        return self._last_tick.damount

    @property
    def sholding(self):
        return self._last_tick.holding

    @property
    def date(self):
        return self._last_tick.date

    @property
    def tdate(self):
        return self._last_tick.tdate

    def calc(self,ticks):
        for i in range(self._ilast,len(ticks)):
            tcur = ticks[i]
            if tcur.tdate > self._cur.stdate:
                self._cur.sopen = tcur.price
                self._cur.stdate = tcur.tdate
            self._last_tick = tcur

        self._ilast = len(ticks)
        return self
