# -*- coding: utf-8 -*-
{
    'name': "Sistema de Evaluación del ISTLA",

    'summary': """
        Sistema desarrollado por Josselyn""",

    'description': """
        Sistema desarrollado para la evaluación del ISTLA
    """,

    'author': "Josselyn",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sistema de Evaluación ISTLA',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/periodo_evaluacion_view.xml',
        'views/periodo_academico_view.xml',
        'views/criterio_view.xml',
        'views/subcriterio_view.xml',
        'views/carrera_view.xml',
        'views/practicas_view.xml',
        'views/evidencia_view.xml',
        'views/malla_view.xml',
        'views/ciclo_view.xml',
        'views/docente_view.xml',
        'views/main_menu_view.xml',

    ],
    # only loaded in demonstration mode
    'installable': True,
    'aplication': True,
    'autoinstall': False,
}
