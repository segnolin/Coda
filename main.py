#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from main_window_class import *
from game_engine_class import *
from load_class import *
from image_button_class import *

import sys
import resources

class Main(QMainWindow):
    """this class init the main window and manage connections"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor

        self.initUI() #run initUI function

    def initUI(self):

        self.game_engine_id = 0 #set the initial game engine id
        self.status = "main" #set the initial game status

        self.setWindowTitle("Coda") #set window title
        self.setFixedSize(960, 540) #set window size to 960 * 540

        self.main_window = MainWindow() #call the MianWindow class from main_window_class.py
        self.main_window.create_main_window_layout() #call function to create the initial layout of main window

        self.stacked_layout = QStackedLayout() #this holds the various layouts this window needs
        self.stacked_layout.addWidget(self.main_window.main_window_widget) #add main window widget to stacked layout

        #set the central widget to display the layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
    
        #connection
        self.main_window.start_button.clicked.connect(self.start)
        self.main_window.load_button.clicked.connect(self.load)
        self.main_window.extra_button.clicked.connect(self.extra)
        self.main_window.settings_button.clicked.connect(self.settings)
        self.main_window.exit_button.clicked.connect(self.exit)

    def load_game_engine(self):

        self.game_engine_id = 3 ####assume the load game engine id is 3
        self.start()

    def back_to_main(self):

        print("back to main")
        self.stacked_layout.setCurrentWidget(self.main_window.main_window_widget) #change the visible layout in the stack
        self.game_engine_id = 0 #set the initial game engine id
        self.status = "main" #set the initial game status

    def back_to_game_engine(self):

        print("back to game engine")
        self.stacked_layout.setCurrentWidget(self.game_engine.game_engine_widget) #change the visible layout in the stack

    def start(self):
        
        print("start")
        self.game_engine = GameEngine() #call the GameEngine class from game_engine_class.py
        self.game_engine.create_game_engine_layout(self.game_engine_id) #create the game engine layout by game engine id
        self.stacked_layout.addWidget(self.game_engine.game_engine_widget) #add new widget to the stacked layout
        self.stacked_layout.setCurrentWidget(self.game_engine.game_engine_widget) #change the visible layout in the stack
        
        self.status = "game_engine" #set the game status to game_engine

        #connection
        self.game_engine.load_button.clicked.connect(self.load)
        self.game_engine.exit_button.clicked.connect(self.back_to_main)

    def load(self):

        print("load")
        self.load_game = Load() #call the Load class from load_class.py
        self.load_game.create_load_layout(self.status) #create the load layout
        self.stacked_layout.addWidget(self.load_game.load_widget) #add new widget to the stacked layout
        self.stacked_layout.setCurrentWidget(self.load_game.load_widget) #change the visible layout in the stack
        
        #connection
        self.load_game.start_button.clicked.connect(self.load_game_engine)
        if self.status == "main":
            self.load_game.exit_button.clicked.connect(self.back_to_main)
        elif self.status == "game_engine":
            self.load_game.exit_button.clicked.connect(self.back_to_game_engine)

    def extra(self):

        print("extra")

    def settings(self):

        print("settings")

    def exit(self):         

        print("exit")
        self.close()

    def closeEvent(self, event):
        #this is the message box with two buttons to confirm the close event
        pass

def main():

    app = QApplication(sys.argv) #create new application
    main_window = Main() #create new instance of main window
    main_window.show() #make instance visible
    main_window.raise_() #raise instance to top of window stack
    sys.exit(app.exec_()) #monitor application for events

if __name__ == "__main__":
    main()