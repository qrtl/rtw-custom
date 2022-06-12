# -*- coding: utf-8 -*-
# from odoo import http


# class RtwExId(http.Controller):
#     @http.route('/rtw_ex_id/rtw_ex_id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_ex_id/rtw_ex_id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_ex_id.listing', {
#             'root': '/rtw_ex_id/rtw_ex_id',
#             'objects': http.request.env['rtw_ex_id.rtw_ex_id'].search([]),
#         })

#     @http.route('/rtw_ex_id/rtw_ex_id/objects/<model("rtw_ex_id.rtw_ex_id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_ex_id.object', {
#             'object': obj
#         })
