#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *

import sys

class DragLabel(QLabel):
    '''this class provide draggable label'''

    def __init__(self, parent):
        super().__init__(parent)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.parent().move(x - x_w, y - y_w)
