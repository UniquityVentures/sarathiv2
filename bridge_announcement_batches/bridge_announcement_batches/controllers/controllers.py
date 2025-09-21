# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAnnouncementBatches(http.Controller):
#     @http.route('/bridge_announcement_batches/bridge_announcement_batches', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_announcement_batches/bridge_announcement_batches/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_announcement_batches.listing', {
#             'root': '/bridge_announcement_batches/bridge_announcement_batches',
#             'objects': http.request.env['bridge_announcement_batches.bridge_announcement_batches'].search([]),
#         })

#     @http.route('/bridge_announcement_batches/bridge_announcement_batches/objects/<model("bridge_announcement_batches.bridge_announcement_batches"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_announcement_batches.object', {
#             'object': obj
#         })

