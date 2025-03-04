from __future__ import print_function
import sys
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]


try:
    import numpy
except ImportError:
    print('numpy is required during installation')
    sys.exit(1)

try:
    import scipy
except ImportError:
    print('scipy is required during installation')
    sys.exit(1)

setup(name='scikit-hyperband',
      version='0.0.2',
      description='A scikit-learn compatible implementation of hyperband for model selection',
      author='Thomas Huijskens',
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      author_email='thomas_huijskens@hotmail.com',
      )
