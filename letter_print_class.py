#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class LetterPrint(QLabel):
    """this class provide the label print letter by letter"""

    #constructor
    def __init__(self, parent):
        super().__init__(parent) #call super class constructor

    def set_text(self, text):

        self.text = text #get text from positional argument
        self.index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_timer)
        self.timer.start(30)

    def handle_timer(self):

        self.index += 1
        self.setText(self.text[:self.index])

        if self.index > len(self.text):
            self.timer.stop()