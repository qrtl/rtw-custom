# -*- coding: utf-8 -*-
# from odoo import http


# class RtwBaseLocationStreet(http.Controller):
#     @http.route('/rtw_base_location_street/rtw_base_location_street/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_base_location_street/rtw_base_location_street/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_base_location_street.listing', {
#             'root': '/rtw_base_location_street/rtw_base_location_street',
#             'objects': http.request.env['rtw_base_location_street.rtw_base_location_street'].search([]),
#         })

#     @http.route('/rtw_base_location_street/rtw_base_location_street/objects/<model("rtw_base_location_street.rtw_base_location_street"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_base_location_street.object', {
#             'object': obj
#         })
