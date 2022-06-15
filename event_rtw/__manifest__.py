# -*- coding: utf-8 -*-
{
    'name': "event_rtw",

    'summary': """
        event Management""",

    'description': """
        event Management
    """,

    'author': "Leverage",
    'website': "https://leverage-system.jp",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'crm', 'rtw_crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/event_rtw.xml',
        'views/calendar_sr.xml',
        'views/calendar_event.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
