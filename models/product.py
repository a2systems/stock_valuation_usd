# Copyright 2020 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _, api
from datetime import date

class ProductProduct(models.Model):
    _inherit = "product.product"

    def _compute_total_value_usd(self):
        for rec in self:
            valuation_layers = self.env['stock.valuation.layer'].search([('product_id','=',rec.id)])
            value_usd = sum(valuation_layers.mapped('value_usd'))
            rec.total_value_usd = value_usd

    def _compute_total_margin_usd(self):
        for rec in self:
            res = 0
            res = self.env.user.company_id.currency_id._convert(
                rec.total_margin,
                self.env.ref('base.USD'),
                self.env.user.company_id,
                date.today(),
                )
            rec.total_margin_usd = res

    total_value_usd = fields.Float('Valor Total USD',compute=_compute_total_value_usd)
    total_margin_usd = fields.Float('Margen USD',compute=_compute_total_margin_usd)
