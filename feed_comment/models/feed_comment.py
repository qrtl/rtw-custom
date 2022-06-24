# -*- coding: utf-8 -*-

from odoo import models, fields, api


class feed_comment(models.Model):
    _name = 'feed.comment'
    _description = 'feed.comment'

    feed_item_id = fields.Char('FeedItemId')  # FeedItemId B
    created_by_id = fields.Many2one('res.users', 'CreatedById')  # 作成ID C
    created_date = fields.Datetime('CreatedDate')  # 作成日 D
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日 E
    revision = fields.Integer('Revision')  # 改版 F ★1,2,3
    last_edit_by_id = fields.Many2one('res.users', 'LastEditById')  # 最終編集者 G
    last_edit_date = fields.Datetime('LastEditDate')  # 最終編集日 H
    comment_body = fields.Text('CommentBody')  # コメント I
    # is_deleted = fields.Integer('IsDeleted')  # 削除フラグ J ★0のみ
    client_oauth_link = fields.Char('ClientOauthLink')  # K ★30000001bXRP300000008OXoのみ
    inserted_by_id = fields.Many2one('res.users', 'InsertedById')  # 添付者 L
    comment_type = fields.Char('CommentType')  # コメントタイプ M
    related_record_id = fields.Char('RelatedRecordId')  # 関連レコードid N
    is_rich_text = fields.Boolean('IsRichText')  # リッチテキスト O ★0,1
    status = fields.Char('Status')  # ステータス P
    # thread_parent_id = fields.Boolean('ThreadParentId')  # 削除フラグ Q ★空白のみ
    thread_level = fields.Integer('ThreadLevel')  # スレッドレベル R ★0,空白
    thread_children_count = fields.Integer('ThreadChildrenCount')  # スレッド子の数 S ★0,空白
    thread_last_updated_date = fields.Datetime('ThreadLastUpdatedDate')  # スレッド最終更新日 T

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
