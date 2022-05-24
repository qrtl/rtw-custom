# -*- coding: utf-8 -*-
# from odoo import http


# class RtwOldMessage(http.Controller):
#     @http.route('/rtw_old_message/rtw_old_message/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_old_message/rtw_old_message/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_old_message.listing', {
#             'root': '/rtw_old_message/rtw_old_message',
#             'objects': http.request.env['rtw_old_message.rtw_old_message'].search([]),
#         })

#     @http.route('/rtw_old_message/rtw_old_message/objects/<model("rtw_old_message.rtw_old_message"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_old_message.object', {
#             'object': obj
#         })
