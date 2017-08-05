#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from coda.image_button import *

class Log(QWidget):
    '''this class provide log function'''

    def __init__(self, parent):
        super().__init__(parent)

        self.log_count = 0

        self._create_layout()

    def _create_layout(self):

        #create background label
        self.setGeometry(0, 0, 1024, 576)
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1024, 576)
        self.background_label.setStyleSheet(
                'QLabel { background-color: rgba(255, 255, 255, 0.4); }')

        #create back button
        self.log_back_button = ImageButton('log_back', self)
        self.log_back_button.setGeometry(844, 490, 96, 32)

        #create base widget
        self.view_area = QWidget()
        self.view_area.setGeometry(0, 0, 854, 440)
        self.view_area.setStyleSheet(
                'QWidget { background-color: rgba(0, 0, 0, 0); }')

        #create scroll area
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidget(self.view_area)
        self.scroll_area.setGeometry(84, 25, 856, 442)
        self.scroll_area.setStyleSheet(
                'QScrollArea { background-color: rgba(0, 0, 0, 0);\
                        border: 0px; }')

    def set_scroll_position(self):

        self.scroll_area.ensureVisible(0, self.view_area.height(), 0, 0)

    def add_log(self, character, text, log_type):

        self.view_area.setGeometry(0, 0, 854, 440 + 100 * self.log_count)

        label = QLabel(self.view_area)
        label.setGeometry(0, 350 + 100 * self.log_count, 854, 90)
        label.setStyleSheet(
                'QLabel { background-color: rgba(255, 255, 255, 0.8);\
                        border-radius: 6; }')

        character_label = QLabel(label)
        character_label.setAlignment(Qt.AlignLeft)
        character_label.setGeometry(10, 5, 200, 80)
        character_label.setText(character)
        character_label.setStyleSheet(
                'QLabel { background-color: rgba(0, 0, 0, 0); }')
        character_label.setFont(QFont('Times New Roman', 20, QFont.Bold))

        text_label = QLabel(label)
        text_label.setAlignment(Qt.AlignLeft)
        text_label.setGeometry(230, 5, 604, 80)
        text_label.setText(text)
        text_label.setStyleSheet(
                'QLabel { background-color: rgba(0, 0, 0, 0); }')
        if log_type:
            text_label.setFont(QFont('Times New Roman', 18, QFont.Bold))
        else:
            text_label.setFont(QFont('Times New Roman', 18))
        text_label.setWordWrap(True)

        self.log_count += 1
