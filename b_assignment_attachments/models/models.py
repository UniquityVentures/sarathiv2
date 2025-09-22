# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assignment(models.Model):
    _inherit = ["assignments.assignment"]

    attachment_ids = fields.Many2many(
        'ir.attachment', string='Attachments')

