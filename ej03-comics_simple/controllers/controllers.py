# -*- coding: utf-8 -*-
# from odoo import http


# class Ej03-comicsSimple/(http.Controller):
#     @http.route('/ej03-comics_simple//ej03-comics_simple/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ej03-comics_simple//ej03-comics_simple//objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ej03-comics_simple/.listing', {
#             'root': '/ej03-comics_simple//ej03-comics_simple/',
#             'objects': http.request.env['ej03-comics_simple/.ej03-comics_simple/'].search([]),
#         })

#     @http.route('/ej03-comics_simple//ej03-comics_simple//objects/<model("ej03-comics_simple/.ej03-comics_simple/"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ej03-comics_simple/.object', {
#             'object': obj
#         })

