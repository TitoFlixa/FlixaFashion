# -*- coding: utf-8 -*-

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api

# 3 :  imports from odoo addons


class ff_Collection_Code(models.Model):
    _name = 'ff.collection.code'
    _description = 'Collection Code'

    name = fields.Char('Collection' , required = True)

    
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100