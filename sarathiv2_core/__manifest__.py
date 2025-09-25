# -*- coding: utf-8 -*-
{
    "name": "Sarathiv2 Core",
    "license": "LGPL-3",
    "summary": "All Apps",
    "description": """
All Apps for core
    """,
    "author": "Uniquity Ventures",
    "website": "https://uniquity.in",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sarathi",
    "version": "0.1",
    'installable': True,
    'application': True,
    'auto_install': True,
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "b_announcement_attachments",
        "b_announcement_batches",
        "b_announcement_courses",
        "b_announcement_teacher",
        "b_assessment_course",
        "b_assessment_teacher",
        "b_assessment_topic",
        "b_assignment_attachments",
        "b_assignment_course",
        "b_assignment_teacher",
        "b_batch_section",
        "b_batch_students",
        "b_batch_teachers",
        "b_batches_courses",
        "b_course_students",
        "b_course_subjects",
        "b_course_teachers",
        "b_guardian_student",
        "b_student_assessment_student",
        "b_submitted_assignment_attachments",
        "b_submitted_assignment_student",
        "b_syllabus_attachments",
        "b_syllabus_course",
    ],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
