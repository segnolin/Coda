#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class ImageButton(QAbstractButton):
    '''this class provide image button functions'''

    def __init__(self, button_id, parent):
        super().__init__(parent)

        self.id = button_id

        self.pressed.connect(self.update)
        self.released.connect(self.update)

        self.pixmap_defaults = QPixmap(':/{0}_button_defaults.png'.format(self.id))
        self.pixmap_hover = QPixmap(':/{0}_button_hover.png'.format(self.id))
        self.pixmap_press = QPixmap(':/{0}_button_press.png'.format(self.id))

    def paintEvent(self, event):

        pixmap = self.pixmap_hover if self.underMouse() else self.pixmap_defaults
        if self.isDown():
            pixmap = self.pixmap_press

        painter = QPainter(self)
        painter.drawPixmap(event.rect(), pixmap)

    def enterEvent(self, event):

        self.update()

    def leaveEvent(self, event):

        self.update()
