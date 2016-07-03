#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class Parser(QXmlStreamReader):

    def __init__(self, game_engine_id):
        super().__init__()

        self.id = str(game_engine_id)

        self.bgm_id = ''

        self.sd_id = ''

        self.eff_id = ''
        self.eff_du = ''

        self.bg_id = ''
        self.bg_x = ''
        self.bg_y = ''
        self.bg_xf = ''
        self.bg_yf = ''
        self.bg_du = ''

        self.pt_id = {}
        self.pt_x = {}
        self.pt_y = {}
        self.pt_xf = {}
        self.pt_yf = {}

        self.tb_sh = ''
        self.tb_td = ''
        self.tb_vc = ''
        self.tb_char = ''
        self.tb_txt = ''
        self.tb_hi = ''

        self.pt_num = -1

        self.file = QFile(':/totono.xml')
        self.file.open(QIODevice.ReadOnly)
        self.setDevice(self.file)

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'content':
                    if self.attributes().value('id') == self.id:
                        self.parse()
                        break

    def parse(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'bgm':
                    self.parse_bgm()
                elif self.name() == 'sd':
                    self.parse_sd()
                elif self.name() == 'eff':
                    self.parse_eff()
                elif self.name() == 'bg':
                    self.parse_bg()
                elif self.name() == 'pt':
                    self.parse_pt()
                elif self.name() == 'tb':
                    self.parse_tb()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'content':
                    #print('break content')
                    break

    def parse_bgm(self):

         while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.bgm_id = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'bgm':
                    break

    def parse_sd(self):

         while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.sd_id = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'sd':
                    break

    def parse_eff(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.eff_id = self.readElementText()
                elif self.name() == 'du':
                    self.eff_du = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'eff':
                    break

    def parse_bg(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.bg_id = self.readElementText()
                elif self.name() == 'x':
                    self.bg_x = self.readElementText()
                elif self.name() == 'y':
                    self.bg_y = self.readElementText()
                elif self.name() == 'xf':
                    self.bg_xf = self.readElementText()
                elif self.name() == 'yf':
                    self.bg_yf = self.readElementText()
                elif self.name() == 'du':
                    self.bg_du = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'bg':
                    break

    def parse_pt(self):

        self.pt_num += 1

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.pt_id[self.pt_num] = self.readElementText()
                elif self.name() == 'x':
                    self.pt_x[self.pt_num] = self.readElementText()
                elif self.name() == 'y':
                    self.pt_y[self.pt_num] = self.readElementText()
                elif self.name() == 'xf':
                    self.pt_xf[self.pt_num] = self.readElementText()
                elif self.name() == 'yf':
                    self.pt_yf[self.pt_num] = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'pt':
                    break

    def parse_tb(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'sh':
                    self.tb_sh = self.readElementText()
                elif self.name() == 'td':
                    self.tb_td = self.readElementText()
                elif self.name() == 'vc':
                    self.tb_vc = self.readElementText()
                elif self.name() == 'char':
                    self.tb_char = self.readElementText()
                elif self.name() == 'txt':
                    self.tb_txt = self.readElementText()
                elif self.name() == 'hi':
                    self.tb_hi = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'tb':
                    break

if __name__ == '__main__':

    game_engine_id = 10
    parser = Parser(game_engine_id)

    print(parser.bgm_id)
    print(parser.sd_id)
    print(parser.eff_id)
    print(parser.eff_du)
    print(parser.bg_id)
    print(parser.bg_x)
    print(parser.bg_y)
    print(parser.bg_xf)
    print(parser.bg_yf)
    print(parser.bg_du)
    print(parser.pt_id)
    print(parser.pt_x)
    print(parser.pt_y)
    print(parser.pt_xf)
    print(parser.pt_yf)
    print(parser.tb_sh)
    print(parser.tb_td)
    print(parser.tb_vc)
    print(parser.tb_char)
    print(parser.tb_txt)
    print(parser.tb_hi)
    print(parser.pt_num)
