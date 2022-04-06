# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_partner(models.Model):
    _inherit = "res.partner"

    fax = fields.Char(string="fax")  # Z
    field4__c = fields.Char('send')  # BH
    channel = fields.Many2one('res.partner.channel')

