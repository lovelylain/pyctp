# -*- coding:utf-8 -*-

"""
    deprecated, 使用md2
    在pyctp2的父目录,执行ipython3
    并且在提示行
    import pyctp2.testbed.ctp as ctp
"""

import logging

from ..common.base import BaseObject,INFO_PATH,DATA_PATH
from ..md import ctp_md as cm
from ..common import controller as ctl
from ..common.contract_type import CM_ALL,CM_SH,CM_DL,CM_ZZ,CM_ZJ
from ..common.contract_type import CM_CU,CM_AL,CM_ZN,CM_AU,CM_AG,ContractManager,A    #测试用
from ..md import save_agent as save_agent

from ..my.md_ports import ZSUser1,ZSUser2

def make_user(ucfg,contract_manager,fpath='md'):
    mdagent = save_agent.SaveAgent(contract_manager,DATA_PATH)
    controller = ctl.Controller([mdagent])
    tt = ctl.TimeTrigger(152000,controller.day_finalize)
    md_spi = cm.MdSpiDelegate(name=ucfg.name,
                             broker_id=ucfg.broker_id,
                             investor_id= ucfg.investor_id,
                             passwd= ucfg.passwd,
                             controller = controller,
                    )
    user = md_spi
    user.Create('%s/%s' % (INFO_PATH,fpath))
    controller.add_listener(md_spi)
    controller.update_listened_contracts()
    user.RegisterFront(ucfg.port)
    #print('before init')
    user.Init()
    return controller

def make_users(mdusers,contract_manager):
    mdagent = save_agent.SaveAgent(contract_manager,DATA_PATH)
    controller = ctl.Controller([mdagent])
    tt = ctl.TimeTrigger(152000,controller.day_finalize)
    #tt = ctl.TimeTrigger(223200,controller.day_finalize,30)
    users = []
    for mduser in mdusers:
        md_spi = cm.MdSpiDelegate(name=mduser.name, 
                                 broker_id=mduser.broker_id,
                                 investor_id= mduser.investor_id,
                                 passwd= mduser.passwd,
                                 controller = controller,
                        )
        user = md_spi
        user.Create('%s/%s' % (INFO_PATH,mduser.name))
        controller.add_listener(md_spi)
        user.RegisterFront(mduser.port)
        #print('before init')
        user.Init()
        users.append(user)
    controller.update_listened_contracts()
    return controller,users,tt

def make_users2(mdusers,contract_manager):
    controller = ctl.Controller()
    mdagent = save_agent.SaveAgent(contract_manager,DATA_PATH)
    controller.register_agent(mdagent)
    #tt = ctl.TimeTrigger(152000,controller.day_finalize)
    #tt = ctl.TimeTrigger(223200,controller.day_finalize,30)
    tt = ctl.Scheduler(160000,controller.day_finalize,12*60*60)
    users = []
    for mduser in mdusers:
        md_spi = cm.MdSpiDelegate(name=mduser.name, 
                                 broker_id=mduser.broker_id,
                                 investor_id= mduser.investor_id,
                                 passwd= mduser.passwd,
                                 controller = controller,
                        )
        user = md_spi
        user.Create('%s/%s' % (INFO_PATH,mduser.name))
        controller.add_listener(md_spi)
        user.RegisterFront(mduser.port)
        #print('before init')
        user.Init()
        users.append(user)
    controller.reset()
    return controller,users#,tt


def make_users_t(mdusers,contract_manager):
    controller = ctl.Controller()
    mdagent = save_agent.TSaveAgent(contract_manager,DATA_PATH)
    mdagent.start()
    controller.register_agent(mdagent)
    #tt = ctl.TimeTrigger(152000,controller.day_finalize)
    #tt = ctl.TimeTrigger(223200,controller.day_finalize,30)
    tt = ctl.Scheduler(160000,controller.day_finalize,12*60*60)
    users = []
    for mduser in mdusers:
        md_spi = cm.MdSpiDelegate(name=mduser.name, 
                                 broker_id=mduser.broker_id,
                                 investor_id= mduser.investor_id,
                                 passwd= mduser.passwd,
                                 controller = controller,
                        )
        user = md_spi
        user.Create('%s/%s' % (INFO_PATH,mduser.name))
        controller.add_listener(md_spi)
        user.RegisterFront(mduser.port)
        #print('before init')
        user.Init()
        users.append(user)
    controller.reset()
    return controller,users#,tt

