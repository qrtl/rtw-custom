# -*- coding: utf-8 -*-
{
    'name': "custom_report_rtw",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account', 'product_spec_rtw'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/report_quotation.xml',
        'report/external_layout.xml',
        'report/internal_layout.xml',
        'report/header_footer.xml',
        'report/mrp.xml',
        'report/invoice.xml',
        'views/views.xml',
        'views/templates.xml',
        # "views/sale_views.xml",
        # "views/assets.xml",
        "views/res_company_view.xml"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
