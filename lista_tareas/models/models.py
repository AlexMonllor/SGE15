# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lista_tareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolena(compute="_value_urgente", store=True)
    realizada = fields.Text()

    @api.depends('value')
    def _value_urgente(self):
        for record in self:
            if record.prioridad>10:
                record.urgente= True
            else:
                record.urgente = False
