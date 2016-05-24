#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button_class import *

import sys
import resources

class Load(QMainWindow):
    """this class creates game load layout and functions"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor

    def create_load_layout(self, status):
        #this is the layout for the load window

        self.status = status
        print(self.status)

        #set QWidget class
        self.load_widget = QWidget()

        #set load page background
        self.bg = QLabel(self.load_widget)
        self.bg.setPixmap(QPixmap(":/load_background.png"))
        self.bg.setGeometry(0, 0, 960, 540)

        #create a strat button
        self.main_start_button = ImageButton("main_start", self.load_widget)
        self.main_start_button.setGeometry(755, 45, 160, 55)

        #create a exit button
        self.main_exit_button = ImageButton("main_exit", self.load_widget)
        self.main_exit_button.setGeometry(755, 445, 160, 55)