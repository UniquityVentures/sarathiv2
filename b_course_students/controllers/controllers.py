# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeCourseStudents(http.Controller):
#     @http.route('/bridge_course_students/bridge_course_students', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_course_students/bridge_course_students/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_course_students.listing', {
#             'root': '/bridge_course_students/bridge_course_students',
#             'objects': http.request.env['bridge_course_students.bridge_course_students'].search([]),
#         })

#     @http.route('/bridge_course_students/bridge_course_students/objects/<model("bridge_course_students.bridge_course_students"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_course_students.object', {
#             'object': obj
#         })

