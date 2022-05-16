# -*- coding: utf-8 -*-
{
    'name': "custom/courses",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'contacts', 'web'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/index.xml',
        'views/students.xml',
        'views/list_courses.xml',
        'views/courses.xml',
        'views/teachers.xml',
        'views/view_course.xml',
        'views/menu.xml',
        'views/wizard_grade.xml',
        'views/report.xml',
        'views/index_sequence.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
