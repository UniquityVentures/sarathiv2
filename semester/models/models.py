# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Semester(models.Model):
    _name = 'semester.semester'
    _description = 'semester.semester'
 
    name = fields.Char(max_length=250)
    code = fields.Char(max_length=50, unique=True, null=True)
    start = fields.Datetime()
    end = fields.Datetime()
    active = fields.Boolean(default=True)

