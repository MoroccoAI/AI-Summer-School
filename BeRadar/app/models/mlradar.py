# -*- coding: utf-8 -*-

from dataclasses import Field
from email.policy import default
import string
from odoo import models, fields, api


class MlRadar(models.Model):
    _name = 'ml.radar'
    _description = 'Radar database'
    
    farm_id = fields.Integer(string='Id Ferme')
    owner=fields.Char(string='Propriétaire')
    cin=fields.Char(string='CIN')
    long = fields.Char(string='Longitude')
    lat = fields.Char(string='Latitude')
    farm_ref = fields.Char(string='Référence Ferme')
    well_ref = fields.Char(string='Référence Puit')
    region = fields.Selection([("souss","Souss"),("elhaouz","El Haouz"),("chaouia","chaouia"),("loukouss","loukouss")], string='Région')
    is_zone_authorized = fields.Boolean(string="Zone autorisée",default=False)
    is_well_authorized = fields.Boolean(string="Puit autorisé",default=False)
    is_alerted = fields.Boolean(string="Infraction",default=False)
    area = fields.Integer(string="Superficie")
    id_img = fields.Binary(string=" ")
    alert_date = fields.Date(string="Date Alerte")


    