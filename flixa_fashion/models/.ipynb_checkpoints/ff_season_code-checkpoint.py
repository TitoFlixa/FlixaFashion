# -*- coding: utf-8 -*-

# 1 : imports of python lib

# 2 :  imports of odoo
from odoo import models, fields, api

# 3 :  imports from odoo addons


class ff_Season_Code(models.Model):
    _name = 'ff.season.code'
    _description = 'Season Code'

    name = fields.Char('Season' , required = True)
    start_production_date = fields.Date("Start Production Date")
    end_production_date = fields.Date("End Production Date")
    start_sales_date = fields.Date("Start Sales Date")
    end_sales_date = fields.Date("End Sales Date")

    
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100