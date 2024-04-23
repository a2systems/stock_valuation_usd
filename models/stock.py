# Copyright 2020 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _, api


class StockValuationLayer(models.Model):
    _inherit = "stock.valuation.layer"

    def _compute_values_usd(self):
        for rec in self:
            res = rec.company_id.currency_id._convert(
                rec.value,
                self.env.ref('base.USD'),
                rec.company_id,
                rec.create_date,
            )
            rec.value_usd = res
            res = rec.company_id.currency_id._convert(
                rec.unit_cost,
                self.env.ref('base.USD'),
                rec.company_id,
                rec.create_date,
            )
            rec.unit_cost_usd = res


    value_usd = fields.Float('Valor USD',compute=_compute_values_usd)
    unit_cost_usd = fields.Float('Unit Cost USD',compute=_compute_values_usd)


