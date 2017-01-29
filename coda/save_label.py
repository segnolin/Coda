#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from coda.image_button import *

class SaveLabel(ImageButton):
    '''this class provide save label functions'''

    def __init__(self, label_name, save_label_id, parent):
        super().__init__(label_name, parent)

        self.id = save_label_id
