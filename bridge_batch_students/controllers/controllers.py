# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeBatchStudents(http.Controller):
#     @http.route('/bridge_batch_students/bridge_batch_students', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_batch_students/bridge_batch_students/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_batch_students.listing', {
#             'root': '/bridge_batch_students/bridge_batch_students',
#             'objects': http.request.env['bridge_batch_students.bridge_batch_students'].search([]),
#         })

#     @http.route('/bridge_batch_students/bridge_batch_students/objects/<model("bridge_batch_students.bridge_batch_students"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_batch_students.object', {
#             'object': obj
#         })

