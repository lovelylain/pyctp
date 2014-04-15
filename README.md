pyctp
=====

ctp wrapper for python

简介
-----
（仅仅只是）对于CTP API的Python封装（使用时遇到问题可以在Issues中反馈，但不要咨询实际的交易事项，因为我没实践过）

CTP版本：futures目录是期货版（包括win32、linux32、linux64），stock目录是linux64股票版，stock2目录是win32股票版

环境：python2.5 ~ python3.3，Windows或者Linux

编译：在本目录或者分别进入futures、stock/stock2目录执行`python setup.py build`

安装：
在本目录编译后复制build/lib.xxx-x.x目录下的ctp目录到site-packages目录：
```python
# 通过以下方式使用期货版API
from ctp.futures import ApiStruct, MdApi, TraderApi
# 通过以下方式使用股票版API
from ctp.stock import ApiStruct, MdApi, TraderApi
```
或者进入futures或stock/stock2子目录`python setup.py build`编译后`python setup.py install`安装：
```python
# 通过以下方式使用期货/股票版API
from ctp import ApiStruct, MdApi, TraderApi
```
推荐使用第一种方式。

如何配合[原版pyctp](https://code.google.com/p/pyctp/)使用
-----
- 如果在Windows下使用，首先需要安装与Python对应的VS，例如Python2.6 ~ Python3.2可以安装一个`VC++ 2008 Express`；如果在Linux下使用，安装好GCC；
- 在本目录执行`python setup.py build`进行编译；
- 编译后复制build/lib.xxx-x.x目录下的ctp目录到example目录下（如果使用Windows + Python2.7，这3步都可以跳过，因为example目录下已有的ctp就是这个环境下编译的）；
- 按照原版pyctp的[配置说明](https://code.google.com/p/pyctp/wiki/pyctpConfiguration)对example/config目录下的文件进行配置；
- 通过example/main.py加参数运行。

通过以上步骤可知，这里基本上只是对原版[安装指南](https://code.google.com/p/pyctp/wiki/pyctpInstallationGuide)进行了替换；

Windows下除了编译需要安装`VC++ 2008 Express`外，直接使用已编译好的貌似是不需要安装的。
