# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'teachers.teachers'
    _description = 'teachers.teachers'

    code = fields.Char(max_length=50, unique=True)
    qualifications = fields.Text("Qualifications", blank=True, null=True)
