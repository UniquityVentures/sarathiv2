# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAnnouncementAttachments(http.Controller):
#     @http.route('/bridge_announcement_attachments/bridge_announcement_attachments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_announcement_attachments/bridge_announcement_attachments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_announcement_attachments.listing', {
#             'root': '/bridge_announcement_attachments/bridge_announcement_attachments',
#             'objects': http.request.env['bridge_announcement_attachments.bridge_announcement_attachments'].search([]),
#         })

#     @http.route('/bridge_announcement_attachments/bridge_announcement_attachments/objects/<model("bridge_announcement_attachments.bridge_announcement_attachments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_announcement_attachments.object', {
#             'object': obj
#         })

