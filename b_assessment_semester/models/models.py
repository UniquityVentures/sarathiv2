# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assessment(models.Model):
    _inherit = [ 'assessments.assessments' ]

    semester_id = fields.Many2one(
        'semester.semester', string='Semester', ondelete='cascade')

