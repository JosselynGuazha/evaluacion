# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Evidencia(models.Model):
    _name = 'evaluacion.evidencia'
    _description = 'Evidencia'

    @api.multi
    def name_get(self):
        result=[]
        for record in self:
            name = '['+ record.nombre+']'
            result.append((record.id, name))
        return result


    elementos_fundamentales=fields.Char('Elementos fundamentales')
    nombre = fields.Char('Nombre del Archivo')
    referencia = fields.Char('Referencia del Archivo')
    fecha = fields.Date('Fecha de carga')
    archivo = fields.Binary('Archivo')

    user_id = fields.Many2one(
        comodel_name='evaluacion.usuarios',
        string='Responsable',
        #default=lambda self: self.env.user.id
    )




    criterio_id = fields.Many2one('evaluacion.criterio', 'Criterio')
    subcriterio_id = fields.Many2one('evaluacion.subcriterio', 'Subcriterio')
    indicador_id = fields.Many2one('evaluacion.indicador', 'Indicador')
