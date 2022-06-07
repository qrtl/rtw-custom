# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_crm_relate(models.Model):
    _inherit = 'crm.lead'

    related_partners = fields.Many2many(
        comodel_name='res.partner',
        relation="crm_partner_rel",
        string="related_partners")

