#-*- coding:utf-8 -*-

from ..base import (
        BaseObject,
        fcustom,
        indicator,
        icache,
    )

import operator

################
# 量能曲线
################
@indicator
def VENERGY(prices,dvols,vunit=500,_ts=None):
    '''
        vunit为量的切分单位
    '''
    if len(prices) == 0:
        return []

    if not _ts.initialized:
        _ts.initialized = True
        _ts.sopen = []  #目前当周期open==上周期close
        _ts.sclose = []
        _ts.shigh = []
        _ts.slow = []
        _ts.siorder = [] #open的ticks时点
        _ts.cur = BaseObject(vopen = prices[0],
                             vhigh = prices[0],
                             vlow = prices[0],
                             dhigh = prices[0],
                             dlow = prices[0],
                             iopen = 0, #当前周期open位置
                             idhigh = 0,    #最高点位置
                             idlow = 0,     #最低点位置
                             pre_v=0,   #前已耗用累计成交
                             ilast=0,   #最后用到的tick的序号
                    )
        _ts.modified = False    #是否切换新单元, 便于外部判断避免每个ticks都计算某些只需要在新单元才用得到的数据(实际上里面也只有判断,但内务处理显然多很多)

    cur = _ts.cur
    _ts.modified = False
    cur.vopen = _ts.sclose[-1] if _ts.sclose else prices[0]
    for i in range(_ts.cur.ilast,len(prices)):
        cp = prices[i]
        cdv = dvols[i]
        if cp > cur.vhigh:
            cur.vhigh = cp
        if cp < cur.vlow:
            cur.vlow = cp
        if cdv - cur.pre_v > vunit:
            _ts.modified = True
            nv = (cdv - cur.pre_v) / vunit
            if nv > 0:
                _ts.sopen.append(cur.vopen)
                _ts.sclose.append(cp)
                _ts.shigh.append(cur.vhigh)
                _ts.slow.append(cur.vlow)
                _ts.siorder.append(cur.iopen)
            cur.iopen = i
            cur.vopen = cp
            for iv in range(1,nv):  #一次tick穿越多个量单位,后面几个量都是同一个价位
                _ts.sopen.append(cur.vopen)
                _ts.sclose.append(cur.vopen)
                _ts.shigh.append(cur.vopen)
                _ts.slow.append(cur.vopen)
                _ts.siorder.append(cur.iopen)
            vremained = (cdv - cur.pre_v) % vunit
            cur.pre_v = cdv - vremained
            cur.vhigh = cur.vlow = cp
        if cp > cur.dhigh:
            cur.dhigh = cp
            cur.idhigh = len(_ts.sclose)
        if cp < cur.dlow:
            cur.dlow = cp
            cur.idlow = len(_ts.sclose)
    _ts.cur.ilast = len(prices)
    return _ts


