from odoo import api, fields, models
from odoo.exceptions import ValidationError


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
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Open'),
         ('finished', 'Finished')],
        string='Course state',
        help="State of the course.",
        default='draft',
        required=True,
        readonly=True)

    description = fields.Char(string='Description')
    beginning_date = fields.Date(string='Beginning Date')
    end_date = fields.Date(string='End Date')
    # attachment = fields.Binary(string="Attachment Button")
    students = fields.Many2many('students.course', string='Students that enrolled this course')
    attachment = fields.Many2many('ir.attachment', string="Attachment Button")
    grades = fields.Selection(selection=[
        ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')
    ], required=True,
        )

    # @api.model
    # def create(self, vals):
    #     # record = ""
    #     record = super(Courses, self).create(vals)
    #     product_data = {"course_name": record.course_name}
    #     record.env["courses.course"].create(product_data)
    #
    #     return record

    def action_draft(self):
        for record in self:
            if record.state == "open" or record.state == "finished":
                record.state = "draft"
            else:
                raise ValidationError(
                    "You're course has "
                    "to be in open state "
                    "in order to change the "
                    "state to Draft."
                )

    def action_open(self):
        for rec in self:
            rec.state = 'open'

    def action_finished(self):
        for rec in self:
            rec.state = 'finished'

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
                'view_type': 'form',
                'view_mode': 'tree',
                'views': [(view_id, 'form')],
                'res_model': 'courses.course',
                'view_id': view_id,
                'type': 'ir.actions.act_window',
                'res_id': record.id,
                'target': 'new',
                'context': context,
            }

    def copy(self, default=None):
        return super(Courses, self).copy(default)

    def print_report(self):
        return self.env.ref('courses.report_courses').report_action(self)
