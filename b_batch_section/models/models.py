# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class bridge_batch_section(models.Model):
#     _name = 'b_batch_section.b_batch_section'
#     _description = 'bridge_batch_section.bridge_batch_section'

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

    section = fields.Many2one("section.section")

class Section(models.Model):
    _inherit = ["section.section"]

    batches = fields.One2many("batches.batches", 'section')
