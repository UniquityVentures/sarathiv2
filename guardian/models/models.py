# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Guardian(models.Model):
    _name = "guardian.guardian"
    _description = "guardian.guardian"

    name = fields.Char("Parent 1 Name")
    email = fields.Char("Parent 1 Email")
    phone = fields.Char(
        "Parent 1 Phone number",
    )
