# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SubmittedAssignment(models.Model):
    _inherit = ["assignments.submitted_assignment"]

    attachment_ids = fields.Many2many(
        'ir.attachment', string='Attachments')

