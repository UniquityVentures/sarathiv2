# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAnnouncementCourses(http.Controller):
#     @http.route('/bridge_announcement_courses/bridge_announcement_courses', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_announcement_courses/bridge_announcement_courses/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_announcement_courses.listing', {
#             'root': '/bridge_announcement_courses/bridge_announcement_courses',
#             'objects': http.request.env['bridge_announcement_courses.bridge_announcement_courses'].search([]),
#         })

#     @http.route('/bridge_announcement_courses/bridge_announcement_courses/objects/<model("bridge_announcement_courses.bridge_announcement_courses"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_announcement_courses.object', {
#             'object': obj
#         })

