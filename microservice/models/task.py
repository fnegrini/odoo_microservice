# -*- coding: utf-8 -*-

from odoo import models, fields, api


class microservice_task(models.Model):
    _name = 'microservice.task'
    _description = "Microservice task"

    
    group = fields.Many2one('microservice.task.group', string="Group", ondelete='set null')

    code = fields.Char(string="Code", size=20)
    
    name = fields.Char(string="Name", size=150)

    model = fields.Many2one('ir.model', string="Model", ondelete='set null')

    run_before = fields.Text(string="Run before request")

    request = fields.Text(string="Request")

    run_after = fields.Text(string="Run code after response")

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        recs = []
        if name:
            recs = self.search([('code', operator, name)] + args, limit=limit)
        if not recs:
            recs = self.search([('name', operator, name)] + args, limit=limit)
        return [rec.id for rec in recs]

    
    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, "%s - %s" % (rec.code, rec.name or '')))
        return result
