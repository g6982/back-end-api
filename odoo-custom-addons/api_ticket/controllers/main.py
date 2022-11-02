from odoo.addons.base_rest.controllers import main 

class PrivateApiController(main.RestController):
   _root_path = '/api/private/helpdesk/'
   _collection_name = "private.helpdesk.service"
#    _default_auth = "api_key"