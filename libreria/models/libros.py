from odoo import models, fields

#creando un modelo a partir de una clase
class Libros(models.Model):
    _name = 'libros'

    name = fields.Char(string="Nombre del libro")
    Description = fields.Char(string="Descripcion")
    Autor = fields.Char(string="Autor")
    Price = fields.Float(string="Precio de venta")
    
    
