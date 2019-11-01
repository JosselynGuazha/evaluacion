# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Indicador(models.Model):
    _name = 'evaluacion.indicador'
    _description = 'Indicador'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = '[' + record.nombre_indicador + ']'
            result.append((record.id, name))
        return result

    nombre_indicador = fields.Char('Nombre del Indicador')
    descripcion = fields.Char('Descripción')
    fecha_creacion = fields.Date('Fecha Creación Indicador')

    subcriterio_id = fields.Many2one('evaluacion.subcriterio', 'Subcriterio')
    evidencia_ids = fields.One2many('evaluacion.evidencia', 'indicador_id', string="Evidencia")


