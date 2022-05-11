# -*- coding: utf-8 -*-

from odoo import models, fields, api


class record_type(models.Model):
    _name = 'rtw_sf.record_type'
    _description = 'rtw_sf.record_type'

    name = fields.Char("Name")
    description = fields.Char("Description")
    businessprocessId = fields.Many2one("rtw_sf.business_process", "BusinessProcessId")
    sobjecttype = fields.Char("SobjectType")
    isactive = fields.Boolean("IsActive")
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID Z列
    created_date = fields.Datetime('CreatedDate')  # 作成日 Y列
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日
    last_modified_by_id = fields.Many2one('res.users', 'LastModifiedById')  # 最終更新者
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日
