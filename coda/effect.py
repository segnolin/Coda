#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources.background_resources

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

        self.pixmap = QPixmap(':/bg/black.png')
        self.pixmap = self.pixmap.scaledToHeight((self.pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.setPixmap(self.pixmap)

    def white_fade(self):

        self.pixmap = QPixmap(':/bg/white.png')
        self.pixmap = self.pixmap.scaledToHeight((self.pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.setPixmap(self.pixmap)
