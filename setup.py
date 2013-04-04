from distutils.core import setup
from distutils.extension import Extension
from sys import platform
import sys, os, struct, shutil
v = sys.dont_write_bytecode; sys.dont_write_bytecode = 1
from ctp import __version__, __author__
sys.dont_write_bytecode = v

BUILD = (
    ('MdApi', 'thostmduserapi'),
    ('TraderApi', 'thosttraderapi'),
)

if platform != 'win32': platform = 'linux' + str(struct.calcsize('P') * 8)
api_dir = 'api/%s'%platform
include_dirs = ['ctp', api_dir]
library_dirs = [api_dir]
ext_modules = []; package_data = []
for k,v in BUILD:
    ext_modules.append(Extension(name='ctp._'+k, language='c++',
        include_dirs=include_dirs, library_dirs=library_dirs,
        libraries=[v], sources=['ctp/%s.cpp'%k],
    ))
    if platform == 'win32':
        k = '%s.dll'%v
        package_data.append(k)
        v = 'ctp/' + k
        if not os.path.exists(v):
            shutil.copy2('%s/%s'%(api_dir,k), v)

setup(
    name='ctp', version=__version__, author=__author__,
    cmdclass={}, ext_modules=ext_modules,
    packages=['ctp'], package_dir={'ctp':'ctp'}, package_data={'ctp':package_data},
)
