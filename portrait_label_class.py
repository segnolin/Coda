#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class Portrait(QLabel):
    '''this class provide the label of portrait'''

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(0, 0, 960, 540)

    def show_portrait(self, portrait_id, posx, posy, posxf, posyf, width, height):

        self.portrait_id = portrait_id
        self.posx = posx
        self.posy = posy
        self.posxf = posxf
        self.posyf = posyf
        self.width = width
        self.height = height
        self.pixmap = QPixmap(':/{0}.png'.format(portrait_id))
        self.pixmap.setDevicePixelRatio(2)

        self.x = posx
        self.y = posy
        self.pixmap_opacity = 0.0

        self.painter = QPainter()

        self.timeline = QTimeLine()
        self.timeline.setUpdateInterval(1000 / 60)
        self.timeline.setCurveShape(QTimeLine.EaseInOutCurve)
        self.timeline.valueChanged.connect(self.show_animate)
        self.timeline.setDuration(800)
        self.timeline.start()

        self.show()

    def show_animate(self, value):

        self.pixmap_opacity = value
        self.x = self.posx + (self.posxf - self.posx) * value
        self.y = self.posy + (self.posyf - self.posy) * value
        self.repaint()

    def hide_portrait(self, portrait_id):

        self.pixmap_opacity = 1.0

        self.timeline = QTimeLine()
        self.timeline.setUpdateInterval(10)
        self.timeline.setCurveShape(QTimeLine.EaseInOutCurve)
        self.timeline.valueChanged.connect(self.hide_animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(800)
        self.timeline.start()

        self.show()

    def hide_animate(self, value):

        self.pixmap_opacity = 1.0 - value
        self.x = self.posxf + (self.posx - self.posxf) * value
        self.y = self.posyf + (self.posy - self.posyf) * value
        self.repaint()

    def paintEvent(self, event):

        self.painter.begin(self)
        self.painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.painter.translate(self.x, self.y)
        self.painter.setOpacity(self.pixmap_opacity)
        self.painter.drawPixmap(0, 0, self.pixmap)
        self.painter.end()

    def show_end(self):

        self.timeline.setDuration(1)

        self.pixmap_opacity = 1.0
        self.x = self.posxf
        self.y = self.posyf

        self.repaint()
