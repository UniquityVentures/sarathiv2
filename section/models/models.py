# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Section(models.Model):
    _name = 'section.section'
    _description = 'section.section'

    name = fields.Char()
    description = fields.Text()

