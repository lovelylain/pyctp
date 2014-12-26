# -*- coding:utf-8 -*-

import unittest
import unittest.mock as mock

from ..common.base import (BaseObject,
                        )
from ..trader.ctp_wrapper import TraderSpiDelegate

class TraderSpiTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_instrument_status(self):
        """
            应当执行的是通道测试而不是逻辑测试, 只需要语句测试即可
            在这里测试逻辑, 重复太多. 测试代码是 运行代码的几倍.
        """
        wrapper = TraderSpiDelegate(mock.Mock(),mock.Mock(),"TEST")
        tmock = mock.Mock()
        wrapper.queue=tmock
        pInstrumentStatus = BaseObject(InstrumentID="TEST",EnterTime="20140101:0855",InstrumentStatus="3")
        wrapper.OnRtnInstrumentStatus(pInstrumentStatus)
        tmock.on_instrument_status.assert_called_once_with(pInstrumentStatus.InstrumentID,pInstrumentStatus.EnterTime,3)
        tmock = mock.Mock()
        wrapper.queue=tmock
        pInstrumentStatus = BaseObject(InstrumentID="TEST",EnterTime="20140101:0855",InstrumentStatus="2")
        wrapper.OnRtnInstrumentStatus(pInstrumentStatus)
        tmock.on_instrument_status.assert_called_once_with(pInstrumentStatus.InstrumentID,pInstrumentStatus.EnterTime,2)
        tmock = mock.Mock()
        wrapper.queue=tmock
        pInstrumentStatus = BaseObject(InstrumentID="TEST",EnterTime="20140101:0855",InstrumentStatus="1")
        wrapper.OnRtnInstrumentStatus(pInstrumentStatus)
        tmock.on_instrument_status.assert_called_once_with(pInstrumentStatus.InstrumentID,pInstrumentStatus.EnterTime,1)


