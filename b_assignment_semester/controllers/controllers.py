# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAssignmentSemester(http.Controller):
#     @http.route('/bridge_assignment_semester/bridge_assignment_semester', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_assignment_semester/bridge_assignment_semester/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_assignment_semester.listing', {
#             'root': '/bridge_assignment_semester/bridge_assignment_semester',
#             'objects': http.request.env['bridge_assignment_semester.bridge_assignment_semester'].search([]),
#         })

#     @http.route('/bridge_assignment_semester/bridge_assignment_semester/objects/<model("bridge_assignment_semester.bridge_assignment_semester"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_assignment_semester.object', {
#             'object': obj
#         })

