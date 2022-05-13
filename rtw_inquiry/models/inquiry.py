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
    product_name1 = fields.Char("Field37__c")  # ①商品名
    product_name2 = fields.Char("Field38__c")  # ②商品名
    product_name3 = fields.Char("Field39__c")  # ③商品名
    product_name4 = fields.Char("Field40__c")  # ④商品名
    product_name5 = fields.Char("Field41__c")  # ⑤商品名
    product_name6 = fields.Char("Field42__c")  # ⑥商品名
    contact_person = fields.Many2one("res.partner", 'contact_person__c')  # 取引先担当者
    accounts = fields.Many2one("res.partner", 'Contact__c')  # 取引先
    summary = fields.Text("Field6")  # 概要
    customer_testimonials = fields.Text("Field7_voice__c")  # お客様の声
    satisfaction_level = fields.Selection([
        ('5', '大変満足'),
        ('4', 'やや満足'),
        ('3', '普通'),
        ('2', 'やや不満'),
        ('1', '大変不満'),
    ], string="Satisfactionlevel_2018__c",
     default='')  # 商品の満足度
    name_of_magazine_other = fields.Char("Field8__c")  # 雑誌名（その他）
    situation = fields.Selection([
        ('buy', '購入後'),
        ('not_buy', '購入前'),
    ], string="Field9__c",
     default='')  # 状況
    magazine_site = fields.Selection([
        ('1', 'モダンリビング'),
        ('2', 'エルデコ'),
        ('3', "I'm home"),
        ('4', '商店建築'),
        ('5', 'シグネチャー'),
        ('6', 'ゲーテ'),
        ('7', 'Pen'),
        ('8', 'Passione'),
        ('9', 'ONLINEサイト'),
        ('10', 'その他'),
        ('11', '不明'),
    ], string="Field7__c",
     default='')  # 雑誌／サイト名
    proposal_to_send_catalog = fields.Boolean('Field10_teian__c', default=0)  # カタログ送付提案
    sr_attracting = fields.Boolean('Field10_sr__c', default=0)  # ＳＲ誘致
    confirm_user_information = fields.Boolean('Field10_user__c', default=0)  # ユーザー情報確認
    event_information_notices = fields.Boolean('Field10_event__c', default=0)  # イベント情報告知
