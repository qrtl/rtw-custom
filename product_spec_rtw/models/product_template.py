# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductSpecRtw(models.Model):
    _inherit = "product.template"
    _description = 'product_spec_rtw.product_spec_rtw'
    summary = fields.Char(
        name="summary",
        string="summary"
    )
    product_no = fields.Char(
        name="product_no",
        string="product no"
    )
    width = fields.Integer(
        name="width",
        string="width"
    )
    height = fields.Integer(
        name="height",
        string="height"
    )
    depth = fields.Integer(
        name="depth",
        string="depth"
    )
    sh = fields.Integer(
        name="sh",
        string="sheet height"
    )

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = 'print_description'
    print_description = fields.Text(name="print_description", string="print description")

    @api.onchange('product_id', 'config_session_id')
    def product_id_change(self):
        if self.product_id:
            res = super(SaleOrderLine, self).product_id_change()
            string = ""
            if self.product_id.product_no != False:
                string += '品番/' + str(self.product_id.product_no) + '\n'
            if self.product_id.height > 0:
                string += 'H/' + str(self.product_id.height) + 'mm\n'
            if self.product_id.depth > 0:
                string += 'D/' + str(self.product_id.depth) + 'mm\n'
            if self.product_id.width > 0:
                string += 'w/' + str(self.product_id.width) + 'mm\n'
            self.print_description = string
            return res

