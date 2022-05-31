from odoo import api, fields, models


class ResCityZipStreet(models.Model):
    _inherit = "res.city.zip"

    street = fields.Char("street")

