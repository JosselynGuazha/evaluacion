# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Practicas(models.Model):
    _name = 'evaluacion.practicas'
    _description = 'Prácticas'


    nombre = fields.Char('Nombre Practicas Pre-Profesionales')
    descrpcion = fields.Char('Descripcion de las Practicas')
    informe = fields.Binary('Informe')

    carrera_id = fields.Many2one('evaluacion.carrera', 'Carrera')


