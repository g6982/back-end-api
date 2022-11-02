# -*- coding: utf-8 -*-
# from odoo import http


# class ApiTicket(http.Controller):
#     @http.route('/api_ticket/api_ticket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/api_ticket/api_ticket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('api_ticket.listing', {
#             'root': '/api_ticket/api_ticket',
#             'objects': http.request.env['api_ticket.api_ticket'].search([]),
#         })

#     @http.route('/api_ticket/api_ticket/objects/<model("api_ticket.api_ticket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('api_ticket.object', {
#             'object': obj
#         })
