# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_partner_channel(models.Model):
    _name = 'res.partner.channel'
    _description = 'rtw_sf.partner_channel'
    _rec_name = "name"

    name = fields.Char('channel')
