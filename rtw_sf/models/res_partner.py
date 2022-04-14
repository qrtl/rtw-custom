# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_partner(models.Model):
    _inherit = "res.partner"
    _description = 'Account.csv'
    # A ID
    is_deleted = fields.Boolean("Is Deleted")  # B 削除フラグ

    fax = fields.Char(string="fax")  # X
    contact_type = fields.Many2one('res.partner.contact_type')  # E
    channel = fields.Many2one('res.partner.channel')  # BG
    account_number = fields.Char("AccountNumber")  # Y
    annual_revenue = fields.Integer("AnnualRevenue")  # AC 年間売上
    number_of_employees = fields.Integer("NumberOfEmployees")  # AD 従業員数
    ownership = fields.Char(string="ownership", )
    ticker_symbol = fields.Char("TickerSymbol")  # AF 銘柄コード
    description = fields.Text("Description")
    rating = fields.Char(string="Rating")
    site = fields.Char("Site")
    supplier_no = fields.Char("Field5__c")
    kana = fields.Char("Field2__c")
    corporate_mail = fields.Boolean("Field6__c")
    transactions = fields.Many2one('res.partner.transactions', string="Field4__c")
    payment_terms_1 = fields.Char("X1__c")  # 支払い条件１
    payment_terms_2 = fields.Char("X2__c")  # 支払い条件2
    multiplier_black = fields.Float("Field7__c")  # 掛率(黒)
    multiplier_green = fields.Float("Field8__c")  # 掛率(黒)
    fare_payment_terms = fields.Char("Field9__c")
    categorization = fields.Char("Field10__c")
    situation = fields.Char("Field11__c")
    address_confirmation_required = fields.Char("Field12__c")
    last_contract_date = fields.Date("Field13__c")
    total_number_of_transactions = fields.Integer("Field14__c")
    cumulative_sales = fields.Float("Field15__c")
    potential = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], string="Field16__c", default='')
    kubun = fields.Char("Field20__c")
    rival_companies = fields.Boolean("Field23__c")
    group = fields.Char("Field21__c")
    transaction_category = fields.Char("Field27__c")
    campaign_1 = fields.Char("Field25__c")
    campaign_2 = fields.Char("Field26__c")
    dummy = fields.Boolean("Field29__c")
    # relation

    # case = fields.One2many('case')

