#-*- coding:gbk -*-

'''
    ctp marketdata 监听
    与ctp_api打交道的底层模块
    须保证与ctp_api行情相关部分均封装于本模块

    TODO:
        考虑到特殊情况, 须将每日15:20-17:00作为不可接收时段,以便数据处理. 不过需要慎重考虑是否需要. 
        目前观察
        

'''

import time
import threading
import logging

from ..common import base
from ..common import utils
from ctp.futures import ApiStruct as ustruct
from ctp.futures import ApiStruct as utype
from ctp.futures import MdApi

class MdSpiDelegate(MdApi):
    '''
        将行情信息转发到Controller
        其中需要将行情中的合约名替换为标准名
        目前CTP所提供的即为标准名,故不需要替换
    '''
    logger = logging.getLogger('ctp.MdSpiDelegate')
    
    def __init__(self,
            name,
            broker_id,   #期货公司ID
            investor_id, #投资者ID
            passwd, #口令
            controller,  #实际操作者
        ):       
        self._name = name
        self._instruments = set()
        self._broker_id =broker_id
        self._investor_id = investor_id
        self._passwd = passwd
        self._cur_day = 0    #int(time.strftime('%Y%m%d'))   #尽可能不依赖于当前系统的日期! #当前的实际交易日. 夜盘归入当日,而非次日!!
        self._controller = controller
        self._request_id = 0

    def inc_request_id(self):
        self._request_id += 1
        return self._request_id

    def checkErrorRspInfo(self, info):
        logging.debug(info)
        if info.ErrorID !=0:
            self.logger.error("MD:ErrorID:%s,ErrorMsg:%s" %(info.ErrorID,info.ErrorMsg))
        return info.ErrorID !=0

    def OnRspError(self, info, RequestId, IsLast):
        self.logger.error('MD:requestID:%s,IsLast:%s,info:%s' % (RequestId,IsLast,str(info)))

    def OnFrontDisConnected(self, reason):
        self.logger.info('MD:front disconnected,reason:%s' % (reason,))

    def OnFrontConnected(self):
        self.logger.info('MD:front connected')
        self.user_login(self._broker_id, self._investor_id, self._passwd)

    def user_login(self, broker_id, investor_id, passwd):
        req = ustruct.ReqUserLogin(BrokerID=broker_id, UserID=investor_id, Password=passwd)
        r=self.ReqUserLogin(req,self.inc_request_id())

    def OnRspUserLogin(self, userlogin, info, rid, is_last):
        self.logger.info('MD:user login:%s,info:%s,rid:%s,is_last:%s' % (userlogin,info,rid,is_last))
        logging.info(self._instruments)
        logging.info('is_last=%s,errorCheck:%s' % (is_last,self.checkErrorRspInfo(info)))
        if is_last and not self.checkErrorRspInfo(info):
            self.logger.info("MD:get today's trading day:%s" % repr(self.GetTradingDay()))
            self.subscribe_market_data(self._instruments)

    def subscribe_market_data(self, instruments):
        if instruments:
            self.SubscribeMarketData(list(instruments))

    def unsubscribe_market_data(self, instruments):
        if instruments:
            self.UnSubscribeMarketData(list(instruments))

    def update_instruments(self,cur_instruments):
        '''
            增订新增合约
            退订不再监听的合约
        '''
        instruments_new = [ instrument for instrument in cur_instruments if instrument not in self._instruments]
        instruments_discard = [ instrument for instrument in self._instruments if instrument not in cur_instruments]
        self._instruments.update(instruments_new)    #set 没有 += 的运算符
        self.subscribe_market_data(instruments_new)
        self._instruments -= set(instruments_discard)
        self.unsubscribe_market_data(instruments_discard)
        logging.info('%s:listen to:%s' % (self._name,self._instruments))
        logging.info('%s:discard:%s' % (self._name,instruments_discard))

    def OnRtnDepthMarketData(self, depth_market_data):
        #print(depth_market_data.BidPrice1,depth_market_data.BidVolume1,depth_market_data.AskPrice1,depth_market_data.AskVolume1,depth_market_data.LastPrice,depth_market_data.Volume,depth_market_data.UpdateTime,depth_market_data.UpdateMillisec,depth_market_data.InstrumentID)
        #print('on data......\n')
        try: #须确保这里不会出啥问题
            dp = depth_market_data
            #print('thread id:',threading.current_thread().ident,dp.InstrumentID,dp.UpdateTime,dp.UpdateMillisec,dp.TradingDay) #夜盘的TradeingDay属于次日,但updateTime未变
            #time.sleep(10)
            if depth_market_data.LastPrice > 999999 or depth_market_data.LastPrice < 10:
                self.logger.warning('MD:收到的行情数据有误:%s,LastPrice=:%s' %(depth_market_data.InstrumentID,depth_market_data.LastPrice))
            if depth_market_data.InstrumentID not in self._instruments:
                self.logger.warning('MD:收到未订阅的行情:%s' %(depth_market_data.InstrumentID,))
                return
            #self.logger.debug('收到行情:%s,time=%s:%s' %(depth_market_data.InstrumentID,depth_market_data.UpdateTime,depth_market_data.UpdateMillisec))
            #4print(dp.InstrumentID,dp.UpdateTime,dp.UpdateMillisec)
            is_updated = self._controller.check_last(dp.InstrumentID,dp.UpdateTime,dp.UpdateMillisec,dp.Volume)
            if is_updated:
                ctick = self.market_data2tick(depth_market_data)
                if ctick:
                    if ctick.date > self._cur_day:   #这样,cur_day完全由tick驱动
                        self._cur_day = ctick.date
                    self._controller.new_tick(ctick)
            else:
                pass
        finally:
            pass
        
    def market_data2tick(self,market_data):
        """
            market_data的格式转换和整理, 交易数据都转换为整数
            夜盘在日期记录上的归属:
                1. 0:0之前, 归属于前一交易日
                2. 0:0及之后,归属于下一交易日
                这么做是为了避免 都归于下一交易日时,出现的该交易日 23:59的数据先于 00:01出现的情况
        """
        try:
            state = '开始'
            rev = base.TICK(instrument = market_data.InstrumentID,date=self._cur_day)
            rev.min1 = int(market_data.UpdateTime[:2]+market_data.UpdateTime[3:5])
            if len(market_data.TradingDay.strip()) > 0:
                rev.tdate = int(market_data.TradingDay)
            else:
                raise ValueError("传入的TradingDay错误,TradingDay=%s" % (market_data.TradingDay,))
            if rev.min1 >= base.NIGHT_BEGIN:
                if self._cur_day > 0:
                    rev.date = self._cur_day
                else:
                    rev.date = utils.pre_day(rev.tdate)
            else:
                rev.date = rev.tdate

            rev.sec = int(market_data.UpdateTime[-2:])
            rev.msec = int(market_data.UpdateMillisec)
            rev.holding = int(market_data.OpenInterest+0.1)
            rev.dvolume = market_data.Volume
            rev.damount = market_data.Turnover + base.EPSL
            rev.price = market_data.LastPrice + base.EPSL
            rev.high = market_data.HighestPrice + base.EPSL
            rev.low = market_data.LowestPrice + base.EPSL
            rev.time = rev.date%10000 * 1000000+ rev.min1*100 + rev.sec
            #添加rev.tdate是为了处理夜盘情况
            state = '完成:low, market_data.BidPrice1=%d' % (market_data.BidPrice1,)
            rev.bid_price = market_data.BidPrice1+ base.EPSL
            state = '完成:bid_price'
            rev.bid_volume = market_data.BidVolume1
            state = '完成:bid_volume'
            rev.ask_price = market_data.AskPrice1 + base.EPSL
            rev.ask_volume = market_data.AskVolume1
            #self.logger.warning('MD:行情数据:%s' % market_data)
            if not rev.is_valid():
                raise ValueError("tick not valid")
        except Exception as inst:
            self.logger.warning('MD:行情数据转换错误:%s,赋值进程=%s' % (str(inst),state))
            self.logger.warning('MD:行情数据转换错误,源记录:%s' % market_data)
            self.logger.warning('MD:%s 行情数据转换错误:%s,updateTime="%s",msec="%s",tday="%s"' % (market_data.InstrumentID,str(inst),market_data.UpdateTime,market_data.UpdateMillisec,market_data.TradingDay))
            return None
        return rev

