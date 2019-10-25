# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Referencia(models.Model):
    _name = 'evaluacion.referencia'
    _description = 'Referencias'


    nombre_referencia = fields.Char('Nombre')
    institucion = fields.Char('Nombre de la Institución')
    correo = fields.Char('Correo Electronico')
    telefono = fields.Char('Telefono o Celular de la Referencia')
    certificado=fields.Binary('Certificado del Curso')






    #tag_ids = fields.Many2many('evaluacion.requisitos')
