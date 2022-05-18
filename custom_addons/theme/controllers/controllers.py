# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/theme(http.Controller):
#     @http.route('/custom/theme/custom/theme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/theme/custom/theme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/theme.listing', {
#             'root': '/custom/theme/custom/theme',
#             'objects': http.request.env['custom/theme.custom/theme'].search([]),
#         })

#     @http.route('/custom/theme/custom/theme/objects/<model("custom/theme.custom/theme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/theme.object', {
#             'object': obj
#         })
