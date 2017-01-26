#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Data(object):

    def __init__(self):
        super().__init__()

        self.bgm_pos = {}
        self.bgm_id = {}
        self.bgm_md = {}
        self.bgm_vol = {}
        self.bgm_num = 0

        self.sd_pos = {}
        self.sd_id = {}
        self.sd_md = {}
        self.sd_lp = {}
        self.sd_fd = {}
        self.sd_dfd = {}
        self.sd_num = 0

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
