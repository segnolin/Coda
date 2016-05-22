from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button_class import *

import sys
import resources

class Load(QMainWindow):

    def __init__(self):
        super().__init__()

    def create_load_layout(self, status):

        self.status = status
        print(self.status)

        self.load_widget = QWidget()

        self.bg = QLabel(self.load_widget)
        self.bg.setPixmap(QPixmap(":/load_background.png"))
        self.bg.setGeometry(0, 0, 960, 540)

        #create a strat button
        self.start_button = ImageButton("start", self.load_widget)
        self.start_button.setGeometry(755, 45, 160, 55)

        #create a exit button
        self.exit_button = ImageButton("exit", self.load_widget)
        self.exit_button.setGeometry(755, 445, 160, 55)