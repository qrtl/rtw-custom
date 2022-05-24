# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_old_message_crm_lead(models.Model):
    _inherit = 'crm.lead'

    old_messages = fields.Many2one(comodel_name="rtw.old_message",
                                   compute="_compute_message_ids",
                                   string="old message",
                                   readonly=True,)

    # @api.depends("id")
    def _compute_message_ids(self):
        for record in self:
            full_id = record.get_metadata()[0].get("xmlid")
            xml_id = full_id.split('.')[1]
            print(xml_id)
            record.old_messages = self.env['rtw.old_message'].search([('parent_id', '=', xml_id)])
