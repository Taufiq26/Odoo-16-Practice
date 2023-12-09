{
    'name': "Master Materials",
    'summary': """
        Manage sellable materials
    """,
    'description': """
        Manage sellable materials data include the price and supplier
    """,
    'author': "Taufiq Ridwan Soleh",
    'website': "https://www.sandraharlim.com",
    'category': 'Inventory',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/materials.xml',
        'views/suppliers.xml'
    ],
     
    'application': True,
}