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
    name = fields.Char('Name')
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
    handover_matters = fields.Text('Field10_toiawase__c')  # 引継ぎ事項
    deign = fields.Boolean('Field12__c')  # デザイン
    use = fields.Boolean('Field13__c')  # 使い心地
    sense_of_materials = fields.Boolean('Field14__c')  # 素材感
    sales_staff_evaluation = fields.Selection([
        ('5', '大変満足'),
        ('4', 'やや満足'),
        ('3', '普通'),
        ('2', 'やや不満'),
        ('1', '大変不満'),
    ], string="Q3_evaluate_2018__c",
     default='')  # 営業スタッフの評価
    originator = fields.Selection([
        ('1', 'IC・設計・クライアント'),
        ('2', 'オーナー・エンドユーザー'),
        ('3', 'その他'),
        ('4', 'メーカー・サプライヤー'),
    ], string="Field43__c",
     default='')  # 発信者
    price = fields.Boolean('Field15__c')  # 価格
    image_atmosphere = fields.Boolean('Field16__c')  # イメージ雰囲気
    sales_staff_response = fields.Boolean('eigyo_2018__c')  # 営業スタッフの対応
    recommendation_from_a_friend = fields.Boolean('Field18__c')  # 友人の勧め
    inet_reputation_and_wom = fields.Boolean('Field19__c')  # ネット評判・口コミ
    glad_bought_it_before = fields.Boolean('Field20__c')  # 以前購入してよかった
    non_response = fields.Boolean('Field21__c')  # 無回答
    oppotunity = fields.Many2one('opportunity.opportunity', 'oppotunity_2__c')
    evaluation_of_delivery_staff = fields.Selection([
        ('5', '大変満足'),
        ('4', 'やや満足'),
        ('3', '普通'),
        ('2', 'やや不満'),
        ('1', '大変不満'),
    ], string="Q4_evaluate_2018__c",
     default='')  # 納品スタッフの評価
    yes = fields.Boolean('Q5__c')  # YES
    no = fields.Boolean('NO_2__c')  # NO
    need_dm = fields.Boolean('DM_1__c')  # DM希望
    not_need_dm = fields.Boolean('DM_3__c')  # DM不要
    mid_category = fields.Selection([
        ('1', '-'),
        ('2', 'ＳＲ展示品について'),
        ('3', "SR予約"),
        ('4', 'セール'),
        ('5', 'プレゼント・キャンペーン'),
        ('6', 'メンテナンス'),
        ('7', '営業日時・時間'),
        ('8', '購入ルート'),
        ('9', '支払い・決済方法'),
        ('10', '資料請求'),
        ('11', '取引条件の確認'),
        ('12', '商品クレーム'),
        ('13', '商品不具合・破損'),
        ('14', '新規注文検討'),
        ('15', '注文済商品'),
        ('16', '納品済商品（メンテ）'),
    ], string="Field45__c",
     default='')  # 中分類
    detail = fields.Selection([
        ('1', '-'),
        ('2', 'スペアカバー・部材購入'),
        ('3', "セール実施予定の確認"),
        ('4', 'セール商品内容'),
        ('5', 'デザイン（特徴・コンセプト・デザイナーほか）'),
        ('6', '画像・資料提供'),
        ('7', '供給（在庫・納期ほか）'),
        ('8', '仕様（価格・サイズ・重量・別注対応ほか）'),
        ('9', '修理・張り替え'),
        ('10', '商品名・品番確認'),
        ('11', '日常的なお手入れ'),
        ('12', '納品日の確認'),
        ('13', '納品方法の確認'),
        ('14', '補修的なメンテ'),
    ], string="Field44__c",
     default='')  # 内容
    survey_no = fields.Char('NO_4__c')  # アンケートNO
    other = fields.Boolean('X4__c')  # その他(4)
    oppotunity_2 = fields.Many2one('opportunity.opportunity', 'Field52__c')  # 関連商談②
    date_time = fields.Datetime('Field34__c')  # 日時
    means = fields.Selection([
        ('1', 'WEBフォーム'),
        ('2', 'メール'),
        ('3', "来場"),
        ('4', '電話'),
        ('5', 'その他'),
    ], string="Field35__c",
     default='')  # 手段
    number = fields.Char('X4__c')  # NO
    confirmation = fields.Boolean('Field47__c')  # 確認
    not_meet = fields.Boolean('Field48__c')  # 会っていない
    not_meet_2 = fields.Boolean('Field49__c')  # 会っていない
