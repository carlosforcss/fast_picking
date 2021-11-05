# -*- coding: utf-8 -*-http://localhost:8069/web?debug=assets#
from odoo import models, fields


class AccountMove(models.Model):

    _inherit = "account.move"

    def action_post(self):
        response = super().action_post()
        if self.move_type == "out_invoice":
            sale_order_model = self.env["sale.order"]
            orders = sale_order_model.search([
                ('partner_id', '=', self.partner_id.id,),
                ('invoice_count', ">=", 1),
            ])
            selected_order = None
            for order in orders:
                for invoice in order.invoice_ids:
                    if invoice.id == self.id:
                        selected_order = order
            if selected_order:
                picking_validation_response = None
                for picking in selected_order.picking_ids:
                    if picking.state in ['assigned']:
                        picking_response = picking.button_validate()
                        if type(picking_response):
                            if picking_validation_response is None:
                                picking_validation_response = picking_response
                            else:
                                picking_validation_response["context"]["button_validate_picking_ids"].push(picking.id)
                return picking_validation_response or response
        return response
