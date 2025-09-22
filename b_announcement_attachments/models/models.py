# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Announcement(models.Model):
    _inherit = ["announcements.announcements"]

    attachment_ids = fields.Many2many(
        'ir.attachment', string='Attachments')

