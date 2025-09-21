# -*- coding: utf-8 -*-
# from odoo import http


# class Assessments(http.Controller):
#     @http.route('/assessments/assessments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/assessments/assessments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('assessments.listing', {
#             'root': '/assessments/assessments',
#             'objects': http.request.env['assessments.assessments'].search([]),
#         })

#     @http.route('/assessments/assessments/objects/<model("assessments.assessments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('assessments.object', {
#             'object': obj
#         })

