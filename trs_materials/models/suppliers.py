from odoo import api, fields, models

class Suppliers(models.Model):
    _name = 'master.suppliers'
    _description = 'Master data of supplier'

    code = fields.Char(string='Supplier Code')
    name = fields.Char(string='Supplier Name')
    address = fields.Char(string='Supplier Address')