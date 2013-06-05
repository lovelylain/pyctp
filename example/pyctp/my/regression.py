# -*- coding: utf-8 -*-
'''
    遍历指定目录下的所有测试文件，运行其中的测试用例
'''
#This file is licensed under the Apache License Version 2.0
#author: enceladus.smth@gmail.com

import logging

import sys, os, os.path, re, unittest

TEST_FILE_PATTERN = 'test\.py$' #默认的测试文件名为以test.py结尾的文件,以test开头的.py文件的pattern串为：'\Atest\w*\.py$'
IGNORE_DIR_TYPE = ".svn,CVS"

logger = logging.getLogger('regression')

def find_tests_in_directory(root_path,sub_path): #root_path:起始目录，sub_path:目标目录，相对于起始目录的路径
    sub_package = sub_path.replace(os.path.sep,'.')
    filenames = [ os.path.splitext(name)[0] for name in os.listdir(sub_path) if find_tests_in_directory.pattern.search(name) ]
    module_names = [ sub_package and sub_package + '.' + name or name for name in filenames ]
    #print module_names
    gs,ls = globals(),locals()
    modules = [ __import__(module_name,gs,ls,[sub_package]) for module_name in module_names]    #只有这样才返回导入的module,否则导入xxx.yyy时，返回的是xxx，而不是yyy.参见__import__的文档
    #print root_path,sub_path,modules
    tests = [ unittest.defaultTestLoader.loadTestsFromModule(module) for module in modules ]
    #print sub_path,[ test.countTestCases() for test in tests]
    #return unittest.TestSuite()
    return unittest.TestSuite(tests)

def find_all_tests():
    all_tests = unittest.TestSuite()
    root_path = os.getcwd()
    sys.path.append(root_path)
    len_root_path = len(root_path)
    for root,dirs,files in os.walk(root_path):    
        #绝对目录遍历时内部修改当前工作目录不会对遍历过程产生影响(相对目录会有影响.walk假设相对目录遍历时，不在内部变动目录)
        #print root  #查看是不是会遍历所有子目录以及孙子目录
        for entry in find_all_tests.ignore:
            if(entry in dirs):
                dirs.remove(entry)
        sub_path = root[len_root_path+1:]    #获得相对于root_path的目录
        #print sub_path
        all_tests.addTest(find_tests_in_directory(root_path,sub_path))
    return all_tests


def setUp():
    from StringIO import StringIO
    tmp = sys.stdout
    sys.stdout = StringIO()  #将标准I/O流重定向到buff对象，抑制输出
    return tmp

def tearDown(tmp):
    sout = sys.stdout.getvalue()
    logger.debug(u'regression 控制台输出:%s',sout)
    sys.stdout = tmp        #恢复标准I/O流
    #print sout

#regression_test.pattern = re.compile(TEST_FILE_PATTERN, re.IGNORECASE)
find_tests_in_directory.pattern = re.compile(TEST_FILE_PATTERN, re.IGNORECASE)
find_all_tests.ignore = IGNORE_DIR_TYPE

import optparse
if __name__ == "__main__":                   
    logging.basicConfig(filename="regression.log",level=logging.DEBUG,format='#%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    #unittest.main(defaultTest="regression_test")
    parser = optparse.OptionParser()
    #parser.add_option("-r","--recursion", action="store_true", dest="recursion",help="遍历所有子目录下的测试")    #所有子目录
    parser.add_option("-o","--only", action="store_true", dest="only",help=u"只执行指定目录下的测试，不包含子目录. 未指定时遍历所有子目录")    #只当前目录
    parser.add_option('-d',"--directory",default='.',dest='directory',help=u"测试起始目录")
    parser.add_option('-f',"--force",action="store_true",dest='force',help=u"强制本文件所在目录为测试起始目录，优先于-d")
    parser.add_option('-p',"--pattern",default='test\.py$',dest='pattern',help=u"测试文件名模式")
    parser.add_option('-i',"--ignore",default=IGNORE_DIR_TYPE,dest='ignore',help=u"忽略的目录，比如.svn/cvs,目录名以逗号隔开")
    
    options,arguments = parser.parse_args()   
    find_all_tests.ignore = options.ignore.split(',')
    #regression_test.pattern = re.compile(options.pattern, re.IGNORECASE)
    find_tests_in_directory.pattern = re.compile(options.pattern, re.IGNORECASE)
    file_path = lambda filename : os.path.split(os.path.abspath(filename))[0]   #根据相对路径文件名获得绝对路径
    #print __file__,file_path(__file__)
    target_directory = options.force and file_path(__file__) or options.directory
    os.chdir(target_directory)
    test_runner = unittest.TextTestRunner()
    tmp = setUp()
    if(options.only):
        test_runner.run(find_tests_in_directory(target_directory,''))    #不能直接使用unittest.main,会导致命令行参数冲突
    else:
        test_runner.run(find_all_tests())   #不能直接使用unittest.main,会导致命令行参数冲突
    tearDown(tmp)

