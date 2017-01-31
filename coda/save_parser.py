#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *

from coda.data import *
from coda.parser import *

class SaveParser(Parser):

    def __init__(self):
        super().__init__()

    def parse_num(self):

        self.file = QFile(QDir().homePath() + '/.coda/save/save_data.xml')
        self.file.open(QIODevice.ReadOnly)
        self.setDevice(self.file)

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'save_data':
                    return self.attributes().value('num')

    def parse(self, content_id):

        self.data = Data()

        self.file = QFile(QDir().homePath() + '/.coda/save/save_data.xml')
        self.file.open(QIODevice.ReadOnly)
        self.setDevice(self.file)

        while not self.atEnd():
            self.readNext()
            if self.isStartElement():
                if self.name() == 'content':
                    if self.attributes().value('id') == str(content_id):
                        self.parse_xml()
                        break
