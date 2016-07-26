#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources.system_resources

class ImageButton(QAbstractButton):
    '''this class provide image button functions'''

    def __init__(self, button_id, parent):
        super().__init__(parent)

        self.id = button_id

        self.pressed.connect(self.update)
        self.released.connect(self.update)

        self.pixmap_defaults = QPixmap(':/sys/{0}_button_defaults.png'.format(self.id))
        self.pixmap_defaults = self.pixmap_defaults.scaledToHeight((self.pixmap_defaults.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.pixmap_defaults.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.pixmap_hover = QPixmap(':/sys/{0}_button_hover.png'.format(self.id))
        self.pixmap_hover = self.pixmap_hover.scaledToHeight((self.pixmap_hover.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.pixmap_hover.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.pixmap_press = QPixmap(':/sys/{0}_button_press.png'.format(self.id))
        self.pixmap_press = self.pixmap_press.scaledToHeight((self.pixmap_press.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.pixmap_press.setDevicePixelRatio(QWindow().devicePixelRatio())

    def paintEvent(self, event):

        pixmap = self.pixmap_hover if self.underMouse() else self.pixmap_defaults
        if self.isDown():
            pixmap = self.pixmap_press

        painter = QPainter(self)
        painter.drawPixmap(0, 0, pixmap)

    def enterEvent(self, event):

        self.update()

    def leaveEvent(self, event):

        self.update()
