# -*- encoding: utf-8 -*-

{
    'name': 'Voluntarees App',
    'description': """
        This module is develop in Technical Training
    """,
    'summary': """
        Technical Training
    """,
    'version': '14.0.0.0.1',
    'license': 'LGPL-3',
    
    'depends':[
      'base', 'web_gantt', 'approvals',
    ],
    
    'data':[
        'security/security_volunteer.xml',
        'security/ir.model.access.csv',
        'views/volunteer_views.xml',
        'views/volunteer_menuitems.xml',
    ],
    'demo':[
        'demo/volunteer_demo.xml',
    ],
}