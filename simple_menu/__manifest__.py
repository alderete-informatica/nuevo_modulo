{
    'name': 'Simple Menu',
    'version': '1.0',
    'summary': 'Un módulo simple con menú y ventanas emergentes',
    'description': 'Muestra un menú con opción "Nuevo" y "Acerca de".',
    'author': 'Alderete Lucas Alberto',
    'website': 'https://aldereteinformatica.com',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'views/simple_menu_views.xml',
        'views/simple_menu_menus.xml',
    ],
    'installable': True,
    'application': True,
}