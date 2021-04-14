# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SpatialPlane(models.Model):
    _name = 'spatial.mission.spatial.plane'
    _description = 'Spatial plane model'
    
    name = fields.Char(string='Name', help='Name of plane', required=True)
    seats = fields.Integer(string='Seats', help='Plane\'s seats', required=True)
    engines = fields.Integer(string='Engine', help='Number of engines in the plane', required=True)
    
    width = fields.Float(string='Width', help='Width plane', required=False, default=0.0)
    height = fields.Float(string='Height', help='Height plane', required=False, default=0.0)
    length = fields.Float(string='Length', help='Length plane', required=False, default=0.0)
    
    type = fields.Selection(string='Type', help='Plane Type', selection=[
        ('turboair', 'Turboprop Aircraft'),
        ('pistonair', 'Piston Aircraft'),
        ('narrowbody', 'Narrow Body Aircraft'),  
    ])
    active = fields.Boolean(string='Is Active?', help='Is active...')
    
    