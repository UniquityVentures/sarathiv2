# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Announcement(models.Model):
    _inherit = 'announcements.announcements'

    created_by_id = fields.Many2one(
        'teachers.teachers', string='Created By', ondelete='set null')
    signed_by_id = fields.Many2one(
        'teachers.teachers', string='Signed By', ondelete='set null')

