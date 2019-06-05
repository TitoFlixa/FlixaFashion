# -*- coding: utf-8 -*-

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api
from odoo.exceptions import Warning

# 3 :  imports from odoo addons

class ResConfigSettings (models.TransientModel):
    
    _inherit = 'res.config.settings'
    module_use_season_codes = fields.Boolean ("Use Season Codes", default = False help = "Associate your products with a specific season such as (Spring Collection, Summer Collection, etc.)")
    module_mandatory_season_code = fields.Boolean ("Mandatory on Product Form", default = False, help = "Force the user to select a season code when adding a new product")
    module__use_division_codes = fields.Boolean ("Use Division Codes", default = False, help = "Associate your products with a specific division code such as (Menswear, Women ware, Children, etc.)")
    module_mandatory_division_code = fields.Boolean ("Mandatory on Product Form", default = False, help = "Force the user to select a division code when adding a new product")
    module_use_classification_codes = fields.Boolean ("Use Classification Codes", default = False, help = "Associate your products with a specific Classification code such as (Pants, T Shirts, Accessories, etc.)")
    module_mandatory_classification_code = fields.Boolean ("Mandatory on Product Form", default = False, help = "Force the user to select a classification code when adding a new product")
    module_use_designer_codes = fields.Boolean ("Use Designer Codes", default = False, help = "Associate your products with a specific designer.")
    module_mandatory_designer_code = fields.Boolean ("Mandatory on Product Form", default = False, help = "Force the user to select a designer code when adding a new product")
    module_use_collection_codes = fields.Boolean ("Use Collection Codes", default = False, help = "Associate your products with a specific collection code.")
    module_mandatory_collection_code = fields.Boolean ("Mandatory on Product Form", default = False, help = "Force the user to select a collection code when adding a new product")