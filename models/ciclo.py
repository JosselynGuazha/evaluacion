# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Ciclo(models.Model):
    _name = 'evaluacion.ciclo'
    _description = 'Ciclo'


    nombre = fields.Char('Nombre del Ciclo')
    numero= fields.Integer('Ciclo')
    descrpcion = fields.Char('Descripcion del Ciclo')



    #tag_ids = fields.Many2many('evaluacion.requisitos')
