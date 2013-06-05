#-*- coding:utf-8 -*-

import ConfigParser

import base
import operator
import strategy

CONFIG_PATH = 'config/'

class CSParser(ConfigParser.ConfigParser):
    '''
        设定Option选项为大小写敏感
    '''
    def optionxform(self,option):
        return str(option)

def parse_base(name='base.ini',root='Base'):
    ''' 
        获得基本配置
        其中name为配置文件名
        root为默认的配置段名
        配置文件格式如下:        
            [Base]
            ;User用于设定连接行情的设定 
            users = User1,User2,User3
            ;Trade用于设定连接交易端的设定
            traders = Trader1,Trader2

            [User1]
            port = 
            broker_id = 
            investor_id = 
            passwd = 

            [User2]
            ....
    '''
    #cfg = ConfigParser.ConfigParser()
    cfg = CSParser()
    cfg.read(CONFIG_PATH + name)
    config = base.BaseObject(users={},traders={})
    users = cfg.get(root,'users').split(',')
    traders = cfg.get(root,'traders').split(',')
    for user in users:
        suser = user.strip()
        if suser == '':
            continue
        cuser = base.BaseObject(name = suser)
        cuser.port = cfg.get(suser,'port')
        cuser.broker_id = cfg.get(suser,'broker_id')
        cuser.investor_id = cfg.get(suser,'investor_id')
        cuser.passwd = cfg.get(suser,'passwd')
        config.users[user] = cuser
    for trader in traders:
        strader = trader.strip()
        if strader == '':
            continue
        ctrader = base.BaseObject(name = strader)
        ctrader.port = cfg.get(strader,'port')
        ctrader.broker_id = cfg.get(strader,'broker_id')
        ctrader.investor_id = cfg.get(strader,'investor_id')
        ctrader.passwd = cfg.get(strader,'passwd')
        config.traders[trader] = ctrader
    return config

def parse_strategy(name='strategy.ini',root='strategy'):
    '''
    获得策略配置
    策略配置包括两方面内容:
    1. 保存行情的设置, 其中[Trace_Instruments]为合约类设置
[Trace_Instruments]
traces = IF,ru,fu,zn,rb,pb,m,a,c,y,b,l,p,v,SR,CF,TA,WS,RO,ER,WT
;a/al/au重复,c/cu重复
;traces = IF,ru,fu,cu,al,zn,au,rb,pb,m,a,c,y,b,l,p,v,SR,CF,TA,WS,RO,ER,WT
    ;[Trace_Instruments_Raw]为绝对设置
[Trace_Instruments_Raw]
IFs = IF1104,IF1105,IF1106,IF1109
CFs = CF109,CF107
   2. 交易策略定制 (todo:将来考虑自动判断主力合约) 
    [Alias_Def]
    IF_main = IF1105
    CF_main = CF109
    ;TODO:确定main之后,计算next,third,fourth,分别表示次合约、第三合约、第四合约. 找到主力合约后，按字母序确定
    [Trade_Config]
    ;如果策略文件为strategy，则可以不写
    ;strategy_file = strategy
    traces = IF_main,CF_main
    
    [IF_main]
    max_volume = 2
    strategys = IF_A,IF_B,IF_C

    [IF_A]
    max_holding = 2
    open_volume = 1
    opener = day_long_break
    closer = datr_long_stoper
    
    [IF_B]
    ...
    '''
    #cfg = ConfigParser.ConfigParser()
    print name
    cfg = CSParser()
    cfg.read(CONFIG_PATH + name)
    config = base.BaseObject(traces=set([]),traces_raw=set([]))
    ##基于type的合约
    ts = cfg.get('Trace_Instruments','traces') 
    for t  in ts.split(','):
        st = t.strip()
        if st == '':
            continue
        config.traces.add(st)
    ##基于直接硬编码的合约
    trs = cfg.items('Trace_Instruments_Raw') 
    tvs = reduce(operator.add,[tv.split(',') for to,tv in trs])
    for tv in tvs:
        stv = tv.strip()
        if stv == '':
            continue
        config.traces_raw.add(stv)

    ##Instrument别名定义
    alias = dict(cfg.items('Alias_Def'))
    trace_instruments = cfg.get('Trade_Config','traces').split(',')
    if cfg.has_option('Trade_Config','strategy_file'):#导入策略文件
        sfile = cfg.get('Trade_Config','strategy_file')
        smod = __import__(sfile)
        mms = sfile.split('.')
        for mm in mms[1:]:  #找到最终的那个模块，__import__返回的是顶级模块
            smod = smod.__dict__[mm]
    else:
        smod = strategy
    #print smod.__dict__.keys()
    config.smodule = smod
    config.strategy = {}
    for ti in trace_instruments:
        sti = ti.strip()
        if sti == '':
            continue
        cs = base.BaseObject(name=alias[sti])
        cs.max_volume = int(cfg.get(sti,'max_volume'))
        cs.max_vtimes = int(cfg.get(sti,'max_vtimes'))
        cs.max_lost = int(cfg.get(sti,'max_lost'))
        cs.strategys = []
        for scs in cfg.get(sti,'strategys').split(','):
            sscs = scs.strip()
            if sscs == '':
                continue
            print sscs
            #current_strategy = base.BaseObject(name=sscs)
            #current_strategy.max_holding = int(cfg.get(sscs,'max_holding'))
            #current_strategy.open_volume = int(cfg.get(sscs,'open_volume'))
            #current_strategy.opener = smod.__dict__[cfg.get(sscs,'opener').strip()]()   #需要实例化
            #current_strategy.closer = smod.__dict__[cfg.get(sscs,'closer').strip()]
            current_strategy = strategy.STRATEGY(name = sscs,
                    opener = smod.__dict__[cfg.get(sscs,'opener').strip()],
                    #closer = smod.__dict__[cfg.get(sscs,'closer').strip()],
                    closers = [smod.__dict__[sc.strip()] for sc in cfg.get(sscs,'closers').split(',') if sc.strip()!=''],
                    max_holding = int(cfg.get(sscs,'max_holding')),
                    open_volume = int(cfg.get(sscs,'open_volume')),
                )

            cs.strategys.append(current_strategy)
        config.strategy[sti] = cs
    return config

