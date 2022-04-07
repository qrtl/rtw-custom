# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_partner(models.Model):
    _inherit = "res.partner"
    _description = 'Account.csv'

    fax = fields.Char(string="fax")  # X
    # contact_type = fields.Many2one('res.partner.contact_type')  # E
    channel = fields.Many2one('res.partner.channel')  # BG

