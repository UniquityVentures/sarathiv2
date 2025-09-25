# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assessment(models.Model):
    _inherit = [ 'assessments.assessments' ]

    created_by_id = fields.Many2one(
        'teachers.teachers', string='Created By', ondelete='set null')

