# -*- encoding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_session_product = fields.Boolean(string='Use as Session Product', help='Checl this box to this a Product for Session Fee',default=False)
    