# -*- coding: utf-8 -*-
#################################################################################
# Author      : Flixa Logic Inc. All Rights Reserved.
# App         : Flixa Fashion.
# Desc        : Flixa_Fashion Size Scale Classes and Methods.
# Comments    :
#################################################################################
from odoo import models, fields, api, _
from odoo.exceptions import Warning


# Inherit Product.Template Class
class ff_ProductTemplateInherit(models.Model):
	"""
    Product Template Inherited Class:
        - Get default Configuration of FlixaFashion Product Matrix Setup.
            -> use this default settings on show there related fields
        - Add fields of Size scale/ Color and use there selected value
            -> on create/write use those value and create product.attribute.line
                with type of attribute and all it's attributes value
            -> grantee that in case of change of it's value delete old records before add new one.
    """
	_inherit = 'product.template'
	
	# used to show size scale field
	is_size_scale = fields.Boolean(string="Size Scale?")
	edit_size_scale = fields.Boolean(string="Size Scale Editable?",default=True)
	size_scale_id = fields.Many2one(comodel_name='product.attribute', string="Size Scale"
	                                , domain=[('is_scale', '=', True)])
	# Related Filed of attributes values as sizes
	value_ids = fields.One2many(related='size_scale_id.value_ids')
	# The line that is marked as size scale
	line_id = fields.Many2one('product.template.attribute.line')
	
	@api.model
	def create(self, vals_list):
		"""
		- On create new attribute reflect it in product.template.attribute.line
		- Then complete default cycle.
		:param vals_list:
		:return: SUPER
		"""
		attribute_value_obj = self.env['product.attribute']
		attribute_line_ids = vals_list.get('attribute_line_ids') or []
		if vals_list.get('size_scale_id') and vals_list.get('is_size_scale'):
			size_scale_id = attribute_value_obj.browse(vals_list.get('size_scale_id'))
			if size_scale_id:
				attribute_line_ids.append((0, 0, {
					'attribute_id': size_scale_id.id,
					'is_size_scale_line': True,
					'active': True,
					'value_ids': [(6, 0, size_scale_id.value_ids.ids)],
				}))
				# MArk size_scale_field as non editable after creating
				vals_list['edit_size_scale'] = False
		if len(attribute_line_ids):
			vals_list['attribute_line_ids'] = attribute_line_ids
		product_id = super(ff_ProductTemplateInherit, self).create(vals_list)
		line_id = (l[0] for l in product_id.get_line())
		if line_id:
			product_id.line_id = line_id
		return product_id
	
	@api.multi
	def write(self, vals):
		variant_obj = self.env['product.product']
		for product_id in self:
			super(ff_ProductTemplateInherit, self).write(vals)
			if 'is_size_scale' in vals:
				# Size scale marked as False -> deactivate product variants that contain this values
				if not product_id.is_size_scale:
					if product_id.line_id:
						variant_ids = [v[0] for v in product_id.get_variants()]
						if variant_ids:
							variants = variant_obj.browse(variant_ids)
							variants.write({'active': False})
					else:
						raise Warning(_("Something went wrong on delete related record of size scale!!!"))
				# Size scale marked as True -> activate product variants that contain this values
				else:
					if product_id.line_id:
						variant_ids = [v[0] for v in product_id.get_variants()]
						if variant_ids:
							variants = variant_obj.browse(variant_ids)
							variants.write({'active': True})
							
	@api.model
	def get_line(self):
		"""
		get variant lines that is deactivated
		:return:
		"""
		query = """
			SELECT id
			FROM product_template_attribute_line
			WHERE product_tmpl_id = %s
				AND attribute_id = %s
				AND active = False AND is_size_scale_line = True
		""" % (self.id, self.size_scale_id.id)
		self.env.cr.execute(query)
		return self.env.cr.fetchall()
	
	@api.model
	def get_variants(self):
		"""
		get all related variants that is created for specific product and attributes
		:return:
		"""
		query = """
			 SELECT id FROM product_product WHERE product_tmpl_id = %s
			 AND id in (
				SELECT product_product_id
				FROM product_attribute_value_product_product_rel
				WHERE product_attribute_value_id in %s)""" %\
		        (self.id, tuple(self.size_scale_id.value_ids.ids))
		self.env.cr.execute(query)
		return self.env.cr.fetchall()
		

# Inherit product.template.attribute.line Class
class ff_product_template_attribute_line(models.Model):
	_inherit = 'product.template.attribute.line'
	# add filed to mark line in case of remove size scale from product delete this line using flag
	is_size_scale_line = fields.Boolean(string="size scale line")
	active = fields.Boolean('Active', default=True)
	
	@api.model
	def create(self, vals_list):
		"""
		- On create change value of active records regarding to it's type
		- [size scale is hide, other showen as default]
		:param vals_list:
		:return: SUPER action
		"""
		line = super(ff_product_template_attribute_line, self).create(vals_list)
		if line.is_size_scale_line:
			line.write({'active': False})
		else:
			line.write({'active': True})
		return line
	
	
class ff_ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    @api.multi
    def name_get(self):
        if not self._context.get('show_attribute', True):  # TDE FIXME: not used
            return super(ff_ProductAttributeValue, self).name_get()
        return [(value.id, " %s" % (value.name)) for value in self]

    