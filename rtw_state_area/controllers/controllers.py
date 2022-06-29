# -*- coding: utf-8 -*-
# from odoo import http


# class RtwStateArea(http.Controller):
#     @http.route('/rtw_state_area/rtw_state_area/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_state_area/rtw_state_area/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_state_area.listing', {
#             'root': '/rtw_state_area/rtw_state_area',
#             'objects': http.request.env['rtw_state_area.rtw_state_area'].search([]),
#         })

#     @http.route('/rtw_state_area/rtw_state_area/objects/<model("rtw_state_area.rtw_state_area"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_state_area.object', {
#             'object': obj
#         })
