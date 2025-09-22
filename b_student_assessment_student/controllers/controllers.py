# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeStudentAssessmentStudent(http.Controller):
#     @http.route('/bridge_student_assessment_student/bridge_student_assessment_student', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_student_assessment_student/bridge_student_assessment_student/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_student_assessment_student.listing', {
#             'root': '/bridge_student_assessment_student/bridge_student_assessment_student',
#             'objects': http.request.env['bridge_student_assessment_student.bridge_student_assessment_student'].search([]),
#         })

#     @http.route('/bridge_student_assessment_student/bridge_student_assessment_student/objects/<model("bridge_student_assessment_student.bridge_student_assessment_student"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_student_assessment_student.object', {
#             'object': obj
#         })

