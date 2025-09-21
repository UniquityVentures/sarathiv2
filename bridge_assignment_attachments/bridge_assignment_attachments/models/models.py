# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BridgeAssignmentAttachments(models.Model):
    _name = 'bridge_assignment_attachments.bridge_assignment_attachments'
    _description = 'Bridge Assignment Attachments'

    assignment_id = fields.Many2one(
        'assignments.assignment', string='Assignment', required=True, ondelete='cascade')
    attachment_id = fields.Many2one(
        'ir.attachment', string='Attachment', required=True, ondelete='cascade')

    _sql_constraints = [
        ('assignment_attachment_unique', 'UNIQUE(assignment_id, attachment_id)', 'Assignment and Attachment combination must be unique!')
    ]

