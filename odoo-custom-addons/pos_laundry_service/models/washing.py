# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-Today Geminate Consultancy Services (<http://geminatecs.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models, fields, api, _


class WashingStages(models.Model):
    _name = 'washing.stage'
    _description = 'Washing Stage'
    
    name = fields.Char('Name')
    sequence=fields.Integer('Sequence')
    active = fields.Boolean('Active')
    amount = fields.Float('Amount')
    
#     @api.multi
    def get_washing_values(self):
        return{
                'name' : self.name,
            }
    
    
class PosConfig(models.Model):
    
    _inherit = 'pos.config'
    
    
    washing_stage_ids = fields.Many2many('washing.stage',string="Washing Stages")
    
    
     