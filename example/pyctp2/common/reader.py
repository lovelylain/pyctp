#-*- coding: utf-8 -*-

import os.path as path
import logging

from .base import (BaseObject,
                   DATA_PATH,
                   EPSL,
                   CN_TRADE_SECTION,
                   TICK,
                )
from ..common import base
from .utils import fcustom,next_trading_day

def check_valid_minute(record):
    if (record.stime > CN_TRADE_SECTION.DAY.begin and record.stime < CN_TRADE_SECTION.DAY.end) or record.stime >= CN_TRADE_SECTION.NIGHT.begin or record.stime <=CN_TRADE_SECTION.NIGHT.end:
        return True
    return False

def check_valid_tick(tick):
    '''
        确认tick是否合法
        目前使用的ctp接口在7:00-7:10,以及15:20-16:00之间有非法数据出现
    '''
    if (tick.min1 > CN_TRADE_SECTION.DAY.begin and tick.min1 < CN_TRADE_SECTION.DAY.end) or tick.min1 >= CN_TRADE_SECTION.NIGHT.begin or tick.min1 <= CN_TRADE_SECTION.NIGHT.end:
        return True
    return False

def read_record(contract_name,fname,extractor,up2day=99999999):
    '''
        用于读取minute和日数据
        不抛出异常.如果文件不存在,则返回[]
    '''
    fpath = '%s/%s/%s.csv' % (base.DATA_PATH,contract_name,fname)
    #print(base.DATA_PATH,contract_name,fname)
    if not path.exists(fpath):
        logging.info("文件 %s 不存在" % (fpath,))
        return []
    records = []
    with open(fpath,'rt') as mf:
        for line in mf:
            record = extractor(line)
            if record:
                if record.sdate <= up2day:
                    records.append(record)
                else:
                    break
    return records

def readn_record(contract_name,fname,extractor,size=99999999):
    '''
        用于读取minute和日数据
        不抛出异常.如果文件不存在,则返回[]
    '''
    if size == 0:
        size = 9999999
    fpath = '%s/%s/%s.csv' % (base.DATA_PATH,contract_name,fname)
    #print(base.DATA_PATH,contract_name,fname,size)
    if not path.exists(fpath):
        logging.info("文件 %s 不存在" % (fpath,))
        return []
    records = []
    with open(fpath,'rt') as mf:
        for line in mf.readlines()[-size:]:
            record = extractor(line)
            if record:
                records.append(record)
    return records

def readn_record0(contract_name,fname,extractor,up2day=99999999,size=99999999):
    '''
        用于读取minute和日数据
        不抛出异常.如果文件不存在,则返回[]
    '''
    if size == 0:
        size = 9999999
    fpath = '%s/%s/%s.csv' % (base.DATA_PATH,contract_name,fname)
    #print(base.DATA_PATH,contract_name,fname,size)
    if not path.exists(fpath):
        logging.info("文件 %s 不存在" % (fpath,))
        return []
    records = []
    with open(fpath,'rt') as mf:
        for line in mf.readlines()[-size:]:
            record = extractor(line)
            if record:
                if record.sdate <= up2day:
                    records.append(record)
                else:
                    break
    return records

def read_tick(contract_name,sdate):
    '''
        用于读取ticks数据
        不抛出异常.如果文件不存在,则返回[]
    '''
    fpath = '%s/%s/%d.csv' % (base.DATA_PATH,contract_name,sdate)
    if not path.exists(fpath):
        logging.info("文件 %s 不存在" % (fpath,))
        return []
    records = []
    with open(fpath,'rt') as mf:
        for line in mf:
            record = _extract_tick(line,sdate)
            if record:
                record.instrument = contract_name   #需要么
                record.sdate = sdate
                records.append(record)
    return records

def _extract_minute(line):
    sline = line.strip()
    if len(sline) == 0:
        return None
    try:
        items = sline.split(',')
        record = BaseObject()
        record.sdate = int(items[0])
        record.stime = int(items[1])
        record.sopen = float(items[2]) + EPSL
        record.shigh = float(items[3]) + EPSL
        record.slow = float(items[4]) + EPSL
        record.sclose = float(items[5]) + EPSL
        record.svolume = float(items[6]) + EPSL
        record.samount = float(items[7]) + EPSL
        record.sholding = float(items[8])  + EPSL
        #TODO. 这里的stdate需要数据读取后再调整
        record.stdate = record.sdate if record.stime < 1600 else next_trading_day(record.sdate)     #可能会有问题,需要后面调整 #TODO
    except Exception as einst:
        print(sline,str(einst))
        return None
    if check_valid_minute(record):
        return record
    return None

def _extract_day(line):
    sline = line.strip()
    if len(sline) == 0:
        return None
    try:
        items = sline.split(',')
        record = BaseObject()
        record.sdate = int(items[0])
        record.sopen = float(items[1]) + EPSL
        record.shigh = float(items[2]) + EPSL
        record.slow = float(items[3]) + EPSL
        record.sclose = float(items[4]) + EPSL
        record.svolume = float(items[5]) + EPSL
        record.samount = float(items[6]) + EPSL
        record.sholding = float(items[7])  + EPSL
    except Exception as einst:
        print(sline,str(einst))
        return None
    return record

def _extract_tick(line,sdate):
    sline = line.strip()
    if len(sline) == 0:
        return None
    try:
        items = line.split(',')
        #print(items[0],items[6])
        record = TICK('',sdate)
        record.time = int(items[0])
        record.min1 = record.time // 100 % 10000
        record.sec = record.time % 100
        record.msec = int(items[1])
        record.price = float(items[2]) + EPSL
        record.high = float(items[3]) + EPSL
        record.low = float(items[4]) + EPSL
        record.dvolume = int(items[5])
        record.damount = int(float(items[6]))
        record.holding = int(items[7])
        record.bid_price = float(items[8]) + EPSL
        record.bid_volume = int(items[9])
        record.ask_price = float(items[10]) + EPSL
        record.ask_volume = int(items[11])
    except Exception as einst:
        print(sline,str(einst))
        return None
    if check_valid_tick(record):   
        return record
    return None


read_m1 = fcustom(read_record,fname='minutes',extractor=_extract_minute)
read_day = fcustom(read_record,fname='days',extractor=_extract_day)
#readn_m1 = fcustom(readn_record,fname='minutes',extractor=_extract_minute)
readn_m1 = fcustom(readn_record0,fname='minutes',extractor=_extract_minute)
