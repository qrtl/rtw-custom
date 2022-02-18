# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_order_rtw(models.Model):
    _inherit = "sale.order"
    _description = 'sale_order_rtw.sale_order_rtw'
    status = fields.Selection([
        ('draft', 'draft'),
        ('done', 'done')
    ],
        string="status", default='draft')
    preferred_delivery_date = fields.Date(string="Preferred delivery date")
    preferred_delivery_period = fields.Char(string="Preferred delivery period")
    forwarding_address = fields.Many2one(
        comodel_name="res.partner",
        string="forwarding address",
        required=False,
        ondelete="set null",
    )
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
