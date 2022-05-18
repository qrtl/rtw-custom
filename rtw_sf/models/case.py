# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rtw_sf_case(models.Model):
    _name = 'rtw_sf_case'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin'
    ]
    _description = 'case'
    _rec_name = "subject"

    partner_ids = fields.Many2one('res.partner')
    contacts = fields.Many2one('res.partner', "Contact", copy=False)  # コンタクト
    accounts = fields.Many2one('res.partner', "Account", copy=False)  # アカウント
    parents = fields.Many2one('rtw_sf_case', "Parents", copy=False)  # 親ケース
    supplied_name = fields.Char('SuppliedName')  # K列
    supplied_email = fields.Char('SuppliedEmail')  # L列
    supplied_phone = fields.Char('SuppliedPhone')  # M列
    supplied_company = fields.Char('SuppliedCompany')  # N列
    type = fields.Char('Type')  # O列
    status = fields.Selection([('new', '新規'),
                               ('sales_representative_is_responding', '営業担当対応中'),
                               ('sales_representative_response_completed', '営業担当対応完了'),
                               ('under_discussion', '協議中'),
                               ('pending', '保留'),
                               ('under_investigation', '調査中'),
                               ('processing_cost', 'コスト処理中'),
                               ('close', 'クローズ')], string="Status",
                              default='new')  # ステータス
    reason = fields.Char('Reason')  # 理由
    origin = fields.Char('Origin')  # 発生場所 v
    is_visible_in_self_service = fields.Boolean('IsVisibleInSelfService')  # 表示確認
    subject = fields.Char('Subject')  # 現象
    priority = fields.Char('Priority')  # 優先順位 v
    description = fields.Char('Description')  # 説明
    isclosed = fields.Boolean('IsClosed')  # 完了済みフラグ
    closed_date = fields.Datetime('ClosedDate')  # 完了日
    is_escalated = fields.Boolean('IsEscalated')  # エスカレーションフラグ
    has_comments_unread_by_owner = fields.Boolean('HasCommentsUnreadByOwner')  # 所有者によるコメント未読の有無
    has_self_service_comments = fields.Boolean('HasSelfServiceComments')  # セルフサービスコメント
    owner_id = fields.Many2one('res.users', 'OwnerId', default=lambda self: self.env.user)  # 所有者Id
    is_closed_on_create = fields.Boolean('IsClosedOnCreate')  # 作成同時完了フラグ
    is_self_service_closed = fields.Boolean('IsSelfServiceClosed')  # 自己完了
    created_date = fields.Datetime('CreatedDate')  # 作成日
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID
    last_modified_date = fields.Datetime('LastModifiedDate')  # 最終更新日
    last_modified_by_id = fields.Many2one('res.users', 'LastModifiedById')  # 最終更新者
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日 v
    order_no = fields.Char('Field1__c')  # 受注番号
    cope_order_no_1 = fields.Char('X1__c')  # 対処受注番号1
    cope_order_no_2 = fields.Char('X2__c')  # 対処受注番号2
    cope_order_no_3 = fields.Char('X3__c')  # 対処受注番号3
    probate_by_president = fields.Boolean('Field6__c')  # 社長検認
    discoverer = fields.Char('Field52__c')  # 発見者
    opportunity = fields.Char('opportunity__c')  # 商談
    delivery_date = fields.Datetime('Field5__c')  # 納品日
    occurrence_status = fields.Char('Field53__c')  # 発生状況
    accounting_department_probate = fields.Boolean('Field7__c')  # 経理部検認
    sales_department_probate = fields.Boolean('Field8__c')  # 営業部検認
    manufacturing_department_probate = fields.Boolean('Field9__c')  # 製造部検認
    initial_explanation_by_person = fields.Text('Field10__c')  # 初動説明（担当者）
    action_details_by_quality_control = fields.Text('Field11__c')  # 対処内容(品管)
    total_sales = fields.Integer('Field12__c')  # 売上総額
    coping_cost = fields.Integer('Field13__c')  # 対処コスト
    billed_freight_cost = fields.Integer('Field42__c')  # 請求運賃コスト
    carrier = fields.Char('Field54__c')  # 運送･搬入業者
    delivery_prefectures = fields.Char('Field4__c')  # 納品先都道府県
    delivery_municipality = fields.Char('Field55__c')  # 納品先市町村郡
    delivery_type = fields.Char('Field56__c')  # 納品種別
    delivery_product_name = fields.Char('Field57__c')  # 納品物件名
    reporter = fields.Char('Field58__c')  # 通報者
    support = fields.Char('Field59__c')  # 対応
    quality_control_comments = fields.Text('Field60__c')  # 品管コメント
    cause_company_name = fields.Char('Field24__c')  # 原因会社名
    size = fields.Char('Field65__c')  # サイズ
    progress_check = fields.Boolean('Field77__c')  # 進捗確認
    cause_by_quality_control = fields.Char('Field61__c')  # 原因（品管検証）
    double_cause_by_quality_control = fields.Char('Field62__c')  # 重複原因（品管検証）
    cause_person_name = fields.Char('Field30__c')  # 原因担当者名
    billing_coping_cost = fields.Integer('Field31__c')  # 請求対処コスト
    sales_department_comments = fields.Text('Field44__c')  # 営業部コメント
    report_date = fields.Datetime('Field34__c')  # 通報日
    Initial_response_date_by_person = fields.Datetime('Field35__c')  # 初動対応日(担当者)
    Initial_response_date_by_quality_control = fields.Datetime('Field36__c')  # 初動対応日(品管)
    double_cause = fields.Char('Field37__c')  # 重複原因リスト
    follow_up_report_by_person = fields.Text('Field63__c')  # 続報（担当者）
    freight_cost = fields.Integer('Field41__c')  # 運賃コスト
    cooperative_factory_opinion = fields.Text('Field45__c')  # 協力工場見解
    manufacturing_department_status = fields.Char('Field46__c')  # 製造部状況
    product_category = fields.Char('Field47__c')  # 商品カテゴリ
    product_name = fields.Char('Field48__c')  # 商品名
    product_name2 = fields.Many2one('product.template', 'Field48__c')  # 商品名
    product_number = fields.Char('Field49__c')  # 品番
    specification = fields.Char('Field50__c')  # 仕様
    quantity = fields.Integer('Field51__c')  # 数量
    percentage_of_fault = fields.Float('percentage of fault')
    # , compute="_compute_percentage_of_fault")
    final_cost_total_sales = fields.Float('Final cost/total sales')
    # , compute="_compute_final_cost_total_sales")

    # def _compute_percentage_of_fault(self):
    #     for rec in self:
    #         if rec.coping_cost == 0 and rec.freight_cost == 0:
    #             pof = 0
    #         else:
    #             pof = (1 - (rec.billing_coping_cost + rec.billed_freight_cost) / (rec.coping_cost + rec.freight_cost)) * 100
    #         # print(pof)
    #         rec.percentage_of_fault = pof
    #
    # def _compute_final_cost_total_sales(self):
    #     for rec in self:
    #         fcts = (
    #                 (rec.coping_cost + rec.freight_cost)
    #                 -
    #                 (rec.billing_coping_cost + rec.billed_freight_cost)
    #         ) / rec.total_sales * 100
    #         print(fcts)
    #         rec.final_cost_total_sales = fcts
    @api.onchange('contacts')
    def _parents_set(self):
        if self.contacts:
            self.accounts = self.contacts.parent_id
