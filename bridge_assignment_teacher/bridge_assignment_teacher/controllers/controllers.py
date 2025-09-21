# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAssignmentTeacher(http.Controller):
#     @http.route('/bridge_assignment_teacher/bridge_assignment_teacher', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_assignment_teacher/bridge_assignment_teacher/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_assignment_teacher.listing', {
#             'root': '/bridge_assignment_teacher/bridge_assignment_teacher',
#             'objects': http.request.env['bridge_assignment_teacher.bridge_assignment_teacher'].search([]),
#         })

#     @http.route('/bridge_assignment_teacher/bridge_assignment_teacher/objects/<model("bridge_assignment_teacher.bridge_assignment_teacher"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_assignment_teacher.object', {
#             'object': obj
#         })

