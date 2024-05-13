# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class event_hide_registration_button(models.Model):
#     _name = 'event_hide_registration_button.event_hide_registration_button'
#     _description = 'event_hide_registration_button.event_hide_registration_button'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
