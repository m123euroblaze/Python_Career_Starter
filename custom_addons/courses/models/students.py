from odoo import api, fields, models, _
import passlib
import datetime


class Students(models.Model):
    _name = "students.course"
    _description = "Students course"

    name = fields.Char(string='Name', compute='get_full_name', readonly=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email')
    enrolled_year = fields.Date(string='Enrolled year')
    birth_date = fields.Date(string='Birth date')
    index_number = fields.Char(string='Index Number', required=False, readonly=True, unique=True)
    students = fields.Many2many('courses.course', string='Students that enrolled this course')
    student_access = fields.Many2one('res.partner', readonly=True)
    student_grades = fields.One2many('grades.course', 'students', string='Grades')
    field_of_study = fields.Char(string='Field of Study')

    def get_full_name(self):
        for record in self:
            record.name = f'{record.first_name} {record.last_name}'

    @api.model
    def default_index_number(self):
        year = datetime.date.today().year
        index = self.env['ir.sequence'].next_by_code('index.number')
        index = f'{str(index)}/{year}'
        return index

    @api.model
    def create(self, vals):
        rec = super(Students, self).create(vals)
        rec.write({'index_number': self.default_index_number()})

        contact_data = {
            'name': rec.name,
            'email': rec.email
        }
        contact = self.env['res.partner'].create(contact_data)
        if contact:
            rec.write({'student_access': contact.id})
            user = self.env['res.users'].sudo().create({'partner_id': contact.id, 'login': contact.email})
            crypt_context = passlib.context.CryptContext(["pbkdf2_sha512", "hex_md5", "plaintext"],
                                                         deprecated=["hex_md5", "plaintext"])
            hashed_password = crypt_context.hash('admin')
            self.env['res.users']._set_encrypted_password(user.id, hashed_password)
            group_portal = self.env.ref('base.group_portal')
            # group_course = self.env.ref('courses.group_courses')
            user.write({'groups_id': [(6, 0, [group_portal.id])]})
        return rec
