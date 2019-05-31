# -*- coding: utf-8 -*-
from odoo import http

# class FlixaFashion(http.Controller):
#     @http.route('/flixa_fashion/flixa_fashion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flixa_fashion/flixa_fashion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('flixa_fashion.listing', {
#             'root': '/flixa_fashion/flixa_fashion',
#             'objects': http.request.env['flixa_fashion.flixa_fashion'].search([]),
#         })

#     @http.route('/flixa_fashion/flixa_fashion/objects/<model("flixa_fashion.flixa_fashion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flixa_fashion.object', {
#             'object': obj
#         })