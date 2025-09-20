# -*- coding: utf-8 -*-

from odoo import models, fields


# class bridge_batch_teachers(models.Model):
#     _name = 'bridge_batch_teachers.bridge_batch_teachers'
#     _description = 'bridge_batch_teachers.bridge_batch_teachers'

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

    teachers = fields.Many2many("teachers.teachers")
