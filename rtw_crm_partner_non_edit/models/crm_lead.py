# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rtw_crm_partner_non_edit(models.Model):
    _inherit = 'crm.lead'

    partner_name_d = fields.Char(
        'Company Name', tracking=20, index=True,
        compute='_compute_partner_name_d', readonly=True, store=True,
        help='The name of the future partner company that will be created while converting the lead into opportunity')
    street_d = fields.Char('Street', related='partner_id.street', store=True, readonly=True)
    street2_d = fields.Char('Street2', related='partner_id.street2', store=True, readonly=True)
    city_d = fields.Char('City', related='partner_id.city', store=True, readonly=True)
    country_id_d = fields.Many2one(
        'res.country', string='Country',
        compute='_compute_partner_country_id_values', readonly=True, store=True)
    state_id_d = fields.Many2one(
        "res.country.state", string='State',
        compute='_compute_partner_state_id_values', readonly=True, store=True,
        domain="[('country_id', '=?', country_id_d)]")
    zip_d = fields.Char('Zip', related='partner_id.zip', store=True, readonly=True)
    website_d = fields.Char('Website', related='partner_id.website', store=True, readonly=True)
    contact_name_d = fields.Char(
        'Contact Name', tracking=30,
        compute='_compute_contact_name_d', readonly=True)
    title_d = fields.Many2one('res.partner.title', string='Title', compute='_compute_title_d', readonly=True)
    function_d = fields.Char('Job Position', related='partner_id.function', readonly=True)
    mobile_d = fields.Char('Mobile', related='partner_id.mobile', store=True, readonly=True)

    @api.depends('partner_id')
    def _compute_partner_name_d(self):
        """ compute the new values when partner_id has changed """
        for lead in self:
            lead.update(lead._prepare_partner_name_from_partner_d(lead.partner_id))

    @api.depends('partner_id')
    def _compute_partner_country_id_values(self):
        """ Sync all or none of address fields """
        for lead in self:
            lead.update(lead._prepare_country_id_values_from_partner(lead.partner_id))

    @api.depends('partner_id')
    def _compute_partner_state_id_values(self):
        """ Sync all or none of address fields """
        for lead in self:
            lead.update(lead._prepare_state_id_values_from_partner(lead.partner_id))

    @api.depends('partner_id')
    def _compute_contact_name_d(self):
        """ compute the new values when partner_id has changed """
        for lead in self:
            lead.update(lead._prepare_contact_name_from_partner_d(lead.partner_id))

    @api.depends('partner_id')
    def _compute_title_d(self):
        """ compute the new values when partner_id has changed """
        for lead in self:
            if not lead.title_d or lead.partner_id.title:
                lead.title_d = lead.partner_id.title

    def _prepare_partner_name_from_partner_d(self, partner):
        partner_name_d = partner.parent_id.name
        if not partner_name_d and partner.is_company:
            partner_name_d = partner.name
        return {'partner_name_d': partner_name_d}
        # return {'partner_name_d': partner_name_d or self.partner_name}

    def _prepare_country_id_values_from_partner(self, partner):
        if any(partner['country_id']):
            values = {'country_id_d': partner['country_id']}
        else:
            values = {'country_id_d': False}
            # values = {'country_id_d': self['country_id']}
        return values

    def _prepare_state_id_values_from_partner(self, partner):
        if any(partner['state_id']):
            values = {'state_id_d': partner['state_id']}
        else:
            values = {'state_id_d': False}
            # values = {'state_id_d': self['state_id']}
        return values

    def _prepare_contact_name_from_partner_d(self, partner):
        contact_name_d = False if partner.is_company else partner.name
        return {'contact_name_d': contact_name_d}
        # return {'contact_name_d': contact_name_d or self.contact_name}

