#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.system_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from coda.image_button import *
from coda.fader import *
from coda.save_button import *
from coda.page import *
from coda.save_writer import *

class Save(QMainWindow):
    '''this class creates game save layout and functions'''

    def __init__(self):
        super().__init__()

        self.pixel_ratio = QWindow().devicePixelRatio()
        self.save_id = ''
        self.state = ''
        self.delete_save = False

    def create_save_layout(self):

        #set QWidget class
        self.save_widget = QWidget()

        #set save page background
        self.background = QLabel(self.save_widget)
        self.background_pixmap = QPixmap(':/sys/save_background.png')
        self.background_pixmap = self.background_pixmap.scaledToHeight(
                self.background_pixmap.height() * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.background_pixmap.setDevicePixelRatio(self.pixel_ratio)
        self.background.setPixmap(self.background_pixmap)
        self.background.setGeometry(0, 0, 1024, 576)

        #create page layout
        self.page = {}
        for i in range(6):
            self.page[i] = Page(self.save_widget)
            self.page[i].create_page_layout(i)
            self.page[i].hide()
            for j in range(6):
                self.page[i].label[j].clicked.connect(self._action)
        self.page[0].show()

        #create save page button
        self.page_background = {}
        self.save_page = {}
        for i in range(6):
            self.page_background[i] = QLabel(self.save_widget)
            self.page_background[i].setGeometry(704 + i * 40, 25, 36, 36)
            self.page_background[i].setStyleSheet(
                    'QLabel { background-color: white;\
                            border-radius: 6px; }')
            self.page_background[i].hide()
        self.page_background[0].show()

        for i in range(6):
            self.save_page[i] = SaveButton(
                    'save_{0}'.format(i + 1), i, self.save_widget)
            self.save_page[i].setGeometry(704 + i * 40, 25, 36, 36)
            self.save_page[i].clicked.connect(self._change_page)

        #modify delete button
        for i in range(6):
            for j in range(6):
                self.page[i].delete[j].clicked.connect(self._delete)
                self.page[i].delete[j].hide()

        #create back button
        self.save_back_button = ImageButton('save_back', self.save_widget)
        self.save_back_button.setGeometry(844, 490, 96, 32)

        #create save writer
        self.save_writer = SaveWriter()

        #write data connection
        self.save_back_button.clicked.connect(self._write_data)

    def add_save(self, save_data, thumbnail):

        self.save_id = ''
        self.state = 'save'
        self.save_data = save_data
        self.thumbnail = thumbnail
        self.save_writer.read()
        self._set_page()
        self.delete_save = False

    def load(self):

        self.state = 'load'
        self.save_writer.read()
        self._set_page()
        self.delete_save = False

    def _set_page(self):

        for i in range(self.save_writer.data_index):
            data = self.save_writer.save_data[i]
            thumbnail = self.save_writer.thumbnail_data[i]
            j = int(data.sys_svid)
            self.page[int(j / 6)].thumbnail[
                    int(j % 6)].setPixmap(thumbnail)
            self.page[int(j / 6)].text_preview[
                    int(j % 6)].setText(data.tb_txt)
            if self.state == 'save':
                self.page[int(j / 6)].label[
                        int(j % 6)].setEnabled(False)
            elif self.state == 'load':
                self.page[int(j / 6)].label[
                        int(j % 6)].setEnabled(True)
            self.page[int(j / 6)].delete[
                    int(j % 6)].show()
            self.page[int(j / 6)].label[
                    int(j % 6)].set_sid(i)
            self.page[int(j / 6)].delete[
                    int(j % 6)].set_sid(i)

    def _action(self):

        if self.state == 'save':
            self._save()
        elif self.state == 'load':
            self._write_data()

    def _save(self):

        self.fader = Fader(self.save_widget, self.save_widget)
        self.fader.fade(200)

        if self.save_id != '':
            self._clear_save(self.save_id)

        self.save_id = self.sender().id
        print(self.save_id)

        self.thumbnail = self.thumbnail.scaledToHeight(216 * self.pixel_ratio / 2,
                Qt.SmoothTransformation)
        self.page[int(self.save_id / 6)].thumbnail[
                int(self.save_id % 6)].setPixmap(self.thumbnail)
        self.page[int(self.save_id / 6)].text_preview[
                int(self.save_id % 6)].setText(self.save_data.tb_txt)
        self.page[int(self.save_id / 6)].label[
                int(self.save_id % 6)].setEnabled(False)
        self.page[int(self.save_id / 6)].delete[
                int(self.save_id % 6)].show()

    def _delete(self):

        print('delete')
        save_id = self.sender().id
        save_sid = self.sender().sid

        if save_id == self.save_id and self.state == 'save':
            self.save_id = ''
        else:
            print('del')
            self.save_writer.save_data.pop(save_sid)
            self.save_writer.thumbnail_data.pop(save_sid)
            self.delete_save = True

        self._clear_save(save_id)

    def _change_page(self):

        page = self.sender().id
        print(page)

        self.fader = Fader(self.save_widget, self.save_widget)
        self.fader.fade(200)

        for i in range(6):
            self.page[i].hide()
            self.page_background[i].hide()
        self.page[page].show()
        self.page_background[page].show()

    def _write_data(self):

        print('write data')
        print(self.save_id)
        if self.save_id != '' and self.state == 'save':
            self.save_writer.collect(self.save_data, self.thumbnail, self.save_id)
            self.save_writer.write()
        elif self.delete_save == True:
            self.save_writer.write()

    def _clear_save(self, save_id):

        self.fader = Fader(self.save_widget, self.save_widget)
        self.fader.fade(200)

        self.page[int(save_id / 6)].thumbnail[
                int(save_id % 6)].clear()
        self.page[int(save_id / 6)].text_preview[
                int(save_id % 6)].clear()
        self.page[int(save_id / 6)].label[
                int(save_id % 6)].setEnabled(True)
        self.page[int(save_id / 6)].delete[
                int(save_id % 6)].hide()
        self.page[int(save_id / 6)].label[
                int(save_id % 6)].set_sid('')
        self.page[int(save_id / 6)].delete[
                int(save_id % 6)].set_sid('')
