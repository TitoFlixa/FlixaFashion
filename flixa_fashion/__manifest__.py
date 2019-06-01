# -*- coding: utf-8 -*-
{
    'name': "FlixaFashion",

    'summary': """
        FlixaFashion, the complete business solution for the Fashion industry.""",

    'description': """
        The only system you will need to run your Fashion related business. Whether you are in Apprell, Accessories,
        Footware, FlixaFashion got you covered. Includes the following:
        
        - E-Commerce
        - Sales and Marketting business flow.
        - Inventory Management.
        - Purchasing and MFG.
        
        Please check the detailed features list at www.FlixaLogix.Com
    """,

    'author': "FlixaLogix Inc.",
    'website': "http://www.FlixaLogix.com",
    'category': 'Fashion ERP',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ff_division_code_views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}