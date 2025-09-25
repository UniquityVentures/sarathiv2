# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assignment(models.Model):
    _inherit = [ 'assignments.assignment' ]

    created_by_id = fields.Many2one(
        'teachers.teachers', string='Created By', ondelete='cascade')

