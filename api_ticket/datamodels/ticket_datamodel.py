from marshmallow import fields
# from datamodel.core import Datamodel
from odoo.addons.datamodel.core import Datamodel # type: ignore

class ticket_input(Datamodel):
   _name = "ticket.input"
   
   subject = fields.String(required=True)
   description = fields.String(required=True)