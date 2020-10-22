#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension

new_package = "hello"

code = Extension('_' + new_package,
                 sources=['hello.cc', 'swig_config_wrap.cxx'],
                 extra_compile_args=['-lpthread', '-lstdc++'])

setup(name=new_package,
      version='0.1',
      author="Peter Somers",
      description="""My super awesome casadi code.""",
      ext_modules=[code],
      py_modules=[new_package],
      )
