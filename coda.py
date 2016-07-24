#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from intro_window import *
from main_window import *
from game_engine import *
from load import *
from image_button import *
from fader import *

import sys

class Coda(QMainWindow):
    '''this class init the main window and manage connections'''

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #set initial game argument
        self.script = 'a0000'
        self.game_engine_id = 0
        self.status = 'main'

        #self.setWindowTitle('Coda')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(1024, 576)

        #create intro window layout
        self.intro_window = IntroWindow()
        self.intro_window.create_intro_window_layout()

        #create main window layout
        self.main_window = MainWindow()
        self.main_window.create_main_window_layout()

        #set multiple stack layout
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(self.intro_window.intro_window_widget)
        self.stacked_layout.addWidget(self.main_window.main_window_widget)

        #set stack to show
        self.stacked_layout.setCurrentWidget(self.intro_window.intro_window_widget)
        QTimer.singleShot(3000, self.go_to_main)

        #set the central widget to display the layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

        #connection
        self.main_window.main_start_button.clicked.connect(self.start)
        self.main_window.main_load_button.clicked.connect(self.load)
        self.main_window.main_extra_button.clicked.connect(self.extra)
        self.main_window.main_config_button.clicked.connect(self.config)
        self.main_window.main_exit_button.clicked.connect(self.exit)

    def go_to_main(self):

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(), self.main_window.main_window_widget)
        self.fader.fade(800)

        self.stacked_layout.setCurrentWidget(self.main_window.main_window_widget)

    def load_game_engine(self):

        #test
        self.script = 'a0003'
        self.game_engine_id = 0
        self.start()

    def back_to_main(self):

        print('back to main')

        self.script = 'a0000'
        self.game_engine_id = 0
        self.status = 'main'

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(), self.main_window.main_window_widget)
        self.fader.fade(350)

        self.stacked_layout.setCurrentWidget(self.main_window.main_window_widget)

    def back_to_game_engine(self):

        print('back to game engine')

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(), self.game_engine.game_engine_widget)
        self.fader.fade(350)

        self.stacked_layout.setCurrentWidget(self.game_engine.game_engine_widget)

    def start(self):

        print('start')

        self.status = 'game_engine'

        self.game_engine = GameEngine()
        self.game_engine.create_game_engine_layout(self.script, self.game_engine_id)

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(), self.game_engine.game_engine_widget)
        self.fader.fade(1500)

        self.stacked_layout.addWidget(self.game_engine.game_engine_widget)
        self.stacked_layout.setCurrentWidget(self.game_engine.game_engine_widget)

        #connection
        self.game_engine.load_button.clicked.connect(self.load)
        self.game_engine.title_button.clicked.connect(self.back_to_main)
        self.game_engine.exit_button.clicked.connect(self.exit)

    def load(self):

        print('load')

        self.load_game = Load()
        self.load_game.create_load_layout(self.status)

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(), self.load_game.load_widget)
        self.fader.fade(350)

        self.stacked_layout.addWidget(self.load_game.load_widget)
        self.stacked_layout.setCurrentWidget(self.load_game.load_widget)

        #connection
        self.load_game.main_start_button.clicked.connect(self.load_game_engine)
        if self.status == 'main':
            self.load_game.main_exit_button.clicked.connect(self.back_to_main)
        elif self.status == 'game_engine':
            self.load_game.main_exit_button.clicked.connect(self.back_to_game_engine)

    def extra(self):

        print('extra')

    def config(self):

        print('config')

    def exit(self):

        print('exit')
        self.close()

    def closeEvent(self, event):

        print('close')
