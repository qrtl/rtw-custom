# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_crm_inq(models.Model):
    _inherit = 'crm.lead'

    role_ids = fields.One2many('rtw_crm_role', inverse_name='opportunity_id')