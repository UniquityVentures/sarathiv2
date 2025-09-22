# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Assessment(models.Model):
    _inherit = ["assessments.assessments"]

    topic_ids = fields.Many2many(
        'topic.topic', string='Topics')

