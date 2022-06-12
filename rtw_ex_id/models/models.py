# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rtw_ex_id(models.Model):
#     _name = 'rtw_ex_id.rtw_ex_id'
#     _description = 'rtw_ex_id.rtw_ex_id'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
