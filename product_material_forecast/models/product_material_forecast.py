# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_material_forecast(models.Model):
    _inherit = "product.template"

    po_count = fields.Integer(compute="_po_count")

    def _po_count(self):
        for line in self:
            print(line.id)
            self.po_count = self.env['purchase.order.line'].search_count([('product_id', '=', line.id)])
