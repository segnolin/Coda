#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class Background(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 960, 540)
        self.painter = QPainter()
        self.x = 0
        self.y = 0
        self.pixmap = QPixmap()
        self.anime = QVariantAnimation()

    def create_bg(self, background_id, posx, posy):

        self.x = posx
        self.y = posy
        self.anime.stop()

        self.background_id = background_id
        self.pixmap = QPixmap(':/{0}.png'.format(background_id))
        self.pixmap.setDevicePixelRatio(2)

        self.repaint()

    def create_mv_bg(self, background_id, posx, posy, posxf, posyf, duration):

        self.posx = posx
        self.posy = posy
        self.posxf = posxf
        self.posyf = posyf
        self.duration = duration

        self.background_id = background_id
        self.pixmap = QPixmap(':/{0}.png'.format(self.background_id))
        self.pixmap.setDevicePixelRatio(2)

        self.x = posx
        self.y = posy

        self.dx = self.posxf - self.posx
        self.dy = self.posyf - self.posy

        self.anime.stop()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(self.duration)
        self.anime.setStartValue(0.0)
        self.anime.setEndValue(1.0)
        self.anime.valueChanged.connect(self.show_animate)
        self.anime.start()

    def show_animate(self, value):

        self.x = self.posx + self.dx  * value
        self.y = self.posy + self.dy  * value
        self.repaint()

    def paintEvent(self, event):

        transform = QTransform()
        transform.translate(self.x, self.y)

        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.painter.setTransform(transform)
        self.painter.drawPixmap(0, 0, self.pixmap)
        self.painter.end()
