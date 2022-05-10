# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contract(models.Model):
    _name = 'rtw_sf.inquiry'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin'
    ]
    _description = 'inquiry'


