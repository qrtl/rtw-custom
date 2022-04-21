# -*- coding: utf-8 -*-
# from odoo import http


# class ReportCommonRtw(http.Controller):
#     @http.route('/report_common_rtw/report_common_rtw/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_common_rtw/report_common_rtw/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_common_rtw.listing', {
#             'root': '/report_common_rtw/report_common_rtw',
#             'objects': http.request.env['report_common_rtw.report_common_rtw'].search([]),
#         })

#     @http.route('/report_common_rtw/report_common_rtw/objects/<model("report_common_rtw.report_common_rtw"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_common_rtw.object', {
#             'object': obj
#         })
