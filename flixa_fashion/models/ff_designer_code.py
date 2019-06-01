# -*- coding: utf-8 -*-

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api

# 3 :  imports from odoo addons


class ff_Designer_Code(models.Model):
    _name = 'ff.designer.code'
    _description = 'Designer Code'

    name = fields.Char('Designer' , required = True)

    
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100