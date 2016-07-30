#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

import sys
import resources.voice_resources

class Voice(QMediaPlayer):

    def __init__(self):
        super().__init__()

    def play_voice(self, voice_id):

        self.voice_id = voice_id

        self.setMedia(QMediaContent(QUrl('qrc:/vc/{0}.mp3'.format(self.voice_id))))
        self.play()
