# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BridgeAssessmentTopic(models.Model):
    _name = 'bridge_assessment_topic.bridge_assessment_topic'
    _description = 'Bridge Assessment Topic'

    assessment_id = fields.Many2one(
        'assessments.assessments', string='Assessment', required=True, ondelete='cascade')
    topic_id = fields.Many2one(
        'topic.topic', string='Topic', required=True, ondelete='cascade')

    _sql_constraints = [
        ('assessment_topic_unique', 'UNIQUE(assessment_id, topic_id)', 'Assessment and Topic combination must be unique!')
    ]

