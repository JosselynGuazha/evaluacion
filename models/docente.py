# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Docente(models.Model):
    _name = 'evaluacion.docente'
    _description = 'Docente'

    @api.multi
    def name_get(self):
        result=[]
        for record in self:
            name = record.nombre
            result.append((record.id, name))
        return result

    @api.one
    @api.depends('user_id')
    def _get_cedula(self):
        if self.user_id.cedula:
            self.cedula = self.user_id.cedula

    @api.one
    @api.depends('user_id')
    def _get_nombres(self):
        if self.user_id.usuario_name and self.user_id.apellidos:
            self.nombre = self.user_id.usuario_name + " " + self.user_id.apellidos

    @api.one
    @api.depends('user_id')
    def _get_correo(self):
        if self.user_id.email:
            self.correo_electronico = self.user_id.email

    @api.one
    @api.depends('user_id')
    def _get_telefono(self):
        if self.user_id.celular:
            self.telefono = self.user_id.celular

    @api.one
    @api.depends('user_id')
    def _get_direccion(self):
        if self.user_id.direccion_domicilio:
            self.direccion = self.user_id.direccion_domicilio

    user_id = fields.Many2one(
        comodel_name='evaluacion.usuarios',
        string='Docente',
    )
    cedula = fields.Char('Cedula de Ciudadania', compute='_get_cedula', store=True)
    nombre = fields.Char('Nombres del Docente', compute='_get_nombres', store=True)
    correo_electronico = fields.Char('Correo del Docente',  compute='_get_correo', store=True)
    telefono = fields.Char('Número de telefono', compute='_get_telefono', store=True)
    direccion = fields.Char('Dirección del Docente', compute='_get_direccion', store=True)

    asignatura_ids = fields.One2many('evaluacion.asignatura', 'docente_id', string="Asigantura")
    cursos_realizados_ids = fields.One2many('evaluacion.cursos_realizados', 'docente_id', string="Cursos realizados")
    experiencia_ids = fields.One2many('evaluacion.experiencia', 'docente_id', string="Experiencia")
    referencia_ids = fields.One2many('evaluacion.referencia', 'docente_id', string="Referencia")
    evaluacion_ids = fields.One2many('evaluacion.evaluacion', 'docente_id', string="Evaluación")
