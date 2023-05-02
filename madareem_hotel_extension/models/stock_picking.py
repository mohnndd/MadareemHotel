# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import date


class StockPiking(models.Model):
    _inherit = 'stock.picking'

    total_cost = fields.Float(string="Total Cost", compute="_compute_product_total_cost")

    # This method use for Product Total Cost.
    @api.depends('move_lines')
    def _compute_product_total_cost(self):
        for record in self:
            total = 0.0
            scraps = self.env['stock.scrap'].search([('picking_id', '=', record.id)])
            domain = [('id', 'in', (record.move_lines + scraps.move_id).stock_valuation_layer_ids.ids)]
            valuations = self.env['stock.valuation.layer'].sudo().search(domain)
            if valuations:
                for valuation_line in valuations:
                    total += valuation_line.value
            record.total_cost = total
