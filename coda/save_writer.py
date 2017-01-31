#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtCore import *

from coda.data import *

class SaveWriter(QXmlStreamWriter):

    def __init__(self):
        super().__init__()

        QDir().mkdir(QDir().homePath() + '/.coda')
        QDir().mkdir(QDir().homePath() + '/.coda/save')
        QFile().copy(':/sys/save_data.xml', QDir().homePath()
                + '/.coda/save/save_data.xml')
        QFile(QDir().homePath() + '/.coda/save/save_data.xml').setPermissions(
                QFileDevice.ReadOwner
                | QFileDevice.WriteOwner
                | QFileDevice.ReadUser
                | QFileDevice.ReadGroup
                | QFileDevice.ReadOther)

        self.save_data = {}
        self.thumbnail_data = {}
        self.data_index = 0

    def read(self):

        pass

    def collect(self, save_data, thumbnail, save_id):

        print('collect')
        save_data.sys_svid = str(save_id)
        self.save_data[self.data_index] = save_data
        self.thumbnail_data[self.data_index] = thumbnail
        self.save_id = save_id
        self.data_index += 1
        print(self.save_data)
        print(self.thumbnail_data)

    def write(self):

        self.file = QFile(QDir().homePath() + '/.coda/save/save_data.xml')
        if self.file.open(QIODevice.WriteOnly) == False:
            print('Error Opening')
        else:
            print('Success')

            self.setDevice(self.file)
            self.setAutoFormatting(True)
            self.writeStartDocument()
            self.writeStartElement('save_data')
            write_index = 0
            for i in range(self.data_index):
                if self.save_data.get(i) != None:
                    self.writeStartElement('content')
                    self.writeAttribute('id', '{0}'.format(write_index))

                    self._write_bgm(self.save_data.get(i))
                    self._write_sd(self.save_data.get(i))
                    self._write_eff(self.save_data.get(i))
                    self._write_mk(self.save_data.get(i))
                    self._write_bg(self.save_data.get(i))
                    self._write_pt(self.save_data.get(i))
                    self._write_tb(self.save_data.get(i))
                    self._write_sl(self.save_data.get(i))
                    self._write_sys(self.save_data.get(i))

                    self.writeEndElement()
                    write_index += 1
            self.writeEndElement()
            self.writeEndDocument()

        self.file.close()

    def _write_bgm(self, data):

        if data.bgm_num == '':
            return

        for i in range(int(data.bgm_num)):
            self.writeStartElement('bgm')
            if data.bgm_pos.get(i) != None:
                self._write_element('pos', data.bgm_pos[i])
            if data.bgm_id.get(i) != None:
                self._write_element('id', data.bgm_id[i])
            if data.bgm_vol.get(i) != None:
                self._write_element('vol', data.bgm_vol[i])
            if data.bgm_md.get(i) != None:
                self._write_element('md', data.bgm_md[i])
            self.writeEndElement()

    def _write_sd(self, data):

        if data.sd_num == '':
            return

        for i in range(int(data.sd_num)):
            self.writeStartElement('sd')
            if data.sd_pos.get(i) != None:
                self._write_element('pos', data.sd_pos[i])
            if data.sd_id.get(i) != None:
                self._write_element('id', data.sd_id[i])
            if data.sd_md.get(i) != None:
                self._write_element('md', data.sd_md[i])
            if data.sd_lp.get(i) != None:
                self._write_element('lp', data.sd_lp[i])
            if data.sd_fd.get(i) != None:
                self._write_element('fd', data.sd_fd[i])
            if data.sd_dfd.get(i) != None:
                self._write_element('dfd', data.sd_dfd[i])
            self.writeEndElement()

    def _write_eff(self, data):

        if data.eff_id == '' and data.eff_du == '':
            return

        self.writeStartElement('eff')
        if data.eff_id != '':
            self._write_element('id', data.eff_id)
        if data.eff_du != '':
            self._write_element('du', data.eff_du)
        self.writeEndElement()

    def _write_mk(self, data):

        if data.mk_id == '' and data.mk_md == '':
            return

        self.writeStartElement('mk')
        if data.mk_id != '':
            self._write_element('id', data.mk_id)
        if data.mk_md != '':
            self._write_element('md', data.mk_md)
        self.writeEndElement()

    def _write_bg(self, data):

        if (data.bg_id == '' and data.bg_x == '' and data.bg_y == ''
                and data.bg_xf == '' and data.bg_yf == '' and data.bg_du == ''):
            return

        self.writeStartElement('bg')
        if data.bg_id != '':
            self._write_element('id', data.bg_id)
        if data.bg_x != '':
            self._write_element('x', data.bg_x)
        if data.bg_y != '':
            self._write_element('y', data.bg_y)
        if data.bg_xf != '':
            self._write_element('xf', data.bg_xf)
        if data.bg_yf != '':
            self._write_element('yf', data.bg_yf)
        if data.bg_du != '':
            self._write_element('du', data.bg_du)
        self.writeEndElement()

    def _write_pt(self, data):

        if data.pt_num == '':
            return

        for i in range(int(data.pt_num)):
            self.writeStartElement('pt')
            if data.pt_pos.get(i) != None:
                self._write_element('pos', data.pt_pos[i])
            if data.pt_id.get(i) != None:
                self._write_element('id', data.pt_id[i])
            if data.pt_md.get(i) != None:
                self._write_element('md', data.pt_md[i])
            if data.pt_x.get(i) != None:
                self._write_element('x', data.pt_x[i])
            if data.pt_y.get(i) != None:
                self._write_element('y', data.pt_y[i])
            if data.pt_xf.get(i) != None:
                self._write_element('xf', data.pt_xf[i])
            if data.pt_yf.get(i) != None:
                self._write_element('yf', data.pt_yf[i])
            if data.pt_du.get(i) != None:
                self._write_element('du', data.pt_du[i])
            self.writeEndElement()

    def _write_tb(self, data):

        if (data.tb_sh == '' and data.tb_td == '' and data.tb_vc == ''
                and data.tb_char == '' and data.tb_txt == '' and data.tb_hi == ''):
            return

        self.writeStartElement('tb')
        if data.tb_sh != '':
            self._write_element('sh', data.tb_sh)
        if data.tb_td != '':
            self._write_element('tb', data.tb_td)
        if data.tb_vc != '':
            self._write_element('vc', data.tb_vc)
        if data.tb_char != '':
            self._write_element('char', data.tb_char)
        if data.tb_txt != '':
            self._write_element('txt', data.tb_txt)
        if data.tb_hi != '':
            self._write_element('hi', data.tb_hi)
        self.writeEndElement()

    def _write_sl(self, data):

        pass

    def _write_sys(self, data):

        if data.sys_sc == '' and data.sys_scid == '' and data.sys_svid == '':
            return

        self.writeStartElement('sys')
        if data.sys_sc != '':
            self._write_element('sc', data.sys_sc)
        if data.sys_scid != '':
            self._write_element('scid', data.sys_scid)
        if data.sys_svid != '':
            self._write_element('svid', data.sys_svid)
        self.writeEndElement()

    def _write_element(self, element_id, character):

        self.writeStartElement(element_id)
        self.writeCharacters(str(character))
        self.writeEndElement()
