#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

import os

DEFSLAM_MODULES = "/home/user3/slam/DefSLAM/Modules"
ORBSLAM_MODULES = "/home/user3/slam/DefSLAM/Thirdparty"

def append_from_walk(list_s, list_h, path):
    for root, dir, files in os.walk(path):
        for name in files:
            if name.endswith("cc"):
                list_s.append(os.path.join(root, name))
            elif name.endswith("h"):
                list_h.append(os.path.join(root, name))
    return list_s, list_h

sources = []
headers = []

sources, headers = append_from_walk(sources, headers, DEFSLAM_MODULES)
sources, headers = append_from_walk(sources, headers, ORBSLAM_MODULES)
sources.append('swig_config_wrap.cxx')

from distutils.core import setup, Extension

new_package = "DefSLAM"

code = Extension('_' + new_package,
                 sources=sources,
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
