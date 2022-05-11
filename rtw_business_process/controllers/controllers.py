# -*- coding: utf-8 -*-
# from odoo import http


# class RtwBusinessProcess(http.Controller):
#     @http.route('/rtw_business_process/rtw_business_process/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_business_process/rtw_business_process/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_business_process.listing', {
#             'root': '/rtw_business_process/rtw_business_process',
#             'objects': http.request.env['rtw_business_process.rtw_business_process'].search([]),
#         })

#     @http.route('/rtw_business_process/rtw_business_process/objects/<model("rtw_business_process.rtw_business_process"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_business_process.object', {
#             'object': obj
#         })
