#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *

from coda.coda import *

def main():

    app = QApplication(sys.argv) #create new application
    coda = Coda() #create new instance of main window
    coda.show() #make instance visible
    coda.raise_() #raise instance to top of window stack
    sys.exit(app.exec_()) #monitor application for events

if __name__ == '__main__':
    main()
