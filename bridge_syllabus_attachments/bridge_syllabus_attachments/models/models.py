# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BridgeSyllabusAttachments(models.Model):
    _name = 'bridge_syllabus_attachments.bridge_syllabus_attachments'
    _description = 'Bridge Syllabus Attachments'

    syllabus_id = fields.Many2one(
        'syllabus.syllabus', string='Syllabus', required=True, ondelete='cascade')
    attachment_id = fields.Many2one(
        'ir.attachment', string='Attachment', required=True, ondelete='cascade')

    _sql_constraints = [
        ('syllabus_attachment_unique', 'UNIQUE(syllabus_id, attachment_id)', 'Syllabus and Attachment combination must be unique!')
    ]

