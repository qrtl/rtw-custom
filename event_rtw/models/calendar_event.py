# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class calendar_event_rtw(models.Model):
    _inherit = 'calendar.event'

    sr = fields.Char('SR__c')  # SR AY
    new_sales = fields.Boolean('new_customer_2__c')  # 新規営業 AZ ★0,1,空白

    # SR来場情報
    reservation = fields.Char('Field20__c')  # 予約 BN
    estimate_flg = fields.Boolean('Field19__c')  # 事前提案・見積り有 BM ★0,1,空白
    visitor_type = fields.Char('Field18__c')  # 来場者タイプ BL
    visitor_set_count = fields.Integer('Field11__c')  # 来場組数 BF
    visitor_count = fields.Integer('Field10__c')  # 来場人数 BC
    lead = fields.Char('Field17__c')  # リード（来場） BK
    visitor_purpose = fields.Char('Field16__c')  # 来場目的 BJ
    guest_book = fields.Char('Field30__c')  # 芳名帳/アンケート BQ
    estimated_accrual = fields.Boolean('Field31__c')  # 見積発生（新規商談） BR ★0,1,空白
    payment_method = fields.Boolean('Field26__c')  # クレジット/現金購入 BI ★0,1,空白
    omotesando = fields.Boolean('Field35__c')  # 表参道来店 BS ★0,1,空白
