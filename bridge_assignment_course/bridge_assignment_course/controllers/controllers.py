# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAssignmentCourse(http.Controller):
#     @http.route('/bridge_assignment_course/bridge_assignment_course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_assignment_course/bridge_assignment_course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_assignment_course.listing', {
#             'root': '/bridge_assignment_course/bridge_assignment_course',
#             'objects': http.request.env['bridge_assignment_course.bridge_assignment_course'].search([]),
#         })

#     @http.route('/bridge_assignment_course/bridge_assignment_course/objects/<model("bridge_assignment_course.bridge_assignment_course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_assignment_course.object', {
#             'object': obj
#         })

