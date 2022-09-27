# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_purchase(models.Model):
    _inherit = "purchase.order"

    # @api.model
    def action_purchase_form(self):
        self.ensure_one()
        action = self.env.ref("purchase.purchase_form_action")
        form = self.env.ref("purchase.purchase_order_form")
        action = action.read()[0]
        action["views"] = [(form.id, "form")]
        action["target"] = "new"
        action["res_id"] = self.id
        return action
