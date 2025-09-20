# -*- coding: utf-8 -*-
# from odoo import http


# class Semester(http.Controller):
#     @http.route('/semester/semester', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/semester/semester/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('semester.listing', {
#             'root': '/semester/semester',
#             'objects': http.request.env['semester.semester'].search([]),
#         })

#     @http.route('/semester/semester/objects/<model("semester.semester"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('semester.object', {
#             'object': obj
#         })

