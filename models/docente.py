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
    cursos_realizados_ids = fields.One2many('evaluacion.cursos_realizados', 'docente_id', string="Cursos realizados")



<<<<<<< HEAD
    cursos_realizados_ids = fields.One2many('evaluacion.cursos_realizados', 'docente_id', string="Cursos realizados")


    #tag_ids = fields.Many2many('evaluacion.requisitos')
=======
>>>>>>> 894d43837e21dfe12ffe701fcd11b97dfd752868
