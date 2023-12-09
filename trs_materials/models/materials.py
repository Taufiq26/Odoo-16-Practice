from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Materials(models.Model):
    _name = 'master.materials'
    _description = 'Master data of materials'

    code = fields.Char(string='Material Code')
    name = fields.Char(string='Material Name')
    type = fields.Selection([
        ('fabric', 'Fabric'), 
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type')
    buy_price = fields.Integer(string='Material Buy Price')
    supplier_id = fields.Many2one('master.suppliers', string='Related Supplier')

    @api.constrains('buy_price')
    def _check_minimum_value(self):
        min_value = 100
        for record in self:
            if record.buy_price < min_value:
                raise ValidationError('The value must be greater than {}'.format(min_value))