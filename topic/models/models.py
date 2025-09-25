# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Topic(models.Model):
    _name = "topic.topic"
    _description = "Topic"
    _order = "name"

    name = fields.Char(string="Topic Name", required=True)
    code = fields.Char(string="Code", copy=False)
    description = fields.Text(string="Description")
    chapter_id = fields.Many2one(
        "syllabus.chapter", string="Chapter", required=True, ondelete="cascade"
    )

    _sql_constraints = [
        ("code_unique", "UNIQUE(code)", "Topic Code must be unique!"),
        (
            "name_chapter_unique",
            "UNIQUE(name, chapter_id)",
            "Topic name must be unique within the chapter!",
        ),
    ]

    def name_get(self):
        return [(record.id, f"{record.name}") for record in self]
