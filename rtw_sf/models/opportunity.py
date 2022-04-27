# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_opportunity(models.Model):
    _name = 'opportunity'
    _description = 'case'
    _rec_name = "subject"