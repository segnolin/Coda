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
        self.data_index += 1

    def write(self):

        self.file = QFile(QDir().homePath() + '/.coda/save/save_data.xml')
        if self.file.open(QIODevice.WriteOnly) == False:
            print('Error Opening')
        else:
            print('Success')

        '''
            self.setDevice(self.file)
            self.setAutoFormatting(True)
            self.writeStartDocument()
            self.writeStartElement('save_data')
            for i in range(5):
                self.writeStartElement('content')
                self.writeAttribute('id', '{0}'.format(i))
                self.writeStartElement('sd')
                self.writeStartElement('pos')
                self.writeCharacters('0')
                self.writeEndElement()
                self.writeStartElement('id')
                self.writeCharacters('sd_object_door_metal_close_01')
                self.writeEndElement()
                self.writeStartElement('md')
                self.writeCharacters('new')
                self.writeEndElement()
                self.writeEndElement()
                self.writeStartElement('sd')
                self.writeStartElement('pos')
                self.writeCharacters('1')
                self.writeEndElement()
                self.writeStartElement('id')
                self.writeCharacters('sd_object_door_metal_open_02')
                self.writeEndElement()
                self.writeStartElement('md')
                self.writeCharacters('new')
                self.writeEndElement()
                self.writeEndElement()
                self.writeEndElement()
            self.writeEndDocument()
        '''

        self.file.close()
