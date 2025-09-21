# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assessment(models.Model):
    _inherit = 'assessments.assessments'

    course_id = fields.Many2one(
        'courses.courses', string='Course', ondelete='set null')

