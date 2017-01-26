#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.script_resources

from PyQt5.QtCore import *

from coda.data import *

class ScriptParser(QXmlStreamReader):

    def __init__(self):
        super().__init__()

    def parse(self, script, game_engine_id):

        self.data = Data()

        self.file = QFile(':/scr/{0}.xml'.format(script))
        self.file.open(QIODevice.ReadOnly)
        self.setDevice(self.file)

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'content':
                    if self.attributes().value('id') == str(game_engine_id):
                        self._parse_xml()
                        break

    def _parse_xml(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'bgm':
                    self._parse_bgm()
                elif self.name() == 'sd':
                    self._parse_sd()
                elif self.name() == 'eff':
                    self._parse_eff()
                elif self.name() == 'mk':
                    self._parse_mk()
                elif self.name() == 'bg':
                    self._parse_bg()
                elif self.name() == 'pt':
                    self._parse_pt()
                elif self.name() == 'tb':
                    self._parse_tb()
                elif self.name() == 'sl':
                    self._parse_sl()
                elif self.name() == 'sys':
                    self._parse_sys()
                else:
                    self._readNext()

            if self.isEndElement():
                if self.name() == 'content':
                    break

    def _parse_bgm(self):

        self.data.bgm_num += 1

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'pos':
                    self.data.bgm_pos[self.data.bgm_num] = self.readElementText()
                elif self.name() == 'id':
                    self.data.bgm_id[self.data.bgm_num] = self.readElementText()
                elif self.name() == 'vol':
                    self.data.bgm_vol[self.data.bgm_num] = self.readElementText()
                elif self.name() == 'md':
                    self.data.bgm_md[self.data.bgm_num] = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'bgm':
                    break

    def _parse_sd(self):

        self.data.sd_num += 1

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'pos':
                    self.data.sd_pos[self.data.sd_num] = self.readElementText()
                elif self.name() == 'id':
                    self.data.sd_id[self.data.sd_num] = self.readElementText()
                elif self.name() == 'md':
                    self.data.sd_md[self.data.sd_num] = self.readElementText()
                elif self.name() == 'lp':
                    self.data.sd_lp[self.data.sd_num] = self.readElementText()
                elif self.name() == 'fd':
                    self.data.sd_fd[self.data.sd_num] = self.readElementText()
                elif self.name() == 'dfd':
                    self.data.sd_dfd[self.data.sd_num] = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'sd':
                    break

    def _parse_eff(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.data.eff_id = self.readElementText()
                elif self.name() == 'du':
                    self.data.eff_du = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'eff':
                    break

    def _parse_mk(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.data.mk_id = self.readElementText()
                elif self.name() == 'md':
                    self.data.mk_md = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'mk':
                    break

    def _parse_bg(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'id':
                    self.data.bg_id = self.readElementText()
                elif self.name() == 'x':
                    self.data.bg_x = self.readElementText()
                elif self.name() == 'y':
                    self.data.bg_y = self.readElementText()
                elif self.name() == 'xf':
                    self.data.bg_xf = self.readElementText()
                elif self.name() == 'yf':
                    self.data.bg_yf = self.readElementText()
                elif self.name() == 'du':
                    self.data.bg_du = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'bg':
                    break

    def _parse_pt(self):

        self.data.pt_num += 1

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'pos':
                    self.data.pt_pos[self.data.pt_num] = self.readElementText()
                elif self.name() == 'id':
                    self.data.pt_id[self.data.pt_num] = self.readElementText()
                elif self.name() == 'md':
                    self.data.pt_md[self.data.pt_num] = self.readElementText()
                elif self.name() == 'x':
                    self.data.pt_x[self.data.pt_num] = self.readElementText()
                elif self.name() == 'y':
                    self.data.pt_y[self.data.pt_num] = self.readElementText()
                elif self.name() == 'xf':
                    self.data.pt_xf[self.data.pt_num] = self.readElementText()
                elif self.name() == 'yf':
                    self.data.pt_yf[self.data.pt_num] = self.readElementText()
                elif self.name() == 'du':
                    self.data.pt_du[self.data.pt_num] = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'pt':
                    break

    def _parse_tb(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'sh':
                    self.data.tb_sh = self.readElementText()
                elif self.name() == 'td':
                    self.data.tb_td = self.readElementText()
                elif self.name() == 'vc':
                    self.data.tb_vc = self.readElementText()
                elif self.name() == 'char':
                    self.data.tb_char = self.readElementText()
                elif self.name() == 'txt':
                    self.data.tb_txt = self.readElementText()
                elif self.name() == 'hi':
                    self.data.tb_hi = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'tb':
                    break

    def _parse_sl(self):

        self.data.sl_num += 1

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'txt':
                    self.data.sl_txt[self.data.sl_num] = self.readElementText()
                elif self.name() == 'sc':
                    self.data.sl_sc[self.data.sl_num] = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'sl':
                    break

    def _parse_sys(self):

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'sc':
                    self.data.sys_sc = self.readElementText()
                else:
                    self.readNext()

            if self.isEndElement():
                if self.name() == 'sys':
                    break
