# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courses(models.Model):
    _name = "courses.courses"
    _description = "courses.courses"

    name = fields.Char(max_length=200)
    active = fields.Boolean(default=True)
    code = fields.Char(max_length=50)
    description = fields.Text(blank=True, null=True)
    remarks = fields.Text(blank=True, null=True)