def parse_state(strategy_cfg,instruments,name='state.ini',root='State'):
    '''现场恢复
    ;
    [State]
    last_update = 20110401
    ;holdings = IF1105,CF109
    holdings = IF1105,CF109

    [IF1105]
    instrument = IF1105
    opened_volume = 5
    opened_orders = IF1105_O1,IF1105_O2

    [IF1105_O1]
    name = IF_A
    volume = 3
    strategy = IF_A    
    ;opener = day_long_break
    stoper = datr_long_stoper_12
    base_price = 32000
    current_stop_price = 31930
    ;target_price = 0

    [IF1105_O2]
    name = IF_B
    volume = 1
    strategy = IF_A    
    ;opener = day_short_break
    stoper = datr_short_stoper_12
    base_price = 32500
    current_stop_price = 32570
    ;target_price = 0

    [CF109]
    instrument = CF109
    opened_volume = 0
    opened_orders =
    '''
    cfg = CSParser()
    cfg.read(CONFIG_PATH + name)
    state = base.BaseObject(last_update = int(cfg.get(root,'last_update').strip()))
    state.holdings = {}
    holdings = cfg.get(root,'holdings')
    for hd in holdings.split(','):
        shd = hd.strip()
        if shd == '':
            continue
        chd = base.BaseObject(name=shd)
        chd.instrument = cfg.get(shd,'instrument').strip()
        state.holdings[chd.instrument] = chd    ##
        chd.opened_volume = int(cfg.get(shd,'opened_volume'))
        chd.orders = []
        oos = cfg.get(shd,'opened_orders').split(',')
        cur_inst = instruments[chd.instrument]
        for oo in oos:
            soo = oo.strip()
            if soo == '':
                continue
            order = base.BaseObject(instrument=chd.instrument)
            order.volume = int(cfg.get(soo,'volume'))
            order.strategy_name = cfg.get(soo,'strategy_name')
            #order.opener = strategy_cfg.smodule.__dict__[cfg.get(soo,'opener').strip()] #仅用于判断strategy
            #order.stoper_class = strategy_cfg.smodule.__dict__[cfg.get(soo,'stoper').strip()]
            
            #order.stoper = strategy_cfg.smodule.__dict__[cfg.get(soo,'stoper').strip()](cur_inst.data,0) #满足签名
            #order.stoper.load_parameters(cfg.get(soo,'stoper_parameters').strip())
            sps = eval(cfg.get(soo,'stopers'))
            order.stopers = []
            print sps
            for stoper,sparameter in sps:
                print stoper.strip()
                xstoper = strategy_cfg.smodule.__dict__[stoper.strip()](cur_inst.data,0)
                xstoper.load_parameters(sparameter)
                order.stopers.append(xstoper)
            #state.mys = cfg.get(soo,'stoper_parameters').strip()   #调试用
            #print cfg.get(soo,'stoper_parameters').strip()
            order.base_price = int(cfg.get(soo,'base_price').strip())
            order.mytime = int(cfg.get(soo,'mytime').strip()) 
            order.action_type = int(cfg.get(soo,'action_type').strip()) 
            #order.stoper.set_cur_stop(int(cfg.get(soo,'current_stop_price').strip()))
            if cfg.has_option(soo,'target_price'):
                order.target_price = int(cfg.get(soo,'target_price'))
            else:
                order.target_price = 0
            chd.orders.append(order)
            #print chd.instrument
    return state

