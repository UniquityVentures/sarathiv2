# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Announcement(models.Model):
    _inherit = ["announcements.announcements"]

    batches_ids = fields.Many2many(
        'batches.batches', string='Batches')

