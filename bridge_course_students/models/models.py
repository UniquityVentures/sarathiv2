# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class bridge_course_students(models.Model):
#     _name = 'bridge_course_students.bridge_course_students'
#     _description = 'bridge_course_students.bridge_course_students'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class Course(models.Model):
    _inherit = ["courses.courses"]

    students = fields.Many2many("students.students")
