# Copyright 2020 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models

from odoo.addons.component.core import Component


class ProductBrand(models.Model):
    _inherit = "product.brand"

    prestashop_bind_ids = fields.One2many(
        comodel_name="prestashop.product.brand",
        inverse_name="odoo_id",
        string="PrestaShop Bindings",
    )


class PrestashopProductBrand(models.Model):
    _name = "prestashop.product.brand"
    _inherit = "prestashop.binding.odoo"
    _inherits = {"product.brand": "odoo_id"}

    odoo_id = fields.Many2one(
        comodel_name="product.brand",
        required=True,
        ondelete="cascade",
        string="Product Brand",
        oldname="openerp_id",
    )
    date_add = fields.Datetime(string="Created At (on PrestaShop)", readonly=True)
    date_upd = fields.Datetime(string="Updated At (on PrestaShop)", readonly=True)


class ProductBrandAdapter(Component):
    _name = "prestashop.product.brand.adapter"
    _inherit = "prestashop.adapter"
    _apply_on = "prestashop.product.brand"

    _model_name = "prestashop.product.brand"
    _prestashop_model = "manufacturers"
    _export_node_name = "manufacturers"
    _export_node_name_res = "manufacturer"
