from odoo import models, fields, api


class rtw_sf_partner_oppo(models.Model):
    _inherit = "res.partner"
    _description = 'opportunity'

    opportunity = fields.One2many('opportunity.opportunity', inverse_name='accounts')  # ケース OK
    opportunity_count = fields.Integer(string="case count", compute="_compute_oppo_count")

    def _compute_oppo_count(self):
        for rec in self:
            opportunity_count = self.env['opportunity.opportunity'].search_count([('accounts', '=', rec.id)])
            rec.opportunity_count = opportunity_count

    def action_open_opportunity(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'opportunity',
            'res_model': 'opportunity.opportunity',
            'domain': [('accounts', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_id': self.id,
                'default_accounts': self.id,
            }
        }
