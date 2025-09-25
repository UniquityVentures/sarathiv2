# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courses(models.Model):
    _name = "courses.courses"
    _description = "courses.courses"

    name = fields.Char()
    active = fields.Boolean(default=True)
    code = fields.Char()
    description = fields.Text()
    remarks = fields.Text()

