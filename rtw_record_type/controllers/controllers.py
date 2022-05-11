# -*- coding: utf-8 -*-
# from odoo import http


# class RtwRecordType(http.Controller):
#     @http.route('/rtw_record_type/rtw_record_type/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_record_type/rtw_record_type/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_record_type.listing', {
#             'root': '/rtw_record_type/rtw_record_type',
#             'objects': http.request.env['rtw_record_type.rtw_record_type'].search([]),
#         })

#     @http.route('/rtw_record_type/rtw_record_type/objects/<model("rtw_record_type.rtw_record_type"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_record_type.object', {
#             'object': obj
#         })
