# -*- coding: utf-8 -*-

import zipfile
import time
import logging


from base import *
from dac import date2week

#logger = logging.getLogger('ctp.hreader')    

DATA_PATH = 'data/'


#################################################################
## 历史数据读取
#################################################################
def extract_std(line):
    items = line.split(',')
    record = BaseObject()
    record.date = int(items[0].replace('/',''))
    record.time = int(items[1].replace(':',''))
    record.open = int(float(items[2])*10 + 0.1)
    record.high = int(float(items[3])*10 + 0.1)
    record.low = int(float(items[4])*10 + 0.1)
    record.close = int(float(items[5])*10 + 0.1)
    record.vol = int(float(items[6]) + 0.1)
    record.holding = int(float(items[7]) + 0.1)
    return record

def read_data(filename,extractor=extract_std):
    file = open(filename,'r')
    data = file.read()
    file.close()
    return read_records(data,extractor)



def read_data_zip(filename,extractor=extract_std):
    df = zipfile.ZipFile(filename,'r')
    data = df.read(df.namelist()[0])    #只包含一个文件
    data = data.replace('\r','')  #去掉zip文件读出的\r，因为直接读文本没有\r这个符号
    df.close()
    return read_records(data,extractor)

def read_records(data,extractor):    
    '''
        根据传入的文本数据切割成record数组
    '''
    data = data.split('\n')
    records = []
    for line in data:
        if len(line.strip()) > 0:
            record = extractor(line)
            #if record.time < 1516 and record.time > 850 or ('min1' in record.__dict__ and record.min1 < 1516 and record.min1 > 850):  #排除错误数据
            if record.time < 1516 and record.time > 850 or (record.min1 < 1516 and record.min1 > 850):  #排除错误数据 #20120723
                records.append(record)
    return records


