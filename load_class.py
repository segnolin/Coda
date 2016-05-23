#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button_class import *

import sys
import resources

class Load(QMainWindow):

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
        self.start_button = ImageButton("start", self.load_widget)
        self.start_button.setGeometry(755, 45, 160, 55)

        #create a exit button
        self.exit_button = ImageButton("exit", self.load_widget)
        self.exit_button.setGeometry(755, 445, 160, 55)