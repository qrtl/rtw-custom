# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductSpecRtw(models.Model):
    _inherit = "partner.delivery.zone"
    _description = 'partner.delivery.zone_extend'

    coefficient = fields.Integer("coefficient")
