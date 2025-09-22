# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Assessment(models.Model):
    _name = "assessments.assessments"
    _description = "Assessment"
    _order = "datetime desc"

    title = fields.Char(string="Title", required=True)
    description = fields.Html(string="Description")
    is_active = fields.Boolean(string="Active", default=True)
    syllabus = fields.Text(string="Syllabus")
    datetime = fields.Datetime(string="Date & Time", required=True)
    venue = fields.Char(string="Venue")
    max_marks = fields.Integer(string="Maximum Marks", required=True)
    passing_marks = fields.Integer(string="Passing Marks", required=True)

    student_assessment_ids = fields.One2many(
        "assessments.student_assessment",
        "assessment_id",
        string="Assessment",
    )

    _sql_constraints = [
        ("title_unique", "UNIQUE(title)", "Assessment title must be unique!"),
        (
            "max_marks_positive",
            "CHECK(max_marks > 0)",
            "Maximum Marks must be positive!",
        ),
        (
            "passing_marks_valid",
            "CHECK(passing_marks >= 0 AND passing_marks <= max_marks)",
            "Passing Marks must be between 0 and Maximum Marks!",
        ),
    ]

    def name_get(self):
        return [(record.id, f"{record.title}") for record in self]


class StudentAssessment(models.Model):
    _name = "assessments.student_assessment"
    _description = "Student Assessment"

    assessment_id = fields.Many2one(
        "assessments.assessments",
        string="Assessment",
        required=True,
        ondelete="cascade",
    )
    marks = fields.Integer(string="Marks Obtained", required=True)
    status = fields.Selection(
        [("PASS", "Pass"), ("FAIL", "Fail")],
        string="Status",
        compute="_compute_status",
        store=True,
    )
    remarks = fields.Text(string="Remarks")

    @api.depends("marks", "assessment_id.passing_marks")
    def _compute_status(self):
        for record in self:
            if record.assessment_id and record.marks is not False:
                if record.marks >= record.assessment_id.passing_marks:
                    record.status = "PASS"
                else:
                    record.status = "FAIL"
            else:
                record.status = False

    @api.constrains("marks", "assessment_id.max_marks")
    def _check_marks_valid(self):
        for record in self:
            if (
                record.marks is not False
                and record.assessment_id
                and record.marks > record.assessment_id.max_marks
            ):
                raise ValidationError(
                    "Marks obtained cannot be greater than Maximum Marks."
                )
            if record.marks < 0:
                raise ValidationError("Marks obtained cannot be negative.")
