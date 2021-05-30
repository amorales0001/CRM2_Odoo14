# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

class VisitControl(http.Controller):

    @http.route('/api/visits', auth='public', method=["GET"], csrf=False)
    def get_visits(self, **kw): #Podemos pasar el número de atributos que queramos una vez invocada la función
        try:  #bloque try-catch
            visits = http.request.env['custom_crm2.visit'].sudo().search_read([], ['id', 'name', 'customer', 'done'])
            res = json.dumps(visits, ensure_ascii=False).encode('utf-8') #Transforma el objeto array en una estructura JSON
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)

# class CustomCrm2(http.Controller):
#     @http.route('/custom_crm2/custom_crm2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_crm2/custom_crm2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_crm2.listing', {
#             'root': '/custom_crm2/custom_crm2',
#             'objects': http.request.env['custom_crm2.custom_crm2'].search([]),
#         })

#     @http.route('/custom_crm2/custom_crm2/objects/<model("custom_crm2.custom_crm2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_crm2.object', {
#             'object': obj
#         })
