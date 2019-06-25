# FRUITpy setup script

from __future__ import (absolute_import, division, print_function)

from distutils.core import setup


setup(name='FRUITPy',
      version='0.1.0',
      description=('Python interface for the FRUIT Fortran unit testing '
                   'framework'),
      author='Adrian Croucher',
      author_email='a.croucher@auckland.ac.nz',
      url='https://github.com/acroucher/FRUITPy',
      license='GPL',
      py_modules=['FRUIT'],
      )
