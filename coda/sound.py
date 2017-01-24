#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.sound_resources

from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

class Sound(QMediaPlayer):

    def __init__(self):
        super().__init__()

        self.sound_id = ''
        self.playlist = QMediaPlaylist()
        self.anime = QVariantAnimation()
        self.end_anime = QVariantAnimation()

    def play_sound(self, sound_id, playback_mode, fade_mode):

        self.sound_id = sound_id

        if playback_mode == None:
            self.playback_mode = QMediaPlaylist.CurrentItemOnce
        elif playback_mode:
            self.playback_mode = QMediaPlaylist.Loop

            if fade_mode:
                self.setVolume(0)
                self.anime.stop()
                self.anime.setEasingCurve(QEasingCurve.OutSine)
                self.anime.setDuration(3000)
                self.anime.setStartValue(0.0)
                self.anime.setEndValue(1.0)
                self.anime.valueChanged.connect(self._start_fade)
                self.anime.start()

        self.playlist.clear()
        self.playlist.addMedia(
                QMediaContent(QUrl(
                'qrc:/sd/{0}.mp3'.format(
                self.sound_id))))
        self.playlist.setPlaybackMode(self.playback_mode)

        self.setPlaylist(self.playlist)
        self.setVolume(60)
        self.play()

    def _start_fade(self, value):

        self.setVolume(60 * value)

    def stop_sound(self, fade_mode):

        if fade_mode:
            self.end_anime.stop()
            self.end_anime.setEasingCurve(QEasingCurve.OutSine)
            self.end_anime.setDuration(1800)
            self.end_anime.setStartValue(1.0)
            self.end_anime.setEndValue(0.0)
            self.end_anime.valueChanged.connect(self._end_fade)
            self.end_anime.finished.connect(self.stop)
            self.end_anime.start()
        else:
            self.stop()

    def _end_fade(self, value):

        self.setVolume(60 * value)
