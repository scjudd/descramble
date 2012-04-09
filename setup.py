#!/usr/bin/env python2

import shutil
from distutils.core import setup

shutil.copyfile('descramble.py', 'descramble/descramble')

setup(name="descramble",
      version="20120409",
      description="Solve Scramble with Friends puzzles like a pro.",
      author="Spencer Judd",
      author_email="spencercjudd@gmail.com",
      url="https://github.com/scjudd/descramble",
      packages=['descramble'],
      package_data={'descramble': ['resources/*.png']},
      data_files=[('share/descramble', [
          'descramble/resources/TWL_2006_ALPHA.txt'])],
      scripts=['descramble/descramble'],
     )

try:
    os.remove('descramble/descramble')
except:
    pass
