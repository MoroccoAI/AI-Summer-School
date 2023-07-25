# -*- coding: utf-8 -*-
{
    'name': "beradar",

    'summary': """
        Well detection ML-based model  
        """,

    'description': 
        """
        Well detection ML-based model in Morocco
        
        """,

    'author': "beRadar Team",
    'website': "http://www.beradar.ma",
    'icon': 'static/description/icon.png',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'installable':'True',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/ml_radar_views.xml',
        'views/radar_dashbord_views.xml',
        'security/ir.model.access.csv',
        ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
