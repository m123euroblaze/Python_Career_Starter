from odoo import api, fields, models, _


class Students(models.Model):
    _name = "students.course"
    _description = "Students course"

    name = fields.Char(string='Name')
    surname = fields.Char(string='Surname')
    email = fields.Char(string='Email')
    enrolled_year = fields.Integer(string='Enrolled year')
    birth_date = fields.Date(string='Date')
    index = fields.Char(string='Index')
    index_seq = fields.Char(string='Index Unique', required=True, copy=False, readonly=True,
                            index=True, default=lambda self: _('New'))
    students = fields.Many2many('courses.course', string='Students that enrolled this course')

    @api.model
    def create(self, vals):
        if not vals.get('index'):
            vals['index'] = 'New Student'
        if vals.get('index_seq', _('New')) == _('New'):
            vals['index_seq'] = self.env['ir.sequence'].next_by_code('students.course') or _('New')
        res = super(Students, self).create(vals)
        return res
