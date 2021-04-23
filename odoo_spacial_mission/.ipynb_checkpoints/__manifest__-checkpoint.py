# -*- coding: utf-8 -*-

{
    'name': 'Odoo Spacial Mission',
    'version': '14.0.1.0',
    'summary': """
        Odoo Inc. Odoo Spacial Mission
    """,
    'description': """
        This module will help to Odoo Inc.
    """,
    'author': 'IINGEN',
    'application': True,
    'depends': [
        'base', 'project',
    ],
    'data': [
        'security/spatial_mission_security.xml',
        'security/ir.model.access.csv',
        'views/spatial_mission_views.xml',
        'views/spatial_mission_menuitems.xml',
        'views/project_mission.xml',
        'report/spatial_plane.xml',
        
    ],
    'demo': [
        'demo/spatial_mission_demo.xml',
    ],
    
    
    
    
}