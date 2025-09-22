# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Guardian(models.Model):
    _inherit = ["guardian.guardian"]

class Students(models.Model):
    _inherit = ["students.students"]

    guardian1 = fields.Many2one("guardian.guardian")
    guardian2 = fields.Many2one("guardian.guardian")
