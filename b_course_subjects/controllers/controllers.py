# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeCourseSubjects(http.Controller):
#     @http.route('/bridge_course_subjects/bridge_course_subjects', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_course_subjects/bridge_course_subjects/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_course_subjects.listing', {
#             'root': '/bridge_course_subjects/bridge_course_subjects',
#             'objects': http.request.env['bridge_course_subjects.bridge_course_subjects'].search([]),
#         })

#     @http.route('/bridge_course_subjects/bridge_course_subjects/objects/<model("bridge_course_subjects.bridge_course_subjects"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_course_subjects.object', {
#             'object': obj
#         })

