# -*- coding: utf-8 -*-
#################################################################################
# Author      : Flixa Logic Inc. All Rights Reserved.
# App         : Flixa Fashion.
# Desc        : Flixa_Fashion Configuration View res.config.settings 
# Comments    :
#################################################################################

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api
from odoo.exceptions import Warning

# 3 :  imports from odoo addons

class ResConfigSettings (models.TransientModel):
    
    _inherit = 'res.config.settings'
