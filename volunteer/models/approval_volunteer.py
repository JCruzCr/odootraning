# -*- encoding: utf-8 -*-

from odoo import fields, api, models

class ApprovalVolunteer(models.Model):
    _inherit = 'approval.request'
    
    task_id = fields.One2many(comodel_name='volunteer.task', inverse_name='approval_ids', string='Task', help='Task related to approval')
    