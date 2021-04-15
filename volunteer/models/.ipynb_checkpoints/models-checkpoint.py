# -*- encodig: utf-8 -*-

from odoo import models, fields, api

class Task(models.Model):
    _name = 'volunteer.task'
    _description = 'Volunteer Task'
    
    name = fields.Char(string='Task\'s name', help='Name of the new tasks', size=2000, required=True)
    description = fields.Char(string='Task', help='Description task', size=5000, required=False)
    type = fields.Selection(
        [
            ('aid', 'Help People'),
            ('guide', 'Guide People'),
            ('other', 'Other'),
        ], default='aid'
        
    )
    
    start_task = fields.Datetime()
    end_task = fields.Datetime()
    repated = fields.Integer(string='Repeated taks', default=0)