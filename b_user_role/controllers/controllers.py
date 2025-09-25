# -*- coding: utf-8 -*-
# from odoo import http


# class BUserRole(http.Controller):
#     @http.route('/b_user_role/b_user_role', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/b_user_role/b_user_role/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('b_user_role.listing', {
#             'root': '/b_user_role/b_user_role',
#             'objects': http.request.env['b_user_role.b_user_role'].search([]),
#         })

#     @http.route('/b_user_role/b_user_role/objects/<model("b_user_role.b_user_role"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('b_user_role.object', {
#             'object': obj
#         })

