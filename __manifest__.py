# -*- coding: utf-8 -*-
{
    'name': "Transportes",

    'summary': """
        Permite gestionar los transportes en la empresa""",

    'description': """
        Permite gestionar los paquetes, conductores y camiones de una empresa de transportes.
    """,

    'author': "Beatriz Calle Henríquez",
    'website': "http://www.beatrizcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/views.xml',
        'views/paquetes.xml',
        'views/conductores.xml',
        'views/camiones.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}