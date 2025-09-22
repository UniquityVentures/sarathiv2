# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class bridge_batch_semester(models.Model):
#     _name = 'b_batch_semester.b_batch_semester'
#     _description = 'bridge_batch_semester.bridge_batch_semester'

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

    semester = fields.Many2one("semester.semester")
