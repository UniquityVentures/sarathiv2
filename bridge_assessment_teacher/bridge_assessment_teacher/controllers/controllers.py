# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAssessmentTeacher(http.Controller):
#     @http.route('/bridge_assessment_teacher/bridge_assessment_teacher', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_assessment_teacher/bridge_assessment_teacher/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_assessment_teacher.listing', {
#             'root': '/bridge_assessment_teacher/bridge_assessment_teacher',
#             'objects': http.request.env['bridge_assessment_teacher.bridge_assessment_teacher'].search([]),
#         })

#     @http.route('/bridge_assessment_teacher/bridge_assessment_teacher/objects/<model("bridge_assessment_teacher.bridge_assessment_teacher"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_assessment_teacher.object', {
#             'object': obj
#         })

