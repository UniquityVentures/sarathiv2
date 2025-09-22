# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Assignment(models.Model):
    _name = 'assignments.assignment'
    _description = 'Assignment'
    _order = 'release_at desc'

    title = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    release_at = fields.Datetime(string='Release Date', default=fields.Datetime.now)
    due_at = fields.Datetime(string='Due Date')
    total_marks = fields.Integer(string='Total Marks', required=True)
    type = fields.Selection([('Online', 'Online'), ('Offline', 'Offline')], string='Type', default='Online')

    is_active = fields.Boolean(string='Active', compute='_compute_is_active', store=True)
    submitted_assignment_ids = fields.One2many(
        'assignments.submitted_assignment', 'assignment_id', string='Submissions')

    @api.depends('release_at', 'due_at')
    def _compute_is_active(self):
        now_datetime = datetime.now()
        for record in self:
            if record.release_at and record.due_at:
                record.is_active = record.release_at < now_datetime < record.due_at
            else:
                record.is_active = False

    _sql_constraints = [
        ('title_unique', 'UNIQUE(title)', 'Assignment title must be unique!'),
        ('total_marks_positive', 'CHECK(total_marks > 0)', 'Total Marks must be positive!')
    ]

    @api.constrains('release_at', 'due_at')
    def _check_dates(self):
        for record in self:
            if record.release_at and record.due_at and record.due_at < record.release_at:
                raise ValidationError("Due Date cannot be before Release Date.")

    def name_get(self):
        return [(record.id, f"{record.title}") for record in self]


class SubmittedAssignment(models.Model):
    _name = 'assignments.submitted_assignment'
    _description = 'Submitted Assignment'

    assignment_id = fields.Many2one(
        'assignments.assignment', string='Assignment', required=True, ondelete='cascade')
    marks = fields.Integer(string='Marks Obtained') # null=True and blank=True from original, but Odoo defaults to 0
    content = fields.Html(string='Content')
    submission_datetime = fields.Datetime(string='Submission Date/Time', default=fields.Datetime.now)
    remarks = fields.Text(string='Remarks')

    status = fields.Selection([('Submitted', 'Submitted'), ('Late', 'Late')], string='Status', compute='_compute_status', store=True)

    @api.depends('submission_datetime', 'assignment_id.due_at')
    def _compute_status(self):
        for record in self:
            if record.submission_datetime and record.assignment_id and record.assignment_id.due_at:
                if record.submission_datetime > record.assignment_id.due_at:
                    record.status = 'Late'
                else:
                    record.status = 'Submitted'
            else:
                record.status = False

    @api.constrains('marks', 'assignment_id.total_marks')
    def _check_marks_valid(self):
        for record in self:
            if record.marks is not False and record.marks < 0:
                raise ValidationError("Marks obtained cannot be negative.")
            if record.marks is not False and record.assignment_id and record.marks > record.assignment_id.total_marks:
                raise ValidationError(f"Marks obtained cannot be greater than the total marks ({record.assignment_id.total_marks}).")

