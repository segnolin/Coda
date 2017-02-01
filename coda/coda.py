#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from coda.intro_window import *
from coda.main_window import *
from coda.game_engine import *
from coda.save import *
from coda.image_button import *
from coda.fader import *

class Coda(QMainWindow):
    '''this class init the main window and manage connections'''

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #set initial game argument
        self.script = 'scr_a0000'
        self.game_engine_id = 0
        self.status = 'main'

        self.setWindowTitle('Coda')
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

        #change stack to main window
        QTimer.singleShot(3500, self._go_to_main)

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

        #set game engine
        self.game_engine = GameEngine()
        self.game_engine.create_game_engine_layout()
        self.stacked_layout.addWidget(self.game_engine.game_engine_widget)

        #game engine connection
        self.game_engine.save_button.clicked.connect(self.save)
        self.game_engine.load_button.clicked.connect(self.load)
        self.game_engine.title_button.clicked.connect(self._back_to_main)
        self.game_engine.exit_button.clicked.connect(self.exit)

        #set save layout
        self.save_game = Save()
        self.save_game.create_save_layout()
        self.stacked_layout.addWidget(self.save_game.save_widget)

        #save connection
        self.save_game.save_back_button.clicked.connect(self._save_back)
        for i in range(6):
            for j in range(6):
                self.save_game.page[i].label[j].clicked.connect(self._action)

    def start(self):

        print('start')

        self.status = 'game_engine'

        self.game_engine.start_game(self.script, self.game_engine_id)

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(),
                self.game_engine.game_engine_widget)
        self.fader.fade(1500)

        self.stacked_layout.setCurrentWidget(self.game_engine.game_engine_widget)

    def save(self):

        print('save')

        self.save_game.add_save(self.game_engine.save_data,
                self.game_engine.thumbnail)

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(),
                self.save_game.save_widget)
        self.fader.fade(350)

        self.stacked_layout.setCurrentWidget(self.save_game.save_widget)
        #print(self.stacked_layout.currentIndex())

    def load(self):

        print('load')

        self.save_game.load()

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(),
                self.save_game.save_widget)
        self.fader.fade(350)

        self.stacked_layout.setCurrentWidget(self.save_game.save_widget)
        #print(self.stacked_layout.currentIndex())

    def extra(self):

        print('extra')

    def config(self):

        print('config')

    def exit(self):

        print('exit')
        self.close()

    def _go_to_main(self):

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(),
                self.main_window.main_window_widget)
        self.fader.fade(600)

        self.stacked_layout.setCurrentWidget(self.main_window.main_window_widget)

    def _save_back(self):

        if self.status == 'main':
            self._back_to_main()
        elif self.status == 'game_engine':
            self._back_to_game_engine()

    def _load_game_engine(self):

        #test
        self.script = 'scr_a0003'
        self.game_engine_id = 0
        self.game_engine.menu_widget.hide()

        self.game_engine.text_box_widget.hide()
        self.game_engine.select_widget.hide()
        self.game_engine.disable_hide_label.hide()
        self.game_engine.effect.hide()

        self.start()

    def _back_to_main(self):

        print('back to main')

        self.script = 'scr_a0000'
        self.game_engine_id = 0
        self.status = 'main'

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(),
                self.main_window.main_window_widget)
        self.fader.fade(350)

        self.stacked_layout.setCurrentWidget(self.main_window.main_window_widget)
        self.game_engine.menu_widget.hide()
        self.game_engine.text_box_widget.hide()
        self.game_engine.select_widget.hide()
        self.game_engine.disable_hide_label.hide()
        self.game_engine.effect.hide()

    def _back_to_game_engine(self):

        print('back to game engine')

        #fade effect
        self.fader = Fader(self.stacked_layout.currentWidget(),
                self.game_engine.game_engine_widget)
        self.fader.fade(350)

        self.stacked_layout.setCurrentWidget(self.game_engine.game_engine_widget)
        #print(self.stacked_layout.currentIndex())

    def _action(self):

        save_id = self.sender().id
        print('coda {0}'.format(save_id))

    def closeEvent(self, event):

        print('close')
