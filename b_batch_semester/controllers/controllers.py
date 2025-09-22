# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeBatchSemester(http.Controller):
#     @http.route('/bridge_batch_semester/bridge_batch_semester', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_batch_semester/bridge_batch_semester/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_batch_semester.listing', {
#             'root': '/bridge_batch_semester/bridge_batch_semester',
#             'objects': http.request.env['bridge_batch_semester.bridge_batch_semester'].search([]),
#         })

#     @http.route('/bridge_batch_semester/bridge_batch_semester/objects/<model("bridge_batch_semester.bridge_batch_semester"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_batch_semester.object', {
#             'object': obj
#         })

