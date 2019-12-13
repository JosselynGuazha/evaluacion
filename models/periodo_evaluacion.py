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
    ], "Estado", readonly=True, default="activo")

    periodoAcademico_id = fields.Many2many('evaluacion.periodo_academico', string="Periodos Academicos")
    criterio_id = fields.Many2many('evaluacion.criterio', string="Criterio")


