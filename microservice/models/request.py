# -*- coding: utf-8 -*-
import uuid

from odoo import models, fields, api

from .constants import REQUEST_STATE

class microservice_request(models.Model):
    _name = 'microservice.request'
    _description = "Microservice request"


    microservice = fields.Many2one('microservice.microservice', string="Microservice", ondelete='set null')
    
    task = fields.Many2one('microservice.task', string="Task", ondelete='set null')

    name = fields.Char(string="UID", size=36, default=lambda self: str(uuid.uuid4()))

    state = fields.Selection(REQUEST_STATE, string="Status", default="initial")

    params = fields.Text(string="Params")

    result = fields.Text(string="Result")

    error_message = fields.Text(string="Error Message")

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, "%s [%s]" % (rec.name, rec.task.name or '')))
        return result
