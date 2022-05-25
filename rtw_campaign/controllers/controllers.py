# -*- coding: utf-8 -*-
# from odoo import http


# class RtwCampaign(http.Controller):
#     @http.route('/rtw_campaign/rtw_campaign/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rtw_campaign/rtw_campaign/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rtw_campaign.listing', {
#             'root': '/rtw_campaign/rtw_campaign',
#             'objects': http.request.env['rtw_campaign.rtw_campaign'].search([]),
#         })

#     @http.route('/rtw_campaign/rtw_campaign/objects/<model("rtw_campaign.rtw_campaign"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rtw_campaign.object', {
#             'object': obj
#         })
