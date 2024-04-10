# -*- coding: utf-8 -*-
from odoo import http

# class GrifoFile(http.Controller):
#     @http.route('/grifo_file/grifo_file/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grifo_file/grifo_file/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('grifo_file.listing', {
#             'root': '/grifo_file/grifo_file',
#             'objects': http.request.env['grifo_file.grifo_file'].search([]),
#         })

#     @http.route('/grifo_file/grifo_file/objects/<model("grifo_file.grifo_file"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grifo_file.object', {
#             'object': obj
#         })