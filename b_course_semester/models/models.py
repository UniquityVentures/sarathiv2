# -*- coding: utf-8 -*-

from odoo import models, fields


# class bridge_course_semester(models.Model):
#     _name = 'b_course_semester.b_course_semester'
#     _description = 'bridge_course_semester.bridge_course_semester'

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

    semester = fields.Many2one("semester.semester")
