from distutils.core import setup
from distutils.extension import Extension
try:
    from Cython.Distutils import build_ext
    ext = 'pyx'; cmdclass = {'build_ext': build_ext}
except ImportError:
    ext = 'cpp'; cmdclass = {}
import re, sys, os, struct, shutil
fp = open('ctp/__init__.py', 'rb'); data = fp.read(); fp.close()
if sys.version_info[0] >= 3: data = data.decode('utf-8')
__version__ = re.search(r"__version__ = '(.+?)'", data).group(1)
__author__ = re.search(r"__author__ = '(.+?)'", data).group(1)

PREFIX = ''
BUILD = (
    ('MdApi', 'thostmduserapi'),
    ('TraderApi', 'thosttraderapi'),
)

def platform():
    map1 = {'win32':'win', 'linux2':'linux', 'linux':'linux'}
    map2 = {'darwin':'ios'}
    os = sys.platform
    if os in map1:
        return '%s%d' % (map1[os], struct.calcsize('P')*8)
    return map2.get(os, os)
platform = platform()

api_dir = PREFIX+'api/%s'%platform
include_dirs = [PREFIX+'ctp', api_dir]
library_dirs = [api_dir]
ext_modules = []; package_data = []
for k,v in BUILD:
    extm = Extension(name='ctp._'+k, language='c++',
        include_dirs=include_dirs, library_dirs=library_dirs,
        libraries=[v], sources=['ctp/%s.%s'%(k,ext)],
    )
    ext_modules.append(extm)
    if platform.startswith('win'):
        k = '%s.dll'%v
    else:
        extm.extra_link_args = ['-Wl,-rpath,$ORIGIN']
        k = 'lib%s.so'%v
    package_data.append(k)
    v = 'ctp/' + k
    shutil.copy2('%s/%s'%(api_dir,k), v)

setup(
    name='ctp', version=__version__, author=__author__,
    cmdclass=cmdclass, ext_modules=ext_modules,
    packages=['ctp'], package_dir={'ctp':'ctp'}, package_data={'ctp':package_data},
)
