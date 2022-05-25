# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_old_message_crm_lead(models.Model):
    _inherit = 'utm.campaign'
    currency_id = fields.Many2one(related="company_id.currency_id", readonly=True)

    parent_id = fields.Many2one('utm.campaign', string="utm.campaign")
    start_date = fields.Datetime('StartDate')

    currency_id = fields.Many2one('res.currency', string='Currency',
                                  required=True, readonly=True,
                                  states={'draft': [('readonly', False)]},
                                  default=lambda
                                      self: self.env.company.currency_id.id)
    budgeted_cost = fields.Monetary(
        string="BudgetedCost",
        default=0.0,
        currency_field="currency_id",
    )
    actual_cost = fields.Monetary(
        string="ActualCost",
        default=0.0,
        currency_field="currency_id",
    )
    description = fields.Text("Description")
    amount_all_opportunities = fields.Monetary(
        string="AmountAllOpportunities",
        default=0.0,
        currency_field="currency_id",
    )
    amount_won_opportunities = fields.Monetary(
        string="AmountWonOpportunities",
        currency_field="currency_id",
        default=0.0,
    )