# -*- coding: utf-8 -*-

from odoo import models, fields, api


class event_rtw(models.Model):
    _name = 'event_rtw.event_rtw'
    _description = 'event_rtw.event_rtw'

    who_id = fields.Char('WhoId')  # 対象者id C列
    what_id = fields.Char('WhatId')  # タスクid D列
    who_count = fields.Integer('WhoCount')  # 対象者アカウント E列
    what_count = fields.Integer('WhatCount')  # タスク件数 F列
    subject = fields.Char('Subject')  # 表題 G列
    Location = fields.Char('Location')  # 場所 H列
    is_all_day_event = fields.Boolean('IsAllDayEvent')  # 終日イベント開催フラグ I列
    activity_datetime = fields.Datetime('ActivityDateTime')  # 活動日 J列
    activity_date = fields.Datetime('ActivityDate')  # 活動日 K列
    duration_in_minutes = fields.Integer('DurationInMinutes')  # 所要時間(分) L列
    description = fields.Text('Description')  # 説明 M列
    account_id = fields.Char('AccountId')  # アカウントid N列
    owner_id = fields.Char('OwnerId')  # 所有者Id O列
    type = fields.Char('Type')  # 種類 P列
    # is_private = fields.Boolean('IsPrivate')  # プライベート Q列 ★0のみ
    # show_as = fields.Char('ShowAs')  # 表示方法 R列 ★Busyのみ
    # is_deleted = fields.Boolean('IsDeleted')  # 削除フラグ S列 ★0のみ
    is_child = fields.Boolean('IsChild')  # 子供フラグ T ★0,空白
    is_group_event = fields.Boolean('IsGroupEvent')  # グループイベントかどうか U ★0,1,空白
    group_event_type = fields.Boolean('GroupEventType')  # グループイベントタイプ V ★0,1,空白
    created_date = fields.Datetime('CreatedDate')  # 作成日 W列
    created_by_id = fields.Char('CreatedById')  # 作成ID X列
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日 Y列
    last_modified_by_id = fields.Char('LastModifiedById')  # 最終更新者 Z列
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日 AA列
    is_archived = fields.Boolean('IsArchived')  # アーカイブフラグ AB列
    # is_visible_in_self_service = fields.Boolean('IsVisibleInSelfService')  # AC列 ★0のみ
    recurrence_activity_id = fields.Char('RecurrenceActivityId')  # 再帰活動id AD
    is_recurrence = fields.Boolean('IsRecurrence')  # フラグ AE ★0,1
    recurrence_start_datetime = fields.Datetime('RecurrenceStartDateTime')  # AF
    recurrence_end_date_only = fields.Datetime('RecurrenceEndDateOnly')  # AG
    recurrence_time_zone_sid_key = fields.Char('RecurrenceTimeZoneSidKey')  # AH
    recurrence_type = fields.Char('RecurrenceType')  # AI
    recurrence_interval = fields.Integer('RecurrenceInterval')  # AJ ★1,空白
    recurrence_day_of_week_mask = fields.Integer('RecurrenceDayOfWeekMask')  # AK
    # recurrence_day_of_month = fields.Char('RecurrenceDayOfMonth')  # AL ★空白のみ
    # recurrence_instance = fields.Char('RecurrenceInstance')  # AM ★空白のみ
    # recurrence_month_of_year = fields.Char('RecurrenceMonthOfYear')  # AN ★空白のみ
    reminder_datetime = fields.Datetime('ReminderDateTime')  # AO
    is_reminder_set = fields.Boolean('IsReminderSet')  # AP ★0,1
    proposed_event_timeframe = fields.Char('ProposedEventTimeframe')  # 提案イベント時間帯 AQ
    # cost = fields.Integer('Field2__c')  # コスト AR ★空白のみ
    # bill_amount = fields.Integer('Field3__c')  # 請求額 AS ★空白のみ
    kpi1 = fields.Char('KPI_1__c')  # KPI項目 AT
    f = fields.Char('KPI__c')  # F AU
    study_meeting_count = fields.Integer('Field4__c')  # 勉強会人数 AV
    campaign_id = fields.Char('campaign_5__c')  # 関連先(キャンペーン)id AW
    situation = fields.Char('Field1__c')  # 状況 AX
    sr = fields.Char('SR__c')  # SR AY
    new_sales = fields.Boolean('new_customer_2__c')  # 新規営業 AZ ★0,1,空白
    belongs = fields.Char('Field7__c')  # 所属 BA
    client_id = fields.Char('Field8__c')  # 関連先(取引先名)id BB
    visitor_count = fields.Integer('Field10__c')  # 来場人数 BC
    customer_service_staff = fields.Char('Field12__c')  # 接客担当 BD
    # start_datetime = fields.Datetime('Field25__c')  # 開始時間 BE ★空白のみ
    visitor_set_count = fields.Integer('Field11__c')  # 来場組数 BF
    calendar_sales = fields.Char('X2021__c')  # ｶﾚﾝﾀﾞｰ販売 BG
    purchaser = fields.Char('Field24__c')  # 購入者 BH
    payment_method = fields.Boolean('Field26__c')  # クレジット/現金購入 BI ★0,1,空白
    visitor_purpose = fields.Char('Field16__c')  # 来場目的 BJ
    lead = fields.Char('Field17__c')  # リード（来場） BK
    visitor_type = fields.Char('Field18__c')  # 来場者タイプ BL
    estimate_flg = fields.Boolean('Field19__c')  # 事前提案・見積り有 BM ★0,1,空白
    reservation = fields.Char('Field20__c')  # 予約 BN
    with_reservation = fields.Boolean('Field21__c')  # 予約あり BO ★0,1,空白
    no_reservation = fields.Boolean('Field22__c')  # 予約なし BP ★0,1,空白
    guest_book = fields.Char('Field30__c')  # 芳名帳/アンケート BQ
    estimated_accrual = fields.Boolean('Field31__c')  # 見積発生（新規商談） BR ★0,1,空白
    omotesando = fields.Boolean('Field35__c')  # 表参道来店 BS ★0,1,空白

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
