# -*- encoding: utf-8 -*-

from odoo import models, api, fields
from odoo.exceptions import UserError, ValidationError

class Book(models.Model):
    _name = 'library.book'
    _description = 'This model is for library App'
    
    name = fields.Char(string='Name', help='Name of the book', size=1000, required=True)
    author = fields.Char(string='Author', help='Author Name', size=1000, required=True)
    pages = fields.Integer(string='Pages', help='Book\'s pages', required=False, default=1)
    ed = fields.Char(string='Edition', help='Book edition', size=500, required=False)
    isbn = fields.Char(string='ISBN', help='ISBN', size=100, required=False)
    
    
    @api.onchange('isbn', 'pages')
    def _onchange_isbn(self):
        if self.pages < 1:
            raise UserError('Pages\'s book must be more than 0')
        #if not self.isbn:
        #    if (len(self.isbn)-self.isbn.count('-')) != 13:
        #        raise ValidationError('ISBN must be 13')
                
    
    
class RentalBook(models.Model):
    _name = 'library.rental'
    _description = 'This is the rental model'
    
    
    #book_id = fields.Many2one(comodel_name='library.book', string='Book', help='Book related', ondelete='cascade', required=True)
    #name = fields.Char(string='Book', help='Related Book', related='book_id.author' )
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer', help='Customer related', ondelete='cascade', required=True)
    book_copy_ids = fields.Many2many(comodel_name='library.book.copy', string='Assign Book', help='Asign Book to Customer')
    
class BookCopy(models.Model):
    _name = 'library.book.copy'
    _inherits = {'library.book': 'book_ids'}
    
    book_ids = fields.Many2one(comodel_name='library.book', ondelete='cascade')
    
    book_reference = fields.Char(string='Book Reference', help='Book Referenda Data', size=100, required=True)
    available = fields.Boolean(string='Is Available?', help='Is Available Book?', default=True)
    
    
    _sql_constraints = [
        ('book_reference_unique', 'unique(book_reference)', 'Book Reference Must Be Unique')
    ]