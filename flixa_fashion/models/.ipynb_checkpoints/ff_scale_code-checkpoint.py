# -*- coding: utf-8 -*-
#################################################################################
# Author      : Flixa Logic Inc. All Rights Reserved.
# App         : Flixa Fashion.
# Desc        : Flixa_Fashion Size Scale Classes and Methods.
# Comments    : 
#################################################################################

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api

# 3 :  imports from odoo addons


# Inhirets the product.attribute class.
class ff_Scale_Code(models.Model): 
	
    _inherit = 'product.attribute'
    desc = fields.Char('Description', required=False)
    is_scale = fields.Boolean(string="Is Scale", help="Flag to show only records of scale codes")
    
    @api.model
    def create(self, vals_list):
        scales = super(ff_Scale_Code, self).create(vals_list)
        return scales
    
    @api.multi
    def write(self, vals_list):
        super(ff_Scale_Code, self).write(vals_list)
        return True
    
    
# Inhirets the product.attribute.value class.    
class ff_Size_Code(models.Model):
    _inherit = 'product.attribute.value'
    is_size = fields.Boolean(related='attribute_id.is_scale')
    sequence_rel = fields.Integer(related='sequence')