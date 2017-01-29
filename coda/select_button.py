#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from coda.image_button import *

class SelectButton(ImageButton):
    '''this class provide image button functions'''

    def __init__(self, parent):
        super().__init__('select', parent)

        self.txt = ''
        self.id = ''

    def set_text(self, txt):

        self.txt = txt

    def paintEvent(self, event):

        if self.underMouse(): pixmap = self.pixmap_hover
        else: pixmap = self.pixmap_defaults
        if self.isDown(): pixmap = self.pixmap_press

        painter = QPainter(self)
        painter.drawPixmap(0, 0, pixmap)
        painter.drawText(QRect(0, 0, 960, 65), Qt.AlignCenter, self.txt)
