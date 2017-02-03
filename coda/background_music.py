#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.background_music_resources

from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

class BackgroundMusic(QMediaPlayer):
    '''this class provide background music'''

    def __init__(self):
        super().__init__()

        self.id = ''
        self.playlist = QMediaPlaylist()
        self.anime = QVariantAnimation()
        self.vol_anime = QVariantAnimation()

    def play_music(self, background_music_id):

        self.id = background_music_id

        self.playlist.clear()
        self.playlist.addMedia(
                QMediaContent(QUrl(
                'qrc:/bgm/{0}.mp3'.format(
                self.id))))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.setPlaylist(self.playlist)
        self.setVolume(0)
        self.play()
        self.music_volume(80)

    def music_volume(self, volume):

        self.current_volume = self.volume()
        self.delta_volume = self.current_volume - volume

        self.vol_anime.stop()
        self.vol_anime.setEasingCurve(QEasingCurve.OutSine)
        self.vol_anime.setDuration(800)
        self.vol_anime.setStartValue(0.0)
        self.vol_anime.setEndValue(1.0)
        self.vol_anime.valueChanged.connect(self._fade_vol)
        self.vol_anime.start()

    def _fade_vol(self, value):

        self.setVolume(self.current_volume - self.delta_volume * value)

    def stop_music(self):

        self.anime.stop()
        self.anime.setEasingCurve(QEasingCurve.OutSine)
        self.anime.setDuration(1800)
        self.anime.setStartValue(1.0)
        self.anime.setEndValue(0.0)
        self.anime.valueChanged.connect(self._fade_out)
        self.anime.finished.connect(self.stop)
        self.anime.start()

    def _fade_out(self, value):

        self.setVolume(80 * value)
