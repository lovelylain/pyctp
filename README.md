pyctp
=====

ctp wrapper for python

简介
-----
（仅仅只是）对于CTP API的Python封装（使用时遇到问题可以在Issues中反馈，但不要咨询实际的交易事项，因为我没实践过`╮(╯_╰)╭`）

CTP版本：futures目录是期货版（包括win32、linux32、linux64），option目录是期权版（包括win32、linux32、linux64），stock目录是linux64股票版，stock2目录是win32股票版

环境：python2.5 ~ python3.4，Windows或者Linux

编译：在本目录或者分别进入futures、option、stock/stock2目录执行`python setup.py build`

安装：
在本目录编译后复制build/lib.xxx-x.x目录下的ctp目录到site-packages目录：
```python
# 通过以下方式使用期货版API
from ctp.futures import ApiStruct, MdApi, TraderApi
# 通过以下方式使用股票版API
from ctp.stock import ApiStruct, MdApi, TraderApi
```
或者进入futures或option、stock/stock2子目录`python setup.py build`编译后`python setup.py install`安装：
```python
# 通过以下方式使用期货/股票版API
from ctp import ApiStruct, MdApi, TraderApi
```
推荐使用第一种方式。

关于代码风格
-----
 本项目只是对于CTP api的封装，大部分代码是生成并非手写，api是给人用而不是给人欣赏内部如何实现的，实用性才是第一考虑：
 - 一套代码支持Python2.5 ~ Python3.x多个版本，直接`python setup.py build`即可编译，不强求特定Python版本或者复杂配置；
 - 干净的模块空间，除了`__author__、__version__`等特殊Python变量，模块中其他变量与API头文件中的符号一一对应；
 - 简洁清晰的注释，每个函数、枚举、typedef、结构体的注释都与API头文件一致，并且标明结构体每个成员的实际基础类型；
 - 结构体和函数参数支持IDE自动补全，并且自动补全时可知道每个参数是字符串、int还是float类型，默认值与提示值一致。

如何配合[原版pyctp](https://code.google.com/p/pyctp/)使用
-----
- 如果在Windows下使用，首先需要安装与Python对应的VS，例如Python2.6 ~ Python3.2可以安装一个`VC++ 2008 Express`；如果在Linux下使用，安装好GCC；
- 在本目录执行`python setup.py build`进行编译；
- 编译后复制build/lib.xxx-x.x目录下的ctp目录到example目录下（如果使用Windows + Python2.7，这3步都可以跳过，因为example目录下已有的ctp就是这个环境下编译的）；
- 按照原版pyctp的[配置说明](https://code.google.com/p/pyctp/wiki/pyctpConfiguration)对example/config目录下的文件进行配置；
- 通过example/main.py加参数运行。

通过以上步骤可知，这里基本上只是对原版[安装指南](https://code.google.com/p/pyctp/wiki/pyctpInstallationGuide)进行了替换；

Windows下除了编译需要安装`VC++ 2008 Express`外，直接使用已编译好的貌似是不需要安装的。
