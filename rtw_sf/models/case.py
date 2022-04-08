# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_case(models.Model):
    _name = 'rtw_sf_case'
    _description = 'case'
    _rec_name = "subject"

    subject = fields.Char('Subject')
    contacts = fields.Many2one('res.partner', "Contact", copy=False)

