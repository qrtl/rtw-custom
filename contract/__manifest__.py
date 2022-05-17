# -*- coding: utf-8 -*-
{
    'name': "contract",

    'summary': """
        contract Management""",

    'description': """
        contract Management
    """,

    'author': "Leverage",
    'website': "https://leverage-system.jp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'opportunity'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/contract.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
