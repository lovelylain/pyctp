# -*- coding=utf-8 -*-

import logging
import unittest

from ..common.base import BaseObject,LONG,SHORT,TEST_PATH,TICK
from ..common import base
from ..common.contract_type import (ContractInfo,
                                    Base_ContractType,
                                    ZN,TF,CU,
                                    CM_ALL,CM_CU,
                                    calc_delay_map,
                                    calc_next_trade_minute,
                                )
from ..common.cjson import dumps,loads


class ContractInfoTest(unittest.TestCase):
    def test_normal(self):
        bct = Base_ContractType("TT","TEST_EXCHANGE",0,0,0,None)
        c1 = ContractInfo(name="TT9901",ctype=bct, ymonth=9901)
        c2 = ContractInfo(name="TT9901",ctype=bct, ymonth=9901)
        c20 = ContractInfo(name="TT9901",ctype=None, ymonth=9901)
        self.assertEqual(id(c1),id(c2))
        self.assertEqual(id(c1),id(c20))
        self.assertEqual(id(c1),id(c1.__class__._args2obj["TT9901"]))
        c3 = ContractInfo(name="TT9902",ctype=bct, ymonth=9901)
        self.assertNotEqual(id(c1),id(c3))

    def test_real_cached(self):
        zn = Base_ContractType("zn","SHFE",0,0,0,None)
        self.assertEqual(id(zn),id(ZN))
        self.assertEqual(id(zn),id(CM_ALL.cname2ctype("zn1409")))

    def test_serialize_dict(self):
        bct = Base_ContractType("TT","TEST_EXCHANGE",0,0,0,None)
        c1 = ContractInfo(name="TT9901",ctype=bct, ymonth=9901)
        dd = c1.to_dict()
        self.assertEqual("TT9901",dd["_name"])
        self.assertEqual("TEST_EXCHANGE",dd["_exchange_name"])
        cx = c1.from_dict(dd)
        self.assertEqual(id(c1),id(cx)) #从缓存中恢复
        self.assertEqual(id(cx),id(cx.__class__._args2obj["TT9901"]))
        dd["_name"] = "TT9902"
        cx2 = c1.from_dict(dd)
        self.assertNotEqual(id(c1),id(cx2)) #从缓存中恢复
        self.assertEqual(id(cx2),id(cx.__class__._args2obj["TT9902"]))
        self.assertEqual(id(c1._ctype),id(cx2.ctype))        #ctype为从Base_ContractType的缓存中恢复

    def test_serialize_dumps_loads(self):
        bct = Base_ContractType("TT","TEST_EXCHANGE",0,0,0,None)
        c1 = ContractInfo(name="TT9901",ctype=bct, ymonth=9901)
        s1 = dumps(c1)
        cx = loads(s1)
        self.assertEqual(id(c1),id(cx)) #从缓存中恢复
        self.assertEqual(id(cx),id(cx.__class__._args2obj["TT9901"]))
        s2 = s1.replace("TT9901","TT9902")
        cx2 = loads(s2)
        self.assertNotEqual(id(c1),id(cx2)) #从缓存中恢复
        self.assertEqual("TT9902",cx2.name)
        self.assertEqual(id(cx2),id(cx.__class__._args2obj["TT9902"]))
        self.assertEqual(id(c1._ctype),id(cx2.ctype))        #ctype为从Base_ContractType的缓存中恢复

    def test_calc_next_trade_minute(self):
        tf1 = ContractInfo("TF_TEST01",9901,TF)     #contract_name必须不同,否则会被缓存
        self.assertEqual(1300,tf1.calc_next_trade_minute(1129))
        self.assertEqual(1300,tf1.calc_next_trade_minute(1130))
        self.assertEqual(915,tf1.calc_next_trade_minute(914))

    def test_calc_month_diff(self):
        tf1 = ContractInfo("TF_TEST02",1401,TF) #contract_name必须不同,否则会被缓存
        self.assertEqual(1401,tf1._ymonth)
        self.assertEqual(-5,tf1.calc_month_distance(1406))
        self.assertEqual(0,tf1.calc_month_distance(1401))
        self.assertEqual(1,tf1.calc_month_distance(1312))
        self.assertEqual(3,tf1.calc_month_distance(1310))

    def test_calc_margin(self):
        tf1 = ContractInfo("TF_TEST02",1401,TF) #contract_name必须不同,否则会被缓存
        tf1.long_marginrate = 0.1
        tf1.short_marginrate = 0.2
        tf1._multiple = 10000
        self.assertTrue(abs(92451.0-tf1.calc_margin(LONG,92.451))<0.001)
        self.assertTrue(abs(92451.0*2-tf1.calc_margin(SHORT,92.451))<0.001)

    def test_last_dvolume(self):
        tf1 = ContractInfo("TF_TEST03",1401,TF) #contract_name必须不同,否则会被缓存
        with self.assertRaises(IndexError):
            ld = tf1.last_dvolume        #http://stackoverflow.com/questions/12009587/testing-failure-of-an-assignment-with-unittest
        self.assertRaises(IndexError,getattr,tf1,"last_dvolume")        #这样也可以
        tf1._days=[BaseObject(svolume=1000)]
        self.assertEqual(1000,tf1.last_dvolume)
        tf1._ticks.append(BaseObject(dvolume=2000))
        self.assertEqual(2000,tf1.last_dvolume)

    def test_last_price(self):
        tf1 = ContractInfo("TF_TEST",1401,TF)
        with self.assertRaises(IndexError):
            tf1._ticks = []
            tf1._days = []
            tf1._minutes = []
            ld = tf1.last_price        #http://stackoverflow.com/questions/12009587/testing-failure-of-an-assignment-with-unittest
        self.assertRaises(IndexError,getattr,tf1,"last_price")        #这样也
        tf1._days=[BaseObject(sclose=1000)]
        self.assertEqual(1000,tf1.last_price)
        tf1._minutes=[BaseObject(sclose=1500)]
        self.assertEqual(1500,tf1.last_price)
        tf1._ticks.append(BaseObject(price=2000))
        self.assertEqual(2000,tf1.last_price)

    def test_last_drange(self):
        tf1 = ContractInfo("TF_TEST",1401,TF)
        with self.assertRaises(IndexError):
            tf1._ticks = []
            tf1._days = []
            ld = tf1.last_drange
        self.assertRaises(IndexError,getattr,tf1,"last_drange")        #这样也
        tf1.ticks.append(TICK("TEST",20140101))
        tf1.ticks[-1].high = 3000
        tf1.ticks[-1].low = 2950
        self.assertEqual(50,tf1.last_drange)
        tf1._days.append(BaseObject(shigh=3000,slow=2900))
        self.assertEqual(100,tf1.last_drange)

    def test_resume(self):
        zn1411 = ContractInfo("zn1411",1411,ZN)
        if zn1411.minutes:
            zn1411.minutes[:] = []
            zn1411.days[:] = []
        import pyctp2.common.reader as reader
        import pyctp2.common.base as base
        old_data_path = base.DATA_PATH
        base.DATA_PATH = base.TEST_DATA_PATH
        zn1411.resume()
        self.assertEqual(2891,len(zn1411.minutes))
        self.assertEqual(20140929,zn1411.minutes[-1].sdate)
        self.assertEqual(10,len(zn1411.days))
        self.assertEqual(20140929,zn1411.days[-1].sdate)
        self.assertEqual(0,len(zn1411.ticks))
        base.DATA_PATH = old_data_path
        self.assertEqual(140,int(zn1411.last_drange))

    def test_resume2(self):
        zn1411 = ContractInfo("zn1411",1411,ZN)
        if zn1411.minutes:
            zn1411.minutes._instances.clear()
            zn1411.minutes[:] = []
            zn1411.days[:] = []
        import pyctp2.common.reader as reader
        import pyctp2.common.base as base
        old_data_path = base.DATA_PATH
        base.DATA_PATH = base.TEST_DATA_PATH
        #print("in test resume2")
        zn1411.resume(20140925)
        #print("after load minutes")
        self.assertEqual(2066,len(zn1411.minutes))
        self.assertEqual(20140925,zn1411.minutes[-1].sdate)
        self.assertEqual(7,len(zn1411.days))
        self.assertEqual(20140925,zn1411.days[-1].sdate)
        self.assertEqual(0,len(zn1411.ticks))
        base.DATA_PATH = old_data_path
        self.assertEqual(230,int(zn1411.last_drange))
        #print("leave test resume2")


