#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from fader import *
from image_button import *

import sys
import resources

class IntroWindow(QMainWindow):
    '''this class creates a introduction window'''

    def __init__(self):
        super().__init__()

    def create_intro_window_layout(self):

        #set QWidget class
        self.intro_window_widget = QWidget()

        #set background picture by QLabel
        self.intro_background_pixmap = QPixmap(':/intro_background.png')
        self.intro_background_pixmap = self.intro_background_pixmap.scaledToHeight((self.intro_background_pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.intro_background_pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.intro_background = QLabel(self.intro_window_widget)
        self.intro_background.setPixmap(self.intro_background_pixmap)
        self.intro_background.setGeometry(0, 0, 1024, 576)

        QTimer.singleShot(2400, self.change_pixmap)

    def change_pixmap(self):

        self.fader = Fader(self.intro_window_widget, self.intro_window_widget)
        self.fader.fade(500)

        self.intro_background_pixmap = QPixmap(':/black.png')
        self.intro_background_pixmap = self.intro_background_pixmap.scaledToHeight((self.intro_background_pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.intro_background_pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.intro_background.setPixmap(self.intro_background_pixmap)
