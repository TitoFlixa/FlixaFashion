# -*- coding: utf-8 -*-

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api
from odoo.exceptions import Warning

# 3 :  imports from odoo addons

class ResConfigSettings (models.TransientModel):
    
    _inherit = 'res.config.settings'
