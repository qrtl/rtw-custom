# -*- coding: utf-8 -*-

from odoo import models, fields, api


class opportunity(models.Model):
    _name = 'opportunity.stage'
    _description = 'opportunity stage'

    accounts = fields.Many2one('res.partner', "Account", copy=False)  # アカウント
    name = fields.Char('Name')  # 名称　E列
    Description = fields.Text('Description')  # 説明　F列
    stage_name = fields.Char('StageName')  # 段階名　G列
    stage_sort_order = fields.Integer('StageSortOrder')  # 受注段階コード　H列
    amount = fields.Float('Amount')  # 金額　I列
    probability = fields.Integer('Probability')  # 確率　J列
    expected_revenue = fields.Float('ExpectedRevenue')  # 予想売上高　K列
    # total_opportunity_quantity = fields.Float('TotalOpportunityQuantity')  # 契約金額合計　L列
    close_date = fields.Datetime('CloseDate')  # 完了日　M列

    is_visible_in_self_service = fields.Boolean('IsVisibleInSelfService')  # 表示確認
    subject = fields.Char('Subject')  # 現象
    priority = fields.Char('Priority')  # 優先順位
    description = fields.Char('Description')  # 説明
    isclosed = fields.Boolean('IsClosed')  # 完了済みフラグ
    closed_date = fields.Datetime('ClosedDate')  # 完了日
    is_escalated = fields.Boolean('IsEscalated')  # エスカレーションフラグ
    name = fields.Char()
    no = fields.Char("license plate number", store=True)
    # size = fields.Char("size")
    length = fields.Float("length")
    wide = fields.Float("wide")
    height = fields.Float("height")
    memo = fields.Text("memo")
    image = fields.Binary("image")
    size = fields.Many2one("car.size", string="size")
    customer = fields.Many2one("res.partner", string="customer")

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
