# -*- coding: utf-8 -*-
#################################################################################
# Author      : Flixa Logic Inc. All Rights Reserved.
# App         : Flixa Fashion.
# Desc        : Flixa_Fashion Size Scale Classes and Methods.
# Comments    :
#################################################################################
from odoo import models, fields, api


# Inherits the product.attribute class.
class ff_Scale_Code(models.Model):
    _inherit = 'product.attribute'
    description = fields.Text(string="Description")
    is_scale = fields.Boolean(string="Is Scale", help="Flag to show only records of scale codes")
    scale_code_image = fields.Binary('Scale Code Image')



# Inherits the product.attribute.value class.
class ff_Size_Code(models.Model):
    _inherit = 'product.attribute.value'
    
    is_scale = fields.Boolean(related='attribute_id.is_scale')


    