# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Asignatura(models.Model):
    _name = 'evaluacion.asignatura'
    _description = 'Asignatura'


    nombre = fields.Char('Nombre de la Asignatura')
    codigo= fields.Char('Código')
    silabo = fields.Binary('Silabo')

    ciclo_id = fields.Many2one('evaluacion.ciclo', 'Ciclo')
    docente_id = fields.Many2one('evaluacion.docente', 'Docente')






    #tag_ids = fields.Many2many('evaluacion.requisitos')