def save_state(state,name='state.ini',root='State'):
    ''' 现场保存
    [State]
    last_update = 20110401
    ;holdings = IF1105,CF109
    holdings = IF1105,CF109

    [IF1105]
    instrument = IF1105
    opened_volume = 5
    opened_orders = IF1105_O1,IF1105_O2

    [IF1105_O1]
    volume = 3
    ;opener = day_long_break
    strategy = IF_A
    stoper = datr_long_stoper_12
    base_price = 32000
    current_stop_price = 31930
    ;target_price = 0

    [IF1105_O2]
    volume = 1
    ;opener = day_short_break
    strategy = IF_B
    stoper = datr_short_stoper_12
    base_price = 32500
    current_stop_price = 32570
    ;target_price = 0

    [CF109]
    instrument = CF109
    opened_volume = 0
    opened_orders =
    '''
    cfg = CSParser()
    cfg.add_section(root)
    cfg.set(root,'holdings',','.join(state.holdings.keys()))
    cfg.set(root,'last_update',state.last_update)
    for key,value in state.holdings.items():
        cfg.add_section(key)
        onum = 1
        cfg.set(key,'instrument',value.instrument.name)
        cfg.set(key,'opened_volume',value.opened_volume)
        ostr = []
        for order in value.orders:
            mystr = '%s_O%d' % (key,onum)
            onum += 1
            ostr.append(mystr)
            cfg.add_section(mystr)
            cfg.set(mystr,'volume',order.volume)
            cfg.set(mystr,'base_price',order.base_price)
            cfg.set(mystr,'mytime',order.mytime)            
            cfg.set(mystr,'action_type',order.action_type)            
            #cfg.set(mystr,'current_stop_price',order.stoper.get_cur_stop())
            cfg.set(mystr,'strategy_name',order.get_strategy_name())
            #cfg.set(mystr,'opener',base.type_name(order.get_opener()))
            #cfg.set(mystr,'opener_parameters',order.get_opener().save_parameters())
            #cfg.set(mystr,'stoper',"('%s',%s)" % (base.type_name(order.get_stoper()),order.stoper.save_parameters()))
            ss =[ "('%s',%s)" % (base.type_name(stoper),stoper.save_parameters()) for stoper in order.get_stopers()]
            cfg.set(mystr,'stopers',','.join(ss)+',')
            #cfg.set(mystr,'stoper',base.type_name(order.get_stoper()))
            #cfg.set(mystr,'stoper_parameters',order.stoper.save_parameters())
            if order.target_price>0:
                cfg.set(mystr,'target_price',order.target_price)
        cfg.set(key,'opened_orders',','.join(ostr))
    fo = open(CONFIG_PATH + name,u'w+')
    cfg.write(fo)
    fo.close()
    return 
