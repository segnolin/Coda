#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import resources

class Parser(QXmlStreamReader):

    def __init__(self):
        super().__init__()

    def parse(self, script, game_engine_id):

        self.script = script
        self.id = str(game_engine_id)

        self.bgm_id = ''

        self.sd_id = ''

        self.eff_id = ''
        self.eff_du = ''

        self.mk_id = ''
        self.mk_md = ''

        self.bg_id = ''
        self.bg_x = ''
        self.bg_y = ''
        self.bg_xf = ''
        self.bg_yf = ''
        self.bg_du = ''

        self.pt_pos = {}
        self.pt_id = {}
        self.pt_md = {}
        self.pt_x = {}
        self.pt_y = {}
        self.pt_xf = {}
        self.pt_yf = {}
        self.pt_du = {}
        self.pt_num = 0

        self.tb_sh = ''
        self.tb_td = ''
        self.tb_vc = ''
        self.tb_char = ''
        self.tb_txt = ''
        self.tb_hi = ''

        self.sl_txt = {}
        self.sl_sc = {}
        self.sl_num = 0

        self.sys_sc = ''

        self.file = QFile(':/{0}.xml'.format(self.script))
        self.file.open(QIODevice.ReadOnly)
        self.setDevice(self.file)

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'content':
                    if self.attributes().value('id') == self.id:
                        self.parse_xml()
                        break

    def parse_xml(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'bgm':
                    self.parse_bgm()
                elif self.name() == 'sd':
                    self.parse_sd()
                elif self.name() == 'eff':
                    self.parse_eff()
                elif self.name() == 'mk':
                    self.parse_mk()
                elif self.name() == 'bg':
                    self.parse_bg()
                elif self.name() == 'pt':
                    self.parse_pt()
                elif self.name() == 'tb':
                    self.parse_tb()
                elif self.name() == 'sl':
                    self.parse_sl()
                elif self.name() == 'sys':
                    self.parse_sys()
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

    def parse_mk(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.mk_id = self.readElementText()
                elif self.name() == 'md':
                    self.mk_md = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'mk':
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
                if self.name() == 'pos':
                    self.pt_pos[self.pt_num] = self.readElementText()
                elif self.name() == 'id':
                    self.pt_id[self.pt_num] = self.readElementText()
                elif self.name() == 'md':
                    self.pt_md[self.pt_num] = self.readElementText()
                elif self.name() == 'x':
                    self.pt_x[self.pt_num] = self.readElementText()
                elif self.name() == 'y':
                    self.pt_y[self.pt_num] = self.readElementText()
                elif self.name() == 'xf':
                    self.pt_xf[self.pt_num] = self.readElementText()
                elif self.name() == 'yf':
                    self.pt_yf[self.pt_num] = self.readElementText()
                elif self.name() == 'du':
                    self.pt_du[self.pt_num] = self.readElementText()
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

    def parse_sl(self):

        self.sl_num += 1

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'txt':
                    self.sl_txt[self.sl_num] = self.readElementText()
                elif self.name() == 'sc':
                    self.sl_sc[self.sl_num] = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'sl':
                    break

    def parse_sys(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'sc':
                    self.sys_sc = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'sys':
                    break

if __name__ == '__main__':

    game_engine_id = 40
    script = 'a0000'
    parser = Parser()
    parser.parse(script, game_engine_id)

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
    print(parser.sl_txt)
    print(parser.sl_sc)
    print(parser.sl_num)
