# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_case(models.Model):
    _name = 'rtw_sf_case'
    _description = 'case'
    _rec_name = "subject"

    partner_ids = fields.Many2one('res.partner')
    contacts = fields.Many2one('res.partner', "Contact", copy=False)  # コンタクト
    accounts = fields.Many2one('res.partner', "Account", copy=False)  # アカウント
    parents = fields.Many2one('rtw_sf_case', "Parents", copy=False)  # 親ケース
    supplied_name = fields.Char('SuppliedName')  # K列
    supplied_email = fields.Char('SuppliedEmail')  # L列
    supplied_phone = fields.Char('SuppliedPhone')  # M列
    supplied_company = fields.Char('SuppliedPhone')  # N列
    type = fields.Char('Type')  # O列
    status = fields.Char('Status')  # ステータス
    reason = fields.Char('Reason')  # 理由
    origin = fields.Char('Origin')  # 発生場所
    is_visible_in_self_service = fields.Boolean('IsVisibleInSelfService')  # 表示確認
    subject = fields.Char('Subject')  # 現象
    priority = fields.Char('Priority')  # 優先順位
    description = fields.Char('Description')  # 説明
    isclosed = fields.Boolean('IsClosed')  # 完了済みフラグ
    closed_date = fields.Datetime('ClosedDate')  # 完了日
    is_escalated = fields.Boolean('IsEscalated')  # エスカレーションフラグ
    has_comments_unread_by_owner = fields.Boolean('HasCommentsUnreadByOwner')  # 所有者によるコメント未読の有無
    has_self_service_comments = fields.Boolean('HasSelfServiceComments')  # セルフサービスコメント
    owner_id = fields.Char('OwnerId')  # 所有者Id
    is_closed_on_create = fields.Boolean('IsClosedOnCreate')  # 作成同時完了フラグ
    is_self_service_closed = fields.Boolean('IsSelfServiceClosed')  # 自己完了
    created_date = fields.Datetime('CreatedDate')  # 作成日
    created_by_id = fields.Char('CreatedById')  # 作成ID
    # description = fields.Char('Description')  # 説明
    # description = fields.Char('Description')  # 説明
    # description = fields.Char('Description')  # 説明



    order_no = fields.Char('Field1__c')

