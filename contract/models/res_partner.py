from odoo import models, fields, api


class rtw_sf_partner_oppo(models.Model):
    _inherit = "res.partner"
    _description = 'contract'

    contract = fields.One2many('contract.contract', inverse_name='accounts')
    contract_count = fields.Integer(string="case count", compute="_compute_contract_count")

    def _compute_contract_count(self):
        for rec in self:
            contract_count = self.env['contract.contract'].search_count([('accounts', '=', rec.id)])
            rec.contract_count = contract_count

    def action_open_contract(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'contract',
            'res_model': 'contract.contract',
            'domain': [('accounts', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_id': self.id,
                'default_accounts': self.id,
            }
        }
