# -*-coding:utf-8 -*-
'''
用到的指标/计算的集合
来自core/d1,d1ex,d1indiactor, 是np版本的list化版

其中 XXX为序列运算版本(list). XXX的参照对象是numpy的运算版本(用于回测)
     XXX1为即时运算版本(计算最后一个值)
        XXX1的函数的最后一个顺序参数都是target, 即要计算的值的已有序列. 其最后一个值会在函数中被设置
    序列函数/动态函数中必须妥善处理输入序列比较短或为空的情况
'''

from collections import deque

XBASE = 100  #整数运算的放大倍数
CBASE = XBASE * XBASE #XATR倍数
FBASE = 10 #整数运算的放大倍数2

def date2week(iday):
    #http://blog.csdn.net/hawkfeifei/article/details/4337181
    year = iday/10000
    month = iday/100%100
    day = iday%100
    if month <= 2:
        month += 12
        year -= 1
    return (day+2*month+3*(month+1)/5+year+year/4-year/100+year/400)%7 + 1  #转化为1-7

def xdiff(source):
    '''
        消除连续的同向信号
        如 0,0,1,0,0,1,0,0,-1,0,1 --> 0,0,1,0,0,0,0,0,-1,0,1
    '''
    if len(source)==0:
        return []
    rev = [0]*len(source)
    dcur = 1 if source[0]>0 else -1 if source[0]<0 else 0
    rev[0] = dcur
    for i in range(len(source)):
        if dcur >= 0 and source[i] < 0:
            dcur = -1
            rev[i] = dcur
        elif dcur <=0 and source[i] > 0:
            dcur = 1
            rev[i] = dcur
        else:#0或同向信号
            pass
    return rev


def cexpma(source,n): 
    ''' 计算cexpma序列
        国内使用的expma,直接用n作为参数
        内部用整数计算
        用于整数的source,有四舍五入因子(n+1)/2. 因此不能传入浮点数，会因为该因子而导致数据变化
    '''
    #rev = np.zeros_like(source)
    rev = [0] * len(source)
    if len(source) == 0:
        return rev
    
    cur = source[0]
    for i in xrange(0,len(source)):
        cur = (source[i]*2 + cur*(n-1) + (n+1)/2)/(n+1) 
        rev[i] = cur
    return rev


def cexpma1_old(source,n,target): 
    ''' 计算最新值
        其中target[:-2]是已经计算的结果
        用于整数的source,有四舍五入因子(n+1)/2. 因此不能传入浮点数，会因为该因子而导致数据变化
    '''
    assert len(source) == len(target),u'源序列与目标序列长度不相等,%s:%s' % (len(source),len(target))
    if(len(source) < 2):
        return 0  
    target[-1] = (source[-1]*2 + target[-2] *(n-1) + (n+1)/2)/(n+1) 
    return target[-1]

def cexpma1(slast,n,target2): 
    ''' 计算最新值
        slast是source最新值
        其中target[:-2]是已经计算的结果
        用于整数的source,有四舍五入因子(n+1)/2. 因此不能传入浮点数，会因为该因子而导致数据变化
    '''
    return (slast*2 + target2 *(n-1) + (n+1)/2)/(n+1) 


def tr(sclose,shigh,slow):
    ''' 真实波幅. 结果被放大XBASE倍
        sclose = rollx(sclose)
        shl = np.abs(shigh - slow)
        shc = np.abs(shigh - sclose)
        slc = np.abs(slow - sclose)
        return gmax(shl,shc,slc)
    '''
    if(len(sclose) < 1):
        return []
    sclose = [sclose[0]] + sclose[:-1]
    shl = [abs(sh-sl) * XBASE for sh,sl in zip(shigh,slow)]
    shc = [abs(sh-sc) * XBASE for sh,sc in zip(shigh,sclose)]
    slc = [abs(sl-sc) * XBASE for sl,sc in zip(slow,sclose)]
    return [max(hl,hc,lc) for hl,hc,lc in zip(shl,shc,slc)]

def tr1(sclose,shigh,slow,target):
    assert len(sclose) == len(target),u'源序列与目标序列长度不相等,%s:%s' % (len(sclose),len(target))
    if(len(sclose) < 2):
        return 0
    hl = abs(shigh[-1] - slow[-1]) * XBASE
    hc = abs(shigh[-1] - sclose[-2]) * XBASE
    lc = abs(slow[-1] - sclose[-2]) * XBASE
    target[-1] = max(hl,hc,lc)
    return target[-1]

