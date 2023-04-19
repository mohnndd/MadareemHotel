# -*- encoding: utf-8 -*-
{
    'name': 'Hall Booking Management',
    'author': 'Intuz',
    'version': '1.12',
    'category': 'Sales',
    'summary': 'Hall Booking Management',
    'website': 'https://www.intuz.net',
    'depends': [
        'base', 'product', 'sale_management', 'stock', 'maintenance', 'sales_team', 'analytic'
    ],
    'data': [
        'views/sale.xml',
        'views/manage_food_package_view.xml',
        'views/manage_hall_view.xml',
        'views/stock_picking_view.xml',
        'security/madareem_security.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {},
    'installable': True,
    'application': True,
    'auto_install': False,

}