def read_min_as_list(filename,length,extractor=extract_std,readfunc = read_data,t2order=t2order_if):
    try:
        records = readfunc(filename,extractor)
    except Exception,inst:#读不到数据,默认都为1(避免出现被0除)
        logging.error(u'文件打开错误，文件名=%s,错误信息=%s' % (filename,str(inst)))
        n = 0
        return [[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n]
    else:   #正常读取到数据
        n = min(len(records),length)
        tran_data = [[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n]
        i = 0
        for record in records[-length:]:
            tran_data[IDATE][i] = record.date
            tran_data[ITIME][i] = record.time
            tran_data[IOPEN][i] = record.open        
            tran_data[ICLOSE][i] = record.close
            tran_data[IHIGH][i] = record.high
            tran_data[ILOW][i] = record.low       
            tran_data[IVOL][i] = record.vol
            tran_data[IHOLDING][i] = record.holding
            tran_data[IORDER][i] = t2order[record.time]
            i += 1
    return tran_data


NULL_RECORD = BaseObject(date=0,time=0,open=0,close=0,high=0,low=0,vol=0,holding=0)
def read_last_record(filename,extractor=extract_std,readfunc = read_data):
    try:
        records = readfunc(filename,extractor)
    except Exception,inst:#读不到数据,默认都为1(避免出现被0除)
        logging.error(u'文件打开错误，文件名=%s,错误信息=%s' % (filename,str(inst)))
        record = NULL_RECORD
    else:   #正常读取到数据
        #print len(records)
        #print records[-1].date,records[-2].date,filename
        if len(records)>0:
            record = records[-1]
        else:
            record = NULL_RECORD
    return record


def concatenate(*args):
    result =  [[],[],[],[],[],[],[],[],[]]
    for arg in args:
        for i in range(9):
            result[i] += arg[i]
    return result

import os
def prepare_directory(instruments):#确认若不存在子目录，则创建之
    for instrument in instruments:
        directory = '%s%s' % (DATA_PATH,instrument)
        if not os.path.exists(directory):
            os.mkdir(directory)
    


prefix = ''
SUFFIX = '.txt'
SUFFIX_ZIP = '.zip'
HISTORY_TXT = 'history.txt'

def make_tick_filename(instrument,tday=0,suffix='txt'):
    if tday == 0:
        tday = time.strftime('%Y%m%d')
    return '%s%s/%s_tick.%s' % (DATA_PATH,instrument,tday,suffix)

def make_min_filename(instrument,path=DATA_PATH,suffix='txt'):
    return '%s%s/%s_min.%s' % (path,instrument,time.strftime('%Y%m%d'),suffix)

def make_min_filename_c(instrument,tday,path=DATA_PATH,suffix='txt'):   #根据指定的日期加载
    return '%s%s/%s_min.%s' % (path,instrument,tday,suffix)

make_his_filename = lambda name,path=DATA_PATH:'%s%s/%s' % (path,name,HISTORY_TXT)

def read1(instrument,length=18000,path=DATA_PATH,extractor=extract_std,readfunc=read_data):
    '''
        历史数据和当日数据的合并，按日处理。即如果历史数据中有当日的，则忽略单文件中的当日数据
    '''
    #6000是22天，足够应付日ATR计算
    t2order = t2order_if if is_if(instrument) else t2order_com
    dhistory = read_min_as_list(make_his_filename(instrument,path),length=length,extractor=extractor,readfunc=readfunc,t2order=t2order)
    dtoday = read_min_as_list(make_min_filename(instrument,path),length=length,extractor=extractor,readfunc=readfunc,t2order=t2order)
    #hdata = BaseObject(name=instrument,instrument=instrument,transaction=concatenate(dhistory,dtoday))
    if (len(dhistory[IDATE]) > 0 and len(dtoday[IDATE])>0 and dhistory[IDATE][-1] >= dtoday[IDATE][-1]) or len(dtoday[0])==0:
        hdata = BaseObject(name=instrument,instrument=instrument,transaction=dhistory)
    else:
        hdata = BaseObject(name=instrument,instrument=instrument,transaction=concatenate(dhistory,dtoday))
    return hdata

def read1_c(instrument,tday,length=18000,path=DATA_PATH,extractor=extract_std,readfunc=read_data):
    '''
        历史数据和当日数据的合并，按日处理。即如果历史数据中有当日的，则忽略单文件中的当日数据
    '''
    #用于mock
    #6000是22天，足够应付日ATR计算,不够，计算日ATR时误差很大
    t2order = t2order_if if is_if(instrument) else t2order_com
    dhistory = read_min_as_list(make_his_filename(instrument,path),length=length,extractor=extractor,readfunc=readfunc,t2order=t2order)
    if tday == -1: #不需要当日数据,用于测试时的初始化
        return BaseObject(name=instrument,instrument=instrument,transaction=dhistory)
    dtoday = read_min_as_list(make_min_filename_c(instrument,tday,path),length=length,extractor=extractor,readfunc=readfunc,t2order=t2order)
    if (len(dhistory[IDATE]) > 0 and len(dtoday[IDATE])>0 and dhistory[IDATE][-1] >= dtoday[IDATE][-1]) or len(dtoday[0])==0:
        hdata = BaseObject(name=instrument,instrument=instrument,transaction=dhistory)
    else:
        hdata = BaseObject(name=instrument,instrument=instrument,transaction=concatenate(dhistory,dtoday))
    return hdata#,dhistory,dtoday


#不从zip读数据
#read1_zip = fcustom(read1,readfunc=read_data_zip)


def read_history(instrument_id,path):
    return read1(instrument_id,path=path)

def read_history_c(instrument_id,tday,path):#指定当前日，用于测试
    print 'instrument=%s,tday=%s' %(instrument_id,tday)
    return read1_c(instrument_id,tday=tday,path=path)

def read_history_last(instrument_id,path=DATA_PATH):
    return read_last_record(make_his_filename(instrument_id,path))

def read_current_last(instrument_id,path=DATA_PATH):
    return read_last_record(make_min_filename(instrument_id,path))

def read_current_last_c(instrument_id,tday,path=DATA_PATH):
    return read_last_record(make_min_filename_c(instrument_id,tday,path))


##检查是否需要合并历史数据和当日数据，如果需要则合并
def check_merge(instrument_id,tday,path=DATA_PATH):
    ##todo:这里应该加个锁
    last_history_date = read_history_last(instrument_id).date
    last_current_date = read_current_last_c(instrument_id,tday).date
    #cur_date = int(time.strftime('%Y%m%d'))
    #print 'in check_merge',cur_date,last_history_date
    print 'in check_merge',last_current_date,last_history_date
    #if cur_date > last_history_date:    #只有当日大于最后历史日时，才需要合并
    if last_current_date > last_history_date:    #只有当日大于最后历史日时，才需要合并
        cur_file = make_min_filename_c(instrument_id,tday,path)
        his_file = make_his_filename(instrument_id,path)
        try:
            hf = open(his_file,'a+')
            cf = open(cur_file,'r')
            hf.write(cf.read())
        finally:
            hf.close()
            cf.close()
        return True
    else:
        #print u'不需要合并,instrument_id=%s 最后日=%s,当前日=%s' % (instrument_id,last_history_date,cur_date)
        #logging.debug(u'不需要合并, instrument=%s,最后日=%s,当前日=%s' % (instrument_id,last_history_date,cur_date))
        print u'不需要合并,instrument_id=%s 最后日=%s,当前日=%s' % (instrument_id,last_history_date,last_current_date)
        logging.debug(u'不需要合并, instrument=%s,最后日=%s,当前日=%s' % (instrument_id,last_history_date,last_current_date))
        return False

#####################################################
#分钟数据写入, 暂时写入到当日的分钟文件，而不是写到历史分钟文件中
#####################################################
def i2s(iv):    #将.1转化为正常点. 以与从文化财经保存的一致
    return '%s.%s' % (iv/10,iv%10)

def save1(instrument,min_data,tday,path=DATA_PATH):
    filename = make_min_filename_c(instrument,tday,path)
    ff = open(filename,'a+')
    sdate = '%s/%02d/%02d' % (min_data.vdate/10000,min_data.vdate/100%100,min_data.vdate%100)
    stime = '%02d:%02d' % (min_data.vtime/100,min_data.vtime%100)
    ff.write('%s,%s,%s,%s,%s,%s,%s,%s\n' % (sdate,stime,i2s(min_data.vopen),i2s(min_data.vhigh),i2s(min_data.vlow),i2s(min_data.vclose),min_data.vvolume,min_data.vholding))
    ff.close()

##############################################################################
##基本数据准备
##############################################################################
def prepare_data(instruments,tday,path=DATA_PATH):
    data = {}
    for inst in instruments:
        PREPARER = PREPARER_INST
        tdata = read_history_c(inst,tday,path)
        tdata.m1 = tdata.transaction
        ###基本序列按1分钟设定,方便快捷查找
        tdata.sdate = tdata.m1[IDATE]
        tdata.stime = tdata.m1[ITIME]
        tdata.sopen = tdata.m1[IOPEN]
        tdata.sclose = tdata.m1[ICLOSE]
        tdata.shigh = tdata.m1[IHIGH]
        tdata.slow = tdata.m1[ILOW]
        tdata.svolume = tdata.m1[IVOL]
        tdata.sholding = tdata.m1[IHOLDING]
        tdata.siorder = tdata.m1[IORDER]
        ###其它周期
        oc_index_3 = PREPARER.p3(tdata.transaction[IORDER])
        tdata.m3 = compress(tdata.transaction,oc_index_3)
        oc_index_5 = PREPARER.p5(tdata.transaction[IORDER])
        tdata.m5 = compress(tdata.transaction,oc_index_5)
        oc_index_10 = PREPARER.p10(tdata.transaction[IORDER])
        tdata.m10 = compress(tdata.transaction,oc_index_10)
        oc_index_15 = PREPARER.p15(tdata.transaction[IORDER])
        tdata.m15 = compress(tdata.transaction,oc_index_15)
        oc_index_30 = PREPARER.p30(tdata.transaction[IORDER])
        tdata.m30 = compress(tdata.transaction,oc_index_30)
        data[inst] = tdata
        oc_index_d = PREPARER.pd(tdata.transaction[IORDER])
        tdata.d1 = compress(tdata.transaction,oc_index_d)
        if len(tdata.d1[IDATE])>0 and tdata.transaction[IORDER][-1]==270:
            tdata.cur_day = BaseObject(
                        vdate= tdata.d1[IDATE][-1],
                        vtime = tdata.stime[-1],    #最后的交易分钟
                        vopen = tdata.d1[IOPEN][-1],
                        vclose = tdata.d1[ICLOSE][-1],
                        vhigh = tdata.d1[IHIGH][-1],    #根据tick中出现价格的最大/最小比较而来
                        vlow = tdata.d1[ILOW][-1],
                        vhighd = tdata.d1[IHIGH][-1],   #根据tick中的当日最大/最小, 是服务器计算的
                        vlowd = tdata.d1[ILOW][-1],
                        vholding = tdata.d1[IHOLDING][-1],
                        vvolume = tdata.d1[IVOL][-1],
                        iihigh = 270,   #与行情无关
                        iilow = 270,
                        weekday = date2week(tdata.d1[IDATE][-1]),
                        ibegin = len(tdata.sdate)-271,    #这个其实不一定对，未必每天有271个数据，可能914会没有,那就是上一天的最后一个。但下一个数据来时会处理掉
                    )
        elif len(tdata.d1[IDATE])>0:
            xtimes = tdata.transaction[IORDER]
            poss = filter(lambda x:SPREPARER.ISEND_DAY(x[0]),zip(xtimes,range(len(xtimes))))
            idlast = poss[-1][1] + 1
            #print tdata.transaction[IORDER][idlast],tdata.transaction[IDATE][idlast],tdata.transaction[ITIME][idlast]
            tdata.cur_day = BaseObject(
                        vdate= tdata.sdate[idlast],
                        vtime = tdata.stime[-1],    #最后的交易分钟
                        vopen = tdata.sopen[idlast],
                        vclose = tdata.sclose[-1],
                        vhigh = max(tdata.shigh[idlast:]),
                        vlow = min(tdata.slow[idlast:]),
                        vhighd = max(tdata.shigh[idlast:]),
                        vlowd = min(tdata.slow[idlast:]),
                        vholding = tdata.sholding[-1],
                        vvolume = tdata.svolume[-1],
                        weekday = date2week(tdata.sdate[idlast]),
                        ibegin = idlast,    #第一分钟的坐标
                    )
            for i in range(len(tdata.stime)-1,idlast-1,-1):
                if tdata.shigh[i] == tdata.cur_day.vhigh:
                    break
            tdata.cur_day.iihigh = tdata.siorder[i]
            for i in range(len(tdata.stime)-1,idlast-1,-1):
                if tdata.slow[i] == tdata.cur_day.vlow:
                    break
            tdata.cur_day.iilow = tdata.siorder[i]
        else:
            tdata.cur_day = BaseObject(
                        vdate= 0,
                        vtime = 0,
                        vopen = 0,
                        vclose = 0,
                        vhigh = 0,
                        vlow = 0,
                        vhighd = 0,
                        vlowd = 0,
                        vholding = 0,
                        vvolume = 0,
                        iihigh = 0,
                        iilow = 0,
                        ibegin = 0,
                        weekday = 0,
                    )
        if len(tdata.sdate)>0:
            tdata.cur_min = BaseObject(
                        vdate = tdata.sdate[-1],
                        vtime = tdata.stime[-1],
                        vopen = tdata.sopen[-1],
                        vclose = tdata.sclose[-1],
                        vhigh = tdata.shigh[-1],
                        vlow = tdata.slow[-1],
                        vholding = tdata.sholding[-1],
                        vvolume = tdata.svolume[-1],
                        viorder = tdata.siorder[-1],
                    )
        else:
            tdata.cur_min = BaseObject(
                        vdate = 0,
                        vtime = 0,
                        vopen = 0,
                        vclose = 0,
                        vhigh = 0,
                        vlow = 0,
                        vholding = 0,
                        vvolume = 0,
                        viorder=0,
                    )
        data[inst] = tdata
    return data

def compress(trans_data,oc_index):
    '''
        将trans_data的各数据根据oc_index压缩成相应的X分钟数据
    '''
    n = len(oc_index)
    xdata = [[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n,[0]*n]
    xdata[IDATE] = [trans_data[IDATE][c] for o,c in oc_index]
    xdata[ITIME] = [trans_data[ITIME][c] for o,c in oc_index]   #收盘时间点
    xdata[IOPEN] = [trans_data[IOPEN][o] for o,c in oc_index]        
    xdata[ICLOSE] = [trans_data[ICLOSE][c] for o,c in oc_index]
    xdata[IHIGH] = [max(trans_data[IHIGH][o:c+1]) for o,c in oc_index]
    xdata[ILOW] = [min(trans_data[ILOW][o:c+1]) for o,c in oc_index]
    xdata[IVOL] = [sum(trans_data[IVOL][o:c+1]) for o,c in oc_index]
    xdata[IHOLDING] = [trans_data[IHOLDING][c] for o,c in oc_index]
    xdata[IORDER] = [trans_data[IORDER][c] for o,c in oc_index]
    return xdata


'''
##是否是IF的X分钟收盘分钟
IF_XPREPARER = BaseObject()
IF_XPREPARER.ISEND_3 = lambda x:(x%100%3==2 or x%10000==1514) and x%1000!=914
IF_XPREPARER.ISEND_5 = lambda x: x%5==4 and x%1000!=914
IF_XPREPARER.ISEND_15 = lambda x:x%100%15 == 14 and x%1000!=914
IF_XPREPARER.ISEND_30 = lambda x:x%100%30 == 14 and x%1000!=914
IF_XPREPARER.ISEND_DAY = lambda x:x%10000 == 1514

##是否是CM的X分钟收盘分钟
CM_XPREPARER = BaseObject()
CM_XPREPARER.ISEND_3 = lambda x:(x%100%3==2 or x%10000==1459) and x%1000!=859
CM_XPREPARER.ISEND_5 = lambda x: x%5==4 and x%1000!=859
CM_XPREPARER.ISEND_15 = lambda x:x%100%15 == 14 and x%1000!=859
CM_XPREPARER.ISEND_30 = lambda x:(x%100%30 == 29 or x%10000 == 1014) and x%1000!=859
CM_XPREPARER.ISEND_DAY = lambda x:x%10000 == 1459
'''

#通用的Preparer
SPREPARER = BaseObject()
SPREPARER.ISEND_3 = lambda x:x%3==2 and x>0
SPREPARER.ISEND_5 = lambda x: x%5==4 and x>0
SPREPARER.ISEND_10 = lambda x: x%10==0 and x>0
SPREPARER.ISEND_15 = lambda x:x%15 == 14 and x>0
SPREPARER.ISEND_30 = lambda x:x%30 == 29 and x>0
SPREPARER.ISEND_DAY = lambda x:x == 270


def is_if(instrument):#判断是否是IF
    return instrument[:2].upper() == 'IF'

class XPREPARER(object):
    def __init__(self,fpreparer):
        self.fpreparer = fpreparer

    def pd(self,xtimes):#切日
        #poss = filter(lambda x:x[0]>x[1],zip(xtimes,xtimes[1:]+[0],range(len(xtimes))))
        #cposs = [z for (x,y,z) in poss]   #close
        poss = filter(lambda x:self.fpreparer.ISEND_DAY(x[0]),zip(xtimes,range(len(xtimes))))
        cposs = [y for (x,y) in poss]   #close
        oposs = [0] + [c+1 if c-1>0 else 0 for c in cposs] #close,第一个算日的开始
        return zip(oposs,cposs)
    
    def p3(self,xtimes):#切3分钟,返回3分钟(3分开盘index,3分收盘index)
        poss = filter(lambda x:self.fpreparer.ISEND_3(x[0]),zip(xtimes,range(len(xtimes))))
        cposs = [y for (x,y) in poss]   #close
        oposs = [c+1 if c-1>0 else 0 for c in cposs] #close
        return zip(oposs,cposs[1:])

    def p5(self,xtimes):#切5分钟,返回5分钟(5分开盘index,5分收盘index)
        poss = filter(lambda x:self.fpreparer.ISEND_5(x[0]),zip(xtimes,range(len(xtimes))))
        cposs = [y for (x,y) in poss]   #close
        oposs = [c+1 if c-1>0 else 0 for c in cposs] #close
        return zip(oposs,cposs[1:])

    def p10(self,xtimes):#切10分钟,返回10分钟(10分开盘index,10分收盘index)
        poss = filter(lambda x:self.fpreparer.ISEND_10(x[0]),zip(xtimes,range(len(xtimes))))
        cposs = [y for (x,y) in poss]   #close
        oposs = [c+1 if c-1>0 else 0 for c in cposs] #close
        return zip(oposs,cposs[1:])

    def p15(self,xtimes):#切15分钟,返回15分钟(15分开盘index,15分收盘index)
        poss = filter(lambda x:self.fpreparer.ISEND_15(x[0]),zip(xtimes,range(len(xtimes))))
        cposs = [y for (x,y) in poss]   #close
        oposs = [c+1 if c-1>0 else 0 for c in cposs] #close
        return zip(oposs,cposs[1:])

    def p30(self,xtimes):#切30分钟,返回30分钟(30分开盘index,30分收盘index)
        poss = filter(lambda x:self.fpreparer.ISEND_30(x[0]),zip(xtimes,range(len(xtimes))))
        cposs = [y for (x,y) in poss]   #close
        oposs = [c+1 if c-1>0 else 0 for c in cposs] #close
        return zip(oposs,cposs[1:])

'''
IF_PREPARER = XPREPARER(IF_XPREPARER)
CM_PREPARER = XPREPARER(CM_XPREPARER)
'''
PREPARER_INST= XPREPARER(SPREPARER)

##############################################
##ticks数据读取
##############################################
def extract_tick(line):
    items = line.split(',')
    #rev = BaseObject()
    rev = TICK()
    rev.sname = items[0]
    rev.date = int(items[1])
    rev.min1 = int(items[2])
    rev.sec = int(items[3])
    rev.msec = int(items[4])
    rev.holding = int(items[5])
    rev.dvolume = int(items[6])
    rev.price = int(items[7])
    rev.high = int(items[8])
    rev.low = int(items[9])
    rev.bid_price = int(items[10])
    rev.bid_volume = int(items[11])
    rev.ask_price = int(items[12])
    rev.ask_volume = int(items[13])
    #rev.time = rev.min1
    rev.time = rev.date%10000 * 1000000+ rev.min1*100 + rev.sec #与market_data2tick一致
    rev.switch_min = False  #分钟切换
    return rev

def read_ticks(instrument,tday=0,length = 36000,extractor=extract_tick,readfunc = read_data):
    #读取指定日数据
    records = readfunc(make_tick_filename(instrument,tday),extractor)
    for record in records:
        record.instrument = instrument
    return records[-length:]


class TICK(object):
    __slots__ = ['sname','instrument','date','min1','sec','msec','time','holding','dvolume','price','high','low','bid_price','bid_volume','ask_price','ask_volume','switch_min','iorder','dorder']



##############################################
##时间轮转
##############################################
def time_period_switch(data):
    '''
        判断分钟数据是否是3/5/15/30的卡点, 并计算相关数据
    '''
    #print 'in time_period_switch'
    #if(len(data.sdate) == 0):   #该合约史上第一分钟,不引起切换. 这个在外部保障
    #    return
    #logging.info('TPS1:len(m1)=%s' % len(data.m1[0]))
    #data.m1就是data.transaction
    assert len(data.sdate)>0
    #fpreparer = IF_XPREPARER if is_if(data.instrument) else CM_XPREPARER
    fpreparer = SPREPARER
    if fpreparer.ISEND_3(data.siorder[-1]) and (len(data.m3[IDATE])==0 
                                        or data.sdate[-1] > data.m3[IDATE][-1] 
                                        or data.stime[-1] > data.m3[ITIME][-1]
                                    ):#添加新的3分钟
        append1(data.m3,data,3)
    if fpreparer.ISEND_5(data.siorder[-1]) and (len(data.m5[IDATE])==0 
                                        or data.sdate[-1] > data.m5[IDATE][-1] 
                                        or data.stime[-1] > data.m5[ITIME][-1]
                                    ):#添加新的5分钟
        append1(data.m5,data,5)
    if fpreparer.ISEND_10(data.siorder[-1]) and (len(data.m10[IDATE])==0 
                                        or data.sdate[-1] > data.m10[IDATE][-1] 
                                        or data.stime[-1] > data.m10[ITIME][-1]
                                    ):#添加新的5分钟
        append1(data.m10,data,10)
    if fpreparer.ISEND_15(data.siorder[-1]) and (len(data.m15[IDATE])==0 
                                        or data.sdate[-1] > data.m15[IDATE][-1] 
                                        or data.stime[-1] > data.m15[ITIME][-1]
                                    ):#添加新的15分钟
        append1(data.m15,data,15)
    if fpreparer.ISEND_30(data.siorder[-1]) and (len(data.m30[IDATE])==0 
                                        or data.sdate[-1] > data.m30[IDATE][-1] 
                                        or data.stime[-1] > data.m30[ITIME][-1]
                                    ):#添加新的30分钟
        append1(data.m30,data,30)
    if fpreparer.ISEND_DAY(data.siorder[-1]) and (len(data.d1[IDATE])==0 
                                        or data.sdate[-1] > data.d1[IDATE][-1] 
                                    ):#添加新的日数据
        append1(data.d1,data,270)
    #logging.info('TPS1:len(m1)=%s' % len(data.m1[0]))
 

def append1(xdata,data1,length):
    '''
        将data1中最后length的数据组合以后放入xdata
    '''
    mlen = min(len(data1.sdate),length)
    xdata[IDATE].append(data1.sdate[-1])
    xdata[ITIME].append(data1.stime[-1])
    xdata[IOPEN].append(data1.sopen[-mlen])
    xdata[ICLOSE].append(data1.sclose[-1])
    xdata[IHIGH].append(max(data1.shigh[-mlen:]))
    xdata[ILOW].append(min(data1.slow[-mlen:]))
    xdata[IVOL].append(sum(data1.svolume[-mlen:]))
    xdata[IHOLDING].append(data1.sholding[-1])
    xdata[IORDER].append(data1.siorder[-1])
