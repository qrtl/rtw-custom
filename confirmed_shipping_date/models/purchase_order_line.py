# -*- coding: utf-8 -*-

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "purchase.order.line"

    confirmed_shipping_date = fields.Date(
        "Confirmed shipping Date",
        store=True,
    )
