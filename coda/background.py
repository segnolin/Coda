#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.background_resources
import resources.event_resources
import resources.scene_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Background(QLabel):
    '''this class provide background effect'''

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 1024, 576)

        self.id = ''
        self.posx = 0
        self.posy = 0
        self.posxf = 0
        self.posyf = 0
        self.duration = 0
        self.x = 0
        self.y = 0
        self.pixmap = QPixmap()
        self.anime = QVariantAnimation()
        self.pixel_ratio = QWindow().devicePixelRatio()

    def create_bg(self, background_id, posx, posy):

        self.id = background_id
        self.x = posx
        self.y = posy
        self.posx = posx
        self.posy = posy
        self.duration = 0

        self.pixmap = QPixmap(':/bg/{0}.png'.format(self.id))
        self.pixmap = self.pixmap.scaledToHeight(
                self.pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.pixmap.setDevicePixelRatio(self.pixel_ratio)

        self.anime.stop()
        self.update()

    def create_mv_bg(
            self, background_id,
            posx, posy, posxf, posyf, duration):

        self.id = background_id
        self.posx = posx
        self.posy = posy
        self.posxf = posxf
        self.posyf = posyf
        self.duration = duration
        self.dx = self.posxf - self.posx
        self.dy = self.posyf - self.posy

        self.pixmap = QPixmap(':/bg/{0}.png'.format(self.id))
        self.pixmap = self.pixmap.scaledToHeight(
                self.pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.pixmap.setDevicePixelRatio(self.pixel_ratio)

        self.anime.stop()
        if self.duration >= 10000:
            self.anime.setEasingCurve(QEasingCurve.OutQuad)
        else:
            self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(self.duration)
        self.anime.setStartValue(0.0)
        self.anime.setEndValue(1.0)
        self.anime.valueChanged.connect(self._show_animate)
        self.anime.start()

    def _show_animate(self, value):

        self.x = self.posx + self.dx  * value
        self.y = self.posy + self.dy  * value
        self.update()

    def paintEvent(self, event):

        transform = QTransform()
        transform.translate(self.x, self.y)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setTransform(transform)
        painter.drawPixmap(0, 0, self.pixmap)
        painter.end()
