#!/bin/bash

if [ ! -d "pyinstaller" ]; then
    mkdir pyinstaller
    git clone https://github.com/pyinstaller/pyinstaller.git pyinstaller
fi

python3 pyinstaller/pyinstaller.py main.spec
