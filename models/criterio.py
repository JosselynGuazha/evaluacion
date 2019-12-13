# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Criterio(models.Model):
    _name = 'evaluacion.criterio'
    _description = 'Criterio'

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = '[' + record.nombre_criterio + ']'
            result.append((record.id, name))
        return result


    nombre_criterio = fields.Char('Nombre del Criterio')
    periodo_inicio = fields.Date('Fecha de Inicio Criterio')
    periodo_fin = fields.Date('Fecha Final del Criterio')

    subcriterio_ids = fields.One2many('evaluacion.subcriterio', 'criterio_id', string="Subcriterio")

 #un responsable por criterio



