# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_partner(models.Model):
    _inherit = "res.partner"
    _description = 'Account.csv'
    # A ID
    is_deleted = fields.Boolean("IsDeleted", default=0)  # B 削除フラグ

    fax = fields.Char(string="fax")  # X OK
    contact_type = fields.Many2one('res.partner.contact_type', string="type")  # E OK
    channel = fields.Many2one('res.partner.channel', 'channel')  # BG OK
    account_number = fields.Char("AccountNumber")  # Y OK
    annual_revenue = fields.Char("AnnualRevenue")  # AC 年間売上 OK
    number_of_employees = fields.Integer("NumberOfEmployees")  # AD 従業員数 OK
    ownership = fields.Char(string="ownership", )  # OK
    ticker_symbol = fields.Char("TickerSymbol")  # AF 銘柄コード OK
    description = fields.Text("Description")  # OK
    rating = fields.Char(string="Rating")  # ok
    site = fields.Char("Site")  # OK
    supplier_no = fields.Char("supplier_no")  # OK 仕入先番号 Field5__c
    kana = fields.Char("kana")  # OK フリガナ Field5__c
    corporate_mail = fields.Boolean("corporate_mail", default=0)  # 法人宛郵便 OK  Field6__c
    transactions = fields.Many2one('res.partner.transactions', string="transactions")  # 取引方法 OK Field4__c
    payment_terms_1 = fields.Char("payment_terms_1")  # 支払い条件１ OK X1__c
    payment_terms_2 = fields.Char("payment_terms_2")  # 支払い条件2 OK X2__c
    multiplier_black = fields.Float("multiplier_black")  # 掛率(黒) OK Field7__c
    multiplier_green = fields.Float("multiplier_green")  # 掛率(黒) OK Field8__c
    fare_payment_terms = fields.Char("fare_payment_terms")  # 支払条件運賃 OK Field9__c
    categorization = fields.Char("categorization")  # 分類 OK Field10__c
    situation = fields.Char("situation")  # 状況 OK Field11__c
    address_confirmation_required = fields.Char("address_confirmation_required")  # 住所要確認 OK Field12__c
    last_contract_date = fields.Datetime("last_contract_date")  # 最新成約日 OK Field13__c
    total_number_of_transactions = fields.Integer("total_number_of_transactions")  # 累計取引回数 OK Field14__c
    cumulative_sales = fields.Float("cumulative_sales")  # 累計売上金額 OK Field15__c
    potential = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], string="potential",
                                 default='')  # ポテンシャル OK Field16__c
    kubun = fields.Char("kubun")  # 区分 OK  Field20__c
    rival_companies = fields.Boolean("rival_companies", default=0)  # 競合他社 OK Field23__c
    group = fields.Char("group")  # G OK Field21__c
    transaction_category = fields.Char("transaction_category")  # 取引区分 OK Field27__c
    campaign_1 = fields.Char("campaign_1")  # キャンペーン① OK Field25__c
    campaign_2 = fields.Char("campaign_2")  # キャンペーン② OK Field26__c
    dummy = fields.Boolean("dummy", default=0)  # ダミー OK Field29__c
    # relation

    case = fields.One2many('rtw_sf_case', inverse_name='contacts')  # ケース OK
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
    ny_card = fields.Boolean("ny_card", default=0)  # 年賀状 OK Field1__c
    need_dm = fields.Boolean("need_dm", default=0)  # DM希望 OK DM__c
    gift = fields.Boolean("gift", default=0,
                          help="Customers, business partners, and suppliers who need to send gifts, gifts, mid-year gifts, New Year's gifts, and year-end gifts"
                          )  # 進物 OK Field2__c2
    summer_greeting = fields.Boolean("summer_greeting", default=0)  # 暑中見舞 OK Field3__c
    send_catalog = fields.Char("send_catalog", default=0)  # カタログ配布 OK Field4__c
    gender = fields.Char("gender")  # 性別 OK Field6__c
    in_has = fields.Char("in_has")  # R社内所有者 OK R__c
    do_not_dm = fields.Boolean("do_not_dm", default=0)  # DM不要 OK DoNotDM
    evaluation = fields.Char("evaluation", help="2015年～2017年　売上金額ベースの評価")  # 評価 OK Field8__c
    dm_unknown = fields.Boolean("dm_unknown", help=">DM欄　未記入", default=0)  # DM不明 OK DM_unknown__c
    r_web_site = fields.Char("r_web_site")  # アクション② OK
    related_attributes = fields.Char("related_attributes")  # 関係者属性 OK HM_OB__c
    cs_number = fields.Char("cs_number")  # 取引先番号 OK Field12__c
    mc_subscriber = fields.Many2one('res.partner', "Contact", copy=False)  # コンタクト OK
    haihai_id = fields.Char("ID__c")  # OK
    mail_change = fields.Boolean("mail_change", default=0)  # メール変更 OK Field14_mail__c
    haihai_open_count = fields.Integer("haihai_open_count")  # 配配開封数 OKField14__c
    calender = fields.Boolean("calender", default=0)  # ｶﾚﾝﾀﾞｰ OKcalendar__c
    key_man = fields.Boolean("key_man", default=0)  # キーマン OKField17__c
    r_owner = fields.Boolean("r_owner", default=0, help="Ritzwell家具の購入実績がある")  # Rオーナー OKR_1__c
    sansancard = fields.Boolean("sansancard",
                                default=0)  # Created by Scan to Salesforce OKsansancard__CreatedByScanToSalesforce__c
    retirement = fields.Char("retirement")  # 退職 OKField18__c
    change = fields.Boolean("change", default=0)  # 異動 OKField19__c
    maternity_leave_and_vacation = fields.Boolean("maternity_leave_and_vacation", default=0)  # 育休・休暇 OK Field20__c2
    unknown = fields.Boolean("unknown", default=0)  # 不明 OKField21__c2
    lead_source_roc = fields.Char("lead_source_roc")  # リードソース(ROC) OKROC__c
    interest_roc = fields.Char("interest_roc")  # 興味・関心(ROC) OK ROC_2__c
    Influencers = fields.Char("Influencers")  # インフルエンサー度 OK Field22__c
    occupational_category = fields.Char("occupational_category")  # 職種 OK Field23__c
    not_use = fields.Boolean("not_use", default=0)  # 使用不可 OK DM_4__c
    mail2 = fields.Char("mail2")  # メール2 OK Field24__c
    mail_1_2 = fields.Boolean("mail_1_2", default=0)  # メール1・2 OK X1_2__c
    haihai_count = fields.Integer("haihai_count")  # 配配送信数 OK Field25__c2
    region = fields.Char("region")  # 地域 OK Field34__c
    stop_letter = fields.Boolean("stop_letter", default=0)  # LETTER停止 OK LETTER__c
    # kin = fields.Char("Field36__c")  # 親類（親戚・家族） OK
    kin = fields.Many2one('res.partner', "kin", copy=False)  # Field36__c
    mail3 = fields.Char("mail3")  # メール3 OK X3__c
    company_name = fields.Char("company_name")  # 会社名 OK Field37__c
    x20 = fields.Boolean("X20__c", default=0)  # OK
    x30 = fields.Boolean("X30__c", default=0)  # OK
    x40 = fields.Boolean("X40__c", default=0)  # OK
    x50 = fields.Boolean("X50__c", default=0)  # OK
    x60 = fields.Boolean("X60__c", default=0)  # OK
    x70 = fields.Boolean("X70__c", default=0)  # OK
    x80 = fields.Boolean("X80__c", default=0)  # OK
    joint_name = fields.Char("X1__c")  # 連名1 OK
    web = fields.Char("web")  # WEBサイト OK WEB__c
    media_name = fields.Char("media_name")  # 媒体名 OK Field39__c
    case_count = fields.Integer(string="case count", compute="_compute_case_count")

    def _compute_case_count(self):
        for rec in self:
            case_count = self.env['rtw_sf_case'].search_count([('contacts', '=', rec.id)])
            rec.case_count = case_count

    def action_open_case(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'case',
            'res_model': 'rtw_sf_case',
            'domain': [('contacts', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_id': self.id,
                'default_contacts': self.id,
                'default_created_by_id': self.env.user.id
            }
        }

    @api.onchange("first_name", "last_name", "company_type")
    def _compute_name(self):
        for rec in self:
            name = rec.name
            print(rec.company_type)
            if rec.company_type == "person":
                if rec.last_name == False and rec.first_name:
                    name = rec.first_name
                if rec.first_name == False and rec.last_name:
                    name = rec.last_name
                if rec.first_name and rec.last_name:
                    name = rec.last_name + " " + rec.first_name
            rec.name = name
            print(name)
