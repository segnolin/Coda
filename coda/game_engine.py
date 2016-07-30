#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from coda.image_button import *
from coda.select_button import *
from coda.fader import *
from coda.fader_widget import *
from coda.letter_print import *
from coda.effect import *
from coda.mask import *
from coda.background import *
from coda.background_music import *
from coda.portrait import *
from coda.script_parser import *
from coda.voice import *

import sys
import resources.system_resources

class GameEngine(QMainWindow):
    '''this class creates game engine layout and functions'''

    def __init__(self):
        super().__init__()

    def create_game_engine_layout(self, script, game_engine_id):

        self.script = script
        self.game_engine_id = game_engine_id
        print(self.game_engine_id)

        #set game status
        self.init_status = True
        self.effect_status = False

        #set QWidget class
        self.game_engine_widget = QOpenGLWidget()
        self.base_widget = QWidget(self.game_engine_widget)
        self.portrait_widget = QWidget(self.game_engine_widget)
        self.basic_widget = QWidget(self.game_engine_widget)
        self.select_widget = QWidget(self.game_engine_widget)
        self.text_box_widget = QWidget(self.game_engine_widget)
        self.menu_widget = QWidget(self.game_engine_widget)

        #create base layout
        #create background label
        self.background = Background(self.base_widget)

        #creaate portrait layout
        #create portrait
        self.portrait = {}
        for i in range(5):
            self.portrait[i] = Portrait(self.portrait_widget)

        #create basic layout
        #create mask label
        self.mask_label = Mask(self.basic_widget)

        #create disable hide label to show all widget
        self.disable_hide_label = QLabel(self.basic_widget)
        self.disable_hide_label.setGeometry(0, 0, 1024, 576)

        #create effect label
        self.effect = Effect(self.basic_widget)

        #create select layout
        #create select label
        self.select_background_pixmap = QPixmap(':/sys/select_background.png')
        self.select_background_pixmap = self.select_background_pixmap.scaledToHeight((self.select_background_pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.select_background_pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.select_background_label = QLabel(self.select_widget)
        self.select_background_label.setPixmap(self.select_background_pixmap)
        self.select_background_label.setGeometry(0, 0, 1024, 576)

        #create selection button
        self.selection_button = {}

        #create text box layout
        #create text background label
        self.text_background_pixmap = QPixmap(':/sys/text_background.png')
        self.text_background_pixmap = self.text_background_pixmap.scaledToHeight((self.text_background_pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.text_background_pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.text_background_label = QLabel(self.text_box_widget)
        self.text_background_label.setPixmap(self.text_background_pixmap)
        self.text_background_label.setGeometry(0, 396, 1024, 180)

        #set the text character label
        self.text_character_label = QLabel(self.text_box_widget)
        self.text_character_label.setAlignment(Qt.AlignLeft)
        self.text_character_label.setGeometry(150, 446, 660, 30)
        self.text_character_label.setStyleSheet('QLabel {color: rgba(0, 0, 0, 100%)}')
        self.text_character_label.setStyleSheet('QLabel {font-family: Times New Roman; font-size: 20px; font-weight: Bold; color: rgba(0, 0, 0, 100%)}')

        #set the text box label
        self.text_box_label = LetterPrint(self.text_box_widget)
        self.text_box_label.setAlignment(Qt.AlignLeft)
        self.text_box_label.setGeometry(160, 486, 650, 75)
        self.text_box_label.setStyleSheet('QLabel {font-family: Times New Roman; font-size: 18px; color: rgba(0, 0, 0, 100%)}')
        self.text_box_label.setWordWrap(True)

        #create transparent label to add game engine id(next)
        self.next_label = QLabel(self.text_box_widget)
        self.next_label.setGeometry(0, 0, 1024, 576)

        #create a auto button
        self.auto_button = ImageButton('auto', self.text_box_widget)
        self.auto_button.setGeometry(874, 486, 35, 35)

        #create a skip button
        self.skip_button = ImageButton('skip', self.text_box_widget)
        self.skip_button.setGeometry(919, 486, 35, 35)

        #create a log button
        self.log_button = ImageButton('log', self.text_box_widget)
        self.log_button.setGeometry(964, 486, 35, 35)

        #create a save button
        self.save_button = ImageButton('save', self.text_box_widget)
        self.save_button.setGeometry(874, 531, 35, 35)

        #create a load button
        self.load_button = ImageButton('load', self.text_box_widget)
        self.load_button.setGeometry(919, 531, 35, 35)

        #create a menu button
        self.menu_button = ImageButton('menu', self.text_box_widget)
        self.menu_button.setGeometry(964, 531, 35, 35)

        #create a hide button
        self.hide_button = ImageButton('hide', self.text_box_widget)
        self.hide_button.setGeometry(824, 461, 25, 25)

        #create menu layout
        #create menu background
        self.menu_background_pixmap = QPixmap(':/sys/menu_background.png')
        self.menu_background_pixmap = self.menu_background_pixmap.scaledToHeight((self.menu_background_pixmap.height() * QWindow().devicePixelRatio()) / 2, Qt.SmoothTransformation)
        self.menu_background_pixmap.setDevicePixelRatio(QWindow().devicePixelRatio())
        self.menu_background_label = QLabel(self.menu_widget)
        self.menu_background_label.setPixmap(self.menu_background_pixmap)
        self.menu_background_label.setGeometry(0, 0, 1024, 576)

        #create back button
        self.back_button = ImageButton('menu_back', self.menu_widget)
        self.back_button.setGeometry(60, 275, 96, 32)

        #create title button
        self.title_button = ImageButton('menu_title', self.menu_widget)
        self.title_button.setGeometry(290, 275, 96, 32)

        #create config button
        self.config_button = ImageButton('menu_config', self.menu_widget)
        self.config_button.setGeometry(520, 275, 96, 32)

        #create exit button
        self.exit_button = ImageButton('menu_quit', self.menu_widget)
        self.exit_button.setGeometry(750, 275, 96, 32)

        #hide widget
        self.menu_widget.hide()
        self.text_box_widget.hide()
        self.select_widget.hide()
        self.disable_hide_label.hide()
        self.effect.hide()

        #connection
        self.back_button.clicked.connect(self.hide_menu)
        self.menu_button.clicked.connect(self.show_menu)
        self.hide_button.clicked.connect(self.hide_widget)
        self.disable_hide_label.mousePressEvent = self.show_widget
        self.next_label.mousePressEvent = self.update_engine

        #set media
        self.voice = Voice()
        self.background_music = {}
        for i in range(2):
            self.background_music[i] = BackgroundMusic()

        #set parser
        self.parser = Parser()
        self.init_parser()

    ################################################## MAIN PROGRAM START ##################################################

    def init_parser(self):

        print('init_parser')

        self.parser.parse(self.script, self.game_engine_id)

        self.bgm_pos = self.parser.bgm_pos
        self.bgm_id = self.parser.bgm_id
        self.bgm_md = self.parser.bgm_md
        self.bgm_vol = self.parser.bgm_vol
        self.bgm_num = self.parser.bgm_num

        self.sd_id = self.parser.sd_id

        self.eff_id = self.parser.eff_id
        self.eff_du = self.parser.eff_du

        self.mk_id = self.parser.mk_id
        self.mk_md = self.parser.mk_md

        self.bg_id = self.parser.bg_id
        self.bg_x = self.parser.bg_x
        self.bg_y = self.parser.bg_y
        self.bg_xf = self.parser.bg_xf
        self.bg_yf = self.parser.bg_yf
        self.bg_du = self.parser.bg_du

        self.pt_pos = self.parser.pt_pos
        self.pt_id = self.parser.pt_id
        self.pt_md = self.parser.pt_md
        self.pt_x = self.parser.pt_x
        self.pt_y = self.parser.pt_y
        self.pt_xf = self.parser.pt_xf
        self.pt_yf = self.parser.pt_yf
        self.pt_du = self.parser.pt_du
        self.pt_num = self.parser.pt_num

        self.tb_sh = self.parser.tb_sh
        self.tb_td = self.parser.tb_td
        self.tb_vc = self.parser.tb_vc
        self.tb_char = self.parser.tb_char
        self.tb_txt = self.parser.tb_txt
        self.tb_hi = self.parser.tb_hi

        self.sl_txt = self.parser.sl_txt
        self.sl_sc = self.parser.sl_sc
        self.sl_num = self.parser.sl_num

        self.sys_sc = self.parser.sys_sc

        if self.sys_sc != '':
            self.script = self.sys_sc
            self.game_engine_id = -1
        if int(self.sl_num) != 0:
            self.selection()
        else:
            if self.init_status:
                self.eff_id = 'black_fade'
                self.eff_du = '3000'
                self.tb_sh = True
                if self.tb_td == '':
                    self.tb_td = 1000
                self.pre_process()
            self.init_background_music()

    def init_background_music(self):

        print('init_background_music')

        if int(self.bgm_num) != 0:
            self.bgm_loop()

        self.init_sound()

    def init_sound(self):

        print('init_sound')

        self.init_effect()

    def init_effect(self):

        print('init_effect')

        if self.eff_id != '':

            self.background.anime.stop()
            self.next_label.hide()

            if not self.init_status:
                self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
                self.fader.fade(800)

            self.effect.show()
            self.effect.create(self.eff_id)
            QTimer.singleShot(int(self.eff_du), self.hide_effect)

        else:
            self.effect_status = False
            self.init_mask()
        
        self.init_status = False

    def init_mask(self):

        print('init_mask')

        if self.mk_md == 'new':
            self.mask_label.set_mask(self.mk_id)
        elif self.mk_md == 'del':
            self.mask_label.set_delete()

        self.init_background()

    def init_background(self):

        print('init_background')

        if self.bg_id != '':

            if not self.effect_status:
                self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
                self.fader.fade(800)

            if self.bg_du != '':
                if self.eff_du == '' and self.tb_sh != '':
                    self.pre_process()
                self.background.create_mv_bg(self.bg_id, int(self.bg_x), int(self.bg_y), int(self.bg_xf), int(self.bg_yf), int(self.bg_du))
            else:
                if self.bg_x == '':
                    self.bg_x = 0
                if self.bg_y == '':
                    self.bg_y = 0
                self.background.create_bg(self.bg_id, int(self.bg_x), int(self.bg_y))

        self.init_portrait()

    def init_portrait(self):

        print('init_portrait')

        if int(self.pt_num) != 0:
            self.pt_loop()

        self.init_text_box()

    def init_text_box(self):

        print('init_text_box')

        self.text_character_label.clear()
        self.text_box_label.clear()

        if self.tb_sh != '':
            self.show_text_box()

        else:
            self.init_voice()

    def init_voice(self):

        print('init_voice')

        if self.tb_vc != '':
            self.voice.play_voice(self.tb_vc)

        self.init_text()

    def init_text(self):

        print('init_text')

        self.text_character_label.setText(self.tb_char)
        self.text_box_label.set_text(self.tb_txt)

    def update_engine(self, event):

        if self.text_box_label.index < len(self.tb_txt):
            self.text_box_label.setText(self.tb_txt)
            self.text_box_label.index = len(self.tb_txt)

        else:
            print('update_engine')

            self.game_engine_id += 1
            print(self.game_engine_id)

            self.set_background_music()

    def set_background_music(self):

        print('set_background_music')

        if int(self.bgm_num) != 0:
            self.post_bgm_loop()

        self.set_sound()

    def set_sound(self):

        print('set_sound')

        self.set_text()

    def set_text(self):

        print('set_text')

        self.text_character_label.clear()
        self.text_box_label.clear()

        self.set_portrait()

    def set_portrait(self):

        print('set_portrait')

        if int(self.pt_num) != 0:
            self.post_pt_loop()

        self.set_text_box()

    def set_text_box(self):

        print('set_text_box')

        if self.tb_hi != '':
            self.hide_text_box()

        else:
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
        self.fader_widget = FaderWidget(self.text_box_widget, 1.0)
        self.fader_widget.hide(250)
        self.fader_widget.anime.finished.connect(self.finsh_hide_widget)

    def finsh_hide_widget(self):

        self.text_box_widget.hide()
        self.disable_hide_label.show()

    def show_widget(self, event):

        self.text_box_widget.show()
        self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
        self.fader_widget.show(250)
        self.fader_widget.anime.finished.connect(self.finish_show_widget)

    def finish_show_widget(self):

        self.disable_hide_label.hide()
        self.hide_button.setEnabled(True)

    def hide_effect(self):

        self.effect_status = True
        self.next_label.show()
        self.text_box_label.clear()
        self.text_character_label.clear()

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(800)

        self.effect.hide()
        self.init_mask()

    def show_text_box(self):

        self.next_label.hide()
        self.hide_button.setEnabled(False)

        if self.tb_td != '':
            QTimer.singleShot(int(self.tb_td), self.delay_show_text_box)

        else:
            self.text_box_widget.show()
            self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
            self.fader_widget.show(400)
            self.fader_widget.anime.finished.connect(self.finish_show_text_box)

    def delay_show_text_box(self):

        self.text_box_widget.show()
        self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
        self.fader_widget.show(400)
        self.fader_widget.anime.finished.connect(self.finish_show_text_box)

    def finish_show_text_box(self):

        self.disable_hide_label.hide()
        self.next_label.show()
        self.hide_button.setEnabled(True)
        self.init_voice()

    def hide_text_box(self):

        self.next_label.hide()
        self.disable_hide_label.hide()
        self.hide_button.setEnabled(False)
        self.fader_widget = FaderWidget(self.text_box_widget, 1.0)
        self.fader_widget.hide(400)
        self.fader_widget.anime.finished.connect(self.finsh_hide_text_box)

    def finsh_hide_text_box(self):

        self.next_label.show()
        self.text_box_widget.hide()
        self.init_parser()

    def pre_process(self):

        self.pre_effect = QGraphicsOpacityEffect()
        self.pre_effect.setOpacity(0.000001)
        self.text_box_widget.setGraphicsEffect(self.pre_effect)
        self.text_box_widget.show()
        self.text_box_label.setText('     ')

    def selection(self):

        print('selection')

        for i in range(int(self.sl_num)):

            pos = 250 + int(i - int(int(self.sl_num) / 2)) * 75

            self.selection_button[i] = SelectButton(self.select_widget)
            self.selection_button.get(i).setStyleSheet('QAbstractButton {font-family: Times New Roman; font-size: 18px; color: rgba(0, 0, 0, 100%)}')
            self.selection_button.get(i).setText('{0}'.format(i))
            self.selection_button.get(i).set_text(self.sl_txt.get(i + 1))
            self.selection_button.get(i).setGeometry(0, pos, 1024, 65)
            self.selection_button.get(i).clicked.connect(self.jump_script)

        fader = Fader(self.game_engine_widget, self.game_engine_widget)
        fader.fade(800)
        self.select_widget.show()

    def jump_script(self):

        selection = int(self.sender().text())
        print(selection)

        self.game_engine_id = 0
        self.script = self.sl_sc.get(selection + 1)
        print(self.script)

        fader = Fader(self.game_engine_widget, self.game_engine_widget)
        fader.fade(800)
        self.select_widget.hide()
        for each in self.selection_button:
            self.selection_button.get(each).deleteLater()
        self.selection_button.clear()
        self.init_parser()

    def pt_loop(self):

        for i in range(self.pt_num):

            if self.pt_md.get(i + 1) == 'new':
                if self.pt_du.get(i + 1) != None:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).create_mv_pt(self.pt_id.get(i + 1), int(self.pt_x.get(i + 1)), int(self.pt_y.get(i + 1)), int(self.pt_xf.get(i + 1)), int(self.pt_yf.get(i + 1)), int(self.pt_du.get(i + 1)))
                else:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).create_pt(self.pt_id.get(i + 1), int(self.pt_x.get(i + 1)), int(self.pt_y.get(i + 1)))
            elif self.pt_md.get(i + 1) == 'mv':
                self.portrait.get(int(self.pt_pos.get(i + 1))).move_pt(int(self.pt_xf.get(i + 1)), int(self.pt_yf.get(i + 1)), int(self.pt_du.get(i + 1)))
            elif self.pt_md.get(i + 1) == 'del':
                if self.pt_du.get(i + 1) != None:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).delete_mv_pt(int(self.pt_xf.get(i + 1)), int(self.pt_yf.get(i + 1)), int(self.pt_du.get(i + 1)))
                else:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).delete_pt()

    def post_pt_loop(self):

        for i in range(int(self.pt_num)):

            if self.pt_md.get(i + 1) == 'dell':
                if self.pt_du.get(i + 1) != None:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).delete_mv_pt(int(self.pt_xf.get(i + 1)), int(self.pt_yf.get(i + 1)), int(self.pt_du.get(i + 1)))
                else:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).delete_pt()

    def bgm_loop(self):

        for i in range(self.bgm_num):

            if self.bgm_md.get(i + 1) == 'new':
                self.background_music.get(int(self.bgm_pos.get(i + 1))).play_music(self.bgm_id.get(i + 1))
            elif self.bgm_md.get(i + 1) == 'vol':
                self.background_music.get(int(self.bgm_pos.get(i + 1))).music_volume(int(self.bgm_vol.get(i + 1)))
            elif self.bgm_md.get(i + 1) == 'del':
                self.background_music.get(int(self.bgm_pos.get(i + 1))).stop_music()

    def post_bgm_loop(self):

        for i in range(int(self.bgm_num)):

            if self.bgm_md.get(i + 1) == 'dell':
                self.background_music.get(int(self.bgm_pos.get(i + 1))).stop_music()
