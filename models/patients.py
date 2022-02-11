from odoo import models, fields, api
from datetime import date


class HmsPatients(models.Model):
    _name = 'hms.patients'
    _rec_name = 'First_name'
    state = fields.Selection([
        ('Default', 'Default'),
        ('Undetermined', 'Undetermined'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious'),
],default='Default')
    First_name = fields.Char()
    Last_name = fields.Char()
    Birth_date = fields.Date()
    History = fields.Html()
    CR_ratio = fields.Float()
    Blood_type = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O')
    ])
    PCR = fields.Boolean()
    Image = fields.Image()
    Address = fields.Text()
    Age = fields.Integer()
    departments_id=fields.Many2one('hms.departments')
    doctor_id=fields.Many2many('hms.doctors','doctor_patient')
    Capacity=fields.Integer(related="departments_id.Capacity")
    # is_opened=fields.Boolean(related="departments_id.is_opened")
    @api.onchange('Birth_date')
    def _onchange(self):
        if self.Birth_date:
            self.Age=date.today().year-self.Birth_date.year
            if self.Age <= 30:
                self.PCR = True
                return {
                    'warning': {
                        'title': 'Alert',
                        'message': 'PCR has been check '
                    }

                }
    def Undetermined(self):
        self.state='Undetermined'
    def Good(self):
        self.state='Good'
    def Fair(self):
        self.state='Fair'
    def Serious(self):
        self.state='Serious'
    # @api.onchange('Age')
    # def _onchange(self):
    #     if self.Age <= 30:
    #         self.PCR=True
    #         return {
    #             'warning':{
    #                 'title':'Alert',
    #                 'message':'PCR has been check '
    #             }
    #
    #
    #         }

