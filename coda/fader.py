#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Fader(QWidget):
    '''this class provide fade in/out animation effect'''

    def __init__(self, pre_widget, post_widget):
        QWidget.__init__(self, post_widget)

        self.pre_widget = pre_widget
        self.post_widget = post_widget
        self.pixel_ratio = QWindow().devicePixelRatio()

    def fade(self, duration):

        self.pixmap_opacity = 1.0
        self.post_pixmap = QPixmap(2048, 1152)
        self.post_pixmap = self.post_pixmap.scaledToHeight(
                self.post_pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.post_pixmap.setDevicePixelRatio(self.pixel_ratio)
        self.pre_widget.render(self.post_pixmap)

        self.anime = QVariantAnimation()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(duration)
        self.anime.setStartValue(1.0)
        self.anime.setEndValue(0.0)
        self.anime.valueChanged.connect(self._animate)
        self.anime.finished.connect(self.close)
        self.anime.start()

        self.resize(1024, 576)
        self.show()

    def _animate(self, value):

        self.pixmap_opacity = value
        self.update()

    def closeEvent(self, event):

        self.deleteLater()

    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.post_pixmap)
        painter.end()
