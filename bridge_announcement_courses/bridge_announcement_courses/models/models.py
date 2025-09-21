# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BridgeAnnouncementCourses(models.Model):
    _name = 'bridge_announcement_courses.bridge_announcement_courses'
    _description = 'Bridge Announcement Courses'

    announcement_id = fields.Many2one(
        'announcements.announcements', string='Announcement', required=True, ondelete='cascade')
    course_id = fields.Many2one(
        'courses.courses', string='Course', required=True, ondelete='cascade')

    _sql_constraints = [
        ('announcement_course_unique', 'UNIQUE(announcement_id, course_id)', 'Announcement and Course combination must be unique!')
    ]

