# -*- coding: utf-8 -*-
# from odoo import http


# class RtwGc(http.Controller):
#     @http.route('/rtw_gc/rtw_gc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_gc/rtw_gc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_gc.listing', {
#             'root': '/rtw_gc/rtw_gc',
#             'objects': http.request.env['rtw_gc.rtw_gc'].search([]),
#         })

#     @http.route('/rtw_gc/rtw_gc/objects/<model("rtw_gc.rtw_gc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_gc.object', {
#             'object': obj
#         })
