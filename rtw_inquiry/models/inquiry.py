# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contract(models.Model):
    _name = 'rtw_sf.inquiry'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin'
    ]
    _description = 'inquiry'
    _rec_name = "name"

    owner_id = fields.Many2one('res.users', 'OwnerId')  # 所有者Id
    name = fields.Chae('Name')
    record_type_id = fields.Many2one('rtw_sf.record_type', 'RecordTypeId')  # レコードタイプId AH列
    created_date = fields.Datetime('CreatedDate')  # 作成日 AM列
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID AN列
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日 AO列
    last_modified_by_id = fields.Many2one('res.users', 'LastModifiedById')  # 最終更新者 AP列
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日 AQ列
    last_activity_date = fields.Datetime('LastActivityDate')  # システム最終活動日 AR列　★空白のみ
    no = fields.Char('NO__c')  # 問い合わせNo
    vendor = fields.Char('Field36__c')  # 納品業者
    # campaign = fields.Many2one()  # キャンペーン
    lead_source = fields.Char(string="Field1__c")  # リードソース
    broad_category = fields.Selection([
        ('event_sale', 'イベント・セール'),
        ('catalog', 'カタログ依頼（メール・ＦＡＸ）'),
        ('claim', 'クレーム'),
        ('show_room', 'ショールーム'),
        ('other', 'その他'),
        ('campaign', '広報・キャンペーン関連'),
        ('buy_method', '購入方法'),
        ('merchandise', '商品関連'),
        ('delivery_problems', '納品トラブル'),
        ('delivery_related', '納品関連')
    ], string="Field2__c",
     default='')  # 大分類 OK
    support = fields.Selection([
        ('1', 'ＳＲ予約'),
        ('2', 'カタログ送付'),
        ('3', 'サンプル送付'),
        ('4', 'その他'),
        ('5', 'ソファ'),
        ('6', 'ダイニングテーブル'),
        ('7', 'チェア'),
        ('8', 'ボード'),
        ('9', 'メール回答完了'),
        ('10', 'メンテナンスキット紹介'),
        ('11', 'メンテナンスキット販売'),
        ('12', 'リビングテーブル'),
        ('13', '営業引継ぎ'),
        ('14', '営業日・営業時間'),
        ('15', '見積り依頼'),
        ('16', '商品資料送付'),
        ('17', '注文（受注）'),
        ('18', '注文書送付'),
        ('19', '電話回答完了'),
        ('20', '納品日決定'),
        ('21', '納品日変更'),
        ('22', '訪問'),
    ], string="Field3__c",
     default='')   # 対応
    product_name1 = fields.Char("Field37__c")
