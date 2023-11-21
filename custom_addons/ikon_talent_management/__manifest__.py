{
    'name': 'IKON Talent Management',
    'summary': """IKON Talent Management""",
    'version': '16.0',
    "author": "Ikon Developer",
    'company': 'Ikonsultan Inovatama',
    'website': 'https://www.ikonsultan.com',
    'category': 'Tools',
    'images': [],
    'depends': ['base', "web", 'hr_recruitment', 'hr_skills'],
    "external_dependencies": {"python3.9": ["graphene"]},
    'license': 'AGPL-3',
    'data': [
        'views/talent_pool_import_data_views.xml',
        'views/talent_tree_view.xml',
        'views/talent_kanban_views.xml',
        'views/menu_talent.xml',
        'views/views.xml',
        'views/pds_talent.xml',
        'views/pds_view.xml',
        'static/src/js/pds.js',
        # 'views/view_report/report_talent.xml',
    ],
    'assets': {
        'ikon_recruitment.assets': [
            '/ikon_talent_management/static/src/js/pds.js'
        ]
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
