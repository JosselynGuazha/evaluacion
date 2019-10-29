# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Malla(models.Model):
    _name = 'evaluacion.malla'
    _description = 'Malla'


    nombre = fields.Char('Nombre de la Malla')
    fecha_origen= fields.Date('Fecha Origen de la Malla')
    descripcion = fields.Char('Descripcion de la Malla')

    carrera_id = fields.Many2one('evaluacion.carrera', 'Carrera')
    ciclo_ids = fields.One2many('evaluacion.ciclo', 'malla_id', string="Ciclo")

    #tag_ids = fields.Many2many('evaluacion.requisitos')
