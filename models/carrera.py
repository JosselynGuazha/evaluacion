# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Carrera(models.Model):
    _name = 'evaluacion.carrera'
    _description = 'Carrera'

    @api.multi
    def name_get(self):
        result=[]
        for record in self:
            name = record.nombre_carrera
            result.append((record.id, name))
        return result

    nombre_carrera = fields.Char('Nombre de la Carrera')
    codigo_carrera = fields.Char('Código Carrera ')
    modalidad = fields.Selection([
        ('presencial', 'Presencial'),
        ('semipresencial', 'Semipresencial'),
        ('distancia', 'Distancia'),
    ], "Modalidad", readonly=True, default="presencial")
    descripcion = fields.Char('Descripción de la Carrera')

    periodoAcademico_id = fields.Many2one('evaluacion.periodo_academico', 'Periodo Academico')

    practicas_ids = fields.One2many('evaluacion.practicas', 'carrera_id', string="Practica")

    malla_ids = fields.One2many('evaluacion.malla', 'carrera_id', string="Malla")
