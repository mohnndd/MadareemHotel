# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import date


class ManagehallProductTemp(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string="Name", required=True)
    list_price = fields.Float(string="Sales Price", required=True)
    is_hall_manage = fields.Boolean(string="Is Manage Hall")
