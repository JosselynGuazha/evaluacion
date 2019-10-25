# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Asignatura(models.Model):
    _name = 'evaluacion.asignatura'
    _description = 'Asignatura'


    nombre = fields.Char('Nombre de la Asignatura')
    codigo= fields.Char('Código')
    silabo = fields.Binary('Silabo')






    #tag_ids = fields.Many2many('evaluacion.requisitos')
