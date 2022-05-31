# -*- coding: utf-8 -*-
# from odoo import http


# class RtwShinsei(http.Controller):
#     @http.route('/rtw_shinsei/rtw_shinsei/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_shinsei/rtw_shinsei/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_shinsei.listing', {
#             'root': '/rtw_shinsei/rtw_shinsei',
#             'objects': http.request.env['rtw_shinsei.rtw_shinsei'].search([]),
#         })

#     @http.route('/rtw_shinsei/rtw_shinsei/objects/<model("rtw_shinsei.rtw_shinsei"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_shinsei.object', {
#             'object': obj
#         })
