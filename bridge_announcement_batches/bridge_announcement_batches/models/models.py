# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BridgeAnnouncementBatches(models.Model):
    _name = 'bridge_announcement_batches.bridge_announcement_batches'
    _description = 'Bridge Announcement Batches'

    announcement_id = fields.Many2one(
        'announcements.announcements', string='Announcement', required=True, ondelete='cascade')
    batch_id = fields.Many2one(
        'batches.batches', string='Batch', required=True, ondelete='cascade')

    _sql_constraints = [
        ('announcement_batch_unique', 'UNIQUE(announcement_id, batch_id)', 'Announcement and Batch combination must be unique!')
    ]

