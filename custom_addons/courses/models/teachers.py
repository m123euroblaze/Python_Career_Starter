import passlib

from odoo import api, fields, models


class Teachers(models.Model):
    _name = "teachers.course"
    _description = "Teachers course"

    name = fields.Char(string='Name', compute='get_full_name', readonly=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email')
    courses_ids = fields.One2many('courses.course', 'teacher', string='Courses')
    teacher_access = fields.Many2one('res.partner')

    def get_full_name(self):
        for record in self:
            record.name = f'{record.first_name} {record.last_name}'

    @api.model
    def create(self, vals):
        rec = super(Teachers, self).create(vals)

        contact_data = {
            'name': rec.name,
            'email': rec.email
        }
        contact = self.env['res.partner'].create(contact_data)
        if contact:
            rec.write({'teacher_access': contact.id})
            user = self.env['res.users'].sudo().create({'partner_id': contact.id, 'login': contact.email})
            crypt_context = passlib.context.CryptContext(["pbkdf2_sha512", "hex_md5", "plaintext"],
                                                         deprecated=["hex_md5", "plaintext"])
            hashed_password = crypt_context.hash('admin')
            self.env['res.users']._set_encrypted_password(user.id, hashed_password)
            group_portal = self.env.ref('base.group_portal')
            # group_courses = self.env.ref('courses.group_courses')
            user.write({'groups_id': [(6, 0, [group_portal.id])]})

        return rec
