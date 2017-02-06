#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ToggleButton(QAbstractButton):
    '''this class provide toggle button functions'''

    mouse_hover = pyqtSignal(bool)

    def __init__(self, button_id, parent):
        super().__init__(parent)

        self.state = 0

        pixel_ratio = QWindow().devicePixelRatio()

        self.pixmap_state_0 = QPixmap(
                ':/sys/{0}_button_state_0.png'.format(button_id))
        self.pixmap_state_0 = self.pixmap_state_0.scaledToHeight(
                self.pixmap_state_0.height() * pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.pixmap_state_0.setDevicePixelRatio(pixel_ratio)
        self.pixmap_state_1 = QPixmap(
                ':/sys/{0}_button_state_1.png'.format(button_id))
        self.pixmap_state_1 = self.pixmap_state_1.scaledToHeight(
                self.pixmap_state_1.height() * pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.pixmap_state_1.setDevicePixelRatio(pixel_ratio)
        self.pixmap_hover = QPixmap(
                ':/sys/{0}_button_hover.png'.format(button_id))
        self.pixmap_hover = self.pixmap_hover.scaledToHeight(
                self.pixmap_hover.height() * pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.pixmap_hover.setDevicePixelRatio(pixel_ratio)
        self.pixmap_press = QPixmap(
                ':/sys/{0}_button_press.png'.format(button_id))
        self.pixmap_press = self.pixmap_press.scaledToHeight(
                self.pixmap_press.height() * pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.pixmap_press.setDevicePixelRatio(pixel_ratio)

        self.pressed.connect(self.update)
        self.released.connect(self.update)
        self.clicked.connect(self._change_state)

    def _change_state(self):

        if self.state == 0:
            self.state = 1
        else: self.state = 0

    def enterEvent(self, event):

        self.mouse_hover.emit(True)
        self.update()

    def leaveEvent(self, event):

        self.mouse_hover.emit(False)
        self.update()

    def paintEvent(self, event):

        if self.underMouse():
            if self.state == 0: pixmap = self.pixmap_hover
            else: pixmap = self.pixmap_state_1
        else:
            if self.state == 0: pixmap = self.pixmap_state_0
            else: pixmap = self.pixmap_state_1
        if self.isDown(): pixmap = self.pixmap_press

        painter = QPainter(self)
        painter.drawPixmap(0, 0, pixmap)
