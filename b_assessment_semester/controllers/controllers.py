# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAssessmentSemester(http.Controller):
#     @http.route('/bridge_assessment_semester/bridge_assessment_semester', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_assessment_semester/bridge_assessment_semester/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_assessment_semester.listing', {
#             'root': '/bridge_assessment_semester/bridge_assessment_semester',
#             'objects': http.request.env['bridge_assessment_semester.bridge_assessment_semester'].search([]),
#         })

#     @http.route('/bridge_assessment_semester/bridge_assessment_semester/objects/<model("bridge_assessment_semester.bridge_assessment_semester"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_assessment_semester.object', {
#             'object': obj
#         })

