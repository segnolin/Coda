#!/usr/bin/python
# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

import sys

application_title = 'Coda' #what you want to application to be called
main_python_file = 'main.py' #the name of the python file you use to run the program
base = None

if sys.platform == 'win32':
    
    base = 'Win32GUI'

includes = ['atexit','re']

setup(
        name = application_title,
        version = '0.1',
        description = 'Visual Novel Game Engine',
        options = {'build_exe' : {'includes': includes}},
        executables = [Executable(main_python_file, base = base)])