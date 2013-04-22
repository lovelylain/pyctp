pyctp
=====

ctp wrapper for python

CTP版本：futures目录是期货版（包括win32、linux32、linux64），stock目录是linux64股票版，stock2目录是win32股票版

环境：python2.5 ~ python3.3，Windows或者Linux

编译：分别进入futures、stock、stock2目录执行`python setup.py build`

安装：如果需要同时使用股票版与期货版，可将期货版改名为ctp.futures包（即置于ctp/futures目录），股票版改名为ctp.stock包（即置于ctp/stock目录）
