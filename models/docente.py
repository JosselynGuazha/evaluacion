# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Docente(models.Model):
    _name = 'evaluacion.docente'
    _description = 'Docente'

    cedula = fields.Char('Cedula de Ciudadania')
    nombre = fields.Char('Nombres del Docente')
    correo_electronico = fields.Char('Correo del Docente')
    telefono = fields.Char('Número de telefono')
    direccion = fields.Char('Dirección del Docente')

    asignatura_ids = fields.One2many('evaluacion.asignatura', 'docente_id', string="Asigantura")
    cursos_realizados_ids = fields.One2many('evaluacion.cursos_realizados', 'docente_id', string="Cursos Realzados")



