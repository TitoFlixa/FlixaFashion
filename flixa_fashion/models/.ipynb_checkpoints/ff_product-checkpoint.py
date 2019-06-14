# -*- coding: utf-8 -*-
#################################################################################
# Author      : Flixa Logic Inc. All Rights Reserved.
# App         : Flixa Fashion.
# Desc        : Flixa_Fashion Product Classes and Methods.
# Comments    : 
#################################################################################

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api



# Inherits product.template Class
class ff_ProductTemplateInherit(models.Model):

	
    _inherit = 'product.template'
	
	# used to show size scale field
    is_size_scale = fields.Boolean(string="Size Scale?")
    size_scale_id = fields.Many2one(comodel_name='product.attribute', string="Size Scale"
                                    , domain=[('is_scale', '=', True)])

    
    # Related Filed of attributes values as sizes
	value_ids = fields.One2many(related='size_scale_id.value_ids')

    
	@api.onchange('size_scale_id')
	@api.multi
	def generate_attribute_lines(self):
		"""
		On Select Size Scale load it on attribute line with all it's scale code sizes
		"""
		for product_id in self:
			vals = []
			for line in product_id.attribute_line_ids.filtered(lambda x: not x.is_size_scale_line):
				vals.append({
					'attribute_id': line.attribute_id.id,
					'value_ids': [(6, 0, line.value_ids.ids)],
					})
			
			if product_id.size_scale_id:
				vals.append({
					'is_size_scale_line': True,
					'attribute_id': product_id.size_scale_id.id,
					'value_ids': [(6, 0, product_id.size_scale_id.value_ids.ids)],
					})
				product_id.update({'attribute_line_ids': vals})

                
                
                
	@api.multi
	def write(self, vals_list):
		"""
		- On write  attribute delete old attribute line if exist.
		- Reflect it in product.template.attribute.line create new record.
		- Then complete default cycle.
		:param vals_list:
		:return: SUPER
		"""
		for product_id in self:
			old_size_scale_id = product_id.size_scale_id
			print ("old_size_scale_id: ",old_size_scale_id)
			attribute_line_obj = self.env['product.template.attribute.line']
			print(vals_list.get('size_scale_id'))
			if 'size_scale_id' in vals_list and not vals_list.get('size_scale_id'):
				if old_size_scale_id:
					old_rec = attribute_line_obj.search([('attribute_id', '=', old_size_scale_id.id)
						                                    , ('product_tmpl_id', '=', product_id.id)])
					print("rec: ",old_rec)
					if old_rec:
						old_rec.unlink()
			super(ff_ProductTemplateInherit, product_id).write(vals_list)
	
		return True


# Inherit product.template.attribute.line Class
class ff_product_template_attribute_line(models.Model):
	_inherit = 'product.template.attribute.line'

    # add filed to mark line in case of remove size scale from product delete this line using flag
	is_size_scale_line = fields.Boolean(string="size scale line")