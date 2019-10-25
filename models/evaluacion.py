# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Evaluacion(models.Model):
    _name = 'evaluacion.evaluacion'
    _description = 'Evaluación'


    nombre = fields.Char('Nombre')
    institucion = fields.Char('Nombre de la Institución')
    fecha= fields.Date('Fecha de Calificación')
    archivo=fields.Binary('Calificación')






    #tag_ids = fields.Many2many('evaluacion.requisitos')
