#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from coda.image_button import *

import sys
import resources.system_resources

class Load(QMainWindow):
    '''this class creates game load layout and functions'''

    def __init__(self):
        super().__init__()

    def create_load_layout(self, status):

        self.status = status
        print(self.status)

        #set QWidget class
        self.load_widget = QOpenGLWidget()

        #set load page background
        self.background_pixmap = QPixmap(':/sys/load_background.png')
        self.background_pixmap = self.background_pixmap.scaledToHeight((self.background_pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.background_pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.background = QLabel(self.load_widget)
        self.background.setPixmap(self.background_pixmap)
        self.background.setGeometry(0, 0, 1024, 576)

        #create a strat button
        self.main_start_button = ImageButton('main_start', self.load_widget)
        self.main_start_button.setGeometry(73, 490, 96, 32)

        #create a exit button
        self.main_exit_button = ImageButton('main_quit', self.load_widget)
        self.main_exit_button.setGeometry(813, 490, 96, 32)
