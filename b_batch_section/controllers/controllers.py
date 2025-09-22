# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeBatchSection(http.Controller):
#     @http.route('/bridge_batch_section/bridge_batch_section', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_batch_section/bridge_batch_section/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_batch_section.listing', {
#             'root': '/bridge_batch_section/bridge_batch_section',
#             'objects': http.request.env['bridge_batch_section.bridge_batch_section'].search([]),
#         })

#     @http.route('/bridge_batch_section/bridge_batch_section/objects/<model("bridge_batch_section.bridge_batch_section"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_batch_section.object', {
#             'object': obj
#         })

