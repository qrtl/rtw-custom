# -*- coding: utf-8 -*-
from datetime import timedelta, datetime, time
from odoo import models, fields, api


class product_material_forecast(models.Model):
    _inherit = "product.template"

    po_count = fields.Integer(compute="_po_count")

    def _po_count(self):
        sumqty = 0
        for line in self:
            # self.po_count = self.env['purchase.order.line'].search_count([('product_id', '=', line.id)])
            order_lines = self.env['purchase.order.line'].search([
                ('product_id', '=', line.id),
                ('qty_received', '=', 0),
                ('order_id.state', 'in', ['done', 'purchase'])
            ]).filtered(lambda l: l.product_id.sudo().product_tmpl_id.type != 'service')
            for ol in order_lines:
                sumqty += ol.product_qty
            self.po_count = sumqty