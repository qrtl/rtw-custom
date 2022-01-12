# -*- coding: utf-8 -*-
# from odoo import http


# class ProductSpecRtw(http.Controller):
#     @http.route('/product_spec_rtw/product_spec_rtw/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_spec_rtw/product_spec_rtw/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_spec_rtw.listing', {
#             'root': '/product_spec_rtw/product_spec_rtw',
#             'objects': http.request.env['product_spec_rtw.product_spec_rtw'].search([]),
#         })

#     @http.route('/product_spec_rtw/product_spec_rtw/objects/<model("product_spec_rtw.product_spec_rtw"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_spec_rtw.object', {
#             'object': obj
#         })
