from lxml import etree

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    street = fields.Char(compute="_compute_street", readonly=False, store=True)

    @api.depends("zip_id")
    def _compute_street(self):
        if hasattr(super(), "_compute_city_id"):
            super()._compute_city_id()  # pragma: no cover
        for record in self:
            if record.zip_id:
                record.street = record.zip_id.street
            elif not record.country_enforce_cities:
                record.street = False