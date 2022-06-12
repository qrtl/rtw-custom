# -*- coding: utf-8 -*-

from odoo import models, fields, api


class meisai(models.Model):
    _name = 'meisai.meisai'
    _description = 'meisai.meisai'

    name = fields.Char('Name')  # 件名 C列
    # record_type_id = fields.Text('RecordTypeId')  # D列 ★１つのIDのみ
    created_date = fields.Datetime('CreatedDate')  # 作成日 E列
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID F列
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日 G列
    last_modified_by_id = fields.Many2one('res.users', 'LastModifiedById')  # 最終更新者 H列
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日 I列
    date = fields.Datetime('Field1__c')  # 日付 J列
    category = fields.Char('Field16__c')  # カテゴリ K列
    purpose = fields.Char('Field3__c')  # 目的/訪問先 L列
    order_no = fields.Char('Field4__c')  # 注番 M列
    sf_no = fields.Char('S_F__c')  # S/F番号 N列
    payee = fields.Char('Field5__c')  # 交通機関/領収書名 O列　
    interval_departure = fields.Char('Field6__c')  # 区間（出発） P列
    interval_arrival = fields.Char('Field7__c')  # 区間（到着） Q列
    amount = fields.Float('Field8__c')  # 金額 R列
    # lodging_expense = fields.Float('Field9__c')  # 宿泊費 S列 ★空白のみ
    # business_trip_start_date = fields.Datetime('Field10__c')  # 出張開始日 T列 ★空白のみ
    # business_trip_end_date = fields.Datetime('Field11__c')  # 出張終了日 U列 ★空白のみ
    # lodging_count = fields.Integer('Field12__c')  # 宿泊数 V列 ★空白のみ
    # daily_allowance = fields.Float('Field13__c')  # 日当 W列 ★空白のみ
    # product_name = fields.Char('shouhinmei__c')  # 商品名 X列 ★空白のみ
    # place_of_business = fields.Char('Field14__c')  # 出張先 Y列 ★空白のみ
    # maker = fields.Char('maker__c')  # メーカー/品番 Z列 ★空白のみ
    # list_price = fields.Float('teika__c')  # 定価 AA列 ★空白のみ
    # volume = fields.Float('suuryou__c')  # 数量 AB列 ★空白のみ
    application_id = fields.Char('Field15__c')  # 経費精算・申請ID AC列

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