@indicator
def AVENERGY(prices,dvols,vtimes=30,_ts=None):
    '''
        自适应量能曲线
        默认根据平均量的30倍来动态调整, 以便将根数控制在1080左右
    '''
    if len(prices) == 0:
        return []

    if not _ts.initialized:
        _ts.initialized = True
        _ts.sopen = []  #目前当周期open==上周期close
        _ts.sclose = []
        _ts.shigh = []
        _ts.slow = []
        _ts.siorder = [] #open的ticks时点
        _ts.cur = BaseObject(vopen = prices[0],
                             vhigh = prices[0],
                             vlow = prices[0],
                             dhigh = prices[0],
                             dlow = prices[0],
                             iopen = 0, #当前周期open位置
                             idhigh = 0,    #最高点位置
                             idlow = 0,     #最低点位置
                             pre_v=0,   #前已耗用累计成交
                             ilast=0,   #最后用到的tick的序号+1
                    )
        _ts.modified = False    #是否切换新单元, 便于外部判断避免每个ticks都计算某些只需要在新单元才用得到的数据(实际上里面也只有判断,但内务处理显然多很多)

    cur = _ts.cur
    _ts.modified = False
    cur.vopen = _ts.sclose[-1] if _ts.sclose else prices[0]
    for i in range(_ts.cur.ilast,len(prices)):
        vunit = dvols[i] * vtimes / (i + 1)
        cp = prices[i]
        cdv = dvols[i]
        if cp > cur.vhigh:
            cur.vhigh = cp
        if cp < cur.vlow:
            cur.vlow = cp
        if cdv - cur.pre_v > vunit:
            _ts.modified = True
            nv = (cdv - cur.pre_v) / vunit
            if nv > 0:
                _ts.sopen.append(cur.vopen)
                _ts.sclose.append(cp)
                _ts.shigh.append(cur.vhigh)
                _ts.slow.append(cur.vlow)
                _ts.siorder.append(cur.iopen)
            cur.iopen = i
            cur.vopen = cp
            for iv in range(1,nv):  #一次tick穿越多个量单位,后面几个量都是同一个价位
                _ts.sopen.append(cur.vopen)
                _ts.sclose.append(cur.vopen)
                _ts.shigh.append(cur.vopen)
                _ts.slow.append(cur.vopen)
                _ts.siorder.append(cur.iopen)
            vremained = (cdv - cur.pre_v) % vunit
            cur.pre_v = cdv - vremained
            cur.vhigh = cur.vlow = cp
        if cp > cur.dhigh:
            cur.dhigh = cp
            cur.idhigh = len(_ts.sclose)
        if cp < cur.dlow:
            cur.dlow = cp
            cur.idlow = len(_ts.sclose)
    _ts.cur.ilast = len(prices)
    return _ts

@indicator
def VSAMPLING(prices,dvols,vtimes=6,_ts=None):
    '''
        自适应量能采样
        与量能曲线相比,只采集量能单位的当前价,不保留其它价格
    '''
    if len(prices) == 0:
        return []

    if not _ts.initialized:
        _ts.initialized = True
        _ts.sclose = []
        _ts.siorder = [] #open的ticks时点
        _ts.cur = BaseObject(dhigh = prices[0],
                             dlow = prices[0],
                             iopen = 0, #当前周期open位置
                             idhigh = 0,    #最高点位置
                             idlow = 0,     #最低点位置
                             pre_v=0,   #前已耗用累计成交
                             ilast=0,   #最后用到的tick的序号+1
                    )
        _ts.modified = False    #是否切换新单元, 便于外部判断避免每个ticks都计算某些只需要在新单元才用得到的数据(实际上里面也只有判断,但内务处理显然多很多)

    cur = _ts.cur
    _ts.modified = False
    for i in range(_ts.cur.ilast,len(prices)):
        vunit = dvols[i] * vtimes / (i + 1)
        cp = prices[i]
        cdv = dvols[i]
        if cdv - cur.pre_v > vunit:
            _ts.modified = True
            nv = (cdv - cur.pre_v) / vunit
            if nv > 0:
                _ts.sclose.append(cp)
                _ts.siorder.append(cur.iopen)
            cur.iopen = i
            for iv in range(1,nv):  #一次tick穿越多个量单位,后面几个量都是同一个价位
                _ts.sclose.append(cp)
                _ts.siorder.append(cur.iopen)
            vremained = (cdv - cur.pre_v) % vunit
            cur.pre_v = cdv - vremained
        if cp > cur.dhigh:
            cur.dhigh = cp
            cur.idhigh = len(_ts.sclose)
        if cp < cur.dlow:
            cur.dlow = cp
            cur.idlow = len(_ts.sclose)
    _ts.cur.ilast = len(prices)
    return _ts

NullSampling = BaseObject(sclose=[],svol=[],sholding=[],siorder=[])

