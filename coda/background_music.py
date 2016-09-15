#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

import sys
import resources.background_music_resources

class BackgroundMusic(QMediaPlayer):

    def __init__(self):
        super().__init__()

        self.playlist = QMediaPlaylist()
        self.anime = QVariantAnimation()
        self.vol_anime = QVariantAnimation()
        self.background_music_id = ''

    def play_music(self, background_music_id):

        self.background_music_id = background_music_id

        self.playlist.clear()
        self.playlist.addMedia(QMediaContent(QUrl('qrc:/bgm/{0}.mp3'.format(self.background_music_id))))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.setPlaylist(self.playlist)
        self.setVolume(80)
        self.play()

    def music_volume(self, volume):

        self.target_volume = volume
        self.current_volume = self.volume()
        self.delta_volume = self.current_volume - self.target_volume

        self.vol_anime.stop()
        self.vol_anime.setEasingCurve(QEasingCurve.OutSine)
        self.vol_anime.setDuration(800)
        self.vol_anime.setStartValue(0.0)
        self.vol_anime.setEndValue(1.0)
        self.vol_anime.valueChanged.connect(self.fade_vol)
        self.vol_anime.start()

    def fade_vol(self, value):

        self.setVolume(self.current_volume - self.delta_volume * value)

    def stop_music(self):

        self.background_music_id = ''

        self.anime.stop()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(1800)
        self.anime.setStartValue(1.0)
        self.anime.setEndValue(0.0)
        self.anime.valueChanged.connect(self.fade)
        self.anime.finished.connect(self.stop)
        self.anime.start()

    def fade(self, value):

        self.setVolume(80 * value)
