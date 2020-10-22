import subprocess

p = subprocess.Popen(['swig',
                      '-c++',
                      '-python',
                      'swig_config.i'])
p.wait()

p = subprocess.Popen(['python3',
                      'setup.py',
                      'build_ext',
                      '--inplace'])
p.wait()