@indicator
def TSAMPLING(prices,dvols,holdings,times,fsection,_ts=None):
    '''
        时间采样
        只采集当前价和成交量,不保留其它价格
        fsection为采样点确认函数
    '''

    if len(prices) == 0:
        return NullSampling

    if not _ts.initialized:
        _ts.initialized = True
        _ts.sclose = []
        _ts.svol = []
        _ts.sholding=[]
        _ts.siorder = [] #open的ticks时点
        _ts.cur = BaseObject(dhigh = prices[0],
                             dlow = prices[0],
                             iopen = 0, #当前周期open位置
                             idhigh = 0,    #最高点位置
                             idlow = 0,     #最低点位置
                             pre_v= dvols[0],   #前已耗用累计成交
                             holding=holdings[0],
                             ilast=0,   #最后用到的tick的序号+1
                             tid = fsection(times[0]/1000),    #第一个会不准,不会引起切分. /1000去掉毫秒
                             iorder=0,
                    )
        _ts.modified = False    #是否切换新单元, 便于外部判断避免每个ticks都计算某些只需要在新单元才用得到的数据(实际上里面也只有判断,但内务处理显然多很多)

    cur = _ts.cur
    _ts.modified = False
    for i in range(_ts.cur.ilast,len(prices)):
        cp = prices[i]
        tid = fsection(times[i]/1000)
        #print tid,times[i]
        if tid > cur.tid:
            cur.tid = tid
            _ts.modified = True
            cv = (dvols[i] - cur.pre_v)
            _ts.siorder.append(cur.iorder)
            _ts.sclose.append(cp)
            _ts.svol.append(cv)
            _ts.sholding.append(cur.holding)
            cur.iopen = i
            cur.iorder += 1
            cur.pre_v = dvols[i]
        if cp > cur.dhigh:
            cur.dhigh = cp
            cur.idhigh = len(_ts.sclose)
        if cp < cur.dlow:
            cur.dlow = cp
            cur.idlow = len(_ts.sclose)
        cur.holding = holdings[i]
    _ts.cur.ilast = len(prices)
    return _ts

ST3 = lambda x:x/100*100+x%100/3    #小时*100+分钟*100+3秒序列
ST5 = lambda x:x/100*100+x%100/5
ST6 = lambda x:x/100*100+x%100/6
ST10 = lambda x:x/100*100+x%100/10
ST15 = lambda x:x/100*100+x%100/15
ST20 = lambda x:x/100*100+x%100/20
ST30 = lambda x:x/100*100+x%100/30
##还可以设定45等分钟以上的秒切分函数, 感觉殊无必要

TSAMPLING3 = fcustom(TSAMPLING,fsection=ST3)
TSAMPLING5 = fcustom(TSAMPLING,fsection=ST5)
TSAMPLING6 = fcustom(TSAMPLING,fsection=ST6)
TSAMPLING10 = fcustom(TSAMPLING,fsection=ST10)
TSAMPLING15 = fcustom(TSAMPLING,fsection=ST15)
TSAMPLING20 = fcustom(TSAMPLING,fsection=ST20)
TSAMPLING30 = fcustom(TSAMPLING,fsection=ST30)


@indicator
def XCROSS(source1,source2,rcmp,lcmp,ctimes=1,_ts=None):
    ''' 
        source2去交叉source1
        rcmp为判断已交叉状态的函数
        lcmp为判断反向状态的函数
        ctimes为确认交叉所需的rcmp状态为正次数
        返回值中,0为未×,1为×
        ###仅用于正常序列,通常没用
    '''
    if len(source1) == 0:
        return []

    if not _ts.initialized:
        _ts.initialized = True
        _ts.state = [1 if rcmp(source2[0],source1[0]) else -1 if lcmp(source2[0],source1[0]) else 0]
        _ts.crs = [1 if _ts.state[0]==ctimes else 0]

    ps = _ts.state[-1]
    for i in range(len(_ts.crs),len(source1)):
        if rcmp(source2[i],source1[i]):
            if ps > 0:
                ps += 1
            else:
                ps = 1
        elif lcmp(source2[i],source1[i]):
            if ps < 0:
                ps -= 1
            else:
                ps = -1
        _ts.crs.append(1 if ps==ctimes else 0)
        _ts.state.append(ps)
    return _ts.crs