def atr(ltr,length=20):
    return cexpma(ltr,length)

def atr1(ltr,target,length=20):
    if len(ltr)<2:
        return 0
    assert len(ltr) == len(target),u'源序列与目标序列长度不相等,%s:%s' % (len(ltr),len(target))
    target[-1] = cexpma1(ltr[-1],length,target[-2])
    return target[-1]
 
def cmacd(source,ifast=12,islow=26,idiff=9):
    source = [s* FBASE for s in source]
    sfast = cexpma(source,ifast)
    sslow = cexpma(source,islow)
    sdiff = [sf - ss for sf,ss in zip(sfast,sslow)]
    sdea = cexpma(sdiff,idiff)
    return sfast,sslow,sdiff,sdea

def cmacd1(source,target_fast,target_slow,target_dea,ifast=12,islow=26,idiff=9):
    if len(source)<2:
        return 0
    assert len(source) == len(target_fast),u'源序列与fast目标序列长度不相等,%s:%s' % (len(source),len(target_fast))
    assert len(source) == len(target_slow),u'源序列与slow目标序列长度不相等,%s:%s' % (len(source),len(target_slow))
    assert len(source) == len(target_dea),u'源序列与dea目标序列长度不相等,%s:%s' % (len(source),len(target_dea))
    
    target_fast[-1] = cexpma1(source[-1]*FBASE,ifast,target_fast[-2])
    target_slow[-1] = cexpma1(source[-1]*FBASE,islow,target_slow[-2])
    target_dea[-1] = cexpma1(target_fast[-1]-target_slow[-1],idiff,target_dea[-2])
    return target_fast[-1],target_slow[-1],target_dea[-1]

def xatr(latr,sclose):
    return [ia * CBASE / ic for ia,ic in zip(latr,sclose)]

def xatr1(latr,sclose,lxatr):
    if len(latr)<1:
        return 0
    assert len(latr) == len(sclose) == len(lxatr),u'源序列与目标序列长度不相等,%s:%s' % (len(latr),len(target))
    lxatr[-1] = latr[-1] * CBASE / sclose[-1]
    return lxatr[-1]

def sdiff(source1,source2):
    return [sf - ss for sf,ss in zip(source1,source2)]

def rsdiff(source1,source2,offset):
    if len(source2) == 0:
        return []
    if len(source2) >= offset:
        return sdiff(source1,[source2[0]]*offset + source2[:len(source2)-offset])
    else:
        return sdiff(source1,[source2[0]]*len(source2))


def accumulate(source):
    if(len(source) < 1):
        return []
    rev = [0] * len(source)
    rev[0] = source[0]
    for i in range(len(source)):
        rev[i] = rev[i-1] + source[i]
    return rev

def accumulate1(source,target):
    assert len(source) == len(target),u'源序列与目标序列长度不相等,%s:%s' % (len(source),len(target))
    if(len(source) < 1):
        return 0
    if(len(source) == 1):
        target[-1] = source[-1]
    else:
        target[-1] = target[-2] + source[-1]
    return target[-1]

def ma(source,length):
    """ 计算移动平均线
        @param source 源数组
        @param length 均线跨度
        @return 移动平均序列
    """
    slen = len(source)
    rev = [0] * slen
    if slen < length:
        return rev
    
    pps = length/2 #用于整数四舍五入尾数

    acc = [0] + accumulate(source)
    rev = [0]*(length-1) + [((sl-sf)+pps)/length for sl,sf in zip(acc[length:],acc[:slen-length+1])]

    return rev

def msum(source,length):
    """ 计算移动累加
        @param source 源数组
        @param length 累加跨度
        @return 移动累加序列
    """
    slen = len(source)
    rev = [0] * slen
    if slen < length:
        return rev
    
    acc = [0] + accumulate(source)
    rev = [0]*(length-1) + [sl-sf for sl,sf in zip(acc[length:],acc[:slen-length+1])]

    return rev


def ma1(source,length,target):
    if len(source)<1:
        return 0
    assert len(source) == len(target),u'源序列与目标序列长度不相等,%s:%s' % (len(source),len(target))
    target[-1] = (sum(source[-length:]) + length/2) / length
    return target[-1]

