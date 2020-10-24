#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension

new_package = "DefSLAM"

code = Extension('_' + new_package,
                 sources=['MapPoint.cc', 'swig_config_wrap.cxx'],
                 libraries=["opencv_core"],
                 library_dirs=['/usr/local/lib'],
                 extra_compile_args=['-lpthread', '-lstdc++',
                    '-I/usr/local/include/opencv4',
                    '-I/usr/include/eigen3',
                    '-I/usr/include/pcl-1.8',
                    '-I/home/user3/slam/DefSLAM',
                    '-I/home/user3/slam/DefSLAM/Modules/Common',
                    '-I/home/user3/slam/DefSLAM/Modules/GroundTruth',
                    '-I/home/user3/slam/DefSLAM/Modules/Mapping',
                    '-I/home/user3/slam/DefSLAM/Modules/Matching',
                    '-I/home/user3/slam/DefSLAM/Modules/Settings',
                    '-I/home/user3/slam/DefSLAM/Modules/Template',
                    '-I/home/user3/slam/DefSLAM/Modules/ToolsPCL',
                    '-I/home/user3/slam/DefSLAM/Modules/Tracking',
                    '-I/home/user3/slam/DefSLAM/Modules/Viewer',
                    '-I/home/user3/slam/DefSLAM/Thirdparty/BBS',
                    '-I/home/user3/slam/DefSLAM/Thirdparty/ORBSLAM_2/include',
                    '-I/usr/include',])

setup(name=new_package,
      version='0.1',
      author="Peter Somers",
      description="""My super awesome casadi code.""",
      ext_modules=[code],
      py_modules=[new_package],
      )
