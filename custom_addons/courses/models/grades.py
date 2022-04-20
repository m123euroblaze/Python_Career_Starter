from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Grades(models.TransientModel):
    _name = "grades.course"
    _description = "Grades course"

    students = fields.Many2one('students.course', string="Student who has grade for the course",
                               required=True, readonly=True)
    course_name = fields.Many2one('courses.course', string="What grade has the student for this course",
                                  required=True, readonly=True)
    grades = fields.Selection(selection=[
        ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
    ], required=True,
       )

    def action_insert_grades(self):
        for record in self:
            form_name = ""

            if record.state == "open":
                form_name = "Insert Grades"
            elif record.state == "finished":
                form_name = "View Grades"

            view_id = record.env.ref('courses.view_grades_course_form').id
            context = record._context.copy()

            return {
                'name': form_name,
                'view_mode': 'tree',
                'views': [(view_id, 'form')],
                'res_model': 'courses.course',
                'view_id': view_id,
                'type': 'ir.actions.act_window',
                'res_id': record.id,
                'target': 'new',
                'context': context,

            }