def strend2(source):
    ''' 简单累积趋势2
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
    '''
    rev = [0] * len(source)
    if len(source) == 0:
        return rev
    pre_v = source[0]
    cur = 0
    for i in range(1,len(source)):
        cur_v = source[i]
        if cur_v > pre_v:
            cur = cur + 1 if cur > 0 else 1
        elif cur_v < pre_v:
            cur = cur - 1 if cur < 0 else -1
        else: #curv == pre_v
            cur = cur + 1 if cur >= 0 else cur-1 #最初为0时，也算上升
        rev[i] = cur
        pre_v = cur_v
    return rev    

def strend2_1(source,target):
    assert len(source) == len(target),u'源序列与目标序列长度不相等,%s:%s' % (len(source),len(target))
    if len(source) < 1:
        return 0
    elif len(source) == 1:
        target[0] = 0
        return 0
    cur_v,pre_v = source[-1],source[-2]
    cur = target[-2]
    if cur_v > pre_v:
        target[-1] = cur + 1 if cur > 0 else 1
    elif cur_v < pre_v:
        target[-1] = cur - 1 if cur < 0 else -1
    else: #curv == pre_v
        target[-1] = cur + 1 if cur >= 0 else cur-1 #最初为0时，也算上升
    return target[-1]



############
# 从d1ex.py复制
#
############
def tmax(source,covered): #最近len个数据的max值
    ''' 等同于
        tmaxmin(source,covered,max,np.max,-99999999)
        是其展开版本
    '''
    tm = -99999999
    length = len(source)
    rev = [0]*length
    prelen = length > covered and covered or length
    for i in range(prelen):
        v = source[i]
        if tm < v:
            tm = v
        rev[i] = tm
    buffer = deque([v for v in source[:prelen]])   #优化方法，避免vquit=source[i-covered]的方式，对nbarray的直接索引有严重的性能问题
    for i in range(prelen,length):
        v = source[i]
        buffer.append(v)
        vquit=buffer.popleft()
        if tm < v:
            tm = v
        if tm == vquit and v != tm: #退出的正好是最大值,计算前covered-1个元素的最大值, pre=source[i-1]
            tm = max(source[i-covered+1:i+1])
        rev[i] = tm
    return rev

def tmin(source,covered): #最近len个数据的max值
    ''' 等同于
        tmaxmin(source,covered,min,np.min,99999999)
        是其展开版本
    '''
    tm = 99999999
    length = len(source)
    rev = [0]*length
    prelen = length > covered and covered or length
    for i in range(prelen):
        v = source[i]
        if tm > v:
            tm = v
        rev[i] = tm
    buffer = deque([v for v in source[:prelen]])   #优化方法，避免vquit=source[i-covered]的方式，对nbarray的直接索引有严重的性能问题
    for i in range(prelen,length):
        v = source[i]
        buffer.append(v)
        vquit=buffer.popleft()
        if tm > v:
            tm = v
        if tm == vquit and v != tm: #退出的正好是最大值,计算前covered-1个元素的最大值, pre=source[i-1]
            tm = min(source[i-covered+1:i+1])
        rev[i] = tm
    return rev


###包装类
from base import *
def ATR(data):
    '''
        计算ATR序列
    '''
    data.tr1 = tr(data.m1[ICLOSE],data.m1[IHIGH],data.m1[ILOW])
    data.atr1 = atr(data.tr1,20)
    data.xatr1 = xatr(data.atr1,data.m1[ICLOSE])
    data.mxatr1 = ma(data.xatr1,13)
    #data.tr3 = tr(data.m3[ICLOSE],data.m3[IHIGH],data.m3[ILOW])
    #data.atr3 = atr(data.tr3,20)
    #data.xatr3 = xatr(data.atr3,data.m3[ICLOSE])
    #data.tr5 = tr(data.m5[ICLOSE],data.m5[IHIGH],data.m5[ILOW])
    #data.atr5 = atr(data.tr5,20)
    #data.xatr5 = xatr(data.atr5,data.m5[ICLOSE])
    #data.tr15 = tr(data.m15[ICLOSE],data.m15[IHIGH],data.m15[ILOW])
    #data.atr15 = atr(data.tr15,20)
    #data.xatr15 = xatr(data.atr15,data.m15[ICLOSE])
    data.tr30 = tr(data.m30[ICLOSE],data.m30[IHIGH],data.m30[ILOW])
    data.atr30 = atr(data.tr30,20)
    data.xatr30 = xatr(data.atr30,data.m30[ICLOSE])
    data.trd1 = tr(data.d1[ICLOSE],data.d1[IHIGH],data.d1[ILOW])
    data.atrd1 = atr(data.trd1,20)
    data.xatrd1 = xatr(data.atrd1,data.d1[ICLOSE])
    
