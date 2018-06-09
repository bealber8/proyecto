# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Paquetes(models.Model):
    _name = 'transportes2.paquetes'

    name = fields.Integer(string="Código")
    descripcion = fields.Text(string="Descripción")
    destinatario = fields.Char(string = "Nombre y Apellidos")
    direccion = fields.Char(string="Dirección")
    fecha = fields.Date(string = "Fecha transporte")
    conductor_id = fields.Many2one('transportes2.conductores', string = "Conductor")

class Conductores(models.Model):
    _name = 'transportes2.conductores'

    name = fields.Char(string = "Nombre y Apellidos")
    dni = fields.Char()
    telefono = fields.Char(string="Teléfono")
    direccion = fields.Char(string="Dirección")
    salario = fields.Float()
    fechaNacimiento = fields.Date(string="Fecha de Nacimiento")
    horas_trabajo = fields.Many2one('resource.calendar', string = "Horas de trabajo")
    paquetes = fields.One2many('transportes2.paquetes', 'conductor_id', string = "Paquetes")
    camiones_ids = fields.Many2many('transportes2.camiones')

class Camiones(models.Model):
    _name = 'transportes2.camiones'

    name = fields.Char(string = "Matrícula")
    modelo = fields.Char()
    potencia = fields.Integer()
    conductores_ids = fields.Many2many('transportes2.conductores')