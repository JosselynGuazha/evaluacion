# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subcriterio(models.Model):
    _name = 'evaluacion.subcriterio'
    _description = 'Subcriterio'

    nombre_subcriterio = fields.Char('Nombre del Subcriterio')
    estado_subcriterio = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], "Estado", readonly=True, default="inactivo")
    tipo_subcriterio = fields.Selection([
        ('organizacion', 'Organización'),
        ('docencia', 'Docencia'),
        ('investigacion_desarrollo', 'Investigacion y Desarrollo Experimental'),
        ('vinculacion_sociedad', 'Vinculación con la Saciedad'),
        ('recursos_infraestructura', 'Recursos e infraestructura'),
        ('estudiantes', 'Estudiantes'),
    ], "Tipo de Subcriterio", readonly=True, default="organizacion")
    descripcion = fields.Char('Descripcion del Subcriterio')
    fecha_creacion = fields.Date('Fecha Creación')

    criterio_id = fields.Many2one('evaluacion.criterio', 'Criterio')
    evidencia_ids = fields.One2many('evaluacion.evidencia', 'subcriterio_id', string="Malla")

    criterio_id

