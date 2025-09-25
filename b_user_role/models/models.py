# -*- coding: utf-8 -*-

from odoo import models, fields, api


class User(models.Model):
    _inherit = [ 'res.users' ]

    role = fields.Charfield()
