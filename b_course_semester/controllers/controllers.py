# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeCourseSemester(http.Controller):
#     @http.route('/bridge_course_semester/bridge_course_semester', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_course_semester/bridge_course_semester/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_course_semester.listing', {
#             'root': '/bridge_course_semester/bridge_course_semester',
#             'objects': http.request.env['bridge_course_semester.bridge_course_semester'].search([]),
#         })

#     @http.route('/bridge_course_semester/bridge_course_semester/objects/<model("bridge_course_semester.bridge_course_semester"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_course_semester.object', {
#             'object': obj
#         })

