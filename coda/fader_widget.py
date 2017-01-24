#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class FaderWidget(QWidget):
    '''this class provide fade in/out animation effect'''

    def __init__(self, widget, init_opacity):
        QWidget.__init__(self, widget)

        self.effect = QGraphicsOpacityEffect()
        self.effect.setOpacity(init_opacity)
        self.widget = widget
        self.widget.setGraphicsEffect(self.effect)

    def hide(self, duration):

        self.opacity = 1.0

        self.anime = QVariantAnimation()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(duration)
        self.anime.setStartValue(1.0)
        self.anime.setEndValue(0.0)
        self.anime.valueChanged.connect(self._animate)
        self.anime.start()

    def show(self, duration):

        self.opacity = 0.0

        self.anime = QVariantAnimation()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(duration)
        self.anime.setStartValue(0.0)
        self.anime.setEndValue(1.0)
        self.anime.valueChanged.connect(self._animate)
        self.anime.start()

    def _animate(self, value):

        self.opacity = value

        self.effect.setOpacity(self.opacity)
        self.widget.setGraphicsEffect(self.effect)
