# -*- coding: utf-8 -*-
{
    'name': "product_spec_rtw",

    'summary': """
        Short (1 phrase/line)f summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Kazushi Eguchi (Enzantrades)",
    'website': "http://www.enzantrades.co.j",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_template.xml',
        'views/templates.xml',
        'views/sales_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
