from odoo import api, _, models, fields
from odoo.exceptions import UserError, ValidationError
import xmlrpc.client
import json
import logging

_logger = logging.getLogger(__name__)


#  return{
#             'type':'ir.actions.client',
#             'tag':'display_notification',
#             'params':{
#                 'title':'Status Message',
#                 'message':AUTH_USERS.name + ' ' + 'Is The User AUthorized User',
#                 'type':'warning',
#                 'sticky':False
#             }
#         }
class DbAccess(models.Model):
    _name = 'db.access'

    AUTH_RELATION = fields.Many2one('res.users', string='Select User')
    AUTH_EMAIL = fields.Char(string='DB Email', related='AUTH_RELATION.login')
    USER_AUTH = fields.Char(string='DB Password')
    USER_AUTH_CENTER = fields.Binary(string='is Auth', default=True)
    AUTH_PHOTO = fields.Binary(string='avata', related='AUTH_RELATION.image_1920', readonly=True)

    @api.model
    def create(self, values):
        """Override default Odoo create function and extend."""
        record = self.env['db.access'].sudo().search([])
        users = len(record)
        if users == 1:
            raise UserError(_('THERE IS ALREADY A CONNECTED USER!'))
        else:
            return super(DbAccess, self).create(values)

    def test_db_connection(self):
        url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        db = self.env.cr.dbname
        username = self.AUTH_EMAIL
        password = self.USER_AUTH
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        AUTHENTICATE = common.authenticate(db, username, password, {})
        if AUTHENTICATE:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'DB CONNECTION STATUS',
                    'message': 'SUCCESSFULLY CONNECTED TO DB',
                    'type': 'success',
                    'sticky': False
                }}
        else:
            raise UserError(_('WRONG CREDENTIALS TO AUTHENTICATE USER'))


class ResUsers(models.Model):
    _inherit = 'res.partner'

    pssword = fields.Char(string='Password')
    otp = fields.Char(string='The Otp')
