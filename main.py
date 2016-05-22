from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from game_engine_class import *
from load_class import *
from image_button_class import *

import sys
import resources

class MainWindow(QMainWindow):
    """this class creates a main window to show the main menu"""

    #constructor
    def __init__(self):
        super().__init__() #call super class constructor

        self.__game_engine_id = 0 #set the initial game engine id
        self.__status = "main" #set the initial game engine id

        self.setWindowTitle("Galgame Engine") #set window title
        self.setFixedSize(960, 540) #set window size to 960 * 540

        self.create_main_window_layout() #call function to create the initial layout of main window

        self.stacked_layout = QStackedLayout() #this holds the various layouts this window needs
        self.stacked_layout.addWidget(self.main_window_widget)

        #set the central widget to display the layout
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def create_main_window_layout(self):
        #this is the initial layout of the main window

        #set QWidget class
        self.main_window_widget = QWidget()
        
        #set background picture by QLabel
        self.main_background = QLabel(self.main_window_widget)
        self.main_background.setPixmap(QPixmap(":/main_background.png"))
        self.main_background.setGeometry(0, 0, 960, 540)

        #set the background label of main button
        self.main_button_background = QLabel(self.main_window_widget)
        self.main_button_background.setPixmap(QPixmap(":/main_button_background.png"))
        self.main_button_background.setGeometry(710, 0, 250, 540)

        #create all the buttons
        #create a strat button
        self.start_button = ImageButton("start", self.main_window_widget)
        self.start_button.setGeometry(755, 45, 160, 55)

        #create a load button
        self.load_button = ImageButton("load", self.main_window_widget)
        self.load_button.setGeometry(755, 145, 160, 55)

        #create a extra button
        self.extra_button = ImageButton("extra", self.main_window_widget)
        self.extra_button.setGeometry(755, 245, 160, 55)

        #create a settings button
        self.settings_button = ImageButton("settings", self.main_window_widget)
        self.settings_button.setGeometry(755, 345, 160, 55)

        #create a exit button
        self.exit_button = ImageButton("exit", self.main_window_widget)
        self.exit_button.setGeometry(755, 445, 160, 55)

        #connections
        self.start_button.clicked.connect(self.start)
        self.load_button.clicked.connect(self.load)
        self.extra_button.clicked.connect(self.extra)
        self.settings_button.clicked.connect(self.settings)
        self.exit_button.clicked.connect(self.exit)

    def load_game_engine(self):
        self.__game_engine_id = 3
        self.start()

    def back_to_main(self):

        print("back to main")
        self.stacked_layout.setCurrentWidget(self.main_window_widget) #change the visible layout in the stack
        self.__game_engine_id = 0 #set the initial game engine id
        self.__status = "main" #set the initial game engine id

    def back_to_game_engine(self):

        print("back to game engine")
        self.stacked_layout.setCurrentWidget(self.game_engine.game_engine_widget)

    def start(self):
        
        print("start")
        #self.game_engine_id = "000000" #set the initial game engine id
        self.game_engine = GameEngine() #call the GameEngine class from game_engine_class.py
        self.game_engine.create_game_engine_layout(self.__game_engine_id) #create the game engine layout by game engine id
        self.stacked_layout.addWidget(self.game_engine.game_engine_widget) #add new widget to the stacked layout
        self.stacked_layout.setCurrentWidget(self.game_engine.game_engine_widget) #change the visible layout in the stack
        
        self.__status = "game_engine"

        #connection
        self.game_engine.load_button.clicked.connect(self.load)
        self.game_engine.exit_button.clicked.connect(self.back_to_main)

    def load(self):

        print("load")
        #self.status = "main" #set the initial game engine id
        self.load_game = Load() #call the Load class from load_class.py
        self.load_game.create_load_layout(self.__status) #create the load layout
        self.stacked_layout.addWidget(self.load_game.load_widget) #add new widget to the stacked layout
        self.stacked_layout.setCurrentWidget(self.load_game.load_widget) #change the visible layout in the stack
        
        #connection
        self.load_game.start_button.clicked.connect(self.load_game_engine)
        if self.__status == "main":
            self.load_game.exit_button.clicked.connect(self.back_to_main)
        elif self.__status == "game_engine":
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
    main_window = MainWindow() #create new instance of main window
    main_window.show() #make instance visible
    main_window.raise_() #raise instance to top of window stack
    sys.exit(app.exec_()) #monitor application for events

if __name__ == "__main__":
    main()