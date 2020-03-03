# FRUITpy setup script

from __future__ import (absolute_import, division, print_function)

from setuptools import setup

setup(name='FRUITPy',
      version='0.1.0',
      author='Adrian Croucher',
      author_email="a.croucher@auckland.ac.nz",
      description=('Python interface for the FRUIT Fortran unit testing '
                   'framework'),
      url='https://github.com/acroucher/FRUITPy',
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
          "Operating System :: OS Independent",
      ],
      python_requires='>=2.7',
      py_modules=['FRUIT']
      )
