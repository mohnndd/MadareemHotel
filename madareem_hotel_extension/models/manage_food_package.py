# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import date


class ManageFoodProductTemp(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string="Name", required=True)
    list_price = fields.Float(string="Sales Price", required=True)
    is_food_package = fields.Boolean(string='Is Food Package')
