# -*- coding: utf-8 -*-
import time
import datetime
from odoo import models, fields, api


class calendar_event_rtw(models.Model):
    _inherit = 'crm.lead'

    last_event = fields.Datetime(compute="_last_event", store=True)
    event_showroom = fields.Char(store=True)

    @api.depends('calendar_ids')
    def _last_event(self):
        # print("a", self)
        for rec in self:
            if rec.calendar_ids:
                i = 0
                for l in rec.calendar_ids:
                    if i == 0:
                        start = l.start
                        showroom = l.sr.name
                        i = 1
                    elif start and l.start > start:
                        start = l.start
                        showroom = l.sr.name
                rec.last_event = start
                rec.event_showroom = showroom
            else:
                rec.last_event = False
