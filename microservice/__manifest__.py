# -*- coding: utf-8 -*-
{
    'name': "Odoo microservices",

    'summary': """
        Odoo integration with microservices FastAPI
        """,

    'description': """
        Odoo integration with microservices FastAPI
    """,

    'author': "Artios",
    'website': "https://www.artios.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/core.xml',
        'views/microservice.xml',
        'views/task_group.xml',
        'views/task.xml',
        'views/request.xml',
        'data/data.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
    'license': 'Other proprietary',
}