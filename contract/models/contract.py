# -*- coding: utf-8 -*-

from odoo import models, fields, api


class contract(models.Model):
    _name = 'contract.contract'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin'
    ]
    _description = 'contract.contract'
    _rec_name = "contract_number"

    accounts = fields.Many2one('res.partner', "Account", copy=False)  # アカウント
    owner_expiration_notice = fields.Integer('OwnerExpirationNotice')  # 所有者有効期限通知 C列
    start_date = fields.Datetime('StartDate')  # 開始日 D列
    billing_Street = fields.Char('BillingStreet')  # 請求先住所 E列
    billing_city = fields.Char('BillingCity')  # 請求先市区名 F列
    billing_state = fields.Char('BillingState')  # 請求先市都道府県名 G列
    billing_postal_code = fields.Char('BillingPostalCode')  # 請求先郵便番号 H列
    billing_country = fields.Char('BillingCountry')  # 請求先国名 I列
    # billing_latitude = fields.Char('BillingLatitude')  # 請求先緯度 J列　★空白のみ
    # billing_longitude = fields.Char('BillingLongitude')  # 請求先経度 K列　★空白のみ
    # billing_geocode_accuracy = fields.Char('BillingGeocodeAccuracy')  # 予想売上高 L列　★空白のみ
    shipping_street = fields.Char('ShippingStreet')  # 配送先住所 M列
    shipping_city = fields.Char('ShippingCity')  # 配送先市区名 N列
    shipping_state = fields.Char('ShippingState')  # 配送先市都道府県名 O列
    shipping_postal_code = fields.Char('ShippingPostalCode')  # 配送先郵便番号 P列
    shipping_country = fields.Char('ShippingCountry')  # 配送先国名 Q列
    contract_term = fields.Integer('ContractTerm')  # 契約期間 U列
    owner_id = fields.Many2one('res.users', 'OwnerId')  # 所有者Id V列
    status = fields.Selection([('draft', 'ドラフト'),
                               ('close', '終了'),
                               ('active', '有効')], string='Status',
                              default="draft")  # ステータス W列
    company_signed_id = fields.Many2one('res.users', 'CompanySignedId')  # 会社署名Id X列
    company_signed_date = fields.Datetime('CompanySignedDate')  # 会社署名日 Y列
    customer_signed_id = fields.Many2one('res.partner', 'CustomerSignedId')  # 顧客署名Id Z列
    # customer_signed_title = fields.Char('CustomerSignedTitle')  # 顧客署名表題 AA列　★空白のみ
    customer_signed_date = fields.Datetime('CustomerSignedDate')  # 顧客署名日 AB列
    special_terms = fields.Text('SpecialTerms')  # 特別条件 AC列
    activated_by_id = fields.Many2one('res.users', 'ActivatedById')  # 有効化Id AD列
    activated_date = fields.Datetime('ActivatedDate')  # 有効期限日 AE列
    status_code = fields.Char('StatusCode')  # 状態コード AF列
    description = fields.Text('Description')  # 説明 AG列
    record_type_id = fields.Many2one('rtw_sf.record_type', 'RecordTypeId')  # レコードタイプId AH列
    # name = fields.Char('Name')  # 名前 AI列　★空白のみ
    # is_deleted = fields.Char('IsDeleted')  # 削除フラグ AJ列　★0のみ
    contract_number = fields.Char('ContractNumber')  # 契約番号 AK列
    # last_approved_date = fields.Datetime('LastApprovedDate')  # 最終承認日 AL列　★空白のみ
    created_date = fields.Datetime('CreatedDate')  # 作成日 AM列
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID AN列
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日 AO列
    last_modified_by_id = fields.Many2one('res.users', 'LastModifiedById')  # 最終更新者 AP列
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日 AQ列
    # last_activity_date = fields.Datetime('LastActivityDate')  # システム最終活動日 AR列　★空白のみ
    lending_reason = fields.Text('Field1__c')  # 貸出理由 AS列
    sales_amount_declaration = fields.Integer('Sales_amount_declaration__c')  # 売上目標 AT列
    sales_amount_results = fields.Integer('sales_results__c')  # 現状売上（直近一年間） AU列
    campaign_id = fields.Char('Field12__c')  # キャンペーンId AV列
    confirmed_by_superior = fields.Boolean('Field2__c')  # 上長確認済 AW列
    implementation_plan = fields.Text('Field3__c')  # 実行案 AX列
    update_reason = fields.Text('Field5__c')  # 更新理由 AY列
    transaction_method = fields.Char('Field14__c')  # 取引方法 AZ列
    long_term_lending = fields.Char('Field7__c')  # 長期貸出【参照】 BA列
    classification1 = fields.Char('Field8__c')  # 分類1 BB列
    classification2 = fields.Char('X2__c')  # 分類2 BC列
    payment_terms_fare = fields.Char('Field15__c')  # 支払条件運賃 BD列
    website = fields.Char('WEB__c')  # WEBサイト BE列
    address_change = fields.Boolean('Field17__c')  # 住所変更 BF列　★0,1,空白
    tel_fax = fields.Boolean('FAX__c')  # 電話・FAX BG列　★0,1,空白
    transaction_terms_change = fields.Boolean('Field18__c')  # 取引条件変更 BH列　★0,1,空白
    change_description = fields.Text('Field19__c')  # 変更説明 BI列
    consolidation = fields.Boolean('Field20__c')  # 統廃合 BJ列　★0,1,空白
    name_change = fields.Boolean('Field21__c')  # 取引先名・部門名変更 BK列　★0,1,空白
    transaction_category = fields.Char('Field26__c')  # 取引区分 BL列
    related_opportunity = fields.Many2one(comodel_name='crm.lead', string='Field27__c')  # 関連商談 BM列
    # oppotunity = fields.Many2one('opportunity.opportunity', 'Field27__c')
    partner_manager = fields.Char('Field29__c')  # 取引先責任者 BN列
    transaction_method_personal = fields.Char('Field37__c')  # 取引方法（個） BO列
    payment_terms_fare_personal = fields.Char('Field38__c')  # 支払条件運賃（個） BP列
    transaction_method_personal2 = fields.Char('Field39__c')  # 取引区分（個） BQ列
    payment_terms1_personal = fields.Char('X1_100__c')  # 支払条件1(個) BR列
    payment_terms2_personal = fields.Char('X2_100__c')  # 支払条件2（個） BS列
    rate_black = fields.Float('Field40__c')  # 掛率（黒） BT列
    rate_green = fields.Float('Field41__c')  # 掛率（緑） BU列
    rate_black_personal = fields.Float('Field42__c')  # 掛率（黒・個） BV列
    rate_green_personal = fields.Float('Field43__c')  # 掛率（緑・個） BW列

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
