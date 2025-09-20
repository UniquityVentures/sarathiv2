# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Students(models.Model):
    _name = 'students.students'
    _description = 'students.students'

    name = fields.Text()

    student_no = fields.Char(max_length=50, unique=True)
    adhaar_no = fields.Char(max_length=50, null=True, blank=True)
    dob = fields.Datetime(blank=True, null=True)
    gender = fields.Char(max_length=50, null=True, blank=True)
    nationality = fields.Char(max_length=50, null=True, blank=True)
    mother_tongue = fields.Char(max_length=50, null=True, blank=True)
    religion = fields.Char(max_length=50, null=True, blank=True)
    caste = fields.Char(max_length=50, null=True, blank=True)
    category = fields.Char(max_length=50, null=True, blank=True)
    special_needs = fields.Text(blank=True, null=True)
    address = fields.Text(blank=True, null=True)

    # Previous School Details
    prev_school_name = fields.Char(max_length=50, null=True, blank=True)
    prev_school_address = fields.Text(blank=True, null=True)
    prev_school_class = fields.Char(max_length=50, null=True, blank=True)
    prev_school_pass_date = fields.Datetime(blank=True, null=True)
    prev_school_udise_code = fields.Char(max_length=50, null=True, blank=True)

