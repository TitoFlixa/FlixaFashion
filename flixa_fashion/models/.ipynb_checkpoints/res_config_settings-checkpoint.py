#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning

class
ResConfigSettings (models.TransientModel):
     _inherit = 'res.config.settings'
  module_use_season_codes = fields.Boolean ("Use Season Codes", default = False,
					 help =
					 "Associate your products with a specific season such as"
					 " (Spring Collection, Summer Collection, etc.)")
  module_mandatory_season_code =
  fields.Boolean ("Mandatory on Product Form", default = False, help =
	       "Force the user to select a season code when"
	       "adding a new product") module__use_division_codes =
  fields.Boolean ("Use Division Codes", default = False, help =
	       "Associate your products with a specific division code such as"
	       " (Menswear, Women ware, Children, etc.)")
  module_mandatory_division_code =
  fields.Boolean ("Mandatory on Product Form", default = False, help =
	       "Force the user to select a division code when"
	       "adding a new product") module_use_classification_codes =
  fields.Boolean ("Use Classification Codes", default = False, help =
	       "Associate your products with a specific "
	       "Classification code such as "
	       "(Pants, T Shirts, Accessories, etc.)")
  module_mandatory_classification_code =
  fields.Boolean ("Mandatory on Product Form", default = False, help =
	       "Force the user to select a classification code when"
	       "adding a new product") module_use_designer_codes =
  fields.Boolean ("Use Designer Codes", default = False, help =
	       "Associate your products with a specific designer.")
  module_mandatory_designer_code =
  fields.Boolean ("Mandatory on Product Form", default = False, help =
	       "Force the user to select a designer code when"
	       "adding a new product") module_use_collection_codes =
  fields.Boolean ("Use Collection Codes", default = False, help =
	       "Associate your products with a specific collection code.")
  module_mandatory_collection_code =
  fields.Boolean ("Mandatory on Product Form", default = False, help =
	       "Force the user to select a collection code when"
	       "adding a new product") def
     get_values (self):
  ir_config = self.env['ir.config_parameter']
  flixa_fashion_res =
super (ResConfigSettings,
       self).get_values ()flixa_fashion_res.update (module_use_season_codes =
						    True if ir_config.sudo ().
						    get_param
						    ('module_use_season_codes')
						    == "True"
						    else
						    False,
						    module_use_division_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_use_division_codes')
						    == "True"
						    else
						    False,
						    module_use_classification_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_use_classification_codes')
						    == "True"
						    else
						    False,
						    module_use_designer_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_use_designer_codes')
						    == "True"
						    else
						    False,
						    module_use_collection_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_use_collection_codes')
						    == "True"
						    else
						    False,
						    module_mandatory_season_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_mandatory_season_codes')
						    == "True"
						    else
						    False,
						    module_mandatory_division_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_mandatory_division_codes')
						    == "True"
						    else
						    False,
						    module_mandatory_classification_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_mandatory_classification_codes')
						    == "True"
						    else
						    False,
						    module_mandatory_designer_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_mandatory_designer_codes')
						    == "True"
						    else
						    False,
						    module_mandatory_collection_codes
						    =
						    True if ir_config.sudo ().
						    get_param
						    ('module_mandatory_collection_codes')
						    == "True"
						    else
						    False,)
return flixa_fashion_res def set_values (self):
  ir_config = self.env['ir.config_parameter']
    super (ResConfigSettings,
	   self).set_values ()ir_config.set_param ('module_use_season_codes',
						   self.
						   module_use_season_codes)
    ir_config.set_param ('module_use_division_codes',
			 self.module_use_division_codes) ir_config.
    set_param ('module_use_classification_codes',
	       self.module_use_classification_codes) ir_config.
    set_param ('module_use_designer_codes',
	       self.module_use_designer_codes) ir_config.
    set_param ('module_use_collection_codes',
	       self.module_use_collection_codes)
