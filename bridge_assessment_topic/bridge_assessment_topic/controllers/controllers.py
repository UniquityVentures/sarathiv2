# -*- coding: utf-8 -*-
# from odoo import http


# class BridgeAssessmentTopic(http.Controller):
#     @http.route('/bridge_assessment_topic/bridge_assessment_topic', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bridge_assessment_topic/bridge_assessment_topic/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bridge_assessment_topic.listing', {
#             'root': '/bridge_assessment_topic/bridge_assessment_topic',
#             'objects': http.request.env['bridge_assessment_topic.bridge_assessment_topic'].search([]),
#         })

#     @http.route('/bridge_assessment_topic/bridge_assessment_topic/objects/<model("bridge_assessment_topic.bridge_assessment_topic"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bridge_assessment_topic.object', {
#             'object': obj
#         })

