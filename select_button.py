#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class SelectButton(QAbstractButton):
    '''this class provide image button functions'''

    def __init__(self, parent):
        super().__init__(parent)

        self.pixmap_defaults = QPixmap(':/select_button_defaults.png')
        self.pixmap_defaults.setDevicePixelRatio(2)
        self.pixmap_hover = QPixmap(':/select_button_hover.png')
        self.pixmap_hover.setDevicePixelRatio(2)
        self.pixmap_press = QPixmap(':/select_button_press.png')
        self.pixmap_press.setDevicePixelRatio(2)

        self.pressed.connect(self.update)
        self.released.connect(self.update)

        self.txt = ''

    def set_text(self, txt):

        self.txt = txt

    def paintEvent(self, event):

        pixmap = self.pixmap_hover if self.underMouse() else self.pixmap_defaults
        if self.isDown():
            pixmap = self.pixmap_press

        painter = QPainter(self)
        painter.drawPixmap(0, 0, pixmap)
        painter.setPen(Qt.white)
        painter.setFont(QFont('Noto Sans CJK TC Regular', 18))
        painter.drawText(QRect(0, 0, 960, 65), Qt.AlignCenter, self.txt)

    def enterEvent(self, event):

        self.update()

    def leaveEvent(self, event):

        self.update()
