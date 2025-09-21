# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAnnouncementTeacher(http.Controller):
#     @http.route('/bridge_announcement_teacher/bridge_announcement_teacher', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_announcement_teacher/bridge_announcement_teacher/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_announcement_teacher.listing', {
#             'root': '/bridge_announcement_teacher/bridge_announcement_teacher',
#             'objects': http.request.env['bridge_announcement_teacher.bridge_announcement_teacher'].search([]),
#         })

#     @http.route('/bridge_announcement_teacher/bridge_announcement_teacher/objects/<model("bridge_announcement_teacher.bridge_announcement_teacher"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_announcement_teacher.object', {
#             'object': obj
#         })

