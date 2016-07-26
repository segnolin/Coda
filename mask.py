#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources.mask_resources

class Mask(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 1024, 576)

    def set_mask(self, mask_id):

        self.mask_id = mask_id

        self.pixmap = QPixmap(':/mk/mk_{0}.png'.format(self.mask_id))
        self.pixmap = self.pixmap.scaledToHeight((self.pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.setPixmap(self.pixmap)

    def set_delete(self):

        self.clear()
