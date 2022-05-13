# -*- coding: utf-8 -*-

from odoo import models, fields, api


class task(models.Model):
    _name = 'task.task'
    _description = 'task.task'

    who_id = fields.Char('WhoId')  # 対象者id B列
    what_id = fields.Char('WhatId')  # タスクid C列
    who_count = fields.Integer('WhoCount')  # 対象者アカウント D列
    what_count = fields.Integer('WhatCount')  # タスク件数 E列
    subject = fields.Char('Subject')  # 課題 F列
    activity_date = fields.Datetime('ActivityDate')  # 活動日 G列
    status = fields.Char('Status')  # ステータス H列
    priority = fields.Char('Priority')  # 優先順位 I列
    owner_id = fields.Char('OwnerId')  # 所有者Id J列 ※
    # owner_id = fields.Many2one('res.users', 'OwnerId')  # 所有者Id J列 ※
    description = fields.Text('Description')  # 説明 K列
    type = fields.Char('Type')  # 種類 L列
    # is_deleted = fields.Datetime('IsDeleted')  # 削除フラグ M列 ★0のみ
    account_id = fields.Char('AccountId')  # アカウントid N列
    isclosed = fields.Boolean('IsClosed')  # 完了済みフラグ O列
    created_date = fields.Datetime('CreatedDate')  # 作成日 P列
    created_by_id = fields.Char('CreatedById')  # 作成ID Q列 ※
    # created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID Q列 ※
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日 R列
    last_modified_by_id = fields.Char('LastModifiedById')  # 最終更新者 S列 ※
    # last_modified_by_id = fields.Many2one('res.users', 'LastModifiedById')  # 最終更新者 S列 ※
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日 T列
    is_archived = fields.Boolean('IsArchived')  # アーカイブフラグ U列
    email_message_id = fields.Char('EmailMessageId')  # emailメッセージid V列
    activity_origin_type = fields.Integer('ActivityOriginType')  # 活動起源タイプ W列
    # IsVisibleInSelfService = fields.Integer('IsVisibleInSelfService')  # X列 ★0のみ
    call_duration_in_seconds = fields.Integer('CallDurationInSeconds')  # 通話時間(秒) Y列
    # CallType = fields.Char('CallType')  # ★空白のみ
    # CallDisposition = fields.Char('CallDisposition')  # ★空白のみ
    # CallObject = fields.Char('CallObject')  # ★空白のみ
    reminder_datetime = fields.Datetime('ReminderDateTime')  # 通知日時 AC
    is_reminder_set = fields.Boolean('IsReminderSet')  # 通知設定 AD
    recurrence_activity_id = fields.Char('RecurrenceActivityId')  # 再帰活動id AE
    is_recurrence = fields.Boolean('IsRecurrence')  # フラグ AF
    recurrence_start_date_only = fields.Datetime('RecurrenceStartDateOnly')  # AG
    recurrence_end_date_only = fields.Datetime('RecurrenceEndDateOnly')  # AH
    recurrence_time_zone_sid_key = fields.Char('RecurrenceTimeZoneSidKey')  # AI
    recurrence_type = fields.Char('RecurrenceType')  # AJ
    recurrence_interval = fields.Integer('RecurrenceInterval')  # AK
    recurrence_day_of_week_mask = fields.Integer('RecurrenceDayOfWeekMask')  # AL
    # recurrence_day_of_month = fields.Char('RecurrenceDayOfMonth')  # AM　★空白のみ
    # recurrence_instance = fields.Char('RecurrenceInstance')  # AN　★空白のみ
    # recurrence_month_of_year = fields.Char('RecurrenceMonthOfYear')  # AO　★空白のみ
    # recurrence_regenerated_type = fields.Char('RecurrenceRegeneratedType')  # AP　★空白のみ
    completed_datetime = fields.Datetime('CompletedDateTime')  # AQ
    cost = fields.Integer('Field2__c')  # コスト AR
    bill_amount = fields.Integer('Field3__c')  # 請求額 AS
    # kpi1 = fields.Char('KPI_1__c')  # KPI項目 AT ★空白のみ
    # f = fields.Char('KPI__c')  # F AU ★空白のみ
    # study_meeting_count = fields.Char('Field4__c')  # 勉強会人数 AV ★空白のみ
    campaign_id = fields.Char('campaign_5__c')  # 関連先(キャンペーン)id AW
    situation = fields.Char('Field1__c')  # 状況 AX
    sr = fields.Char('SR__c')  # SR AY
    new_sales = fields.Char('new_customer_2__c')  # 新規営業 AZ ★0、空白のみ
    belongs = fields.Char('Field7__c')  # 所属 BA
    client_id = fields.Char('Field8__c')  # 関連先(取引先名)id BB
    visitor_count = fields.Integer('Field10__c')  # 来場人数 BC
    customer_service_staff = fields.Char('Field12__c')  # 接客担当 BD
    start_datetime = fields.Datetime('Field25__c')  # 開始時間 BE
    visitor_set_count = fields.Integer('Field11__c')  # 来場組数 BF ★0、1、空白
    # calendar_sales = fields.Char('X2021__c')  # ｶﾚﾝﾀﾞｰ販売 BG ★空白のみ
    # purchaser = fields.Char('Field24__c')  # 購入者 BH ★空白のみ
    payment_method = fields.Integer('Field26__c')  # クレジット/現金購入 BI ★0、空白
    visitor_purpose = fields.Char('Field16__c')  # 来場目的 BJ
    lead = fields.Char('Field17__c')  # リード（来場） BK
    visitor_type = fields.Char('Field18__c')  # 来場者タイプ BL
    estimate_flg = fields.Integer('Field19__c')  # 事前提案・見積り有 BM ★0、1、空白
    # reservation = fields.Char('Field20__c')  # 予約 BN ★空白のみ
    with_reservation = fields.Integer('Field21__c')  # 予約あり BO ★0、空白
    no_reservation = fields.Integer('Field22__c')  # 予約なし BP ★0、空白
    # guest_book = fields.Char('Field30__c')  # 芳名帳/アンケート BQ ★空白のみ
    estimated_accrual = fields.Char('Field31__c')  # 見積発生（新規商談） BR ★0、空白
    omotesando = fields.Char('Field35__c')  # 表参道来店 BS ★0、空白

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
