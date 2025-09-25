# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assignment(models.Model):
    _inherit = [ 'assignments.assignment' ]

    course_id = fields.Many2one(
        'courses.courses', string='Course', required=True, ondelete='cascade')

