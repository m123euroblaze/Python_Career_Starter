import requests
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class Courses(CustomerPortal):

    @http.route("/courses/", type='http', auth='user', website=True)
    def list_courses(self, **kw):
        print(1)
        partner = request.env.user.partner_id
        student_id = request.env['students.course'].sudo().search([('student_access', '=', partner.id)], limit=1)
        teacher_id = request.env['teachers.course'].sudo().search([('teacher_access', '=', partner.id)], limit=1)
        if student_id:
            values = {}
            courses = request.env['courses.course'].sudo().search([('state', '=', 'open')])
            values.update({'courses': courses})
            print(2)
            return request.render('courses.list_courses', values)
        if teacher_id:
            values = {}
            courses = request.env['courses.course'].sudo().search(
                [('state', '=', 'open'), ('teacher', '=', teacher_id.id)])
            values.update({'courses': courses})
            print(3)
            return request.render('courses.list_courses', values)
        else:
            print(4)
            return request.render('website.page_404')

    @http.route("/courses/<int:courses_id>/", type='http', auth='user', website=True)
    def students_in_courses(self, courses_id):
        course = request.env['courses.course'].sudo().search([('id', '=', courses_id)], limit=1)
        if not course:
            return request.render('website.page_404')
        elif course.state != 'open':
            return request.render('website.page_404')
        else:
            values = {'courses': course}
            return request.render('courses.view_course', values)


