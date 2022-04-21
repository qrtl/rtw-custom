# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_case(models.Model):
    _name = 'rtw_sf_case'
    _description = 'case'
    _rec_name = "subject"

    partner_ids = fields.Many2one('res.partner')
    subject = fields.Char('Subject')
    contacts = fields.Many2one('res.partner', "Contact", copy=False)  # コンタクト
    accounts = fields.Many2one('res.partner', "Account", copy=False)  # アカウント
    parents = fields.Many2one('rtw_sf_case', "Parents", copy=False)  # 親ケース
