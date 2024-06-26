{
    'name': 'Maqsam Dial Integration',
    'author': 'zaan ',
    'website':'www.zaan.com.sa',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Integrate Maqsam dialing with Odoo Contacts',
    'depends': ['base', 'contacts'],
    'license': 'LGPL-3',
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/logo.png'],
}
