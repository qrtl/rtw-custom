# -*- coding: utf-8 -*-
# from odoo import http


# class ProductMaterialForecast(http.Controller):
#     @http.route('/product_material_forecast/product_material_forecast/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_material_forecast/product_material_forecast/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_material_forecast.listing', {
#             'root': '/product_material_forecast/product_material_forecast',
#             'objects': http.request.env['product_material_forecast.product_material_forecast'].search([]),
#         })

#     @http.route('/product_material_forecast/product_material_forecast/objects/<model("product_material_forecast.product_material_forecast"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_material_forecast.object', {
#             'object': obj
#         })
