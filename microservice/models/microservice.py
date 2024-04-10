# -*- coding: utf-8 -*-

from odoo import models, fields, api


class microservice_microservice(models.Model):
    _name = 'microservice.microservice'
    _description = "Microservice"

    
    name = fields.Char(string="Name", size=100)
        
    url = fields.Char(string="URL location", size=200)


    def test_service(self):
        pass