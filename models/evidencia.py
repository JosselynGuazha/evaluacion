# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Evidencia(models.Model):
    _name = 'evaluacion.evidencia'
    _description = 'Evidencia'


    nombre = fields.Char('Nombre del Archivo')
    referencia = fields.Char('Referencia del Archivo')
    fecha = fields.Date('Fecha de carga')
    archivo = fields.Binary('Archivo')

    subcriterio_id = fields.Many2one('evaluacion.subcriterio', 'Subcriterio')

