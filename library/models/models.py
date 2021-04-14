# -*- encoding: utf-8 -*-

from odoo import models, api, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'This model is for library App'
    
    name = fields.Char(string='Name', help='Name of the book', size=1000, required=True)
    author = fields.Char(string='Author', help='Author Name', size=1000, required=True)
    pages = fields.Integer(string='Pages', help='Book\'s pages', required=False)
    ed = fields.Char(string='Edition', help='Book edition', size=500, required=False)
    