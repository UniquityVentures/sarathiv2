# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class bridge_batch_students(models.Model):
#     _name = 'b_batch_students.b_batch_students'
#     _description = 'bridge_batch_students.bridge_batch_students'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Batch(models.Model):
    _inherit = ["batches.batches"]

    students = fields.Many2many("students.students")
