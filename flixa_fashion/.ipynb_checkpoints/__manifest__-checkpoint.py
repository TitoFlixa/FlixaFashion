# -*- coding: utf-8 -*-
#################################################################################
# Author      : Flixa Logic Inc. All Rights Reserved.
# App         : Flixa Fashion.
# Desc        : Flixa_Fashion Manifest.
# Comments    : Base Eddition - Includes Sales, Inoicing, Inventory, Analytics
#################################################################################


{
    'name': "FlixaFashion",

    'summary': """
        FlixaFashion, the complete business solution for the Fashion industry.""",

    'description': """
        The only system you will need to run your Fashion related business. Whether you are in Apprell, Accessories,
        Footwear, or anything in between, FlixaFashion got you covered.  The base package includes the following modules:
        
        - Quote and complete Sales Management.
        - Invoices and Customer Payment processes.
        - Inventory Management with multi warehouse management.
        - Analytics and Dashboards.
        
        Please check the detailed features list at www.FlixaLogix.Com
    """,

    'author': "FlixaLogix Inc.",
    'website': "http://www.FlixaLogix.com",
    'category': 'Fashion ERP',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base', 'analytic', 'sale_stock', 'sale_management'],
    'depends': ['base', 'stock', 'website_sale','account', 'product'],

    
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/ff_menu.xml',
        'views/ff_scale_code_views.xml',        
        'views/res_config_settings.xml',
        
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}