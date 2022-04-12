# -*- coding: utf-8 -*-
# from odoo import http


# class Custom/testModule(http.Controller):
#     @http.route('/custom/test_module/custom/test_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/test_module/custom/test_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom/test_module.listing', {
#             'root': '/custom/test_module/custom/test_module',
#             'objects': http.request.env['custom/test_module.custom/test_module'].search([]),
#         })

#     @http.route('/custom/test_module/custom/test_module/objects/<model("custom/test_module.custom/test_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom/test_module.object', {
#             'object': obj
#         })
