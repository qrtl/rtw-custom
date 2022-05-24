# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_old_message_crm_lead(models.Model):
    _inherit = 'utm.campaign'

    parent_id = fields.Many2one('utm.campaign', string="utm.campaign")
    start_date = fields.Datetime('StartDate')
    budgeted_cost = fields.Monetary(
        string="BudgetedCost",
        default=0.0,
    )
    actual_cost = fields.Monetary(
        string="ActualCost",
        default=0.0,
    )
    description = fields.Text("Description")
    amount_all_opportunities = fields.Monetary(
        string="AmountAllOpportunities",
        default=0.0,
    )
    amount_won_opportunities = fields.Monetary(
        string="AmountWonOpportunities",
        default=0.0,
    )