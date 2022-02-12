from odoo import api, fields, models, _
from odoo.osv import expression


class contact_nepal(models.Model):
    _inherit = "res.partner"
    _description = "Nepal Address"
    
    state_id = fields.Many2one('res.country.state', string='State', required=True)
    district_id = fields.Many2one(
        'res.country.district',
        string='District',domain="[('state_id', '=', state_id)]", required=True
        )
    check_municipality = fields.Selection([
        ('municipality', 'Municipality'),
        ('rural_municipality', 'Rural Municipality')],required=True, default='municipality')
   
    municipality = fields.Many2one(
        'res.country.municipality',
        string='Municipality',domain="[('district_id', '=', district_id)]"
        )
    
    rural_municipality=fields.Many2one(
        'res.country.rural_municipality',
        string='Rural Municipality',domain="[('district_id', '=', district_id)]"
    )
    @api.onchange('state_id')
    def _onchange_state(self):
        self.municipality=''
        self.district_id=''
        self.rural_municipality=''

    @api.onchange('district_id')
    def _onchange_district(self):
        self.municipality=''
        self.rural_municipality=''
    

class CountryDistrict(models.Model):
    _description = "Country District"
    _name = 'res.country.district'
    _order = 'code'
    _rec_name="name"

    state_id = fields.Many2one('res.country.state', string='State', required=True)
    name = fields.Char(string='District Name', required=True,
               help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton')
    code = fields.Char(string='State Code', help='The state code.', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(state_id, code)', 'The code of the state must be unique by country !')
    ]

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if self.env.context.get('state_id'):
            args = expression.AND([args, [('state_id', '=', self.env.context.get('state_id'))]])

        if operator == 'ilike' and not (name or '').strip():
            first_domain = []
            domain = []
        else:
            first_domain = [('code', '=ilike', name)]
            domain = [('name', operator, name)]

        first_district_ids = self._search(expression.AND([first_domain, args]), limit=limit, access_rights_uid=name_get_uid) if first_domain else []
        return list(first_district_ids) + [
            district_id
            for district_id in self._search(expression.AND([domain, args]),
                                         limit=limit, access_rights_uid=name_get_uid)
            if district_id not in first_district_ids
        ]
    
        

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}".format(record.name)))
        return result

class CountryMunicipality(models.Model):
    _description = "Country Municipalities"
    _name = 'res.country.municipality'
    _order = 'code'

    district_id = fields.Many2one('res.country.district', string='District', required=True)
    name = fields.Char(string='Municipality', required=True,
               help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton')
    code = fields.Char(string='district Code', help='The district code.', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(district_id, code)', 'The code of the district must be unique by country !')
    ]

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if self.env.context.get('district_id'):
            args = expression.AND([args, [('district_id', '=', self.env.context.get('district_id'))]])

        if operator == 'ilike' and not (name or '').strip():
            first_domain = []
            domain = []
        else:
            first_domain = [('code', '=ilike', name)]
            domain = [('name', operator, name)]

        first_municipality_ids = self._search(expression.AND([first_domain, args]), limit=limit, access_rights_uid=name_get_uid) if first_domain else []
        return list(first_municipality_ids) + [
            municipality_id
            for municipality_id in self._search(expression.AND([domain, args]),
                                         limit=limit, access_rights_uid=name_get_uid)
            if municipality_id not in first_municipality_ids
        ]

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}".format(record.name)))
        return result

class CountryRuralMunicipality(models.Model):
    _description = "Country Municipalities"
    _name = 'res.country.rural_municipality'
    _order = 'code'

    district_id = fields.Many2one('res.country.district', string='District', required=True)
    name = fields.Char(string='Rural Municipality', required=True,
               help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton')
    code = fields.Char(string='district Code', help='The district code.', required=True)

    _sql_constraints = [
        ('name_code_uniq', 'unique(district_id, code)', 'The code of the district must be unique by country !')
    ]

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if self.env.context.get('district_id'):
            args = expression.AND([args, [('district_id', '=', self.env.context.get('district_id'))]])

        if operator == 'ilike' and not (name or '').strip():
            first_domain = []
            domain = []
        else:
            first_domain = [('code', '=ilike', name)]
            domain = [('name', operator, name)]

        first_rural_municipality_ids = self._search(expression.AND([first_domain, args]), limit=limit, access_rights_uid=name_get_uid) if first_domain else []
        return list(first_rural_municipality_ids) + [
            municipality_id
            for municipality_id in self._search(expression.AND([domain, args]),
                                         limit=limit, access_rights_uid=name_get_uid)
            if municipality_id not in first_rural_municipality_ids
        ]

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}".format(record.name)))
        return result
    
    
    