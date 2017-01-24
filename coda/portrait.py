#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.portrait_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Portrait(QLabel):
    '''this class provide the label of portrait'''

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 1024, 576)

        self.portrait_id = ''
        self.pixel_ratio = QWindow().devicePixelRatio()
        self.x = 0
        self.y = 0
        self.pixmap = QPixmap()
        self.sh_anime = QVariantAnimation()
        self.hi_anime = QVariantAnimation()
        self.mv_anime = QVariantAnimation()
        self.opacity = 0.0

    def create_pt(self, portrait_id, posx, posy):

        self.portrait_id = portrait_id
        self.posx = posx
        self.posy = posy
        self.x = self.posx
        self.y = self.posy
        self.dx = 0
        self.dy = 0

        self.pixmap = QPixmap(':/pt/{0}.png'.format(self.portrait_id))
        self.pixmap = self.pixmap.scaledToHeight(
                self.pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.pixmap.setDevicePixelRatio(self.pixel_ratio)

        self.sh_anime.stop()
        self.sh_anime.setDuration(300)
        self.sh_anime.setEasingCurve(QEasingCurve.OutSine)
        self.sh_anime.setStartValue(0.0)
        self.sh_anime.setEndValue(1.0)
        self.sh_anime.valueChanged.connect(self.show_animate)
        self.sh_anime.start()

    def create_mv_pt(self, portrait_id, posx, posy, posxf, posyf, duration):

        self.portrait_id = portrait_id
        self.posx = posx
        self.posy = posy
        self.posxf = posxf
        self.posyf = posyf
        self.duration = duration

        self.pixmap = QPixmap(':/pt/{0}.png'.format(self.portrait_id))
        self.pixmap = self.pixmap.scaledToHeight(
                self.pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.pixmap.setDevicePixelRatio(self.pixel_ratio)

        self.x = posx
        self.y = posy
        self.dx = self.posxf - self.posx
        self.dy = self.posyf - self.posy

        self.sh_anime.stop()
        self.sh_anime.setDuration(self.duration)
        self.sh_anime.setEasingCurve(QEasingCurve.OutSine)
        self.sh_anime.setStartValue(0.0)
        self.sh_anime.setEndValue(1.0)
        self.sh_anime.valueChanged.connect(self.show_animate)
        self.sh_anime.start()

    def show_animate(self, value):

        self.x = self.posx + self.dx * value
        self.y = self.posy + self.dy * value
        self.opacity = value
        self.update()

    def move_pt(self, posxf, posyf, duration):

        self.posx = self.x
        self.posy = self.y
        self.posxf = posxf
        self.posyf = posyf
        self.duration = duration
        self.dx = self.posxf - self.posx
        self.dy = self.posyf - self.posy

        self.mv_anime.stop()
        self.mv_anime.setDuration(self.duration)
        self.mv_anime.setEasingCurve(QEasingCurve.OutSine)
        self.mv_anime.setStartValue(0.0)
        self.mv_anime.setEndValue(1.0)
        self.mv_anime.valueChanged.connect(self.move_animate)
        self.mv_anime.start()

    def move_animate(self, value):

        self.x = self.posx + self.dx * value
        self.y = self.posy + self.dy * value
        self.update()

    def delete_pt(self):

        self.dx = 0
        self.dy = 0

        self.hi_anime.stop()
        self.hi_anime.setDuration(300)
        self.hi_anime.setEasingCurve(QEasingCurve.OutSine)
        self.hi_anime.setStartValue(0.0)
        self.hi_anime.setEndValue(1.0)
        self.hi_anime.valueChanged.connect(self.hide_animate)
        self.hi_anime.start()

    def delete_mv_pt(self, posxf, posyf, duration):

        self.posx = self.x
        self.posy = self.y
        self.posxf = posxf
        self.posyf = posyf
        self.duration = duration
        self.dx = self.posxf - self.posx
        self.dy = self.posyf - self.posy

        self.hi_anime.stop()
        self.hi_anime.setDuration(self.duration)
        self.hi_anime.setEasingCurve(QEasingCurve.OutSine)
        self.hi_anime.setStartValue(0.0)
        self.hi_anime.setEndValue(1.0)
        self.hi_anime.valueChanged.connect(self.hide_animate)
        self.hi_anime.start()

    def hide_animate(self, value):

        self.x = self.posx + self.dx *  value
        self.y = self.posy + self.dy *  value
        self.opacity = 1 - value
        self.update()

    def paintEvent(self, event):

        transform = QTransform()
        transform.translate(self.x, self.y)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setTransform(transform)
        painter.setOpacity(self.opacity)
        painter.drawPixmap(0, 0, self.pixmap)
        painter.end()
