# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleSubscriptionLine(models.Model):
    _inherit = 'sale.subscription.line'
    _description = 'Subscription Line Extension'
    

    service_id  = fields.Char(string='SID',required=True)
    tag_ids = fields.Many2many('crm.tag','subscription_extended_crm_tag_rel',
                    'subscription_id','crm_id',string='Service Tags')
    archived_product_count = fields.Integer("Archived Product")

 
    def _compute_service_id(self):
        code = self.env['sale.subscription.line'].search(['id','=',str(self.id)]).code
        display_name = self.env['sale.subscription.line'].search(['id','=',str(self.id)]).display_name
        full_code =  code 
        self.service_id = full_code




