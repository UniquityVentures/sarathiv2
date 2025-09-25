# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Users(models.Model):
    _inherit = ["res.users"]

    semester_ids = fields.Many2many(
        "semester.semester",
        "res_users_semester_rel",
        "user_id",
        "semester_id",
        string="Allowed Semesters",
    )
    semester_id = fields.Many2one(
        "semester.semester",
        string="Current Semester",
        compute="_compute_semester_id",
        inverse="_inverse_semester_id",
        store=True,
    )

    @api.depends("semester_ids")
    def _compute_semester_id(self):
        for user in self:
            try:
                user.semester_id = user.semester_ids[0]
            except Exception:
                user.semester_id = False

    def _inverse_semester_id(self):
        for user in self:
            if user.semester_id:
                user.semester_ids = user.semester_id


class Semester(models.Model):
    _name = "semester.semester"
    _description = "semester.semester"

    name = fields.Char()
    code = fields.Char()
    start = fields.Datetime()
    end = fields.Datetime()
    active = fields.Boolean(default=True)
