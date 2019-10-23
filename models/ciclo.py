# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ciclo(models.Model):
    _name = 'evaluacion.ciclo'
    _description = 'Ciclo'


    nombre = fields.Char('Nombre del Ciclo')
    numero= fields.Integer('Ciclo')
    descripcion = fields.Char('Descripcion del Ciclo')

    malla_id = fields.Many2one('evaluacion.malla', 'Malla')




    #tag_ids = fields.Many2many('evaluacion.requisitos')
