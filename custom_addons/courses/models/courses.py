from odoo import api, fields, models


class Courses(models.Model):
    _name = "courses.course"
    _description = "Courses course"

    teacher = fields.Many2one('teachers.course', string='Teacher')
    course_name = fields.Char(string='Course Name')
    field_of_study = fields.Char(string='Field of Study')
    semestar = fields.Selection([
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8')
    ])
    state = fields.Selection([
        ('draft', 'Draft'), ('open', 'Open'), ('finished', 'Finished')
    ], readonly=True)

    description = fields.Char(string='Description')
    beginning_date = fields.Date(string='Beginning Date')
    end_date = fields.Date(string='End Date')
    attachment = fields.Binary(string="Attachment Button")
    students = fields.Many2many('students.course', string='Students that enrolled this course')
