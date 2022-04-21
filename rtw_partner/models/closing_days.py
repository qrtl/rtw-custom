from odoo import fields, models

class ClosingDays(models.Model):

    _name = 'closing_days'
    _description = 'Closing Days'

    name = fields.Char()
