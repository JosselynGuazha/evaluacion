# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CursosRealizados(models.Model):
    _name = 'evaluacion.cursos_realizados'
    _description = 'Cursos Realizados'


    nombre_curso = fields.Char('Nombre de la Institución')
    institucion = fields.Char('Nombre de la Institución')
    fecha_inicio= fields.Date('Fecha de Inicio')
    fecha_fin = fields.Date('Fecha de Finalización')
    certificado=fields.Binary('Certificado del Curso')

    docente_id = fields.Many2one('evaluacion.docente', 'Docente')






    #tag_ids = fields.Many2many('evaluacion.requisitos')
