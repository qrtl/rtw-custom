# Copyright 2019-2020 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, models, fields
_STATES = [
    ("draft", "Draft"),
    ("to_approve", "To be approved"),
    ("approved", "Approved"),
    ("rejected", "Rejected"),
    ("done", "Done"),
]


class PurchaseRequest(models.Model):
    _name = "shinsei.sample"
    _inherit = _inherit = ["mail.thread", "mail.activity.mixin", "tier.validation"]
    _state_from = ["draft"]
    _state_to = ["approved"]

    _tier_validation_manual_config = True

    name = fields.Char("name")
    state = fields.Selection(
        selection=_STATES,
        string="Status",
        index=True,
        tracking=True,
        required=True,
        copy=False,
        default="draft",
    )

    @api.model
    def _get_under_validation_exceptions(self):
        res = super(PurchaseRequest, self)._get_under_validation_exceptions()
        res.append("route_id")
        return res
