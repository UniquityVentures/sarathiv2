# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Announcement(models.Model):
    _inherit = ["announcements.announcements"]

    course_ids = fields.Many2many(
        'courses.courses', string='Courses')

