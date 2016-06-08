#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

from coda_class import *

import sys

def main():

    app = QApplication(sys.argv) #create new application
    main_window = Coda() #create new instance of main window
    main_window.show() #make instance visible
    main_window.raise_() #raise instance to top of window stack
    sys.exit(app.exec_()) #monitor application for events

if __name__ == '__main__':
    main()