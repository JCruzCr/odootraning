# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SpatialPlane(models.Model):
    _name = 'spatial.mission.spatial.plane'
    _description = 'Spatial plane model'
    
    name = fields.Char(string='Name', help='Name of plane', required=True)
    seats = fields.Integer(string='Seats', help='Plane\'s seats', required=True)
    engines = fields.Integer(string='Engine', help='Number of engines in the plane', required=True)
    
    