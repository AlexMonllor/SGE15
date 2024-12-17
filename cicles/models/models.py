from odoo import models, fields

# Modelo Cicle Formatiu
class CicleFormatiu(models.Model):
    _name = 'cicle.formatiu'
    _description = 'Cicle Formatiu'
    
    name = fields.Char(string="Nom del Cicle", required=True)
    descripcio = fields.Text(string="Descripció")
    moduls_ids = fields.One2many('cicle.formatiu.modul', 'cicle_id', string="Mòduls")

# Modelo Mòdul
class Modul(models.Model):
    _name = 'cicle.formatiu.modul'
    _description = 'Mòdul'

    name = fields.Char(string="Nom del Mòdul", required=True)
    cicle_id = fields.Many2one('cicle.formatiu', string="Cicle Formatiu", required=True)
    professor_id = fields.Many2one('cicle.formatiu.professor', string="Professor", required=True)
    alumne_ids = fields.Many2many('cicle.formatiu.alumne', string="Alumnes")

# Modelo Alumne
class Alumne(models.Model):
    _name = 'cicle.formatiu.alumne'
    _description = 'Alumne'

    name = fields.Char(string="Nom de l'Alumne", required=True)
    mòduls_ids = fields.Many2many('cicle.formatiu.modul', string="Mòduls Matriculats")

# Modelo Professor
class Professor(models.Model):
    _name = 'cicle.formatiu.professor'
    _description = 'Professor'

    name = fields.Char(string="Nom del Professor", required=True)
    num_collegiat = fields.Char(string="Número de Col·legiat", required=True)
    mòduls_ids = fields.One2many('cicle.formatiu.modul', 'professor_id', string="Mòduls Imparteix")
