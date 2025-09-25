# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Syllabus(models.Model):
    _inherit = [ 'syllabus.syllabus' ]

    course_id = fields.Many2one(
        'courses.courses', string='Course', required=True, ondelete='cascade')

