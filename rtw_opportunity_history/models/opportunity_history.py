# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_opportunity_history(models.Model):
    _name = 'rtw_opportunity_history'
    _description = 'rtw_opportunity_history'

    phase = fields.Char("phase")
    amount = fields.Float("Amount")
    crm_id = fields.Many2one("crm.lead", string="OpportunityId")
    probability = fields.Integer("Probability")
    close_date = fields.Datetime("CloseDate")
    created_date = fields.Datetime('CreatedDate')  # 作成日 AM列
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID AN列
    currency_id = fields.Many2one('res.currency', string='Currency',
                                  required=True, readonly=True,
                                  default=lambda
                                      self: self.env.company.currency_id.id)
