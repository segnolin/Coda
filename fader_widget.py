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

    def hide(self, duration):

        self.duration = duration
        self.opacity = 1.0

        self.timeline = QTimeLine()
        self.timeline.setUpdateInterval(1000 / 60)
        self.timeline.setCurveShape(QTimeLine.EaseInOutCurve)
        self.timeline.valueChanged.connect(self.hide_animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(self.duration)
        self.timeline.start()

        self.resize(960, 540)

    def hide_animate(self, value):

        self.opacity = 1.0 - value

        self.effect.setOpacity(self.opacity)
        self.widget.setGraphicsEffect(self.effect)

    def show(self, duration):

        self.duration = duration
        self.opacity = 0.0

        self.timeline = QTimeLine()
        self.timeline.setUpdateInterval(1000 / 60)
        self.timeline.setCurveShape(QTimeLine.EaseInOutCurve)
        self.timeline.valueChanged.connect(self.show_animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(self.duration)
        self.timeline.start()

        self.resize(960, 540)

    def show_animate(self, value):

        self.opacity = value

        self.effect.setOpacity(self.opacity)
        self.widget.setGraphicsEffect(self.effect)
