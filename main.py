#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import resources.icon_resources

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from coda.coda import *

def main():

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling) #set scaling attribute
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps) #set high dpi icon
    app = QApplication(sys.argv) #create new application
    if sys.platform != 'darwin':
        app.setWindowIcon(QIcon(':/ic/coda.png')) #set window icon
    coda = Coda() #create new instance of main window
    coda.show() #make instance visible
    coda.raise_() #raise instance to top of window stack
    sys.exit(app.exec_()) #monitor application for events

if __name__ == '__main__':
    main()
