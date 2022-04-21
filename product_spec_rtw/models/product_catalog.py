# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_product_catalog(models.Model):
    _name = 'product.catalog'
    _description = 'catalog'
    _rec_name = "name"

    name = fields.Char('name')
