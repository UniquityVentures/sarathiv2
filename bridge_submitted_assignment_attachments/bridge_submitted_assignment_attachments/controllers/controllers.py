# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeSubmittedAssignmentAttachments(http.Controller):
#     @http.route('/bridge_submitted_assignment_attachments/bridge_submitted_assignment_attachments', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_submitted_assignment_attachments/bridge_submitted_assignment_attachments/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_submitted_assignment_attachments.listing', {
#             'root': '/bridge_submitted_assignment_attachments/bridge_submitted_assignment_attachments',
#             'objects': http.request.env['bridge_submitted_assignment_attachments.bridge_submitted_assignment_attachments'].search([]),
#         })

#     @http.route('/bridge_submitted_assignment_attachments/bridge_submitted_assignment_attachments/objects/<model("bridge_submitted_assignment_attachments.bridge_submitted_assignment_attachments"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_submitted_assignment_attachments.object', {
#             'object': obj
#         })

