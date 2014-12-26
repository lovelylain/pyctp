
import unittest
from ..common.controller import (SyncLastMap,
                            )


class SyncLastMapTestCase(unittest.TestCase):
    def setUp(self):
        self._smap = SyncLastMap()
        self._smap.reset(["CTest"])

    def test_last_time(self):
        self.assertRaises(AssertionError,self._smap.check,"CTEST","13:59:01","0",123456)
        self.assertTrue(self._smap.check("CTest","13:59:01","0",123456))
        self.assertFalse(self._smap.check("CTest","13:59:01","0",123456))
        self.assertTrue(self._smap.check("CTest","13:59:01","500",123456))
        self.assertTrue(self._smap.check("CTest","13:59:02","0",123456))
        self.assertTrue(self._smap.check("CTest","13:59:02","0",123457))
        self.assertFalse(self._smap.check("CTest","13:59:02","0",123457))

    def test_next_day(self):
        self.assertTrue(self._smap.check("CTest","23:59:01","0",123456))
        self.assertTrue(self._smap.check("CTest","23:59:59","0",123456))
        self.assertTrue(self._smap.check("CTest","00:00:01","500",123457))
        self.assertTrue(self._smap.check("CTest","00:00:02","500",123457))

    def test_next_day2(self):
        self.assertTrue(self._smap.check("CTest","23:59:01","0",123456))
        self.assertTrue(self._smap.check("CTest","23:59:59","0",123456))
        self.assertFalse(self._smap.check("CTest","00:00:01","500",123456))
