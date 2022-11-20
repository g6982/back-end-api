from odoo import _, api, fields, models, tools
from odoo import http
import json
import xmlrpc.client
from odoo.http import request, Response
import logging
import os
import math
import random
import smtplib

_logger = logging.getLogger(__name__)


class Controller(http.Controller):
    @http.route('/auth_register', type='json', auth='public', cors='*', method=['POST'])
    def auth_register(self, **kwargs):
        data = json.loads(request.httprequest.data)
        auth_user = request.env['db.access'].sudo().search([('USER_AUTH_CENTER', '=', True)])
        url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
        db = request.env.cr.dbname
        username = auth_user.AUTH_EMAIL
        password = auth_user.USER_AUTH
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        uid = common.authenticate(db, username, password, {})
        if uid:
            existing = request.env['res.partner'].sudo().search([('email', '=', data['email'])])
            if existing:
                response = {
                    'code': 422,
                    'message': 'Email Already Exists'
                }
                return response
            else:
                payload = {
                    'type': 'contact',
                    'phone': data['phone'],
                    'email': data['email'],
                    'name': data['name'],
                    'company_type': 'person'
                }
                new_user = request.env['res.partner'].sudo().create(data)
                # self.send_email(new_user)
                return {
                    'code': 200,
                    'status': "success",
                    'message': "SuccessFuly Created a user"
                }
    #
    # def send_email(self, new_user):
    #     digits = "0123456789"
    #     OTP = "12"
    #     mail_server = request.env['ir.mail_server'].sudo().search([('smtp_host', '=', 'smtp.gmail.com')])
    #     if new_user:
    #         for i in range(4):
    #             OTP += digits[math.floor(random.random() * 10)]
    #             new_user.sudo().write({'otp': OTP})
    #             otpMessage = new_user.otp + 'is your otp'
    #             _logger.error(mail_server.smtp_host)
    #             _logger.error("TESTING THE VALUES!!")
    #             s = smtplib.SMTP(mail_server.smtp_host, 587)
    #             s.starttls()
    #             s.login(mail_server.smtp_user, mail_server.smtp_pass)
    #             s.sendmail('&&&&&&&&&&&', new_user.email, otpMessage)
    #     return {
    #         'code': 200,
    #         'status': 'Success',
    #         'message': 'SUCCESSFULLY CREATED A USER,CHECK YOUR EMAIL FOR AN OTP'
    #     }
