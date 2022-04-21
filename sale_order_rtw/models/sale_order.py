# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_order_rtw(models.Model):
    _inherit = "sale.order"
    _description = 'sale_order_rtw.sale_order_rtw'
    title = fields.Char('title')
    status = fields.Selection([
        ('draft', 'draft'),
        ('done', 'done')
    ],
        string="status", default='draft')
    process = fields.Selection([
        ('draft', 'draft'),
        ('manufactured', 'manufactured'),
        ('delivered', 'delivered'),
    ],
        string="status", default='draft')
    preferred_delivery_date = fields.Date(string="Preferred delivery date", tracking=True)
    preferred_delivery_period = fields.Char(string="Preferred delivery period")

    forwarding_address = fields.Many2one(
        comodel_name="res.partner",
        string="forwarding address",
        required=False,
        ondelete="set null",
    )
    shiratani_entry_date = fields.Date(string="Shiratani entry Date")
    depo_date = fields.Date(string="Depo Date")
    customer_order_number = fields.Char('Customer Order Number')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
