# -*- coding: utf-8 -*-
# from odoo import http


# class ReportRtw(http.Controller):
#     @http.route('/report_rtw/report_rtw/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_rtw/report_rtw/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_rtw.listing', {
#             'root': '/report_rtw/report_rtw',
#             'objects': http.request.env['report_rtw.report_rtw'].search([]),
#         })

#     @http.route('/report_rtw/report_rtw/objects/<model("report_rtw.report_rtw"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_rtw.object', {
#             'object': obj
#         })