def make_users_t2(mdusers,contract_managers):
    controller = ctl.Controller()
    mdagents = [save_agent.TSaveAgent(cmng,DATA_PATH) for cmng in contract_managers]
    for mdagent in mdagents:
        mdagent.start()
        controller.register_agent(mdagent)
    #tt = ctl.TimeTrigger(152000,controller.day_finalize)
    #tt = ctl.TimeTrigger(223200,controller.day_finalize,30)
    tt = ctl.Scheduler(160000,controller.day_finalize,12*60*60)
    users = []
    for mduser in mdusers:
        md_spi = cm.MdSpiDelegate(name=mduser.name, 
                                 broker_id=mduser.broker_id,
                                 investor_id= mduser.investor_id,
                                 passwd= mduser.passwd,
                                 controller = controller,
                        )
        user = md_spi
        user.Create('%s/%s' % (INFO_PATH,mduser.name))
        controller.add_listener(md_spi)
        user.RegisterFront(mduser.port)
        #print('before init')
        user.Init()
        users.append(user)
    controller.reset()
    return controller,users#,tt

def make_users_c(mdusers,contract_managers):
    controller = ctl.TController()
    mdagents = [save_agent.SaveAgent(cmng,DATA_PATH) for cmng in contract_managers]
    for mdagent in mdagents:
        controller.register_agent(mdagent)
    #tt = ctl.TimeTrigger(152000,controller.day_finalize)
    #tt = ctl.TimeTrigger(223200,controller.day_finalize,30)
    #tt = ctl.Scheduler(160000,controller.day_finalize,12*60*60)
    tt = ctl.Scheduler(160000,controller.day_finalize,24*60*60)
    #tt = ctl.Scheduler(160000,controller.day_finalize,30)
    users = []
    for mduser in mdusers:
        md_spi = cm.MdSpiDelegate(name=mduser.name, 
                                 broker_id=mduser.broker_id,
                                 investor_id= mduser.investor_id,
                                 passwd= mduser.passwd,
                                 controller = controller,
                        )
        user = md_spi
        user.Create('%s/%s' % (INFO_PATH,mduser.name))
        controller.add_listener(md_spi)
        user.RegisterFront(mduser.port)
        #print('before init')
        user.Init()
        users.append(user)
    controller.reset()
    controller.start()
    return controller,users#,tt

def t2014022701():
    logging.basicConfig(filename="%s/pyctp2_t2014022701.log" % (INFO_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    return make_user(ZSUser1,CM_ALL)

def t2014031601():
    logging.basicConfig(filename="%s/pyctp2_t2014031601.log" % (INFO_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    return make_users([ZSUser1,ZSUser2],CM_ALL)

def t2014032701():
    logging.basicConfig(filename="%s/pyctp2_t2014032701.log" % (INFO_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    return make_users2([ZSUser1,ZSUser1,ZSUser1,ZSUser2,ZSUser2,ZSUser2],CM_ALL)

def t20140515t():
    logging.basicConfig(filename="%s/pyctp2_t2014032701.log" % (INFO_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    return make_users_t([ZSUser1,ZSUser1,ZSUser1,ZSUser2,ZSUser2,ZSUser2],CM_ALL)

def t20140515t2():
    logging.basicConfig(filename="%s/pyctp2_t2014032701.log" % (INFO_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    return make_users_t2([ZSUser1,ZSUser1,ZSUser1,ZSUser2,ZSUser2,ZSUser2],[CM_CU,CM_AL,CM_ZN,CM_AG,CM_AU])
    #return make_users_t2([ZSUser1,ZSUser1,ZSUser1,ZSUser2,ZSUser2,ZSUser2],[CM_CU,CM_AG,CM_AU])

def t20140515c():
    '''
        当前使用版本
    '''
    logging.basicConfig(filename="%s/pyctp2_t2014032701.log" % (INFO_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    return make_users_c([ZSUser1,ZSUser2],[CM_ALL])

def t20140515d():
    '''
        当前使用版本
    '''
    logging.basicConfig(filename="%s/pyctp2_t2014032701.log" % (INFO_PATH,),level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    return make_users_c([ZSUser1,ZSUser2],[ContractManager([A])])
