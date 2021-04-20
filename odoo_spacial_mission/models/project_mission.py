# -*- encoding="utf-8" -*-

from odoo import models, api, fields


class ProjectMission(models.Model):
    _inherit = 'project.project'
    
    mission_id = fields.Many2one(comodel_name='mission', string='Mission Related', help='Mission Realted Field', ondelete='set null')
    mission_ids = fields.Many2one(comodel_name='mission', ondelete='set null', string='Missions', help='Mission IDs')