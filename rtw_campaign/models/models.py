# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rtw_campaign(models.Model):
#     _name = 'rtw_campaign.rtw_campaign'
#     _description = 'rtw_campaign.rtw_campaign'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
