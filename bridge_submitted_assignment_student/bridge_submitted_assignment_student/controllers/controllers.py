# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeSubmittedAssignmentStudent(http.Controller):
#     @http.route('/bridge_submitted_assignment_student/bridge_submitted_assignment_student', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_submitted_assignment_student/bridge_submitted_assignment_student/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_submitted_assignment_student.listing', {
#             'root': '/bridge_submitted_assignment_student/bridge_submitted_assignment_student',
#             'objects': http.request.env['bridge_submitted_assignment_student.bridge_submitted_assignment_student'].search([]),
#         })

#     @http.route('/bridge_submitted_assignment_student/bridge_submitted_assignment_student/objects/<model("bridge_submitted_assignment_student.bridge_submitted_assignment_student"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_submitted_assignment_student.object', {
#             'object': obj
#         })

