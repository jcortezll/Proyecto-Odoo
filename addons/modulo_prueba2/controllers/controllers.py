# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloPrueba2(http.Controller):
#     @http.route('/modulo_prueba2/modulo_prueba2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_prueba2/modulo_prueba2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_prueba2.listing', {
#             'root': '/modulo_prueba2/modulo_prueba2',
#             'objects': http.request.env['modulo_prueba2.modulo_prueba2'].search([]),
#         })

#     @http.route('/modulo_prueba2/modulo_prueba2/objects/<model("modulo_prueba2.modulo_prueba2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_prueba2.object', {
#             'object': obj
#         })
