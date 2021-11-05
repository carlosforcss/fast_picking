# -*- coding: utf-8 -*-
from odoo import http

# class MoldService(http.Controller):
#     @http.route('/mold_service/mold_service/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mold_service/mold_service/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mold_service.listing', {
#             'root': '/mold_service/mold_service',
#             'objects': http.request.env['mold_service.mold_service'].search([]),
#         })

#     @http.route('/mold_service/mold_service/objects/<model("mold_service.mold_service"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mold_service.object', {
#             'object': obj
#         })