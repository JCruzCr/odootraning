# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class SpatialPlane(models.Model):
    _name = 'spatial.mission.spatial.plane'
    _description = 'Spatial plane model'
    
    name = fields.Char(string='Name', help='Name of plane', required=True)
    seats = fields.Integer(string='Seats', help='Plane\'s seats', required=True)
    engines = fields.Integer(string='Engine', help='Number of engines in the plane', required=True)
    
    width = fields.Float(string='Width', help='Width plane', required=False, default=0.0)
    height = fields.Float(string='Height', help='Height plane', required=False, default=0.0)
    length = fields.Float(string='Length', help='Length plane', required=False, default=0.0)
    fuel_amount = fields.Integer(string='Amount fuel', help='Amount fuel required', compute='_set_fuel_amount', store=True)
    
    type = fields.Selection(string='Type', help='Plane Type', selection=[
        ('turboair', 'Turboprop Aircraft'),
        ('pistonair', 'Piston Aircraft'),
        ('narrowbody', 'Narrow Body Aircraft'),  
    ])
    active = fields.Boolean(string='Is Active?', help='Is active...')
    
    @api.depends('engines')
    def _set_fuel_amount(self):
        for r in self:
            r.fuel_amount = r.engines * 100
    
    @api.constrains('engines')
    def _check_engines(self):
        for rec in self:
            if rec.engines < 2:
                raise UserError('The engines must be more than 2')
                
                
    @api.constrains('length') 
    def _check_length(self):
        for rec in self:
            if rec.length <= rec.width:
                raise UserError('The length must be more than width')
    
    
class SpatialMission(models.Model):
    _name = 'mission'
    _description = 'Mission'
    
    name = fields.Char(string="Mission Name", help="Mission Name", size=500, required=True)
    description = fields.Char(string='Mission Description', help='Mission Description', size=500, required=True)
    
    
    plane_ids = fields.Many2many(comodel_name='spatial.mission.spatial.plane')
    partner_mission_ids = fields.Many2many(comodel_name='res.partner')
    leader_id = fields.Many2one(comodel_name='res.partner')
    leader_name = fields.Char(string="Leader Name", help="Leader Name", related='leader_id.name')
    
    project_id = fields.One2many(comodel_name='project.project', inverse_name='mission_ids', string='Project', help='Associated Project')
    