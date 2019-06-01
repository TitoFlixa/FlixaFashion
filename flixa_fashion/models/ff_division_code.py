# -*- coding: utf-8 -*-

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api

# 3 :  imports from odoo addons


class ffDivisionCode(models.Model):
    _name = 'ff.Division.Code'
    _description = 'Division Code'

    name = fields.Char('Division' , required = True)

    
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100