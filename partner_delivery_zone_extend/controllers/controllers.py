# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerDeliveryZoneExtend(http.Controller):
#     @http.route('/partner_delivery_zone_extend/partner_delivery_zone_extend/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_delivery_zone_extend/partner_delivery_zone_extend/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_delivery_zone_extend.listing', {
#             'root': '/partner_delivery_zone_extend/partner_delivery_zone_extend',
#             'objects': http.request.env['partner_delivery_zone_extend.partner_delivery_zone_extend'].search([]),
#         })

#     @http.route('/partner_delivery_zone_extend/partner_delivery_zone_extend/objects/<model("partner_delivery_zone_extend.partner_delivery_zone_extend"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_delivery_zone_extend.object', {
#             'object': obj
#         })
