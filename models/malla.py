# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Malla(models.Model):
    _name = 'evaluacion.malla'
    _description = 'Malla'


    nombre = fields.Char('Nombre Practicas Pre-Profesionales')
    fecha_origen= fields.Char('Fecha Origen de la Malla')
    descripcion = fields.Char('Descripcion de la Malla')

    carrera_id = fields.Many2one('evaluacion.carrera', 'Carrera')

    #tag_ids = fields.Many2many('evaluacion.requisitos')
