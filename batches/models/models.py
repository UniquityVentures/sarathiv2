# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Batches(models.Model):
    _name = 'batches.batches'
    _description = 'batches.batches'

    name = fields.Char()

    active = fields.Boolean()

    description = fields.Text()
    code = fields.Char(max_length=50)