def ATR1(data):
    '''
        动态计算最新ATR
    '''
    if len(data.m1[ICLOSE]) > len(data.tr1):    #1分钟数据
        #print len(data.m1[ICLOSE]),len(data.tr1)
        data.tr1.append(0)
        tr1(data.m1[ICLOSE],data.m1[IHIGH],data.m1[ILOW],data.tr1)
        data.atr1.append(0)
        atr1(data.tr1,data.atr1,20)
        data.xatr1.append(0)
        xatr1(data.atr1,data.m1[ICLOSE],data.xatr1)
        data.mxatr1.append(0)
        ma1(data.xatr1,13,data.mxatr1)
        
    #if len(data.m5[ICLOSE]) > len(data.tr5):    #5分钟数据
    #    data.tr5.append(0)
    #    tr1(data.m5[ICLOSE],data.m5[IHIGH],data.m5[ILOW],data.tr5)
    #    data.atr5.append(0)
    #    atr1(data.tr5,data.atr5,20)
    #    data.xatr5.append(0)
    #    xatr1(data.atr5,data.m5[ICLOSE],data.xatr5)
    if len(data.m30[ICLOSE]) > len(data.tr30):    #30分钟数据
        data.tr30.append(0)
        tr1(data.m30[ICLOSE],data.m30[IHIGH],data.m30[ILOW],data.tr30)
        data.atr30.append(0)
        atr1(data.tr30,data.atr30,20)
        data.xatr30.append(0)
        xatr1(data.atr30,data.m30[ICLOSE],data.xatr30)
    if len(data.d1[ICLOSE]) > len(data.trd1):    #d1分钟数据
        data.trd1.append(0)
        tr1(data.d1[ICLOSE],data.d1[IHIGH],data.d1[ILOW],data.trd1)
        data.atrd1.append(0)
        atr1(data.trd1,data.atrd1,20)
        data.xatrd1.append(0)
        xatr1(data.atrd1,data.d1[ICLOSE],data.xatrd1)


def STREND(data):
    '''
        计算趋势
    '''
    data.ma30_120 = ma(data.m30[ICLOSE],120)
    data.t120 = strend2(data.ma30_120)
    data.ma15_20 = ma(data.m15[ICLOSE],20)
    data.r20 = strend2(data.ma15_20)
    data.s_ma20 = strend2(data.ma_20)
    data.sh10 = strend2(data.m10[IHIGH])
    #data.slh_10 = strend2(data.dlh_10)
    #pass

def STREND1(data):
    '''
        动态计算t120的最新值
    '''
    if len(data.m30[ICLOSE]) > len(data.ma30_120):  #需要计算
        data.ma30_120.append(0)
        data.t120.append(0)
        ma1(data.m30[ICLOSE],120,data.ma30_120)
        strend2_1(data.ma30_120,data.t120)
    if len(data.m15[ICLOSE]) > len(data.ma15_20):  #需要计算
        data.ma15_20.append(0)
        data.r20.append(0)
        ma1(data.m15[ICLOSE],20,data.ma15_20)
        strend2_1(data.ma15_20,data.r20)
    if len(data.m10[ICLOSE]) > len(data.sh10):  #需要计算
        data.sh10.append(0)
        strend2_1(data.m10[IHIGH],data.sh10)
    data.s_ma20.append(0)
    strend2_1(data.ma_20,data.s_ma20)
    #data.slh_10.append(0)
    #strend2_1(data.dlh_10,data.slh_10)

    #pass

def MA(data):
    '''
        序列计算基本均线, 1分钟的5/7/10/13/20/30/60/120/135/270均线
    '''
    #data.ma_1 = ma(data.sclose,1)
    
    data.ma_5 = ma(data.sclose,5)
    data.ma_7 = ma(data.sclose,7)
    #data.ma_10 = ma(data.sclose,10)
    data.ma_13 = ma(data.sclose,13)
    data.ma_20 = ma(data.sclose,20)
    data.ma_30 = ma(data.sclose,30)
    #data.ma_60 = ma(data.sclose,60)
    #data.ma_120 = ma(data.sclose,120)
    #data.ma_135 = ma(data.sclose,135)
    #data.ma_270 = ma(data.sclose,270)
    
    #data.hma30 = ma(data.shigh,30)
    #data.lma30 = ma(data.slow,30)
    #data.hma60 = ma(data.shigh,60)
    #data.lma60 = ma(data.slow,60)
    #data.dlh_10 = rsdiff(data.lma60,data.hma60,10) 

