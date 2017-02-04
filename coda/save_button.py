#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from coda.image_button import *

class SaveButton(ImageButton):
    '''this class provide save button functions'''

    def __init__(self, button_name, save_button_id, parent):
        super().__init__(button_name, parent)

        self.id = save_button_id
        self.sid = ''

    def set_sid(self, sid):

        self.sid = sid
