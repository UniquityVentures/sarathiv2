# -*- coding: utf-8 -*-
{
    'name': "Bridge Assessment Course",

    'summary': "Bridge module for Assessments and Courses",

    'description': """
Bridge module to link Assessments with Courses.
    """,

    'author': "Uniquity Ventures",
    'website': "https://uniquity.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sarathi',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'assessments', 'courses'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

