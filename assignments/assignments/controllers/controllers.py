# -*- coding: utf-8 -*-
# from odoo import http


# class Assignments(http.Controller):
#     @http.route('/assignments/assignments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assignments/assignments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('assignments.listing', {
#             'root': '/assignments/assignments',
#             'objects': http.request.env['assignments.assignments'].search([]),
#         })

#     @http.route('/assignments/assignments/objects/<model("assignments.assignments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assignments.object', {
#             'object': obj
#         })

