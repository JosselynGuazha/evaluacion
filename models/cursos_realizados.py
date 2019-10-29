# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CursosRealizados(models.Model):
    _name = 'evaluacion.cursos_realizados'
    _description = 'Cursos Realizados'


    nombre_curso = fields.Char('Nombre del Curso realizado')
    institucion = fields.Char('Nombre de la Institución')
    fecha_inicio= fields.Date('Fecha de Inicio del Curso')
    fecha_fin = fields.Date('Fecha de Finalización Curso')
    certificado=fields.Binary('Certificado del Curso')

    docente_id = fields.Many2one('evaluacion.docente', 'Docente')






