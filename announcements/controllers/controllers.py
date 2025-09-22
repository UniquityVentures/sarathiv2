# -*- coding: utf-8 -*-
# from odoo import http


# class Announcements(http.Controller):
#     @http.route('/announcements/announcements', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/announcements/announcements/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('announcements.listing', {
#             'root': '/announcements/announcements',
#             'objects': http.request.env['announcements.announcements'].search([]),
#         })

#     @http.route('/announcements/announcements/objects/<model("announcements.announcements"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('announcements.object', {
#             'object': obj
#         })

