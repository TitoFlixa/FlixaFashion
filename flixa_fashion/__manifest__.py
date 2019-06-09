# -*- coding: utf-8 -*-
{
    'name': "FlixaFashion",

    'summary': """
        FlixaFashion, the complete business solution for the Fashion industry.""",

    'description': """
        The only system you will need to run your Fashion related business. Whether you are in Apprell, Accessories,
        Footware, or anythung in between, FlixaFashion got you covered. Includes the following modules:
        
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
    'depends': ['base', 'analytic'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ff_menu.xml',
        'views/ff_division_code_views.xml',
        'views/ff_designer_code_views.xml',
        'views/ff_collection_code_views.xml',
        'views/ff_classification_code_views.xml',
        'views/ff_season_code_views.xml',
        'views/ff_scale_code_views.xml',        
        'views/res_config_settings.xml',
        
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}