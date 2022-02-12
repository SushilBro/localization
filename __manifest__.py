# -*- coding: utf-8 -*-
{
    'name' : 'Nepal Localization',
    'version' : '1.0',
    'summary': 'Create Localization',
    'sequence': 10,
    'description': """Localization For Country Nepal""",
    'category': 'Sales/Sales',
    'website': 'https://www.hotellila.com',
    'depends' : ['base','contacts','web'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/district.xml',
        'data/municipality.xml',
        'data/rural_municipalities.xml',
        'views/inherit.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
