from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Grades(models.TransientModel):
    _name = "grades.course"
    _description = "Grades course"

    students = fields.Many2one('students.course', string="Students",
                               required=False, ondelete='cascade')
    course_id = fields.Many2one('courses.course', string="Course Name",
                           required=False, ondelete='cascade')
    grades = fields.Selection(selection=[
        ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
    ], required=False,
        string="Grades")
