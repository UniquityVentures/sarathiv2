# -*- coding: utf-8 -*-
# from odoo import http


# class Topic(http.Controller):
#     @http.route('/topic/topic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/topic/topic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('topic.listing', {
#             'root': '/topic/topic',
#             'objects': http.request.env['topic.topic'].search([]),
#         })

#     @http.route('/topic/topic/objects/<model("topic.topic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('topic.object', {
#             'object': obj
#         })

