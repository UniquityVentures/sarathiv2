# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeSyllabusAttachments(http.Controller):
#     @http.route('/bridge_syllabus_attachments/bridge_syllabus_attachments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_syllabus_attachments/bridge_syllabus_attachments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_syllabus_attachments.listing', {
#             'root': '/bridge_syllabus_attachments/bridge_syllabus_attachments',
#             'objects': http.request.env['bridge_syllabus_attachments.bridge_syllabus_attachments'].search([]),
#         })

#     @http.route('/bridge_syllabus_attachments/bridge_syllabus_attachments/objects/<model("bridge_syllabus_attachments.bridge_syllabus_attachments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_syllabus_attachments.object', {
#             'object': obj
#         })

