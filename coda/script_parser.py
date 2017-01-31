#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.script_resources

from coda.data import *
from coda.parser import *

class ScriptParser(Parser):

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
                        self.parse_xml()
                        break
