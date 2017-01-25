#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.mask_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Mask(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 1024, 576)

        self.id = ''

    def set_mask(self, mask_id):

        self.id = mask_id

        pixel_ratio = QWindow().devicePixelRatio()

        pixmap = QPixmap(':/mk/mk_{0}.png'.format(self.id))
        pixmap = pixmap.scaledToHeight(
                pixmap.height() * pixel_ratio / 2,
                Qt.SmoothTransformation)
        pixmap.setDevicePixelRatio(pixel_ratio)
        self.setPixmap(pixmap)

    def delete_mask(self):

        self.id = ''
        self.clear()
