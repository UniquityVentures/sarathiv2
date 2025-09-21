# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Announcement(models.Model):
    _inherit = 'announcements.announcements'

    semester_id = fields.Many2one(
        'semester.semester', string='Semester', ondelete='cascade')

