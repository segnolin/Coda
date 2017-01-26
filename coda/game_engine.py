#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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
from coda.sound import *
from coda.voice import *
from coda.data import *

class GameEngine(QMainWindow):
    '''this class creates game engine layout and functions'''

    def __init__(self):
        super().__init__()

        self._pixel_ratio = QWindow().devicePixelRatio()

    def create_game_engine_layout(self):

        #set game status
        self.init_status = True
        self.effect_status = False

        #set QWidget class
        self.game_engine_widget = QWidget()
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
        self.select_background_pixmap = self.select_background_pixmap.scaledToHeight(
                self.select_background_pixmap.height() * self._pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.select_background_pixmap.setDevicePixelRatio(self._pixel_ratio)
        self.select_background_label = QLabel(self.select_widget)
        self.select_background_label.setPixmap(self.select_background_pixmap)
        self.select_background_label.setGeometry(0, 0, 1024, 576)

        #create selection button
        self.selection_button = {}

        #create text box layout
        #create text background label
        self.text_background_pixmap = QPixmap(':/sys/text_background.png')
        self.text_background_pixmap = self.text_background_pixmap.scaledToHeight(
                self.text_background_pixmap.height() * self._pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.text_background_pixmap.setDevicePixelRatio(self._pixel_ratio)
        self.text_background_label = QLabel(self.text_box_widget)
        self.text_background_label.setPixmap(self.text_background_pixmap)
        self.text_background_label.setGeometry(0, 396, 1024, 180)

        #set the text character label
        self.text_character_label = QLabel(self.text_box_widget)
        self.text_character_label.setAlignment(Qt.AlignLeft)
        self.text_character_label.setGeometry(150, 446, 660, 30)
        self.text_character_label.setStyleSheet(
                'QLabel {color: rgba(0, 0, 0, 100%)}')
        self.text_character_label.setStyleSheet(
                'QLabel {font-family: Times New Roman;'
                'font-size: 20px; font-weight: Bold;'
                'color: rgba(0, 0, 0, 100%)}')

        #set the text box label
        self.text_box_label = LetterPrint(self.text_box_widget)
        self.text_box_label.setAlignment(Qt.AlignLeft)
        self.text_box_label.setGeometry(160, 486, 650, 75)
        self.text_box_label.setStyleSheet(
                'QLabel {font-family: Times New Roman;'
                'font-size: 18px; color: rgba(0, 0, 0, 100%)}')
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
        self.menu_background_pixmap = self.menu_background_pixmap.scaledToHeight(
                self.menu_background_pixmap.height() * self._pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.menu_background_pixmap.setDevicePixelRatio(self._pixel_ratio)
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
        self.save_button.clicked.connect(self._save_data)
        self.back_button.clicked.connect(self._hide_menu)
        self.menu_button.clicked.connect(self._show_menu)
        self.hide_button.clicked.connect(self._hide_widget)
        self.disable_hide_label.mousePressEvent = self._show_widget
        self.next_label.mousePressEvent = self._update_engine

        #set media
        self.voice = Voice()
        self.background_music = {}
        self.sound = {}
        for i in range(2):
            self.background_music[i] = BackgroundMusic()
        for i in range(3):
            self.sound[i] = Sound()

        #set parser
        self.parser = ScriptParser()

        #set save data 
        self.save_data = Data()

    ############################## MAIN PROGRAM START ##############################

    def start_game(self, script, game_engine_id):

        self.script = script
        self.game_engine_id = game_engine_id
        self.init_status = True
        self._init_parser()

    def _init_parser(self):

        #print('init_parser')

        self._parse_script()

        if self.sys_sc != '':
            self.script = self.sys_sc
            self.game_engine_id = -1
        if int(self.sl_num) != 0:
            self._selection()
        else:
            if self.init_status:
                self.eff_id = 'black_fade'
                self.eff_du = '2000'
                self.tb_sh = True
                if self.tb_td == '':
                    self.tb_td = 1000
                self._pre_process()
            self._init_background_music()

    def _init_background_music(self):

        #print('init_background_music')

        if int(self.bgm_num) != 0:
            self._pre_bgm_loop()

        self._init_effect()

    def _init_effect(self):

        #print('init_effect')

        if self.eff_id != '':

            self.background.anime.stop()
            self.next_label.hide()

            if not self.init_status:
                self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
                self.fader.fade(800)

            self.effect.show()
            self.effect.create(self.eff_id)
            QTimer.singleShot(int(self.eff_du), self._hide_effect)

        else:
            self.effect_status = False
            self._init_sound()
        
        self.init_status = False

    def _init_sound(self):

        #print('init_sound')

        if int(self.sd_num) != 0:
            self._pre_sd_loop()

        self._init_mask()

    def _init_mask(self):

        #print('init_mask')

        if self.mk_md == 'new':
            self.mask_label.set_mask(self.mk_id)
        elif self.mk_md == 'del':
            self.mask_label.delete_mask()

        self._init_background()

    def _init_background(self):

        #print('init_background')

        if self.bg_id != '':

            if not self.effect_status:
                self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
                self.fader.fade(800)

            if self.bg_du != '':
                if self.eff_du == '' and self.tb_sh != '':
                    self._pre_process()
                self.background.create_mv_bg(self.bg_id,
                        int(self.bg_x), int(self.bg_y),
                        int(self.bg_xf), int(self.bg_yf),
                        int(self.bg_du))
            else:
                if self.bg_x == '':
                    self.bg_x = 0
                if self.bg_y == '':
                    self.bg_y = 0
                self.background.create_bg(self.bg_id,
                        int(self.bg_x), int(self.bg_y))

        self._init_portrait()

    def _init_portrait(self):

        #print('init_portrait')

        if int(self.pt_num) != 0:
            self._pre_pt_loop()

        self._init_text_box()

    def _init_text_box(self):

        #print('init_text_box')

        self.text_character_label.clear()
        self.text_box_label.clear()

        if self.tb_sh != '':
            self._show_text_box()

        else:
            self._init_voice()

    def _init_voice(self):

        #print('init_voice')

        if self.tb_vc != '':
            self.voice.play_voice(self.tb_vc)

        self._init_text()

    def _init_text(self):

        #print('init_text')

        self.text_character_label.setText(self.tb_char)
        self.text_box_label.set_verbatim_text(self.tb_txt)

        self._standby()

    def _standby(self):

        pass

    def _update_engine(self, event):

        if self.text_box_label.index < len(self.tb_txt):
            self.text_box_label.setText(self.tb_txt)
            self.text_box_label.index = len(self.tb_txt)

        else:
            #print('update_engine')

            self.game_engine_id += 1
            #print(self.game_engine_id)

            self._set_background_music()

    def _set_background_music(self):

        #print('set_background_music')

        if int(self.bgm_num) != 0:
            self._post_bgm_loop()

        self._set_sound()

    def _set_sound(self):

        #print('set_sound')

        if int(self.sd_num) != 0:
            self._post_sd_loop()

        self._set_text()

    def _set_text(self):

        #print('set_text')

        self.text_character_label.clear()
        self.text_box_label.clear()

        self._set_portrait()

    def _set_portrait(self):

        #print('set_portrait')

        if int(self.pt_num) != 0:
            self._post_pt_loop()

        self._set_text_box()

    def _set_text_box(self):

        #print('set_text_box')

        if self.tb_hi != '':
            self._hide_text_box()

        else:
            self._init_parser()

    ############################## MAIN PROGRAM END ##############################

    #widget utilities
    def _hide_menu(self):

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(250)
        self.menu_widget.hide()
        self.text_box_widget.show()

    def _show_menu(self):

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(250)
        self.menu_widget.show()
        self.text_box_widget.hide()

    def _hide_widget(self):

        self.hide_button.setEnabled(False)
        self.fader_widget = FaderWidget(self.text_box_widget, 1.0)
        self.fader_widget.hide(250)
        self.fader_widget.anime.finished.connect(self._finish_hide_widget)

    def _finish_hide_widget(self):

        self.text_box_widget.hide()
        self.disable_hide_label.show()

    def _show_widget(self, event):

        self.text_box_widget.show()
        self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
        self.fader_widget.show(250)
        self.fader_widget.anime.finished.connect(self._finish_show_widget)

    def _finish_show_widget(self):

        self.disable_hide_label.hide()
        self.hide_button.setEnabled(True)

    def _hide_effect(self):

        self.effect_status = True
        self.next_label.show()
        self.text_box_label.clear()
        self.text_character_label.clear()

        self.fader = Fader(self.game_engine_widget, self.game_engine_widget)
        self.fader.fade(800)

        self.effect.hide()
        self._init_sound()

    def _show_text_box(self):

        self.next_label.hide()
        self.hide_button.setEnabled(False)

        if self.tb_td != '':
            QTimer.singleShot(int(self.tb_td), self._delay_show_text_box)

        else:
            self.text_box_widget.show()
            self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
            self.fader_widget.show(400)
            self.fader_widget.anime.finished.connect(self._finish_show_text_box)

    def _delay_show_text_box(self):

        self.text_box_widget.show()
        self.fader_widget = FaderWidget(self.text_box_widget, 0.0)
        self.fader_widget.show(400)
        self.fader_widget.anime.finished.connect(self._finish_show_text_box)

    def _finish_show_text_box(self):

        self.disable_hide_label.hide()
        self.next_label.show()
        self.hide_button.setEnabled(True)
        self._init_voice()

    def _hide_text_box(self):

        self.next_label.hide()
        self.disable_hide_label.hide()
        self.hide_button.setEnabled(False)
        self.fader_widget = FaderWidget(self.text_box_widget, 1.0)
        self.fader_widget.hide(400)
        self.fader_widget.anime.finished.connect(self._finsh_hide_text_box)

    def _finsh_hide_text_box(self):

        self.next_label.show()
        self.text_box_widget.hide()
        self._init_parser()

    def _pre_process(self):

        self.pre_effect = QGraphicsOpacityEffect()
        self.pre_effect.setOpacity(0.000001)
        self.text_box_widget.setGraphicsEffect(self.pre_effect)
        self.text_box_widget.show()
        self.text_box_label.setText('     ')

    #main program functions
    def _parse_script(self):

        self.parser.parse(self.script, self.game_engine_id)

        self.bgm_pos = self.parser.data.bgm_pos
        self.bgm_id = self.parser.data.bgm_id
        self.bgm_md = self.parser.data.bgm_md
        self.bgm_vol = self.parser.data.bgm_vol
        self.bgm_num = self.parser.data.bgm_num

        self.sd_pos = self.parser.data.sd_pos
        self.sd_id = self.parser.data.sd_id
        self.sd_md = self.parser.data.sd_md
        self.sd_lp = self.parser.data.sd_lp
        self.sd_fd = self.parser.data.sd_fd
        self.sd_dfd = self.parser.data.sd_dfd
        self.sd_num = self.parser.data.sd_num

        self.eff_id = self.parser.data.eff_id
        self.eff_du = self.parser.data.eff_du

        self.mk_id = self.parser.data.mk_id
        self.mk_md = self.parser.data.mk_md

        self.bg_id = self.parser.data.bg_id
        self.bg_x = self.parser.data.bg_x
        self.bg_y = self.parser.data.bg_y
        self.bg_xf = self.parser.data.bg_xf
        self.bg_yf = self.parser.data.bg_yf
        self.bg_du = self.parser.data.bg_du

        self.pt_pos = self.parser.data.pt_pos
        self.pt_id = self.parser.data.pt_id
        self.pt_md = self.parser.data.pt_md
        self.pt_x = self.parser.data.pt_x
        self.pt_y = self.parser.data.pt_y
        self.pt_xf = self.parser.data.pt_xf
        self.pt_yf = self.parser.data.pt_yf
        self.pt_du = self.parser.data.pt_du
        self.pt_num = self.parser.data.pt_num

        self.tb_sh = self.parser.data.tb_sh
        self.tb_td = self.parser.data.tb_td
        self.tb_vc = self.parser.data.tb_vc
        self.tb_char = self.parser.data.tb_char
        self.tb_txt = self.parser.data.tb_txt
        self.tb_hi = self.parser.data.tb_hi

        self.sl_txt = self.parser.data.sl_txt
        self.sl_sc = self.parser.data.sl_sc
        self.sl_num = self.parser.data.sl_num

        self.sys_sc = self.parser.data.sys_sc

    def _selection(self):

        #print('selection')

        for i in range(int(self.sl_num)):

            pos = 250 + int(i - int(int(self.sl_num) / 2)) * 75

            self.selection_button[i] = SelectButton(self.select_widget)
            self.selection_button.get(i).setStyleSheet(
                    'QAbstractButton {font-family: Times New Roman;'
                    'font-size: 18px; color: rgba(0, 0, 0, 100%)}')
            self.selection_button.get(i).setText('{0}'.format(i))
            self.selection_button.get(i).set_text(self.sl_txt.get(i + 1))
            self.selection_button.get(i).setGeometry(0, pos, 1024, 65)
            self.selection_button.get(i).clicked.connect(self._jump_script)

        fader = Fader(self.game_engine_widget, self.game_engine_widget)
        fader.fade(800)
        self.select_widget.show()

    def _jump_script(self):

        selection = int(self.sender().text())
        #print(selection)

        self.game_engine_id = 0
        self.script = self.sl_sc.get(selection + 1)
        #print(self.script)

        fader = Fader(self.game_engine_widget, self.game_engine_widget)
        fader.fade(800)
        self.select_widget.hide()
        for each in self.selection_button:
            self.selection_button.get(each).deleteLater()
        self.selection_button.clear()
        self._init_parser()

    def _pre_bgm_loop(self):

        for i in range(self.bgm_num):

            if self.bgm_md.get(i + 1) == 'new':
                self.background_music.get(
                        int(self.bgm_pos.get(i + 1))).play_music(
                                self.bgm_id.get(i + 1))
            elif self.bgm_md.get(i + 1) == 'vol':
                self.background_music.get(
                        int(self.bgm_pos.get(i + 1))).music_volume(
                                int(self.bgm_vol.get(i + 1)))
            elif self.bgm_md.get(i + 1) == 'del':
                self.background_music.get(
                        int(self.bgm_pos.get(i + 1))).stop_music()

    def _post_bgm_loop(self):

        for i in range(int(self.bgm_num)):

            if self.bgm_md.get(i + 1) == 'dell':
                self.background_music.get(int(self.bgm_pos.get(i + 1))).stop_music()

    def _pre_pt_loop(self):

        for i in range(self.pt_num):

            if self.pt_md.get(i + 1) == 'new':
                if self.pt_du.get(i + 1) != None:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).create_mv_pt(
                            self.pt_id.get(i + 1),
                            int(self.pt_x.get(i + 1)), int(self.pt_y.get(i + 1)),
                            int(self.pt_xf.get(i + 1)), int(self.pt_yf.get(i + 1)),
                            int(self.pt_du.get(i + 1)))
                else:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).create_pt(
                            self.pt_id.get(i + 1),
                            int(self.pt_x.get(i + 1)), int(self.pt_y.get(i + 1)))

            elif self.pt_md.get(i + 1) == 'mv':
                self.portrait.get(int(self.pt_pos.get(i + 1))).move_pt(
                        int(self.pt_xf.get(i + 1)),
                        int(self.pt_yf.get(i + 1)), int(self.pt_du.get(i + 1)))

            elif self.pt_md.get(i + 1) == 'del':
                if self.pt_du.get(i + 1) != None:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).delete_mv_pt(
                            int(self.pt_xf.get(i + 1)),
                            int(self.pt_yf.get(i + 1)), int(self.pt_du.get(i + 1)))
                else:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).delete_pt()

    def _post_pt_loop(self):

        for i in range(int(self.pt_num)):

            if self.pt_md.get(i + 1) == 'dell':
                if self.pt_du.get(i + 1) != None:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).delete_mv_pt(
                            int(self.pt_xf.get(i + 1)),
                            int(self.pt_yf.get(i + 1)), int(self.pt_du.get(i + 1)))
                else:
                    self.portrait.get(int(self.pt_pos.get(i + 1))).delete_pt()

    def _pre_sd_loop(self):

        for i in range(self.sd_num):

            if self.sd_md.get(i + 1) == 'new':
                self.sound.get(
                        int(self.sd_pos.get(i + 1))).play_sound(self.sd_id.get(i + 1),
                                self.sd_lp.get(i + 1), self.sd_fd.get(i + 1))
            elif self.sd_md.get(i + 1) == 'del':
                self.sound.get(
                        int(self.sd_pos.get(i + 1))).stop_sound(self.sd_dfd.get(i + 1))

    def _post_sd_loop(self):

        for i in range(int(self.sd_num)):

            if self.sd_md.get(i + 1) == 'newl':
                self.sound.get(
                        int(self.sd_pos.get(i + 1))).play_sound(self.sd_id.get(i + 1),
                                self.sd_lp.get(i + 1), self.sd_fd.get(i + 1))
            if self.sd_md.get(i + 1) == 'dell':
                self.sound.get(
                        int(self.sd_pos.get(i + 1))).stop_sound(self.sd_dfd.get(i + 1))

    def _save_data(self):

        self.save_data = self.parser.data

        '''
        print()
        print('<background_music>')
        for i in range(2):
            print('\t[{0}]background_music_id: {1}'.format(
                    i, self.background_music.get(i).id))
            print('\t[{0}]background_music_vol: {1}'.format(
                    i, self.background_music.get(i).volume()))
            print('\t[{0}]background_music_state: {1}'.format(
                    i, self.background_music.get(i).state()))
        print()
        '''

        '''
        print('<sound>')
        for i in range(3):
            print('\t[{0}]sound_id: {1}'.format(
                    i, self.sound.get(i).id))
            print('\t[{0}]sound_mode: {1}'.format(
                    i, self.sound.get(i).playlist.playbackMode()))
            print('\t[{0}]sound_state: {1}'.format(
                    i, self.sound.get(i).state()))
        print()
        '''

        '''
        print('<mask>')
        print('\tmask_id: {0}'.format(self.mask_label.id))
        print()

        print('<background>')
        print('\tbackground_id: {0}'.format(self.background.background_id))
        print('\tbackground_x: {0}'.format(self.background.x))
        print('\tbackground_y: {0}'.format(self.background.y))
        print('\tbackground_posx: {0}'.format(self.background.posx))
        print('\tbackground_posy: {0}'.format(self.background.posy))
        print('\tbackground_posxf: {0}'.format(self.background.posxf))
        print('\tbackground_posyf: {0}'.format(self.background.posyf))
        print('\tbackground_duration: {0}'.format(self.background.duration))
        print()
        '''

        '''
        print('<portrait>')
        for i in range(5):
            print('\t[{0}]portrait_id: {1}'.format(
                    i, self.portrait.get(i).id))
            print('\t[{0}]portrait_x: {1}'.format(
                    i, self.portrait.get(i).x))
            print('\t[{0}]portrait_y: {1}'.format(
                    i, self.portrait.get(i).y))
            print('\t[{0}]portrait_posx: {1}'.format(
                    i, self.portrait.get(i).posx))
            print('\t[{0}]portrait_posy: {1}'.format(
                    i, self.portrait.get(i).posy))
            print('\t[{0}]portrait_posxf: {1}'.format(
                    i, self.portrait.get(i).posxf))
            print('\t[{0}]portrait_posyf: {1}'.format(
                    i, self.portrait.get(i).posyf))
            print('\t[{0}]portrait_duration: {1}'.format(
                    i, self.portrait.get(i).duration))
            print('\t[{0}]portrait_opac: {1}'.format(
                    i, self.portrait.get(i).opacity))
        print()
        print('=======================================')
        '''

        self.print_data(self.save_data)

    def print_data(self, data):

        print()

        print('self.bgm_pos: {0}'.format(self.bgm_pos))
        print('self.bgm_id: {0}'.format(self.bgm_id))
        print('self.bgm_md: {0}'.format(self.bgm_md))
        print('self.bgm_vol: {0}'.format(self.bgm_vol))
        print('self.bgm_num: {0}'.format(self.bgm_num))

        print('self.sd_pos: {0}'.format(self.sd_pos))
        print('self.sd_id: {0}'.format(self.sd_id))
        print('self.sd_md: {0}'.format(self.sd_md))
        print('self.sd_lp: {0}'.format(self.sd_lp))
        print('self.sd_fd: {0}'.format(self.sd_fd))
        print('self.sd_dfd: {0}'.format(self.sd_dfd))
        print('self.sd_num: {0}'.format(self.sd_num))

        print('self.eff_id: {0}'.format(self.eff_id))
        print('self.eff_du: {0}'.format(self.eff_du))

        print('self.mk_id: {0}'.format(self.mk_id))
        print('self.mk_md: {0}'.format(self.mk_md))

        print('self.bg_id: {0}'.format(self.bg_id))
        print('self.bg_x: {0}'.format(self.bg_x))
        print('self.bg_y: {0}'.format(self.bg_y))
        print('self.bg_xf: {0}'.format(self.bg_xf))
        print('self.bg_yf: {0}'.format(self.bg_yf))
        print('self.bg_du: {0}'.format(self.bg_du))

        print('self.pt_pos: {0}'.format(self.pt_pos))
        print('self.pt_id: {0}'.format(self.pt_id))
        print('self.pt_md: {0}'.format(self.pt_md))
        print('self.pt_x: {0}'.format(self.pt_x))
        print('self.pt_y: {0}'.format(self.pt_y))
        print('self.pt_xf: {0}'.format(self.pt_xf))
        print('self.pt_yf: {0}'.format(self.pt_yf))
        print('self.pt_du: {0}'.format(self.pt_du))
        print('self.pt_num: {0}'.format(self.pt_num))

        print('self.tb_sh: {0}'.format(self.tb_sh))
        print('self.tb_td: {0}'.format(self.tb_td))
        print('self.tb_vc: {0}'.format(self.tb_vc))
        print('self.tb_char: {0}'.format(self.tb_char))
        print('self.tb_txt: {0}'.format(self.tb_txt))
        print('self.tb_hi: {0}'.format(self.tb_hi))

        print('self.sl_txt: {0}'.format(self.sl_txt))
        print('self.sl_sc: {0}'.format(self.sl_sc))
        print('self.sl_num: {0}'.format(self.sl_num))

        print('self.sys_sc: {0}'.format(self.sys_sc))

        print()
        print('=======================================')
