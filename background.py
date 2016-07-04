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
        self.timeline = QTimeLine()

    def create_bg(self, background_id):

        self.x = 0
        self.y = 0
        self.timeline.stop()

        self.background_id = background_id
        self.pixmap = QPixmap(':/{0}.png'.format(background_id))
        self.pixmap.setDevicePixelRatio(2)

        self.setPixmap(self.pixmap)

    def create_mv_bg(self, background_id, posx, posy, posxf, posyf, duration):

        self.background_id = background_id
        self.posx = posx
        self.posy = posy
        self.posxf = posxf
        self.posyf = posyf
        self.duration = duration
        self.pixmap = QPixmap(':/{0}.png'.format(self.background_id))
        self.pixmap.setDevicePixelRatio(2)

        self.x = posx
        self.y = posy

        self.timeline.stop()
        self.timeline.setUpdateInterval(1000 / 60)
        self.timeline.setCurveShape(QTimeLine.EaseOutCurve)
        self.timeline.valueChanged.connect(self.show_animate)
        self.timeline.setDuration(self.duration)
        self.timeline.start()

    def show_animate(self, value):

        self.x = self.posx + (self.posxf - self.posx) * value
        self.y = self.posy + (self.posyf - self.posy) * value
        self.repaint()

    def paintEvent(self, event):

        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.painter.translate(self.x, self.y)
        self.painter.drawPixmap(0, 0, self.pixmap)
        self.painter.end()
