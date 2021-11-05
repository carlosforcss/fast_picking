# -*- coding: utf-8 -*-
{
    'name': "fast_picking",

    'summary': """
        Fast picking allows users to send pickings by invoices. 
    """,

    'description': """
        Fast picking allows users to send pickings by invoices. 
    """,

    'author': "Sursoom",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base', 'stock', 'crm', 'sale_management', 'account',
    ],
    # always loaded
    'data': [
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
