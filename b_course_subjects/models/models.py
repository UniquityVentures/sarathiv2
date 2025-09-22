# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class bridge_course_subjects(models.Model):
#     _name = 'b_course_subjects.b_course_subjects'
#     _description = 'bridge_course_subjects.bridge_course_subjects'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class Courses(models.Model):
    _inherit = ["batches.batches"]

    subject = fields.Many2many("subject.subject")
