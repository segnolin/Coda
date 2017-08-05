#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from coda.image_button import *

class MainWindow(QMainWindow):
    '''this class creates a main window to show the menu'''

    def __init__(self):
        super().__init__()

    def create_main_window_layout(self):

        pixel_ratio = QWindow().devicePixelRatio()

        #set QWidget class
        self.main_window_widget = QWidget()

        #set background picture by QLabel
        main_background_pixmap = QPixmap(':/sys/main_background.png')
        main_background_pixmap = main_background_pixmap.scaledToHeight(
                main_background_pixmap.height() * pixel_ratio / 2,
                Qt.SmoothTransformation)
        main_background_pixmap.setDevicePixelRatio(pixel_ratio)
        self.main_background = QLabel(self.main_window_widget)
        self.main_background.setPixmap(main_background_pixmap)
        self.main_background.setGeometry(0, 0, 1024, 576)

        #create all the buttons
        #create a strat button
        self.main_start_button = ImageButton(
                'main_start', self.main_window_widget)
        self.main_start_button.setGeometry(73, 440, 96, 32)

        #create a load button
        self.main_load_button = ImageButton(
                'main_load', self.main_window_widget)
        self.main_load_button.setGeometry(258, 440, 96, 32)

        #create a extra button
        self.main_extra_button = ImageButton(
                'main_extra', self.main_window_widget)
        self.main_extra_button.setGeometry(443, 440, 96, 32)

        #create a config button
        self.main_config_button = ImageButton(
                'main_config', self.main_window_widget)
        self.main_config_button.setGeometry(628, 440, 96, 32)

        #create a quit button
        self.main_quit_button = ImageButton(
                'main_quit', self.main_window_widget)
        self.main_quit_button.setGeometry(813, 440, 96, 32)
