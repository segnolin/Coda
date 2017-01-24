#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.background_resources
import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from coda.fader import *
from coda.image_button import *

class IntroWindow(QMainWindow):
    '''this class creates a introduction window'''

    def __init__(self):
        super().__init__()

        self._pixel_ratio = QWindow().devicePixelRatio()

    def create_intro_window_layout(self):

        #set QWidget class
        self.intro_window_widget = QWidget()

        #set background picture by QLabel
        intro_background_pixmap = QPixmap(':/sys/intro_background.png')
        intro_background_pixmap = intro_background_pixmap.scaledToHeight(
                intro_background_pixmap.height() * self._pixel_ratio / 2,
                Qt.SmoothTransformation)
        intro_background_pixmap.setDevicePixelRatio(self._pixel_ratio)
        self.intro_background = QLabel(self.intro_window_widget)
        self.intro_background.setPixmap(intro_background_pixmap)
        self.intro_background.setGeometry(0, 0, 1024, 576)

        QTimer.singleShot(2400, self._change_pixmap)

    def _change_pixmap(self):

        fader = Fader(self.intro_window_widget, self.intro_window_widget)
        fader.fade(500)

        intro_background_pixmap = QPixmap(':/bg/white.png')
        intro_background_pixmap = intro_background_pixmap.scaledToHeight(
                intro_background_pixmap.height() * self._pixel_ratio / 2,
                Qt.SmoothTransformation)
        intro_background_pixmap.setDevicePixelRatio(self._pixel_ratio)
        self.intro_background.setPixmap(intro_background_pixmap)
