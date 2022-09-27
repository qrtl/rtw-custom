# -*- coding: utf-8 -*-
# from odoo import http


# class RtwFilterMenu(http.Controller):
#     @http.route('/rtw_filter_menu/rtw_filter_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_filter_menu/rtw_filter_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_filter_menu.listing', {
#             'root': '/rtw_filter_menu/rtw_filter_menu',
#             'objects': http.request.env['rtw_filter_menu.rtw_filter_menu'].search([]),
#         })

#     @http.route('/rtw_filter_menu/rtw_filter_menu/objects/<model("rtw_filter_menu.rtw_filter_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_filter_menu.object', {
#             'object': obj
#         })
