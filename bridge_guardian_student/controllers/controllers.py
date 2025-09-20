# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeGuardianStudent(http.Controller):
#     @http.route('/bridge_guardian_student/bridge_guardian_student', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_guardian_student/bridge_guardian_student/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_guardian_student.listing', {
#             'root': '/bridge_guardian_student/bridge_guardian_student',
#             'objects': http.request.env['bridge_guardian_student.bridge_guardian_student'].search([]),
#         })

#     @http.route('/bridge_guardian_student/bridge_guardian_student/objects/<model("bridge_guardian_student.bridge_guardian_student"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_guardian_student.object', {
#             'object': obj
#         })

