# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Evaluacion(models.Model):
    _name = 'evaluacion.evaluacion'
    _description = 'Evaluación'


    institucion = fields.Char('Nombre de la Institución')
    fecha= fields.Date('Fecha de Calificación')
    archivo=fields.Binary('Calificación')

    docente_id = fields.Many2one('evaluacion.docente', 'Docente')






