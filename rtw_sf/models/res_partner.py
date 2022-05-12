# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_partner(models.Model):
    _inherit = "res.partner"
    _description = 'Account.csv'
    # A ID
    is_deleted = fields.Boolean("IsDeleted", default=0)  # B 削除フラグ

    fax = fields.Char(string="fax")  # X OK
    contact_type = fields.Many2one('res.partner.contact_type', string="type")  # E OK
    channel = fields.Many2one('res.partner.channel')  # BG OK
    account_number = fields.Char("AccountNumber")  # Y OK
    annual_revenue = fields.Char("AnnualRevenue")  # AC 年間売上 OK
    number_of_employees = fields.Integer("NumberOfEmployees")  # AD 従業員数 OK
    ownership = fields.Char(string="ownership", )  # OK
    ticker_symbol = fields.Char("TickerSymbol")  # AF 銘柄コード OK
    description = fields.Text("Description")  # OK
    rating = fields.Char(string="Rating")  # ok
    site = fields.Char("Site")  # OK
    supplier_no = fields.Char("Field5__c")  # OK 仕入先番号
    kana = fields.Char("Field2__c")  # OK フリガナ
    corporate_mail = fields.Boolean("Field6__c", default=0)  # 法人宛郵便 OK
    transactions = fields.Many2one('res.partner.transactions', string="Field4__c")  # 取引方法 OK
    payment_terms_1 = fields.Char("X1__c")  # 支払い条件１ OK
    payment_terms_2 = fields.Char("X2__c")  # 支払い条件2 OK
    multiplier_black = fields.Float("Field7__c")  # 掛率(黒) OK
    multiplier_green = fields.Float("Field8__c")  # 掛率(黒) OK
    fare_payment_terms = fields.Char("Field9__c")  # 支払条件運賃 OK
    categorization = fields.Char("Field10__c")  # 分類 OK
    situation = fields.Char("Field11__c")  # 状況 OK
    address_confirmation_required = fields.Char("Field12__c")  # 住所要確認 OK
    last_contract_date = fields.Datetime("Field13__c")  # 最新成約日 OK
    total_number_of_transactions = fields.Integer("Field14__c")  # 累計取引回数 OK
    cumulative_sales = fields.Float("Field15__c")  # 累計売上金額 OK
    potential = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], string="Field16__c",
                                 default='')  # ポテンシャル OK
    kubun = fields.Char("Field20__c")  # 区分 OK
    rival_companies = fields.Boolean("Field23__c", default=0)  # 競合他社 OK
    group = fields.Char("Field21__c")  # G OK
    transaction_category = fields.Char("Field27__c")  # 取引区分 OK
    campaign_1 = fields.Char("Field25__c")  # キャンペーン① OK
    campaign_2 = fields.Char("Field26__c")  # キャンペーン② OK
    dummy = fields.Boolean("Field29__c", default=0)  # ダミー OK
    # relation

    case = fields.One2many('rtw_sf_case', inverse_name='accounts')  # ケース OK
    # contact
    account_id = fields.Many2one('res.partner', "AccountId")  # OK
    first_name = fields.Char("FirstName")  # OK
    last_name = fields.Char("LastName")  # OK
    record_type = fields.Char("RecordTypeId")  # OK
    other_country = fields.Char("OtherCountry")  # OK
    other_postal_code = fields.Char("OtherPostalCode")  # OK
    other_state = fields.Char("OtherState")  # OK
    other_city = fields.Char("OtherCity")  # OK
    other_street = fields.Char("OtherStreet")  # OK
    mailing_country = fields.Char("MailingCountry")  # OK
    mailing_postal_code = fields.Char("MailingPostalCode")  # OK
    mailing_state = fields.Char("MailingState")  # OK
    mailing_city = fields.Char("MailingCity")  # OK
    mailing_street = fields.Char("MailingStreet")  # OK
    home_phone = fields.Char("HomePhone")  # OK
    other_phone = fields.Char("OtherPhone")  # OK
    reports_to_id = fields.Char("ReportsToId")  # OK
    department = fields.Char("Department")  # OK
    lead_source = fields.Char(string="LeadSource")  # OK
    birthdate = fields.Date(string="Birthdate")  # OK
    opt_out_email = fields.Boolean(string="HasOptedOutOfEmail", default=0)  # OK
    opt_out_fax = fields.Boolean(string="HasOptedOutOfFax", default=0)  # ok
    do_not_call = fields.Boolean(string="DoNotCall", default=0)  # OK
    last_cu_request_date = fields.Datetime("LastCURequestDate")  # OK
    last_cu_update_date = fields.Datetime("LastCUUpdateDate")  # OK
    email_bounced_reason = fields.Text("EmailBouncedReason")  # OK
    email_bounced_date = fields.Datetime("EmailBouncedDate")  # OK
    ny_card = fields.Boolean("Field1__c", default=0)  # 年賀状 OK
    need_dm = fields.Boolean("DM__c", default=0)  # DM希望 OK
    gift = fields.Boolean("Field2__c2", default=0,
                          help="Customers, business partners, and suppliers who need to send gifts, gifts, mid-year gifts, New Year's gifts, and year-end gifts"
                          )  # 進物 OK
    summer_greeting = fields.Boolean("Field3__c", default=0)  # 暑中見舞 OK
    send_catalog = fields.Char("Field4__c2", default=0)  # カタログ配布 OK
    gender = fields.Char("Field6__c")  # 性別 OK
    in_has = fields.Char("R__c")  # R社内所有者 OK
    do_not_dm = fields.Boolean("DoNotDM", default=0)  # DM不要 OK
    evaluation = fields.Char("Field8__c", help="2015年～2017年　売上金額ベースの評価")  # 評価 OK
    dm_unknown = fields.Boolean("DM_unknown__c", help=">DM欄　未記入", default=0)  # DM不明 OK
    r_web_site = fields.Char("Field11__c")  # アクション② OK
    related_attributes = fields.Char("HM_OB__c")  # 関係者属性 OK
    cs_number = fields.Char("Field12__c")  # 取引先番号 OK
    mc_subscriber = fields.Many2one('res.partner', "Contact", copy=False)  # コンタクト OK
    haihai_id = fields.Char("ID__c")  # OK
    mail_change = fields.Boolean("Field14_mail__c", default=0)  # メール変更 OK
    haihai_open_count = fields.Integer("Field14__c")  # 配配開封数 OK
    calender = fields.Boolean("calendar__c", default=0)  # ｶﾚﾝﾀﾞｰ OK
    key_man = fields.Boolean("Field17__c", default=0)  # キーマン OK
    r_owner = fields.Boolean("R_1__c", default=0, help="Ritzwell家具の購入実績がある")  # Rオーナー OK
    sansancard = fields.Boolean("sansancard__CreatedByScanToSalesforce__c",
                                default=0)  # Created by Scan to Salesforce OK
    retirement = fields.Char("Field18__c")  # 退職 OK
    change = fields.Boolean("Field19__c", default=0)  # 異動 OK
    maternity_leave_and_vacation = fields.Boolean("Field20__c2", default=0)  # 育休・休暇 OK
    unknown = fields.Boolean("Field21__c2", default=0)  # 不明 OK
    lead_source_roc = fields.Char("ROC__c")  # リードソース(ROC) OK
    interest_roc = fields.Char("ROC_2__c")  # 興味・関心(ROC) OK
    Influencers = fields.Char("Field22__c")  # インフルエンサー度 OK
    occupational_category = fields.Char("Field23__c")  # 職種 OK
    not_use = fields.Boolean("DM_4__c", default=0)  # 使用不可 OK
    mail2 = fields.Char("Field24__c")  # メール2 OK
    mail_1_2 = fields.Boolean("X1_2__c", default=0)  # メール1・2 OK
    haihai_count = fields.Integer("Field25__c2")  # 配配送信数 OK
    region = fields.Char("Field34__c")  # 地域 OK
    stop_letter = fields.Boolean("LETTER__c", default=0)  # LETTER停止 OK
    # kin = fields.Char("Field36__c")  # 親類（親戚・家族） OK
    kin = fields.Many2one('res.partner', "Field36__c", copy=False)
    mail3 = fields.Char("X3__c")  # メール3 OK
    company_name = fields.Char("Field37__c")  # 会社名 OK
    x20 = fields.Boolean("X20__c", default=0)  # OK
    x30 = fields.Boolean("X30__c", default=0)  # OK
    x40 = fields.Boolean("X40__c", default=0)  # OK
    x50 = fields.Boolean("X50__c", default=0)  # OK
    x60 = fields.Boolean("X60__c", default=0)  # OK
    x70 = fields.Boolean("X70__c", default=0)  # OK
    x80 = fields.Boolean("X80__c", default=0)  # OK
    joint_name = fields.Char("X1__c")  # 連名1 OK
    web = fields.Char("WEB__c")  # WEBサイト OK
    media_name = fields.Char("Field39__c")  # 媒体名 OK
    case_count = fields.Integer(string="case count", compute="_compute_case_count")

    def _compute_case_count(self):
        for rec in self:
            case_count = self.env['rtw_sf_case'].search_count([('accounts', '=', rec.id)])
            rec.case_count = case_count

    def action_open_case(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'case',
            'res_model': 'rtw_sf_case',
            'domain': [('accounts', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_id': self.id,
                'default_accounts': self.id,
                'default_created_by_id': self.env.user.id
            }
        }
