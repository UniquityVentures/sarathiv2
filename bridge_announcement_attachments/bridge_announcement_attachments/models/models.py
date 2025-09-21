# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BridgeAnnouncementAttachments(models.Model):
    _name = 'bridge_announcement_attachments.bridge_announcement_attachments'
    _description = 'Bridge Announcement Attachments'

    announcement_id = fields.Many2one(
        'announcements.announcements', string='Announcement', required=True, ondelete='cascade')
    attachment_id = fields.Many2one(
        'ir.attachment', string='Attachment', required=True, ondelete='cascade')

    _sql_constraints = [
        ('announcement_attachment_unique', 'UNIQUE(announcement_id, attachment_id)', 'Announcement and Attachment combination must be unique!')
    ]

