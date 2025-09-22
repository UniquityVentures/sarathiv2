# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAssessmentCourse(http.Controller):
#     @http.route('/bridge_assessment_course/bridge_assessment_course', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_assessment_course/bridge_assessment_course/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_assessment_course.listing', {
#             'root': '/bridge_assessment_course/bridge_assessment_course',
#             'objects': http.request.env['bridge_assessment_course.bridge_assessment_course'].search([]),
#         })

#     @http.route('/bridge_assessment_course/bridge_assessment_course/objects/<model("bridge_assessment_course.bridge_assessment_course"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_assessment_course.object', {
#             'object': obj
#         })

