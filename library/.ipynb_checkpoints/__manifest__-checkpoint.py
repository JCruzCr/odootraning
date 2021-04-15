# -*- encodig: utf-8 -*-

{
    'name': 'Library',
    'description': """
    """,
    'summary': 'Local Library',
    'version': '14.0.0.1.0',
    'application': True,
    
    'depends': [
        'base',
    ],
    
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitems.xml',
        'views/book_view.xml',
    ],
    
    'demo': [
        'demo/library_demo.xml',
    ],
    
}