XUPCROSS = fcustom(XCROSS,rcmp = operator.gt,lcmp = operator.lt) #
XDOWNCROSS = fcustom(XCROSS,rcmp = operator.lt,lcmp = operator.gt) #


@indicator
def NXCROSS(source,target,rcmp,lcmp,ctimes=1,_ts=None):
    ''' 
        source去交叉target,target为数字
        rcmp为判断已交叉状态的函数
        lcmp为判断反向状态的函数
        ctimes为确认交叉所需的rcmp状态为正次数
        返回值中,0为未×,1为×
        ###仅用于正常序列,通常没用
    '''
    if len(source) == 0:
        return []

    if not _ts.initialized:
        _ts.initialized = True
        _ts.state = [1 if rcmp(source[0],target) else -1 if lcmp(source[0],target) else 0]
        _ts.crs = [1 if _ts.state[0]==ctimes else 0]

    ps = _ts.state[-1]
    for i in range(len(_ts.crs),len(source)):
        if rcmp(source[i],target):
            if ps > 0:
                ps += 1
            else:
                ps = 1
        elif lcmp(source[i],target):
            if ps < 0:
                ps -= 1
            else:
                ps = -1
        _ts.crs.append(1 if ps==ctimes else 0)
        _ts.state.append(ps)
    return _ts.crs

NXUPCROSS = fcustom(NXCROSS,rcmp = operator.gt,lcmp = operator.lt) #
NXDOWNCROSS = fcustom(NXCROSS,rcmp = operator.lt,lcmp = operator.gt) #


##使用于ticks序列
def check_cross(price,bline,pre_count,rcmp,lcmp):
    cur_count = pre_count
    if rcmp(price,bline):
        if pre_count <= 0:
            cur_count = 1
        else:
            cur_count += 1
    elif lcmp(price,bline):
        if pre_count <= 0:
            cur_count -= 1
        else:
            cur_count = -1
    return cur_count

check_up_cross = fcustom(check_cross,rcmp = operator.gt,lcmp = operator.lt)
check_down_cross = fcustom(check_cross,rcmp = operator.lt,lcmp = operator.gt)

##计算高\低点
import dac2
@indicator
def XPEAK(source,mlen=5,fmm=dac2.TMAX,_ts=None):
    ''' 
        source为价格序列
        fmm为求极值函数
        mlen为高/低点的左右距离
        返回值中,peaks为高/低点, orders为source中的序号(0基)
    '''
    if not _ts.initialized:
        _ts.initialized = True
        _ts.cur = BaseObject(
                    peaks = [],
                    siorder = [],
                )
        _ts.cpos = mlen*2   #为第mlen*2+1位

    if len(source) < mlen*2+1:
        return _ts.cur

    mm = fmm(source,mlen*2+1)
    for i in range(_ts.cpos,len(source)):
        if source[i-mlen] == mm[i]:
            _ts.cur.peaks.append(mm[i])
            _ts.cur.siorder.append(i-mlen)
    _ts.cpos = len(source)
    return _ts.cur

UPEAK = fcustom(XPEAK,fmm=dac2.TMAX)
DPEAK = fcustom(XPEAK,fmm=dac2.TMIN)


@indicator
def XPEAK2(source,mlen=5,fmm=max,_ts=None):
    ''' 
        同XPEAK,采用max/min来计算. 效率上可能有差别
        source为价格序列
        fmm为求极值函数
        mlen为高/低点的左右距离
        返回值中,peaks为高/低点, orders为source中的序号
    '''
    if not _ts.initialized:
        _ts.initialized = True
        _ts.cur = BaseObject(
                    peaks = [],
                    siorder = [],
                )
        _ts.cpos = mlen*2   #为第mlen*2+1位
    
    if len(source) < mlen*2+1:
        return _ts.cur
    
    for i in range(_ts.cpos,len(source)):
        mm = fmm(source[i-(mlen*2):i+1]) if mlen>0 else source[i]
        if source[i-mlen] == mm:
            _ts.cur.peaks.append(mm)
            _ts.cur.siorder.append(i-mlen)
    _ts.cpos = len(source)
    return _ts.cur

