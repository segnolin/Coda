#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class Effect(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 1024, 576)

    def create(self, mode):

        self.mode = mode

        if self.mode == 'black_fade':
            self.black_fade()
        elif self.mode == 'white_fade':
            self.white_fade()

    def black_fade(self):

        self.pixmap = QPixmap(':/black.png')
        self.pixmap.setDevicePixelRatio(2)
        self.setPixmap(self.pixmap)

    def white_fade(self):

        self.pixmap = QPixmap(':/white.png')
        self.pixmap.setDevicePixelRatio(2)
        self.setPixmap(self.pixmap)
