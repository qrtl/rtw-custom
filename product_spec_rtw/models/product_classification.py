# Copyright (C) 2021 Picg

from odoo import api, fields, models


class ProductClassification(models.Model):
    _name = "product.classification"
    _description = "Classification"
    # _rec_name = "combination"
    name = fields.Char("name")
