#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from coda.save_label import *

class Page(QWidget):
    '''this class creates page layout'''

    def __init__(self, parent):
        super().__init__(parent)

        self._pixel_ratio = QWindow().devicePixelRatio()
        self.thumbnail = {}
        self.label = {}

    def create_page_layout(self, num):

        for i in range(6):
            self.thumbnail[i] = QLabel(self)
            self.thumbnail[i].setGeometry(90 + int(i / 3) * 436, 82
                    + (i % 3) * 136, 192, 108)

        for i in range(6):
            self.label[i] = SaveLabel('save_label', i + num * 6, self)
            self.label[i].setGeometry(84 + int(i / 3) * 436, 76
                    + (i % 3) * 136, 420, 120)