UPEAK2 = fcustom(XPEAK2,fmm=max)
DPEAK2 = fcustom(XPEAK2,fmm=min)

NullSection = BaseObject(sopen=[],sclose=[],shigh=[],slow=[],svol=[],sholding=[],siorder=[])

@indicator
def TSECTION(prices,dvols,holdings,times,fsection,_ts=None):
    '''
        秒级别切分
        fsectionr为id函数
    '''

    if len(prices) == 0:
        return NullSection

    if not _ts.initialized:
        _ts.initialized = True
        _ts.sopen = []
        _ts.sclose = []
        _ts.shigh = []
        _ts.slow = []
        _ts.svol = []
        _ts.sholding=[]
        _ts.siorder = []
        _ts.cur = BaseObject(vopen = prices[0],    
                             vclose = prices[0],    
                             vhigh=prices[0],    
                             vlow=prices[0],    
                             open_dvol=dvols[0],    #存在初始误差
                             close_dvol=dvols[0],
                             holding = holdings[0],
                             tid = fsection(times[0]/1000),#/1000去掉毫秒
                             iorder=0,
                        )  #这里对dvol的处理,使得中断恢复也必须从当日最开始开始,否则所有前述成交量被归结到第一tick
        _ts.ilast = 0
        _ts.modified = False    #上周期完成标志

    scur = _ts.cur
    for i in range(_ts.ilast,len(prices)):
        tid = fsection(times[i]/1000)
        #print tid,times[i],fsection(916091309)
        if tid > scur.tid:  #切换, 避免ticks数据错误引发分钟序列紊乱,如20120905:958:59:500插入在20120905:959:00:00之后,虽然非常罕见,但会导致分钟序列出现958->959->958->959...这个情况
            ##这样,年切换时必须重新启动程序
            #print 'vclose:',scur.vclose,times[i],prices[i]
            _ts.sopen.append(scur.vopen)
            _ts.sclose.append(scur.vclose)
            _ts.shigh.append(scur.vhigh)
            _ts.slow.append(scur.vlow)
            _ts.svol.append(scur.close_dvol - scur.open_dvol)
            _ts.sholding.append(scur.holding)
            _ts.siorder.append(scur.iorder)
            scur.vopen = scur.vclose = scur.vhigh = scur.vlow = prices[i]
            scur.open_dvol = scur.close_dvol
            scur.close_dvol = dvols[i]
            scur.dvol = dvols[i]
            scur.holding = holdings[i]
            scur.iorder += 1
            scur.tid = tid
            _ts.modified = True
        else:   #未切换
            scur.vclose = prices[i]
            #print 'vclose:',scur.vclose
            scur.close_dvol = dvols[i]
            #print scur.tid,'close:',scur.vclose
            if prices[i] > scur.vhigh:
                scur.vhigh = prices[i]
            elif prices[i] < scur.vlow:
                scur.vlow = prices[i]
            _ts.modified = False
            scur.holding = holdings[i]

    _ts.ilast = len(prices)
    return _ts

TSECTION3 = fcustom(TSECTION,fsection=ST3)
TSECTION5 = fcustom(TSECTION,fsection=ST5)
TSECTION6 = fcustom(TSECTION,fsection=ST6)
TSECTION10 = fcustom(TSECTION,fsection=ST10)
TSECTION15 = fcustom(TSECTION,fsection=ST15)
TSECTION20 = fcustom(TSECTION,fsection=ST20)
TSECTION30 = fcustom(TSECTION,fsection=ST30)
