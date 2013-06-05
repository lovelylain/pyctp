#-*- coding:utf-8 -*-

import sys, time
from pyctp.my import entry

from ctp.futures import ApiStruct
ApiStruct.BaseStruct.__str__ = lambda self: '[%s]' % ', '.join(
    '%s=%s'%(k,getattr(self,k)) for k,t in self._fields_)
# oenc, oerr = ctypes.set_conversion_mode('gbk','ignore')
reload(sys); sys.setdefaultencoding('gbk')

if __name__=="__main__":
    try:
        agent = getattr(entry, sys.argv[1])()
        try:
            while 1: time.sleep(1)
        except KeyboardInterrupt:
            agent.mdapis = []; agent.trader = None
    except (IndexError, AttributeError):
        print 'Usage: %s [save_demo|trade_demo|trade_mock|d_demo|t_demo]' % sys.argv[0]