def MA1(data):
    '''
        动态计算基本均线, 1分钟的5/7/10/13/20/30/60/120/135/270均线
    '''
    #print u'before:收盘序列长度:%s,ma5序列长度:%s' % (len(data.sclose),len(data.ma_5))
    #data.ma_1.append(0)
    data.ma_5.append(0)
    data.ma_7.append(0)
    #data.ma_10.append(0)
    data.ma_13.append(0)
    data.ma_20.append(0)
    data.ma_30.append(0)
    #data.hma30.append(0)
    #data.lma30.append(0)
    #data.hma60.append(0)
    #data.lma60.append(0)
    
    #data.ma_60.append(0)
    #data.ma_120.append(0)
    #data.ma_135.append(0)    
    #data.ma_270.append(0)    
    #ma1(data.sclose,1,data.ma_1)    
    ma1(data.sclose,5,data.ma_5)
    ma1(data.sclose,7,data.ma_7)
    #ma1(data.sclose,10,data.ma_10)
    ma1(data.sclose,13,data.ma_13)
    ma1(data.sclose,20,data.ma_20)
    ma1(data.sclose,30,data.ma_30)
    
    #ma1(data.shigh,30,data.hma30)
    #ma1(data.slow,30,data.lma30)
    #ma1(data.shigh,60,data.hma60)
    #ma1(data.slow,60,data.lma60)
    
    #ma1(data.sclose,60,data.ma_60)
    #ma1(data.sclose,120,data.ma_120)
    #ma1(data.sclose,135,data.ma_135)
    #ma1(data.sclose,270,data.ma_270)
    #print u'after:收盘序列长度:%s,ma5序列长度:%s' % (len(data.sclose),len(data.ma_5))
    assert len(data.sclose) == len(data.ma_5),u'sclose序列和ma_5序列长度不同 len(data.sclose)=%s,len(data.ma5)=%s' % (len(data.sclose),len(data.ma_5))
    #if len(data.hma60)>11:
    #    data.dlh_10.append(data.lma60[-1] - data.hma60[-11])
    #else:
    #    data.dlh_10.append(data.lma60[-1] - data.hma60[0])

def ADX(data,n=14,m=6):
    '''计算ADX
    '''
    tpdm = [ x1-x2 for x1,x2 in zip(data.high,[0]+data.high[0:1]+data.high[:-1])]
    tndm = [ x2-x1 for x1,x2 in zip(data.low,data.low[0:1]+data.low[:-1])]
    pdm = [ p if p>0 and p>d else 0 for p,d in zip(tpdm,tndm)]
    ndm = [ d if d>0 and d>p else 0 for p,d in zip(tpdm,tndm)]
    xtr = msum(data.tr,n)
    data.pdi = [ ps * 10000 / x for ps,x in zip(msum(pdm,n),xtr)]
    data.ndi = [ ps * 10000 / x for ps,x in zip(msum(ndm,n),xtr)]
    vadx = [ (pi-di)*10000 / (pi+di) for pi,di in zip(data.pdi,data.ndi)]
    vadx = [ v if v>0 else -v for v in vadx]
    data.adx = ma(vadx,m)

def ADX1(data,n=14,m=6):
    pass



def MACD(data):
    '''
        序列计算1分钟MACD
    '''
    data.sfast,data.sslow,data.sdiff,data.sdea = cmacd(data.sclose)
    data.macd = [sdi-sde for sdi,sde in zip(data.sdiff,data.sdea)]
    data.mmacd = ma(data.macd,3)
    data.s1 = strend2(data.mmacd)

def MACD1(data):
    '''
        动态计算1分钟MACD
    '''
    data.sfast.append(0)
    data.sslow.append(0)    
    data.sdea.append(0)
    cmacd1(data.sclose,data.sfast,data.sslow,data.sdea)
    data.sdiff.append(data.sfast[-1] - data.sslow[-1])
    data.macd.append(data.sdiff[-1] - data.sdea[-1])
    data.mmacd.append(0)
    ma1(data.macd,3,data.mmacd)
    data.s1.append(0)
    strend2_1(data.mmacd,data.s1)
