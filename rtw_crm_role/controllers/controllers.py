# -*- coding: utf-8 -*-
# from odoo import http


# class RtwCrmRole(http.Controller):
#     @http.route('/rtw_crm_role/rtw_crm_role/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_crm_role/rtw_crm_role/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_crm_role.listing', {
#             'root': '/rtw_crm_role/rtw_crm_role',
#             'objects': http.request.env['rtw_crm_role.rtw_crm_role'].search([]),
#         })

#     @http.route('/rtw_crm_role/rtw_crm_role/objects/<model("rtw_crm_role.rtw_crm_role"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_crm_role.object', {
#             'object': obj
#         })
