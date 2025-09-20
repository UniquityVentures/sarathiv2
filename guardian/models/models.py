# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Guardian(models.Model):
    _name = 'guardian.guardian'
    _description = 'guardian.guardian'

    name = fields.Char("Parent 1 Name", max_length=300, blank=True)
    email = fields.Char("Parent 1 Email", blank=True)
    phone = fields.Char(
        "Parent 1 Phone number", max_length=20, blank=True
    )
