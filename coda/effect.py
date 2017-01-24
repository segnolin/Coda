#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.background_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Effect(QLabel):
    '''this class provide transition screen'''

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 1024, 576)

        self.pixel_ratio = QWindow().devicePixelRatio()

    def create(self, mode):

        if mode == 'black_fade':
            self._black_fade()
        elif mode == 'white_fade':
            self._white_fade()

    def _black_fade(self):

        pixmap = QPixmap(':/bg/black.png')
        pixmap = pixmap.scaledToHeight(
                pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        pixmap.setDevicePixelRatio(self.pixel_ratio)
        self.setPixmap(pixmap)

    def _white_fade(self):

        pixmap = QPixmap(':/bg/white.png')
        pixmap = pixmap.scaledToHeight(
                pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        pixmap.setDevicePixelRatio(self.pixel_ratio)
        self.setPixmap(pixmap)
