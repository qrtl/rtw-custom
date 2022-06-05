# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class event_rtw(models.Model):
    _name = 'calendar.sr'
    _description = 'calendar.sr'

    name = fields.Char('name')
    user_ids = fields.Many2one('res.users')
