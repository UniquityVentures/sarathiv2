# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'teachers.teachers'
    _description = 'teachers.teachers'

    code = fields.Char()
    qualifications = fields.Text("Qualifications")
