# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_partner(models.Model):
    _inherit = "res.partner"
    _description = 'Account.csv'
    # A ID
    is_deleted = fields.Boolean("IsDeleted", default=0)  # B 削除フラグ

    fax = fields.Char(string="fax")  # X
    contact_type = fields.Many2one('res.partner.contact_type', string="type")  # E
    channel = fields.Many2one('res.partner.channel')  # BG
    account_number = fields.Char("AccountNumber")  # Y
    annual_revenue = fields.Char("AnnualRevenue")  # AC 年間売上
    number_of_employees = fields.Integer("NumberOfEmployees")  # AD 従業員数
    ownership = fields.Char(string="ownership", )
    ticker_symbol = fields.Char("TickerSymbol")  # AF 銘柄コード
    description = fields.Text("Description")
    rating = fields.Char(string="Rating")
    site = fields.Char("Site")
    supplier_no = fields.Char("Field5__c")
    kana = fields.Char("Field2__c")
    corporate_mail = fields.Boolean("Field6__c", default=0)
    transactions = fields.Many2one('res.partner.transactions', string="Field4__c")
    payment_terms_1 = fields.Char("X1__c")  # 支払い条件１
    payment_terms_2 = fields.Char("X2__c")  # 支払い条件2
    multiplier_black = fields.Float("Field7__c")  # 掛率(黒)
    multiplier_green = fields.Float("Field8__c")  # 掛率(黒)
    fare_payment_terms = fields.Char("Field9__c")
    categorization = fields.Char("Field10__c")
    situation = fields.Char("Field11__c")
    address_confirmation_required = fields.Char("Field12__c")
    last_contract_date = fields.Datetime("Field13__c")
    total_number_of_transactions = fields.Integer("Field14__c")
    cumulative_sales = fields.Float("Field15__c")
    potential = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], string="Field16__c", default='')
    kubun = fields.Char("Field20__c")
    rival_companies = fields.Boolean("Field23__c", default=0)
    group = fields.Char("Field21__c")
    transaction_category = fields.Char("Field27__c")
    campaign_1 = fields.Char("Field25__c")
    campaign_2 = fields.Char("Field26__c")
    dummy = fields.Boolean("Field29__c", default=0)
    # relation

    case = fields.One2many('rtw_sf_case', inverse_name='accounts')
    # contact
    account_id = fields.Char("AccountId")
    first_name = fields.Char("FirstName")
    last_name = fields.Char("LastName")
    record_type = fields.Char("RecordTypeId")
    other_country = fields.Char("OtherCountry")
    other_postal_code = fields.Char("OtherPostalCode")
    other_state = fields.Char("OtherState")
    other_city = fields.Char("OtherCity")
    other_street = fields.Char("OtherStreet")
    mailing_country = fields.Char("MailingCountry")
    mailing_postal_code = fields.Char("MailingPostalCode")
    mailing_state = fields.Char("MailingState")
    mailing_city = fields.Char("MailingCity")
    mailing_street = fields.Char("MailingStreet")
    home_phone = fields.Char("HomePhone")
    other_phone = fields.Char("OtherPhone")
    reports_to_id = fields.Char("ReportsToId")
    department = fields.Char("Department")
    lead_source = fields.Char(string="LeadSource")
    birthdate = fields.Date(string="Birthdate")
    opt_out_email = fields.Boolean(string="HasOptedOutOfEmail", default=0)
    opt_out_fax = fields.Boolean(string="HasOptedOutOfFax", default=0)
    do_not_call = fields.Boolean(string="DoNotCall", default=0)
    last_cu_request_date = fields.Datetime("LastCURequestDate")
    last_cu_update_date = fields.Datetime("LastCUUpdateDate")
    email_bounced_reason = fields.Text("EmailBouncedReason")
    email_bounced_date = fields.Datetime("EmailBouncedDate")
    ny_card = fields.Boolean("Field1__c", default=0)
    need_dm = fields.Boolean("DM__c", default=0)
    gift = fields.Boolean("Field2__c2", default=0, help="Customers, business partners, and suppliers who need to send gifts, gifts, mid-year gifts, New Year's gifts, and year-end gifts")
    summer_greeting = fields.Boolean("Field3__c", default=0)
    send_catalog = fields.Boolean("Field4__c2", default=0)
    gender = fields.Char("Field6__c")
    in_has = fields.Char("R__c")
    do_not_dm = fields.Boolean("DoNotDM", default=0)
    evaluation = fields.Char("Field8__c", help="2015年～2017年　売上金額ベースの評価")
    dm_unknown = fields.Boolean("DM_unknown__c", help=">DM欄　未記入", default=0)
    r_web_site = fields.Char("Field11__c")
    related_attributes = fields.Char("HM_OB__c")
    cs_number = fields.Char("Field12__c")
    mc_subscriber = fields.Many2one('res.partner', "Contact", copy=False)  # コンタクト
    haihai_id = fields.Char("ID__c")
    mail_change = fields.Boolean("Field14_mail__c", default=0)
    haihai_open_count = fields.Integer("Field14__c")
    calender = fields.Boolean("calendar__c", default=0)
    key_man = fields.Boolean("Field17__c", default=0)
    r_owner = fields.Boolean("R_1__c", default=0, help="Ritzwell家具の購入実績がある")
    sansancard = fields.Boolean("sansancard__CreatedByScanToSalesforce__c", default=0)
    retirement = fields.Char("Field18__c")
    change = fields.Boolean("Field19__c", default=0)
    maternity_leave_and_vacation = fields.Boolean("Field20__c2", default=0)
    unknown = fields.Boolean("Field21__c2", default=0)
    lead_source_roc = fields.Char("ROC__c")
    interest_roc = fields.Char("ROC_2__c")
    Influencers = fields.Char("Field22__c")
    occupational_category = fields.Char("Field23__c")
    not_use = fields.Boolean("DM_4__c", default=0)
    mail2 = fields.Char("Field24__c")
    mail_1_2 = fields.Boolean("X1_2__c", default=0)
    haihai_count = fields.Integer("Field25__c2")
    region = fields.Char("Field34__c")
    stop_letter = fields.Boolean("LETTER__c", default=0)
    kin = fields.Char("Field36__c")
    mail3 = fields.Char("X3__c")
    company_name = fields.Char("Field37__c")
    x20 = fields.Boolean("X20__c", default=0)
    x30 = fields.Boolean("X30__c", default=0)
    x40 = fields.Boolean("X40__c", default=0)
    x50 = fields.Boolean("X50__c", default=0)
    x60 = fields.Boolean("X60__c", default=0)
    x70 = fields.Boolean("X70__c", default=0)
    x80 = fields.Boolean("X80__c", default=0)
    joint_name = fields.Char("X1__c")
    web = fields.Char("WEB__c")
    media_name = fields.Char("Field39__c")
