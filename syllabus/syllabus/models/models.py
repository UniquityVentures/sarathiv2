# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Syllabus(models.Model):
    _name = 'syllabus.syllabus'
    _description = 'Syllabus'
    _order = 'name'

    name = fields.Char(string='Syllabus Name', required=True)
    overview = fields.Html(string='Overview')
    chapter_ids = fields.One2many(
        'syllabus.chapter', 'syllabus_id', string='Chapters')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Syllabus name must be unique!')
    ]

    def name_get(self):
        return [(record.id, f"{record.name}") for record in self]


class Chapter(models.Model):
    _name = 'syllabus.chapter'
    _description = 'Chapter'
    _order = 'syllabus_id, order, name'

    name = fields.Char(string='Chapter Name', required=True)
    book = fields.Char(string='Book')
    page_range = fields.Char(string='Page Range')
    syllabus_id = fields.Many2one(
        'syllabus.syllabus', string='Syllabus', required=True, ondelete='cascade')
    order = fields.Integer(string='Order', default=0)
    topic_ids = fields.One2many(
        'topic.topic', 'chapter_id', string='Topics')

    _sql_constraints = [
        ('name_syllabus_unique', 'UNIQUE(name, syllabus_id)', 'Chapter name must be unique within the syllabus!')
    ]

