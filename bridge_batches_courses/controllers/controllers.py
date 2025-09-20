# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeBatchesCourses(http.Controller):
#     @http.route('/bridge_batches_courses/bridge_batches_courses', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_batches_courses/bridge_batches_courses/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_batches_courses.listing', {
#             'root': '/bridge_batches_courses/bridge_batches_courses',
#             'objects': http.request.env['bridge_batches_courses.bridge_batches_courses'].search([]),
#         })

#     @http.route('/bridge_batches_courses/bridge_batches_courses/objects/<model("bridge_batches_courses.bridge_batches_courses"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_batches_courses.object', {
#             'object': obj
#         })

