# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_crm_role(models.Model):
    _name = 'rtw_crm_role'
    _description = 'rtw_crm_role'
    _rec_name = "contact_id"
    
    opportunity_id = fields.Many2one('crm.lead', 'OpportunityId')
    contact_id = fields.Many2one('res.user', 'ContactId')
    role = fields.Selection([
        ('1', '意思決定者'),
        ('2', '業務担当者'),
        ('3', '有力者'),
        ('4', '技術担当者'),
        ('5', '予算決定者'),
        ('6', '予算担当者'),
        ('7', '評価者'),
        ('8', '発注担当者'),
        ('9', '担当役員'),
        ('10', '商品選定者'),
        ('11', '設計担当者'),
        ('12', '主担当'),
        ('13', 'その他'),
    ], default='',
        string="Role")
    created_date = fields.Datetime('CreatedDate')  # 作成日 AM列
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID AN列
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日 AO列
    last_modified_by_id = fields.Many2one('res.users', 'LastModifiedById')  # 最終更新者 AP列
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日 AQ列
