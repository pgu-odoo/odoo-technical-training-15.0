# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Odoo Academy',

    'version' : '0.1',

    'summary': 'An app for odoo training',

    'author': 'Odoo',

    'description': """An app for odoo training. """,

    'website': 'https://www.odoo.com',

    'depends': ['sale'],

    'demo': [
        'demo/academy_demo.xml',

    ],

    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/academy_menuitems.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',

    ],
    'license': 'LGPL-3'
}
