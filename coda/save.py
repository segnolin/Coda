#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from coda.image_button import *
from coda.fader import *
from coda.save_label import *
from coda.page import *
from coda.save_writer import *

class Save(QMainWindow):
    '''this class creates game save layout and functions'''

    def __init__(self):
        super().__init__()

        self.pixel_ratio = QWindow().devicePixelRatio()

    def create_save_layout(self):

        #set QWidget class
        self.save_widget = QWidget()

        #set save page background
        self.background = QLabel(self.save_widget)
        self.background_pixmap = QPixmap(':/sys/save_background.png')
        self.background_pixmap = self.background_pixmap.scaledToHeight(
                self.background_pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.background_pixmap.setDevicePixelRatio(self.pixel_ratio)
        self.background.setPixmap(self.background_pixmap)
        self.background.setGeometry(0, 0, 1024, 576)

        #create page layout
        self.page = {}
        for i in range(6):
            self.page[i] = Page(self.save_widget)
            self.page[i].create_page_layout(i)
            self.page[i].hide()
            for j in range(6):
                self.page.get(i).label.get(j).clicked.connect(self._save)
        self.page.get(0).show()

        #create save page button
        self.page_background = {}
        self.save_page = {}
        for i in range(6):
            self.page_background[i] = QLabel(self.save_widget)
            self.page_background[i].setGeometry(724 + i * 36, 25, 36, 36)
            self.page_background[i].setStyleSheet('QLabel {background-color: white}')
            self.page_background[i].hide()
        self.page_background[0].show()

        for i in range(6):
            self.save_page[i] = SaveLabel(
                    'save_{0}'.format(i + 1), i, self.save_widget)
            self.save_page[i].setGeometry(724 + i * 36, 25, 36, 36)
            self.save_page[i].clicked.connect(self._change_page)

        #create back button
        self.save_back_button = ImageButton('save_back', self.save_widget)
        self.save_back_button.setGeometry(844, 490, 96, 32)

        #create save writer
        self.save_writer = SaveWriter()

    def add_save(self, save_data, thumbnail):

        self.save_writer.collect(save_data, thumbnail)

    def _save(self):

        save_id = int(self.sender().id)
        print(save_id)

    def _change_page(self):

        page = int(self.sender().id)
        print(page)

        self.fader = Fader(self.save_widget, self.save_widget)
        self.fader.fade(200)

        for i in range(6):
            self.page[i].hide()
            self.page_background[i].hide()
        self.page[page].show()
        self.page_background[page].show()
