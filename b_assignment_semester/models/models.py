# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assignment(models.Model):
    _inherit = [ 'assignments.assignment' ]

    semester_id = fields.Many2one(
        'semester.semester', string='Semester', ondelete='cascade')

