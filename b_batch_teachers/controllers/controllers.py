# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeBatchTeachers(http.Controller):
#     @http.route('/bridge_batch_teachers/bridge_batch_teachers', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_batch_teachers/bridge_batch_teachers/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_batch_teachers.listing', {
#             'root': '/bridge_batch_teachers/bridge_batch_teachers',
#             'objects': http.request.env['bridge_batch_teachers.bridge_batch_teachers'].search([]),
#         })

#     @http.route('/bridge_batch_teachers/bridge_batch_teachers/objects/<model("bridge_batch_teachers.bridge_batch_teachers"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_batch_teachers.object', {
#             'object': obj
#         })

