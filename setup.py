import os, shutil, sys
from distutils.core import setup
from distutils.util import get_platform

TASKS = (
    ('futures', None, 'ctp'),
    ('stock2' if sys.platform == 'win32' else 'stock', 'stock', 'ctp'),
)

dir = 'lib.%s-%s' % (get_platform(), sys.version[0:3])
pwd = os.getcwd()
build_dir = os.path.join(pwd, 'build', dir, 'ctp')

if sys.version_info[0] >= 3:
    def execfile(path):
        fp = open(path, 'U'); data = fp.read(); fp.close()
        exec(data.rstrip()+'\n')

def build():
    sys.argv[1:] = ('build',)
    if not os.path.isdir(build_dir): os.makedirs(build_dir)
    open(os.path.join(build_dir, '__init__.py'), 'wb').close()
    for d,o,t in TASKS:
        os.chdir(d); execfile('setup.py')
        dir2 = os.path.join(build_dir, o or d)
        if os.path.exists(dir2): shutil.rmtree(dir2)
        shutil.move(os.path.join('build', dir, t), dir2)
        shutil.rmtree('build'); os.chdir(pwd)

def install():
    sys.stderr.write('Please copy "%s" manually.\n' % build_dir)

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'build': return build()
        elif sys.argv[1] == 'install': return install()
    sys.stderr.write('usage: setup.py build\n')

if __name__ == '__main__':
    main()
