#!/usr/bin/env python

from setuptools import setup

DESCRIPTION = """
Pydump allows post-mortem debugging for Python programs.

It writes the traceback of an exception into a file and can later load
it in a Python debugger.

Works with the built-in pdb and with other popular debuggers
(pudb, ipdb and pdbpp).
"""

DEV = [
    'pytest',
    'yapf',
    'flake8',
    'invoke',
    'twine',
]

# get version without importing
__version__ = 'unknown'
for line in open('pydump.py'):
    if line.startswith('__version__ = '):
        exec(line)
        break

setup(name='pydump',
      version=__version__,
      description='Post-mortem debugging for Python programs',
      long_description=DESCRIPTION,
      author='Eli Finer',
      license='MIT',
      author_email='eli.finer@gmail.com',
      url='https://github.com/gooli/pydump',
      py_modules=['pydump'],
      extras_require={
          'dev': DEV,
      },
      entry_points={
          'console_scripts': [
              'pydump = pydump:main',
          ],
      },
      classifiers=[
          'Development Status :: 4 - Beta', 'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English', 'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Debuggers'
      ])
