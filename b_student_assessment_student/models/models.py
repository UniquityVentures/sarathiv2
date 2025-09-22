# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentAssessment(models.Model):
    _inherit = 'assessments.student_assessment'

    student_id = fields.Many2one(
        'students.students', string='Student', required=True, ondelete='cascade')

