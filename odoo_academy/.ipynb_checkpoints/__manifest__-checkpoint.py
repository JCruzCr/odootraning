# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage training""",
    
    'description': """
        Academy Module to Manage Training:
        - Courses
        - Sessions
        -Attendees
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version': '0.1',
    
    'depends': [
      'base', 'sale',
    ],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/sale_views_inherit.xml'

    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],
    
}