# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_size_scale = fields.Boolean("Size scales", default=False,
                                       help="Configure multiple size scales for your products.")
    module_color_palette = fields.Boolean("Color Palette", default=False,
                                          help="Define a collection of color codes to assign as "
                                               "a group to your products.")
    module_season_codes = fields.Boolean("Season Codes", default=False,
                                         help="Associate your products with a specific season such as"
                                              " (Spring Collection, Summer Collection, etc.)")
    module_division_codes = fields.Boolean("Division Codes", default=False,
                                           help="Associate your products with a specific division code such as"
                                                " (Menswear, Women ware, Children, etc.)")
    module_classification_codes = fields.Boolean("Classification Codes", default=False,
                                                 help="Associate your products with a specific "
                                                      "Classification code such as "
                                                      "(Pants, T Shirts, Accessories, etc.)")
    module_designer_codes = fields.Boolean("Designer Codes", default=False,
                                           help="Associate your products with a specific designer.")
    module_collection_codes = fields.Boolean("Collection Codes", default=False,
                                             help="Associate your products with a specific collection code.")
    
    def get_values(self):
        ir_config = self.env['ir.config_parameter']
        flixa_fashion_res = super(ResConfigSettings, self).get_values()
        flixa_fashion_res.update(
            module_size_scale=True if ir_config.sudo().get_param('module_size_scale') == "True" else False,
            module_color_palette=True if ir_config.sudo().get_param('module_color_palette') == "True" else False,
            module_season_codes=True if ir_config.sudo().get_param('module_season_codes') == "True" else False,
            module_division_codes=True if ir_config.sudo().get_param('module_division_codes') == "True" else False,
            module_classification_codes=True if ir_config.sudo().get_param('module_classification_codes') == "True" else False,
            module_designer_codes=True if ir_config.sudo().get_param('module_designer_codes') == "True" else False,
            module_collection_codes=True if ir_config.sudo().get_param('module_collection_codes') == "True" else False,

        )
        return flixa_fashion_res

    def set_values(self):
        ir_config = self.env['ir.config_parameter']
        super(ResConfigSettings, self).set_values()
        ir_config.set_param('module_size_scale', self.module_size_scale)
        ir_config.set_param('module_color_palette', self.module_color_palette)
        ir_config.set_param('module_season_codes', self.module_season_codes)
        ir_config.set_param('module_division_codes', self.module_division_codes)
        ir_config.set_param('module_classification_codes', self.module_classification_codes)
        ir_config.set_param('module_designer_codes', self.module_designer_codes)
        ir_config.set_param('module_collection_codes', self.module_collection_codes)
        
