# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PeriodoAcademico(models.Model):
    _name = 'evaluacion.periodo_academico'
    _description = 'Periodo Académico'

    fecha_inicio = fields.Date('Fecha Inicio Periodo Acadèmico')
    fecha_fin = fields.Date('Fecha Fin Periodo Acadèmico')
    estado = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], "Estado", readonly=True, default="activo")


    carrera_ids = fields.One2many('evaluacion.carrera', 'periodoAcademico_id', string="Carrera")



