#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class FaderWidget(QWidget):
    '''this class provide fade in/out animation effect'''

    def __init__(self, widget, init_opacity):
        QWidget.__init__(self, widget)

        self.widget = widget
        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(init_opacity)
        self.widget.setGraphicsEffect(self.effect)

    def animate(self, value):

        self.opacity = value

        self.effect.setOpacity(self.opacity)
        self.widget.setGraphicsEffect(self.effect)

    def hide(self, duration):

        self.duration = duration
        self.opacity = 1.0

        self.anime = QVariantAnimation()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(self.duration)
        self.anime.setStartValue(1.0)
        self.anime.setEndValue(0.0)
        self.anime.valueChanged.connect(self.animate)
        self.anime.start()
        
    def show(self, duration):

        self.duration = duration
        self.opacity = 0.0

        self.anime = QVariantAnimation()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(self.duration)
        self.anime.setStartValue(0.0)
        self.anime.setEndValue(1.0)
        self.anime.valueChanged.connect(self.animate)
        self.anime.start()
