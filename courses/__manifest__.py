# -*- coding: utf-8 -*-
{
    'name': "Courses",
    "license": "LGPL-3",

    'summary': "Course management app",

    'description': """
Course management app
    """,

    'author': "Uniquity Ventures",
    'website': "https://uniquity.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sarathi',
    'version': '0.1',
    'installable': True,
    'application': True,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

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

