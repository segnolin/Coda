#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ToolTip(QLabel):
    '''this class provide tool tip label'''

    def __init__(self, tool_tip_id, parent):
        super().__init__(parent)

        pixel_ratio = QWindow().devicePixelRatio()

        pixmap = QPixmap(
                ':/sys/{0}_tool_tip.png'.format(tool_tip_id))
        pixmap = pixmap.scaledToHeight(
                pixmap.height() * pixel_ratio / 2,
                Qt.SmoothTransformation)
        pixmap.setDevicePixelRatio(pixel_ratio)
        self.setPixmap(pixmap)
