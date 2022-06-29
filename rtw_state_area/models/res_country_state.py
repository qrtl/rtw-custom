# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_country_state(models.Model):
    _inherit = 'res.country.state'

    area = fields.Selection([
        ('1', '関東'),
        ('2', '北関東'),
        ('3', '東北・北海道'),
        ('4', '甲信越'),
        ('5', '東海'),
        ('6', '北陸'),
        ('7', '関西'),
        ('8', '中国'),
        ('9', '四国'),
        ('10', '九州・沖縄'),
    ], default='',
        string="area")
