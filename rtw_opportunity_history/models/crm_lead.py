# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_crm(models.Model):
    _inherit = 'crm.lead'

    opportunity_history_ids = fields.One2many("rtw_opportunity_history", "crm_id", string="opportunity history")