#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button_class import *

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
        self.text_box_label = QLabel(self.game_engine_widget)
        self.text_box_label.setText("Test Text\n測試文本\nテストテキスト")        
        self.text_box_label.setFont(self.text_font)
        self.text_box_label.setAlignment(Qt.AlignLeft) #make text align top left
        self.text_box_label.setGeometry(100, 430, 685, 100)
        self.text_box_label.setStyleSheet("QLabel {color: rgba(255, 255, 255, 80%)}")

        '''###################################################################### test button start
        #create a load button
        self.main_load_button = ImageButton("main_load", self.game_engine_widget)
        self.main_load_button.setGeometry(755, 145, 160, 55)

        #create a extra button
        self.main_extra_button = ImageButton("main_extra", self.game_engine_widget)
        self.main_extra_button.setGeometry(755, 245, 160, 55)

        #create a exit button
        self.main_exit_button = ImageButton("main_exit", self.game_engine_widget)
        self.main_exit_button.setGeometry(755, 45, 160, 55)

        #connection
        self.main_extra_button.clicked.connect(self.add_engine_id)
        ###################################################################### test button end'''

        self.auto_button = ImageButton("auto", self.game_engine_widget)
        self.auto_button.setGeometry(810, 435, 35, 35)

        self.skip_button = ImageButton("skip", self.game_engine_widget)
        self.skip_button.setGeometry(855, 435, 35, 35)

        self.log_button = ImageButton("log", self.game_engine_widget)
        self.log_button.setGeometry(900, 435, 35, 35)

        self.save_button = ImageButton("save", self.game_engine_widget)
        self.save_button.setGeometry(810, 480, 35, 35)

        self.load_button = ImageButton("load", self.game_engine_widget)
        self.load_button.setGeometry(855, 480, 35, 35)

        self.menu_button = ImageButton("menu", self.game_engine_widget)
        self.menu_button.setGeometry(900, 480, 35, 35)

        self.hide_button = ImageButton("hide", self.game_engine_widget)
        self.hide_button.setGeometry(755, 395, 30, 30)

    '''def add_engine_id(self):
        ####this is the test function

        self.game_engine_id += 1
        print(self.game_engine_id)'''
