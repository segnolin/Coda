#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtGui import *

def set_font(font_type, font_size):

    font = QFont()
    font.setFamily(QFontDatabase.applicationFontFamilies(font_type)[0])
    font.setStyleStrategy(QFont.PreferQuality)
    font.setHintingPreference(QFont.PreferFullHinting)
    font.setPixelSize(font_size)
    if font_type:
        font.setWeight(QFont.Medium)
    else:
        font.setWeight(QFont.Normal)

    return font
