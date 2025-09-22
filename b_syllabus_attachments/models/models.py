# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Syllabus(models.Model):
    _inherit = ["syllabus.syllabus"]

    attachment_ids = fields.Many2many(
        'ir.attachment', string='Attachments')

