# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Criterio(models.Model):
    _name = 'evaluacion.criterio'
    _description = 'Criterio'

    nombre_criterio = fields.Char('Nombre del Criterio')
    periodo_inicio = fields.Date('Fecha de Inicio Criterio')
    periodo_fin = fields.Date('Fecha Final del Criterio')

    periodoEvaluacion_id = fields.Many2one('evaluacion.periodo_evaluacion', 'Periodo de Evaluación')

    subcriterio_ids = fields.One2many('evaluacion.subcriterio', 'criterio_id', string="Malla")


