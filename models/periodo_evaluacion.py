# -*- coding: utf-8 -*

from odoo import models, fields, api


class PeriodoEvaluacion(models.Model):
    _name = 'evaluacion.periodo_evaluacion'
    _description = 'Periodo de Evaluación'

    fecha_inicio = fields.Date('Fecha Inicio de Evaluación')
    fecha_fin = fields.Date('Fecha Fin de Evaluación')
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], "Estado", readonly=True, default="inactivo")

    periodoAcademico_ids = fields.One2many('evaluacion.periodo_academico', 'periodoEvaluacion_id', string="Periodos Academicos")
    criterio_ids = fields.One2many('evaluacion.criterio', 'periodoEvaluacion_id', string="Criterio")
