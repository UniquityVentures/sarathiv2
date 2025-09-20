# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subject(models.Model):
    _name = 'subject.subject'
    _description = 'subject.subject'

    name = fields.Char()
    code = fields.Char()
    description = fields.Text()

