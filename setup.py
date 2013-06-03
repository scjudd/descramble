#!/usr/bin/env python2

import shutil
from distutils.core import setup

shutil.copyfile('descramble.py', 'descramble/descramble')

setup(name="descramble",
      version="20130602",
      description="Solve Scramble with Friends puzzles like a pro.",
      author="Spencer Judd",
      author_email="spencercjudd@gmail.com",
      url="https://github.com/scjudd/descramble",
      packages=['descramble'],
      package_data={'descramble': ['resources/*.png']},
      data_files=[('share/descramble', [
          'descramble/resources/words.marisa'])],
      scripts=['descramble/descramble'],
     )

try:
    os.remove('descramble/descramble')
except:
    pass
