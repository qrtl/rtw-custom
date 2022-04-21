# -*- coding: utf-8 -*-
{
    'name': "report_rtw",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kazushi Eguchi (Enzantrades)",
    'website': "http://www.enzantrades.co.j",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        "report/report_invoice_rtw.xml",
        "report/report_unit_price_list_rtw.xml",
        "report/report.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
