# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Announcement(models.Model):
    _name = 'announcements.announcements'
    _description = 'Announcements'
    _order = 'release_at desc, priority desc'

    PRIORITY_CHOICES = [
        ('1', 'Low Priority'),
        ('2', 'Medium Priority'),
        ('3', 'High  Priority'),
    ]

    title = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    is_universal = fields.Boolean(string='Universal Announcement', default=False)
    release_at = fields.Datetime(string='Release Date', default=fields.Datetime.now, required=True)
    expiry_at = fields.Datetime(string='Expiry Date')
    priority = fields.Selection(PRIORITY_CHOICES, string='Priority', default='2')

    @api.constrains('release_at', 'expiry_at')
    def _check_dates(self):
        for record in self:
            if record.expiry_at and record.release_at and record.expiry_at < record.release_at:
                raise ValidationError("Expiry Date cannot be before Release Date.")

    def name_get(self):
        return [(record.id, f"{record.title}") for record in self]

    _sql_constraints = [
        ('title_unique', 'UNIQUE(title)', 'Announcement title must be unique!')
    ]

