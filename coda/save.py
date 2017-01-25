#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from coda.image_button import *

class Save(QMainWindow):
    '''this class creates game save layout and functions'''

    def __init__(self):
        super().__init__()

        self.pixel_ratio = QWindow().devicePixelRatio()

    def create_save_layout(self):

        #set QWidget class
        self.save_widget = QWidget()
        self.background = QLabel(self.save_widget)
        self.test_label = QLabel(self.save_widget)

        #set save page background
        self.background_pixmap = QPixmap(':/sys/save_background.png')
        self.background_pixmap = self.background_pixmap.scaledToHeight(
                self.background_pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.background_pixmap.setDevicePixelRatio(self.pixel_ratio)
        self.background.setPixmap(self.background_pixmap)
        self.background.setGeometry(0, 0, 1024, 576)

        #create a back button
        self.save_back_button = ImageButton('save_back', self.save_widget)
        self.save_back_button.setGeometry(844, 490, 96, 32)

    def thumbnail(self, pixmap):

        pixmap = pixmap.scaledToHeight(216 * self.pixel_ratio / 2,
                Qt.SmoothTransformation)

        self.test_label.setPixmap(pixmap)
        self.test_label.setGeometry(90, 82, 192, 108)
