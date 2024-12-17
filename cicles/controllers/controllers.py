# -*- coding: utf-8 -*-
# from odoo import http


# class Cicles(http.Controller):
#     @http.route('/cicles/cicles', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cicles/cicles/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cicles.listing', {
#             'root': '/cicles/cicles',
#             'objects': http.request.env['cicles.cicles'].search([]),
#         })

#     @http.route('/cicles/cicles/objects/<model("cicles.cicles"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cicles.object', {
#             'object': obj
#         })

