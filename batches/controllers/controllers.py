# -*- coding: utf-8 -*-
# from odoo import http


# class Batches(http.Controller):
#     @http.route('/batches/batches', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/batches/batches/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('batches.listing', {
#             'root': '/batches/batches',
#             'objects': http.request.env['batches.batches'].search([]),
#         })

#     @http.route('/batches/batches/objects/<model("batches.batches"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('batches.object', {
#             'object': obj
#         })

