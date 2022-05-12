# -*- coding: utf-8 -*-

from odoo import models, fields, api


class opportunity(models.Model):
    _name = 'rtw_sf.business_process'
    _description = 'rtw_sf.business_process'
    _rec_name = "name"

    name = fields.Char("Name")
    description = fields.Char("Description")
    table_enum_or_id = fields.Char("TableEnumOrId")
    created_date = fields.Datetime('CreatedDate')  # 作成日 Y列
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID Z列
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日
    last_modified_by_id = fields.Many2one('res.users', 'LastModifiedById')  # 最終更新者
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日
