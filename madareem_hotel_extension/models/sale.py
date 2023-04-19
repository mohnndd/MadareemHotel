# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from datetime import date


class saleorderdetails(models.Model):
    _inherit = 'sale.order'

    check_in_date = fields.Datetime(string="Check-In Date")
    check_out_date = fields.Datetime(string="Check-Out Date")
    choose_hall_id = fields.Many2one('product.template', string="Choose Hall",
                                     domain="[('is_hall_manage', '=',True)]")
    choose_food_package_id = fields.Many2one('product.template', string="Choose Food Package",
                                             domain="[('is_food_package', '=', True)]")

    # this onchange use for create new manage hall and update manage hal
    @api.onchange('choose_hall_id')
    def onchange_choose_hall(self):
        if self.choose_hall_id:
            for order in self:
                choose_hall = order.choose_hall_id.product_variant_id
                rec = order.order_line
                if rec:
                    rec_to_update = rec.filtered(lambda l: l.is_line_manage_hall == True)
                    if rec_to_update:
                        rec_to_update.product_id = self.choose_hall_id.product_variant_id.id
                        rec_to_update.name = self.choose_hall_id.product_variant_id.name
                        rec_to_update.price_unit = self.choose_hall_id.product_variant_id.list_price
                    else:
                        order.write({
                            'order_line': [
                                (0, 0, {
                                    'product_id': self.choose_hall_id.product_variant_id.id,
                                    'name': self.choose_hall_id.product_variant_id.name,
                                    'order_id': self.id,
                                    'product_uom': order.choose_hall_id.product_variant_id.uom_id.id,
                                    'is_line_manage_hall': True,
                                    'display_type': False,
                                    'price_unit': order.choose_hall_id.product_variant_id.list_price,
                                })
                            ]
                        })
                else:
                    order.order_line = [(0, 0, {
                        'product_id': order.choose_hall_id.product_variant_id.id,
                        'name': order.choose_hall_id.product_variant_id.name,
                        'order_id': order.id,
                        'product_uom': order.choose_hall_id.product_variant_id.uom_id.id,
                        'is_line_manage_hall': True,
                        'price_unit': order.choose_hall_id.product_variant_id.list_price,
                        'display_type': False, })]

    # This Onchange use for create new food package and update food package
    @api.onchange('choose_food_package_id')
    def onchange_choose_food_package_id(self):
        if self.choose_food_package_id:
            for order in self:
                choose_food = order.choose_food_package_id.product_variant_id
                if order.order_line:
                    rec = order.order_line
                    rec_to_update = rec.filtered(lambda l: l.is_line_food_package == True)
                    if rec_to_update:
                        rec_to_update.product_id = self.choose_food_package_id.product_variant_id.id
                        rec_to_update.name = self.choose_food_package_id.product_variant_id.name
                        rec_to_update.price_unit = self.choose_food_package_id.product_variant_id.list_price
                    else:
                        order.write({
                            'order_line': [
                                (0, 0, {
                                    'product_id': order.choose_food_package_id.product_variant_id.id,
                                    'name': order.choose_food_package_id.product_variant_id.name,
                                    'order_id': order.id,
                                    'product_uom': order.choose_food_package_id.product_variant_id.uom_id.id,
                                    'is_line_food_package': True,
                                    'display_type': False,
                                    'price_unit': order.choose_food_package_id.product_variant_id.list_price,
                                })
                            ]
                        })
                else:
                    order.order_line = [(0, 0, {
                        'product_id': order.choose_food_package_id.product_variant_id.id,
                        'name': order.choose_food_package_id.product_variant_id.name,
                        'order_id': order.id,
                        'product_uom': order.choose_food_package_id.product_variant_id.uom_id.id,
                        'is_line_food_package': True,
                        'price_unit': order.choose_food_package_id.product_variant_id.list_price,
                        'display_type': False, })]

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_line_manage_hall = fields.Boolean(string="Is Manage Hall")
    is_line_food_package = fields.Boolean(string="Is Food Package")

    @api.onchange('product_id')
    def _onchange_vehicle(self):
        if self.product_id.is_food_package == True:
            self.is_line_food_package = True
        else:
            self.is_line_food_package = False

        if self.product_id.is_hall_manage == True:
            self.is_line_manage_hall = True
        else:
            self.is_line_manage_hall = False


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    barcode = fields.Char(string='Barcode')

