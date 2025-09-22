# -*- coding: utf-8 -*-
{
    'name': "Assessments",

    'summary': "Module for Management of Assessments",

    'description': """
Module for Management of Assessments
    """,

    'author': "Uniquity Ventures",
    'website': "https://uniquity.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sarathi',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'topic'],

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

