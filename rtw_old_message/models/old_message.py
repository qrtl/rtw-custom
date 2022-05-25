# -*- coding: utf-8 -*-

from odoo import models, fields, api


class old_message(models.Model):
    _name = 'rtw.old_message'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin'
    ]
    _description = 'old_message'
    _rec_name = "body"

    feed_item_id = fields.Char("FeedItemId")
    parent_id = fields.Char("ParentId")
    type = fields.Selection([('text_post', 'TextPost'),
                             ('user_status', 'UserStatus'),
                             ('link_post', 'LinkPost'),
                             ('content_post', 'ContentPost')], string='Status',
                            default="user_status")
    created_by_id = fields.Many2one('res.users', 'CreatedById')
    created_date = fields.Datetime('CreatedDate')  # 作成日 Y列
    system_mod_stamp = fields.Datetime('SystemModstamp')  # システム最終更新日
    title = fields.Char("Title")
    body = fields.Html("Body")
    link_url = fields.Char("LinkUrl")
    content_id = fields.Char("ContentId")
    related_record_id = fields.Char("RelatedRecordId")
    inserted_by_id = fields.Char("InsertedById")
    is_rich_text = fields.Char("IsRichText")
