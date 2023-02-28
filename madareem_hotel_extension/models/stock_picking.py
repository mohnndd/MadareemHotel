# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import date


class StockPiking(models.Model):
    _inherit = 'stock.picking'

    total_cost = fields.Float(string="Total Cost", compute="_compute_product_total_cost")

    # This method use for Product Total Cost.
    @api.depends('move_ids_without_package.product_uom_qty')
    def _compute_product_total_cost(self):
        for record in self:
            total = 0.0
            for line in record.move_ids_without_package:
                total += line.product_id.standard_price * line.product_uom_qty
            record.total_cost = total
