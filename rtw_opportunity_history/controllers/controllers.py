# -*- coding: utf-8 -*-
# from odoo import http


# class RtwOpportunityHistory(http.Controller):
#     @http.route('/rtw_opportunity_history/rtw_opportunity_history/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_opportunity_history/rtw_opportunity_history/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_opportunity_history.listing', {
#             'root': '/rtw_opportunity_history/rtw_opportunity_history',
#             'objects': http.request.env['rtw_opportunity_history.rtw_opportunity_history'].search([]),
#         })

#     @http.route('/rtw_opportunity_history/rtw_opportunity_history/objects/<model("rtw_opportunity_history.rtw_opportunity_history"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_opportunity_history.object', {
#             'object': obj
#         })
