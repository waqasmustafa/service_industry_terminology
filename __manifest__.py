{
    'name': 'Service Industry Terminology',
    'version': '1.0',
    'summary': 'Rename core terms: Product→Service, Sale Order→Work Order, etc.',
    'description': """
Service Industry Terminology
============================

This module replaces some default Odoo terms across the whole UI:

- Product → Service
- Products → Services
- Sale Order → Work Order
- Sales Order → Work Orders
- Quotation → Estimate
- Quotations → Estimates
- Delivery Address → Service Address
""",
    'author': 'Waqas Mustafa',
    'category': 'Localization',
    'depends': [
        'sale',
        'product',
        'stock',
    ],
    'data': [
        # no XML needed – translations are loaded automatically from i18n
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
