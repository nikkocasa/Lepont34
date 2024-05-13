# -*- coding: utf-8 -*-
# from odoo import http


# class EventHideRegistrationButton(http.Controller):
#     @http.route('/event_hide_registration_button/event_hide_registration_button', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/event_hide_registration_button/event_hide_registration_button/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('event_hide_registration_button.listing', {
#             'root': '/event_hide_registration_button/event_hide_registration_button',
#             'objects': http.request.env['event_hide_registration_button.event_hide_registration_button'].search([]),
#         })

#     @http.route('/event_hide_registration_button/event_hide_registration_button/objects/<model("event_hide_registration_button.event_hide_registration_button"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('event_hide_registration_button.object', {
#             'object': obj
#         })
