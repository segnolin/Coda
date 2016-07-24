#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class Mask(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 1024, 576)

    def set_mask(self, mask_id):

        self.mask_id = mask_id

        self.pixmap = QPixmap(':/mk_{0}.png'.format(self.mask_id))
        self.pixmap.setDevicePixelRatio(2)
        self.setPixmap(self.pixmap)

    def set_delete(self):

        self.clear()
