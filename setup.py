#!/usr/bin/env python

from distutils.command.install import install as DistutilsInstall
from setuptools import setup
import os


class MyInstall(DistutilsInstall):

    def run(self):
        print "setup for cwltool-ucsc beginning"
        DistutilsInstall.run(self)
        SETUP_DIR = os.path.dirname(os.path.abspath(__file__))
        PATCH_CMD = 'bash'+SETUP_DIR+'/patch.sh'
        os.system(PATCH_CMD)

setup(name='cwltool-ucsc',
      version='1.0.20170217172322',
      description='A patch for cwltool',
      url='https://github.com/tboser/cwltool-ucsc',
      author='UCSC CGL',
      author_email='tboser@ucsc.edu',
      license='MIT',
      packages=['cwltool-ucsc'],
      cmdclass={'install': MyInstall},
      zip_safe=False)
