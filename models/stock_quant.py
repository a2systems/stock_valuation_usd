# Copyright 2020 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, _, api


class StockQuant(models.Model):
    _inherit = "stock.quant"

    def _compute_values_usd(self):
        for rec in self:
            if rec.company_id and rec.value:
                res = rec.company_id.currency_id._convert(
                    rec.product_id.value_svl,
                    self.env.ref('base.USD'),
                    rec.company_id,
                    rec.in_date,
                    )
            else:
                res = 0
            rec.value_usd = res


    value_usd = fields.Float('Valor USD',compute=_compute_values_usd)

