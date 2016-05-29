#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button_class import *
from fader_widget_class import *
from letter_print_class import *

import sys
import resources

class GameEngine(QMainWindow):
    """this class creates game engine layout and functions"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor

    def create_game_engine_layout(self, game_engine_id):
        #this is the layout for the game engine window

        self.game_engine_id = game_engine_id #get the game engine id from positional argument
        print(self.game_engine_id)

        #set QWidget class
        self.game_engine_widget = QWidget()

        #create basic game engine layout
        #create background cg
        self.cg = QLabel(self.game_engine_widget)
        self.cg.setPixmap(QPixmap(":/bg_0000.png"))
        self.cg.setGeometry(0, 0, 960, 540)

        #create text background label
        self.text_background_label = QLabel(self.game_engine_widget)
        self.text_background_label.setPixmap(QPixmap(":/text_background.png"))
        self.text_background_label.setGeometry(0, 340, 960, 200)

        #set the text box label
        self.text_font = QFont("Noto Sans CJK TC Regular", 14, QFont.Bold)
        self.text_box_label = LetterPrint(self.game_engine_widget)
        self.text_box_label.set_text("Test Text\n測試文本\nテストテキスト")
        self.text_box_label.setFont(self.text_font)
        self.text_box_label.setAlignment(Qt.AlignLeft) #make text align top left
        self.text_box_label.setGeometry(100, 430, 685, 100)
        self.text_box_label.setStyleSheet("QLabel {color: rgba(255, 255, 255, 100%)}")

        #create disable hide label to show all widget
        self.disable_hide_label = QLabel(self.game_engine_widget)
        self.disable_hide_label.setGeometry(0, 0, 960, 540)
        self.hide()

        #create transparent label to add game engine id(next)
        self.next_label = QLabel(self.game_engine_widget)
        self.next_label.setGeometry(0, 0, 960, 540)

        #create a auto button
        self.auto_button = ImageButton("auto", self.game_engine_widget)
        self.auto_button.setGeometry(810, 435, 35, 35)

        #create a skip button
        self.skip_button = ImageButton("skip", self.game_engine_widget)
        self.skip_button.setGeometry(855, 435, 35, 35)

        #create a log button
        self.log_button = ImageButton("log", self.game_engine_widget)
        self.log_button.setGeometry(900, 435, 35, 35)

        #create a save button
        self.save_button = ImageButton("save", self.game_engine_widget)
        self.save_button.setGeometry(810, 480, 35, 35)

        #create a load button
        self.load_button = ImageButton("load", self.game_engine_widget)
        self.load_button.setGeometry(855, 480, 35, 35)

        #create a menu button
        self.menu_button = ImageButton("menu", self.game_engine_widget)
        self.menu_button.setGeometry(900, 480, 35, 35)

        #create a hide button
        self.hide_button = ImageButton("hide", self.game_engine_widget)
        self.hide_button.setGeometry(760, 400, 25, 25)

        #create menu layout
        #create menu background
        self.menu_background_label = QLabel(self.game_engine_widget)
        self.menu_background_label.setPixmap(QPixmap(":/menu_background.png"))
        self.menu_background_label.setGeometry(0, 0, 960, 540)
        self.menu_background_label.hide()

        #create back button
        self.back_button = ImageButton("menu_back", self.game_engine_widget)
        self.back_button.setGeometry(400, 64, 160, 55)
        self.back_button.hide()

        #create title button
        self.title_button = ImageButton("menu_title", self.game_engine_widget)
        self.title_button.setGeometry(400, 183, 160, 55)
        self.title_button.hide()

        #create config button
        self.config_button = ImageButton("menu_config", self.game_engine_widget)
        self.config_button.setGeometry(400, 302, 160, 55)
        self.config_button.hide()

        #create exit button
        self.exit_button = ImageButton("menu_exit", self.game_engine_widget)
        self.exit_button.setGeometry(400, 421, 160, 55)
        self.exit_button.hide()

        #connection
        self.back_button.clicked.connect(self.hide_menu)
        self.menu_button.clicked.connect(self.show_menu)
        self.hide_button.clicked.connect(self.hide_widget)
        self.disable_hide_label.mousePressEvent = self.show_widget
        self.next_label.mousePressEvent = self.add_engine_id

    def hide_menu(self):
        #this is the funtion to hide menu layout

        self.fader_widget = FaderWidget(self.game_engine_widget, self.game_engine_widget, 250) #call fade class
        
        self.text_background_label.show()
        self.text_box_label.show()
        self.auto_button.show()
        self.skip_button.show()
        self.log_button.show()
        self.save_button.show()
        self.load_button.show()
        self.menu_button.show()
        self.hide_button.show()

        self.menu_background_label.hide()
        self.back_button.hide()
        self.title_button.hide()
        self.config_button.hide()
        self.exit_button.hide()

    def show_menu(self):
        #this is the funtion to show menu layout

        self.fader_widget = FaderWidget(self.game_engine_widget, self.game_engine_widget, 250) #call fade class
        
        self.text_background_label.hide()
        self.text_box_label.hide()
        self.auto_button.hide()
        self.skip_button.hide()
        self.log_button.hide()
        self.save_button.hide()
        self.load_button.hide()
        self.menu_button.hide()
        self.hide_button.hide()

        self.menu_background_label.show()
        self.back_button.show()
        self.title_button.show()
        self.config_button.show()
        self.exit_button.show()

    def hide_widget(self):
        #this is the funtion to hide all widgets

        self.fader_widget = FaderWidget(self.game_engine_widget, self.game_engine_widget, 250) #call fade class
        
        self.text_background_label.hide()
        self.text_box_label.hide()
        self.next_label.hide()
        self.auto_button.hide()
        self.skip_button.hide()
        self.log_button.hide()
        self.save_button.hide()
        self.load_button.hide()
        self.menu_button.hide()
        self.hide_button.hide()
        
        self.disable_hide_label.show()

    def show_widget(self, event):
        #this is the funtion to show all widgets

        self.fader_widget = FaderWidget(self.game_engine_widget, self.game_engine_widget, 250) #call fade class
        
        self.text_background_label.show()
        self.text_box_label.show()
        self.next_label.show()
        self.auto_button.show()
        self.skip_button.show()
        self.log_button.show()
        self.save_button.show()
        self.load_button.show()
        self.menu_button.show()
        self.hide_button.show()

        self.disable_hide_label.hide()

    def add_engine_id(self, event):
        #this is the function to add game engine id

        self.game_engine_id += 1
        print(self.game_engine_id)

        self.update()

    def update(self):

        print("update")
        self.new_text = "Hi! This is line {0}".format(self.game_engine_id)
        self.text_box_label.set_text(self.new_text)
