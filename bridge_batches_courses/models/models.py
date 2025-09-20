# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Courses(models.Model):
    _inherit = ["courses.courses"]

    batches = fields.Many2many("batches.batches")
