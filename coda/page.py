#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from coda.save_button import *

class Page(QWidget):
    '''this class creates page layout'''

    def __init__(self, parent):
        super().__init__(parent)

        self.thumbnail = {}
        self.text_preview = {}
        self.label = {}
        self.delete = {}

    def create_page_layout(self, num):

        for i in range(6):
            self.thumbnail[i] = QLabel(self)
            self.thumbnail[i].setGeometry(90 + int(i / 3) * 436, 82
                    + (i % 3) * 136, 192, 108)

        for i in range(6):
            self.text_preview[i] = QLabel(self)
            self.text_preview[i].setGeometry(291 + int(i / 3) * 436, 82
                    + (i % 3) * 136, 204, 108)
            self.text_preview[i].setStyleSheet(
                    'QLabel { font-family: Times New Roman;'
                    'font-size: 14px; }')
            self.text_preview[i].setAlignment(Qt.AlignLeft)
            self.text_preview[i].setWordWrap(True)

        for i in range(6):
            self.label[i] = SaveButton('save_label', i + num * 6, self)
            self.label[i].setGeometry(84 + int(i / 3) * 436, 76
                    + (i % 3) * 136, 420, 120)

        for i in range(6):
            self.delete[i] = SaveButton('save_delete', i + num * 6, self)
            self.delete[i].setGeometry(432 + int(i / 3) * 436, 172
                    + (i % 3) * 136, 72, 24)
