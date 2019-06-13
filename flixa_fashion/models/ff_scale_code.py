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
	
	@api.model
	def create(self, vals_list):
		"""
		- Add Warning in case sale scale and it's lines is empty
		- Add Warning in case color and it's lines is empty
		:param vals_list:
		:return: SUPER
		"""
		fashion = super(ProductAttributeInherit, self).create(vals_list)
		# if fashion.type == 'select' and not fashion.value_ids:
		# 	raise Warning("Size Scale lines is required!!!")
		# elif fashion.type == 'color' and not fashion.value_ids:
		# 	raise Warning("Color lines is required!!!")
		return fashion
	
	@api.multi
	def write(self, vals_list):
		"""
		- Add Warning in case sale scale and it's  lines is empty
		- Add Warning in case color and it's lines is empty
		:param vals_list:
		:return: SUPER
		"""
		super(ProductAttributeInherit, self).write(vals_list)
		# if self.type == 'select' and not self.value_ids:
		# 	raise Warning("Size Scale lines is required!!!")
		# elif self.type == 'color' and not self.value_ids:
		# 	raise Warning("Color lines is required!!!")
		return True
# New Sprint 12July2019
	is_scale = fields.Boolean(string="Is Scale", help="Flag to show only records of scale codes")


class ProductAttributeValueInherit(models.Model):
	_inherit = 'product.attribute.value'
	
	is_scale = fields.Boolean(related='attribute_id.is_scale')
	sequence_rel = fields.Integer(related='sequence')


    
    
