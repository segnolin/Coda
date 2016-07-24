#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Fader(QWidget):
    '''this class provide fade in/out animation effect'''

    def __init__(self, pre_widget, post_widget):
        QWidget.__init__(self, post_widget)

        self.pre_widget = pre_widget
        self.post_widget = post_widget

    def fade(self, duration):

        self.duration = duration
        self.pixmap_opacity = 1.0
        self.post_pixmap = QPixmap(2048, 1152)
        self.post_pixmap.setDevicePixelRatio(2)
        self.pre_widget.render(self.post_pixmap)

        self.anime = QVariantAnimation()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(self.duration)
        self.anime.setStartValue(1.0)
        self.anime.setEndValue(0.0)
        self.anime.valueChanged.connect(self.animate)
        self.anime.finished.connect(self.close)
        self.anime.start()

        self.resize(1024, 576)
        self.show()

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.post_pixmap)
        painter.end()

    def animate(self, value):

        self.pixmap_opacity = value
        self.repaint()

    def closeEvent(self, event):

        self.deleteLater()
