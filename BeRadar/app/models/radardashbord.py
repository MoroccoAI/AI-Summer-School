# -*- coding: utf-8 -*-

from dataclasses import Field
from email.policy import default
import string
from odoo import models, fields, api


class RadarDashbord(models.Model):
    _name = 'radar.dashbord'
    _description = 'Radar Dashbord'

    total_wells = fields.Integer(string='Nombre Puits')
    auth_wells = fields.Integer(string='Autorisés')
    n_auth_wells = fields.Integer(string='Non Autorisés')
    infractions = fields.Integer(string='Infractions')


    