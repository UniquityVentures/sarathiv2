# -*- coding: utf-8 -*-
# from odoo import http


# class Sarathiv2Core(http.Controller):
#     @http.route('/sarathiv2_core/sarathiv2_core', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sarathiv2_core/sarathiv2_core/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sarathiv2_core.listing', {
#             'root': '/sarathiv2_core/sarathiv2_core',
#             'objects': http.request.env['sarathiv2_core.sarathiv2_core'].search([]),
#         })

#     @http.route('/sarathiv2_core/sarathiv2_core/objects/<model("sarathiv2_core.sarathiv2_core"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sarathiv2_core.object', {
#             'object': obj
#         })

