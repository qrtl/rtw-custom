# -*- coding: utf-8 -*-
# from odoo import http


# class RtwCrmRelatedPartner(http.Controller):
#     @http.route('/rtw_crm_related_partner/rtw_crm_related_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_crm_related_partner/rtw_crm_related_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_crm_related_partner.listing', {
#             'root': '/rtw_crm_related_partner/rtw_crm_related_partner',
#             'objects': http.request.env['rtw_crm_related_partner.rtw_crm_related_partner'].search([]),
#         })

#     @http.route('/rtw_crm_related_partner/rtw_crm_related_partner/objects/<model("rtw_crm_related_partner.rtw_crm_related_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_crm_related_partner.object', {
#             'object': obj
#         })
