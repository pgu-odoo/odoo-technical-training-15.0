# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):

    _name = 'academy.course'
    _description = 'Course info'


    name = fields.Char(string='Title', required=True)
    description = fields.Char(string='Description')

    level = fields.Selection(string='Level',
                             selection=[('beginner', 'Beginner'),
                                        ('immediate', 'Immediate'),
                                        ('advance', 'Advance')],
                            copy=False)
    active = fields.Boolean(string='Active', default=True)
