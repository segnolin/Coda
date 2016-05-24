#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class ImageButton(QPushButton):
    """this class provide image button functions"""

    #constructor
    def __init__(self, button_id, parent):
        super().__init__(parent) #call super class constructor

        self.id = button_id #get button name from positional argument

        self.create_button()

    def create_button(self):

        #set defaults image of button
        self.palette_defaults = QPalette()
        self.palette_defaults.setBrush(self.backgroundRole(), QBrush(QPixmap(":/{0}_button_defaults.png".format(self.id))))

        #set hover image of button
        self.palette_hover = QPalette()
        self.palette_hover.setBrush(self.backgroundRole(), QBrush(QPixmap(":/{0}_button_hover.png".format(self.id))))

        #set press image of button
        self.palette_press = QPalette()
        self.palette_press.setBrush(self.backgroundRole(), QBrush(QPixmap(":/{0}_button_press.png".format(self.id))))

        self.setAutoFillBackground(True)
        self.setPalette(self.palette_defaults)
        self.installEventFilter(self) #call event filter function

    def eventFilter(self, object, event):

        if event.type() == QEvent.HoverMove:

            self.setPalette(self.palette_hover)

        elif event.type() == QEvent.MouseButtonPress:

            self.setPalette(self.palette_press)

        elif event.type() == QEvent.HoverLeave:

            self.setPalette(self.palette_defaults)

        elif event.type() == QEvent.Paint:
            
            return True

        return False