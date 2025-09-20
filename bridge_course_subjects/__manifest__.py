# -*- coding: utf-8 -*-
{
    'name': "Bridge for Course and Subjects",

    'summary': "Bridge for Course and Subjects",

    'description': """
Bridge for Course and Subjects
    """,

    'author': "Uniquity Ventures",
    'website': "https://uniquity.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'courses', 'subject'],

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

