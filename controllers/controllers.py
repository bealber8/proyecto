# -*- coding: utf-8 -*-
from odoo import http

# class Transportes2(http.Controller):
#     @http.route('/transportes2/transportes2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transportes2/transportes2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('transportes2.listing', {
#             'root': '/transportes2/transportes2',
#             'objects': http.request.env['transportes2.transportes2'].search([]),
#         })

#     @http.route('/transportes2/transportes2/objects/<model("transportes2.transportes2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transportes2.object', {
#             'object': obj
#         })