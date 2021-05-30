# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api

class visit(models.Model):
    _name = 'custom_crm2.visit'
    _description = 'visit'

    name = fields.Char(string='Descripción')
    customer = fields.Many2one(string='Cliente', comodel_name="res.partner")
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W','Whatsapp'), ('T','Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen')

    def toggle_state(self):
        self.done = not self.done
#ORM
    def f_create(self):
     #Creando nueva entidad a través de un Json y este se define como un diccionario en python
        visit = {
            'name':'ORM test',
            'customer':'1', # 1 -> ID de BD ya que es una clave externa
            'date': str(datetime.date(2020, 8, 7)), #cast a string de datetime
            'type':'P',
            'done': False #False no "" porque es un valor standard de python
        }
        print(visit) #imprimir en pantalla
        self.env['custom_crm2.visit'].create(visit) #almacenar en BD con el método del ORM CREATE

    def f_search_update(self):
        visit = self.env['custom_crm2.visit'].search([('name', '=', 'ORM test')])
        print('search()',visit, visit.name)

        visit_b = self.env['custom_crm2.visit'].browse([7])
        print('browse()', visit_b, visit_b.name)

        visit.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        visit = self.env['custom_crm2.visit'].browse([7])
        visit.unlink()

#Report
class VisitReport(models.AbstractModel): #ABSMODEL Este modelo podríamos heredarlo en otra clase y contendría todas las operaciones aquí

    _name = 'report.custom_crm2.report_visit_card' #el nombre del arch models

    @api.model
    #Invocar función
    def _get_report_values(self, docids, data=None): #data=none hasta que se inicialice la función
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('custom_crm2.report_visit_card') #Especificar el nombre del formulario
        return {
            'doc_ids': docids,
            'doc_model': self.env['custom_crm2.visit'],
            'docs': self.env['custom_crm2.visit'].browse(docids)
        }

#Clase para heredar sale.order y crear campo zona en presupuestos del CRM
class CustomSalesOrder(models.Model):

    _inherit = 'sale.order'

    zone = fields.Selection([('N', 'Norte'), ('C', 'Centro'), 
                            ('S', 'Sur')], string='Zona comercial')








class CustomAccountMove(models.Model):

    _inherit = 'account.move'
     
    labelNombre = fields.Char(string='Nuevo custom')

















# class custom_crm2(models.Model):
#     _name = 'custom_crm2.custom_crm2'
#     _description = 'custom_crm2.custom_crm2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
