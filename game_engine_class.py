from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button_class import *

import sys
import resources

class GameEngine(QMainWindow):

    def __init__(self):
        super().__init__()

    def create_game_engine_layout(self, game_engine_id):
        #this is the layout for the game engine window

        self.__game_engine_id = game_engine_id
        print(self.__game_engine_id)

        #create a widget to add some widget
        self.game_engine_widget = QWidget()
        
        self.cg = QLabel(self.game_engine_widget)
        self.cg.setPixmap(QPixmap(":/bg_0000.png"))
        self.cg.setGeometry(0, 0, 960, 540)
        
        self.text_background_label = QLabel(self.game_engine_widget)
        self.text_background_label.setPixmap(QPixmap(":/text_background.png"))
        self.text_background_label.setGeometry(0, 340, 960, 200)

        #set the text box label
        self.text_box_label = QLabel(self.game_engine_widget)
        self.text_box_label.setText("Test Text\n測試文本\nテストテキスト")

        self.text_font = QFont("Noto Sans CJK TC Regular", 16, QFont.Bold)
        self.text_box_label.setFont(self.text_font)

        self.text_box_label.setAlignment(Qt.AlignLeft) #make text align top left
        self.text_box_label.setGeometry(60, 400, 840, 120)
        self.text_box_label.setStyleSheet("QLabel {color: rgba(255, 255, 255, 80%)}")

        #create a load button
        self.load_button = ImageButton("load", self.game_engine_widget)
        self.load_button.setGeometry(755, 145, 160, 55)

        #create a extra button
        self.extra_button = ImageButton("extra", self.game_engine_widget)
        self.extra_button.setGeometry(755, 245, 160, 55)

        #create a exit button
        self.exit_button = ImageButton("exit", self.game_engine_widget)
        self.exit_button.setGeometry(755, 445, 160, 55)

        #connection
        self.extra_button.clicked.connect(self.add_engine_id)

    def add_engine_id(self):

        self.__game_engine_id += 1
        print(self.__game_engine_id)
