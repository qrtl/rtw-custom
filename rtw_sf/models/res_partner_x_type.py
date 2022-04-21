# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_partner_x_type(models.Model):
    _name = 'res.partner.contact_type'
    _description = 'res.partner.contact_type'
    _rec_name = "name"

    name = fields.Char('type')