class ContractManagerTest(unittest.TestCase):
    def test_cached(self):
        cs = CM_ALL.current_contracts(2014,8,1)
        cms = dict([ (c.name,c) for c in cs])
        cu1411 = cms["cu1411"]
        cs2 = CM_CU.current_contracts(2014,9,1)
        cms2 = dict([ (c.name,c) for c in cs])
        cu1411_2 = cms2["cu1411"]
        self.assertEqual(id(cu1411),id(cu1411_2))

    def test_tname(self):
        self.assertEqual(ZN,CM_ALL.tname2ctype("zn"))
        self.assertRaises(KeyError,CM_ALL.tname2ctype,"znefp")

    def test_current_contracts_by_ctype(self):
        CM_ALL.current_contracts_by_ctype(CU)
        CM_ALL.current_contracts_by_ctype(CU,2014,5,1)
        self.assertTrue(True)


class ModuleTest(unittest.TestCase):
    def test_calc_delay_map_fin(self):
        cdm = calc_delay_map([(910,914),(915,1129),(1300,1514)])
        #print(cdm)
        self.assertEqual(3,len(cdm))
        self.assertEqual(1300,cdm[1129])
        self.assertEqual(1300,cdm[1130])
        self.assertEqual(915,cdm[914])

    def test_calc_delay_map_com(self):
        cdm = calc_delay_map([(855,859),(900,1014),(1030,1129),(1330,1459)])
        #print(cdm)
        self.assertEqual(5,len(cdm))
        self.assertEqual(1330,cdm[1129])
        self.assertEqual(1330,cdm[1130])
        self.assertEqual(1030,cdm[1014])
        self.assertEqual(1030,cdm[1015])
        self.assertEqual(900,cdm[859])

    def test_calc_delay_map_fin2(self): #跨交易日
        cdm = calc_delay_map([(910,914),(915,1129),(1300,1514),(929,0)])
        #print(cdm)
        self.assertEqual(5,len(cdm))
        self.assertEqual(1300,cdm[1129])
        self.assertEqual(1300,cdm[1130])
        self.assertEqual(915,cdm[914])
        self.assertEqual(929,cdm[1514])
        self.assertEqual(929,cdm[1515])

    def test_calc_delay_map_com2(self):     #跨交易日
        cdm = calc_delay_map([(855,859),(900,1014),(1030,1129),(1330,1459),(914,0)])
        #print(cdm)
        self.assertEqual(7,len(cdm))
        self.assertEqual(1330,cdm[1129])
        self.assertEqual(1330,cdm[1130])
        self.assertEqual(1030,cdm[1014])
        self.assertEqual(1030,cdm[1015])
        self.assertEqual(900,cdm[859])
        self.assertEqual(914,cdm[1459])
        self.assertEqual(914,cdm[1500])


    def test_calc_next_trade_minute(self):
        tf1 = ContractInfo("TF_TEST",9901,TF)
        zn1 = ContractInfo("ZN_TEST",9901,ZN)
        self.assertEqual(1300,calc_next_trade_minute(tf1,1129))
        self.assertEqual(1300,calc_next_trade_minute(tf1,1130))
        self.assertEqual(-1,calc_next_trade_minute(tf1,1514))
        self.assertEqual(-1,calc_next_trade_minute(tf1,1300))
        self.assertEqual(-1,calc_next_trade_minute(tf1,1600))
        self.assertEqual(-1,calc_next_trade_minute(tf1,915))
        self.assertEqual(-1,calc_next_trade_minute(tf1,800))
        self.assertEqual(1330,calc_next_trade_minute(zn1,1129))
        self.assertEqual(1330,calc_next_trade_minute(zn1,1130))
        self.assertEqual(-1,calc_next_trade_minute(zn1,1500))
        self.assertEqual(-1,calc_next_trade_minute(zn1,1330))
        self.assertEqual(-1,calc_next_trade_minute(zn1,1600))
        self.assertEqual(-1,calc_next_trade_minute(zn1,915))
        self.assertEqual(-1,calc_next_trade_minute(zn1,800))

if __name__ == '__main__':
    logging.basicConfig(filename="%s/test_contract_type.log" % (TEST_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    unittest.main()
