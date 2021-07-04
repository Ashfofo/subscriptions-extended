# -*- coding: utf-8 -*-
# from odoo import http


# class Subscriptions-extended(http.Controller):
#     @http.route('/subscriptions-extended/subscriptions-extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subscriptions-extended/subscriptions-extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('subscriptions-extended.listing', {
#             'root': '/subscriptions-extended/subscriptions-extended',
#             'objects': http.request.env['subscriptions-extended.subscriptions-extended'].search([]),
#         })

#     @http.route('/subscriptions-extended/subscriptions-extended/objects/<model("subscriptions-extended.subscriptions-extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subscriptions-extended.object', {
#             'object': obj
#         })
