# -*- coding: utf-8 -*-
{
    "name": "Semester",
    "license": "LGPL-3",
    "summary": "App for managing Semester",
    "description": """
App for managing Semester
    """,
    "author": "Uniquity Ventures",
    "website": "https://uniquity.in",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sarathi",
    "version": "0.1",
    "installable": True,
    "application": True,
    "auto_install": True,
    # any module necessary for this one to work correctly
    "depends": ["base", "web"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "semester/src/static/webclient.js",
            "semester/src/static/switch_semester_item.js",
            "semester/src/static/switch_semester_menu.js",
        ],
        "web.assets_backend": [
            "semester/src/static/switch_semester_item.xml",
            "semester/src/static/switch_semester_menu.xml",
        ],
    },
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
