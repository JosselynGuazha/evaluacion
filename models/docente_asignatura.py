# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DocenteAsignatura(models.Model):
    _name = 'evaluacion.docente_asignatura'
    _description = 'Asignar Asignatura a Docente'

    docente_id = fields.Many2one('evaluacion.docente', 'Docente')
    carrera_id = fields.Many2one('evaluacion.carrera', 'Carrera')
    ciclo_id = fields.Many2one('evaluacion.ciclo', 'Ciclo')
    asignatura_id = fields.Many2one('evaluacion.asignatura', 'Asignatura')



