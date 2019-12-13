# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Asignatura(models.Model):
    _name = 'evaluacion.asignatura'
    _description = 'Asignatura'

    @api.multi
    def name_get(self):
        result=[]
        for record in self:
            name = record.nombre
            result.append((record.id, name))
        return result

    nombre = fields.Char('Nombre de la Asignatura')
    codigo= fields.Char('Código')
    silabo = fields.Binary('Silabo')

    ciclo_id = fields.Many2one('evaluacion.ciclo', 'Ciclo')
    docente_id = fields.Many2one('evaluacion.docente', 'Docente')
