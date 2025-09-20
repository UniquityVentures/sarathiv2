# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeCourseTeachers(http.Controller):
#     @http.route('/bridge_course_teachers/bridge_course_teachers', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_course_teachers/bridge_course_teachers/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_course_teachers.listing', {
#             'root': '/bridge_course_teachers/bridge_course_teachers',
#             'objects': http.request.env['bridge_course_teachers.bridge_course_teachers'].search([]),
#         })

#     @http.route('/bridge_course_teachers/bridge_course_teachers/objects/<model("bridge_course_teachers.bridge_course_teachers"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_course_teachers.object', {
#             'object': obj
#         })

