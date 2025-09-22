# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAnnouncementSemester(http.Controller):
#     @http.route('/bridge_announcement_semester/bridge_announcement_semester', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_announcement_semester/bridge_announcement_semester/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_announcement_semester.listing', {
#             'root': '/bridge_announcement_semester/bridge_announcement_semester',
#             'objects': http.request.env['bridge_announcement_semester.bridge_announcement_semester'].search([]),
#         })

#     @http.route('/bridge_announcement_semester/bridge_announcement_semester/objects/<model("bridge_announcement_semester.bridge_announcement_semester"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_announcement_semester.object', {
#             'object': obj
#         })

