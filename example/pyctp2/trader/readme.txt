
运行结构

核心数据结构:

Account:
    SPI
    Trade Command Queue
    帐户信息
        用于在一个TICK周期中计算开平仓的可用数

Environ:
    Accounts
    Instruments信息
        用于计算单手所需的保证金数
        #TODO: 须确认查询返回的保证金率是交易所的还是已做了期货公司调整的

TradeCommandQueue
    独立的交易命令守护线程
    隔离底层交易接口。调用SPI的方法，并承接回调，并进一步回调命令的Callback



3. 处理流程
==>MD SPI thread ->
           ==>Controller Thread
                drive MacroCommand exec (thru Event)
                drive Agent handle
                    -> check 现有position是否需要close
                        -> 确定关闭数量, 在position.open_order中有开仓的Account
                        -> put到 Env
                    -> check 现有策略是否需要新开
                        -> 确定开仓数量，平仓方法. 此时已确定开仓Account
                        -> put到 Env
Env -> 根据Account, Put到相应的TradeCommandQueue中
       并设定Defer的撤单命令，Put到MacroCommandQueue

==>TradeCommandQueue
    解析命令，－> SPI执行
                    -> SPI回调 -> 调用TradeComandQueue的回调设定
                                    -> 调用指定Command的回调
                                            在Position/Order设定相应的完成数量及完成情况
                                            -> 调用指定策略的回调


4. MacroCommandQueue队列
    A. Controller的Tick驱动
    B. EventDaemon的循环驱动, 多少秒？


#2014-07-14
关于头寸管理
1. 开仓
允许同一时刻 开 多个品种的仓位
同时开列的仓位, 其closer以多个品种的position为参数之一

问题:
strategy必须处理开仓失败的情况
A. 单品种开仓失败或者开仓数不足
B. 多品种开仓失败/不足/单边失败
   尤其是多品种失败时,导致各品种仓位不匹配的,需要strategy自行处理,
   调度程序不会做出自动回滚(平掉已成功的仓位)的动作 


