# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Experiencia(models.Model):
    _name = 'evaluacion.experiencia'
    _description = 'Experiencia'


    nombre_institucion = fields.Char('Nombre de la Institución')
    fecha_inicio= fields.Date('Fecha Inicio')
    fecha_fin = fields.Date('Fecha Fin')
    cargo = fields.Char('Cargo')
    certificado_trabajo=fields.Binary('Certificado de Trabajo')

    docente_id = fields.Many2one('evaluacion.docente', 'Docente')







