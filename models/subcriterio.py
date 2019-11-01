# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subcriterio(models.Model):
    _name = 'evaluacion.subcriterio'
    _description = 'Subcriterio'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = '[' + record.nombre_subcriterio + ']'
            result.append((record.id, name))
        return result

    nombre_subcriterio = fields.Char('Nombre del Subcriterio')
    estado_subcriterio = fields.Selection([
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ], "Estado", readonly=True, default="inactivo")
    descripcion = fields.Char('Descripcion del Subcriterio')
    fecha_creacion = fields.Date('Fecha Creación')

    criterio_id = fields.Many2one('evaluacion.criterio', 'Criterio')
    indicador_ids = fields.One2many('evaluacion.indicador', 'subcriterio_id', string="Indicador")





