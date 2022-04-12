from odoo import api, fields, models


class Teachers(models.Model):
    _name = "teachers.course"
    _description = "Teachers course"

    name = fields.Char(string='Name')
    surname = fields.Char(string='Surname')
    email = fields.Char(string='Email')
    course = fields.Char(string='Courses of the Teacher')
