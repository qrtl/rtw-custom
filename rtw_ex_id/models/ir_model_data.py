# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_crm(models.Model):
    _inherit = 'ir.model.data'

    del_flag = fields.Boolean("del_flag")
