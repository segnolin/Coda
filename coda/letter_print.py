#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class LetterPrint(QLabel):
    '''this class provide the label print letter by letter'''

    def __init__(self, parent):
        super().__init__(parent)

        self.txt = ''
        self.index = 0
        self.next_timer = QTimer()
        self.next_timer.setSingleShot(True)

    def set_verbatim_text(self, txt):

        self.txt = txt
        self.index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self._handle_timer)
        self.timer.start(30)

    def _handle_timer(self):

        self.index += 1
        self.setText(self.txt[:self.index])

        if self.index > len(self.txt):
            self.timer.stop()
            self.next_timer.start(0)
