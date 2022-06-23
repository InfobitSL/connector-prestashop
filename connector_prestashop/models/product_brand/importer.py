# Copyright 2020 PlanetaTIC - Marc Poch <mpoch@planetatic.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class ProductBrandMapper(Component):
    _name = "prestashop.product.brand.import.mapper"
    _inherit = "prestashop.import.mapper"
    _apply_on = "prestashop.product.brand"

    _model_name = "prestashop.product.brand"

    direct = [
        ("name", "name"),
    ]


class ProductBrandImporter(Component):
    _name = "prestashop.product.brand.importer"
    _inherit = "prestashop.importer"
    _apply_on = "prestashop.product.brand"
    _model_name = "prestashop.product.brand"


class ProductBrandBatchImporter(Component):
    _name = "prestashop.product.brand.delayed.batch.importer"
    _inherit = "prestashop.delayed.batch.importer"
    _apply_on = "prestashop.product.brand"

    _model_name = "prestashop.product.brand"
