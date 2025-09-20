# -*- coding: utf-8 -*-
# from odoo import http


# class Section(http.Controller):
#     @http.route('/section/section', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/section/section/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('section.listing', {
#             'root': '/section/section',
#             'objects': http.request.env['section.section'].search([]),
#         })

#     @http.route('/section/section/objects/<model("section.section"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('section.object', {
#             'object': obj
#         })

