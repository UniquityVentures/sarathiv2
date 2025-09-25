# -*- coding: utf-8 -*-
{
    "name": "BatchCourseBridge",
    "license": "LGPL-3",
    "summary": "App for bridging functionality between batches and courses",
    "description": """
App for bridging functionality between batches and courses
    """,
    "author": "Uniquity Ventures",
    "website": "https://www.uniquity.in",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sarathi",
    "version": "0.1",
    'installable': True,
    'application': True,
    'auto_install': True,
    # any module necessary for this one to work correctly
    "depends": ["base", "batches", "courses"],
    # always loaded
    "data": [
        'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
