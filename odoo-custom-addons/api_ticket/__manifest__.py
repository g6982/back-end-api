# -*- coding: utf-8 -*-
{
    'name': "api_ticket",

    'summary': """
        REST API Odoo Helpdesk""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Aziz Adi Nugroho",
    'website': "https://medium.com/@azizadingrh",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "helpdesk_mgmt","base_rest_auth_api_key","base_rest_datamodel"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
}
