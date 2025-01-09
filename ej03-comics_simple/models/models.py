# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ej03-comics_simple/(models.Model):
#     _name = 'ej03-comics_simple/.ej03-comics_simple/'
#     _description = 'ej03-comics_simple/.ej03-comics_simple/'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

