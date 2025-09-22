# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeSyllabusCourse(http.Controller):
#     @http.route('/bridge_syllabus_course/bridge_syllabus_course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_syllabus_course/bridge_syllabus_course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_syllabus_course.listing', {
#             'root': '/bridge_syllabus_course/bridge_syllabus_course',
#             'objects': http.request.env['bridge_syllabus_course.bridge_syllabus_course'].search([]),
#         })

#     @http.route('/bridge_syllabus_course/bridge_syllabus_course/objects/<model("bridge_syllabus_course.bridge_syllabus_course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_syllabus_course.object', {
#             'object': obj
#         })

