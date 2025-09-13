from odoo import models

class SimpleMenu(models.Model):
    _name = 'simple.menu'
    _description = 'Modelo vacío solo para menú'
    
    name = fields.Char(string="Nombre")
