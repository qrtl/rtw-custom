# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_order_line_rtw(models.Model):
    _inherit = "sale.order.line"

    memo = fields.Char('memo')
