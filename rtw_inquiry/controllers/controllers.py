# -*- coding: utf-8 -*-
# from odoo import http


# class RtwInquiry(http.Controller):
#     @http.route('/rtw_inquiry/rtw_inquiry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_inquiry/rtw_inquiry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_inquiry.listing', {
#             'root': '/rtw_inquiry/rtw_inquiry',
#             'objects': http.request.env['rtw_inquiry.rtw_inquiry'].search([]),
#         })

#     @http.route('/rtw_inquiry/rtw_inquiry/objects/<model("rtw_inquiry.rtw_inquiry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_inquiry.object', {
#             'object': obj
#         })
