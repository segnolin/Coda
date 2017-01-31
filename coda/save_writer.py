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
                self.writeStartElement('pos')
                self.writeCharacters(data.bgm_pos[i])
                self.writeEndElement()
            if data.bgm_id.get(i) != None:
                self.writeStartElement('id')
                self.writeCharacters(data.bgm_id[i])
                self.writeEndElement()
            if data.bgm_vol.get(i) != None:
                self.writeStartElement('vol')
                self.writeCharacters(data.bgm_vol[i])
                self.writeEndElement()
            if data.bgm_md.get(i) != None:
                self.writeStartElement('md')
                self.writeCharacters(data.bgm_md[i])
                self.writeEndElement()
            self.writeEndElement()

    def _write_sd(self, data):

        if data.sd_num == '':
            return

        for i in range(int(data.sd_num)):
            self.writeStartElement('sd')
            if data.sd_pos.get(i) != None:
                self.writeStartElement('pos')
                self.writeCharacters(data.sd_pos[i])
                self.writeEndElement()
            if data.sd_id.get(i) != None:
                self.writeStartElement('id')
                self.writeCharacters(data.sd_id[i])
                self.writeEndElement()
            if data.sd_md.get(i) != None:
                self.writeStartElement('md')
                self.writeCharacters(data.sd_md[i])
                self.writeEndElement()
            if data.sd_lp.get(i) != None:
                self.writeStartElement('lp')
                self.writeCharacters(data.sd_lp[i])
                self.writeEndElement()
            if data.sd_fd.get(i) != None:
                self.writeStartElement('fd')
                self.writeCharacters(data.sd_fd[i])
                self.writeEndElement()
            if data.sd_dfd.get(i) != None:
                self.writeStartElement('dfd')
                self.writeCharacters(data.sd_dfd[i])
                self.writeEndElement()
            self.writeEndElement()

    def _write_eff(self, data):

        if data.eff_id == '' and data.eff_du == '':
            return

        self.writeStartElement('eff')
        if data.eff_id != '':
            self.writeStartElement('id')
            self.writeCharacters(data.eff_id)
            self.writeEndElement()
        if data.eff_du != '':
            self.writeStartElement('du')
            self.writeCharacters(data.eff_du)
            self.writeEndElement()
        self.writeEndElement()

    def _write_mk(self, data):

        if data.mk_id == '' and data.mk_md == '':
            return

        self.writeStartElement('mk')
        if data.mk_id != '':
            self.writeStartElement('id')
            self.writeCharacters(data.mk_id)
            self.writeEndElement()
        if data.mk_md != '':
            self.writeStartElement('md')
            self.writeCharacters(data.mk_md)
            self.writeEndElement()
        self.writeEndElement()

    def _write_bg(self, data):

        if (data.bg_id == '' and data.bg_x == '' and data.bg_y == ''
                and data.bg_xf == '' and data.bg_yf == '' and data.bg_du == ''):
            return

        self.writeStartElement('bg')
        if data.bg_id != '':
            self.writeStartElement('id')
            self.writeCharacters(data.bg_id)
            self.writeEndElement()
        if data.bg_x != '':
            self.writeStartElement('x')
            self.writeCharacters(str(data.bg_x))
            self.writeEndElement()
        if data.bg_y != '':
            self.writeStartElement('y')
            self.writeCharacters(str(data.bg_y))
            self.writeEndElement()
        if data.bg_xf != '':
            self.writeStartElement('xf')
            self.writeCharacters(str(data.bg_xf))
            self.writeEndElement()
        if data.bg_yf != '':
            self.writeStartElement('yf')
            self.writeCharacters(str(data.bg_yf))
            self.writeEndElement()
        if data.bg_du != '':
            self.writeStartElement('du')
            self.writeCharacters(str(data.bg_du))
            self.writeEndElement()
        self.writeEndElement()

    def _write_pt(self, data):

        if data.pt_num == '':
            return

        for i in range(int(data.pt_num)):
            self.writeStartElement('pt')
            if data.pt_pos.get(i) != None:
                self.writeStartElement('pos')
                self.writeCharacters(data.pt_pos[i])
                self.writeEndElement()
            if data.pt_id.get(i) != None:
                self.writeStartElement('id')
                self.writeCharacters(data.pt_id[i])
                self.writeEndElement()
            if data.pt_md.get(i) != None:
                self.writeStartElement('md')
                self.writeCharacters(data.pt_md[i])
                self.writeEndElement()
            if data.pt_x.get(i) != None:
                self.writeStartElement('x')
                self.writeCharacters(data.pt_x[i])
                self.writeEndElement()
            if data.pt_y.get(i) != None:
                self.writeStartElement('y')
                self.writeCharacters(data.pt_y[i])
                self.writeEndElement()
            if data.pt_xf.get(i) != None:
                self.writeStartElement('xf')
                self.writeCharacters(data.pt_xf[i])
                self.writeEndElement()
            if data.pt_yf.get(i) != None:
                self.writeStartElement('yf')
                self.writeCharacters(data.pt_yf[i])
                self.writeEndElement()
            if data.pt_du.get(i) != None:
                self.writeStartElement('du')
                self.writeCharacters(data.pt_du[i])
                self.writeEndElement()
            self.writeEndElement()

    def _write_tb(self, data):

        if (data.tb_sh == '' and data.tb_td == '' and data.tb_vc == ''
                and data.tb_char == '' and data.tb_txt == '' and data.tb_hi == ''):
            return

        self.writeStartElement('tb')
        if data.tb_sh != '':
            self.writeStartElement('sh')
            self.writeCharacters(data.tb_sh)
            self.writeEndElement()
        if data.tb_td != '':
            self.writeStartElement('td')
            self.writeCharacters(data.tb_td)
            self.writeEndElement()
        if data.tb_vc != '':
            self.writeStartElement('vc')
            self.writeCharacters(data.tb_vc)
            self.writeEndElement()
        if data.tb_char != '':
            self.writeStartElement('char')
            self.writeCharacters(data.tb_char)
            self.writeEndElement()
        if data.tb_txt != '':
            self.writeStartElement('txt')
            self.writeCharacters(data.tb_txt)
            self.writeEndElement()
        if data.tb_hi != '':
            self.writeStartElement('hi')
            self.writeCharacters(data.tb_hi)
            self.writeEndElement()
        self.writeEndElement()

    def _write_sl(self, data):

        pass

    def _write_sys(self, data):

        if data.sys_sc == '' and data.sys_scid == '' and data.sys_svid == '':
            return

        self.writeStartElement('sys')
        if data.sys_sc != '':
            self.writeStartElement('sc')
            self.writeCharacters(data.sys_sc)
            self.writeEndElement()
        if data.sys_scid != '':
            self.writeStartElement('scid')
            self.writeCharacters(data.sys_scid)
            self.writeEndElement()
        if data.sys_svid != '':
            self.writeStartElement('svid')
            self.writeCharacters(data.sys_svid)
            self.writeEndElement()
        self.writeEndElement()
