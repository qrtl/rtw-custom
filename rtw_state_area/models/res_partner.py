# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_res_partner_area(models.Model):
    _inherit = 'res.partner'

    rel_region = fields.Char(related="state_id.name")

