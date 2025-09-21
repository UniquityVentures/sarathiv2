# -*- coding: utf-8 -*-
# from odoo import http


# class Syllabus(http.Controller):
#     @http.route('/syllabus/syllabus', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syllabus/syllabus/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('syllabus.listing', {
#             'root': '/syllabus/syllabus',
#             'objects': http.request.env['syllabus.syllabus'].search([]),
#         })

#     @http.route('/syllabus/syllabus/objects/<model("syllabus.syllabus"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syllabus.object', {
#             'object': obj
#         })

