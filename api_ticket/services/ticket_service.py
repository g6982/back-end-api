from odoo.addons.base_rest import restapi # type: ignore
from odoo.addons.base_rest_datamodel.restapi import Datamodel # type: ignore
from odoo.addons.component.core import Component # type: ignore


class ticket_service(Component):
    _inherit = "base.rest.service"
    _name = "ticket.service"
    _usage = "ticket"
    _collection = "private.helpdesk.service"
    _description = """Helpdesk Ticket Services"""

    def _res_ticket(self):
        return {
            'code': {'type': 'integer'},
            'status': {'type': 'string'},
            'message': {'type': 'string'},
        }

    @restapi.method(
    [(['/create'], 'POST')],
    input_param=Datamodel('ticket.input'),
    output_param=restapi.CerberusListValidator('_res_ticket'),
    auth='api_key',
    )
    def create(self, body):
        ticket_obj = self.env['helpdesk.ticket']
        res = []
        try:
            ticket_id = ticket_obj.create({
                'name': body.subject,
                'description': body.description
            })
            res = [{
                'code': 200,
                'status': 'success'
            }]
        except Exception as e:
            res = [{
                'code': 404,
                'status': 'Failed',
                'message': str(e)
            }]
        return res