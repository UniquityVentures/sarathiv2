# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SubmittedAssignment(models.Model):
    _inherit = 'assignments.submitted_assignment'

    student_id = fields.Many2one(
        'students.students', string='Student', required=True, ondelete='cascade')

    _sql_constraints = [
        ('student_assignment_unique', 'UNIQUE(student_id, assignment_id)', 'Student and Assignment combination must be unique!')
    ]

