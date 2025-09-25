# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Students(models.Model):
    _name = 'students.students'
    _description = 'students.students'

    name = fields.Text()

    student_no = fields.Char()
    adhaar_no = fields.Char()
    dob = fields.Datetime()
    gender = fields.Char()
    nationality = fields.Char()
    mother_tongue = fields.Char()
    religion = fields.Char()
    caste = fields.Char()
    category = fields.Char()
    special_needs = fields.Text()
    address = fields.Text()

    # Previous School Details
    prev_school_name = fields.Char()
    prev_school_address = fields.Text()
    prev_school_class = fields.Char()
    prev_school_pass_date = fields.Datetime()
    prev_school_udise_code = fields.Char()

