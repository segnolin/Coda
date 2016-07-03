#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button import *
from fader import *
from fader_widget import *
from letter_print import *
from portrait import *
from parser import *

import sys
import resources

class GameEngine(QMainWindow):
    '''this class creates game engine layout and functions'''

    def __init__(self):
        super().__init__()

    def create_game_engine_layout(self, game_engine_id):

        self.script = ':/totono.xml'
        self.game_engine_id = game_engine_id
        print(self.game_engine_id)

        #set game status
        self.init_status = True
        self.portrait_status = 'not shown'

        #set QWidget class
        self.game_engine_widget = QWidget()
        self.basic_widget = QWidget(self.game_engine_widget)
        self.text_box_widget = QWidget(self.game_engine_widget)
        self.log_widget = QWidget(self.game_engine_widget)
        self.menu_widget = QWidget(self.game_engine_widget)

        #create basic layout
        #create background label
        self.background_pixmap = QPixmap(':/bg_0000.png')
        self.background_pixmap.setDevicePixelRatio(2)
        self.background = QLabel(self.basic_widget)
        self.background.setPixmap(self.background_pixmap)
        self.background.setGeometry(0, 0, 960, 540)

        #create portrait label
        self.portrait = Portrait(self.basic_widget)

        #create disable hide label to show all widget
        self.disable_hide_label = QLabel(self.basic_widget)
        self.disable_hide_label.setGeometry(0, 0, 960, 540)
        self.disable_hide_label.hide()

        #create text box layout
        #create text background label
        self.text_background_pixmap = QPixmap(':/text_background.png')
        self.text_background_pixmap.setDevicePixelRatio(2)
        self.text_background_label = QLabel(self.text_box_widget)
        self.text_background_label.setPixmap(self.text_background_pixmap)
        self.text_background_label.setGeometry(0, 340, 960, 200)

        #set the text character label
        self.character = 'AOI'
        self.text_font = QFont('Noto Sans CJK TC Regular', 16, QFont.Bold)
        self.text_character_label = QLabel(self.text_box_widget)
        self.text_character_label.setFont(self.text_font)
        self.text_character_label.setAlignment(Qt.AlignLeft)
        self.text_character_label.setGeometry(90, 390, 695, 30)
        self.text_character_label.setStyleSheet('QLabel {color: rgba(255, 255, 255, 100%)}')

        #set the text box label
        self.text = 'Test Text\n測試文本\nテストテキスト'
        self.text_font = QFont('Noto Sans CJK TC Regular', 14, QFont.Bold)
        self.text_box_label = LetterPrint(self.text_box_widget)
        self.text_box_label.setFont(self.text_font)
        self.text_box_label.setAlignment(Qt.AlignLeft)
        self.text_box_label.setGeometry(100, 430, 685, 100)
        self.text_box_label.setStyleSheet('QLabel {color: rgba(255, 255, 255, 100%)}')
        self.text_box_label.setWordWrap(True)

        #create transparent label to add game engine id(next)
        self.next_label = QLabel(self.text_box_widget)
        self.next_label.setGeometry(0, 0, 960, 540)

        #create a auto button
        self.auto_button = ImageButton('auto', self.text_box_widget)
        self.auto_button.setGeometry(810, 435, 35, 35)

        #create a skip button
        self.skip_button = ImageButton('skip', self.text_box_widget)
        self.skip_button.setGeometry(855, 435, 35, 35)

        #create a log button
        self.log_button = ImageButton('log', self.text_box_widget)
        self.log_button.setGeometry(900, 435, 35, 35)

        #create a save button
        self.save_button = ImageButton('save', self.text_box_widget)
        self.save_button.setGeometry(810, 480, 35, 35)

        #create a load button
        self.load_button = ImageButton('load', self.text_box_widget)
        self.load_button.setGeometry(855, 480, 35, 35)

        #create a menu button
        self.menu_button = ImageButton('menu', self.text_box_widget)
        self.menu_button.setGeometry(900, 480, 35, 35)

        #create a hide button
        self.hide_button = ImageButton('hide', self.text_box_widget)
        self.hide_button.setGeometry(760, 400, 25, 25)

        #create menu layout
        #create menu background
        self.menu_background_pixmap = QPixmap(':/menu_background.png')
        self.menu_background_pixmap.setDevicePixelRatio(2)
        self.menu_background_label = QLabel(self.menu_widget)
        self.menu_background_label.setPixmap(self.menu_background_pixmap)
        self.menu_background_label.setGeometry(0, 0, 960, 540)

        #create back button
        self.back_button = ImageButton('menu_back', self.menu_widget)
        self.back_button.setGeometry(400, 64, 160, 55)

        #create title button
        self.title_button = ImageButton('menu_title', self.menu_widget)
        self.title_button.setGeometry(400, 183, 160, 55)

        #create config button
        self.config_button = ImageButton('menu_config', self.menu_widget)
        self.config_button.setGeometry(400, 302, 160, 55)

        #create exit button
        self.exit_button = ImageButton('menu_exit', self.menu_widget)
        self.exit_button.setGeometry(400, 421, 160, 55)

        #hide all widget
        self.basic_widget.hide()
        self.text_box_widget.hide()
        self.menu_widget.hide()

        #connection
        self.back_button.clicked.connect(self.hide_menu)
        self.menu_button.clicked.connect(self.show_menu)
        self.hide_button.clicked.connect(self.hide_widget)
        self.disable_hide_label.mousePressEvent = self.show_widget
        self.next_label.mousePressEvent = self.update

        #set parser
        self.parser = Parser()
        self.init_parser()

    ################################################## MAIN PROGRAM START ##################################################

    def init_parser(self):

        print('init_parser')

        self.parser.parse(self.script, self.game_engine_id)

        self.bgm_id = self.parser.bgm_id

        self.sd_id = self.parser.sd_id

        self.eff_id = self.parser.eff_id
        self.eff_du = self.parser.eff_du

        self.bg_id = self.parser.bg_id
        self.bg_x = self.parser.bg_x
        self.bg_y = self.parser.bg_y
        self.bg_xf = self.parser.bg_xf
        self.bg_yf = self.parser.bg_yf
        self.bg_du = self.parser.bg_du

        self.pt_id = self.parser.pt_id
        self.pt_x = self.parser.pt_x
        self.pt_y = self.parser.pt_y
        self.pt_xf = self.parser.pt_xf
        self.pt_yf = self.parser.pt_yf

        self.tb_sh = self.parser.tb_sh
        self.tb_td = self.parser.tb_td
        self.tb_vc = self.parser.tb_vc
        self.tb_char = self.parser.tb_char
        self.tb_txt = self.parser.tb_txt
        self.tb_hi = self.parser.tb_hi

        self.init_background_music()

    def init_background_music(self):

        print('init_background_music')

        self.portrait_status = 'not shown'

        self.init_sound()

    def init_sound(self):

        print('init_sound')

        self.init_effect()

    def init_effect(self):

        print('init_effect')

        self.init_background()

    def init_background(self):

        print('init_background')

        if self.init_status:
            self.basic_widget.show()

        self.init_portrait()

    def init_portrait(self):

        print('init_portrait')

        self.portrait.show_portrait('aoi_normal', 400, 40, 500, 40)
        self.portrait.timeline.finished.connect(self.init_text_box)

    def init_text_box(self):

        print('init_text_box')

        self.portrait_status = 'shown'
        self.init_voice()

    def init_voice(self):

        print('init_voice')

        self.init_text()

    def init_text(self):

        print('init_text')

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(250)

        if self.init_status:
            self.text_box_widget.show()
            self.init_status = False

        self.text_character_label.setText(self.character)
        self.text_box_label.set_text(self.text)

    def update(self, event):

        if self.portrait_status == 'not shown':

            self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
            self.fader.fade(250)
            self.portrait.show_end()

        elif self.portrait_status == 'shown':

            #check if this text is already shown after label was pressed
            if self.text_box_label.index < len(self.text):
                self.text_box_label.setText(self.text)
                self.text_box_label.index = len(self.text)

            else:
                self.game_engine_id += 1
                print('update')
                print(self.game_engine_id)

                self.set_background_music()

        elif self.portrait_status == 'not closed':

            self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
            self.fader.fade(250)
            self.set_text_box()

    def set_background_music(self):

        print('set_background_music')

        self.portrait_status = 'not closed'

        self.set_sound()

    def set_sound(self):

        print('set_sound')

        self.set_voice()

    def set_voice(self):

        print('set_voice')

        self.set_text()

    def set_text(self):

        print('set_text')

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(250)
        self.fader.timeline.finished.connect(self.set_portrait)

        self.text = 'Hi! This is line {0}'.format(self.game_engine_id)

        self.text_character_label.clear()
        self.text_box_label.clear()

    def set_portrait(self):

        print('set_portrait')

        self.portrait.hide_portrait('aoi_normal')
        self.portrait.timeline.finished.connect(self.set_text_box)

    def set_text_box(self):

        print('set_text_box')

        self.init_parser()

    ################################################## MAIN PROGRAM END ##################################################

    def hide_menu(self):

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(250)
        self.menu_widget.hide()
        self.text_box_widget.show()

    def show_menu(self):

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(250)
        self.menu_widget.show()
        self.text_box_widget.hide()

    def hide_widget(self):

        self.hide_button.setEnabled(False)
        self.fader_widget = FaderWidget(self.text_box_widget)
        self.fader_widget.hide(250)
        self.fader_widget.timeline.finished.connect(self.finsh_hide)

    def finsh_hide(self):

        self.text_box_widget.hide()
        self.disable_hide_label.show()

    def show_widget(self, event):

        self.text_box_widget.show()
        self.fader_widget = FaderWidget(self.text_box_widget)
        self.fader_widget.show(250)
        self.fader_widget.timeline.finished.connect(self.finish_show)

    def finish_show(self):

        self.disable_hide_label.hide()
        self.hide_button.setEnabled(True)
