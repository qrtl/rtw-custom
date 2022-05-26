from odoo import models, fields, api


class rtw_sf_partner_oppo(models.Model):
    _inherit = "res.partner"
    _description = 'inquiry'

    inquiry = fields.One2many('rtw_sf.inquiry', inverse_name='contact_person')
    inquiry_count = fields.Integer(string="inquiry count", compute="_compute_inquiry_count")

    def _compute_inquiry_count(self):
        for rec in self:
            inquiry_count = self.env['rtw_sf.inquiry'].search_count([('contact_person', '=', rec.id)])
            rec.inquiry_count = inquiry_count

    def action_open_inquiry(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'c',
            'res_model': 'rtw_sf.inquiry',
            'domain': [('contact_person', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_id': self.id,
                'default_contact_person': self.id,
            }
        }

    def create_inquiry(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'rtw_sf.inquiry',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_id': self.id,
                'default_contact_person': self.id,
                'default_created_by_id': self.env.user.id,
                'default_last_modified_by_id': self.env.user.id,
                'default_owner_id': self.env.user.id,
            }
        }



