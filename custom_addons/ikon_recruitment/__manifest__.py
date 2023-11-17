{
    'name': 'IKON Recruitment Module',
    'summary': """IKON Rec Module""",
    'version': '16.0',
    "author": "Ikon Developer",
    'company': 'Ikonsultan Inovatama',
    'website': 'https://www.ikonsultan.com',
    'category': 'Tools',
    'images': [],
    'depends': ['base', 'website', 'website_hr_recruitment', 'portal'],
    "external_dependencies": {"python3.9": ["graphene"]},
    'license': 'AGPL-3',
    'data': [
        'views/inherit/jobs_portal.xml',
        'views/inherit/footer_login.xml',
        'views/inherit/custom_job_detail.xml',
        'views/custom_skill_form_view.xml',
        'views/custom_job_detail.xml',
        'views/my_profile_view.xml',
        'static/src/js/user_profile.js',

        'views/custom_hr_applicant_kanban.xml',
        'views/custom_job_position.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/ikon_recruitment/static/src/scss/my_profile.css',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
