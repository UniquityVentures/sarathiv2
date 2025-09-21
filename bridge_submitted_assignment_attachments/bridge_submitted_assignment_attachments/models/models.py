# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BridgeSubmittedAssignmentAttachments(models.Model):
    _name = 'bridge_submitted_assignment_attachments.bridge_submitted_assignment_attachments'
    _description = 'Bridge Submitted Assignment Attachments'

    submitted_assignment_id = fields.Many2one(
        'assignments.submitted_assignment', string='Submitted Assignment', required=True, ondelete='cascade')
    attachment_id = fields.Many2one(
        'ir.attachment', string='Attachment', required=True, ondelete='cascade')

    _sql_constraints = [
        ('submitted_assignment_attachment_unique', 'UNIQUE(submitted_assignment_id, attachment_id)', 'Submitted Assignment and Attachment combination must be unique!')
    ]

