# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ciclo(models.Model):
    _name = 'evaluacion.ciclo'
    _description = 'Ciclo'

    @api.multi
    def name_get(self):
        result=[]
        for record in self:
            name = record.numero
            result.append((record.id, name))
        return result

    nombre = fields.Char('Nombre del Ciclo')
    numero= fields.Char('Número de Ciclo')
    descripcion = fields.Char('Descripción del Ciclo')

    malla_id = fields.Many2one('evaluacion.malla', 'Malla')
    asignatura_ids = fields.One2many('evaluacion.asignatura', 'ciclo_id', string="Asignatura")
